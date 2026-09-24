#!/usr/bin/env python3
"""Validate cases.json against schema/cases.schema.json and the corpus's own
CASES.md / BOUNDARY-CASES.md id lists.

cases.json is the single source of truth. The two Markdown files are generated
from it by scripts/build_cases_md.py; run that script with --check to prove they
have not drifted.

Stdlib only. Checks:
  1. Every case object matches schema/cases.schema.json (hand-rolled checks
     covering the schema's structural constraints -- required keys, types,
     enums, id patterns -- since no third-party jsonschema library is used).
  2. No duplicate ids in cases.json.
  3. Every id that appears as a "#### LC-..." heading in CASES.md or
     BOUNDARY-CASES.md appears in cases.json, and the reverse.
  4. Sourcing rules are tier-specific:
       - verified: at least one source with a non-empty quote.
       - hypothetical: zero sources, and a notes entry stating explicitly
         that no external precedent is claimed.
       - candidate: a notes entry carrying the "Known issue" marker that
         records the source as claimed but not yet verified.
  5. Extra: every quote is 40 words or fewer (the corpus's own sourcing
     rule), reported as a validation error rather than silently ignored.
  6. Every fixture entry names a decision, a family (unless the decision is
     RESEARCH_ONLY), a vector id list and an SDK summary, and carries a url
     only when pending_pr is false.
  7. Taxonomy fields: every case carries exactly one known semantic_family and
     one known domain, a non-empty fixture_family, and an out_of_scope_reason
     if and only if its tier is boundary.
  8. Source prose: source_prose_label is set if and only if source_prose is
     non-empty, a verified or candidate case has source prose, and every url in
     `sources` appears somewhere in that prose.

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
SEMANTIC_FAMILIES = {
    "creation-and-activation",
    "issuer-standing-and-authority-to-change",
    "dependencies-and-subdelegation",
    "succession-and-replacement",
    "collective-and-multi-principal-authority",
    "suspension-restriction-and-release",
    "revocation-expiry-and-exhaustion",
    "external-authority-changing-events",
    "notice-observation-and-reliance",
    "credentials-keys-and-derived-authority",
    "in-flight-actions-and-authorization-boundaries",
    "scheduled-and-dormant-authority",
    "replication-rollback-and-stale-state",
    "identity-target-and-capability-drift",
    "policy-version-and-rule-change",
    "retroactive-findings-and-recharacterization",
    "time-clocks-and-validity-windows",
    "evidence-attribution-and-completeness",
}
DOMAINS = {
    "agency-law", "estates-and-trusts", "corporate", "banking-payments",
    "insolvency", "civil-procedure", "regulatory", "government", "military",
    "aviation", "medicine", "maritime", "industrial-safety", "security-incident",
    "distributed-systems", "cryptography-and-pki", "platform-engineering",
    "naming-and-registry", "agent-native",
}
OUT_OF_SCOPE_REASONS = {
    "security-control",
    "liability-or-legal-consequence",
    "execution-and-scheduler-mechanics",
    "no-verifier-in-the-scenario",
    "implementation-or-configuration-defect",
    "no-authority-transition-in-the-scenario",
}
FIXTURE_DECISIONS = {"VECTOR", "COVERED", "RESEARCH_ONLY"}
REQUIRED_FIXTURE_KEYS = {"decision", "family", "vector_ids", "sdk_results", "pending_pr"}
ALLOWED_FIXTURE_KEYS = REQUIRED_FIXTURE_KEYS | {"url", "note"}
HEADING_ID_RE = re.compile(r"^#{3,4} (LC-[A-Z]-[0-9]{3})\.")


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
    "id", "title", "semantic_family", "domain", "fixture_family", "tier", "status",
    "situation", "source_prose_label", "source_prose", "expected_outcome",
    "naive_failure", "related", "sources", "variants", "fixtures",
}
SOURCE_PROSE_LABELS = {"Human analog.", "Source.", "Source verified.", ""}
ALLOWED_CASE_KEYS = REQUIRED_CASE_KEYS | {"notes", "out_of_scope_reason"}
ALLOWED_TIERS = {"verified", "hypothetical", "candidate", "boundary"}
ALLOWED_STATUS = {"proposed"}
NO_PRECEDENT_MARKER = "no external precedent claimed"
KNOWN_ISSUE_MARKER = "known issue"


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
    for key in ("title", "fixture_family"):
        if not isinstance(case.get(key), str) or not case.get(key, "").strip():
            err(errors, case_id, f"{key} must be a non-empty string")
    if case.get("semantic_family") not in SEMANTIC_FAMILIES:
        err(errors, case_id, f"semantic_family {case.get('semantic_family')!r} is not one of "
                             f"the {len(SEMANTIC_FAMILIES)} families in drafts/TAXONOMY.md")
    if case.get("domain") not in DOMAINS:
        err(errors, case_id, f"domain {case.get('domain')!r} not in {sorted(DOMAINS)}")
    if case.get("tier") not in ALLOWED_TIERS:
        err(errors, case_id, f"tier {case.get('tier')!r} not in {sorted(ALLOWED_TIERS)}")
    reason = case.get("out_of_scope_reason")
    if case.get("tier") == "boundary":
        if reason is None:
            err(errors, case_id, "tier is boundary but no out_of_scope_reason is given")
        elif reason not in OUT_OF_SCOPE_REASONS:
            err(errors, case_id, f"out_of_scope_reason {reason!r} not in "
                                 f"{sorted(OUT_OF_SCOPE_REASONS)}")
    elif reason is not None:
        err(errors, case_id, f"tier is {case.get('tier')!r} but an out_of_scope_reason "
                             f"({reason!r}) is set; only boundary cases carry one")
    if case.get("status") not in ALLOWED_STATUS:
        err(errors, case_id, f"status {case.get('status')!r} not in {sorted(ALLOWED_STATUS)}")
    for key in ("situation", "expected_outcome", "naive_failure", "source_prose"):
        if not isinstance(case.get(key, ""), str):
            err(errors, case_id, f"{key} must be a string")

    label = case.get("source_prose_label")
    prose = case.get("source_prose") or ""
    if label not in SOURCE_PROSE_LABELS:
        err(errors, case_id, f"source_prose_label {label!r} not in "
                             f"{sorted(SOURCE_PROSE_LABELS)}")
    elif bool(label) != bool(prose.strip()):
        err(errors, case_id, "source_prose_label and source_prose must both be set "
                             f"or both be empty (label {label!r}, prose "
                             f"{'non-empty' if prose.strip() else 'empty'})")
    if case.get("tier") in ("verified", "candidate") and not prose.strip():
        err(errors, case_id, f"tier is {case.get('tier')!r} but the case carries no "
                             "source prose")
    for i, src in enumerate(case.get("sources") or []):
        if isinstance(src, dict) and src.get("url") and src["url"] not in prose:
            err(errors, case_id, f"sources[{i}] url is not cited in source_prose: "
                                 f"{src['url']}")

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
        if case.get("tier") in ("verified", "hypothetical", "candidate") and not fixtures:
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
        if not isinstance(case, dict):
            continue
        cid = case.get("id")
        tier = case.get("tier")
        sources = case.get("sources") or []
        notes = case.get("notes") or []
        notes_text = " ".join(n for n in notes if isinstance(n, str)).lower()

        if tier == "verified":
            has_quote = any(isinstance(s, dict) and (s.get("quote") or "").strip() for s in sources)
            if not has_quote:
                unsourced_verified.append(cid)
                errors.append(f"{cid}: tier is verified but has no source with a quote")
        elif tier == "hypothetical":
            if sources:
                errors.append(f"{cid}: tier is hypothetical but carries {len(sources)} source(s), expected none")
            if NO_PRECEDENT_MARKER not in notes_text:
                errors.append(f"{cid}: tier is hypothetical but notes carry no explicit "
                               f"no-external-precedent statement")
        elif tier == "candidate":
            if KNOWN_ISSUE_MARKER not in notes_text:
                errors.append(f"{cid}: tier is candidate but notes carry no 'Known issue' marker "
                               f"for the claimed-but-unverified source")

    print(f"cases.json: {len(cases)} entries, {len(json_ids)} unique ids")
    print(f"CASES.md ids: {len(md_case_ids)}, BOUNDARY-CASES.md ids: {len(md_boundary_ids)}")
    with_prose = sum(1 for c in cases if isinstance(c, dict) and (c.get("source_prose") or "").strip())
    print(f"cases carrying source prose: {with_prose} of {len(cases)}")
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
    semantic_counts = {}
    domain_counts = {}
    reason_counts = {}
    for case in cases:
        if not isinstance(case, dict):
            continue
        semantic_counts[case.get("semantic_family")] = \
            semantic_counts.get(case.get("semantic_family"), 0) + 1
        domain_counts[case.get("domain")] = domain_counts.get(case.get("domain"), 0) + 1
        if case.get("tier") == "boundary":
            reason_counts[case.get("out_of_scope_reason")] = \
                reason_counts.get(case.get("out_of_scope_reason"), 0) + 1
    print(f"semantic families in use: {len(semantic_counts)} of {len(SEMANTIC_FAMILIES)}, "
          f"domains in use: {len(domain_counts)} of {len(DOMAINS)}")
    print("semantic families: " + ", ".join(
        f"{k} {v}" for k, v in sorted(semantic_counts.items(), key=lambda kv: (-kv[1], str(kv[0])))))
    print("boundary reasons: " + ", ".join(
        f"{k} {v}" for k, v in sorted(reason_counts.items(), key=lambda kv: (-kv[1], str(kv[0])))))
    tier_counts = {}
    for case in cases:
        if isinstance(case, dict):
            tier_counts[case.get("tier")] = tier_counts.get(case.get("tier"), 0) + 1
    print("tier counts: " + ", ".join(f"{k} {v}" for k, v in sorted(tier_counts.items(), key=lambda kv: str(kv[0]))))
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
    print("Note: this checks cases.json. Run 'python3 scripts/build_cases_md.py "
          "--check' to prove CASES.md and BOUNDARY-CASES.md still match it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
