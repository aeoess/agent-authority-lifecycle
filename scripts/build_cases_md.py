#!/usr/bin/env python3
"""Generate CASES.md and BOUNDARY-CASES.md from cases.json.

cases.json is the single source of truth for case content. This script renders
it into the two Markdown views: CASES.md grouped by semantic_family, and
BOUNDARY-CASES.md grouped by out_of_scope_reason.

Stdlib only. Output is deterministic: families and boundary reasons are ordered
by slug, cases inside a family by (tier, id), and nothing depends on dict
ordering, locale or the clock.

  python3 scripts/build_cases_md.py           write both files
  python3 scripts/build_cases_md.py --check    regenerate in memory and exit 1
                                               if either file on disk differs
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "0.3.0-draft"
GENERATED_BY = ("Generated from cases.json by scripts/build_cases_md.py. "
                "Do not edit case data here.")

# Vector id lists this long or longer are rendered as a first-to-last range.
VECTOR_RANGE_THRESHOLD = 9

# Slug -> (heading, the question a reader arrives with). Both come from the
# v0.3 taxonomy pass; the slugs are the enum in schema/cases.schema.json.
FAMILIES = {
    "collective-and-multi-principal-authority": (
        "Collective and multi-principal authority",
        "More than one principal is involved. Who has to agree, and whose "
        "instruction wins?"),
    "creation-and-activation": (
        "Creation and activation",
        "Is this authority in force yet, and does this newly created party hold any?"),
    "credentials-keys-and-derived-authority": (
        "Credentials, keys and derived authority",
        "What does this credential, key or session actually prove, separately "
        "from the grant behind it?"),
    "dependencies-and-subdelegation": (
        "Dependencies and subdelegation",
        "What does this grant currently depend on, and what may it issue below itself?"),
    "evidence-attribution-and-completeness": (
        "Evidence, attribution and completeness",
        "What do the records establish, whom do they attribute an action to, "
        "and what set do they cover?"),
    "external-authority-changing-events": (
        "External authority-changing events",
        "Something happened outside the delegation graph. What did it do to "
        "authority, and when?"),
    "identity-target-and-capability-drift": (
        "Identity, target and capability drift",
        "The name stayed the same while the identity, target or capability "
        "behind it changed."),
    "in-flight-actions-and-authorization-boundaries": (
        "In-flight actions and authorization boundaries",
        "Authority changed between authorization and outcome. What governs at "
        "the next authorization boundary?"),
    "issuer-standing-and-authority-to-change": (
        "Issuer standing and authority to change",
        "Who was entitled to issue, suspend, revoke or replace this, and did "
        "they have standing?"),
    "notice-observation-and-reliance": (
        "Notice, observation and reliance",
        "Who learned of a transition, when, with what freshness, and what may "
        "a party relying on the old view still do?"),
    "policy-version-and-rule-change": (
        "Policy version and rule change",
        "Which version of the rules governs this grant or this past decision?"),
    "replication-rollback-and-stale-state": (
        "Replication, rollback and stale state",
        "Which copy of authority state is the current one, and what does a "
        "restore or a lagging replica bring back?"),
    "retroactive-findings-and-recharacterization": (
        "Retroactive findings and recharacterization",
        "Something established later changes the verdict on a past act. What "
        "does that do to the earlier record?"),
    "revocation-expiry-and-exhaustion": (
        "Revocation, expiry and exhaustion",
        "Authority ended. Which kind of ending was it, and what does it reach?"),
    "scheduled-and-dormant-authority": (
        "Scheduled and dormant authority",
        "Authority that fires later or sits unused. Whose authority is it when it fires?"),
    "succession-and-replacement": (
        "Succession and replacement",
        "The holder is gone, leaving or contested. Who holds this now, and on what terms?"),
    "suspension-restriction-and-release": (
        "Suspension, restriction and release",
        "Authority is paused or narrowed rather than ended. What state is that, "
        "and what lifts it?"),
    "time-clocks-and-validity-windows": (
        "Time, clocks and validity windows",
        "Whose clock and which timestamp decide whether this is currently in force?"),
}

BOUNDARY_REASONS = {
    "execution-and-scheduler-mechanics": (
        "Execution and scheduler mechanics",
        "Delivery, retry, lateness and overlap are execution behaviour. No "
        "authority transition happens in the scenario."),
    "implementation-or-configuration-defect": (
        "Implementation or configuration defect",
        "The model already fixes the required behaviour. What is in question is "
        "whether a running system does what it declares, which is conformance "
        "testing and configuration monitoring."),
    "liability-or-legal-consequence": (
        "Liability or legal consequence",
        "The case ends in who is answerable rather than in an authority verdict. "
        "The underlying validity is untouched either way."),
    "no-authority-transition-in-the-scenario": (
        "No authority transition in the scenario",
        "A verifier is present and returns the right answer, and nothing about "
        "authority changed. What moves is dependent operational state or live "
        "context."),
    "no-verifier-in-the-scenario": (
        "No verifier in the scenario",
        "There is nobody to check the claim against, or the chain is correctly "
        "revoked and only a rendered view is stale, so no verification decision "
        "is wrong."),
    "security-control": (
        "Security control",
        "The case resolves into a control, detection or incident-governance "
        "question. The grant is valid throughout, or the case turns on whether a "
        "compromise would have been noticed, which no verifier decides from "
        "records."),
}

TIER_ORDER = {"verified": 0, "hypothetical": 1, "candidate": 2}
TIER_LABEL = {"verified": "verified", "hypothetical": "reviewed hypothetical",
              "candidate": "candidate", "boundary": "boundary"}


def slugify(text):
    """GitHub-flavoured heading anchor for a Markdown heading."""
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s.strip())


def case_anchor(case):
    return slugify(f"{case['id']}. {case['title']}")


def status_line(case):
    notes = case.get("notes") or []
    stated = [n for n in notes if n.startswith("source status line: ")]
    if not stated:
        raise SystemExit(f"{case['id']}: notes carry no 'source status line:' entry")
    line = stated[0].split(": ", 1)[1] + "."
    if "source_type: law" in notes:
        line += " (source_type: law)"
    return line


def fixture_line(case):
    """The **Fixture:** line, or '' for a case the lab wave built nothing for."""
    parts = []
    for f in case["fixtures"]:
        if not f.get("family"):
            continue
        vectors = f["vector_ids"]
        if len(vectors) >= VECTOR_RANGE_THRESHOLD:
            shown = f"`{vectors[0]}` to `{vectors[-1]}` ({len(vectors)})"
        elif vectors:
            shown = ", ".join(f"`{v}`" for v in vectors)
        else:
            shown = "no vector ids named in the coverage table"
        where = ("candidate, not yet merged" if f["pending_pr"]
                 else f"merged_candidate, {f['url']}")
        parts.append(f"`{f['family']}` / {shown} ({where})")
    # A period, not a semicolon, separates families on one Fixture line.
    return ". ".join(parts)


def variants_line(case):
    if not case["variants"]:
        return ""
    items = ", ".join(f"{v['id']} ({v['difference']})" for v in case["variants"])
    return f"Variants: {items}."


def fixture_families(case):
    names = []
    for f in case["fixtures"]:
        if f.get("family") and f["family"] not in names:
            names.append(f["family"])
    return names


def render_case(case):
    """One case entry, from its heading to the closing rule."""
    out = [f"### {case['id']}. {case['title']}", ""]
    related = case["related"]["text"]
    # The short reason-plus-source form: the survivor pass wrote one paragraph
    # that is both the situation and the reason, and stated no outcome.
    short_form = (related == case["situation"]
                  and not case["expected_outcome"]
                  and not case["naive_failure"])

    if short_form:
        out += [f"**Reason.** {case['situation']}", ""]
    else:
        out += [f"**Situation.** {case['situation']}", ""]

    if case["source_prose"]:
        out += [f"**{case['source_prose_label']}** {case['source_prose']}", ""]

    if not short_form:
        if case["expected_outcome"]:
            out += [f"**What should happen.** {case['expected_outcome']}", ""]
        if case["naive_failure"]:
            out += [f"**What a naive system gets wrong.** {case['naive_failure']}", ""]
        if related:
            label = ("Boundary reason." if case["tier"] == "boundary"
                     else "Related invariant/open question.")
            out += [f"**{label}** {related}", ""]

    for note in case.get("notes") or []:
        if note.startswith("Known issue: "):
            out += [f"**Known issue.** {note[len('Known issue: '):]}", ""]

    out += [f"**Status:** {status_line(case)}", ""]

    fixtures = fixture_line(case)
    if fixtures:
        out += [f"**Fixture:** {fixtures}", ""]

    variants = variants_line(case)
    if variants:
        out += [variants, ""]

    out += ["---", ""]
    return out


def index_table(cases, columns):
    rows = ["| " + " | ".join(h for h, _ in columns) + " |",
            "|" + "|".join("---" for _ in columns) + "|"]
    for c in cases:
        rows.append("| " + " | ".join(fn(c) for _, fn in columns) + " |")
    return rows


def build_cases_md(cases):
    live = [c for c in cases if c["tier"] != "boundary"]
    live.sort(key=lambda c: (c["semantic_family"], TIER_ORDER[c["tier"]], c["id"]))

    counts = {t: sum(1 for c in live if c["tier"] == t) for t in TIER_ORDER}
    no_fixture = sorted(c["id"] for c in live if not fixture_line(c))
    with_fixture = len(live) - len(no_fixture)

    if len(no_fixture) == 1:
        missing = (f"One case, {no_fixture[0]}, has no fixture because no record "
                   f"set decides it.")
    elif no_fixture:
        missing = (f"{len(no_fixture)} cases ({', '.join(no_fixture)}) have no "
                   f"fixture because no record set decides them.")
    else:
        missing = "Every case carries a fixture line."

    L = [
        "# Authority Lifecycle: Cases",
        "",
        GENERATED_BY,
        "",
        f"Part of Authority Lifecycle v{VERSION}. From the Agent Passport System "
        f"work. Apache-2.0.",
        "",
        "These are situations where the people, keys, approvals, offices, resources "
        "or infrastructure around an agent change, and the question is what happens "
        "to its authority. They test the concepts and invariants in "
        "[AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md) and the gaps in "
        "[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).",
        "",
        "Many cases rest on a human, institutional or systems precedent: a statute, "
        "a court or agency finding, a standard or a documented incident. None of "
        "those sources says anything about AI agents. The translation into agent "
        "terms is ours, and the precedent is a source of cases, not a claim that "
        "the law applies to AI agents.",
        "",
        "There are three tiers.",
        "",
        "- **Verified.** We fetched the cited source and checked that it supports "
        "the stated precedent. The expected outcome is still **proposed**. A "
        "fixture existing for a case does not change that: the vectors are "
        "candidates against proposed text, not conformance results.",
        "- **Reviewed hypothetical.** The case survived the same review pass as a "
        "verified case, but it claims no external precedent: no statute, court or "
        "agency finding, standard or documented incident supports it. The source "
        "line says so, in place of a citation.",
        "- **Candidate.** Produced by a research pass and not yet checked. The "
        "source is claimed, not verified. A \"Known issue\" note marks a problem "
        "already found. Candidates are verified, corrected, merged into another "
        "case or removed as review continues. Do not cite a candidate's source "
        "without checking it.",
        "",
        f"Current count: {counts['verified']} verified, {counts['hypothetical']} "
        f"reviewed hypothetical, {counts['candidate']} candidate. No case is a "
        f"conformance result. {with_fixture} of the {len(live)} carry a **Fixture** "
        f"line naming the fixture family and vector ids that now exist for them in "
        f"the [Agent Authority Conformance]"
        f"(https://github.com/Agent-Authority-Conformance/aps-conformance-suite) "
        f"suite. Most of those are now merged_candidate, pinned to the lab main "
        f"commit the line links, still candidates against proposed text rather than "
        f"conformance results. The `lifecycle-purpose-exhaustion` family is held "
        f"back and stays on an unmerged candidate branch, which the line says. "
        f"{missing} The same mapping in machine-readable form is the `fixtures` "
        f"array in [cases.json](cases.json).",
        "",
        "What changed since v0.1. Every v0.1 candidate was read against its source "
        "by a survivor pass and then re-checked by an independent auditor who "
        "fetched each source again. Candidates that survived both became verified, "
        "duplicates were folded into a representative and listed under it as named "
        "variants, cases that resolve to a security or evidence question rather "
        "than an authority verdict moved to "
        "[BOUNDARY-CASES.md](BOUNDARY-CASES.md), and the rest were removed. "
        "Thirteen families the corpus covered thinly or not at all were researched "
        "from scratch in the same pass. IDs are stable: an ID that appears in v0.1 "
        "means the same case here.",
        "",
        "Cases are grouped by the authority question they ask, not by the research "
        "domain they came from. Each case carries exactly one semantic family. The "
        "source domain survives as the Domain column in the index below and as the "
        "`domain` field in [cases.json](cases.json), and the pre-v0.3 grouping "
        "survives there as `fixture_family`. Same family does not mean duplicate: a "
        "representative case lists its folded duplicates on a \"Variants\" line, "
        "with the one-line difference that made each a duplicate rather than a "
        "separate case.",
        "",
        "## Contents",
        "",
    ]

    for slug in sorted(FAMILIES):
        members = [c for c in live if c["semantic_family"] == slug]
        heading = FAMILIES[slug][0]
        L.append(f"- [{heading}](#{slugify(heading)}) ({len(members)})")

    # Tier is not a section any more, so say where a reader finds it.
    hyp = [c for c in live if c["tier"] == "hypothetical"]
    cand = [c for c in live if c["tier"] == "candidate"]
    L += ["", "Tier is a column in the index below and a line on each case, not a "
          "section of its own. " + tier_pointer("reviewed hypothetical", hyp) + " "
          + tier_pointer("candidate", cand) + " Everything else is verified."]

    L += ["", f"<details>", f"<summary>All {len(live)} cases</summary>", ""]
    L += index_table(live, [
        ("ID", lambda c: f"[{c['id']}](#{case_anchor(c)})"),
        ("Case", lambda c: c["title"]),
        ("Semantic family", lambda c: (f"[{FAMILIES[c['semantic_family']][0]}]"
                                       f"(#{slugify(FAMILIES[c['semantic_family']][0])})")),
        ("Domain", lambda c: c["domain"]),
        ("Tier", lambda c: TIER_LABEL[c["tier"]]),
        ("Fixture", lambda c: ", ".join(f"`{f}`" for f in fixture_families(c)) or "none"),
    ])
    L += ["", "</details>", ""]

    for slug in sorted(FAMILIES):
        members = [c for c in live if c["semantic_family"] == slug]
        heading, question = FAMILIES[slug]
        L += [f"## {heading}", "", question, ""]
        for c in members:
            L += render_case(c)

    return "\n".join(L).rstrip("\n") + "\n"


def tier_pointer(label, cases):
    """One sentence naming the cases at a tier, linked, for the Contents block."""
    if not cases:
        return f"No case is {label}."
    links = [f"[{c['id']}](#{case_anchor(c)})"
             for c in sorted(cases, key=lambda c: c["id"])]
    if len(links) == 1:
        return f"The one {label} case is {links[0]}."
    listed = ", ".join(links[:-1]) + " and " + links[-1]
    return f"The {len(links)} {label} cases are {listed}."


def build_boundary_md(cases):
    boundary = [c for c in cases if c["tier"] == "boundary"]
    boundary.sort(key=lambda c: (c["out_of_scope_reason"], c["id"]))

    L = [
        "# Authority Lifecycle: Boundary Cases",
        "",
        GENERATED_BY,
        "",
        f"Part of Authority Lifecycle v{VERSION}. From the Agent Passport System "
        f"work. Apache-2.0.",
        "",
        f"These are the {len(boundary)} security and evidence cases that sit next to "
        f"authority lifecycle without being lifecycle cases. Each one came out of the "
        f"same research and audit pass as [CASES.md](CASES.md), and each one is sound. "
        f"What each lacks is a lifecycle verdict: it resolves to a liability outcome, "
        f"a detection-surface gap, an operational practice or an evidence question, "
        f"not to an authority state a verifier returns from records (valid, invalid, "
        f"not established, suspended, restricted, not yet effective).",
        "",
        "They are kept because they bound the model. They mark where the "
        "authority-lifecycle question stops and a different question starts, and a "
        "design that answers them by extending the lifecycle model is probably "
        "answering the wrong question.",
        "",
        "Entry format matches CASES.md. Some entries are in the shorter "
        "reason-plus-source form the survivor pass used for them, rather than the "
        "full situation-and-outcome form. IDs are stable and match the ones used in "
        "CASES.md and in the research record. Status is **proposed** unless the entry "
        "says otherwise. None of the sources says anything about AI agents.",
        "",
        "Cases are grouped by why each one is out of scope. Each also carries a "
        "semantic family, shown in the index below, which records the nearest "
        "authority question rather than a claim that the case resolves to an "
        "authority verdict.",
        "",
        "## Contents",
        "",
    ]

    for slug in sorted(BOUNDARY_REASONS):
        members = [c for c in boundary if c["out_of_scope_reason"] == slug]
        heading = BOUNDARY_REASONS[slug][0]
        L.append(f"- [{heading}](#{slugify(heading)}) ({len(members)})")

    L += ["", "<details>", f"<summary>All {len(boundary)} boundary cases</summary>", ""]
    L += index_table(boundary, [
        ("ID", lambda c: f"[{c['id']}](#{case_anchor(c)})"),
        ("Case", lambda c: c["title"]),
        ("Out of scope because", lambda c: (
            f"[{BOUNDARY_REASONS[c['out_of_scope_reason']][0]}]"
            f"(#{slugify(BOUNDARY_REASONS[c['out_of_scope_reason']][0])})")),
        ("Semantic family", lambda c: FAMILIES[c["semantic_family"]][0]),
        ("Domain", lambda c: c["domain"]),
        ("Tier", lambda c: TIER_LABEL[c["tier"]]),
    ])
    L += ["", "</details>", ""]

    for slug in sorted(BOUNDARY_REASONS):
        members = [c for c in boundary if c["out_of_scope_reason"] == slug]
        heading, why = BOUNDARY_REASONS[slug]
        L += [f"## {heading}", "", why, ""]
        for c in members:
            L += render_case(c)

    return "\n".join(L).rstrip("\n") + "\n"


def main(argv):
    check = "--check" in argv[1:]
    unknown = [a for a in argv[1:] if a != "--check"]
    if unknown:
        print(f"unknown argument(s): {' '.join(unknown)}")
        return 2

    cases = json.loads((ROOT / "cases.json").read_text())
    rendered = {
        "CASES.md": build_cases_md(cases),
        "BOUNDARY-CASES.md": build_boundary_md(cases),
    }

    drift = []
    for name, text in sorted(rendered.items()):
        path = ROOT / name
        current = path.read_text() if path.exists() else None
        if check:
            if current != text:
                drift.append(name)
                print(f"DRIFT: {name} on disk does not match cases.json")
            else:
                print(f"OK: {name} matches cases.json")
        else:
            path.write_text(text)
            state = "unchanged" if current == text else "written"
            print(f"{state}: {name} ({len(text.splitlines())} lines)")

    if check and drift:
        print()
        print("FAILED: run 'python3 scripts/build_cases_md.py' and commit the result. "
              "Case content is edited in cases.json, never in the generated Markdown.")
        return 1
    if check:
        print()
        print("PASSED: both generated files match cases.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
