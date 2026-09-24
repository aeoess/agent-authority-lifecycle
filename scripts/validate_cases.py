#!/usr/bin/env python3
"""Validate cases.json against schema/cases.schema.json and the corpus's own
CASES.md / BOUNDARY-CASES.md id lists.

Stdlib only. Checks:
  1. Every case object matches schema/cases.schema.json (hand-rolled checks
     covering the schema's structural constraints -- required keys, types,
     enums, id patterns -- since no third-party jsonschema library is used).
  2. No duplicate ids in cases.json.
  3. Every id that appears as a "#### LC-..." heading in CASES.md or
     BOUNDARY-CASES.md appears in cases.json, and the reverse.
  4. Every case with tier "verified" carries at least one source with a
     non-empty quote.
  5. Extra: every quote is 40 words or fewer (the corpus's own sourcing
     rule), reported as a validation error rather than silently ignored.
  6. Every fixture entry names a decision, a family (unless the decision is
     RESEARCH_ONLY), a vector id list and an SDK summary, and carries a url
     only when pending_pr is false.

Exit code 0 if every check passes, 1 otherwise. Prints a report either way.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CASE_ID_RE = re.compile(r"^LC-[A-Z]-[0-9]{3}$")
INVARIANT_ID_RE = re.compile(r"^L([1-9]|1[0-2])$")
OPEN_QUESTION_SLUGS = {
    "teardown-completeness",
    "work-in-flight",
    "release-from-suspension",
    "critical-revocation",
    "office-vacancy-and-succession",
    "grants-signed-just-before-departure",
    "authority-rollback",
    "semantic-drift",
    "notice-and-relying-parties",
}
FETCHED_BY_VALUES = {"auditor", "thin-group ledger"}
FIXTURE_DECISIONS = {"VECTOR", "COVERED", "RESEARCH_ONLY"}
REQUIRED_FIXTURE_KEYS = {"decision", "family", "vector_ids", "sdk_results", "pending_pr"}
ALLOWED_FIXTURE_KEYS = REQUIRED_FIXTURE_KEYS | {"url", "note"}
HEADING_ID_RE = re.compile(r"^#### (LC-[A-Z]-[0-9]{3})\.")


def md_ids(path):
    ids = set()
    for line in path.read_text().splitlines():
        m = HEADING_ID_RE.match(line)
        if m:
            ids.add(m.group(1))
    return ids


def err(errors, case_id, msg):
    errors.append(f"{case_id or '(no id)'}: {msg}")


def check_source(src, case_id, idx, errors):
    if not isinstance(src, dict):
        err(errors, case_id, f"sources[{idx}] is not an object")
        return
    for key in ("url", "quote", "fetched_by"):
        if key not in src:
            err(errors, case_id, f"sources[{idx}] missing '{key}'")
    extra = set(src.keys()) - {"url", "quote", "fetched_by"}
    if extra:
        err(errors, case_id, f"sources[{idx}] has unexpected keys {sorted(extra)}")
    url = src.get("url", "")
    if not isinstance(url, str) or not re.match(r"^https?://", url):
        err(errors, case_id, f"sources[{idx}] url is not http(s): {url!r}")
    quote = src.get("quote", "")
    if not isinstance(quote, str) or not quote.strip():
        err(errors, case_id, f"sources[{idx}] quote is empty")
    else:
        wc = len(quote.split())
        if wc > 40:
            err(errors, case_id, f"sources[{idx}] quote is {wc} words, over the 40-word limit")
    fb = src.get("fetched_by")
    if fb not in FETCHED_BY_VALUES:
        err(errors, case_id, f"sources[{idx}] fetched_by {fb!r} not in {sorted(FETCHED_BY_VALUES)}")


def check_fixture(f, case_id, idx, errors):
    if not isinstance(f, dict):
        err(errors, case_id, f"fixtures[{idx}] is not an object")
        return
    for key in sorted(REQUIRED_FIXTURE_KEYS - set(f.keys())):
        err(errors, case_id, f"fixtures[{idx}] missing '{key}'")
    extra = set(f.keys()) - ALLOWED_FIXTURE_KEYS
    if extra:
        err(errors, case_id, f"fixtures[{idx}] has unexpected keys {sorted(extra)}")

    decision = f.get("decision")
    if decision not in FIXTURE_DECISIONS:
        err(errors, case_id, f"fixtures[{idx}] decision {decision!r} not in {sorted(FIXTURE_DECISIONS)}")

    family = f.get("family")
    if family is None:
        if decision != "RESEARCH_ONLY":
            err(errors, case_id, f"fixtures[{idx}] family is null but decision is {decision!r}")
    elif not isinstance(family, str) or not family.strip():
        err(errors, case_id, f"fixtures[{idx}] family must be a non-empty string or null")

    vector_ids = f.get("vector_ids")
    if not isinstance(vector_ids, list):
        err(errors, case_id, f"fixtures[{idx}] vector_ids must be an array")
    else:
        for j, vid in enumerate(vector_ids):
            if not isinstance(vid, str) or not vid.strip():
                err(errors, case_id, f"fixtures[{idx}] vector_ids[{j}] is not a non-empty string")
        if len(set(vector_ids)) != len(vector_ids):
            err(errors, case_id, f"fixtures[{idx}] vector_ids has duplicates")
        if decision == "VECTOR" and not vector_ids:
            err(errors, case_id, f"fixtures[{idx}] decision is VECTOR but no vector id is listed")

    if not isinstance(f.get("sdk_results", ""), str) or not (f.get("sdk_results") or "").strip():
        err(errors, case_id, f"fixtures[{idx}] sdk_results must be a non-empty string")

    pending = f.get("pending_pr")
    if not isinstance(pending, bool):
        err(errors, case_id, f"fixtures[{idx}] pending_pr must be a boolean")
    url = f.get("url")
    if url is not None:
        if pending is True:
            err(errors, case_id, f"fixtures[{idx}] carries a url while pending_pr is true")
        if not isinstance(url, str) or not re.match(r"^https?://", url):
            err(errors, case_id, f"fixtures[{idx}] url is not http(s): {url!r}")


def check_variant(v, case_id, idx, errors):
    if not isinstance(v, dict):
        err(errors, case_id, f"variants[{idx}] is not an object")
        return
    for key in ("id", "difference"):
        if key not in v:
            err(errors, case_id, f"variants[{idx}] missing '{key}'")
    vid = v.get("id", "")
    if not isinstance(vid, str) or not CASE_ID_RE.match(vid):
        err(errors, case_id, f"variants[{idx}] id {vid!r} does not match LC-<letter>-<3 digits>")
    diff = v.get("difference", "")
    if not isinstance(diff, str) or not diff.strip():
        err(errors, case_id, f"variants[{idx}] difference is empty")


def check_related(rel, case_id, errors):
    if not isinstance(rel, dict):
        err(errors, case_id, "related is not an object")
        return
    for key in ("invariants", "open_questions", "concepts", "text"):
        if key not in rel:
            err(errors, case_id, f"related missing '{key}'")
    for inv in rel.get("invariants", []) or []:
        if not isinstance(inv, str) or not INVARIANT_ID_RE.match(inv):
            err(errors, case_id, f"related.invariants has invalid id {inv!r}")
    for oq in rel.get("open_questions", []) or []:
        if oq not in OPEN_QUESTION_SLUGS:
            err(errors, case_id, f"related.open_questions has unknown slug {oq!r}")
    if not isinstance(rel.get("text", ""), str):
        err(errors, case_id, "related.text is not a string")


REQUIRED_CASE_KEYS = {
    "id", "title", "family", "tier", "status",
    "situation", "expected_outcome", "naive_failure",
    "related", "sources", "variants", "fixtures",
}
ALLOWED_CASE_KEYS = REQUIRED_CASE_KEYS | {"notes"}
ALLOWED_TIERS = {"verified", "candidate", "boundary"}
ALLOWED_STATUS = {"proposed"}


def check_case(case, errors):
    if not isinstance(case, dict):
        errors.append("top-level entry is not an object")
        return None
    case_id = case.get("id")
    missing = REQUIRED_CASE_KEYS - set(case.keys())
    if missing:
        err(errors, case_id, f"missing required keys {sorted(missing)}")
    extra = set(case.keys()) - ALLOWED_CASE_KEYS
    if extra:
        err(errors, case_id, f"unexpected keys {sorted(extra)}")

    if not isinstance(case_id, str) or not CASE_ID_RE.match(case_id):
        err(errors, case_id, f"id {case_id!r} does not match ^LC-[A-Z]-[0-9]{{3}}$")
    for key in ("title", "family"):
        if not isinstance(case.get(key), str) or not case.get(key, "").strip():
            err(errors, case_id, f"{key} must be a non-empty string")
    if case.get("tier") not in ALLOWED_TIERS:
        err(errors, case_id, f"tier {case.get('tier')!r} not in {sorted(ALLOWED_TIERS)}")
    if case.get("status") not in ALLOWED_STATUS:
        err(errors, case_id, f"status {case.get('status')!r} not in {sorted(ALLOWED_STATUS)}")
    for key in ("situation", "expected_outcome", "naive_failure"):
        if not isinstance(case.get(key, ""), str):
            err(errors, case_id, f"{key} must be a string")

    check_related(case.get("related", {}), case_id, errors)

    sources = case.get("sources")
    if not isinstance(sources, list):
        err(errors, case_id, "sources must be an array")
    else:
        for i, s in enumerate(sources):
            check_source(s, case_id, i, errors)

    variants = case.get("variants")
    if not isinstance(variants, list):
        err(errors, case_id, "variants must be an array")
    else:
        for i, v in enumerate(variants):
            check_variant(v, case_id, i, errors)

    fixtures = case.get("fixtures")
    if not isinstance(fixtures, list):
        err(errors, case_id, "fixtures must be an array")
    else:
        for i, f in enumerate(fixtures):
            check_fixture(f, case_id, i, errors)
        if case.get("tier") == "boundary" and fixtures:
            err(errors, case_id, "boundary cases carry no fixture entries, found "
                                 f"{len(fixtures)}")
        if case.get("tier") in ("verified", "candidate") and not fixtures:
            err(errors, case_id, "case is in CASES.md but carries no fixture entry")

    if "notes" in case and not isinstance(case["notes"], list):
        err(errors, case_id, "notes must be an array of strings")

    return case_id


def main():
    errors = []

    cases_path = ROOT / "cases.json"
    cases = json.loads(cases_path.read_text())
    if not isinstance(cases, list):
        print("FATAL: cases.json is not a JSON array")
        return 1

    seen_ids = []
    for case in cases:
        cid = check_case(case, errors)
        if cid:
            seen_ids.append(cid)

    dupes = sorted({cid for cid in seen_ids if seen_ids.count(cid) > 1})
    for d in dupes:
        errors.append(f"{d}: duplicate id in cases.json")

    md_case_ids = md_ids(ROOT / "CASES.md")
    md_boundary_ids = md_ids(ROOT / "BOUNDARY-CASES.md")
    all_md_ids = md_case_ids | md_boundary_ids
    json_ids = set(seen_ids)

    missing_from_json = sorted(all_md_ids - json_ids)
    missing_from_md = sorted(json_ids - all_md_ids)
    for m in missing_from_json:
        errors.append(f"{m}: appears as a heading in CASES.md/BOUNDARY-CASES.md but not in cases.json")
    for m in missing_from_md:
        errors.append(f"{m}: appears in cases.json but not as a heading in CASES.md/BOUNDARY-CASES.md")

    unsourced_verified = []
    for case in cases:
        if isinstance(case, dict) and case.get("tier") == "verified":
            sources = case.get("sources") or []
            has_quote = any(isinstance(s, dict) and (s.get("quote") or "").strip() for s in sources)
            if not has_quote:
                unsourced_verified.append(case.get("id"))
    for cid in unsourced_verified:
        errors.append(f"{cid}: tier is verified but has no source with a quote")

    print(f"cases.json: {len(cases)} entries, {len(json_ids)} unique ids")
    print(f"CASES.md ids: {len(md_case_ids)}, BOUNDARY-CASES.md ids: {len(md_boundary_ids)}")
    print(f"id set match (md union vs json): {'OK' if not missing_from_json and not missing_from_md else 'MISMATCH'}")
    print(f"duplicate ids: {len(dupes)}")
    fixture_entries = 0
    vector_refs = 0
    decisions = {"VECTOR": 0, "COVERED": 0, "RESEARCH_ONLY": 0}
    families = set()
    for case in cases:
        if not isinstance(case, dict):
            continue
        for f in case.get("fixtures") or []:
            if not isinstance(f, dict):
                continue
            fixture_entries += 1
            vector_refs += len(f.get("vector_ids") or [])
            if f.get("decision") in decisions:
                decisions[f["decision"]] += 1
            if f.get("family"):
                families.add(f["family"])

    print(f"fixture entries: {fixture_entries} across {len(families)} families, "
          f"{vector_refs} vector id references")
    print("fixture decisions: " + ", ".join(f"{k} {v}" for k, v in sorted(decisions.items())))
    print(f"verified cases without a sourced quote: {len(unsourced_verified)}")
    if unsourced_verified:
        print("  " + ", ".join(unsourced_verified))
    print()

    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for e in errors:
            print(" -", e)
        return 1

    print("PASSED: all checks clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
