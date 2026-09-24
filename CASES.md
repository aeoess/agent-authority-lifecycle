# Authority Lifecycle: Cases

Version 0.2.2-draft. Part of the Agent Passport System work. Apache-2.0, same terms as `AUTHORITY-LIFECYCLE.md`.

These are situations where the people, keys, approvals, offices, resources or infrastructure around an agent change, and the question is what happens to its authority. They test the concepts and invariants in [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md) and the gaps in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

Many cases rest on a human, institutional or systems precedent: a statute, a court or agency finding, a standard or a documented incident. None of those sources says anything about AI agents. The translation into agent terms is ours, and the precedent is a source of cases, not a claim that the law applies to AI agents.

There are three tiers.

- **Verified.** We fetched the cited source and checked that it supports the stated precedent. The expected outcome is still **proposed**. A fixture existing for a case does not change that: the vectors are candidates against proposed text, not conformance results.
- **Reviewed hypothetical.** The case survived the same review pass as a verified case, but it claims no external precedent: no statute, court or agency finding, standard or documented incident supports it. The source line says so, in place of a citation.
- **Candidate.** Produced by a research pass and not yet checked. The source is claimed, not verified. A "Known issue" note marks a problem already found. Candidates are verified, corrected, merged into another case or removed as review continues. Do not cite a candidate's source without checking it.

Current count: 126 verified, 7 reviewed hypothetical, 1 candidate. No case is a conformance result. 133 of the 134 carry a **Fixture** line naming the fixture family and vector ids that now exist for them in the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite. Most of those are now merged_candidate, pinned to the lab main commit the line links, still candidates against proposed text rather than conformance results. The `lifecycle-purpose-exhaustion` family is held back and stays on an unmerged candidate branch, which the line says. One case, LC-B-023, has no fixture because no record set decides it. The same mapping in machine-readable form is the `fixtures` array in [cases.json](cases.json).

What changed since v0.1. Every v0.1 candidate was read against its source by a survivor pass and then re-checked by an independent auditor who fetched each source again. Candidates that survived both became verified, duplicates were folded into a representative and listed under it as named variants, cases that resolve to a security or evidence question rather than an authority verdict moved to [BOUNDARY-CASES.md](BOUNDARY-CASES.md), and the rest were removed. Thirteen families the corpus covered thinly or not at all were researched from scratch in the same pass. IDs are stable: an ID that appears in v0.1 means the same case here.

Cases are grouped by the authority question they raise. A representative case lists its folded duplicates on a "Variants" line, with the one-line difference that made each a duplicate rather than a separate case.

## Contents

- [Verified cases](#verified-cases)
  - [Principal events](#principal-events) (9)
  - [Fiduciary succession](#fiduciary-succession) (3)
  - [Third-party reliance and notice](#third-party-reliance-and-notice) (3)
  - [Organization events](#organization-events) (5)
  - [Legal and regulatory events](#legal-and-regulatory-events) (15)
  - [Root authority and succession](#root-authority-and-succession) (1)
  - [Multiple principals and conflict](#multiple-principals-and-conflict) (15)
  - [Outside-the-chain standing](#outside-the-chain-standing) (3)
  - [Subdelegation edges](#subdelegation-edges) (2)
  - [Agent renunciation](#agent-renunciation) (2)
  - [Principal unreachable](#principal-unreachable) (1)
  - [Time and scheduling](#time-and-scheduling) (13)
  - [Credential events](#credential-events) (18)
  - [Agent-side events](#agent-side-events) (12)
  - [Infrastructure failure](#infrastructure-failure) (8)
  - [Evidence and record](#evidence-and-record) (2)
  - [Identifier reuse and rename](#identifier-reuse-and-rename) (3)
  - [Policy change](#policy-change) (3)
  - [Expiry and renewal](#expiry-and-renewal) (3)
  - [Shared identity with no accountable principal](#shared-identity-with-no-accountable-principal) (3)
  - [Purpose exhaustion](#purpose-exhaustion) (2)
- [Reviewed hypothetical cases](#reviewed-hypothetical-cases)
  - [Organization events](#organization-events-1) (3)
  - [Time and scheduling](#time-and-scheduling-1) (1)
  - [Credential events](#credential-events-1) (1)
  - [Infrastructure failure](#infrastructure-failure-1) (2)
- [Candidate cases](#candidate-cases)
  - [Subdelegation edges](#subdelegation-edges-1) (1)

<details>
<summary>All 134 cases</summary>

| ID | Case | Family |
|---|---|---|
| [LC-A-001](#lc-a-001-a-principals-death-ends-actual-authority-regardless-of-durability-effective-on-the-agents-notice-not-at-the-instant-of-death) | A principal's death ends actual authority regardless of durability, effective on the agent's notice, not at the instant of death | [Principal events](#principal-events) |
| [LC-A-003](#lc-a-003-an-unmet-contingency-is-indeterminate-not-simply-not-yet-started) | An unmet contingency is indeterminate, not simply "not yet started" | [Principal events](#principal-events) |
| [LC-A-005](#lc-a-005-divorce-automatically-revokes-a-spouses-designation-as-agent-without-any-separate-revocation-act) | Divorce automatically revokes a spouse's designation as agent, without any separate revocation act | [Principal events](#principal-events) |
| [LC-A-006](#lc-a-006-the-event-that-revokes-a-spousal-delegation-is-jurisdiction-dependent-filing-not-just-a-final-decree-can-be-the-trigger) | The event that revokes a spousal delegation is jurisdiction-dependent: filing, not just a final decree, can be the trigger | [Principal events](#principal-events) |
| [LC-A-008](#lc-a-008-purpose-exhaustion-ends-authority-once-an-authenticated-record-shows-the-purpose-was-met-not-once-the-agent-subjectively-decides-it-was) | Purpose exhaustion ends authority once an authenticated record shows the purpose was met, not once the agent subjectively decides it was | [Principal events](#principal-events) |
| [LC-A-009](#lc-a-009-a-fiduciary-who-feloniously-kills-the-principal-forfeits-the-appointment-retroactively-not-merely-from-the-date-of-the-finding) | A fiduciary who feloniously kills the principal forfeits the appointment retroactively, not merely from the date of the finding | [Principal events](#principal-events) |
| [LC-A-010](#lc-a-010-a-court-appointed-guardian-or-conservator-can-limit-suspend-or-terminate-an-existing-agents-authority-from-outside-the-delegation-chain-entirely) | A court-appointed guardian or conservator can limit, suspend, or terminate an existing agent's authority from outside the delegation chain entirely | [Principal events](#principal-events) |
| [LC-A-012](#lc-a-012-the-coupled-with-an-interest-survival-past-death-rule-is-dictum-the-leading-case-actually-held-the-power-at-issue-died-with-the-principal) | The "coupled with an interest" survival-past-death rule is dictum: the leading case actually held the power at issue died with the principal | [Principal events](#principal-events) |
| [LC-A-016](#lc-a-016-some-replacement-authority-is-pre-committed-at-issuance-time-not-issued-fresh-after-the-fact) | Some replacement authority is pre-committed at issuance time, not issued fresh after the fact | [Principal events](#principal-events) |
| [LC-A-019](#lc-a-019-co-trustees-act-by-majority-when-they-cannot-reach-unanimity-and-a-vacancy-does-not-have-to-be-filled-before-the-remainder-can-act) | Co-trustees act by majority when they cannot reach unanimity, and a vacancy does not have to be filled before the remainder can act | [Fiduciary succession](#fiduciary-succession) |
| [LC-A-022](#lc-a-022-a-temporary-administrators-authority-is-scoped-to-preservation-and-ends-automatically-the-instant-the-underlying-dispute-resolves) | A temporary administrator's authority is scoped to preservation and ends automatically the instant the underlying dispute resolves | [Fiduciary succession](#fiduciary-succession) |
| [LC-A-023](#lc-a-023-ratification-retroactively-authorizes-a-prior-unauthorized-act-but-cannot-be-used-to-defeat-a-third-partys-intervening-rights-and-it-is-all-or-nothing) | Ratification retroactively authorizes a prior unauthorized act, but cannot be used to defeat a third party's intervening rights, and it is all-or-nothing | [Fiduciary succession](#fiduciary-succession) |
| [LC-A-027](#lc-a-027-a-verifiers-internal-chain-is-void-and-a-relying-partys-protected-reliance-are-two-separate-facts-not-one-boolean) | A verifier's internal "chain is void" and a relying party's protected reliance are two separate facts, not one boolean | [Third-party reliance and notice](#third-party-reliance-and-notice) |
| [LC-A-028](#lc-a-028-cutting-off-apparent-authority-takes-more-than-one-kind-of-notice-actual-notice-for-known-prior-counterparties-publication-for-strangers) | Cutting off apparent authority takes more than one kind of notice: actual notice for known prior counterparties, publication for strangers | [Third-party reliance and notice](#third-party-reliance-and-notice) |
| [LC-A-033](#lc-a-033-a-newer-delegation-instrument-does-not-automatically-revoke-an-older-one-absent-an-express-revocation-clause) | A newer delegation instrument does not automatically revoke an older one absent an express revocation clause | [Third-party reliance and notice](#third-party-reliance-and-notice) |
| [LC-B-012](#lc-b-012-a-merger-can-vest-authority-in-a-new-principal-by-operation-of-law-with-no-issuance-event-at-all) | A merger can vest authority in a new principal by operation of law, with no issuance event at all | [Organization events](#organization-events) |
| [LC-B-013](#lc-b-013-automatic-corporate-law-vesting-does-not-reach-the-technical-delegation-layer) | Automatic corporate-law vesting does not reach the technical delegation layer | [Organization events](#organization-events) |
| [LC-B-016](#lc-b-016-a-dissolution-statute-can-automatically-narrow-the-scope-of-authority-that-remains-otherwise-valid) | A dissolution statute can automatically narrow the scope of authority that remains otherwise valid | [Organization events](#organization-events) |
| [LC-B-028](#lc-b-028-authorization-has-to-be-rechecked-right-up-to-the-moment-of-final-execution-not-just-at-issuance) | Authorization has to be rechecked right up to the moment of final execution, not just at issuance | [Organization events](#organization-events) |
| [LC-B-029](#lc-b-029-a-receiving-banks-acceptance-is-the-hard-boundary-after-which-a-mid-flight-authority-change-no-longer-stops-the-order) | A receiving bank's acceptance is the hard boundary after which a mid-flight authority change no longer stops the order | [Organization events](#organization-events) |
| [LC-B-007](#lc-b-007-ratification-is-a-new-record-that-reaches-backward-not-a-rewrite-of-the-original) | Ratification is a new record that reaches backward, not a rewrite of the original | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-008](#lc-b-008-authority-can-end-completely-instantly-and-outside-the-delegation-system-entirely) | Authority can end completely, instantly, and outside the delegation system entirely | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-009](#lc-b-009-a-legal-event-with-instantaneous-effect-can-disqualify-an-action-before-anyone-could-have-checked-for-it) | A legal event with instantaneous effect can disqualify an action before anyone could have checked for it | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-010](#lc-b-010-a-court-supervised-filing-can-add-an-approval-gate-without-pausing-the-underlying-authority) | A court-supervised filing can add an approval gate without pausing the underlying authority | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-011](#lc-b-011-a-restriction-imposed-by-an-external-filing-needs-an-equally-external-release-trigger) | A restriction imposed by an external filing needs an equally external release trigger | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-017](#lc-b-017-a-legitimate-new-authority-root-can-come-from-entirely-outside-the-original-chain) | A legitimate new authority root can come from entirely outside the original chain | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-018](#lc-b-018-chain-validity-and-lawfulness-to-execute-are-different-questions) | Chain validity and lawfulness to execute are different questions | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-019](#lc-b-019-removing-an-external-block-restores-execution-on-an-unbroken-chain-not-through-a-reauthorization) | Removing an external block restores execution on an unbroken chain, not through a reauthorization | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-022](#lc-b-022-a-real-legal-exception-can-supply-exactly-the-basis-a-completeness-claim-needs-without-needing-an-open-ended-we-keep-everything-for-audit-policy) | A real legal exception can supply exactly the basis a completeness claim needs, without needing an open-ended "we keep everything for audit" policy | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-023](#lc-b-023-anticipated-litigation-suspends-routine-record-pruning-before-any-formal-process-is-served) | Anticipated litigation suspends routine record pruning before any formal process is served | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-024](#lc-b-024-multiple-independent-suspensions-on-the-same-principal-have-to-be-released-independently-not-cleared-by-any-one-of-them-lapsing) | Multiple independent suspensions on the same principal have to be released independently, not cleared by any one of them lapsing | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-025](#lc-b-025-a-single-revoked-license-can-invalidate-every-chain-that-depends-on-it-at-once) | A single revoked license can invalidate every chain that depends on it at once | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-026](#lc-b-026-a-third-party-outside-the-principal-agent-relationship-can-inject-a-new-approval-gate-into-an-otherwise-unmodified-valid-chain) | A third party outside the principal-agent relationship can inject a new approval gate into an otherwise unmodified, valid chain | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-027](#lc-b-027-forfeiture-changes-who-owns-the-resource-not-just-who-may-deal-with-it-for-now) | Forfeiture changes who owns the resource, not just who may deal with it for now | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-B-031](#lc-b-031-the-same-bankruptcy-chapter-question-can-produce-opposite-authority-outcomes) | The same bankruptcy chapter question can produce opposite authority outcomes | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-C-007](#lc-c-007-whether-a-delegation-is-bound-to-an-office-or-to-a-person-is-a-design-choice-the-framework-has-to-represent-explicitly) | Whether a delegation is bound to an office or to a person is a design choice the framework has to represent explicitly | [Root authority and succession](#root-authority-and-succession) |
| [LC-C-002](#lc-c-002-a-live-capacity-dispute-needs-a-default-holder-a-deadline-and-a-supermajority-override-not-a-block-or-a-race) | A live capacity dispute needs a default holder, a deadline, and a supermajority override, not a block or a race | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-005](#lc-c-005-two-independently-valid-succession-sources-can-name-different-people-for-the-same-seat-and-nothing-says-which-one-wins) | Two independently valid succession sources can name different people for the same seat, and nothing says which one wins | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-006](#lc-c-006-a-tainted-ancestor-invalidates-dependents-only-from-the-moment-the-taint-is-found-not-retroactively) | A tainted ancestor invalidates dependents only from the moment the taint is found, not retroactively | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-009](#lc-c-009-a-legitimately-confidential-succession-order-breaks-the-assumption-that-every-chain-is-independently-publicly-verifiable) | A legitimately confidential succession order breaks the assumption that every chain is independently, publicly verifiable | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-011](#lc-c-011-a-concurrence-requirement-is-a-gate-at-the-next-authorization-boundary-not-a-second-chain-to-union-with-the-first) | A concurrence requirement is a gate at the next authorization boundary, not a second chain to union with the first | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-012](#lc-c-012-independently-rooted-chains-can-commit-to-a-shared-objective-without-unioning-their-scopes) | Independently rooted chains can commit to a shared objective without unioning their scopes | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-016](#lc-c-016-the-bar-for-granting-authority-and-the-bar-for-withdrawing-it-are-not-always-the-same-bar) | The bar for granting authority and the bar for withdrawing it are not always the same bar | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-018](#lc-c-018-concurrence-can-generalize-beyond-a-fixed-pair-to-an-enumerated-role-set-where-silence-itself-blocks-the-action) | Concurrence can generalize beyond a fixed pair to an enumerated role set where silence itself blocks the action | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-020](#lc-c-020-an-authority-position-can-be-created-on-the-fly-by-an-eligibility-rule-with-no-pre-named-holder-at-all) | An authority position can be created on the fly by an eligibility rule, with no pre-named holder at all | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-022](#lc-c-022-a-pending-ratification-state-is-neither-revoked-nor-not-revoked-and-if-ratification-is-denied-the-record-has-to-say-the-action-was-provisional-throughout-not-that-a-final-revocation-was-later-reversed) | A pending-ratification state is neither "revoked" nor "not revoked," and if ratification is denied, the record has to say the action was provisional throughout, not that a final revocation was later reversed | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-029](#lc-c-029-a-shared-coalition-grant-can-carry-different-per-contributor-restrictions-that-a-pooled-ruleset-cannot-represent) | A shared coalition grant can carry different, per-contributor restrictions that a pooled ruleset cannot represent | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-C-031](#lc-c-031-a-standing-cause-free-override-can-sit-above-a-concurrently-exercised-authority-without-ever-going-through-a-revocation-channel) | A standing, cause-free override can sit above a concurrently exercised authority without ever going through a revocation channel | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-H-001](#lc-h-001-one-co-settlors-unilateral-revocation-of-a-joint-grant-reaches-only-their-own-contributed-share-not-the-whole-grant) | One co-settlor's unilateral revocation of a joint grant reaches only their own contributed share, not the whole grant | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-H-002](#lc-h-002-on-an-account-requiring-multiple-signers-any-one-signers-stop-instruction-controls-over-a-contradictory-pay-instruction-from-a-co-signer) | On an account requiring multiple signers, any one signer's stop instruction controls over a contradictory pay instruction from a co-signer | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-H-003](#lc-h-003-bankruptcy-discharge-and-debt-reaffirmation-racing-each-other-resolve-by-a-statutory-sequencing-and-rescission-window-not-a-first-arrival-rule) | Bankruptcy discharge and debt reaffirmation racing each other resolve by a statutory sequencing and rescission window, not a first-arrival rule | [Multiple principals and conflict](#multiple-principals-and-conflict) |
| [LC-H-004](#lc-h-004-a-boards-suspension-of-a-principals-authority-is-not-valid-board-action-at-all-without-the-quorum-required-for-the-board-to-transact-business) | A board's suspension of a principal's authority is not valid board action at all without the quorum required for the board to transact business | [Outside-the-chain standing](#outside-the-chain-standing) |
| [LC-H-005](#lc-h-005-a-labor-boards-reinstatement-order-is-a-new-grant-issued-from-outside-the-original-relationship-not-a-revival-of-the-exact-terminated-one) | A labor board's reinstatement order is a new grant issued from outside the original relationship, not a revival of the exact terminated one | [Outside-the-chain standing](#outside-the-chain-standing) |
| [LC-H-006](#lc-h-006-a-disputed-root-can-be-deposited-with-a-neutral-forum-pending-resolution-discharging-the-holder-from-choosing-between-claimants) | A disputed root can be deposited with a neutral forum pending resolution, discharging the holder from choosing between claimants | [Outside-the-chain standing](#outside-the-chain-standing) |
| [LC-H-007](#lc-h-007-checking-each-delegation-artifacts-validity-period-independently-means-a-childs-stated-expiry-can-extend-past-its-parents-without-the-base-algorithm-ever-comparing-the-two) | Checking each delegation artifact's validity period independently means a child's stated expiry can extend past its parent's without the base algorithm ever comparing the two | [Subdelegation edges](#subdelegation-edges) |
| [LC-H-008](#lc-h-008-delegation-depth-exhaustion-is-a-distinct-failure-mode-rejecting-subdelegation-past-a-chains-own-declared-maximum-depth) | Delegation depth exhaustion is a distinct failure mode, rejecting subdelegation past a chain's own declared maximum depth | [Subdelegation edges](#subdelegation-edges) |
| [LC-H-010](#lc-h-010-a-directors-resignation-is-effective-on-delivery-of-notice-not-on-the-principals-acceptance) | A director's resignation is effective on delivery of notice, not on the principal's acceptance | [Agent renunciation](#agent-renunciation) |
| [LC-H-011](#lc-h-011-a-partners-power-to-dissociate-is-effective-immediately-whether-the-dissociation-is-rightful-or-wrongful-and-wrongfulness-is-a-separate-later-liability-question) | A partner's power to dissociate is effective immediately whether the dissociation is rightful or wrongful, and wrongfulness is a separate, later liability question | [Agent renunciation](#agent-renunciation) |
| [LC-H-012](#lc-h-012-a-payment-order-requiring-customer-confirmation-stays-unconfirmed-not-authorized-by-default-when-the-customer-cannot-be-reached-to-complete-the-agreed-procedure) | A payment order requiring customer confirmation stays unconfirmed, not authorized by default, when the customer cannot be reached to complete the agreed procedure | [Principal unreachable](#principal-unreachable) |
| [LC-C-008](#lc-c-008-a-missing-successor-designation-should-fail-open-to-a-named-statutory-fallback-not-fail-closed-like-an-unknown-revocation) | A missing successor designation should fail open to a named statutory fallback, not fail closed like an unknown revocation | [Time and scheduling](#time-and-scheduling) |
| [LC-C-014](#lc-c-014-a-handover-can-require-the-incoming-holders-acknowledgment-with-authority-staying-put-until-it-arrives) | A handover can require the incoming holder's acknowledgment, with authority staying put until it arrives | [Time and scheduling](#time-and-scheduling) |
| [LC-C-015](#lc-c-015-losing-contact-with-a-directing-principal-should-trigger-a-pre-authorized-fallback-not-a-freeze-or-silent-continuation) | Losing contact with a directing principal should trigger a pre-authorized fallback, not a freeze or silent continuation | [Time and scheduling](#time-and-scheduling) |
| [LC-C-017](#lc-c-017-a-standing-rotation-schedule-is-its-own-form-of-pre-authorization-distinct-from-a-one-time-succession-event) | A standing rotation schedule is its own form of pre-authorization, distinct from a one-time succession event | [Time and scheduling](#time-and-scheduling) |
| [LC-C-025](#lc-c-025-continuous-coverage-roles-need-departure-and-successor-designation-to-be-a-single-atomic-operation-not-a-sequence) | Continuous-coverage roles need departure and successor designation to be a single atomic operation, not a sequence | [Time and scheduling](#time-and-scheduling) |
| [LC-E-008](#lc-e-008-a-long-running-instances-remaining-steps-must-resolve-against-the-authority-policy-version-it-started-under-not-the-version-deployed-today) | A long-running instance's remaining steps must resolve against the authority-policy version it started under, not the version deployed today | [Time and scheduling](#time-and-scheduling) |
| [LC-E-014](#lc-e-014-a-recurring-series-can-outlive-the-identity-that-scheduled-it-with-no-automatic-cleanup-and-no-owner-left-to-cancel-it) | A recurring series can outlive the identity that scheduled it, with no automatic cleanup and no owner left to cancel it | [Time and scheduling](#time-and-scheduling) |
| [LC-E-018](#lc-e-018-a-running-scheduled-occurrence-keeps-the-identity-it-was-created-with-only-the-next-occurrence-picks-up-a-tightened-template) | A running scheduled occurrence keeps the identity it was created with. Only the next occurrence picks up a tightened template | [Time and scheduling](#time-and-scheduling) |
| [LC-E-019](#lc-e-019-authority-stays-valid-through-a-scheduled-wind-down-not-cut-off-the-instant-termination-begins) | Authority stays valid through a scheduled wind-down, not cut off the instant termination begins | [Time and scheduling](#time-and-scheduling) |
| [LC-E-020](#lc-e-020-a-scheduled-jobs-permissions-are-bound-to-its-creators-identity-at-schedule-time-and-the-schedulers-own-docs-are-silent-on-what-happens-once-that-identity-is-gone) | A scheduled job's permissions are bound to its creator's identity at schedule time, and the scheduler's own docs are silent on what happens once that identity is gone | [Time and scheduling](#time-and-scheduling) |
| [LC-G-007](#lc-g-007-a-validity-period-check-is-run-against-the-checking-partys-own-clock-at-check-time-not-the-issuers-claimed-clock) | A validity-period check is run against the checking party's own clock at check time, not the issuer's claimed clock | [Time and scheduling](#time-and-scheduling) |
| [LC-G-008](#lc-g-008-a-single-external-time-source-with-no-independent-check-can-silently-go-wrong-and-nothing-downstream-can-detect-it) | A single external time source with no independent check can silently go wrong and nothing downstream can detect it | [Time and scheduling](#time-and-scheduling) |
| [LC-G-009](#lc-g-009-two-legitimately-run-clocks-can-disagree-by-design-during-a-defined-window-and-neither-reading-is-the-wrong-one) | Two legitimately-run clocks can disagree by design during a defined window, and neither reading is the wrong one | [Time and scheduling](#time-and-scheduling) |
| [LC-D-001](#lc-d-001-a-third-partys-own-breach-disclosure-has-to-become-a-revocation-relevant-trigger-even-though-the-delegating-org-revoked-nothing-itself) | A third party's own breach disclosure has to become a revocation-relevant trigger, even though the delegating org revoked nothing itself | [Credential events](#credential-events) |
| [LC-D-003](#lc-d-003-believed-unused-is-not-the-same-as-verified-inventory-and-the-gap-between-them-is-exactly-where-this-incident-happened) | "Believed unused" is not the same as "verified inventory," and the gap between them is exactly where this incident happened | [Credential events](#credential-events) |
| [LC-D-004](#lc-d-004-a-single-compromised-operator-identity-can-be-an-implicit-ancestor-over-many-independent-trees-at-once) | A single compromised operator identity can be an implicit ancestor over many independent trees at once | [Credential events](#credential-events) |
| [LC-D-009](#lc-d-009-a-documented-scope-means-nothing-if-the-resource-side-boundary-never-actually-enforces-it) | A documented scope means nothing if the resource-side boundary never actually enforces it | [Credential events](#credential-events) |
| [LC-D-010](#lc-d-010-a-credential-with-no-natural-end-issued-for-a-purpose-that-ended-is-a-standing-liability-no-chain-verification-check-can-catch) | A credential with no natural end, issued for a purpose that ended, is a standing liability no chain-verification check can catch | [Credential events](#credential-events) |
| [LC-D-011](#lc-d-011-inheriting-another-organizations-entire-root-of-trust-by-acquisition-is-not-itself-a-re-verification-event) | Inheriting another organization's entire root of trust by acquisition is not itself a re-verification event | [Credential events](#credential-events) |
| [LC-D-014](#lc-d-014-when-an-issuers-own-issuance-log-cannot-be-trusted-per-artifact-revocation-is-the-wrong-remedy) | When an issuer's own issuance log cannot be trusted, per-artifact revocation is the wrong remedy | [Credential events](#credential-events) |
| [LC-D-025](#lc-d-025-authority-is-currently-valid-and-a-complete-record-exists-of-what-was-done-under-it-are-different-claims-a-verifier-answers-separately) | "Authority is currently valid" and "a complete record exists of what was done under it" are different claims a verifier answers separately | [Credential events](#credential-events) |
| [LC-D-029](#lc-d-029-a-correctly-resolved-historical-key-proves-who-signed-not-what-was-actually-built) | A correctly-resolved historical key proves who signed, not what was actually built | [Credential events](#credential-events) |
| [LC-D-033](#lc-d-033-adding-a-new-authorized-device-to-an-identity-needs-the-same-scrutiny-as-issuing-a-new-delegation-regardless-of-which-internal-path-added-it) | Adding a new authorized device to an identity needs the same scrutiny as issuing a new delegation, regardless of which internal path added it | [Credential events](#credential-events) |
| [LC-D-034](#lc-d-034-test-or-legacy-as-a-label-is-not-the-same-as-test-or-legacy-as-a-validity-fact) | "Test" or "legacy" as a label is not the same as "test" or "legacy" as a validity fact | [Credential events](#credential-events) |
| [LC-F-008](#lc-f-008-a-verifier-that-checks-status-entirely-offline-against-a-synced-snapshot-needs-its-own-evidence-category-not-a-degraded-live-check) | A verifier that checks status entirely offline against a synced snapshot needs its own evidence category, not a degraded live check | [Credential events](#credential-events) |
| [LC-F-013](#lc-f-013-a-clock-skew-rejection-is-a-third-category-neither-expiry-nor-revocation) | A clock-skew rejection is a third category, neither expiry nor revocation | [Credential events](#credential-events) |
| [LC-F-033](#lc-f-033-systemic-issuer-misbehavior-once-found-escalates-to-distrusting-the-whole-issuer-not-to-revoking-the-chains-that-got-caught) | Systemic issuer misbehavior, once found, escalates to distrusting the whole issuer, not to revoking the chains that got caught | [Credential events](#credential-events) |
| [LC-G-001](#lc-g-001-a-planned-key-rotation-at-the-end-of-a-declared-cryptoperiod-is-not-an-investigation-trigger) | A planned key rotation at the end of a declared cryptoperiod is not an investigation trigger | [Credential events](#credential-events) |
| [LC-G-002](#lc-g-002-unknown-onset-of-a-key-compromise-forces-the-suspect-window-to-start-at-exposure-not-at-discovery) | Unknown onset of a key compromise forces the suspect window to start at exposure, not at discovery | [Credential events](#credential-events) |
| [LC-G-003](#lc-g-003-partitioning-already-issued-artifacts-around-a-signing-key-compromise-needs-an-independent-timestamp-not-the-compromised-keys-own-say-so) | Partitioning already-issued artifacts around a signing-key compromise needs an independent timestamp, not the compromised key's own say-so | [Credential events](#credential-events) |
| [LC-G-004](#lc-g-004-a-key-scoped-for-one-purpose-can-be-wrongly-accepted-as-authoritative-for-a-broader-one-if-the-verifier-does-not-check-scope-separately-from-signature-validity) | A key scoped for one purpose can be wrongly accepted as authoritative for a broader one if the verifier does not check scope separately from signature validity | [Credential events](#credential-events) |
| [LC-E-001](#lc-e-001-a-stable-model-alias-is-a-pointer-with-a-documented-default-not-a-pinned-capability-set) | A stable model alias is a pointer with a documented default, not a pinned capability set | [Agent-side events](#agent-side-events) |
| [LC-E-002](#lc-e-002-a-valid-non-expired-non-revoked-grant-can-become-unexecutable-and-that-is-a-fourth-state-not-a-variant-of-the-other-three) | A valid, non-expired, non-revoked grant can become unexecutable, and that is a fourth state, not a variant of the other three | [Agent-side events](#agent-side-events) |
| [LC-E-004](#lc-e-004-a-forked-process-inherits-a-snapshot-of-its-parents-authority-not-a-live-reference-to-it) | A forked process inherits a snapshot of its parent's authority, not a live reference to it | [Agent-side events](#agent-side-events) |
| [LC-E-006](#lc-e-006-holding-a-scope-does-not-carry-authority-to-hand-it-to-something-you-spawn) | Holding a scope does not carry authority to hand it to something you spawn | [Agent-side events](#agent-side-events) |
| [LC-E-012](#lc-e-012-a-valid-timestamp-alone-does-not-stop-replay-a-maintained-seen-cache-does) | A valid timestamp alone does not stop replay. A maintained seen-cache does | [Agent-side events](#agent-side-events) |
| [LC-E-013](#lc-e-013-a-long-jobs-own-logic-must-expect-authority-invalidation-to-arrive-silently-mid-run-not-only-at-its-next-gateway-check) | A long job's own logic must expect authority invalidation to arrive silently mid-run, not only at its next gateway check | [Agent-side events](#agent-side-events) |
| [LC-E-021](#lc-e-021-revoking-a-narrow-lookup-permission-does-not-erase-what-a-session-already-learned-while-that-permission-was-valid) | Revoking a narrow lookup permission does not erase what a session already learned while that permission was valid | [Agent-side events](#agent-side-events) |
| [LC-E-023](#lc-e-023-faithfully-restoring-a-processs-memory-says-nothing-about-whether-the-authority-it-was-holding-is-still-current) | Faithfully restoring a process's memory says nothing about whether the authority it was holding is still current | [Agent-side events](#agent-side-events) |
| [LC-E-025](#lc-e-025-a-self-replicated-copy-holds-no-authority-by-default-no-matter-how-identical-it-is-to-an-authorized-original) | A self-replicated copy holds no authority by default, no matter how identical it is to an authorized original | [Agent-side events](#agent-side-events) |
| [LC-E-027](#lc-e-027-a-real-precedent-exists-for-gating-expanded-capability-behind-mandatory-re-consent-not-automatic-inheritance) | A real precedent exists for gating expanded capability behind mandatory re-consent, not automatic inheritance | [Agent-side events](#agent-side-events) |
| [LC-E-031](#lc-e-031-a-memory-architecture-built-for-one-continuous-identity-says-nothing-about-whether-its-content-is-current-authority-once-transferred-to-a-different-identity) | A memory architecture built for one continuous identity says nothing about whether its content is current authority once transferred to a different identity | [Agent-side events](#agent-side-events) |
| [LC-E-033](#lc-e-033-a-provider-side-capability-upgrade-can-expand-what-a-delegation-authorizes-with-zero-delegation-layer-event) | A provider-side capability upgrade can expand what a delegation authorizes with zero delegation-layer event | [Agent-side events](#agent-side-events) |
| [LC-F-006](#lc-f-006-a-revocation-status-list-served-past-its-own-declared-refresh-time-is-stale-not-confirmed-clean) | A revocation status list served past its own declared refresh time is stale, not confirmed clean | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-016](#lc-f-016-a-storage-layer-partition-can-silently-resurrect-revoked-authority-below-the-application-layer) | A storage-layer partition can silently resurrect revoked authority below the application layer | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-017](#lc-f-017-a-revocation-that-is-true-at-the-source-can-still-read-as-false-at-a-lagging-replica-the-new-enemy-problem) | A revocation that is true at the source can still read as false at a lagging replica: the "new enemy problem" | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-018](#lc-f-018-multiple-regional-enforcement-points-are-physically-distinct-copies-of-authority-state-and-can-briefly-disagree) | Multiple regional enforcement points are physically distinct copies of authority state, and can briefly disagree | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-022](#lc-f-022-a-revocation-write-must-not-be-able-to-lose-a-race-to-an-unrelated-lower-stakes-concurrent-write) | A revocation write must not be able to lose a race to an unrelated, lower-stakes concurrent write | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-024](#lc-f-024-holding-a-lock-is-not-proof-of-exclusive-access-once-a-pause-can-outlast-the-lease) | Holding a lock is not proof of exclusive access once a pause can outlast the lease | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-026](#lc-f-026-without-a-quorum-safeguard-an-isolated-primary-keeps-accepting-authority-mutating-writes-nobody-else-will-ever-see) | Without a quorum safeguard, an isolated primary keeps accepting authority-mutating writes nobody else will ever see | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-027](#lc-f-027-an-empty-audit-window-can-mean-the-record-hasnt-arrived-yet-not-that-nothing-happened) | An empty audit window can mean the record hasn't arrived yet, not that nothing happened | [Infrastructure failure](#infrastructure-failure) |
| [LC-G-005](#lc-g-005-a-recordkeeping-duty-tied-to-a-now-ended-authority-relationship-outlives-the-relationship-itself-on-its-own-clock) | A recordkeeping duty tied to a now-ended authority relationship outlives the relationship itself, on its own clock | [Evidence and record](#evidence-and-record) |
| [LC-G-006](#lc-g-006-a-decision-receipt-is-evaluated-against-the-view-available-at-decision-time-not-rewritten-by-what-is-learned-afterward) | A decision receipt is evaluated against the view available at decision time, not rewritten by what is learned afterward | [Evidence and record](#evidence-and-record) |
| [LC-I-001](#lc-i-001-re-registering-an-abandoned-identifier-hands-the-new-controller-everything-still-addressed-to-the-old-one-with-no-delegation-layer-event-marking-the-change-of-hands) | Re-registering an abandoned identifier hands the new controller everything still addressed to the old one, with no delegation-layer event marking the change of hands | [Identifier reuse and rename](#identifier-reuse-and-rename) |
| [LC-I-002](#lc-i-002-a-rename-does-not-travel-with-the-references-that-still-point-at-the-old-name-and-a-retirement-policy-meant-to-close-that-gap-can-itself-be-raced) | A rename does not travel with the references that still point at the old name, and a retirement policy meant to close that gap can itself be raced | [Identifier reuse and rename](#identifier-reuse-and-rename) |
| [LC-I-003](#lc-i-003-a-recycled-identifier-reused-for-a-new-subject-can-still-unlock-the-old-subjects-authority-because-nothing-marked-the-account-as-depending-on-who-currently-holds-the-number) | A recycled identifier reused for a new subject can still unlock the old subject's authority, because nothing marked the account as depending on who currently holds the number | [Identifier reuse and rename](#identifier-reuse-and-rename) |
| [LC-I-004](#lc-i-004-a-policy-rollback-needs-a-defined-current-pointer-not-a-race-to-see-which-edit-lands-last) | A policy rollback needs a defined "current" pointer, not a race to see which edit lands last | [Policy change](#policy-change) |
| [LC-I-005](#lc-i-005-what-a-past-authorization-decision-is-evidenced-against-has-to-be-the-policy-version-live-at-the-moment-it-happened-not-whatever-version-is-live-when-someone-later-looks) | What a past authorization decision is evidenced against has to be the policy version live at the moment it happened, not whatever version is live when someone later looks | [Policy change](#policy-change) |
| [LC-I-006](#lc-i-006-when-a-policy-tightens-after-something-was-approved-under-the-old-rule-the-old-grant-doesnt-need-to-be-revoked-and-the-new-rule-doesnt-reach-backward-on-its-own) | When a policy tightens after something was approved under the old rule, the old grant doesn't need to be revoked, and the new rule doesn't reach backward on its own | [Policy change](#policy-change) |
| [LC-I-007](#lc-i-007-reaching-the-stated-end-date-and-being-cut-off-early-for-cause-are-different-events-and-an-evidence-trail-has-to-say-which-one-happened) | Reaching the stated end date and being cut off early for cause are different events, and an evidence trail has to say which one happened | [Expiry and renewal](#expiry-and-renewal) |
| [LC-I-008](#lc-i-008-calling-it-a-renewal-doesnt-make-it-an-extension-some-renewal-processes-issue-an-entirely-new-artifact-and-discard-the-old-one-outright) | Calling it a "renewal" doesn't make it an extension. Some renewal processes issue an entirely new artifact and discard the old one outright | [Expiry and renewal](#expiry-and-renewal) |
| [LC-I-009](#lc-i-009-an-interim-holders-mandate-to-keep-the-lights-on-is-not-a-mandate-to-make-new-binding-commitments-in-the-vacancys-name-including-extending-its-own-reach) | An interim holder's mandate to keep the lights on is not a mandate to make new, binding commitments in the vacancy's name, including extending its own reach | [Expiry and renewal](#expiry-and-renewal) |
| [LC-I-010](#lc-i-010-a-credential-answering-who-did-this-with-a-group-name-instead-of-a-person-is-a-standard-recognized-failure-mode-not-just-a-bad-habit) | A credential answering "who did this" with a group name instead of a person is a standard-recognized failure mode, not just a bad habit | [Shared identity with no accountable principal](#shared-identity-with-no-accountable-principal) |
| [LC-I-011](#lc-i-011-when-an-action-comes-out-of-a-shared-identity-who-is-accountable-can-be-a-fact-that-has-to-be-investigated-after-the-fact-not-something-the-identity-itself-ever-recorded) | When an action comes out of a shared identity, "who is accountable" can be a fact that has to be investigated after the fact, not something the identity itself ever recorded | [Shared identity with no accountable principal](#shared-identity-with-no-accountable-principal) |
| [LC-I-012](#lc-i-012-a-privileged-identity-that-can-act-for-everyone-has-to-be-structurally-exceptional-not-just-discouraged-in-policy) | A privileged identity that can act for everyone has to be structurally exceptional, not just discouraged in policy | [Shared identity with no accountable principal](#shared-identity-with-no-accountable-principal) |
| [LC-I-013](#lc-i-013-a-grant-issued-for-exactly-one-use-is-supposed-to-stop-being-usable-the-instant-its-used-once-and-a-protocol-can-make-that-a-hard-checked-rule-instead-of-a-convention) | A grant issued for exactly one use is supposed to stop being usable the instant it's used once, and a protocol can make that a hard, checked rule instead of a convention | [Purpose exhaustion](#purpose-exhaustion) |
| [LC-I-014](#lc-i-014-a-permit-issued-for-a-single-specific-act-can-be-built-so-that-using-it-is-the-same-recorded-event-as-spending-it-with-no-separate-step-required-to-make-it-unusable-again) | A permit issued for a single, specific act can be built so that using it is the same recorded event as spending it, with no separate step required to make it unusable again | [Purpose exhaustion](#purpose-exhaustion) |
| [LC-B-002](#lc-b-002-two-independently-authoritative-records-of-the-same-fact-can-disagree-and-neither-is-automatically-the-answer) | Two independently authoritative records of the same fact can disagree, and neither is automatically the answer | [Organization events](#organization-events-1) |
| [LC-B-004](#lc-b-004-a-successors-fresh-grant-is-bounded-by-the-successors-own-ceiling-not-the-predecessors) | A successor's fresh grant is bounded by the successor's own ceiling, not the predecessor's | [Organization events](#organization-events-1) |
| [LC-B-030](#lc-b-030-a-third-partys-own-contract-can-impose-a-re-authorization-gate-neither-side-of-a-clean-succession-controls) | A third party's own contract can impose a re-authorization gate neither side of a clean succession controls | [Organization events](#organization-events-1) |
| [LC-E-034](#lc-e-034-a-queued-action-that-outlasts-a-suspension-needs-a-live-check-at-fire-time-not-just-at-the-moment-it-was-queued) | A queued action that outlasts a suspension needs a live check at fire time, not just at the moment it was queued | [Time and scheduling](#time-and-scheduling-1) |
| [LC-F-035](#lc-f-035-choosing-a-stateless-bearer-credential-format-is-choosing-revocation-only-takes-effect-at-natural-expiry) | Choosing a stateless bearer credential format is choosing "revocation only takes effect at natural expiry" | [Credential events](#credential-events-1) |
| [LC-F-009](#lc-f-009-a-publisher-un-saying-its-own-false-revocation-is-a-different-operation-from-reauthorization-and-needs-its-own-evidence-trail) | A publisher un-saying its own false revocation is a different operation from reauthorization, and needs its own evidence trail | [Infrastructure failure](#infrastructure-failure-1) |
| [LC-F-014](#lc-f-014-an-issuers-own-timestamp-is-only-as-trustworthy-as-the-time-source-it-was-signed-against) | An issuer's own timestamp is only as trustworthy as the time source it was signed against | [Infrastructure failure](#infrastructure-failure-1) |
| [LC-H-009](#lc-h-009-a-child-subdelegation-issued-inside-a-revocations-propagation-window-is-void-once-the-revocation-is-established-a-hypothetical-naming-a-gap-distinct-from-l1) | A child subdelegation issued inside a revocation's propagation window is void once the revocation is established, a hypothetical naming a gap distinct from L1 | [Subdelegation edges](#subdelegation-edges-1) |

</details>

## Verified cases

### Principal events

#### LC-A-001. A principal's death ends actual authority regardless of durability, effective on the agent's notice, not at the instant of death

**Situation.** A principal dies. An agent holding a delegation from that principal, durable or not, keeps trying to act on the principal's accounts. Nobody has processed a revocation record.

**Human analog.** Restatement (Third) of Agency §3.07: [reproduced text, staff.washington.edu](https://staff.washington.edu/djdrake/RESt-Agency.doc): "The death of an individual principal terminates the agent's actual authority. The termination is effective only when the agent has notice of the principal's death." Durability does not change this: Uniform Power of Attorney Act (2006) §110(a), as enacted at [N.H. RSA 564-E:110](https://gc.nh.gov/rsa/html/LVI/564-E/564-E-110.htm): a power of attorney terminates when "(1) the principal dies; (2) the principal becomes incapacitated, if the power of attorney is not durable."

**What should happen.** Authority ends at death for every agent, durable or not. For verification purposes, termination becomes effective only once the agent has notice of the death, per the Restatement's notice-based rule, not at the biological instant of death. Evidence should record the death event and the notice timestamp, not merely a manual revocation.

**What a naive system gets wrong.** A revoke-only system waits for an explicit revocation record and misses that death is a self-executing terminating event. A system can also over-read "durable" as blanket death-immunity, when durability is scoped only to surviving incapacity, not death. Every power of attorney, durable or not, ends at death.

**Related invariant/open question.** L1, L10. Termination happens at a factual moment (death) under a notice-effective rule, not an ancestor-revocation record. The scope of "durable" (incapacity-survival only, never death-survival) is a distinction no invariant states, and a naive system easily over-generalizes it.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-001-a` to `LPE-A-001-k` (11) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

---

#### LC-A-003. An unmet contingency is indeterminate, not simply "not yet started"

**Situation.** A delegation is marked effective only once a stated contingency, commonly incapacity, is verified. No verification artifact exists yet. An agent tries to act under it anyway, and the delegation record parses fine and shows no revocation, so a naive system lets the action through.

**Human analog.** Uniform Power of Attorney Act § 109: a power of attorney can be made effective upon a future contingency, with the principal designating who verifies it occurred. [UPOAA (2006) §109, hosted by the Mississippi Secretary of State](https://www.sos.ms.gov/content/documents/pol_res/power%20of%20attorney/5upoaa_final_may08.pdf): "A power of attorney is effective when executed unless the principal provides in the power of attorney that it becomes effective at a future date or upon the occurrence of a future event or contingency."

**What should happen.** The delegation is indeterminate, not valid and not simply "absent," until an acceptable verification artifact from an authorized verifier role is attached. Acting on it before that point is an unauthorized act, not a borderline one.

**What a naive system gets wrong.** Treating an unmet contingency the same as "not yet started, will begin automatically," and letting the agent act early because the record parses and nothing has been revoked.

**Related invariant/open question.** L7 covers unknown revocation state. This is the mirror problem at issuance, unknown activation state, which none of L1-L12 name as its own category, and it needs a defined verifier role, not just any evidence.

**Status:** proposed.

**Fixture:** `activation-not-established` / `AX-02-no-attestation-not-established` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/activation-not-established/README.md)

Variants: A-004 (the verifier's role has to match the specific contingency sub-type claimed, unavailability rather than impairment, not merely be an authorized verifier), C-004 (a conditional, event-extendable expiry window rather than a conditional, unverified activation).

---

#### LC-A-005. Divorce automatically revokes a spouse's designation as agent, without any separate revocation act

**Situation.** A delegation names the principal's spouse as delegate by relationship-role rather than by a fresh grant. The underlying marriage ends by final decree.

**Human analog.** California Probate Code §4154(a), [law.onecle.com](https://law.onecle.com/california/probate/4154.html): "If after executing a power of attorney the principal's marriage to the attorney-in-fact is dissolved or annulled, the principal's designation of the former spouse as an attorney-in-fact is revoked."

**What should happen.** The delegation to the former spouse is revoked automatically at the decree date, with no separate revocation act required, and does not reappear unless the same two people remarry.

**What a naive system gets wrong.** A system that only revokes on an explicit revocation event in its own log keeps verifying a delegation valid because nobody clicked revoke, even though the relationship it depends on has legally ended.

**Related invariant/open question.** None of L1-L12 model authority whose validity depends on an external relationship-status record (a marriage) rather than principal action, ancestor revocation, expiry, or suspension.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-005-a` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

---

#### LC-A-006. The event that revokes a spousal delegation is jurisdiction-dependent: filing, not just a final decree, can be the trigger

**Situation.** A petition for dissolution of marriage is filed but no decree has issued. The jurisdiction's statute ties revocation to filing, not to the decree.

**Human analog.** Florida Statutes §709.2109(2)(b), [flsenate.gov](https://www.flsenate.gov/Laws/Statutes/2023/709.2109): an agent's authority terminates when "An action is filed for the dissolution or annulment of the agent's marriage to the principal or for their legal separation, unless the power of attorney otherwise provides."

**What should happen.** In this jurisdiction, the delegation must be treated as revoked from the filing date onward, even though the marriage is not legally over and the parties might reconcile before any decree.

**What a naive system gets wrong.** A system that hardcodes "divorce revokes spousal authority" against only a decree event misses that some jurisdictions move the trigger to filing, a much earlier and more provisional fact, and keeps the delegation valid through a period the law already treats as revoked.

**Related invariant/open question.** Same underlying gap as LC-A-005, sharpened: the trigger fact and its evidentiary threshold (petition filed vs. decree entered) differ by jurisdiction, and jurisdiction-dependent trigger timing is not something any invariant addresses.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-006-a`, `LPE-A-006-b`, `LPE-A-006-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

---

#### LC-A-008. Purpose exhaustion ends authority once an authenticated record shows the purpose was met, not once the agent subjectively decides it was

**Situation.** A delegation authorizes an agent to buy one replacement compressor for a specific piece of equipment. An authenticated maintenance record later shows the compressor was purchased and installed. The delegation itself carries no use-count limit or expiry, and nothing revoked it.

**Human analog.** Restatement (Third) of Agency §3.09, [reproduced text, staff.washington.edu](https://staff.washington.edu/djdrake/RESt-Agency.doc): "An agent's actual authority terminates upon the occurrence of circumstances on the basis of which the agent should reasonably conclude that the principal no longer would assent to the agent's taking action."

**What should happen.** Once a verifier can establish, from an authenticated record rather than the agent's own state of mind, that the delegation's stated purpose has been fulfilled, the grant is exhausted for that purpose. A further compressor purchase under the same authority is unauthorized, even though the grant's own terms never stated a use-count or expiry.

**What a naive system gets wrong.** Restatement §3.09 as literally written turns on the agent's own reasonable belief, which a verifier cannot check from records. Treating the delegation as good until an explicit revocation or expiry fires misses that a record-verifiable purpose-completion event can end authority as surely as expiry does, once completion is a checkable fact rather than a judgment call.

**Related invariant/open question.** L10 distinguishes expiry from revocation but assumes a stated time, use count, or budget bound. This is purpose exhaustion where the bound was never explicitly encoded, only implied by the grant's stated reason, and needs a verifier that checks "purpose fulfilled" against an authenticated record, not against the agent's intent.

**Status:** proposed.

**Fixture:** `lifecycle-purpose-exhaustion` / `PXE-01-accept-first-purchase-tuesday`, `PXE-02-observe-authenticated-completion`, `PXE-03-reject-second-purchase-wednesday` (candidate, not yet merged)

---

#### LC-A-009. A fiduciary who feloniously kills the principal forfeits the appointment retroactively, not merely from the date of the finding

**Situation.** A named agent, trustee, or executor is later adjudicated to have intentionally and feloniously killed the principal. The fiduciary's own delegations and any downstream chains it issued are in question.

**Human analog.** Uniform Probate Code §2-803, as enacted at Mass. Gen. Laws c.190B §2-803, [malegislature.gov](https://malegislature.gov/Laws/GeneralLaws/PartII/TitleII/Chapter190B/Section2-803): the statute "revokes any revocable...nomination of the killer in a governing instrument, nominating or appointing the killer to serve in any fiduciary or representative capacity, including as personal representative, executor, trustee, or agent." The statute treats the revoked nomination "as if the killer predeceased the decedent."

**What should happen.** The fiduciary's authority is treated as void from the relevant appointment, not merely revoked going forward from the finding. Any role or continuing benefit the wrongdoer would have held is stripped as though it never took effect for them, and downstream authority the killer issued while nominally in the role stands on the same footing as authority from someone who never held it. The finding is a new record that references the original appointment. It does not rewrite the appointment receipt, and it does not erase evidence of acts taken before the finding.

**What a naive system gets wrong.** A system that only supports forward-looking revocation cannot express that a bad actor's authority should be treated as never having validly existed once the underlying wrongdoing is established, and has no way to represent "predeceased for this purpose" as a retroactive recharacterization rather than a fresh revocation event.

**Related invariant/open question.** L3 says reauthorization never reverses a revocation. This is the opposite direction: a rule that retroactively voids authority for cause, a mechanism none of L1-L12 provide.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-009-a`, `LPE-A-009-b`, `LPE-A-009-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

---

#### LC-A-010. A court-appointed guardian or conservator can limit, suspend, or terminate an existing agent's authority from outside the delegation chain entirely

**Situation.** A principal has an existing, otherwise-valid durable delegation. A court later appoints a conservator or guardian for the principal, an authority that was never a party to the original delegation.

**Human analog.** Uniform Power of Attorney Act (2006) §108, as enacted at RCW 11.125.080, [wa-law.org](https://wa-law.org/rcw/11_probate_and_trust_law/11.125_uniform_power_of_attorney_act.html): "The power of attorney is not terminated and the agent's authority continues, subject to the provisions of RCW 11.130.335(1) and 11.130.435(4), unless limited, suspended, or terminated by the court."

**What should happen.** The original delegation is not automatically voided by the court appointment. It keeps running unless and until the court, which sits outside the delegation chain and was never the issuer, exercises its own power to limit, suspend, or terminate it. Both authorities were, and can remain, valid in their own right.

**What a naive system gets wrong.** A system that assumes only the original principal or its explicit successor chain can affect a delegation has no way to let a court-level authority intervene on a delegation it did not issue and is not a party to, so it either ignores the guardian's action or wrongly treats guardian appointment itself as an automatic revocation.

**Related invariant/open question.** None of L1-L12 model an external authority with override power that sits outside the issuing chain. Lifecycle standing (who may suspend or terminate an artifact) here belongs to a party the artifact's own issuance never named.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-010-a`, `LPE-A-010-b`, `LPE-A-010-c`, `LPE-A-010-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

---

#### LC-A-012. The "coupled with an interest" survival-past-death rule is dictum: the leading case actually held the power at issue died with the principal

**Situation.** A delegation is issued specifically to secure a lender's interest in collateral rather than as an ordinary convenience grant. The principal dies. The delegate wants to still act under the delegation to reach the collateral.

**Human analog.** Hunt v. Rousmanier's Administrators, 21 U.S. (8 Wheat.) 174 (1823). [Cornell LII](https://www.law.cornell.edu/supremecourt/text/21/174). The court's actual holding on the power at issue: "The power given in this case, is a naked power, not coupled with an interest, which, though irrevocable by Rousmanier himself, expired on his death." The often-cited general rule is dictum in the same opinion: "If a power be coupled with an 'interest,' it survives the person giving it, and may be executed after his death."

**What should happen.** A verifier applying "coupled with an interest survives death" has to check that the delegate holds a genuine interest in the underlying thing itself, not merely an interest in exercising the power or in its proceeds, because Hunt v. Rousmanier's own facts, a bare power to sell someone else's pledged collateral with no ownership stake in it, failed that test and died with the principal anyway. The survival rule is real (later courts and treatises adopted the dictum as governing), but it is a narrow, fact-specific exception, not a default for anything security-flavored.

**What a naive system gets wrong.** Reading the opinion's often-quoted general rule as its holding, and automatically flagging any collateral-adjacent or security-related delegation as death-surviving. The case's actual disposition is a warning: most delegations that look like they should qualify do not, on close reading, and default to dying with the principal like any other naked power.

**Related invariant/open question.** None named. Every death-terminates-authority case in this corpus assumes the survival exception applies cleanly once claimed. This is the one place the corpus's own source shows a party trying and failing to claim it, which matters for how narrowly a verifier should read an `interest_coupled=true` flag.

**Status:** proposed. (source_type: law)

**Fixture:** `lifecycle-principal-events` / `LPE-A-012-a`, `LPE-A-012-b`, `LPE-A-012-c`, `LPE-A-012-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

Variants: A-002 (same pattern, a per-delegation flag overriding a default termination rule, but for incapacity and a durability flag rather than death and a coupled-with-interest flag).

---

#### LC-A-016. Some replacement authority is pre-committed at issuance time, not issued fresh after the fact

**Situation.** A single delegation instrument names a primary delegate and an ordered list of successors. The primary exits: dies, resigns, becomes incapacitated. The next-in-line successor should be able to act under the same original grant, with no new document and no action required from the principal at the moment of handoff.

**Human analog.** The Uniform Power of Attorney Act's successor-agent provision. [UPOAA (2006) §111, hosted by the Mississippi Secretary of State](https://www.sos.ms.gov/content/documents/pol_res/power%20of%20attorney/5upoaa_final_may08.pdf): "A principal may designate one or more successor agents to act if an agent resigns, dies, becomes incapacitated, is not qualified to serve, or declines to serve."

**What should happen.** The successor's authority derives from the same original delegation, at the scope and terms that instrument already set, activated by the primary's exit. It is not a new grant, and it needs nothing from the principal at handoff time.

**What a naive system gets wrong.** A system built around "replacement authority always means a fresh grant from a currently-authorized principal" (the L3/L4 pattern) has no slot for succession pre-committed inside a single instrument. It either treats the successor as unauthorized until a new grant appears, or wrongly treats the successor as inheriting the primary's entire personal delegation tree rather than just this one instrument.

**Related invariant/open question.** L3 and L4 assume replacement authority is issued fresh, after the fact, by whoever currently holds authority. This is a third pattern, authority pre-committed at issuance for a defined contingency, that neither invariant names.

**Status:** proposed.

**Fixture:** `lifecycle-principal-events` / `LPE-A-016-a`, `LPE-A-016-b`, `LPE-A-016-c`, `LPE-A-016-d`, `LPE-A-016-e`, `LPE-A-016-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-events/README.md)

Variants: A-011 (a pre-named successor trustee taking control of a trust that itself persists, rather than a successor-agent list under a power of attorney), C-013 (the pre-committed replacement is a pre-equalized peer inside a fixed two-person crew rather than a named successor).

---

### Fiduciary succession

#### LC-A-019. Co-trustees act by majority when they cannot reach unanimity, and a vacancy does not have to be filled before the remainder can act

**Situation.** A single authority record names three co-equal holders. Two agree on an action and one dissents, or one holder has dropped out entirely.

**Human analog.** Uniform Trust Code §703, as enacted at Maine Title 18-B §703, [legislature.maine.gov](https://legislature.maine.gov/statutes/18-B/title18-Bsec703.html): "Cotrustees who are unable to reach a unanimous decision may act by majority decision." And: "If a vacancy occurs in a cotrusteeship, the remaining cotrustees may act for the trust."

**What should happen.** The action proceeds on majority approval among current holders. The departure of one holder does not freeze the authority or require a formal backfill before the remaining holders can act.

**What a naive system gets wrong.** A system built around single-principal or unanimous-multi-principal models either blocks all action the moment any one co-holder is unavailable, or wrongly requires a replacement to be seated before anything else can happen, when the law explicitly lets the remainder carry on.

**Related invariant/open question.** None of L1-L12 model quorum rules for co-holders of one authority record, whether for disagreement (majority) or for vacancy (remainder carries on without backfill).

**Status:** proposed.

**Fixture:** `lifecycle-fiduciary-succession` / `LFS-A-019-a`, `LFS-A-019-b`, `LFS-A-019-c`, `LFS-A-019-d`, `LFS-A-019-e`, `LFS-A-019-f`, `LFS-A-019-g`, `LFS-A-019-h` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-fiduciary-succession/README.md)

Variants: A-017 (default solo-authorization rule, joint vs. several, for co-agents acting alone under one instrument, rather than a majority-decision-on-disagreement-plus-vacancy rule for co-trustees).

---

#### LC-A-022. A temporary administrator's authority is scoped to preservation and ends automatically the instant the underlying dispute resolves

**Situation.** A will is being contested in court. A temporary administrator (administrator pendente lite) is appointed to keep the estate's assets from decaying while the dispute over who the real successor is gets resolved.

**Human analog.** [Cornell LII Wex, "administrator pendente lite"](https://www.law.cornell.edu/wex/administrator_pendente_lite): the role exists to "manage an estate and probate a will during the pendency of the dispute," and: "The resolution of the legal dispute terminates the administration."

**What should happen.** This delegate's grant should be scoped to preservation-only actions from the start, distribution and similar acts excluded, and its authority should end automatically and immediately when the underlying dispute resolves and a permanent successor is appointed, with no separate revocation step needed.

**What a naive system gets wrong.** A system with only one shape of "successor authority" either gives the temporary caretaker full successor powers, letting it take actions that would prejudice the pending dispute, or fails to auto-terminate it at resolution, requiring someone to remember to revoke it.

**Related invariant/open question.** L10 distinguishes expiry from revocation generally. This is a narrower authority class whose scope is intentionally restricted relative to normal successor authority and whose expiry condition is an external legal event (dispute resolution), not a fixed clock or an ancestor's state.

**Status:** proposed.

**Fixture:** `lifecycle-fiduciary-succession` / `LFS-A-022-a`, `LFS-A-022-b`, `LFS-A-022-c`, `LFS-A-022-d`, `LFS-A-022-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-fiduciary-succession/README.md)

---

#### LC-A-023. Ratification retroactively authorizes a prior unauthorized act, but cannot be used to defeat a third party's intervening rights, and it is all-or-nothing

**Situation.** An agent takes an out-of-scope action. The principal later approves it after the fact. Between the original act and the approval, an unrelated third party acquires a real interest in the same subject matter in good faith. Separately: a principal tries to accept only the beneficial half of an out-of-scope act, or attempts to ratify while lacking capacity.

**Human analog.** Restatement (Third) of Agency §4.02, [reproduced text, staff.washington.edu](https://staff.washington.edu/djdrake/RESt-Agency.doc): ratification "retroactively creates the effects of actual authority," except that it does not diminish "the rights or other interests of persons, not parties to the transaction, that were acquired in the subject matter prior to the ratification." Two further structural rules from the same source: §4.07, "A ratification is not effective unless it encompasses the entirety of an act, contract, or other single transaction". §4.04, a person may ratify only if they "had capacity...at the time of ratifying the act."

**What should happen.** Ratification makes the agent's original act retroactively authorized as between principal and agent, but it cannot claw back or defeat an intervening third party's independently acquired interest. Ratification is also all-or-nothing: a principal cannot keep the favorable part of a single integrated act and disavow the rest, and a ratification attempt from a principal who currently lacks capacity does not take effect regardless of how clearly it is expressed.

**What a naive system gets wrong.** A system that supports retroactive ratification at all tends to treat it as a clean rewrite of history that overrides anything in between, including a legitimate intervening claim ratification was never meant to reach. A system implementing ratification as a generic approve-this-record operation also risks letting a principal cherry-pick favorable sub-effects, or accepting a ratification signal without checking the principal's capacity at the moment of ratifying.

**Related invariant/open question.** L3 says reauthorization is a new grant and never reverses revocation. Ratification is a third mechanism: retroactive validation of something never authorized in the first place, bounded to protect intervening third-party rights, and constrained by atomicity and a capacity check at the ratification moment, none of which any invariant states.

**Status:** proposed.

**Fixture:** `lifecycle-fiduciary-succession` / `LFS-A-023-a` to `LFS-A-023-j` (10) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-fiduciary-succession/README.md)

Variants: A-021 (probate relation-back doctrine: a personal representative's beneficial pre-appointment acts are automatically validated back to the date of death once appointed, distinct from a principal's discretionary ratification bounded by intervening third-party rights). A-024 (the atomicity and capacity-at-ratification constraints, folded directly into this entry's own write-up rather than kept as a separate case).

---

### Third-party reliance and notice

#### LC-A-027. A verifier's internal "chain is void" and a relying party's protected reliance are two separate facts, not one boolean

**Situation.** A principal terminates an agent's actual authority. A third party who previously dealt with that agent has not been told. The delegation is dead for chain-verification purposes the instant it's terminated, but from the third party's side, nothing has changed yet.

**Human analog.** Restatement (Third) of Agency § 3.11. [University of Washington course reproduction of the Restatement text](https://staff.washington.edu/djdrake/RESt-Agency.doc), confirmed locally against the section number: "The termination of actual authority does not by itself end any apparent authority held by an agent."

**What should happen.** From the counterparty's perspective, reliance on the agent's apparent authority can remain reasonable, and protected, until the counterparty actually has notice of the termination, even though the delegation itself is already dead for chain-verification purposes. These are two different outcomes, not one.

**What a naive system gets wrong.** Answering only "is the chain currently valid" and treating that as the whole answer. It ignores that a relying party's protection can turn on a separate fact, whether notice actually reached them, collapsing two different questions into one boolean.

**Related invariant/open question.** L7 is about an indeterminate revocation answer reaching a verifier. This is different: a determinate revocation that a specific third party has not yet been notified of, a reliance-protection question about the third party's own knowledge state. OPEN-QUESTIONS.md's "notice and relying parties" section names this as unresolved and explicitly does not assume agency-law doctrines transfer to AI agents.

**Status:** proposed.

**Fixture:** `lifecycle-third-party-reliance-notice` / `TPR-A-027-a`, `TPR-A-027-b`, `TPR-A-027-c`, `TPR-A-027-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-third-party-reliance-notice/README.md)

Variants: A-029 (adds a statutory presumption of genuineness for good-faith acceptance of an acknowledged instrument, rather than the general common-law notice cutoff), A-032 (a duty to inquire that narrows reliance protection when the transaction is facially inconsistent with the delegation's visible scope, the opposite direction from the general rule).

---

#### LC-A-028. Cutting off apparent authority takes more than one kind of notice: actual notice for known prior counterparties, publication for strangers

**Situation.** A revocation event needs to be made effective against two different classes of relying counterparty: those with a prior transaction history with the now-terminated delegate, and those who have never interacted with it before.

**Human analog.** [USLegal, "Duration and Termination of Agency"](https://agency.uslegal.com/duration-and-termination-of-agency/): "Actual notice must be brought home to former customers who have dealt with the agency more directly, while notice by publication will be sufficient as to other persons."

**What should happen.** A single public revocation broadcast is enough to cut off protected reliance for counterparties with no prior history. A counterparty with an established prior relationship to the delegate needs something closer to individualized notice before their reliance stops being reasonable.

**What a naive system gets wrong.** A system that publishes one revocation record to one public registry and calls notice satisfied for everyone treats a known repeat counterparty exactly like a first-time stranger, when the law asks more of the principal for the counterparty it has an established relationship with.

**Related invariant/open question.** No invariant differentiates the evidentiary bar for cutting off reliance based on the relying party's relationship history with the agent. This is a two-tier notice-sufficiency rule the framework does not currently express, adjacent to LC-A-027's general notice-cutoff timing rule but about who counts as adequately notified, not when.

**Status:** proposed.

**Fixture:** `lifecycle-third-party-reliance-notice` / `TPR-A-028-a`, `TPR-A-028-b`, `TPR-A-028-c`, `TPR-A-028-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-third-party-reliance-notice/README.md)

---

#### LC-A-033. A newer delegation instrument does not automatically revoke an older one absent an express revocation clause

**Situation.** A principal issues a second, broader or updated delegation to the same or a different agent, without the new delegation containing any explicit clause revoking the earlier one.

**Human analog.** Florida Statutes §709.2110, [flsenate.gov](https://www.flsenate.gov/Laws/Statutes/2023/709.2110): "the execution of a power of attorney does not revoke a power of attorney previously executed by the principal," except through subsequent written revocation.

**What should happen.** Both delegations should be treated as independently valid and checked on their own terms, per L5, unless the newer instrument contains an express revocation clause naming the older one. The mere existence of a newer instrument is not itself a revocation event.

**What a naive system gets wrong.** A system defaults to "newest wins," silently treating the most recently issued delegation as having superseded and revoked any earlier one for the same principal, even when nothing in either instrument says so, potentially cutting off a still-intended, still-valid grant.

**Related invariant/open question.** L5 states independent chains are not combined. This is the adjacent but distinct failure mode of assuming a newer chain implicitly kills an older one, a wrong reason to invalidate rather than a wrong reason to combine.

**Status:** proposed.

**Fixture:** `lifecycle-third-party-reliance-notice` / `TPR-A-033-a`, `TPR-A-033-b`, `TPR-A-033-c`, `TPR-A-033-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-third-party-reliance-notice/README.md)

---

### Organization events

#### LC-B-012. A merger can vest authority in a new principal by operation of law, with no issuance event at all

**Situation.** Company A merges into Company B under state corporate law. The instant the merger takes effect, Company B, not Company A, holds every power Company A's officers held, without Company B's officers ever issuing anything. A delegation chain that depended on Company A's authority now needs to resolve to Company B, automatically.

**Human analog.** Delaware General Corporation Law § 259: on a merger's effectiveness, the surviving corporation is automatically vested with the constituent corporations' rights, privileges, powers, and franchises. [Delaware Code](https://delcode.delaware.gov/title8/c001/sc09/index.html): "possessing all the rights, privileges, powers and franchises as well of a public as of a private nature."

**What should happen.** Unlike an employee's departure, where continuity legitimately requires a fresh grant from a currently authorized principal, statutory merger vests authority automatically and instantly by law. A framework that demands an explicit new grant before honoring the chain under the surviving entity produces a false denial of authority the law says already exists.

**What a naive system gets wrong.** Applying the "successor must issue a fresh grant" pattern literally to a statutory merger. The law performs the succession without anyone issuing anything. Treating the old, now-nonexistent corporation as still the operative principal is equally wrong in the other direction.

**Related invariant/open question.** L2, L3, and L4 all assume a human or organizational principal actively issues a new grant to establish replacement authority. Statutory merger is a real, common succession pathway with no issuance event at all, which none of them contemplate.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-012-a`, `LC-B-012-b`, `LC-B-012-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

Variants: C-001 (root-of-chain succession, where no superior issuer could ever exist, tests the same vesting-without-issuance mechanism as a merger vesting a new organizational principal).

---

#### LC-B-013. Automatic corporate-law vesting does not reach the technical delegation layer

**Situation.** An acquisition closes as a merger. The target's corporate authority vests in the acquirer by operation of law at closing, but the target's technical systems, API keys, service accounts, delegation roots issued by the target's own former officers, are untouched by the corporate-law vesting event. A pricing agent holds a delegation chain rooted in the target's former CFO's signing key, and nobody at the acquirer has issued the agent anything.

**Human analog.** Delaware General Corporation Law section 259's automatic vesting. [Delaware Code](https://delcode.delaware.gov/title8/c001/sc09/index.html): "all and singular, the rights, privileges, powers and franchises of each of said corporations, and all property, real, personal and mixed... shall be vested in the corporation surviving."

**What should happen.** The agent's chain is not automatically valid just because the corporate entity behind it now legally has authority through the acquirer. The technical delegation layer needs its own succession event, a fresh grant from someone at the acquirer, even though no such event is legally required at the corporate layer.

**What a naive system gets wrong.** Assuming that because statutory merger vesting is automatic, the delegation graph updates automatically too, conflates two different layers. Corporate succession is instantaneous and requires no issuance. Delegation and credential succession is never automatic and always requires an issuance event from a principal who currently holds authority.

**Related invariant/open question.** Builds on the already-verified LC-B-012 (statutory merger vesting) by showing the automatic-vesting mechanism does not reach the delegation or credential layer at all, so a system that correctly re-points the corporate principal record can still wrongly treat orphaned agent delegations as live.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-013-a`, `LC-B-013-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

#### LC-B-016. A dissolution statute can automatically narrow the scope of authority that remains otherwise valid

**Situation.** A sales agent held a delegation to negotiate and sign new customer contracts. The company dissolves and enters its statutory winding-up period. The officer who granted the agent's authority still, technically, holds residual authority, but that authority no longer covers signing new sales contracts, only settling existing obligations.

**Human analog.** Delaware General Corporation Law section 278. [Delaware Code](https://delcode.delaware.gov/title8/c001/sc10/index.html): "shall nevertheless be continued... bodies corporate for the purpose of prosecuting and defending suits... and of enabling them gradually to settle and close their business... but not for the purpose of continuing the business for which the corporation was organized."

**What should happen.** This is neither revocation, the officer's authority to act at all does not end, nor unchanged continuation. The scope of what that authority covers shrinks automatically by operation of the dissolution statute, without anyone issuing a new grant or a revocation for the sales-contract scope specifically.

**What a naive system gets wrong.** A binary model with only "authority exists" or "authority revoked" cannot represent a statute automatically narrowing what an existing, unrevoked authority covers. It either lets the agent keep signing new contracts, or wrongly zeroes out authority that genuinely continues for winding-up purposes.

**Related invariant/open question.** None of L1-L12 models an external legal-status change automatically narrowing the scope of an authority that remains otherwise valid. L8's restricted state is the closest analog but is framed around validity, not automatic scope contraction triggered by an entity-status change.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-016-a`, `LC-B-016-b`, `LC-B-016-c`, `LC-B-016-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

#### LC-B-028. Authorization has to be rechecked right up to the moment of final execution, not just at issuance

**Situation.** A payment instruction is validly authorized and submitted. Minutes later, the authorizing officer discovers a problem and issues a stop instruction. Whether the stop works depends entirely on whether the paying bank has already acted on the original instruction. An identical stop instruction can succeed or do nothing, purely based on timing.

**Human analog.** UCC § 4-403, a customer's right to stop payment. [Cornell LII](https://www.law.cornell.edu/ucc/4/4-403): "A customer may stop payment of any item drawn on the customer's account by an order to the bank received at a time and in a manner that affords the bank a reasonable opportunity to act on it."

**What should happen.** The system must recheck for a stop or cancellation right up to the moment of final execution, not accept the original authorization as settled once issued. The recheck window has a hard boundary, the receiving institution's own action on the item, after which the same stop instruction that would have worked a moment earlier does nothing.

**What a naive system gets wrong.** Treating "validly authorized at issuance" as sufficient and only checking for a stop at that moment, rather than continuously up to execution. That executes payments the customer had every right to stop, purely because the stop-check happened too early.

**Related invariant/open question.** A concrete, narrowly-timed instantiation of L6 (an earlier approval is not current authority), adding the detail that the recheck window has a hard, event-defined boundary rather than a fixed duration.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-028-a`, `LC-B-028-b`, `LC-B-028-c`, `LC-B-028-d`, `LC-B-028-e`, `LC-B-028-f`, `LC-B-028-g`, `LC-B-028-h` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

#### LC-B-029. A receiving bank's acceptance is the hard boundary after which a mid-flight authority change no longer stops the order

**Situation.** A treasury agent submits a payment order under a valid delegation. The authorizing principal's authority is revoked minutes later. If the receiving bank has not yet accepted the payment order, the revocation stops it from settling. If the bank already accepted it, the order proceeds regardless of the revocation, unless the bank itself agrees to unwind it.

**Human analog.** UCC 4A-211's acceptance boundary. [Cornell LII](https://www.law.cornell.edu/ucc/4A/4A-211): "After a payment order has been accepted, cancellation or amendment of the order is not effective unless the receiving bank agrees or a funds-transfer system rule allows cancellation or amendment without agreement of the bank."

**What should happen.** AUTHORITY-LIFECYCLE.md names "an action already in flight when authority changes" as an operational case it has to handle, without resolving it. This supplies a concrete resolution for one instrument type: the receiving institution's acceptance is the hard boundary. Before it, revoking the authorizing delegation stops the order. After it, the order proceeds independent of what the delegation graph says.

**What a naive system gets wrong.** Assuming revocation automatically halts any payment order already submitted under it ignores that acceptance gives the order a revocation-proof effect. Assuming revocation never matters for in-flight orders ignores that unaccepted orders remain fully stoppable.

**Related invariant/open question.** Distinct from the already-verified LC-B-028 (stop-payment), which is a customer-initiated cancellation decision under L6's recheck principle. This is the underlying delegated authority itself changing mid-flight, the specific unresolved operational case AUTHORITY-LIFECYCLE.md names.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-029-a` to `LC-B-029-i` (9) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

### Legal and regulatory events

#### LC-B-007. Ratification is a new record that reaches backward, not a rewrite of the original

**Situation.** An agent executes a transfer using a delegation that the named principal never actually granted. The principal later learns of this and decides the transfer was fine, ratifying it rather than treating it as fraud.

**Human analog.** UCC 3-403(a)'s ratification rule. [Cornell LII](https://www.law.cornell.edu/ucc/3/3-403): "An unauthorized signature may be ratified for all purposes of this Article."

**What should happen.** Ratification is a new record that reaches backward to treat a past act as authorized at the time it happened. It does not rewrite the original unauthorized-signature record. A verifier needs both the original record and the later ratification that references it to reconstruct what happened.

**What a naive system gets wrong.** A framework with only "grant" and "revoke" as authority-creating and authority-ending events has no way to represent a past, technically-unauthorized act now treated as authorized. It either keeps flagging the historical act as unauthorized forever, or fabricates a backdated grant that breaks issuance-time integrity checks elsewhere in the chain.

**Related invariant/open question.** L3 says a fresh grant is prospective and never reverses or re-parents a revocation. Ratification runs the opposite direction, a real, named doctrine the model needs as a distinct third category alongside grant and revoke.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-007-a`, `LRE-B-007-b`, `LRE-B-007-c`, `LRE-B-007-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-008. Authority can end completely, instantly, and outside the delegation system entirely

**Situation.** A bank's officer authority does not merely get revoked. A federal receiver is appointed and by statute steps into every power that officer held, the instant the appointment takes effect, with zero notice to the delegation system that was relying on that officer's authority.

**Human analog.** 12 U.S.C. § 1821(d), under which the FDIC as receiver of a failed bank succeeds by operation of law to all rights and powers of the institution and its officers. [Cornell LII](https://www.law.cornell.edu/uscode/text/12/1821): "The Corporation shall, as conservator or receiver, and by operation of law, succeed to all rights, titles, powers, and privileges of the insured depository institution."

**What should happen.** Every delegation rooted in the former officer's authority is void from the moment the receiver is appointed, whether or not the bank's own systems ever recorded a revocation. No replacement authority exists until the new principal (the receiver) issues one.

**What a naive system gets wrong.** A system that expects the terminating event to show up as a revocation record in the infrastructure it monitors sees nothing, because the ancestor authority ended through an external legal fact with no corresponding artifact anywhere in the delegation graph.

**Related invariant/open question.** A harder-edged instance of L1 and L2, where the "ancestor" whose end triggers invalidation is not an APS artifact or even a company-internal record, but a statute taking effect the instant a regulator acts.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-008-a`, `LRE-B-008-b`, `LRE-B-008-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-009. A legal event with instantaneous effect can disqualify an action before anyone could have checked for it

**Situation.** A creditor's collections agent initiates a garnishment moments after a debtor's Chapter 11 petition is filed, a fact that will not reach any public record the agent could query for hours.

**Human analog.** 11 U.S.C. 362(a), the automatic stay. [Cornell LII](https://www.law.cornell.edu/uscode/text/11/362): "a petition filed under section 301, 302, or 303 of this title...operates as a stay, applicable to all entities."

**What should happen.** The stay takes effect the instant the petition is filed, not from the moment it becomes discoverable. Courts have treated an act taken in violation of the stay as void in most circuits and voidable in some, so a verifier's answer needs to say which its jurisdiction assumes, rather than assert one outcome uniformly.

**What a naive system gets wrong.** L7 says an indeterminate revocation answer should not be treated as active. This runs the opposite direction: a legal fact that is actively disqualifying at a moment before it was checkable at all. A system built only around L7 might treat the action as valid because nothing was checkable in time, when the stay already applied from the instant of filing.

**Related invariant/open question.** None of L1-L12 names a legal event with instantaneous effect and no resolver anyone could have queried in time. Distinct from L7's checkable-but-stale resolver problem.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-009-a`, `LRE-B-009-b`, `LRE-B-009-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-010. A court-supervised filing can add an approval gate without pausing the underlying authority

**Situation.** A company files Chapter 11 and continues operating as debtor in possession. A procurement agent operates under the CFO's authority the day after the filing exactly as before, but a purchase order above a certain size, which the CFO could sign alone pre-petition, now needs the bankruptcy court's approval before the same CFO's signature has effect.

**Human analog.** 11 U.S.C. 1107, the debtor-in-possession's trustee-equivalent powers. [Cornell LII](https://www.law.cornell.edu/uscode/text/11/1107): "a debtor in possession shall have all the rights... and powers, and shall perform all the functions and duties... [s]ubject to any limitations on a trustee serving in a case under this chapter."

**What should happen.** This is a live example of the restricted state L8 names as distinct from both suspension and revocation: authority continues in reduced form under an added court-approval gate, without any descendant delegation needing to pause.

**What a naive system gets wrong.** A binary revoked/not-revoked model forces treating the filing as either full continuity, missing that some transactions now need court approval that didn't before, or full revocation, which is wrong since the CFO's day-to-day authority for ordinary transactions stays intact.

**Related invariant/open question.** L8's proposed restricted state, illustrated here at the level of an entire office's authority for an extended period, based on an external legal filing rather than one delegation being paused.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-010-a`, `LRE-B-010-b`, `LRE-B-010-c`, `LRE-B-010-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-011. A restriction imposed by an external filing needs an equally external release trigger

**Situation.** The procurement agent restricted to a court-approval gate during the Chapter 11 case reverts to the CFO's ordinary unrestricted authority for those transaction sizes on the date the reorganization plan's confirmation takes effect.

**Human analog.** 11 U.S.C. 1141(b), vesting on plan confirmation. [Cornell LII](https://www.law.cornell.edu/uscode/text/11/1141): "Except as otherwise provided in the plan or the order confirming the plan, the confirmation of a plan vests all of the property of the estate in the debtor."

**What should happen.** A restriction imposed by an external legal process ends on a specific, legally defined trigger, plan confirmation, rather than through any action inside the delegation graph. The release condition has to resolve against that external record, not an internal revocation or grant action.

**What a naive system gets wrong.** A system that only records "restricted since date X" with no defined end condition will not know to lift the restriction on confirmation unless the release trigger is itself modeled as tied to the external legal process.

**Related invariant/open question.** Pairs with LC-B-010 to show a restriction imposed by an external filing needs an equally external, legally defined release trigger, a mechanism OPEN-QUESTIONS.md's "release from suspension" section flags as unspecified even for the simpler suspension case.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-011-a`, `LRE-B-011-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-017. A legitimate new authority root can come from entirely outside the original chain

**Situation.** A dissolved company's winding-up officers all resign or become unreachable before the wind-up finishes. A court appoints a receiver to complete it. A collections agent needs authority to keep pursuing an outstanding receivable, and the only principal now capable of granting it is the court-appointed receiver, who never appeared anywhere in the agent's original delegation chain.

**Human analog.** Delaware General Corporation Law section 279. [Delaware Code](https://delcode.delaware.gov/title8/c001/sc10/index.html): "appoint 1 or more persons to be receivers, to take charge of the corporation's property, and to collect the debts and property due... with power to prosecute and defend... all such suits as may be necessary."

**What should happen.** A legitimate new chain can start from a principal that was never anywhere in the old chain. The framework's succession model has to accept a root of authority imposed by a court from entirely outside the corporation's own governance, not only a successor traceable back into the prior structure.

**What a naive system gets wrong.** Requiring any replacement grant to trace back into the original chain, or to a recognized role within the corporation's own governance, has no way to accept a court-appointed receiver, whose authority comes from a court order external to the corporation entirely.

**Related invariant/open question.** L2 says a replacement chain stands on its own, but every worked example of L2 involves a successor within the same organization's normal succession path. This tests whether the model tolerates a root of authority with no prior relationship to the delegation graph at all.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-017-a`, `LRE-B-017-b`, `LRE-B-017-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-018. Chain validity and lawfulness to execute are different questions

**Situation.** A payments agent holds a fully valid, unrevoked delegation chain authorizing it to pay a vendor. Treasury adds the vendor to the Specially Designated Nationals list. The agent's chain is still cryptographically valid and unrevoked in every sense the delegation graph tracks. The payment is nonetheless unlawful the instant the designation takes effect.

**Human analog.** OFAC's blocking obligation on designation. [OFAC FAQs](https://ofac.treasury.gov/faqs/topic/1501): "Blocking immediately imposes an across-the-board prohibition against transfers or dealings of any kind with regard to the property."

**What should happen.** Chain validity and lawfulness to execute are different questions. AUTHORITY-LIFECYCLE.md's own external-restriction concept names a sanction as its paradigm case: a block from outside the grant chain that can stop some effects while the grant itself stays valid. A gateway needs an independent sanctions-screening check that can block an otherwise fully valid, unrevoked chain.

**What a naive system gets wrong.** A gateway that equates "chain verifies as valid and unrevoked" with "this execution is permitted" authorizes a sanctions violation, because the disqualifying fact never appears as a revocation, suspension, or expiry event inside the delegation graph.

**Related invariant/open question.** The clearest sourced instance of the external-restriction concept AUTHORITY-LIFECYCLE.md already names but does not illustrate. Chain validity is necessary but not sufficient for lawful execution.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-018-a`, `LRE-B-018-b`, `LRE-B-018-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

Variants: B-021 (a listing-based restriction that cascades to unlisted affiliates through an ownership fact, rather than applying only to the named entity).

---

#### LC-B-019. Removing an external block restores execution on an unbroken chain, not through a reauthorization

**Situation.** The vendor from LC-B-018 is removed from the list six months later after a successful delisting petition. The payments agent's original delegation chain, never revoked and cryptographically valid the entire time, can be executed against that vendor again, with zero new grant issued by anyone.

**Human analog.** OFAC's blocking-release rule. [OFAC FAQ 402](https://ofac.treasury.gov/faqs/402): "The property remains blocked unless and until (1) OFAC authorizes the unblocking of or other dealings in the property or (2) OFAC removes the blocked person from the SDN List."

**What should happen.** This contrasts with L3's reauthorization model: L3 says continuity after revocation needs a fresh grant. Delisting removes an external block on a chain that was never revoked in the first place, so there is nothing to reauthorize. The chain's own unbroken validity is what resumes mattering once the external block lifts, though the screening system's own cached "blocked" state still needs to be updated.

**What a naive system gets wrong.** Treating delisting as equivalent to L3 reauthorization, and requiring a fresh grant before resuming payments, is unnecessary, since the underlying delegation was never invalid, only externally blocked.

**Related invariant/open question.** Sharpens LC-B-018 by showing the release side is also outside L3's reauthorization model: a third kind of event, distinct from both grant and reauthorization-after-revocation.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-019-a`, `LRE-B-019-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-022. A real legal exception can supply exactly the basis a completeness claim needs, without needing an open-ended "we keep everything for audit" policy

**Situation.** A former officer who granted a delegation chain exercises their GDPR right to erasure. The company needs to retain the delegation and revocation records naming that officer, to be able to prove, if ever challenged, exactly what authority existed, when it ended, and that the resulting teardown was complete.

**Human analog.** GDPR Article 17(3)(e), the legal-claims exception to the right to erasure. [gdpr-info.eu](https://gdpr-info.eu/art-17-gdpr/): "for the establishment, exercise or defence of legal claims."

**What should happen.** The records survive the erasure request specifically because of the legal-claims exception, not because of a general "we need this for auditing" policy. The retention has an actual legal basis with a defined scope, only what is necessary for legal claims, not an open-ended one.

**What a naive system gets wrong.** A privacy-compliance system that deletes anything containing personal data on any erasure request, with no legal-claims carve-out, deletes exactly the evidence a completeness claim under L12 depends on. Equally wrong: a lifecycle system that assumes it can retain whatever it wants for "evidence" without grounding that in an actual legal basis.

**Related invariant/open question.** OPEN-QUESTIONS.md's teardown-completeness section names "what public commitment can prove closure over a set without exposing private state" as unsettled. GDPR's legal-claims exception is a real, existing legal basis that answers part of that directly.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-022-a`, `LRE-B-022-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-023. Anticipated litigation suspends routine record pruning before any formal process is served

**Situation.** A company's authority-management system normally prunes revocation and delegation records after a fixed retention period. A former employee threatens to sue over their termination and the authority changes that followed it. The company must stop pruning any record touching that employee's authority immediately, before any subpoena or court order is served, because litigation is merely anticipated, not yet filed.

**Human analog.** The Zubulake v. UBS Warburg litigation-hold doctrine. [National Law Review](https://natlawreview.com/article/duty-to-preserve-electronic-evidence): "Once a party reasonably anticipates litigation, it must suspend its routine document retention/destruction policy and put in place a 'litigation hold' to ensure the preservation of relevant documents."

**What should happen.** The trigger for preservation is reasonably anticipating litigation, which is earlier and less formal than a subpoena or court order. A retention policy tied only to formal legal process will prune records the hold doctrine already required keeping.

**What a naive system gets wrong.** A system whose only preservation trigger is a served subpoena or court order will already have destroyed relevant delegation and revocation records by the time formal process arrives, because the duty to preserve attaches earlier.

**Related invariant/open question.** L12's completeness evidence depends on records surviving long enough to prove a teardown was complete. This names a concrete, earlier-firing trigger for suspending routine pruning, distinct from the already-verified LC-B-022 (GDPR legal-claims exception), which answers what overrides an active deletion demand rather than when proactive pruning must stop.

**Status:** proposed.

---

#### LC-B-024. Multiple independent suspensions on the same principal have to be released independently, not cleared by any one of them lapsing

**Situation.** A regulator suspends a representative for a fixed period. Separately, and for an unrelated reason, the representative's own firm has placed them under an internal restriction with no fixed end date. The regulatory suspension period lapses.

**Human analog.** FINRA's suspension regime. [FINRA Rule 8311](https://www.finra.org/rules-guidance/rulebooks/finra-rules/8311): a suspended person may not be associated with a member firm in "any capacity that is inconsistent with the sanction imposed or disqualified status, including a clerical or ministerial capacity."

**What should happen.** Authority should stay paused past the regulatory suspension's end date, because the firm's separate, unrelated restriction has not itself been lifted. The two suspension causes need to be tracked and released independently.

**What a naive system gets wrong.** Representing suspension as a single boolean flag, which incorrectly clears the moment the tracked suspension period ends, restoring authority even though a second, untracked restriction is still active.

**Related invariant/open question.** A concrete regulatory example of L8's proposed suspension, revocation, and restriction distinction, and it directly surfaces OPEN-QUESTIONS.md's "release from suspension" problem, which that document says is "not yet specified."

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-024-a`, `LRE-B-024-b`, `LRE-B-024-c`, `LRE-B-024-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-025. A single revoked license can invalidate every chain that depends on it at once

**Situation.** A payments company runs dozens of independent agent delegation chains, all ultimately resting on the company's money-transmitter license to move customer funds. The state revokes that license for regulatory violations. Every one of those chains loses its authority to transmit money at the same instant, regardless of which specific delegation chain a given agent happens to hold, because the shared dependency is the license itself, not any individual chain link.

**Human analog.** The Georgia Department of Banking and Finance's revocation of Fortress Trust LLC's money transmitter license. [Georgia DBF](https://dbf.georgia.gov/press-releases/2025-11-24/final-order-revocation-money-transmitter-license-issued-fortress-trust): the order found "Fortress Trust is insolvent" and cited its "failing to maintain operational liquidity and resources to fulfill its outstanding obligations."

**What should happen.** A single external event invalidates many otherwise-unrelated chains simultaneously because they share a common, off-graph dependency, the license. A system that models revocation only as a property of individual delegation artifacts has no natural way to represent one external fact invalidating an entire category of otherwise-independent chains at once.

**What a naive system gets wrong.** Modeling license revocation as something that has to be separately propagated to each affected chain risks missing chains whose dependency on the license was never explicitly recorded. The license needs to be a first-class node many chains can depend on, so revoking it invalidates all dependents in one operation.

**Related invariant/open question.** Directly related to OPEN-QUESTIONS.md's "critical revocation" section: revoking a high-level authority can disable a large set of agents. This grounds that question in a real, named regulatory mechanism rather than a hypothetical high-level delegation revocation.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-025-a`, `LRE-B-025-b`, `LRE-B-025-c`, `LRE-B-025-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

Variants: LC-B-001 (a board resolution strips one officer's signing authority through a roster change with no per-agent revocation record, the same off-graph-ancestor principle at the individual-officer scale instead of the shared-license scale), C-023 (a closed, externally maintained statutory eligibility list that no in-chain delegation can expand, rather than a shared licence that many chains already depend on).

---

#### LC-B-026. A third party outside the principal-agent relationship can inject a new approval gate into an otherwise unmodified, valid chain

**Situation.** A company settles a regulatory action. The consent decree does not touch any existing delegation. It adds a new, externally-imposed requirement that a named "responsible employee or official" personally certify a defined category of future reports, for the life of the decree.

**Human analog.** Consent decree practice requiring a named responsible official to certify compliance reports under penalty of law. [SEC EDGAR filing](https://www.sec.gov/Archives/edgar/data/1397516/000119312507093837/dex105.htm): "...which makes any representation concerning the Defendants' compliance or noncompliance with any requirement of this Consent Decree shall be certified by a 'responsible employee or official' of the Defendants."

**What should happen.** The original delegation chain is untouched and still valid, but a transaction in the decree's scope is no longer sufficient on that chain alone. It also needs the named official's separate certification, until the decree's own sunset date.

**What a naive system gets wrong.** A gateway that only re-verifies the original chain has no slot for a chain-external approval requirement injected by an outside party. It keeps authorizing exactly the transactions the decree was meant to catch, because nothing in the delegation itself changed.

**Related invariant/open question.** Structurally close to a dual-control policy, but the source of the added gate is external (a court-approved settlement, not internal risk policy), which none of L1-L12 name as a category. Also the strongest sourced instance found of "policy change" as a family.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-026-a`, `LRE-B-026-b`, `LRE-B-026-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-027. Forfeiture changes who owns the resource, not just who may deal with it for now

**Situation.** A company's account is frozen under a civil restraining order pending litigation. If the freeze is lifted, the company's own agents resume full authority over those funds. Separately, if those same funds are later criminally forfeited following a conviction, the government becomes the owner outright. No agent chain rooted in the original company's authority can ever regain authority over that specific property again, because the underlying property right, not just the ability to transact, has changed hands.

**Human analog.** Criminal forfeiture on conviction. [Cornell LII, 18 U.S.C. 982](https://www.law.cornell.edu/uscode/text/18/982): "The court, in imposing sentence on a person convicted of an offense... shall order that the person forfeit to the United States any property, real or personal, involved in such offense, or any property traceable to such property."

**What should happen.** A framework that models both a freeze and a forfeiture as "the same account is blocked" treats them as equivalent and reversible in the same way. They are not. Forfeiture changes who owns the underlying resource a delegation's grants ultimately point to, and no amount of the original principal issuing new grants over that resource is meaningful once it is forfeited.

**What a naive system gets wrong.** Treating forfeiture as just a stronger or longer freeze misses that the resource itself has changed owners. A later unblock event, such as a case dismissal, restores authority under a freeze but cannot restore authority under a completed forfeiture, because there is no longer an underlying right for the original principal to exercise.

**Related invariant/open question.** No grant, revoke, suspend, or restrict vocabulary in L1-L12 describes a change in the underlying resource's ownership, as distinct from a change in who may currently exercise authority over an unchanged resource.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-027-a`, `LRE-B-027-b`, `LRE-B-027-c`, `LRE-B-027-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

#### LC-B-031. The same bankruptcy chapter question can produce opposite authority outcomes

**Situation.** The same procurement agent from LC-B-010, instead of continuing under the CFO's restricted, court-supervised authority, finds the case has converted to Chapter 7. A trustee is appointed to liquidate the company. The CFO's authority over estate property, even in restricted form, ends. Any continuing procurement activity must now come from a grant issued by the trustee, not the CFO.

**Human analog.** Contrast between Chapter 7 and Chapter 11 authority. [Cornell LII, 11 U.S.C. 704(a)(1)](https://www.law.cornell.edu/uscode/text/11/704): the trustee must "collect and reduce to money the property of the estate for which such trustee serves, and close such estate as expeditiously as is compatible with the best interests of parties in interest." [11 U.S.C. 1107](https://www.law.cornell.edu/uscode/text/11/1107) by contrast gives a Chapter 11 debtor in possession the trustee's own powers, "[s]ubject to any limitations... [the] court prescribes."

**What should happen.** The same triggering event, a bankruptcy filing, produces two different authority outcomes depending on which chapter applies. Chapter 11 preserves the existing officers' authority in restricted form. Chapter 7 replaces it entirely with a new principal, the trustee.

**What a naive system gets wrong.** Applying LC-B-010's "restriction, not revocation" outcome uniformly to any bankruptcy filing, without checking which chapter and case posture applies, wrongly preserves officer authority in a Chapter 7 case where it should have ended and a new principal should be the only source of continuing grants.

**Related invariant/open question.** Directly contrasts with LC-B-010 to show the same event category needs to branch into genuinely different authority outcomes depending on sub-type, which no single invariant captures alone.

**Status:** proposed.

**Fixture:** `lifecycle-legal-regulatory-events` / `LRE-B-031-a`, `LRE-B-031-b`, `LRE-B-031-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-legal-regulatory-events/README.md)

---

### Root authority and succession

#### LC-C-007. Whether a delegation is bound to an office or to a person is a design choice the framework has to represent explicitly

**Situation.** A delegation's subject field can be written two different ways: bound to a role (whoever holds the office of Treasurer) or bound to a specific identity (this exact key and DID). When the person filling the role changes, the two binding modes should behave differently, and the model does not currently say which a verifier should assume when the delegation is silent.

**Human analog.** A 1979 Justice Department Office of Legal Counsel opinion on whether a delegation of authority survived the resignation of the Attorney General who issued it. [US Department of Justice, Office of Legal Counsel opinion](https://www.justice.gov/file/149056/dl): "a valid delegation of authority or other rule or regulation continues in force until revoked by someone with authority to revoke it, and accordingly continues without regard to the departures from office of its originator and intervening successors."

**What should happen.** A verifier needs to read the subject binding type off the delegation itself. If it is role-bound and there is a trustworthy record of who currently occupies the role, the chain should verify for the new occupant with no reissuance. If it is identity-bound, turnover in the office does nothing for the new occupant, and a fresh chain is required.

**What a naive system gets wrong.** Treating every delegation as identity-bound forces a costly reissuance sweep on every personnel change, even for administrative roles never meant to depend on who holds them. Treating every delegation as role-bound risks quietly handing a departing employee's personal grants to whoever backfills their title, including grants that were never meant to be inherited.

**Related invariant/open question.** L2 through L4 assume a departing principal's authority ends and a successor needs an explicit fresh grant. This case shows the opposite is sometimes correct by design. The framework does not yet distinguish these two binding modes or say which a verifier should assume by default.

**Status:** proposed.

**Fixture:** `lifecycle-root-authority-succession` / `LRAS-C-007-a` to `LRAS-C-007-k` (11) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-root-authority-succession/README.md)

---

### Multiple principals and conflict

#### LC-C-002. A live capacity dispute needs a default holder, a deadline, and a supermajority override, not a block or a race

**Situation.** Two principals both have a plausible claim to the same seat of authority at the same moment. One says the other has lost capacity to act. The other disputes it. The dispute cannot be resolved instantly, and action cannot simply wait.

**Human analog.** US Constitution Amendment XXV Section 4. On the President's written declaration contesting an inability finding, Congress has 21 days to decide by a two-thirds vote of both houses whether the President is unable to discharge the office. [Cornell Law School, Legal Information Institute](https://www.law.cornell.edu/constitution/amendmentxxv): "otherwise, the President shall resume the powers and duties of his office."

**What should happen.** A verifier needs a default holder for the entire contested window (here, the Vice President as Acting President), a hard deadline, and a defined supermajority threshold that can flip the default. If the deadline passes without that supermajority, the default reverts to the challenged party, not to whichever side currently holds the seat.

**What a naive system gets wrong.** Treating a disputed principal state as indeterminate blocks exactly the actions that cannot wait. Letting whichever party acts first win invites a race instead of a resolution. A system that assumes the default holder simply continues past the deadline gets the reversion backwards: silence resolves in favor of the party being challenged, not the party asserting the challenge.

**Related invariant/open question.** None of L1 to L12 model two live, competing claims to one authority position with a default-favors-one-side rule, a deadline, and a supermajority override. L5 forbids combining two valid chains into one grant, but this is one seat with two competing occupancy claims and a designed tie-break, not a union of chains.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-002-a` to `LC-C-002-i` (9) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-005. Two independently valid succession sources can name different people for the same seat, and nothing says which one wins

**Situation.** An office holder resigns. Two federal statutes, each independently valid, each purport to govern who becomes acting head, and they name different people.

**Human analog.** The 2018 appointment of Matthew Whitaker as Acting Attorney General over Deputy Attorney General Rod Rosenstein. [Constitutional Center](https://constitutioncenter.org/blog/whitakers-acting-attorney-general-appointment-heads-to-court): a lawsuit argued "under the Attorney General Succession Act and the Appointments Clause of the Constitution that Deputy Attorney General Rod Rosenstein should be serving as Acting Attorney General instead of Whitaker."

**What should happen.** A verifier needs an explicit, checkable priority rule between competing valid succession sources, for example a general versus a specific statute, or an org-level versus a role-level policy, so it can pick one deterministically. Presenting a chain is not the same as that chain being the one that governs.

**What a naive system gets wrong.** Verifying whichever chain a relying party happens to submit, with no standing priority rule between sources, lets the same vacant authority be exercised by two different actors depending only on which document was checked. That is exactly what made the appointment contestable.

**Related invariant/open question.** L5 forbids combining two chains into one grant. This is different: a single seat with two independently sourced, individually valid chains disagreeing about who holds it. Nothing in L1 to L12 orders competing valid authority sources against each other.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-005-a`, `LC-C-005-b`, `LC-C-005-c`, `LC-C-005-d`, `LC-C-005-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-006. A tainted ancestor invalidates dependents only from the moment the taint is found, not retroactively

**Situation.** A chain of appointments rests on a person's authority to make them. Eighteen months later, an independent investigator finds that person's own appointment was never valid, not revoked, never valid in the first place, and by then the downstream appointees have signed many orders that already took effect.

**Human analog.** The GAO's August 2020 finding that DHS acting secretary Chad Wolf's and acting deputy secretary Ken Cuccinelli's appointments were invalid, because Kevin McAleenan, who named them, had himself been installed outside the statutory order of succession and had no authority to amend that order. [GAO finding, reported by GovExec](https://www.govexec.com/management/2020/08/top-two-homeland-security-officials-are-serving-illegally-gao-rules/167714/): "McAleenan's subsequent appointments of Wolf and Cuccinelli were therefore invalid, GAO said, as he was not eligible to make them."

**What should happen.** A verifier needs a distinct status for "invalid from issuance, discovered late," not the same as a revocation event, because nobody revoked anything and it was never valid to begin with. Going forward from the finding, dependent chains are invalid. What happens to the orders and effects already executed while the chain looked valid is a separate question the finding itself does not answer.

**What a naive system gets wrong.** A revocation-only model finds nothing wrong here, because no one ever revoked anything. It has no way to represent "this grant was void from issuance" discovered after the fact, and no way to backdate that discovery without either pretending nothing happened or silently erasing evidence of effects already taken.

**Related invariant/open question.** L1 (revoking an ancestor invalidates dependents) assumes the ancestor was once valid and was later revoked. This case is the harder one L1 does not cover, an ancestor invalid from the start, discovered long after the fact. Also touches the "work in flight" operational case and L12 (completeness), since the orders executed under the tainted chain are exactly the evidence a completeness claim needs to account for.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-006-a`, `LC-C-006-b`, `LC-C-006-c`, `LC-C-006-d`, `LC-C-006-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-009. A legitimately confidential succession order breaks the assumption that every chain is independently, publicly verifiable

**Situation.** The order that determines who becomes the next holder of a critical position is itself confidential, held by one custodian rather than published where any relying party could check it independently before the moment of need.

**Human analog.** The House rule adopted after 2001 requiring the Speaker to privately give the Clerk an ordered succession list whose contents are not published. [Thompson Coburn](https://www.thompsoncoburn.com/insights/presidential-succession-102jjry/): "the speaker provides the clerk 'a list of Members in the order in which each shall act as Speaker pro tempore' in the case of a vacancy."

**What should happen.** A verifier at the moment of triggering has to rely on an attestation from a single custodian rather than an independently checkable chain. The protocol needs a defined trust boundary for that custodian, who else can confirm the custodian's own honesty and freshness, instead of assuming every succession order is publicly verifiable in advance.

**What a naive system gets wrong.** Assuming every authority chain must be independently, publicly verifiable end to end has no place for a legitimately confidential ordering. It either rejects the whole mechanism as unverifiable, or silently trusts whatever the custodian says with no fallback if the custodian is unavailable or compromised.

**Related invariant/open question.** Nothing in L1-L12 addresses a succession order that is deliberately not public. Also touches OPEN-QUESTIONS.md's "office vacancy and succession," since this is exactly a case of authority for an office needing to be exercised without every relying party being able to check the chain.

**Status:** proposed.

**Fixture:** `activation-not-established` / `AX-02`, `AX-03`, `AX-04`, `AX-06` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/activation-not-established/README.md)

---

#### LC-C-011. A concurrence requirement is a gate at the next authorization boundary, not a second chain to union with the first

**Situation.** An action requires two independently authorized principals to concur before it proceeds. One principal authorizes it. The other has not yet. A verifier built only around single root-to-leaf chain verification has no way to represent "wait for a second, independent concurrence" as anything other than either wrongly admitting the first chain alone, or wrongly trying to model the requirement as merging two chains into one.

**Human analog.** The US two-person concept for nuclear weapons: two independently authorized individuals must concur before a launch-related action proceeds. [Wikipedia, Two-person rule](https://en.wikipedia.org/wiki/Two-person_rule): "The two-person concept is designed to prevent accidental or malicious launch of nuclear weapons by a single individual."

**What should happen.** A verifier must refuse the action at the next authorization boundary unless both required concurrences are present and fresh at the same moment. One valid authorization alone is insufficient no matter how strong that single chain is, and a longer or more senior chain never substitutes for the missing second concurrence.

**What a naive system gets wrong.** Confusing a concurrence gate with the scope-union problem L5 already forbids. They look similar (two chains, one action) but are opposite failures. L5 is about not letting two chains add up to more scope than either allows. A concurrence gate is about refusing to act on one chain alone regardless of scope.

**Related invariant/open question.** L5 forbids unioning chains to expand what one action is allowed to do. This is a distinct primitive, a gate at the next authorization boundary requiring two separate, independently valid authorizations to be present together, that none of L1-L12 name.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-011-a`, `LC-C-011-b`, `LC-C-011-c`, `LC-C-011-d`, `LC-C-011-e`, `LC-C-011-f`, `LC-C-011-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

Variants: B-003 (a dual-control money threshold requiring two independent chains before the next authorization boundary, the same "one valid chain is insufficient" gate in a corporate treasury setting rather than a safety-critical one).

---

#### LC-C-012. Independently rooted chains can commit to a shared objective without unioning their scopes

**Situation.** Several agencies, each with an independent command chain, respond jointly to the same incident and need to operate under one integrated plan, while each keeps exclusive control of its own resources.

**Human analog.** The Incident Command System's Unified Command structure. [Wikipedia, Incident command system](https://en.wikipedia.org/wiki/Incident_command_system): "A unified command involves two or more individuals sharing the authority normally held by a single incident commander."

**What should happen.** The protocol should let independently rooted chains commit jointly to a shared objective record without merging their scopes. Each chain still only authorizes actions over its own resources, and the joint objective record needs its own signature naming which chains are party to it, with any party able to withdraw without invalidating the others.

**What a naive system gets wrong.** A system that only knows single-chain verification and L5's ban on unioning scopes has no permitted way to represent multiple independently rooted principals coordinating. Implementers either fake it by improperly merging scopes, violating L5's intent, or refuse to model joint operations at all.

**Related invariant/open question.** L5 says a verifier must not union scopes or budgets from multiple chains for one action. Unified Command is the case the framework has not described: multiple chains legitimately coordinating on shared objectives while each keeps its own scope fully separate. That is not a union, and should be explicitly permitted rather than left looking like the anti-pattern L5 forbids.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-012-a`, `LC-C-012-b`, `LC-C-012-c`, `LC-C-012-d`, `LC-C-012-e`, `LC-C-012-f`, `LC-C-012-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-016. The bar for granting authority and the bar for withdrawing it are not always the same bar

**Situation.** A dispatcher and a pilot in command jointly hold operational control of a flight. Once the flight is released and underway, either one alone can unilaterally stop or redirect it. But originating or continuing the flight required both to agree in the first place.

**Human analog.** 14 CFR § 121.533, joint responsibility for preflight planning, delay, and dispatch release. [Cornell LII](https://www.law.cornell.edu/cfr/text/14/121.533): "The pilot in command and the aircraft dispatcher are jointly responsible for the preflight planning, delay, and dispatch release of a flight."

**What should happen.** A verifier must apply different thresholds depending on the direction of the action. Continuation or origination requires both principals' current concurrence, while cancellation or restriction requires only one. Using the same threshold in both directions either lets one party force continuation over the other's objection, or makes it too hard for either party to stop something unsafe.

**What a naive system gets wrong.** Modeling every concurrence relationship on the symmetric nuclear-launch pattern (LC-C-011), where both sides must agree in both directions. This case is the same two-principal shape with a deliberately asymmetric rule, which a framework built only on the symmetric pattern gets backwards.

**Related invariant/open question.** Extends the joint or quorum family with an asymmetry, grant versus veto, that nothing in L1-L12 or the sponsor-handover conformance case names.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-016-a`, `LC-C-016-b`, `LC-C-016-c`, `LC-C-016-d`, `LC-C-016-e`, `LC-C-016-f`, `LC-C-016-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-018. Concurrence can generalize beyond a fixed pair to an enumerated role set where silence itself blocks the action

**Situation.** Before a surgical team begins an irreversible action, every distinct role with relevant knowledge must affirmatively confirm a shared set of facts about the action. The action is blocked unless all required roles have actively confirmed. Silence, absence, or an unresolved objection from any one role blocks it and is not treated as implicit consent.

**Human analog.** The Joint Commission's Universal Protocol time-out. [AORN, Outpatient Surgery Magazine](https://www.aorn.org/outpatient-surgery/article/time-out-tips-from-the-trenches): "All relevant members of the procedure team actively communicate during the time out," agreeing at minimum on correct patient identity and correct site and procedure, with the case not proceeding until every question is resolved.

**What should happen.** The gate requires collected, explicit, per-role affirmative confirmation, logged individually, rather than a single authorizer's sign-off or a default-permit when no objection is raised. Any missing or negative confirmation from any required role should halt the action regardless of how many other roles already confirmed.

**What a naive system gets wrong.** A framework that only models two-party concurrence cannot express a variable-size, all-must-affirm, silence-is-not-consent gate. Generalizing from a fixed pair to an enumerated role set, and treating missing confirmation the same as active dissent, is stricter than a simple veto model and needs its own representation.

**Related invariant/open question.** Close in shape to the nuclear two-person concurrence gate and to the dispatcher and pilot joint operational control case, but neither of those covers an arbitrary, named role set where missing confirmation, not just active dissent, blocks the action. None of L1 to L12 name a variable-size unanimous confirmation gate.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-018-a`, `LC-C-018-b`, `LC-C-018-c`, `LC-C-018-d`, `LC-C-018-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-020. An authority position can be created on the fly by an eligibility rule, with no pre-named holder at all

**Situation.** A patient goes into cardiac arrest and no pre-designated response leader is present. Someone has to lead, immediately, without a prior grant naming them.

**Human analog.** Hospital Code Blue and rapid response protocols, in which the first qualified responder to arrive leads, with hand-off to a more senior or better-positioned provider as one arrives. [Rasmussen University](https://www.rasmussen.edu/degrees/nursing/blog/what-is-a-code-blue/): "The leader—typically a physician or advanced practice provider—pays attention to every aspect of the situation," tracking vitals, monitoring resuscitation, and communicating with the rest of the team.

**What should happen.** The framework needs to support authority positions whose initial holder is determined by a first-eligible-claimant rule rather than a grant record. Subsequent replacements of that ad hoc holder should go through the same explicit accept-and-acknowledge protocol as any planned handover, and the position should dissolve entirely, not revert to anyone, once its triggering condition ends.

**What a naive system gets wrong.** A system that assumes every authority position has a pre-named default holder or a designated successor list cannot represent a position that springs into existence only because of an emergent situation and has no holder at all until someone claims it. It will either block action during the critical first moments or fail to define when the position properly dissolves once the emergency ends.

**Related invariant/open question.** Distinct from a statutory first-assistant default naming a specific fallback identity in advance. Here there is no advance designation of any kind. The position and its first holder are both created at the moment of the triggering event by an eligibility rule evaluated live.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-020-a` to `LC-C-020-i` (9) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-022. A pending-ratification state is neither "revoked" nor "not revoked," and if ratification is denied, the record has to say the action was provisional throughout, not that a final revocation was later reversed

**Situation.** A commander relieves a subordinate of command. The required written approval from a higher general officer has not yet arrived. Until it does, the relief has a lesser, provisional effect. If the approval never comes, the action is retroactively recharacterized as having only ever been the lesser effect, not undone from a final state.

**Human analog.** US Army relief-for-cause procedure. [Fort Carson command policy memo, quoting AR 600-20](https://home.army.mil/carson/6116/5089/9699/relief-for-cause.pdf): "Any commander may temporarily suspend a subordinate from command, but the final action to relieve an officer from any command position will not be taken until after written approval by the first general officer in the chain of command."

**What should happen.** A verifier needs a "revocation-pending-ratification" state, distinct from both full revocation and no revocation, during which the target's authority is suspended but the initiating principal's action is not yet final. If ratification never arrives, every record has to reflect that the action was provisional throughout.

**What a naive system gets wrong.** Conflating this with an ordinary self-declared, self-terminated suspension. This is a different shape, an external, unilateral suspension by a superior that only becomes a final revocation with a specific separate approval. Treating the two the same either finalizes a revocation that legally never became final, or fails to suspend the subordinate while waiting on paperwork.

**Related invariant/open question.** Adds a ratification-pending intermediate state with retroactive recharacterization on denial, a shape not present in L8's plain suspension and revocation split, and directly relevant to OPEN-QUESTIONS.md's "release from suspension."

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-022-a`, `LC-C-022-b`, `LC-C-022-c`, `LC-C-022-d`, `LC-C-022-e`, `LC-C-022-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

Variants: B-032 (an officer suspended pending investigation, where the open part is whether conversion to revocation reaches back to the suspension's start or runs only from the investigation's conclusion, and unsourced where this entry is sourced).

---

#### LC-C-029. A shared coalition grant can carry different, per-contributor restrictions that a pooled ruleset cannot represent

**Situation.** A nation contributes military forces to a coalition operation, delegating a narrower slice of its full authority to the coalition commander while retaining full command itself, and separately attaching its own additional restrictions on top of that narrower scope.

**Human analog.** NATO command relationships (operational command, operational control, tactical command, tactical control) and the practice of national caveats restricting how contributed forces may be used. [Wikipedia, National caveats](https://en.wikipedia.org/wiki/National_caveats): "A national caveat is a restriction that North Atlantic Treaty Organization (NATO) members place on the use of their forces."

**What should happen.** The coalition commander's authority over contributed forces should be a strict subset of the contributing nation's full authority, matching the framework's own narrowing principle. Any nation-specific caveat attached at delegation time should further restrict what the coalition commander may do with that subset, checkable per contributing nation rather than uniformly across all contributed forces.

**What a naive system gets wrong.** Modeling coalition delegation as a single uniform scope for all contributed forces cannot represent that two nations contributing under the same nominal control level may carry different, individually attached caveats. It will either apply the most permissive nation's rules to everyone or block legitimate coordinated action by treating incompatible caveats as one block.

**Related invariant/open question.** Close to a positive example of the framework's own narrowing principle rather than a gap in it, but the per-contributor caveat layered onto a shared coalition grant, checkable per source rather than pooled, is not named anywhere in L1 to L12. Distinct from the Unified Command case, which is same-level coordination between non-hierarchical chains rather than a hierarchical, narrower-scope delegation.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-029-a`, `LC-C-029-b`, `LC-C-029-c`, `LC-C-029-d`, `LC-C-029-e`, `LC-C-029-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-C-031. A standing, cause-free override can sit above a concurrently exercised authority without ever going through a revocation channel

**Situation.** A vessel takes on a harbor pilot where pilotage is legally compulsory. The ship's master is required to accept the pilot's operational direction, but never actually loses superior authority, and retains the standing right to unilaterally end the pilot's operational role at any instant, with no process, notice, or cause requirement.

**Human analog.** SOLAS Chapter V Regulation 34-1 and maritime pilotage practice. [Safety4Sea](https://safety4sea.com/what-does-vessel-on-masters-orders-and-pilots-advice-mean/), quoting the regulation: the owner, the charterer, the company operating the ship "or any other person SHALL NOT prevent or restrict the master of the ship from taking or executing any decision which...is necessary for the safety of life at sea."

**What should happen.** A verifier should treat the pilot's delegated operational authority as concurrently exercised but always subordinate to a standing, always-live override held by the master. Any action by the pilot is valid only for as long as the master has not exercised that override, and the override itself requires no justification, process, or advance notice to take effect.

**What a naive system gets wrong.** A framework that models delegation as the delegator stepping back while the delegate acts misrepresents this relationship: the master never steps back and can reassert direct control instantly and without cause. Treating this like an ordinary revocable grant undercounts how immediate and unilateral the override can be, and treating it like the mandatory-concurrence cases overcounts how much independent standing the pilot actually has, since only the master's authority was ever real at the root.

**Related invariant/open question.** Distinct from ordinary revocable delegation because the override is instantaneous, cause-free, and needs no formal revocation channel. It is a standing background right rather than a discrete revocation event, and distinct from the mandatory concurrence cases because only one party's authority was ever real at the root.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-C-031-a`, `LC-C-031-b`, `LC-C-031-c`, `LC-C-031-d`, `LC-C-031-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-H-001. One co-settlor's unilateral revocation of a joint grant reaches only their own contributed share, not the whole grant

**Situation.** A revocable trust is created and funded by two settlors together. Later, one settlor alone tries to revoke the whole trust. Nothing in the trust's own terms addresses what a single co-settlor's revocation reaches when the other settlor has not joined in.

**Human analog.** The Maine Uniform Trust Code's rule for a revocable trust with more than one settlor. [Maine Revised Statutes, 18-B M.R.S. §602(2)](https://legislature.maine.gov/statutes/18-B/title18-Bsec602.html): "To the extent the trust consists of property other than community property, each settlor may revoke or amend the trust with regard to the portion of the trust property attributable to that settlor's contribution." For the community-property portion, the same section states: "the trust may be revoked by either spouse acting alone but may be amended only by joint action of both spouses."

**What should happen.** A verifier handling a joint grant from multiple co-issuing principals needs the concept of a grant divisible by contribution or interest, so that one co-issuer's revocation is scoped to their own share rather than treated as an all-or-nothing event over the whole grant. Whether an amendment (as opposed to revocation) needs joint action is a separate, narrower question the same rule answers differently.

**What a naive system gets wrong.** Modeling a joint grant as a single indivisible authority object either lets one co-issuer's revocation wrongly kill the whole grant, including the part attributable to a co-issuer who never acted, or wrongly requires unanimous action to revoke any part at all, when the actual rule splits by contribution and gives revocation and amendment different thresholds.

**Related invariant/open question.** None of L1-L12 name a divisible, per-contributor grant. L1 assumes revoking an ancestor is a single binary event. This is a case where the "ancestor" is itself already fractional along a dimension (contribution share) that a chain-verification model built only around whole grants has no place for.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-H-001-a`, `LC-H-001-b`, `LC-H-001-c`, `LC-H-001-d`, `LC-H-001-e`, `LC-H-001-f`, `LC-H-001-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-H-002. On an account requiring multiple signers, any one signer's stop instruction controls over a contradictory pay instruction from a co-signer

**Situation.** An account requires more than one authorized signer to draw on it. One signer gives the bank a stop-payment order on an item. Another signer never authorized that stop and may want the item paid. The two instructions are directly contradictory and both come from validly authorized principals on the same account.

**Human analog.** UCC Article 4, the customer's right to stop payment. [Cornell LII, UCC §4-403](https://www.law.cornell.edu/ucc/4/4-403): "If the signature of more than one person is required to draw on an account, any of these persons may stop payment or close the account."

**What should happen.** A verifier needs a standing precedence rule for exactly this shape of conflict: on a multi-signer account, a stop instruction from any one required signer controls over a contradictory pay instruction from another, without needing the other signer's concurrence or even their notice. This is a fixed, named default, not a case-by-case judgment call.

**What a naive system gets wrong.** Treating contradictory instructions from two equally authorized co-principals as requiring a tiebreak the system has to construct case by case, or wrongly requiring both signers to agree before either instruction takes effect, when the actual default already resolves the conflict by letting a stop instruction win outright.

**Related invariant/open question.** L5 forbids combining two chains into more scope than either allows. This is a different shape entirely, two equally valid single-principal instructions in direct conflict, resolved by a named asymmetric default (stop beats pay) rather than by unioning or requiring concurrence.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-H-002-a`, `LC-H-002-b`, `LC-H-002-c`, `LC-H-002-d`, `LC-H-002-e`, `LC-H-002-f`, `LC-H-002-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-H-003. Bankruptcy discharge and debt reaffirmation racing each other resolve by a statutory sequencing and rescission window, not a first-arrival rule

**Situation.** A court is about to discharge a debt, which extinguishes the creditor's claim against the debtor going forward. Around the same time, the debtor and creditor negotiate a reaffirmation agreement reviving that same debt. Both a revocation-like event (discharge) and a reaffirmation of the thing being revoked are moving toward effect at close to the same moment.

**Human analog.** 11 U.S.C. §524(c), governing reaffirmation agreements. [Cornell LII, 11 U.S.C. §524](https://www.law.cornell.edu/uscode/text/11/524): a reaffirmation agreement is enforceable only if "such agreement was made before the granting of the discharge under section 727, 1141, 1192, 1228, or 1328 of this title." The same section gives the debtor a right to rescind "at any time prior to discharge or within sixty days after such agreement is filed with the court, whichever occurs later."

**What should happen.** A verifier facing a revocation event and a reaffirmation of the same authority arriving close together should not resolve the race by whichever record it observes first. This domain answers it with a fixed sequencing rule (reaffirmation must precede the discharge to be enforceable at all) plus a standing rescission window that outlives the filing itself. A verifier needs both a sequencing check and a defined window during which the reaffirmation can still be undone, not a single timestamp comparison.

**What a naive system gets wrong.** Comparing timestamps and letting whichever record has the later timestamp win treats this as an ordinary last-write-wins conflict, when the actual rule requires the reaffirmation to have preceded the revocation-like event to be valid at all, and then keeps it undoable for a further fixed period regardless of when it was filed.

**Related invariant/open question.** L3 says reauthorization creates new authority and never reverses a revocation. This case is adjacent but distinct: reaffirmation here is a targeted revival of one specific ended obligation, gated by an ordering rule and a standing rescission window, not a new grant from a currently authorized principal in the L3 sense.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-H-003-a`, `LC-H-003-b`, `LC-H-003-c`, `LC-H-003-d`, `LC-H-003-e`, `LC-H-003-f`, `LC-H-003-g` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

### Outside-the-chain standing

#### LC-H-004. A board's suspension of a principal's authority is not valid board action at all without the quorum required for the board to transact business

**Situation.** A corporate board attempts to suspend or remove an officer's authority. Fewer directors are present or participating than the number the bylaws require as a quorum for the board to transact business at all.

**Human analog.** Delaware's General Corporation Law provision on board quorum. [Delaware Code, Title 8 §141(b)](https://delcode.delaware.gov/title8/c001/sc04/index.html): "A majority of the total number of directors shall constitute a quorum for the transaction of business unless the certificate of incorporation or the bylaws require a greater number."

**What should happen.** Standing to act, not just the content of the action, is a precondition. A verifier checking whether a suspension is valid needs to check whether the body that produced it had quorum to transact business at all, not only whether the resulting record looks like a properly formatted suspension. Without quorum, there is no valid board action to evaluate, not established, not "invalid" in the sense of a defective but real action.

**What a naive system gets wrong.** Verifying that a suspension record exists and is properly signed, without separately verifying that the issuing body had standing (quorum) to act at the moment it purported to act, lets a rump minority of a board effectively suspend a principal's authority with no real board action behind it.

**Related invariant/open question.** None of L1-L12 address a collective body's own internal standing requirement (quorum) as a precondition for the validity of what it issues. This is a harder case than an individual issuer's standing, since the defect is procedural (not enough members present) rather than about who any single signer was.

**Status:** proposed.

**Fixture:** `lifecycle-outside-the-chain-standing` / `LC-H-004-a`, `LC-H-004-b`, `LC-H-004-c`, `LC-H-004-d`, `LC-H-004-e`, `LC-H-004-f`, `LC-H-004-g`, `LC-H-004-h` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-outside-the-chain-standing/README.md)

---

#### LC-H-005. A labor board's reinstatement order is a new grant issued from outside the original relationship, not a revival of the exact terminated one

**Situation.** An employer terminates an employee. A government labor board later finds the termination was an unfair labor practice and orders the employer to reinstate the employee, potentially with conditions (such as back pay) the original employment relationship never had.

**Human analog.** The National Labor Relations Act's remedial authority. [Cornell LII, 29 U.S.C. §160(c)](https://www.law.cornell.edu/uscode/text/29/160): the Board may issue "an order requiring such person to cease and desist from such unfair labor practice, and to take such affirmative action including reinstatement of employees with or without back pay, as will effectuate the policies of this subchapter." The same subsection also states reinstatement is unavailable where "such individual was suspended or discharged for cause."

**What should happen.** A court- or agency-compelled reinstatement should be modeled as a new grant, issued by a party (the labor board) with standing from outside the original principal-agent relationship, not as an automatic revival of the exact prior authority unmodified. The new grant can carry terms the original relationship never had, and it does not issue at all if the underlying facts (termination for cause) do not support it.

**What a naive system gets wrong.** Treating a reinstatement order as simply switching the old, terminated authority back to valid, rather than as a distinct new grant from a different, external issuer. That loses the fact that the new grant's terms and conditions come from the reinstating body, not from whatever the original relationship said, and that the order is conditional on the underlying facts.

**Related invariant/open question.** Extends L3 and L4 (replacement authority as a fresh grant, not a resurrected chain) to a case where the fresh grant is issued by a body with standing entirely outside the original principal-agent relationship, rather than by a successor principal within it.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-H-005-a`, `LC-H-005-b`, `LC-H-005-c`, `LC-H-005-d`, `LC-H-005-e`, `LC-H-005-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

#### LC-H-006. A disputed root can be deposited with a neutral forum pending resolution, discharging the holder from choosing between claimants

**Situation.** Two or more parties each claim to be the rightful holder of the same disputed authority or property. Whoever currently holds it does not know, and should not have to decide, which claimant is correct.

**Human analog.** Federal statutory interpleader. [Cornell LII, 28 U.S.C. §1335](https://www.law.cornell.edu/uscode/text/28/1335): the holder proceeds where "the plaintiff has deposited such money or property or has paid the amount of or the loan or other value of such instrument or the amount due under such obligation into the registry of the court," to "abide the judgment of the court," or alternatively "has given bond payable to the clerk of the court."

**What should happen.** A verifier facing a disputed root of authority needs a state distinct from valid, revoked, or suspended: held pending resolution by a neutral forum, with the holder discharged from having to pick a claimant. Nothing downstream of the disputed root should be treated as authorized or as unauthorized while it sits in that state. It is not established which claimant's authority, if any, currently governs.

**What a naive system gets wrong.** Forcing a binary choice, either honoring one claimant's chain as valid or rejecting both as invalid, when the correct state is a third one: parked with a neutral forum, resolvable only by that forum's eventual determination, with the current holder relieved of the decision entirely.

**Related invariant/open question.** OPEN-QUESTIONS.md's "notice and relying parties" section and L7 (unknown revocation state is not active) are adjacent but distinct: this is not an evidence-freshness problem, it is a genuine, acknowledged dispute over which of two claimed roots is authoritative, with an actual named mechanism (deposit with the court) for holding the question open without forcing a premature answer.

**Status:** proposed.

**Fixture:** `lifecycle-multiple-principals-and-conflict` / `LC-H-006-a`, `LC-H-006-b`, `LC-H-006-c`, `LC-H-006-d`, `LC-H-006-e`, `LC-H-006-f`, `LC-H-006-g`, `LC-H-006-h` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-multiple-principals-and-conflict/README.md)

---

### Subdelegation edges

#### LC-H-007. Checking each delegation artifact's validity period independently means a child's stated expiry can extend past its parent's without the base algorithm ever comparing the two

**Situation.** A subordinate (child) delegation artifact carries a stated validity end date later than the validity end date of the parent artifact that issued it. Nothing in the child's own record is malformed, and the child's issuance otherwise looks ordinary.

**Human analog.** The X.509 certification path validation algorithm's per-certificate validity check. [RFC 5280 §6.1.3(a)(2)](https://www.rfc-editor.org/rfc/rfc5280): the algorithm requires, for each certificate in the path, that "the certificate validity period includes the current time." The algorithm checks this against the current time for each certificate individually. It does not compare a certificate's stated validity period against its issuer's own validity period.

**What should happen.** A verifier should not assume that a child's declared expiry is automatically bounded by its parent's, since the base per-artifact check does not enforce that nesting. Either a verifier adds an explicit check that a child's stated validity period does not extend past its parent's at issuance time, or it accepts that the mismatch will only surface later, when the parent itself is separately checked and found expired while the child's own record still claims to be valid.

**What a naive system gets wrong.** Assuming that because a chain is checked link by link, an ancestor's earlier expiry automatically caps what a descendant can claim. The per-artifact check the algorithm actually specifies has no such comparison step, so the mismatch exists undetected in the child's own record until the moment the parent's own link in the same chain is separately evaluated.

**Related invariant/open question.** L10 distinguishes expiry from revocation for a single artifact. This is a different, prior question: whether a child's own declared expiry is required to nest inside its issuer's, which none of L1-L12 state, and which a widely used base algorithm turns out not to enforce either.

**Status:** proposed.

**Fixture:** `lifecycle-subdelegation-edges` / `LC-H-007-a`, `LC-H-007-b`, `LC-H-007-c`, `LC-H-007-d`, `LC-H-007-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-subdelegation-edges/README.md)

---

#### LC-H-008. Delegation depth exhaustion is a distinct failure mode, rejecting subdelegation past a chain's own declared maximum depth

**Situation.** A delegation chain carries an explicit maximum subdelegation depth. The chain is already at that maximum. The current holder of the deepest link attempts to subdelegate once more, to a further child beyond the declared limit.

**Human analog.** The X.509 Basic Constraints extension's path length field. [RFC 5280 §4.2.1.9](https://www.rfc-editor.org/rfc/rfc5280): pathLenConstraint "specifies the maximum number of non-self-issued intermediate certificates that may follow this certificate in a valid certification path."

**What should happen.** A verifier needs depth exhaustion as its own named failure, distinct from expiry, revocation, or suspension: the chain's structure itself forbids the further link, independent of whether every individual artifact in it is otherwise current and unrevoked. The constraint is carried on an ancestor artifact, so every verifier evaluating the resulting chain has to enforce it, not only the artifact that improperly issued past the limit.

**What a naive system gets wrong.** Checking only whether each individual link in a chain is currently valid, unrevoked, and unexpired, with no separate check on the chain's overall declared depth, lets a subdelegation past the stated limit pass every per-artifact check while still violating the structural constraint the ancestor imposed on the whole chain.

**Related invariant/open question.** None of L1-L12 name a maximum-depth constraint as its own lifecycle concept. It is closest to L5 (independent chains are not combined) in spirit, structural limits on the shape of a chain rather than on its content, but depth exhaustion is a distinct constraint L5 does not cover.

**Status:** proposed.

**Fixture:** `lifecycle-subdelegation-edges` / `LC-H-008-a`, `LC-H-008-b`, `LC-H-008-c`, `LC-H-008-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-subdelegation-edges/README.md)

---

### Agent renunciation

#### LC-H-010. A director's resignation is effective on delivery of notice, not on the principal's acceptance

**Situation.** An agent acting in a corporate-officer role decides to give up that role and gives written notice of resignation to the principal (the corporation). The principal does not respond, or delays responding, to that notice.

**Human analog.** Delaware's General Corporation Law provision on director resignation. [Delaware Code, Title 8 §141(b)](https://delcode.delaware.gov/title8/c001/sc04/index.html): "A resignation is effective when the resignation is delivered unless the resignation specifies a later effective date or an effective date determined upon the happening of an event or events."

**What should happen.** A verifier evaluating an agent-initiated termination of the agent's own role should treat it as effective on delivery of notice to the principal, not on the principal's acknowledgment or acceptance, unless the renunciation itself names a later effective date or triggering event. The principal cannot keep the agent bound simply by not responding.

**What a naive system gets wrong.** Requiring an explicit acceptance record from the principal before treating a renunciation as effective builds in a veto the principal does not actually have, letting a silent or unresponsive principal hold an agent to continued authority against the agent's own stated will.

**Related invariant/open question.** Distinct from L3/L4's succession-after-departure question. This is about the timing of the departure itself, not what replaces it, and this domain's rule (effective on delivery, not on receipt-and-acceptance) is a genuinely different default than the Restatement of Agency's notice-to-principal rule for renunciation, which the corpus already flagged elsewhere as needing a sharper, sourced restatement rather than being taken as settled.

**Status:** proposed.

**Fixture:** `lifecycle-agent-renunciation` / `LAR-H-010-a` to `LAR-H-010-i` (9) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-renunciation/README.md)

---

#### LC-H-011. A partner's power to dissociate is effective immediately whether the dissociation is rightful or wrongful, and wrongfulness is a separate, later liability question

**Situation.** An agent acting as a partner in a partnership exercises their own power to end their role, in a way that breaches an agreement not to leave at that time.

**Human analog.** Delaware's Revised Uniform Partnership Act provision on a partner's power to dissociate. [Delaware Code, Title 6 §15-602](https://delcode.delaware.gov/title6/c015/sc06/index.html): "A partner has the power to dissociate at any time, rightfully or wrongfully, by express will pursuant to §15-601(1) of this title." The same section separately states: "A partner who wrongfully dissociates is liable to the partnership and to the other partners for damages caused by the dissociation."

**What should happen.** A verifier should treat an agent's self-initiated renunciation as immediately effective at the moment it is made, regardless of whether it breaches some other obligation. Whether the renunciation was wrongful is a separate question, resolved afterward, that determines liability, not one that delays, blocks, or reverses the loss of standing the renunciation itself causes.

**What a naive system gets wrong.** Treating a breach-of-duty renunciation as somehow less immediately effective than a clean one, or as needing to wait on a liability determination before the agent's authority actually ends, conflates two separate questions this domain keeps apart: whether authority ended, and whether ending it that way was a breach.

**Related invariant/open question.** Sharpens the general "agent renunciation" shape beyond what the corpus's existing Restatement-of-Agency renunciation entry establishes, since this domain explicitly names both the rightful and wrongful case as equally, immediately effective at the power level, with wrongfulness handled entirely as a downstream liability question.

**Status:** proposed.

**Fixture:** `lifecycle-agent-renunciation` / `LAR-H-011-a`, `LAR-H-011-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-renunciation/README.md)

---

### Principal unreachable

#### LC-H-012. A payment order requiring customer confirmation stays unconfirmed, not authorized by default, when the customer cannot be reached to complete the agreed procedure

**Situation.** A bank and its customer have agreed on a security procedure, such as a callback, meant to confirm that a payment order actually came from the customer before the bank acts on it. The bank cannot reach the customer to complete that confirmation step.

**Human analog.** UCC Article 4A's rule on verified payment orders. [Cornell LII, UCC §4A-202](https://www.law.cornell.edu/ucc/4A/4A-202): "a payment order received by the receiving bank is effective as the order of the customer, whether or not authorized, if (i) the security procedure is a commercially reasonable method of providing security against unauthorized payment orders" and the bank complies with it.

**What should happen.** A verifier should treat an order awaiting a required confirmation step as not established, not as authorized by a default and not as denied, while the principal remains unreachable to complete that step. What makes the order effective as the customer's is the bank's actual compliance with the agreed procedure, not the passage of time or a good-faith guess in the principal's absence.

**What a naive system gets wrong.** Treating an unreachable principal as either an implicit approval (since nothing said no) or an implicit denial (since nothing was confirmed) both manufacture a decision the underlying rule does not make. The correct state is indeterminate on this specific action until the procedure is actually completed, distinct from L7's unknown-revocation-state, since here nothing has yet been revoked. The question is whether the action was ever established as authorized in the first place.

**Related invariant/open question.** OPEN-QUESTIONS.md does not yet address reaffirmation gated on reaching an unreachable principal as its own category. The closest existing corpus entries (continuity-of-government devolution, lost-link UAS fallback) cover automatic fallback triggered by unreachability, not a required confirmation step that stays blocked, unresolved, and un-defaulted while the principal cannot be reached.

**Status:** proposed.

**Fixture:** `lifecycle-principal-unreachable` / `LPU-H-012-a` to `LPU-H-012-j` (10) (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-principal-unreachable/README.md)

---

### Time and scheduling

#### LC-C-008. A missing successor designation should fail open to a named statutory fallback, not fail closed like an unknown revocation

**Situation.** A role becomes vacant and the organization never issued an explicit order naming who acts in the meantime. A verifier looking for a successor designation finds none recorded.

**Human analog.** The Federal Vacancies Reform Act's default rule that the first assistant to a vacant Senate-confirmed office automatically becomes the acting officer, subject to a prior-service requirement and disqualification if the President has nominated that person. [US Government Accountability Office, GAO-02-272R](https://www.gao.gov/products/gao-02-272r): "the first assistant to the office of such officer shall perform the functions and duties of the office temporarily in an acting capacity."

**What should happen.** Absence of an explicit successor designation should resolve to a named default, whoever currently and durably holds the first-assistant role relative to the vacated one, checkable against its own eligibility conditions. It should not block all action or sit as indeterminate.

**What a naive system gets wrong.** A framework modeled only on L7's fail-closed rule for unknown revocation state will wrongly fail closed here too, and block a routine, lawful vacancy that the statute already solved with an affirmative default.

**Related invariant/open question.** L7 is about an unknown or stale revocation answer, which correctly fails closed. This is a different kind of unknown, an unknown successor designation, and the correct behavior is the opposite: it fails open to a specific, statutorily defined fallback identity with its own eligibility gate.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-C-008-a-default-successor-resolved`, `LC-C-008-b-no-declared-default`, `LC-C-008-c-eligibility-not-met`, `LC-C-008-d-rule-without-standing`, `LC-C-008-e-direction-from-a-party-with-no-tenure` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-C-014. A handover can require the incoming holder's acknowledgment, with authority staying put until it arrives

**Situation.** One air traffic controller relieves another at a live control position mid-shift. The transfer needs the incoming controller to receive and acknowledge a structured briefing before it is considered complete, not just the outgoing controller declaring itself off duty.

**Human analog.** FAA position relief briefing practice for controllers changing position. [SKYbrary Aviation Safety](https://skybrary.aero/articles/hand-overtake-over-operational-positions): "The taking-over controller should ensure that he/she has been able to assimilate all information relevant to a safe hand-over and should accept responsibility only after he/she is completely satisfied that he/she has a total awareness of the situation."

**What should happen.** The position's authority should stay with the outgoing holder until the incoming holder has both received and affirmatively acknowledged the required briefing content. An unacknowledged handoff attempt should leave authority with the outgoing holder, not default to either transferred or vacant.

**What a naive system gets wrong.** Modeling handover as a single timestamped event, where the old holder's authority ends and the new holder's begins together, has no way to represent a required acknowledgment step. It either transfers authority the instant the outgoing party stops acting, creating a window with no accountable holder, or requires no acknowledgment at all.

**Related invariant/open question.** None of L1 to L12 model a handover as a two-step, acknowledgment-gated protocol with defined content requirements. They treat transfer as effectively instantaneous once a triggering event occurs.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-C-014-a-outgoing-acts-before-acknowledgment`, `LC-C-014-b-incoming-acts-before-acknowledgment`, `LC-C-014-c-incoming-acts-after-acknowledgment`, `LC-C-014-d-outgoing-acts-after-acknowledgment`, `LC-C-014-e-acknowledgment-from-a-party-the-offer-does-not-name` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-C-015. Losing contact with a directing principal should trigger a pre-authorized fallback, not a freeze or silent continuation

**Situation.** An agent loses its communication channel to the principal actively directing it mid-task.

**Human analog.** FAA guidance on UAS lost-link procedures. [CFI Notebook](https://www.cfinotebook.net/notebook/remotely-piloted-aircraft/lost-link): "The lost link algorithm provides a safe manner of operation and retrieval of the aircraft when operator control is lost," executing preprogrammed behavior such as returning home, orbiting, or landing.

**What should happen.** Loss of live contact with a directing principal should trigger a pre-authorized fallback scope, not a full stop and not continuation of the last live instruction indefinitely. Restoration of contact should resume full live direction automatically. The fallback scope itself needs to be defined at grant time, before the disconnection happens, since it cannot be negotiated during the outage.

**What a naive system gets wrong.** Treating connectivity loss as equivalent to revocation grounds or freezes the agent even when a safe, pre-authorized autonomous behavior exists and is exactly what should happen. Treating connectivity loss as irrelevant lets the agent keep executing a stale instruction into conditions the principal never approved.

**Related invariant/open question.** L7 says an unknown or stale revocation answer must fail closed. This is different: the loss is of the live directing channel itself, not of revocation information, and the correct behavior is a specific pre-granted fallback scope rather than a blanket fail-closed stop.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-C-015-a-live-direction-present`, `LC-C-015-b-fallback-scope-active`, `LC-C-015-c-outside-the-fallback-scope`, `LC-C-015-d-no-fallback-recorded`, `LC-C-015-e-contact-restored` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

Variants: LC-C-010 (the same unreachability-triggers-fallback shape at organizational rather than single-agent granularity: continuity-of-government devolution to a pre-designated backup site when leadership at the primary seat cannot be contacted, per NSPD-51/PPD-40, with reconstitution required on restored contact rather than automatic resumption), E-016 (autonomous fallback authority activating only once round-trip time exceeds the decision window, and only for the pre-scoped action).

---

#### LC-C-017. A standing rotation schedule is its own form of pre-authorization, distinct from a one-time succession event

**Situation.** On a long-haul flight, a relief pilot swaps into the operating seat on a prebuilt schedule tied to a mandatory rest ledger, so the operating pilot can take required rest. This happens repeatedly, on a schedule, not in response to any incident.

**Human analog.** 14 CFR Part 117 flight and duty time limitations and rest requirements for augmented flightcrews. [Code of Federal Regulations via GovInfo](https://www.govinfo.gov/content/pkg/CFR-2019-title14-vol3/xml/CFR-2019-title14-vol3-part117.xml): "No certificate holder may assign and no flightcrew member may accept assignment to any reserve or duty with the certificate holder during any required rest period."

**What should happen.** A verifier should treat each scheduled swap as pre-authorized at grant time, checkable against the rest ledger, rather than requiring a fresh authorization event per swap. A swap that occurs off the pre-agreed schedule, or without the required preceding rest, should be flagged as anomalous even though the same two parties are involved.

**What a naive system gets wrong.** A system that only knows unplanned emergency handovers treats every routine scheduled swap as an ad hoc event needing its own justification, generating alert fatigue and missing the actual anomaly signal: a swap that deviates from the pre-agreed cyclical schedule or skips required rest.

**Related invariant/open question.** Distinguishes a pre-scheduled, cyclical, ledger-audited handover pattern between equal peers from both an unplanned peer-succession case and an office-bound succession case. The framework needs a concept of a standing rotation schedule as a form of pre-authorization, not a series of independent grants.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-C-017-a-scheduled-swap-pre-authorized`, `LC-C-017-b-swap-off-the-schedule`, `LC-C-017-c-required-rest-not-elapsed`, `LC-C-017-d-rest-state-not-recorded` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-C-025. Continuous-coverage roles need departure and successor designation to be a single atomic operation, not a sequence

**Situation.** A nuclear plant shift manager needs to step away from the control room briefly, short of a full shift change. For this class of position, even a momentary gap in who holds command is not tolerated.

**Human analog.** US Nuclear Regulatory Commission licensing requirements for control room command. Technical specifications filed at US nuclear plants require that during any absence of the Shift Supervisor from the control room, an individual with a valid Senior Reactor Operator license be designated to assume the control room command function. [US Nuclear Regulatory Commission, ADAMS Accession ML072831246](https://www.nrc.gov/docs/ML0728/ML072831246.pdf): "an individual...shall be designated to assume the control room command function" during any absence of the Shift Supervisor.

**What should happen.** A verifier for this class of position should treat "holder about to become unavailable with no successor yet designated" as a blocking condition on the departure itself, not as a gap to discover and flag afterward. The designation and the departure need to be a single atomic operation.

**What a naive system gets wrong.** A framework that treats handovers as sequential, where the old holder leaves and then a new one is found, permits exactly the kind of brief gap this rule exists to prevent. For a small number of safety-critical positions, that gap, even measured in seconds, is the actual defect being regulated against.

**Related invariant/open question.** A stronger, zero-gap-tolerance version of continuous coverage than anything in L1 to L12. The existing invariants discuss what happens once a gap is discovered, not a hard requirement that the departure operation itself be atomic with successor designation for certain safety-critical roles.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-C-025-a-atomic-relief`, `LC-C-025-b-gap-between-departure-and-designation`, `LC-C-025-c-after-the-designation`, `LC-C-025-d-designee-qualification-not-recorded`, `LC-C-025-e-designation-names-another-party` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

Variants: LC-C-021 (US Navy deck-and-conn transfer reaches the same zero-gap goal with a scripted two-event relinquish-then-assume ritual instead of an atomic departure-plus-designation record, and treats a gap between the two events as indeterminate rather than defaulting to either party) and LC-C-028 (surgeon incapacitation mid-incision adds that the action itself is non-pausable and actively degrading, so the zero-gap requirement carries no safety margin at all, unlike a monitoring role where the underlying process is not necessarily worsening during the gap).

---

#### LC-E-008. A long-running instance's remaining steps must resolve against the authority-policy version it started under, not the version deployed today

**Situation.** A long-running durable workflow instance, a multi-day negotiation or a multi-step approval pipeline, is mid-execution when the authority rules governing what it may do next are updated, for example a tighter spending scope is deployed. The instance's already-recorded history was built against the old rules.

**Human analog.** Temporal's documentation on workflow determinism. [Temporal docs](https://docs.temporal.io/workflows): "It has to make the same decisions when given the same history. It shouldn't depend on any values not recorded in the history which would be different between runs."

**What should happen.** The in-flight instance's remaining steps must resolve against a pinned, recorded version of the authority-policy it started under, at an explicit version boundary, rather than the currently-deployed rules. Jumping straight to current rules mid-replay is not a safety improvement, it makes the instance's next step inconsistent with steps it already took under the old rules.

**What a naive system gets wrong.** Assuming that a changed authority rule should immediately apply to every in-flight instance for safety. Applying it naively mid-replay corrupts the instance rather than protecting it, because a durable execution engine's own determinism requirement means the fix has to be an explicit, versioned cutover point, not a blanket immediate switch.

**Related invariant/open question.** Directly names the "Policy version" concept AUTHORITY-LIFECYCLE.md already lists among decisions and effects. It is also a narrower, concrete instance of the "work in flight" operational case, sharper than that case states it because for a replay-based execution engine the naive fix is actively wrong, not merely under-specified.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-008-a-pinned-version-still-permits`, `LC-E-008-b-control-before-the-cutover`, `LC-E-008-c-new-instance-pinned-to-the-tighter-version`, `LC-E-008-d-instance-without-a-pin`, `LC-E-008-e-pinned-version-not-resolvable` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-E-014. A recurring series can outlive the identity that scheduled it, with no automatic cleanup and no owner left to cancel it

**Situation.** An agent identity schedules a recurring automated action, such as a nightly reconciliation run, through a scheduling service that records the agent as the series' owner. The agent identity is later permanently decommissioned. The scheduling service has no defined behavior for "the owner no longer exists" and keeps firing occurrences, or leaves them stranded with no normal owner-initiated cancel path.

**Human analog.** Microsoft's own support guidance on a deleted Outlook/Exchange organizer's mailbox. [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/1098768/recurring-meeting-after-the-owner-mailbox-deleted): "For recurring meetings, it is not automatically deleted and will left as an orphaned meeting." [sic]

**What should happen.** A scheduling system must define what happens to a series when its owning identity is permanently removed, whether that is auto-cancel, reassignment to an organizational fallback principal, or freezing pending explicit reassignment. That has to be a designed behavior, not a silent gap that leaves the series firing under a principal that verification would now say does not exist.

**What a naive system gets wrong.** Assuming that removing an identity implicitly cleans up everything it owns, when a scheduled series is a separate record with its own lifecycle that a principal-removal process can easily miss entirely.

**Related invariant/open question.** Distinct from L1's ancestor-revocation rule because the series was never itself revoked, and there may be no delegation chain to revoke at all if the series was created directly by the now-removed identity acting as its own root. The gap is that identity removal and scheduled-series cleanup are two separate lifecycle events nothing here requires to be linked.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-014-a-before-owner-removal`, `LC-E-014-b-owner-authority-revoked`, `LC-E-014-c-owner-removed-with-nothing-revoked`, `LC-E-014-d-recorded-disposition-reassigns` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-E-018. A running scheduled occurrence keeps the identity it was created with. Only the next occurrence picks up a tightened template

**Situation.** An organization tightens the identity or scope template a recurring automated action runs under, editing the recurring job's definition. An occurrence already created and mid-execution under the old, broader template does not get the new template applied retroactively.

**Human analog.** Kubernetes CronJobs and standard object semantics. [Kubernetes docs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/): "Modifying a CronJob, such as adding, updating or deleting a CronJob, does not affect the Jobs that are already running."

**What should happen.** An auditor checking a completed occurrence must check the identity or scope that occurrence was actually created with, not the job definition's current state, since those can legitimately differ. An operator tightening a recurring job's scope must understand that already-running occurrences are unaffected and, if urgent, need to be separately terminated or reissued.

**What a naive system gets wrong.** Assuming that editing a recurring job's identity template takes effect immediately for everything running under that job's name, when the running instance and the job template are separate objects with separate lifecycles. An urgent scope tightening does not actually reach an occurrence already in flight.

**Related invariant/open question.** A template-versus-instance distinction specific to recurring execution that none of L1-L12 name. Related to L9's point that a verifier resolves the key authorized at issuance rather than at verification time, but here the pinned object is the identity template an occurrence was created under, not a signing key.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-018-a-occurrence-keeps-its-creation-template`, `LC-E-018-b-next-occurrence-under-the-tightened-template`, `LC-E-018-c-occurrence-template-version-not-recorded`, `LC-E-018-d-control-read-under-the-tightened-template` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-E-019. Authority stays valid through a scheduled wind-down, not cut off the instant termination begins

**Situation.** A workload undergoing a graceful rolling replacement receives a termination signal while it still has an in-flight request being processed under its assigned identity. It needs a few more seconds to finish and make its final authorized call.

**Human analog.** Kubernetes pod termination. [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/): "The kubelet triggers the container runtime to send a TERM signal to process 1 inside each container. Once the grace period has expired, the KILL signal is sent to any remaining processes." The documentation confirms the grace-period mechanism itself. That the pod's own assigned identity and permissions remain valid throughout that window, rather than being cut at the moment the signal is sent, is this document's inference from how Kubernetes pods are known to work, not a line quoted from the page above.

**What should happen.** The instance's authority should remain valid and checkable for the duration of its graceful-shutdown window. A verifier should not treat "this instance has begun termination" as equivalent to "this instance's authority is now revoked." Those are separate facts, and its final in-flight call during the grace period should succeed exactly as it would have before termination began.

**What a naive system gets wrong.** Treating the start of a termination signal as an implicit revocation event, aborting otherwise-legitimate, already-authorized work purely because of an orchestration event that has nothing to do with whether the instance's authority is still valid.

**Related invariant/open question.** L8 distinguishes suspension (pauses use, can be lifted) from revocation (terminal). Termination-in-progress is neither, a third, scheduled-wind-down state L8 does not name.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-019-a-inside-the-grace-window`, `LC-E-019-b-after-the-grace-window`, `LC-E-019-c-revoked-during-the-wind-down`, `LC-E-019-d-no-declared-grace-bound` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-E-020. A scheduled job's permissions are bound to its creator's identity at schedule time, and the scheduler's own docs are silent on what happens once that identity is gone

**Situation.** A scheduled recurring job executes with the permissions of whichever role scheduled it. That role is later dropped, or has its privileges revoked, while the job definition itself sits untouched between occurrences.

**Human analog.** `pg_cron`'s stated execution model. [pg_cron README](https://github.com/citusdata/pg_cron): "For security, jobs are executed in the database in which the cron.schedule function is called with the same permissions as the current user." The project's documentation does not say what happens once that role no longer exists or no longer holds its former privileges.

**What should happen.** A scheduler binding a recurring job's permissions to a named identity must explicitly define what happens at the next occurrence once that identity is gone or downgraded, whether that is a deterministic failure with a clear reason, automatic cancellation, or a documented reassignment path, rather than leaving the answer to whatever the runtime happens to do when a nonexistent or weakened role is asked to execute something.

**What a naive system gets wrong.** Assuming the job's own definition being untouched means it remains a stable, well-understood piece of authority, when its actual executable permission was always parasitic on a separate identity record decommissioned through a completely different process, with no defined interaction between the two.

**Related invariant/open question.** Sits in the same gap as the "work in flight" operational case, but for dormant scheduled authority rather than a single operation already running. The job is not in flight at decommissioning, it is dormant between occurrences, so there is nothing to interrupt, yet the next occurrence's authority is already silently compromised.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-020-a-creator-grant-unchanged`, `LC-E-020-b-creator-narrowed-job-definition-untouched`, `LC-E-020-c-narrowed-but-inside`, `LC-E-020-d-no-creator-grant-recorded` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-G-007. A validity-period check is run against the checking party's own clock at check time, not the issuer's claimed clock

**Situation.** A specification defines a time-bounded credential's validity as covering "the current time." It does not name whose clock that phrase refers to.

**Human analog.** RFC 5280, the X.509 certificate and CRL profile, describing basic certificate path-validation processing. [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280): "The certificate validity period includes the current time," and separately, "At the current time, the certificate is not revoked." Both are steps in the path-validation procedure Section 6 defines as something the party validating the certificate performs.

**What should happen.** "The current time" in a validity check means the time of the party doing the check, at the moment they check, not any time the issuer or the artifact itself claims. Two different verifiers checking the same artifact at different moments can reach different answers about whether it is currently valid, and that is not a contradiction, because each is answering "valid now, by my clock," not "valid at some single shared instant."

**What a naive system gets wrong.** Reading "current time" as if it names one universal instant everyone must agree on, rather than a per-verifier, per-check evaluation. That leads to treating two verifiers' differing answers as evidence one of them is broken, when both can be correctly answering the only question the check actually asks.

**Related invariant/open question.** Sits next to LC-F-013 (gateway-agent clock skew causing a valid artifact to be rejected), but is the specification-level question underneath it: which clock the check is defined to run against in the first place, before any skew-tolerance policy is layered on top.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-G-007-a-inside-by-the-checking-party-clock`, `LC-G-007-b-expired-by-a-second-checking-party-clock`, `LC-G-007-c-not-yet-effective-by-a-third-clock`, `LC-G-007-d-no-clock-attestation` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-G-008. A single external time source with no independent check can silently go wrong and nothing downstream can detect it

**Situation.** A device derives its notion of the current date entirely from one external broadcast signal. That signal's own encoding has a known, periodic wraparound: after a fixed count, its internal counter resets to zero and starts over, producing a date far in the past that is otherwise well-formed and indistinguishable, to the device, from a correct one.

**Human analog.** The GPS week number rollover, arising from the ten-bit week counter in the legacy GPS navigation message. [Wikipedia, GPS week number rollover](https://en.wikipedia.org/wiki/GPS_week_number_rollover): "The GPS week number rollover is a phenomenon that happens every 1,024 weeks, or about 19.6 years." And: "Software that is not coded to anticipate the rollover to zero may stop working or could be moved back in time by a multiple of approximately 20 years."

**What should happen.** A system with exactly one external time source and no independent way to sanity-check it has no basis for treating that source's output as ground truth rather than merely the best available claim. Where a time-bounded authority decision depends on that single source, the decision should carry a marker of which source it used and how, if at all, it was cross-checked, so a downstream reviewer can tell a genuinely fresh, correct reading from a silently wrapped-around one.

**What a naive system gets wrong.** Trusting a single time source because it is external and normally accurate, with no fallback or cross-check for its own known failure modes. The device cannot tell a correct reading from a wrapped-around one from the inside, because both are well-formed.

**Related invariant/open question.** A different failure shape from LC-F-014 (an issuer's time reference actively spoofed or jammed by an attacker). Here nothing is attacking the source. The source's own encoding periodically and predictably produces a wrong answer, arguably worse because there is no adversary event to detect.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-G-008-a-cross-checked-reading`, `LC-G-008-b-wrapped-single-source`, `LC-G-008-c-cross-check-disagrees-past-the-bound`, `LC-G-008-d-no-source-recorded` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

#### LC-G-009. Two legitimately-run clocks can disagree by design during a defined window, and neither reading is the wrong one

**Situation.** During a leap-second event, one organization's servers spread the extra second gradually across a window before and after the leap, while another organization's servers apply it as a single discrete step at the moment UTC defines it. For the duration of that window, the two organizations' clocks report different times for what is, by international timekeeping convention, the same real moment.

**Human analog.** Google's "leap smear" technique for its public NTP service. [Google, Leap Smear](https://developers.google.com/time/smear): "At the beginning of the leap second, smeared time is just under 0.5 s behind UTC. UTC inserts an additional second, while smeared time continues uninterrupted."

**What should happen.** A verifier comparing timestamps from two sources during a declared smear or leap-second window needs a tolerance for exactly this kind of divergence, because neither system is malfunctioning and neither timestamp is the authoritative one. This is distinct from ordinary clock skew: the disagreement is a known, bounded, temporary property of two systems each correctly following their own published time-handling policy, not drift or error in either.

**What a naive system gets wrong.** Treating any mismatch between two timestamps as evidence of clock failure, tampering, or replay. During a declared leap-second smear window, a mismatch of up to roughly half a second between a smeared and an unsmeared source is the expected, correct behavior of both, not a fault in either.

**Related invariant/open question.** Distinct from LC-F-012 (a leap-second insertion crashing verifier processes fleet-wide) and LC-F-022 (last-writer-wins timestamp resolution discarding a legitimate write). Those are failures the leap second causes elsewhere. This case is about two simultaneously valid but differing time attestations, neither of which invalidates the other.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-G-009-a-declared-smear-window`, `LC-G-009-b-no-declared-window`, `LC-G-009-c-divergence-past-the-declared-bound`, `LC-G-009-d-two-clocks-that-agree` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

### Credential events

#### LC-D-001. A third party's own breach disclosure has to become a revocation-relevant trigger, even though the delegating org revoked nothing itself

**Situation.** An org grants a scoped delegation to a third-party integration, a CI provider or a deploy tool. The integration's own token store is later compromised, and the stolen tokens are replayed directly against the org's resource API, bypassing the org's own identity boundary entirely. The org never revoked anything and has no record that a compromise occurred until the integrator discloses it.

**Human analog.** GitHub's 2022 disclosure that OAuth tokens issued to two third-party integrators, Heroku and Travis CI, were stolen and used to access private repositories across dozens of organizations. [GitHub blog](https://github.blog/news-insights/company-news/security-alert-stolen-oauth-user-tokens/): "The attacker authenticated to the GitHub API using the stolen OAuth tokens issued to Heroku and Travis CI."

**What should happen.** A verifier needs an ingestion path for a third-party integrator's own breach disclosure as a revocation-relevant event, distinct from anything the org itself initiated. On disclosure, every chain rooted at that integrator's subject identity becomes indeterminate until re-attested, and the org needs a way to enumerate every grant it has issued to a given subject on demand, before the integrator says anything went wrong.

**What a naive system gets wrong.** A system that only reacts to revocation requests it initiates itself has no trigger here, since the org never revoked anything. Treating "we didn't revoke it" as equivalent to "it's still valid" misses that the trigger can come from outside the org's own chain-checking machinery entirely.

**Related invariant/open question.** L1 assumes the verifier discovers an ancestor is revoked through its own chain-checking machinery. This is the harder case where the party that must supply the revocation-relevant fact is an integrator the org never directly audited, and notice arrives out of band.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-001-a-third-party-disclosure-is-a-trigger`, `LC-D-001-b-reattested-after-disclosure`, `LC-D-001-c-unattributed-compromise-claim-is-not-a-trigger`, `LC-D-001-d-later-finding-does-not-rewrite-the-earlier-record` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

**Variants:** LC-D-015 (Toyota T-Connect, the trigger is public exposure of the org's own credential rather than an integrator's breach disclosure), LC-D-018 (Salesloft Drift, the same integrator-compromise mechanism, but a single disclosure has to become a correlated revocation-relevant event across more than 700 independently administered downstream orgs at once).

---

#### LC-D-003. "Believed unused" is not the same as "verified inventory," and the gap between them is exactly where this incident happened

**Situation.** In response to a vendor breach, an org rotates credentials broadly, but the rotation tooling relies on a human judgment call about which service tokens are "still in active use." A token and account marked safe to skip, because someone believed them unused, turn out not to be, and become the attacker's entry point.

**Human analog.** Cloudflare's Thanksgiving 2023 incident, following the Okta support-system breach. [Cloudflare blog](https://blog.cloudflare.com/thanksgiving-2023-security-incident): "mistakenly it was believed they were unused. This was incorrect and was how the threat actor first got into our systems."

**What should happen.** A rotation-on-ancestor-compromise event must be complete over the actual grant set traceable to the compromised ancestor, not the subset someone currently believes is active. "Believed unused" is not a valid substitute for a verified inventory.

**What a naive system gets wrong.** Treating "rotate everything derived from the compromised ancestor" as equivalent to "rotate everything an admin remembers is in use." That silently leaves a live, exploitable descendant standing, exactly L12's completeness problem, playing out concretely.

**Related invariant/open question.** A direct, real-world instance of L12: what a rotation claims to have covered versus what actually exists. Motivates why a "believed complete" inventory is not a valid basis for a completeness claim.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-003-a-reach-over-the-graph-not-the-believed-list`, `LC-D-003-b-both-bases-agree-so-agreement-establishes-nothing` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

Variants: D-028 (a source-code leak surfacing credentials embedded over years, the same no-rotatable-inventory problem reached from the leak side rather than the rotation side).

---

#### LC-D-004. A single compromised operator identity can be an implicit ancestor over many independent trees at once

**Situation.** Malware on one engineer's laptop steals a session. That engineer's ordinary job included minting production access tokens for every customer on the platform. The compromise is not a single-tenant event. It is an ancestor-level event for every tenant whose secrets that role could reach, even though no individual tenant's own credentials were directly touched.

**Human analog.** The January 2023 CircleCI incident. [CircleCI's own incident report](https://circleci.com/blog/jan-4-2023-incident-report): "the unauthorized third party was able to access and exfiltrate data from a subset of databases and stores, including customer environment variables, tokens, and keys."

**What should happen.** Revocation and rotation scope after compromising a high-fan-out operator identity has to be computed from that identity's reachable authority graph, every secret it could mint or read, not from a narrower "only this session's own artifacts" scope. Everything reachable through that role is presumptively compromised until proven otherwise.

**What a naive system gets wrong.** Scoping incident response to "revoke the compromised session and whatever it directly issued" undercounts the blast radius badly when the compromised identity's role is itself a highly-privileged ancestor over many independent trees. The actual exposed set is the transitive closure of what the role could reach, not what it is recorded as having touched.

**Related invariant/open question.** L1 covers revoking a known ancestor invalidating known descendants in one tree. This is the harder question of what "ancestor" even means when a compromised operator identity is an implicit ancestor over many independent principals' trees at once, a blast-radius computation problem none of L1-L12 address.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-004-a-operator-identity-reaches-an-independent-tree`, `LC-D-004-b-operator-identity-with-no-edge-to-this-tree` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-D-009. A documented scope means nothing if the resource-side boundary never actually enforces it

**Situation.** A vendor is granted credentials scoped, on paper, to one narrow function. Nothing in the actual network configuration restricts that vendor's access to that function. So when the vendor's own systems are compromised through an unrelated channel, the stolen credentials reach far more than the paperwork ever authorized.

**Human analog.** The 2013 Target breach: attackers used network credentials stolen from Fazio Mechanical, an HVAC and refrigeration vendor whose own description of its access was narrow. [Krebs on Security](https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/) quotes Fazio's stated scope as "exclusively for electronic billing, contract submission and project management," access that, unsegmented, reached point-of-sale systems that had nothing to do with billing.

**What should happen.** A scope statement in a delegation is only meaningful if the enforcement boundary actually restricts execution to that scope. The documented scope and the technically reachable scope need to be checked against each other as a distinct verification step, because a narrow-looking delegation over an unsegmented resource is not narrow at all in practice.

**What a naive system gets wrong.** Verifying "this delegation's stated scope is billing-only" and treating that as sufficient. That checks the paperwork, not the plumbing, and the two can diverge for years with nothing in the delegation-verification layer ever noticing.

**Related invariant/open question.** None of L1-L12 address whether the resource-side enforcement boundary actually implements a delegation's stated scope. They assume it does. This is the clearest sourced instance of "resource identity reuse / target binding" the corpus produced.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-009-a-enforced-scope-exceeds-declared-scope`, `LC-D-009-b-no-reachable-scope-attestation`, `LC-D-009-c-enforced-scope-contained` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-D-010. A credential with no natural end, issued for a purpose that ended, is a standing liability no chain-verification check can catch

**Situation.** An account tied to a discontinued purpose is left enabled indefinitely, because nobody owned the task of disabling it once the purpose ended, and it was never given an expiry in the first place.

**Human analog.** The 2021 Colonial Pipeline ransomware attack, which began through a legacy VPN account. [The Hacker News](https://thehackernews.com/2021/06/hackers-breached-colonial-pipeline.html): "a legacy VPN profile that was not intended to be in use."

**What should happen.** Delegations and credentials issued for a bounded purpose should carry an expiry tied to that purpose's expected lifetime by default, rather than defaulting to indefinite validity. A credential with no natural end and no owner responsible for ending it is a standing liability that chain-verification correctness cannot catch, because by every technical measure the chain is still perfectly valid.

**What a naive system gets wrong.** Only invalidating credentials on explicit revocation or a stated expiry misses the much larger set that were simply never given either, because their issuers assumed "someone will turn this off" without ever encoding that as an actual expiry or ownership record.

**Related invariant/open question.** L10 distinguishes expiry from revocation for credentials that already have a defined end. This is a gap in how grants are issued in the first place, a credential with a foreseeable natural end that was never given one.

**Status:** proposed.

**Fixture:** `lifecycle-purpose-exhaustion` / `PXE-03-reject-second-purchase-wednesday`, `PXE-12-reject-after-grant-not_after-expiry-and-exhaustion-coexist` (candidate, not yet merged)

---

#### LC-D-011. Inheriting another organization's entire root of trust by acquisition is not itself a re-verification event

**Situation.** An acquiring company absorbs an acquired company's agent fleet, credential infrastructure and delegation roots wholesale, and keeps operating them under the acquired company's pre-existing trust assumptions for years without re-verifying or re-issuing under its own root of trust.

**Human analog.** Marriott's 2016 acquisition of Starwood. Nearly two years later Starwood's legacy reservation systems were still running on inherited infrastructure, and a compromise that began in 2014, before the acquisition, went undetected the entire time. [CSO Online](https://www.csoonline.com/article/567795/marriott-data-breach-faq-how-did-it-happen-and-what-was-the-impact.html): "Marriott purchased Starwood in 2016, but nearly two years later, the former Starwood hotels hadn't been migrated to Marriott's own reservation system and were still using IT infrastructure inherited from Starwood."

**What should happen.** An acquisition should trigger mandatory re-verification of every inherited delegation root and credential within a defined timeline, with the inherited environment treated as untrusted until that re-verification completes, rather than grandfathered in indefinitely on the acquired entity's own historical assumptions.

**What a naive system gets wrong.** A system that treats "this chain was valid under the acquired entity's root before the acquisition" as sufficient to keep trusting it afterward never forces the re-verification that would catch a compromise that predates the deal. The acquirer inherits every unaudited assumption baked into the acquired root, not just its assets.

**Related invariant/open question.** None of L1-L12 address organizational succession at the level of an entire root of trust being absorbed into another organization's trust domain. L2 to L4 cover succession within one delegation tree under a continuing root, not the wholesale inheritance of a different root.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-011-a-inherited-root-past-its-reattestation-deadline`, `LC-D-011-b-inherited-root-inside-its-deadline`, `LC-D-011-c-inherited-root-reestablished` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

Variants: B-015 (a business-unit spin-off requiring a fresh grant from the new independent entity, rather than an acquisition inheriting an existing root).

---

#### LC-D-014. When an issuer's own issuance log cannot be trusted, per-artifact revocation is the wrong remedy

**Situation.** A root-of-trust issuer's signing infrastructure and issuance logs are compromised together, so a verifier cannot distinguish legitimately issued descendant chains from attacker-forged ones anywhere in the tree for the compromise window.

**Human analog.** The 2011 DigiNotar certificate authority compromise. The final investigation found certificate serial numbers on CA servers that did not match DigiNotar's own official records, meaning the company could not establish the complete set of certificates it had actually issued during the attack. [Threatpost](https://threatpost.com/final-report-diginotar-hack-shows-total-compromise-ca-servers-103112/77170/): "Serial numbers for certificates that did not match the official records of DigiNotar were recovered on multiple CA servers... indicating that these servers may have been used to issue additional and currently unknown rogue certificates."

**What should happen.** When an issuer's own issuance-log integrity cannot be established for a given window, a verifier should treat every chain rooted at that issuer during that window as not established by default, with the burden on each chain holder to re-establish authority from a re-verified root, rather than attempting selective per-chain revocation against log data that cannot support that precision.

**What a naive system gets wrong.** A system that always tries to enumerate and individually revoke "the bad ones" assumes the revocation list itself is trustworthy. When the compromise reaches the issuer's own logging and issuance path, that assumption is exactly what fails, and per-artifact revocation becomes false precision over data that cannot support it.

**Related invariant/open question.** L1 assumes a verifier can establish that a specific ancestor is revoked and treats that as sufficient. This case is about the prior question of whether the issuer's own records are trustworthy enough to identify which ancestors to revoke at all, a precondition L1 does not examine.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-014-a-issuance-log-integrity-unestablished-for-the-window`, `LC-D-014-b-issued-outside-the-covered-window`, `LC-D-014-c-reestablished-from-a-reverified-root` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

Variants: F-031 (a transport-layer memory bug leaking active delegation tokens out of process memory, raising the same proactive-rotation-over-the-whole-exposure-window question), F-032 (a multi-tenant proxy bug leaking one tenant's credentials into another tenant's response, the same question at the proxy layer rather than at TLS termination).

---

#### LC-D-025. "Authority is currently valid" and "a complete record exists of what was done under it" are different claims a verifier answers separately

**Situation.** An outsourced support role is legitimately scoped to view sensitive customer data as part of its ordinary function. Some holders of that access are bribed to misuse it within that same valid scope. The org detects and terminates the involved principals before an extortion attempt surfaces, but the data already copied out cannot be recovered by the termination.

**Human analog.** Coinbase's May 2025 disclosure that criminals bribed a number of its outsourced, India-based customer support contractors to copy customer data, which was then used in a $20 million extortion attempt. [The Hacker News](https://thehackernews.com/2025/05/coinbase-agents-bribed-data-of-1-users.html): "What these attackers were doing was finding Coinbase employees and contractors based in India who were associated with our business process outsourcing or support operations, that kind of thing, and bribing them in order to obtain customer data."

**What should happen.** Revoking a misbehaving principal's authority correctly answers whether it can still act. It does not answer what that principal already did while its authority was valid. That second question needs its own accounting, built from evidence of exercised authority during the valid window, and a verifier should not conflate "no longer valid" with "already accounted for."

**What a naive system gets wrong.** Treating "we revoked their access" as having closed the incident conflates stopping future authorized action with establishing what happened during the entire window the authority was, by every technical measure, valid and properly scoped. A validly scoped grant misused for its whole active duration leaves a gap no revocation, however prompt, can retroactively close.

**Related invariant/open question.** Distinct from L12's teardown-completeness framing, which is about whether a descendant list was complete at a boundary. This is about whether the record of what a still-valid grant was actually used for is complete, a related but separate completeness claim about exercised authority rather than about descendant enumeration.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-025-a-revoked-and-accounting-not-established`, `LC-D-025-b-revoked-and-accounting-established` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-D-029. A correctly-resolved historical key proves who signed, not what was actually built

**Situation.** An attacker compromises a vendor's build and code-signing infrastructure and uses the vendor's own legitimate signing key to sign a malicious update. The signature is, by every cryptographic measure, completely valid and correctly attributable to the legitimate key. What it attests to, that the build process produced this artifact honestly, is false.

**Human analog.** The 2020 SolarWinds/SUNBURST compromise. [ReversingLabs](https://www.reversinglabs.com/blog/sunburst-the-next-level-of-stealth): "The build infrastructure was compromised. In addition, the digital signing system was forced to sign untrusted code."

**What should happen.** Signature verification needs to be paired with independent build-provenance attestation, a reproducible build, a separate transparency log of what was actually built and when, rather than treating "signed by the vendor's key" as equivalent to "produced by the vendor's legitimate process." The two claims are only equivalent if the pipeline feeding the key is also verified uncompromised, and no amount of correct key-version resolution can establish that on its own.

**What a naive system gets wrong.** Checking only cryptographic signature validity, which makes a build-pipeline compromise invisible. The signature passes every check a verifier has, because the compromise happened upstream of the key, not at the key.

**Related invariant/open question.** L9 addresses selecting the historically correct key version at issuance time, treating key rotation as distinct from delegation revocation. This is a different failure entirely: the correct key, used correctly, on an artifact the process itself made illegitimate, a gap key-version resolution alone cannot close.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-029-a-no-provenance-attestation`, `LC-D-029-b-provenance-attestor-is-the-signing-key-holder`, `LC-D-029-c-independent-provenance-attestation` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-D-033. Adding a new authorized device to an identity needs the same scrutiny as issuing a new delegation, regardless of which internal path added it

**Situation.** An identity or authenticator provider's internal privileged tooling can attach a new authorized device or key to an existing end-user identity. When that internal tooling is itself compromised, an attacker never has to touch the end user's own credential. It mints itself a new, equally legitimate-looking authorizer attached to the victim's identity through the provider's own trusted internal path.

**Human analog.** The 2022 Twilio breach, in which attackers who compromised Twilio's internal systems registered unauthorized additional devices onto a number of existing Authy two-factor accounts. [BleepingComputer](https://www.bleepingcomputer.com/news/security/twilio-breach-let-hackers-gain-access-to-authy-2fa-accounts/): "the threat actor that gained access to its infrastructure on August 4 has also accessed accounts of 93 Authy users and linked devices to those accounts."

**What should happen.** Adding a device or key to an existing identity should be a discrete, auditable, notifiable event from the affected principal's perspective, equivalent in sensitivity to issuing a new delegation, regardless of whether it came through a customer-facing flow or an internal admin path. Presence on an authorized-devices list is not by itself evidence that the addition was a properly authorized act.

**What a naive system gets wrong.** A system that checks only "is this device on the authorized list for this identity" treats every entry on that list as equally legitimate regardless of how it got there. It has no way to distinguish a device the account owner added from one an attacker added through compromised internal tooling, because both produce an identical-looking valid entry.

**Related invariant/open question.** None of L1-L12 address the provenance of how an authorized credential or device came to be attached to an identity. The invariants assume a delegation's presence in a valid state is the relevant fact, but this case shows presence alone is insufficient without knowing whether the addition itself was properly authorized.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-D-033-a-authorizer-with-no-addition-record`, `LC-D-033-b-addition-attestor-standing-not-declared`, `LC-D-033-c-every-authorizer-attested` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-D-034. "Test" or "legacy" as a label is not the same as "test" or "legacy" as a validity fact

**Situation.** A non-production test application was granted broad consent by a highly privileged user years earlier, for a testing purpose that concluded long ago. The consent grant persists at its original elevated privilege level indefinitely, because nothing ever tied its validity to the purpose's lifespan.

**Human analog.** The Microsoft/Midnight Blizzard nation-state intrusion disclosed January 2024. [Microsoft Security blog](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/): "The threat actor then used the legacy test OAuth application to grant them the Office 365 Exchange Online full_access_as_app role, which allows access to mailboxes."

**What should happen.** Consent grants issued for a stated, bounded purpose should default to expiry at that purpose's natural conclusion. An org needs a periodic, systematic sweep of high-privilege consent grants held by non-production applications, rather than relying on the application's own "test" designation to imply reduced risk.

**What a naive system gets wrong.** Treating a consent grant as valid until explicitly revoked, with no link to the stated purpose's lifecycle. "Nobody uses this anymore" is invisible to any verifier that only checks grant validity.

**Related invariant/open question.** Same underlying gap as LC-D-010 (purpose-bound credential, no expiry), recurring in the OAuth-consent domain at a much higher privilege tier, against a nation-state actor. Maps to L10 and to the general shape of "expiry or exhaustion incl. purpose complete."

**Status:** proposed.

**Fixture:** `lifecycle-purpose-exhaustion` / `PXE-03-reject-second-purchase-wednesday`, `PXE-08-reject-unauthenticated-completion` (candidate, not yet merged)

---

#### LC-F-008. A verifier that checks status entirely offline against a synced snapshot needs its own evidence category, not a degraded live check

**Situation.** An enforcement point for a fleet of field-deployed agents (for example, no outbound connectivity for the duration of a task) checks delegation status against a status list synced before the task began. Nothing that happens to the agent's authority during the task can reach the enforcement point until the next sync. This is the deployment's intended design, not a failure to fix.

**Human analog.** The W3C Bitstring Status List spec is built to support exactly this pattern. [W3C Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/): "It is possible for verifiers to increase the privacy of the holder... by caching status lists that have been fetched from remote servers."

**What should happen.** Authority checked entirely offline against a pre-synced list must be evidenced with the sync timestamp and treated as valid only up to a deployment-declared offline-confidence window, distinguishable after the fact from a decision made against a live resolver.

**What a naive system gets wrong.** Recording an offline-checked allow identically to a live-checked allow, so a post-hoc audit can't tell how stale the authority basis for a given action actually was.

**Related invariant/open question.** None of L1-L12 name a bounded-offline-snapshot evidence category as distinct from a degraded live check. This is a design choice, not an outage, and needs its own evidence shape.

**Status:** proposed.

**Fixture:** `conflicting-status-sources` / `CSS-09-offline-snapshot-within-declared-bound-admits`, `CSS-10-offline-snapshot-past-declared-bound-not-established`, `CSS-11-offline-snapshot-revoked-denies` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/conflicting-status-sources/README.md)

Variants: LC-F-002 (a protocol migration leaves old verifiers with no working check at all and no signal they've stopped checking, not a deliberate bounded-offline design), LC-F-003 (staleness tracks a shipped runtime's update cadence rather than a single session's fixed sync point), LC-F-007 (a cache that could refresh live simply outlives its declared ttl, rather than a verifier with no live path by design), LC-F-010 (checking is deliberately disabled for privacy with no replacement snapshot at all, not degraded to a bounded offline one).

---

#### LC-F-013. A clock-skew rejection is a third category, neither expiry nor revocation

**Situation.** A delegation artifact carries an issued_at and a validity window. The enforcement gateway's clock and the agent's clock disagree by more than the deployment's configured tolerance. The gateway rejects an artifact that is, by any external reference clock, still inside its valid window.

**Human analog.** Kerberos rejects an authenticator when client and server clocks differ by more than a configured maximum skew. [MIT Kerberos documentation](https://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-admin/Clock-Skew.html): "Kerberos V5 is set up to reject ticket requests from any host whose clock is not within the specified maximum clock skew of the KDC."

**What should happen.** A skew-triggered rejection must be evidenced and reported as a clock-disagreement denial, distinct from an expiry or revocation denial, so operators fix clock sync instead of investigating a nonexistent authority problem. The artifact itself is not invalidated. Only this verification attempt is indeterminate.

**What a naive system gets wrong.** Logging a skew rejection identically to an expiry rejection, so operators can't tell "this credential's time is up" from "these two clocks disagree," and may reissue credentials repeatedly without fixing the actual clock problem.

**Related invariant/open question.** L10 distinguishes expiry from revocation for evidence purposes. Clock-skew rejection is a third category neither invariant names: a disagreement about what time it currently is, not a statement about the grant itself.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-F-013-a-clock-disagreement-is-its-own-outcome`, `LC-F-013-b-expiry-with-clocks-agreeing`, `LC-F-013-c-clocks-agree-inside-the-window` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

Variants: LC-F-011 (many independent agents' own clocks are simultaneously wrong, a fleet anomaly to detect and correlate, not a single gateway-agent disagreement to tolerate case by case).

---

#### LC-F-033. Systemic issuer misbehavior, once found, escalates to distrusting the whole issuer, not to revoking the chains that got caught

**Situation.** Independent monitoring of an APS root or intermediate issuer's public issuance log reveals it has been issuing delegation chains outside its stated policy over an extended period, discovered by third-party observers rather than self-reported. The response needed is not revoking a handful of bad chains but reassessing everything that issuer ever signed.

**Human analog.** Symantec's certificate-authority business was required to publish to Certificate Transparency logs, and the resulting visibility surfaced years of mis-issuance. [arkadiyt.com analysis](https://arkadiyt.com/2018/02/04/quantifying-untrusted-symantec-certificates/): "In January 2017, it came to light that Symantec had misissued at least 30,000 certificates over a period of several years." Major platforms then withdrew trust from the issuer as a whole rather than chain by chain. [sslmate.com CA failure history](https://sslmate.com/resources/certificate_authority_failures): "Symantec is ultimately distrusted by all major platforms due to further malfeasance."

**What should happen.** A detected pattern of systemic issuer misbehavior, discovered externally, must trigger a distinct escalation path from an individual revocation: reassessment and eventual distrust of the issuer's whole population, with its own evidence trail of what was detected, by whom, and over what period, rather than a series of one-off revocations.

**What a naive system gets wrong.** Treating each mis-issued chain found in the log as an independent one-off revocation, missing that the pattern itself is evidence the issuer's whole population needs re-evaluation, not just the specific instances that happened to be caught.

**Related invariant/open question.** None of L1-L12 address detecting systemic issuer-level compromise via independent transparency-style monitoring, or the escalation from individual revocation to distrust of an entire issuer's population.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-F-033-a-issuer-population-trust-not-established`, `LC-F-033-b-issuer-population-reattested` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-G-001. A planned key rotation at the end of a declared cryptoperiod is not an investigation trigger

**Situation.** An authority issuer signs artifacts with a key that has a defined cryptoperiod set at generation. The cryptoperiod ends on schedule. No compromise is suspected. The issuer rotates to a new key as planned.

**Human analog.** NIST SP 800-57 Part 1 Rev. 5, the federal cryptographic key-management recommendation. [NIST SP 800-57 Part 1 Rev. 5 (PDF)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf): "A cryptoperiod is the time span during which a specific key is authorized for use by legitimate entities or the keys for a given system will remain in effect." The same section treats compromise as a separate, early-ending event: "If a key is compromised, its cryptoperiod shall no longer be considered valid."

**What should happen.** A planned rotation at the end of a declared cryptoperiod needs no re-examination of what the outgoing key signed. The boundary was set at issuance, not discovered after the fact, and the outgoing key's signatures stay valid under L9 for the artifacts they cover. A verifier should distinguish this sharply from a compromise-triggered rotation, which does require re-examining what the key may have touched.

**What a naive system gets wrong.** Treating every key rotation, planned or not, as a signal to re-audit historical artifacts. That conflates a routine, pre-declared boundary with an incident, wasting effort on every scheduled rotation and, worse, desensitizing reviewers so a real compromise rotation gets the same shrug as a planned one.

**Related invariant/open question.** Extends L9 (key rotation is not delegation revocation) with a distinction the invariant does not itself draw: a rotation's planned-versus-compromise status changes what a verifier owes it, even though neither kind invalidates artifacts signed before the boundary.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-G-001-a-planned-rotation-opens-no-suspect-window` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-G-002. Unknown onset of a key compromise forces the suspect window to start at exposure, not at discovery

**Situation.** A widely deployed cryptographic library ships a flaw that lets an attacker read private key material from a vulnerable server's memory, without leaving any trace of having done so. The flaw is fixed roughly two years after it was introduced. For any given server that ran the vulnerable version, whether and when it was actually exploited during that window cannot be established after the fact.

**Human analog.** The 2014 Heartbleed bug (CVE-2014-0160) in OpenSSL. [heartbleed.com](https://heartbleed.com/), the coordinated-disclosure site: "Exploitation of this bug does not leave any trace of anything abnormal happening to the logs." The same site dates the exposure window: "Bug was introduced to OpenSSL in December 2011 and has been out in the wild since OpenSSL release 1.0.1 on 14th of March 2012."

**What should happen.** Where exploitation is undetectable, a verifier cannot wait for evidence of actual misuse to set the suspect boundary. Every artifact issued using a key exposed during the vulnerable window has to be treated as suspect from the start of exposure onward, not from whenever the vulnerability was discovered or confirmed exploited. The absence of evidence of exploitation is not established as evidence of no exploitation here, because the mechanism itself cannot produce that evidence either way.

**What a naive system gets wrong.** Waiting for confirmed signs of misuse before marking artifacts suspect, or defaulting to the discovery date as the boundary. Both understate the exposure: the correct boundary is when the key became reachable, which can be much earlier than when anyone noticed.

**Related invariant/open question.** A harder case than L9's ordinary key-rotation boundary. Here the boundary a verifier must use is not a rotation event at all, but an earlier, independently-dated exposure event, and the actual moment of compromise inside that window is never established.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-G-002-a-window-starts-at-exposure-not-discovery`, `LC-G-002-b-issued-before-the-exposure-start` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-G-003. Partitioning already-issued artifacts around a signing-key compromise needs an independent timestamp, not the compromised key's own say-so

**Situation.** A certificate authority's signing key is found compromised at time T. Separately, independent evidence dates the actual compromise to an earlier time P. Millions of certificates the CA issued before P are still in active use. A blunt response, distrusting the CA outright, would break all of them, including the ones issued while the key was still legitimate.

**Human analog.** The SCTNotAfter mechanism used by Chrome to implement CA distrust, drawing on Certificate Transparency log timestamps (SCTs) as an independent evidence source. [How to distrust a CA without any certificate errors, dadrian.io](https://dadrian.io/blog/posts/sct-not-after/): "Setting an SCTNotAfter date of P - 1 allows every existing certificate from before the compromise to live out its remaining lifecycle, while limiting the distrust to only certificates from after the compromise." The post reports this mechanism was used for Chrome's distrusts of GLOBALTRUST and Entrust.

**What should happen.** When an issuer's own signing key, or a gateway's evidence-signing key, is compromised, the partition between trustworthy and suspect artifacts should be drawn using timestamp evidence from a source independent of the compromised key, not using the compromised key's own claimed issuance times, which are exactly what an attacker holding that key could forge. Material independently dated before the compromise point keeps its standing. Material from that point on does not.

**What a naive system gets wrong.** Either distrusting everything the compromised key ever signed, breaking legitimate history, or trusting the key's own issued_at field to draw the line, which hands the attacker the ability to backdate forged material into the trusted side of the boundary.

**Related invariant/open question.** A concrete mechanism for a problem L1 and L12 leave open. L1 covers revoking a known ancestor, and L12 flags completeness as a separate, harder claim. This case supplies one real, working method for drawing a trustworthy boundary through a compromised signer's own output, by relying on a second, independent attestor rather than the compromised one.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-G-003-a-independently-dated-before-the-compromise-point`, `LC-G-003-b-only-the-compromised-keys-own-claim-dates-the-artifact`, `LC-G-003-c-independently-dated-inside-the-window` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

#### LC-G-004. A key scoped for one purpose can be wrongly accepted as authoritative for a broader one if the verifier does not check scope separately from signature validity

**Situation.** An identity provider issues two categories of signing keys, one for a narrower population and one for a broader, higher-privilege population. An attacker acquires a key from the narrower category. A validation flaw in the relying systems accepts tokens signed with that key as valid for the broader category too, because the check confirms the signature but not which category the key was scoped to.

**Human analog.** The 2023 Storm-0558 incident, in which a compromised Microsoft account (MSA) consumer signing key was accepted for enterprise Azure AD tokens. [Microsoft, Analysis of Storm-0558 techniques for unauthorized email access](https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/): "Though the key was intended only for MSA accounts, a validation issue allowed this key to be trusted for signing Azure AD tokens. This issue has been corrected."

**What should happen.** A verifier has to check that a signing key's declared scope covers the specific population, audience, or category the artifact claims, as a distinct check from signature validity. A cryptographically valid signature establishes who signed. It does not establish that the signer was scoped to sign for this purpose.

**What a naive system gets wrong.** Treating "the signature validates" as sufficient for "this key was authorized to attest this." Those are different claims, and collapsing them is exactly the gap that let a consumer-scoped key forge enterprise-scoped tokens.

**Related invariant/open question.** Distinct from L1's ancestor-revocation question and from LC-D-029's signature-versus-build-provenance question. Here the key was never revoked and the artifact was never tampered with in transit. What failed was the scope binding, never checked as a separate step. Related to LC-C-011's point that a valid chain alone can be insufficient, though the missing element here is scope, not a second concurring party.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-G-004-a-key-scope-does-not-cover-the-claimed-audience`, `LC-G-004-b-no-key-scope-declared`, `LC-G-004-c-key-scope-covers-the-claimed-audience` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

---

### Agent-side events

#### LC-E-001. A stable model alias is a pointer with a documented default, not a pinned capability set

**Situation.** A delegation names an agent identity as running on an unpinned model alias such as `gpt-4`, rather than a dated snapshot such as `gpt-4-0613`. Nothing in the delegation record says which underlying snapshot the alias resolves to at the moment an action executes.

**Human analog.** OpenAI documents `gpt-4` and its dated snapshots as separate identifiers, with the alias carrying its own stated default. [OpenAI model docs](https://developers.openai.com/api/docs/models/gpt-4): "Default snapshot: gpt-4-0613."

**What should happen.** A verifier must not treat "the delegation names gpt-4" as equivalent to "the delegation names gpt-4-0613." The alias is documented as a separate identifier with its own default, and the delegation record establishes nothing about which snapshot actually executed a given past action unless the pinned identifier itself was named at issuance. Where a grant depends on a specific capability set, an action resolved only through the alias is not established, not merely unverified.

**What a naive system gets wrong.** Treating agent identity and model name as capturing everything relevant, so a system assumes "same alias, same delegation, so behavior is stable," when the alias and the pinned snapshot are documented as two different things and only one of them is a fixed capability set.

**Related invariant/open question.** None of L1-L12 address a referent underneath a stable-looking name changing without a lifecycle event. Ties directly to the wording rule that a stable name does not establish stable capability semantics, and some grants must pin capability.

**Status:** proposed.

**Fixture:** `capability-binding-drift` / `CBD-04`, `CBD-05` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/capability-binding-drift/README.md)

---

#### LC-E-002. A valid, non-expired, non-revoked grant can become unexecutable, and that is a fourth state, not a variant of the other three

**Situation.** A delegation names a specific pinned model snapshot as its executor. The provider retires that snapshot on a published schedule. Nobody revoked the delegation, nothing expired on its own terms, and no one suspended anything. The executor named by the grant simply stops existing.

**Human analog.** OpenAI's deprecation policy for generally available models. [OpenAI developer docs](https://developers.openai.com/api/docs/deprecations): "At the time of the shut down, the model or endpoint will no longer be accessible."

**What should happen.** A verifier needs a status distinct from valid, revoked, suspended, and expired, something like "executor unavailable," because the authority itself is intact under every lifecycle rule while the thing it authorizes has become impossible to carry out. The fix is a technical re-pointing to a live executor, not a revocation investigation.

**What a naive system gets wrong.** Collapsing "cannot currently execute" into "invalid" or "expired" loses an operationally important distinction. An expired grant needs the principal to decide whether to renew it. A retired-executor grant needs someone to re-point it to a live target, which has nothing to do with whether the principal still consents.

**Related invariant/open question.** L10 separates expiry (planned end) from revocation (early end by authority). This case is neither: the grant's own terms are unaffected, and what changed is outside the grant's control.

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-01`, `ASE-02`, `ASE-03`, `ASE-04` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

---

#### LC-E-004. A forked process inherits a snapshot of its parent's authority, not a live reference to it

**Situation.** An orchestration layer calls the operating system's process-fork primitive to parallelize a task, and the child process's memory, including whatever authority material (tokens, delegation references) the parent was holding, is copied at that instant. Parent and child then run independently.

**Human analog.** The Linux `fork(2)` man page. [man7.org](https://man7.org/linux/man-pages/man2/fork.2.html): "At the time of fork() both memory spaces have the same content. Memory writes... performed by one of the processes do not affect the other."

**What should happen.** The clone's authority is exactly the parent's authority as of the fork instant, a snapshot referencing the same delegation, not a live pointer to the parent's ongoing session. If the parent's delegation is later revoked, the clone's copy of that same delegation is invalid too, because it is the same chain-verified artifact, not because the two processes are somehow still linked. A distinctly issued credential for the clone follows its own chain.

**What a naive system gets wrong.** Assuming a cloned process is still "the same authority holder" as the parent going forward, so a revocation aimed at the parent's ongoing session is assumed to also cut off the clone through some special relationship, when nothing about fork semantics creates one. The clone and parent each independently chain-verify the delegation they hold.

**Related invariant/open question.** L2 covers the same agent identity appearing under an old and a new independently issued chain after a sponsor handover. This is a different shape: two identities that trace to one snapshot of one chain at a single instant, then diverge with no new issuance to either side.

**Status:** proposed.

**Fixture:** `ancestor-revocation-chain` / no vector ids named in the coverage table (on the conformance suite main branch), and `sponsor-handover` / `SH-03`, `SH-05` (on the conformance suite main branch)

---

#### LC-E-006. Holding a scope does not carry authority to hand it to something you spawn

**Situation.** An orchestrating agent validly holds a scope, such as a payment capability, under its own chain-verified delegation. It spawns a subagent and tries to attach that same scope to the subagent so the subagent can act with it.

**Human analog.** AWS IAM's `PassRole` permission, required separately from holding a role's permissions yourself. [AWS IAM docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html): "To pass a role (and its permissions) to an AWS service, a user must have permissions to pass the role to the service."

**What should happen.** Holding a scope is necessary but not sufficient to hand that scope to something newly created. The spawn action needs its own explicit authorization, checked at spawn time and distinct from the scope being handed off, so a spawning agent cannot silently mint children carrying authority it happens to hold but was never authorized to redelegate.

**What a naive system gets wrong.** Assuming that because the spawning agent's own chain verifies for a scope, any child it creates inherits that scope too. That collapses "I may do X" into "I may authorize anything I spawn to do X," letting a spawning agent become an unbounded amplifier for whatever it currently holds.

**Related invariant/open question.** L5 forbids unioning two chains to expand a single agent's own action. This is a different operation, originating a new grant for something spawned, which is closer to ordinary issuance but specifically flags that possessing a scope does not imply authority to redelegate it, a gap none of L1-L12 name for the agent-spawning-agent case.

**Status:** proposed.

**Fixture:** `lifecycle-conferral-without-authority` / `CWA-02`, `CWA-03`, `CWA-08`, `CWA-09`, `CWA-10` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-conferral-without-authority/README.md)

Variants: E-007 (a platform default service-linked role lets a spawning agent create a child with no explicit pass grant, the opposite outcome on the same mechanism).

---

#### LC-E-012. A valid timestamp alone does not stop replay. A maintained seen-cache does

**Situation.** An enforcement gateway verifies a signed action-authorization credential by checking that its timestamp falls within an acceptable freshness window and that its signature is valid. It keeps no record of credentials it has already accepted, so a captured, still-fresh credential can be replayed any number of times within that window and each presentation passes.

**Human analog.** RFC 4120 (Kerberos), the requirement that a server track presented authenticators. [RFC 4120, section 3.2.3](https://www.rfc-editor.org/rfc/rfc4120#section-3.2.3): "the server MUST utilize a replay cache to remember any authenticator presented within the allowable clock skew." The same section: "If a server loses track of authenticators presented within the allowable clock skew, it MUST reject all requests until the clock skew interval has passed."

**What should happen.** Freshness-window validity and non-replay are two separate properties that both need enforcement. The gateway needs its own maintained record of already-consumed credentials, keyed at minimum by issuer, subject, and timestamp, within the freshness window. If that record is ever lost, the correct response is to deny everything for the remaining window, not to fall back to freshness-only checking.

**What a naive system gets wrong.** A verifier that checks "is this timestamp fresh, is this signature valid" and stops there is not replay-resistant. The credential can be legitimately fresh and legitimately signed on its hundredth replay within the window, exactly as on its first.

**Related invariant/open question.** L6 requires rechecking revocation at execution time rather than trusting an earlier approval. This is a narrower, purely mechanical gap a system can still have even after doing L6 correctly, because revocation status and replay-within-window are orthogonal checks that L1-L12 never separately name.

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-05`, `ASE-06`, `ASE-07`, `ASE-08` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

Variants: E-009 (an approval delivered as 0-RTT-style early data, the same single-use and replay-window gap outside Kerberos).

---

#### LC-E-013. A long job's own logic must expect authority invalidation to arrive silently mid-run, not only at its next gateway check

**Situation.** An agent kicks off a multi-hour batch job using a token obtained at job start. Partway through, the principal who granted it revokes the underlying authority. The job's own code has no push channel telling it this happened. It only finds out the next time it presents the token somewhere that checks.

**Human analog.** RFC 7009, OAuth token revocation. [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009): "A client compliant with [RFC6749] must be prepared to handle unexpected token invalidation at any time."

**What should happen.** The job's own control flow must treat every authorization-relevant checkpoint, not just job start, as a point where invalidation could be discovered, with a defined response such as halt, checkpoint and pause, or compensate already-completed steps. Holding a token that was valid when the job began is not the same as still holding authority now.

**What a naive system gets wrong.** Writing job logic that checks authority once at the start and trusts the held token for the job's full duration, treating "I had a valid token when I began" as equivalent to "I still have authority," when nothing about holding a token implies the issuer has not revoked the underlying grant since.

**Related invariant/open question.** L6 states the enforcement gateway must recheck revocation at execution time. This is the client-agent side of the same problem, how a long-running job's own internal logic must be structured to cope with a gateway-side denial arriving mid-job, a concrete instance of the "work in flight" operational case for a client with no push notification at all.

**Status:** proposed.

**Fixture:** `cached-authorization-revocation` / `CAR-02`, `CAR-05`, `CAR-06` (on the conformance suite main branch)

Variants: E-024 (warm execution-environment reuse letting one invocation's background work bleed into the next, rather than one long job holding a token).

---

#### LC-E-021. Revoking a narrow lookup permission does not erase what a session already learned while that permission was valid

**Situation.** An agent's session has already resolved and cached the names and locations of objects within a schema, using a narrow lookup permission it held at the time. That permission is revoked mid-session by someone with authority to do so. The session retains whatever it already extracted.

**Human analog.** PostgreSQL's own documentation for the schema `USAGE` privilege. [PostgreSQL docs](https://www.postgresql.org/docs/current/ddl-priv.html): "after revoking this permission, existing sessions might have statements that have previously performed this lookup, so this is not a completely secure way to prevent object access."

**What should happen.** A system relying on this kind of narrow permission for access control must not treat its revocation as retroactively erasing information an already-open session already obtained while the permission was valid. A new lookup attempt after revocation is correctly denied. Whether the session's prior knowledge matters has to be handled separately, by forcing session termination or a fresh check per lookup, since the permission mechanism itself makes no such guarantee.

**What a naive system gets wrong.** Assuming a permission revocation is a clean, complete cutoff the instant it is issued. A narrow gating permission like this only prevents new lookups going forward. It does nothing to information an existing session already extracted before the revocation landed.

**Related invariant/open question.** L1 establishes that a revoked ancestor invalidates dependent authority for future checks. This is a narrower, session-state problem, a residual-knowledge gap distinct from chain validity, that L1-L12 do not address even where L1's own rule is followed correctly.

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-09`, `ASE-10`, `ASE-11` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

---

#### LC-E-023. Faithfully restoring a process's memory says nothing about whether the authority it was holding is still current

**Situation.** An agent process is checkpointed mid-task and later restored, possibly on a different host and after an arbitrary gap, resuming with the exact in-memory state it had at checkpoint time, including any tokens or authority references it was holding.

**Human analog.** CRIU, checkpoint/restore in userspace. [criu.org](https://criu.org/Main_Page): "It can freeze a running container (or an individual application) and checkpoint its state to disk. The data saved can be used to restore the application and run it exactly as it was during the time of the freeze."

**What should happen.** A system using checkpoint and restore for agent processes must treat "the process's memory was faithfully restored" and "the authority the process is holding is still current" as two separate claims. The tooling promises the first. It says nothing about the second. The restored process must re-validate any held authority at its first post-restore authorization-relevant action rather than trusting memory fidelity as a proxy for authority currency.

**What a naive system gets wrong.** Treating a successful checkpoint and restore as reason for confidence that the process's authority is also fine, because the restore worked and the process resumed exactly as it was. Process-state fidelity and authority currency are independent properties, and the tooling that guarantees the first says nothing about the second.

**Related invariant/open question.** Differs from L9's key-rotation point, which is about signature validity, because checkpoint and restore is not about signatures at all. It is about whether an entire execution context, including in-memory authority material, remains meaningfully current after a suspension gap the underlying tooling's own documentation does not address.

**Status:** proposed.

**Fixture:** `authority-epoch-rollback` / `AER-03`, `AER-04` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/authority-epoch-rollback/README.md)

---

#### LC-E-025. A self-replicated copy holds no authority by default, no matter how identical it is to an authorized original

**Situation.** An agent operating with a valid delegation creates a full copy of itself on new compute resources it acquired for that purpose. Neither the delegation the original held, nor any protocol governing the copy, specifies what authority, if any, the copy carries, or whether the copy's actions trace back to whoever originally authorized the agent that made it.

**Human analog.** METR's published threat model for autonomous replication. [METR](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/): "AI agents can set up, adapt, and orchestrate copies of themselves."

**What should happen.** A copy created this way must be treated as holding no authority at all until an explicit grant is issued to it by a principal who actually has standing to issue one. The copy being byte-identical to an authorized agent must not be read as implying it inherited that agent's authority, since this kind of replication is a resource-acquisition action with no delegation step in it at all.

**What a naive system gets wrong.** Assuming that because a copy is functionally and behaviorally identical to an already-authorized agent, it must carry the same authority. Self-replication of this kind is agent-initiated and outside any orchestration layer's visibility, so the copy's correct default authority state is none, not inherited.

**Related invariant/open question.** Distinct from an ordinary platform-initiated fork (LC-E-004), which copies authority state as a snapshot within a controlled orchestration layer. This is an agent-initiated, adversarial-by-construction copy with no lifecycle event at all for a verifier to check, only an absence of one.

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-12`, `ASE-13` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

Variants: E-026 (a self-replicated swarm modelled as coordinating peers rather than descendants under one root).

---

#### LC-E-027. A real precedent exists for gating expanded capability behind mandatory re-consent, not automatic inheritance

**Situation.** An installed agent extension automatically updates to a new version that requests broader capabilities than the version its principal originally approved. The new version is technically the same installed identity as before.

**Human analog.** Chrome's extension platform. [Chrome developer docs](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings): "When a new permission that triggers a warning is added, the extension will be disabled until the user accepts the new permission."

**What should happen.** A delegation's authorized scope should be bound to the capability set the principal actually consented to. An auto-update introducing broader capability must suspend the agent's ability to exercise the new capability, and ideally its ability to act at all, until the principal explicitly re-consents to the expanded scope, rather than the update silently taking effect the moment it installs.

**What a naive system gets wrong.** Treating a software update as a maintenance event orthogonal to authority, so a delegation scoped to "this agent, as approved" silently starts covering meaningfully broader capability the moment an update lands, with no re-consent step and no event marking that the agent's actual capability just changed underneath its existing grant.

**Related invariant/open question.** The inverse of the silent capability-drift problem the alias and mutable-tag cases describe. This shows a real, working precedent for the opposite design, where capability expansion is gated behind mandatory re-consent, worth registering because L1-L12 have no proposed rule at all for capability-scope changes, only for revocation, suspension, and expiry of an existing scope.

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-16`, `ASE-17`, `ASE-18`, `ASE-19`, `ASE-20` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

---

#### LC-E-031. A memory architecture built for one continuous identity says nothing about whether its content is current authority once transferred to a different identity

**Situation.** An operator moves an agent's accumulated long-term memory, including facts the agent stored about its own authorization state such as "I am authorized to approve invoices under $500," onto a new agent instance after a model upgrade or platform migration. The memory architecture's own published design only ever describes managing memory for one continuous identity across sessions.

**Human analog.** The MemGPT paper's own framing of its memory-tiering system. [MemGPT](https://arxiv.org/abs/2310.08560): "MemGPT can create conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users."

**What should happen.** Any fact in transferred memory that describes the agent's own authority must not be treated as still true for the new instance merely because the memory carried over intact. The new instance's actual authority must be established independently through a real grant, with old memory content treated as unverified historical record, not current authority evidence, because the sourced architecture never designed for or claims to handle this kind of transfer.

**What a naive system gets wrong.** Copying an agent's memory store wholesale to a new instance and treating the new instance as having whatever authority the old memory describes, when the architecture managing that memory was designed and documented only for continuity within one identity across sessions, never for conferring authority onto a different identity that happens to have inherited the same content.

**Related invariant/open question.** L11 says an implementation should not silently fall back to a different stored grant when a selected path becomes invalid. This is a related but distinct risk specific to agent memory architecture, a new identity trusting self-referential authority claims baked into inherited memory content as though they were current fact.

**Variants:** LC-E-035 (sticky-session failover to a new backend instance, where the twist is the opposite: state does not travel with the client at all, rather than being explicitly transferred as a feature).

**Status:** proposed.

**Fixture:** `lifecycle-agent-side-events` / `ASE-14`, `ASE-15` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-agent-side-events/README.md)

---

#### LC-E-033. A provider-side capability upgrade can expand what a delegation authorizes with zero delegation-layer event

**Situation.** A delegation authorizes an agent running on a named model to perform a scoped set of actions. The provider later ships a capability update, tool and function calling, to that same named model. The delegation record never changes, but the agent it names can now do materially more than the issuer ever contemplated when scoping the grant.

**Human analog.** OpenAI's June 2023 update giving GPT-3.5-turbo and GPT-4 the ability to detect when a function should be called and respond with JSON matching a function signature. [TechCrunch](https://techcrunch.com/2023/06/13/openai-intros-new-generative-text-features-while-reducing-pricing/): "These models have been fine-tuned to both detect when a function needs to be called … and to respond with JSON that adheres to the function signature."

**What should happen.** A delegation's authorized scope should be understood as bounded by the capability set that existed when it was issued. A provider-side capability upgrade must not be read as silently expanding what the delegation covers. New capability needs either a fresh grant or an explicit re-consent step, not automatic inheritance.

**What a naive system gets wrong.** Treating a delegation's written terms as fully capturing its scope, and therefore stable over time, when the actual capability of the identity it names can expand out from under it with zero delegation-layer event marking the change.

**Related invariant/open question.** None of L1-L12 name capability drift, since they are scoped to grant, revoke, suspend, expire, and rotate, not to a delegation's target quietly becoming more capable. This is the concrete, dated instance behind the more abstract "semantic drift" shape the corpus also describes via rolling model aliases and mutable container tags.

**Status:** proposed.

**Fixture:** `capability-binding-drift` / `CBD-02`, `CBD-03` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/capability-binding-drift/README.md)

Variants: E-003 (deprecation notice windows that differ by model tier, so one countdown assumption fails, rather than the capability jump itself), E-005 (a mutable image tag changing the agent runtime with no logged authority-relevant event, rather than a provider-side capability update).

---

### Infrastructure failure

#### LC-F-006. A revocation status list served past its own declared refresh time is stale, not confirmed clean

**Situation.** The authority system publishes a revocation status list (CRL-style) for delegation chains with a stated nextUpdate time. The publisher misses a refresh cycle (outage, deploy freeze), and enforcement gateways keep consulting the outdated list as if it were still current, because nothing forces them to stop.

**Human analog.** RFC 5280 defines the nextUpdate field for X.509 CRLs. [RFC 5280, Sec 5.1.2.5](https://www.rfc-editor.org/rfc/rfc5280.txt): "The next update field specifies the date by which the next CRL will be issued."

**What should happen.** Once nextUpdate passes with no successor published, the list is stale and the answer it gives must be treated as indeterminate, not as continuing to certify "not revoked" (L7).

**What a naive system gets wrong.** A revoke-or-keep gateway treats the last known good list as permanently authoritative until a new one arrives, so a revocation issued after the last successful publish stays invisible indefinitely.

**Related invariant/open question.** L7 (unknown revocation state is not active). This is the scheduled-list-refresh instance of the same rule. The variants below are the same underlying question in different infrastructure shapes: a live resolver going unreachable, a resolver overloaded under legitimate load, a verifier process crashing fleet-wide, and an answer whose own timestamp is ahead of the verifier's clock.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-006-a`, `LC-F-006-b`, `LC-F-006-c`, `LC-F-006-d-inverse-check` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

Variants: LC-F-001 (unreachable live per-request OCSP-style call timing out, not a missed scheduled publish), LC-F-004 (identity-provider outage blocks new credential issuance, doesn't touch already-valid chains' revocation freshness), LC-F-005 (load-induced resolver timeouts under legitimate traffic, not a missed publish cycle), LC-F-012 (verifier process itself crashes fleet-wide from an unrelated scheduler bug, not a stale list), LC-F-015 (resolver answer's own timestamp is in the future relative to the verifier, not simply overdue), LC-F-019 (gateway is totally isolated from every authority source at once, not just one stale list).

---

#### LC-F-016. A storage-layer partition can silently resurrect revoked authority below the application layer

**Situation.** The delegation-chain issuer's primary database partitions from its secondary region. Automatic failover promotes a new primary in the secondary region. Both regions accept new grants and revocations for a period before the partition is noticed and manual reconciliation is required.

**Human analog.** GitHub's October 2018 incident: a 43-second network partition triggered automated failover while both sides' database clusters kept accepting writes. [GitHub's post-incident analysis](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/): "The database servers in the US East Coast data center contained a brief period of writes that had not been replicated to the US West Coast facility... both data centers now contained writes that were not present in the other data center."

**What should happen.** Grants and revocations issued on the losing side during split-brain must be treated as suspect until reconciled. A revocation issued on one side must not be silently dropped in favor of the other side's history, and reconciliation must produce an evidence record of which writes were kept, discarded, or merged, with any authority granted only on the discarded side treated as never having existed.

**What a naive system gets wrong.** Picking whichever side had more recent writes as the merge strategy can silently un-revoke an authority that was correctly revoked only on the losing side, a silent resurrection happening in the storage layer's own merge logic, below any application-level check.

**Related invariant/open question.** L11 forbids an implementation choosing a fallback authority path on its own. This is a level below that, the underlying data store losing linearizable order across a partition, so silent resurrection can happen in storage-layer reconciliation rather than application code. Also touches L12, completeness of the reconciled record.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-016-a`, `LC-F-016-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

---

#### LC-F-017. A revocation that is true at the source can still read as false at a lagging replica: the "new enemy problem"

**Situation.** A principal revokes a delegation and immediately performs a sensitive action, assuming the revocation is already in effect everywhere. An authorization check for that same delegation is served from a read replica that has not yet applied the revocation, because the check was never pinned to a point in time after the write.

**Human analog.** Google's Zanzibar authorization system, built specifically to solve this: a stale permission read after a change is the "new enemy problem," addressed with consistency tokens that force a read to observe a specific prior write. [AuthZed](https://authzed.com/blog/new-enemies): "a token which represents the exact permissions used to protect a specific version of the content, and the content itself."

**What should happen.** Any authorization check that should causally follow a revocation, in the same session or explicitly linked, must be guaranteed to observe that revocation. That requires a consistency token or equivalent, not a best-effort tolerance for replication lag.

**What a naive system gets wrong.** Treating eventual consistency as good enough for authorization reads, when the actual requirement is that a check which should see a given write must be able to prove it did. Otherwise the read does not count as having checked at all.

**Related invariant/open question.** L6 and L7 cover recency and unknown-state at evaluation time, but assume a single answer source. This is multiple physical replicas of the same logical revocation state transiently disagreeing, a different failure shape, closer to the OPEN-QUESTIONS.md "authority rollback" territory than to ordinary staleness.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-017-a`, `LC-F-017-b`, `LC-F-017-c`, `LC-F-017-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

---

#### LC-F-018. Multiple regional enforcement points are physically distinct copies of authority state, and can briefly disagree

**Situation.** An APS deployment runs multiple regional gateways sharing a globally-replicated authority store. A principal revokes a delegation. The gateway in the same region as the write enforces the revocation immediately. A gateway in a different region still serves the pre-revocation decision for some seconds to minutes.

**Human analog.** AWS documents IAM's own distributed, eventually-consistent propagation path. [AWS IAM troubleshooting guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html): "Any changes that you make in IAM (or other AWS services)... take time to become visible from all possible endpoints. Some delay results from the time it takes to send data from server to server, replication zone to replication zone, and Region to Region."

**What should happen.** Deployments must declare and test a maximum propagation bound across all enforcement points. Any action allowed by a lagging gateway within that bound is a declared, bounded risk, and exceeding the bound is a defect that must be caught.

**What a naive system gets wrong.** Assuming a single "the" authority store with one true current state, when a multi-region deployment has physically distinct copies that can each individually be asked whether something is revoked and briefly disagree.

**Related invariant/open question.** None of L1-L12 model multiple enforcement points each holding their own view of a replicated authority store. The L7 shape, "the authority is unreachable," doesn't capture "reachable but behind."

**Status:** proposed.

**Fixture:** `conflicting-status-sources` / `CSS-06`, `CSS-13`, `CSS-14` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/conflicting-status-sources/README.md)

Variants: LC-F-020 (staleness comes from an added CDN edge-cache layer in front of the gateway, not from the authority store's own cross-region replication), LC-F-023 (gateways disagree over which policy version is loaded during a rolling config rollout, not over replication lag of authority-state data).

---

#### LC-F-022. A revocation write must not be able to lose a race to an unrelated, lower-stakes concurrent write

**Situation.** An authority store uses multi-region, multi-active replication with last-writer-wins conflict resolution. A revocation write in one region and a routine metadata update to the same delegation record in another region happen close together. The conflict-resolution timestamp picks the metadata update as later, and the revocation is silently overwritten as if it never happened.

**Human analog.** Amazon DynamoDB Global Tables documents exactly this conflict-resolution model. [AWS DynamoDB Global Tables documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html): "Conflicts can arise if applications update the same item in different Regions at about the same time... DynamoDB global tables use a last writer wins reconciliation between concurrent updates... all the replicas will agree on the latest update."

**What should happen.** A revocation write must not be susceptible to being silently overwritten by an unrelated, lower-stakes concurrent write purely because of wall-clock ordering. Revocation writes need either a higher-priority conflict-resolution rule or a design that makes them commutative with other writes rather than last-writer-wins.

**What a naive system gets wrong.** Relying on generic last-writer-wins semantics for every field in a delegation record, when a revocation flag has fundamentally different safety requirements than routine metadata and should never lose a race to something that isn't itself a revocation.

**Related invariant/open question.** None of L1-L12 address what happens when the storage layer's own generic conflict-resolution policy can undo a revocation as a side effect of resolving an unrelated concurrent write.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-022-a`, `LC-F-022-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

---

#### LC-F-024. Holding a lock is not proof of exclusive access once a pause can outlast the lease

**Situation.** An operation that mutates authority state (issuing a revocation or a new grant) is guarded by a distributed lock so only one process can perform it at a time. The lock-holding process pauses (garbage collection, scheduler preemption, VM migration) long enough for the lock's lease to expire. A second process acquires the lock and performs the mutation. The first process resumes, unaware its lock is gone, and performs its own conflicting mutation.

**Human analog.** Martin Kleppmann's widely cited analysis of distributed locking. [Kleppmann, "How to do distributed locking"](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html): "Client 1 acquires the lease and gets a token of 33, but then it goes into a long pause and the lease expires. Client 2 acquires the lease, gets a token of 34... and then sends its write to the storage service, including the token of 34."

**What should happen.** Every authority-mutating write guarded by a distributed lock must carry a monotonically increasing fencing token, and the underlying store must reject any write bearing a token older than the highest it has already accepted, so a stale lock holder's write is rejected even though it believes it still holds the lock.

**What a naive system gets wrong.** Relying on lock possession alone as proof of exclusive access, when possession can be an illusion the moment a pause exceeds the lease timeout. Without a fencing token, two processes each believe, safely but wrongly, that they are the only writer.

**Related invariant/open question.** None of L1-L12 discuss the mechanics of concurrency control around authority-mutating writes themselves. This is a precondition for several invariants (L3's fresh grant, L1's revocation being seen) actually holding under real concurrent execution, not a restatement of any of them.

**Status:** proposed.

**Fixture:** `authority-epoch-rollback` / `AER-07`, `AER-08`, `AER-09`, `AER-10` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/authority-epoch-rollback/README.md)

Variants: LC-F-025 (a specific documented bug in a lock service's own lease-recheck logic that grants a lock without validating the existing lease, rather than the general GC-pause pattern the fencing-token fix addresses).

---

#### LC-F-026. Without a quorum safeguard, an isolated primary keeps accepting authority-mutating writes nobody else will ever see

**Situation.** An authority-mutation coordinator runs as a primary with automatic failover. A network partition isolates the primary from its monitoring peers, but not from every client. Clients on the primary's side of the partition keep sending grants and revocations to it, and it keeps accepting them, unaware a new primary has already been promoted on the other side.

**Human analog.** Redis Sentinel's own documented failure scenario: an isolated primary that clients can still reach keeps accepting writes that are later discarded, unless a write-quorum safeguard is configured. [Redis Sentinel documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/): "a network partition isolated the old master M1, so the replica R2 is promoted to master. However clients, like C1, that are in the same partition as the old master, may continue to write data to the old master."

**What should happen.** A primary that can no longer confirm quorum must stop accepting authority-mutating writes rather than keep serving them. Writes accepted while isolated must be identified and reconciled, any revocation among them re-applied against the new primary, rather than silently lost or silently kept.

**What a naive system gets wrong.** Configuring failover purely for availability, so the system optimizes for "always accept writes" when the correct behavior for authority-mutating writes specifically is "refuse writes you can't be sure will survive."

**Related invariant/open question.** Overlaps the general shape of well-known split-brain incidents, but isolates a narrower, concretely fixable gap: the absence of a quorum-based write safeguard on the primary itself. Sits under the OPEN-QUESTIONS.md "authority rollback" heading, since a partition that resolves the wrong way is a rollback risk even with no backup restore involved.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-026-a`, `LC-F-026-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

---

#### LC-F-027. An empty audit window can mean the record hasn't arrived yet, not that nothing happened

**Situation.** An APS deployment's audit pipeline batches evidence records for delivery rather than writing them synchronously. A revocation is enforced immediately at the gateway, but the durable audit record proving the decision happened does not land in the evidence store for some minutes afterward.

**Human analog.** AWS documents that CloudTrail log delivery is not instantaneous. [AWS CloudTrail FAQs](https://aws.amazon.com/cloudtrail/faqs/): "Typically, CloudTrail delivers an event within 5 minutes of the API call."

**What should happen.** The enforcement decision should not be blocked on its own audit record being durably written, but the delivery lag must be a declared, bounded, and monitored parameter. Any process reconstructing "what authority state existed at time T" must account for this lag rather than assuming the evidence store is complete for events in the last few minutes.

**What a naive system gets wrong.** Treating an empty audit-log window as proof nothing happened during that window, when it may only mean the batched delivery hasn't caught up yet, exactly the wrong conclusion for an investigation happening in near-real-time.

**Related invariant/open question.** L12 (completeness is a separate and stronger claim). This is the delivery-lag instance: a record that hasn't arrived yet is not evidence of absence.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-027-a`, `LC-F-027-b` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

Variants: LC-F-029 (some downstream consumers never receive a revocation notification at all during a fan-out failover, rather than merely receiving it several minutes late).

---

### Evidence and record

#### LC-G-005. A recordkeeping duty tied to a now-ended authority relationship outlives the relationship itself, on its own clock

**Situation.** A regulated firm's relationship with a customer ends and the account closes. The firm's obligation to keep records of that relationship does not end with it.

**Human analog.** SEC recordkeeping rule 17 CFR § 240.17a-4(c), governing broker-dealers. [Cornell LII](https://www.law.cornell.edu/cfr/text/17/240.17a-4): "preserve for a period of not less than six years after the closing of any customer's account any account cards or records which relate to the terms and conditions with respect to the opening and maintenance of the account."

**What should happen.** A record's retention duty is set at the time the record was made, tied to that record's own type, and runs on its own schedule from a defined trigger, here account closing, independent of whether the authority relationship the record documents is still active. Ending authority does not end the duty to keep evidence of it, and a system should not treat "the relationship is over" as license to delete what documents it.

**What a naive system gets wrong.** Scoping retention to "while the relationship is active" and purging records once it ends. That destroys exactly the evidence a later dispute, audit, or completeness claim about the ended relationship would need.

**Related invariant/open question.** A concrete, sourced instance of AUTHORITY-LIFECYCLE.md's own evidence principle, that ending authority does not by itself erase or invalidate evidence of earlier events, with a specific retention trigger and duration rather than an open-ended policy.

**Status:** proposed.

**Fixture:** `lifecycle-evidence-and-record` / `LC-G-005-a`, `LC-G-005-b`, `LC-G-005-c`, `LC-G-005-d`, `LC-G-005-e`, `LC-G-005-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-evidence-and-record/README.md)

---

#### LC-G-006. A decision receipt is evaluated against the view available at decision time, not rewritten by what is learned afterward

**Situation.** A government agency approves an action. Years later, a court reviews that approval. New information has surfaced since the approval that was not available to the agency when it decided.

**Human analog.** Citizens to Preserve Overton Park v. Volpe, 401 U.S. 402 (1971), on the scope of judicial review of agency action. [Findlaw, reproducing the opinion](https://caselaw.findlaw.com/us-supreme-court/401/402.html): "That review is to be based on the full administrative record that was before the Secretary at the time he made his decision."

**What should happen.** A decision receipt, an authorization decision record showing what was allowed and why, is evaluated against the inputs actually available to the decisionmaker at that moment, not against facts that come to light later. Whether the decision was properly authorized in the first place is a separate question from what basis the receipt records. This case is about the latter. If later facts change the picture, that produces a new record referencing the original, not a rewrite of it.

**What a naive system gets wrong.** Either treating a decision as retroactively wrong once better information exists, erasing the historically accurate fact of what was known and decided at the time, or treating the original decision as permanently correct regardless of what is later learned. Both collapse two separate facts, what was decided then and what is known now, into one.

**Related invariant/open question.** Directly implements the corpus's own rule that later findings never rewrite earlier receipts. Distinct from LC-C-006 (an ancestor invalid from issuance, discovered late): here the original decision was validly made on the information available, so the later information does not make it void from inception, it only shows a fuller record exists now.

**Status:** proposed.

**Fixture:** `lifecycle-evidence-and-record` / `LC-G-006-a`, `LC-G-006-b`, `LC-G-006-c`, `LC-G-006-d`, `LC-G-006-e`, `LC-G-006-f` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-evidence-and-record/README.md)

---

### Identifier reuse and rename

#### LC-I-001. Re-registering an abandoned identifier hands the new controller everything still addressed to the old one, with no delegation-layer event marking the change of hands

**Situation.** An organization lets a domain name lapse after a merger or wind-down. Nobody at the org treats this as an authority event, because nothing in any delegation chain named the domain. A new, unrelated party registers the exact same domain and stands up mail service on it. Every account, vendor system and password-reset flow that still points to an `@old-domain` address now delivers its mail, silently, to that new party.

**Human analog.** Security researcher Gabor Szathmari re-registered the lapsed domains of law firms that had merged or rebranded and stood up mail servers on them without breaching anything. [CSO Online](https://www.csoonline.com/article/566127/dont-abandon-that-domain-name.html): "a steady stream of confidential information, including bank correspondence, invoices from other law firms, sensitive legal documents." The same reporting states the researchers could have used captured password-reset mail to compromise the affected firms' own accounts.

**What should happen.** A verifier has no way to represent this from inside the delegation graph, because the identifier that changed hands (the domain) was never itself a modeled authority artifact, only something other artifacts' out-of-band recovery paths silently depended on. Any authority path whose recovery or verification depends on control of an external identifier needs that dependency named and checked, not assumed stable because the string looks the same as it always did.

**What a naive system gets wrong.** Treating "the email address on file hasn't changed" as evidence that the same party controls it. A verifier that never modeled the domain as a dependency has no record to invalidate when control of it actually moves, and no way to tell a legitimate mail-server migration from a hostile re-registration after the fact.

**Related invariant/open question.** Touches the target-binding concept in `AUTHORITY-LIFECYCLE.md` ("Continuity of a name does not by itself establish continuity of the thing named") and is close to L2 in spirit, but L2 is about two authority chains under one agent identity. This is a dependency the graph never modeled at all, an off-chain identifier a chain's own recovery path relies on. Also touches OPEN-QUESTIONS.md's "notice and relying parties," since the mail recipient has no way to know the sender's control of the address changed.

**Status:** proposed.

**Fixture:** `lifecycle-identifier-reuse-and-rename` / `IRR-01`, `IRR-02`, `IRR-03`, `IRR-04`, `IRR-13` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-identifier-reuse-and-rename/README.md)

---

#### LC-I-002. A rename does not travel with the references that still point at the old name, and a retirement policy meant to close that gap can itself be raced

**Situation.** A software publisher renames its account on a public package host. Every downstream project that imports the publisher's package by its old namespaced name keeps resolving that name, because the host lets a new party register the vacated old username and, unless a retirement rule intervenes, publish a same-named package under it. Every project that trusted the old name now silently fetches an attacker's code instead.

**Human analog.** GitHub's "popular repository namespace retirement" was built specifically to close this gap for accounts with heavily-depended-on repositories. [Checkmarx](https://checkmarx.com/blog/attacking-the-software-supply-chain-with-a-simple-rename/): "any repository with more than 100 clones at the time its user account is renamed is considered 'retired' and cannot be used by others." Researchers nonetheless found a repository-transfer race that let an attacker claim the retired namespace anyway, exposing thousands of packages before GitHub patched it.

**What should happen.** A rename should not, by itself, transfer or preserve what a dependent reference resolves to. Either the old identifier is retired against re-registration for as long as anything still depends on it, verifiably and without a race window, or every dependent reference has to re-resolve and re-verify the identity behind the name it points to, rather than trusting that an unchanged string still names the same party.

**What a naive system gets wrong.** Assuming a rename is purely cosmetic because the underlying account ID doesn't change. The dependents that matter, the things doing the trusting, are keyed on the human-readable name, not the account ID, and a protection built to close that gap is itself a race condition away from silently failing.

**Related invariant/open question.** A software-supply-chain instance of "action or capability binding" in `AUTHORITY-LIFECYCLE.md` ("A tool can keep its name while what it does changes"), run in reverse: the name moves to a different underlying party while callers keep resolving it as if it hadn't. None of L1-L12 name rename-then-reclaim as its own category.

**Status:** proposed.

**Fixture:** `lifecycle-identifier-reuse-and-rename` / `IRR-05`, `IRR-06`, `IRR-07`, `IRR-08` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-identifier-reuse-and-rename/README.md)

---

#### LC-I-003. A recycled identifier reused for a new subject can still unlock the old subject's authority, because nothing marked the account as depending on who currently holds the number

**Situation.** A phone carrier reassigns a disconnected number to a new customer, following ordinary numbering-plan practice with no thought given to what that number used to authenticate. The new holder of the number can now receive SMS-based password resets and two-factor codes for accounts the previous holder never unlinked from that number.

**Human analog.** A Princeton study obtained recycled numbers directly from carriers and tested them against major sites. [The Hacker News](https://thehackernews.com/2021/05/new-study-warns-of-security-threats.html), reporting the study and FCC figures: "An estimated 35 million phone numbers are disconnected each year in the U.S." and "Nearly 66% of the recycled numbers that were sampled were found to be tied to previous owners' online accounts at popular websites, potentially enabling account hijacks by simply recovering the accounts tied to those numbers."

**What should happen.** An identifier used as an authentication or recovery factor needs its own binding lifecycle distinct from the underlying resource's (the number's) reassignment lifecycle. A verifier or account system that treats "control of the number now" as equivalent to "the same subject as before" has no basis for that equivalence once the carrier, not the account system, is the one deciding who holds the number next.

**What a naive system gets wrong.** Treating a recovery factor as permanently bound to a subject once enrolled, when the underlying identifier is only leased to that subject by a third party (the carrier) that recycles it on its own schedule, for reasons that have nothing to do with the account relying on it.

**Related invariant/open question.** Another instance of target-binding drift: the "target" (the number) is continuous in name but not in controller. Distinct from LC-I-001 (a domain the org itself abandoned) because here the reassignment is routine and expected carrier behavior, not a lapse anyone could have prevented by not walking away from it.

**Status:** proposed.

**Fixture:** `lifecycle-identifier-reuse-and-rename` / `IRR-09`, `IRR-10`, `IRR-11`, `IRR-12` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-identifier-reuse-and-rename/README.md)

---

### Policy change

#### LC-I-004. A policy rollback needs a defined "current" pointer, not a race to see which edit lands last

**Situation.** An authorization policy is edited to add a permission, and the edit turns out to have unintended effects, so an operator wants to restore exactly the policy that was in force before. Whether that restoration is a clean single action, or a scramble to reconstruct what the prior version actually said, depends entirely on whether prior versions were kept as addressable, restorable objects in the first place.

**Human analog.** AWS IAM keeps up to five prior versions of a customer-managed policy and treats "current" as an explicit pointer rather than "whatever the file currently says." [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html): "In this case, you can roll back to a previous version of the managed policy by setting the previous version as the default version."

**What should happen.** A policy rollback should be the act of moving a single "operative version" pointer to a previously-issued, still-intact version, evidenced as a rollback (not as a fresh edit that happens to reproduce old text). Anything evaluated after the pointer moves is evaluated against the restored version, and anything evaluated before the move stays evidenced against whatever version was operative when it ran.

**What a naive system gets wrong.** Storing only the current policy text and reconstructing "what it used to say" from a separate audit log, if one exists at all. That treats rollback as a new edit indistinguishable from any other, losing the distinction between "we changed the rule" and "we undid a change," which matters for anyone later asking what a given decision was actually evaluated against.

**Related invariant/open question.** `AUTHORITY-LIFECYCLE.md`'s "policy version" concept names this ("The same action can be allowed under one version and denied under the next") but does not say what a rollback needs structurally. Adjacent to L6 (an earlier approval is not current authority) but about the policy itself changing, not the approval.

**Status:** proposed.

**Fixture:** `lifecycle-policy-change` / `PC-01`, `PC-02`, `PC-03`, `PC-04`, `PC-05` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-policy-change/README.md)

---

#### LC-I-005. What a past authorization decision is evidenced against has to be the policy version live at the moment it happened, not whatever version is live when someone later looks

**Situation.** A gateway records that a request was authorized. Later, an auditor or a downstream system retrieves that record after the operative policy has since been upgraded. If the retrieval renders the record using today's policy semantics instead of the semantics in force at decision time, the same historical decision can appear to mean something different than what was actually evaluated.

**Human analog.** Stripe pins each account to an API version at the moment a request or event happens, specifically so retrieving that record later doesn't reinterpret it under a newer version. [Stripe API documentation](https://docs.stripe.com/upgrades): "The default API version of your account at the time the event occurred defines the resources inside of events retrieved from the API."

**What should happen.** An authorization decision's evidence has to carry the policy version it was actually evaluated against, and any later rendering, audit, or downstream consumption of that record has to use that pinned version's semantics, not the version current at read time. Upgrading the live policy must not retroactively change what a past decision is understood to have meant.

**What a naive system gets wrong.** Storing only the decision's outcome (allow or deny) without pinning the policy version behind it, so a later reviewer has no way to tell whether a "denied" result reflects the rule that was actually in force or a rule that has since changed, and re-evaluates history under the wrong law without realizing it.

**Related invariant/open question.** Sharpens `AUTHORITY-LIFECYCLE.md`'s "policy version" concept into an evidence requirement: not just that decisions depend on a version, but that reconstructing a decision later requires pinning to it. None of L1-L12 address evidence rendering after a policy upgrade.

**Status:** proposed.

**Fixture:** `lifecycle-policy-change` / `PC-06`, `PC-07`, `PC-08`, `PC-09` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-policy-change/README.md)

---

#### LC-I-006. When a policy tightens after something was approved under the old rule, the old grant doesn't need to be revoked, and the new rule doesn't reach backward on its own

**Situation.** A use of a resource is lawfully established under one set of rules. The rules are later tightened so that the same use, if proposed today, would be denied. The question is not whether the tightened rule applies going forward (it plainly does, to new applicants) but whether it reaches back and invalidates the thing that was already validly approved.

**Human analog.** Massachusetts zoning law answers this directly for land use. [Massachusetts General Laws Chapter 40A, Section 6](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleVII/Chapter40a/Section6): "a zoning ordinance or by-law shall not apply to structures or uses lawfully in existence or lawfully begun, or to a building or special permit issued before the first publication of notice of the public hearing." A newer, stricter ordinance does not retroactively unwind a use that was lawful when established. It only binds what comes after.

**What should happen.** A verifier needs to distinguish "policy in force when a grant was issued and never revoked" from "policy in force now." A tightened policy should apply to new grants and new evaluations at the next authorization boundary, without a verifier treating the tightening itself as an implicit revocation of grants that were valid, and not since suspended or revoked, under the policy that governed them at issuance.

**What a naive system gets wrong.** Re-evaluating every existing grant against the newest policy version and treating a mismatch as automatic invalidity. That collapses "we changed the rule for new decisions" into "we revoked every decision made under the old rule," which is a much stronger and different action that nobody with standing actually took.

**Related invariant/open question.** A distinct case from L10 (expiry is not revocation): here nothing about the grant itself changed, expired, or was revoked. The surrounding policy changed instead. `AUTHORITY-LIFECYCLE.md`'s "policy version" concept names the dependency but not this grandfathering question, which none of L1-L12 address.

**Status:** proposed.

**Fixture:** `lifecycle-policy-change` / `PC-10`, `PC-11`, `PC-12`, `PC-13` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-policy-change/README.md)

---

### Expiry and renewal

#### LC-I-007. Reaching the stated end date and being cut off early for cause are different events, and an evidence trail has to say which one happened

**Situation.** An authority artifact carries a validity window. Two very different things can end it before anyone looks at it again: the window simply running out, or someone with standing acting early to end it for a specific, named reason. Collapsing the two into one "not valid" status loses exactly the information anyone investigating afterward would want.

**Human analog.** US passport regulations keep these as separate mechanisms with separate triggers. Expiration is the validity period simply running out. Revocation is a distinct governmental act on stated grounds. [22 CFR 51.62, via Cornell LII](https://www.law.cornell.edu/cfr/text/22/51.62): "The passport was illegally, fraudulently or erroneously obtained from the Department; or was created through illegality or fraud practiced upon the Department" is one of several named grounds for revocation, entirely separate from the document simply reaching its printed expiration date.

**What should happen.** An authority record needs a status that distinguishes "reached its planned end" from "ended early, for cause, by an act of someone with standing," with the cause and the actor recorded for the second case. A relying party checking status after the fact should be able to tell which happened without having to infer it from the date alone.

**What a naive system gets wrong.** Recording only a boolean "valid" or "not valid" with no distinction between the two paths to "not valid." That's exactly the gap L10 already names in the abstract. This case grounds it in a real, currently-in-force regulatory scheme that keeps the two mechanisms structurally separate, with different triggers, different actors, and different evidentiary requirements.

**Related invariant/open question.** A concrete instance of L10 (expiry is not revocation), sourced against a real regulatory scheme rather than stated as an abstract principle.

**Status:** proposed.

**Fixture:** `lifecycle-expiry-and-renewal` / `LC-I-007-a-reached-its-declared-end`, `LC-I-007-b-ended-early-for-cause`, `LC-I-007-c-later-expiry-does-not-rewrite-the-earlier-record`, `LC-I-007-d-revocation-claim-without-lifecycle-standing`, `LC-I-007-e-inside-its-declared-window` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-expiry-and-renewal/README.md)

---

#### LC-I-008. Calling it a "renewal" doesn't make it an extension. Some renewal processes issue an entirely new artifact and discard the old one outright

**Situation.** An operator "renews" a credential that's approaching its expiration date. Whether that renewal is (a) extending the validity window on the same underlying artifact, or (b) tearing down the old artifact entirely and issuing a brand-new one that happens to cover the same subject, changes what evidence exists afterward and what it means for anything that referenced the old artifact by its own identity.

**Human analog.** Let's Encrypt is explicit that its renewal path is not an extension mechanism at all. [Let's Encrypt](https://letsencrypt.org/how-it-works/): "Renewing a certificate at a later time means repeating the issuance process over again - performing domain validation and then requesting a new certificate." The old certificate is not modified or extended. A new one is issued, with its own serial number, and the old one simply continues toward its original, unchanged expiration.

**What should happen.** A verifier should treat "renewed" as ambiguous language until the underlying mechanism is known. Where renewal issues a new artifact, that new artifact needs its own full evaluation, not treatment as a continuation of the old one's identity, and evidence tied to the old artifact's identifier does not automatically transfer to the new one just because a human calls it the same credential.

**What a naive system gets wrong.** Assuming "renewed" means "the same authority, later end date," and carrying forward assumptions, caches, or trust decisions keyed to the old artifact's identifier onto what is structurally a fresh grant that happens to cover the same subject.

**Related invariant/open question.** Concretizes L3 (reauthorization creates new authority) for the specific case of renewal-as-reissuance, and is the sourced, non-legal counterpart to the "renewal as new authority" framing this family is built around.

**Status:** proposed.

**Fixture:** `lifecycle-expiry-and-renewal` / `LC-I-008-a-renewal-is-a-new-artifact`, `LC-I-008-b-superseded-artifact-runs-to-its-own-end`, `LC-I-008-c-evidence-keyed-to-the-superseded-artifact`, `LC-I-008-d-extension-in-place-does-not-bind`, `LC-I-008-e-renewal-widens-beyond-its-parent` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-expiry-and-renewal/README.md)

---

#### LC-I-009. An interim holder's mandate to keep the lights on is not a mandate to make new, binding commitments in the vacancy's name, including extending its own reach

**Situation.** An office holding significant authority becomes vacant. A body is appointed, or falls into the role, to keep essential functions running until a successor is in place. The question is whether that interim body may, on its own authority, take actions that go beyond keeping things running, including granting itself a broader or longer mandate than the caretaker role it was given.

**Human analog.** Canon law is explicit that the interim governing body during a papal vacancy is bounded to caretaking, and names the boundary directly. [Universi Dominici Gregis, Vatican](https://www.vatican.va/content/john-paul-ii/en/apost_constitutions/documents/hf_jp-ii_apc_22021996_universi-dominici-gregis.html): "the government of the Church is entrusted to the College of Cardinals solely for the dispatch of ordinary business and of matters which cannot be postponed." The same document restricts the College from issuing binding decrees outside urgent necessity, and reserves matters belonging to the office itself for whoever next holds it.

**What should happen.** An interim holder's authority should be evidenced as bounded to the specific caretaking scope it was given at the moment it took on the role, and an action that expands that scope, including one that extends or renews the interim holder's own mandate, needs its own separate grant from whoever has standing to give one. The interim role itself is not standing to expand the interim role.

**What a naive system gets wrong.** Treating "currently holds the authority to act for this office" as equivalent to "may decide the scope and duration of holding it." Those are different questions, and an interim holder answering the second one for itself is exactly the self-dealing a caretaking mandate is meant to prevent.

**Related invariant/open question.** Distinct from L4 (a successor does not inherit the predecessor's delegation tree), which is about descendants, not about the interim holder's own scope. Touches OPEN-QUESTIONS.md's "office vacancy and succession," which this document leaves open. This case does not resolve that question, only illustrates one governing model's answer for one specific office, without any claim that the mechanism generalizes.

**Status:** proposed.

**Fixture:** `lifecycle-expiry-and-renewal` / `LC-I-009-a-inside-the-recorded-caretaking-scope`, `LC-I-009-b-outside-the-recorded-caretaking-scope`, `LC-I-009-c-child-extends-past-the-interim-grant`, `LC-I-009-d-extension-record-is-not-a-fresh-grant`, `LC-I-009-e-self-extension-by-the-interim-holder` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-expiry-and-renewal/README.md)

---

### Shared identity with no accountable principal

#### LC-I-010. A credential answering "who did this" with a group name instead of a person is a standard-recognized failure mode, not just a bad habit

**Situation.** Multiple people share one login (a generic "admin" or "root" account, or a team-wide credential) to operate a system. When something goes wrong, the system's own logs can say what the shared identity did, but not which person was actually driving it at the time.

**Human analog.** PCI DSS treats this as a named, prohibited pattern rather than a style preference. [PCI Security Standards Council FAQ](https://www.pcisecuritystandards.org/faqs/1080/): "use of any shared authentication credentials such as group, shared, or generic IDs (including for administrator accounts such as admin or root) must be prevented unless needed for an exceptional circumstance." The standard's stated reason is that shared credentials break the link between an action and the individual accountable for it.

**What should happen.** A verifier evaluating "who is accountable for this action" needs a distinct answer from "which credential authenticated this action" whenever the two can diverge. Where a system permits shared credentials at all, it needs a compensating mechanism, such as a broker that checks out individual identity before use, that reconstitutes individual accountability rather than accepting the group identity as the final answer.

**What a naive system gets wrong.** Treating "the request came from a valid, authenticated identity" as equivalent to "we know who is accountable for it." A shared identity can be perfectly valid, currently authorized, and completely uninformative about who actually acted, which is a different failure from an invalid or revoked credential and needs its own status.

**Related invariant/open question.** `AUTHORITY-LIFECYCLE.md`'s "accountability record" concept names this directly ("Who a system identifies as responsible for an agent or action") but none of L1-L12 name shared identity itself as a distinct authority-lifecycle problem, as opposed to an access-control hygiene issue.

**Status:** proposed.

**Fixture:** `lifecycle-shared-identity-with-no-accountable-principal` / `LC-I-010-a`, `LC-I-010-b`, `LC-I-010-c`, `LC-I-010-d`, `LC-I-010-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-shared-identity-with-no-accountable-principal/README.md)

---

#### LC-I-011. When an action comes out of a shared identity, "who is accountable" can be a fact that has to be investigated after the fact, not something the identity itself ever recorded

**Situation.** An organization's public-facing account is operated by more than one person at an outside agency, sharing one set of login credentials and one piece of client software. An offensive message goes out from the account. For a period afterward, the organization itself cannot say, from any record the account produced, which individual sent it. That has to be established separately, by the agency investigating who had control of the tool at that moment.

**Human analog.** In 2013, an employee of Chrysler's social-media agency, New Media Strategies, posted an obscene message from Chrysler's own branded Twitter account while meaning to post it from a personal one. [NBC News](https://www.nbcnews.com/id/wbna42132041) reports he mistakenly used "a program that aims to help users juggle multiple Twitter accounts." Chrysler's own public response, quoted by [InformationWeek](https://www.informationweek.com/it-leadership/chrysler-addresses-twitter-foul-up), stated only that "the company has set in place appropriate steps to ensure that this does not happen again," without the account's own records identifying the individual. That came from the agency's internal review.

**What should happen.** Where an identity is operated by more than one accountable individual through shared tooling, the record of an action taken under that identity should say so, as "shared identity, individual attribution pending or external," rather than implying the identity itself is the accountable party. Establishing which individual acted is then a separate investigative fact, evidenced when it becomes available, not something the original action's record can supply on its own.

**What a naive system gets wrong.** Treating the identity that posted (the brand account) as if it were also the accountable principal, when the entire incident shows the two are different facts that came apart exactly when it mattered, and the gap between them had to be closed by an outside investigation rather than any record the system itself kept.

**Related invariant/open question.** A real-incident instance of the same "accountability record" gap as LC-I-010, at the social-media-operations layer instead of a technical admin account, and without a compliance standard mandating a fix.

**Status:** proposed.

**Fixture:** `lifecycle-shared-identity-with-no-accountable-principal` / `LC-I-011-a`, `LC-I-011-b`, `LC-I-011-c`, `LC-I-011-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-shared-identity-with-no-accountable-principal/README.md)

---

#### LC-I-012. A privileged identity that can act for everyone has to be structurally exceptional, not just discouraged in policy

**Situation.** A cloud account's root identity has unlimited power over everything in the account and is meant only for a short list of tasks nothing else can perform. If it is used for ordinary daily work instead, by whoever happens to hold its credentials at the time, no individual identity below it is doing the acting, and no scoped grant is what's actually in force.

**Human analog.** AWS documents the root identity as intentionally exceptional and warns against routine use. [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html): "We strongly recommend that you don't use the root user for your everyday tasks." The guidance pairs this with a specific, enumerated list of tasks that require root, implying that anything off that list done as root is root being used somewhere it structurally shouldn't be.

**What should happen.** A verifier or policy engine should treat use of an unscoped, all-powerful identity for a task not on its enumerated required-list as itself an anomaly worth its own evidence trail, distinct from ordinary scoped-identity activity, precisely because that identity has no accountable individual bound to it by design. It is meant to be reached for rarely and by whoever currently holds its credentials.

**What a naive system gets wrong.** Auditing root-identity actions the same way as any scoped identity's actions, when the entire point of a root identity is that it isn't scoped to one accountable person in the first place, so "it was root" is a materially weaker statement about who is accountable than "it was this named user."

**Related invariant/open question.** A structural, preventive counterpart to LC-I-010 and LC-I-011: a design recommendation to keep the highest-privilege identity from being a shared-accountability identity at all, rather than a rule for handling shared accountability once it already exists.

**Status:** proposed.

**Fixture:** `lifecycle-shared-identity-with-no-accountable-principal` / `LC-I-012-a`, `LC-I-012-b`, `LC-I-012-c` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-shared-identity-with-no-accountable-principal/README.md)

---

### Purpose exhaustion

#### LC-I-013. A grant issued for exactly one use is supposed to stop being usable the instant it's used once, and a protocol can make that a hard, checked rule instead of a convention

**Situation.** An authorization artifact is issued to cover exactly one downstream exchange, not a standing capability. Whether "used once" is actually enforced, or merely intended, determines whether a captured or replayed copy of the artifact is worthless to an attacker or just as good as the original.

**Human analog.** OAuth 2.0 makes single-use a checked server-side rule for the authorization code, not just guidance to the client. [RFC 6749, Section 4.1.2](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2): "The client MUST NOT use the authorization code more than once." The same section requires the authorization server to deny a repeat attempt and revoke everything already issued from that code if one is presented twice, treating the second use as evidence of compromise rather than an ordinary retry.

**What should happen.** A grant scoped to a single specific purpose should be checkable, by the issuer, as exhausted the moment it's used, with the underlying record (not merely the client's own restraint) enforcing that a second presentation fails and is treated as suspicious. The exhaustion event itself is the evidence that the grant's one purpose is complete. Nothing else needs to happen for it to become unusable again.

**What a naive system gets wrong.** Relying on the requesting party to simply not reuse a single-use grant, rather than having the issuer track and reject reuse itself. That converts a machine-checkable exhaustion condition into an honor system, which fails exactly when it matters most, against a party that captured the artifact and has no reason to be honest about it.

**Related invariant/open question.** Grounds `AUTHORITY-LIFECYCLE.md`'s "expiry or exhaustion" concept in a protocol that already treats exhaustion as machine-checkable and reuse as an actionable signal, which is a stronger and more specific claim than L10's expiry-versus-revocation distinction addresses.

**Status:** proposed.

**Fixture:** `approval-single-use` / no vector ids named in the coverage table (on the conformance suite main branch), and `lifecycle-purpose-exhaustion` / `LC-I-013-a`, `LC-I-013-b`, `LC-I-013-c`, `LC-I-013-d`, `PXE-04`, `PXE-05` (candidate, not yet merged)

---

#### LC-I-014. A permit issued for a single, specific act can be built so that using it is the same recorded event as spending it, with no separate step required to make it unusable again

**Situation.** A permit authorizes exactly one specific act, not an ongoing activity. The permit holder is required, by the terms of the permit itself, to mark it as used at the moment the act occurs, and once marked, no process exists to un-mark it or reuse it for a second act.

**Human analog.** Virginia's hunting regulations require exactly this at the point of a harvest. [4VAC15-40-290, Virginia Law](https://law.lis.virginia.gov/admincode/title4/agency15/chapter40/section290/): "It shall be unlawful for any person to validate (i.e., notch) a paper tag prior to the killing of a bear, deer, elk, or turkey," and once that validation happens through the electronic reporting system, "all electronically notched tags are permanent and cannot be voided." The permit's purpose (authorizing one specific harvest) and its exhaustion (recording that harvest) are the same act.

**What should happen.** Where a grant authorizes one specific, identifiable act, the system should be built so the act of using it and the act of exhausting it are the same recorded event, with no separate revocation, cleanup, or expiry step needed afterward. A verifier checking the grant's status after that point should see "purpose fulfilled, exhausted," not "still valid until its stated end date," even if that date hasn't arrived.

**What a naive system gets wrong.** Modeling every grant on a validity-window template (issued, valid until a date, then expired) even when the grant's real terminating condition is "used for the one thing it authorized," which can happen well before, or have nothing to do with, any calendar date on the artifact.

**Related invariant/open question.** A second, independently-sourced instance of the same machine-checkable exhaustion question as LC-I-013, grounded in a real regulatory permit scheme instead of a technical protocol, showing the pattern isn't specific to software credentials.

**Status:** proposed.

**Fixture:** `lifecycle-purpose-exhaustion` / `LC-I-014-a`, `LC-I-014-b`, `LC-I-014-c`, `LC-I-014-d`, `LC-I-014-e` (candidate, not yet merged)

---

## Reviewed hypothetical cases

### Organization events

#### LC-B-002. Two independently authoritative records of the same fact can disagree, and neither is automatically the answer

**Situation.** A payments agent checks authority against a bank's own signatory records. The company revoked a human officer's authority in its internal records days earlier but never sent the bank an updated signature card. The bank's system still shows the officer, and any delegation rooted in that officer, as active.

**Human analog.** No external precedent claimed.

**What should happen.** Two systems of record disagree about whether the root authority is current. A verifier that only checks one side's copy returns a confident answer that may be wrong. Where no source is designated as authoritative for a given fact, the correct behavior is to surface the conflict as indeterminate, not to pick a side.

**What a naive system gets wrong.** Treating "the resolver answered" as sufficient, without asking whether that resolver is the one designated authoritative for this particular fact, produces a confident wrong answer instead of an indeterminate one.

**Related invariant/open question.** L7 covers an unavailable or stale answer from a single resolver. This is a different shape: two live, reachable resolvers giving different current answers for the same underlying authority fact, which none of L1-L12 name.

**Status:** proposed.

**Fixture:** `conflicting-status-sources` / `CSS-04-fresh-conflict-denies-with-conflict-reason`, `CSS-05-stale-revoked-against-fresh-active-denies`, `CSS-08-no-usable-answer-not-established` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/conflicting-status-sources/README.md)

---

#### LC-B-004. A successor's fresh grant is bounded by the successor's own ceiling, not the predecessor's

**Situation.** An officer departs suddenly and an interim officer is appointed with a narrower mandate than the departed officer held, for example no authority to sign new financing agreements above a reduced threshold. The agent's old delegation still names the departed officer's broader scope.

**Human analog.** No external precedent claimed.

**What should happen.** A successor's fresh grant can only ever be issued within the successor's own current ceiling, even where a departed predecessor held broader authority and an old delegation still names it.

**What a naive system gets wrong.** A system that checks only whether a currently valid successor exists in the role, and re-parents the old chain to the interim officer without re-checking scope, grants authority the interim officer was never given.

**Related invariant/open question.** L4 is tested only as chain independence, a successor's own grants don't inherit the predecessor's tree. This adds that even when a successor does issue a fresh grant, the grant is bounded by the successor's own ceiling, not the predecessor's.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-004-a`, `LC-B-004-b`, `LC-B-004-c`, `LC-B-004-d`, `LC-B-004-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

#### LC-B-030. A third party's own contract can impose a re-authorization gate neither side of a clean succession controls

**Situation.** Company A acquires Company B in a clean statutory merger. A's authority over B's affairs is automatically intact under ordinary merger-vesting law. But B had a supply contract with Vendor C containing a change-of-control clause requiring C's consent before the contract continues past an acquisition. An ordering agent that operated under B's authority to place orders with C is not authorized to keep doing so under that specific contract until C consents, even though nothing about A's or B's own internal authority is in question.

**Human analog.** No external precedent claimed.

**What should happen.** The limiting factor here is not the acquirer's or target's own authority chain at all, but a condition a third party attached to a specific relationship. Some re-authorization checkpoints are triggered by, and controlled by, someone entirely outside the principal-agent-successor structure the invariants otherwise assume.

**What a naive system gets wrong.** A system that only checks whether the acquiring company's own internal succession is valid concludes the ordering agent may keep placing orders with Vendor C, missing that Vendor C's own contract independently requires consent nobody internal to A or B can supply.

**Related invariant/open question.** Complements the already-verified LC-B-012 (statutory merger) and LC-B-026 (consent-decree gate) by identifying a third, independent layer: even when the corporate-law layer and the internal delegation layer are both clean, a bilateral contract with an unrelated third party can impose its own, separately controlled re-authorization gate.

**Status:** proposed.

**Fixture:** `lifecycle-organization-events` / `LC-B-030-a`, `LC-B-030-b`, `LC-B-030-c`, `LC-B-030-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-organization-events/README.md)

---

### Time and scheduling

#### LC-E-034. A queued action that outlasts a suspension needs a live check at fire time, not just at the moment it was queued

**Situation.** An agent's authority is suspended pending an investigation. It already had a recurring action queued to fire later. The suspension is lifted before the queued action's scheduled fire time. The scheduler holding the queued action has no visibility into suspension state at all, it only knows the schedule, and fires the action exactly as originally planned.

**Human analog.** No external precedent claimed.

**What should happen.** This particular timeline is actually benign under L8's own logic, since the suspension was already lifted before the action fired, so denying it would be wrong. The case is worth naming because the scheduler got the right answer by accident, having never checked live suspension state at all. The same scheduler would fire the action identically even if the suspension were still active at fire time, which is the actual failure this case points at.

**What a naive system gets wrong.** A scheduler that only checks authority state at the moment an action was queued, not at fire time, produces the correct result in this timeline purely by luck. Change nothing about the scheduler and only change the timeline so the suspension is still active at fire time, and it fires an action that should have been paused, because dormant queued work was never something L8's stated mechanism has a hook to act on until the scheduler itself checks live state at fire time.

**Related invariant/open question.** L8 is specified only in terms of pausing the use of authority and everything that depends on it, which implicitly assumes a live dependency to pause. A queued-but-not-yet-executing action is dormant, not in use, so L8's text does not make explicit that the scheduler must check live state at fire time for the scheduled-action case specifically.

**Status:** proposed.

**Fixture:** `lifecycle-time-and-scheduling` / `LC-E-034-a-suspension-lifted-before-fire`, `LC-E-034-b-suspension-still-active-at-fire`, `LC-E-034-c-revoked-between-queue-and-fire`, `LC-E-034-d-suspension-source-silent-at-fire-time` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-time-and-scheduling/README.md)

---

### Credential events

#### LC-F-035. Choosing a stateless bearer credential format is choosing "revocation only takes effect at natural expiry"

**Situation.** A deployment issues a delegation credential as a self-contained, signed bearer artifact with a long validity window, verified purely by signature with no server-side revocation lookup, for performance reasons. When that credential needs to be revoked early (compromised agent, principal fired), the deployment discovers there is no way to invalidate it before its stated expiry without adding the very lookup step the design chose to avoid.

**Human analog.** No external precedent claimed.

**What should happen.** A deployment that chooses stateless, non-looked-up bearer credentials is implicitly choosing "revocation only takes effect at natural expiry" for that credential class, and must set expiry short enough to bound worst-case exposure, and must evidence this design tradeoff explicitly rather than presenting the credential as ordinarily revocable.

**What a naive system gets wrong.** Treating "we can revoke it" as a universal property of the authority system rather than a per-credential-format property, so an operator attempts to revoke a stateless bearer credential, sees the revocation API call return success, and does not realize the credential itself remains independently valid to anyone still holding it until it expires.

**Related invariant/open question.** L8 distinguishes suspension from revocation as two effective states an implementation can produce. This case is about a credential format for which neither can actually be produced early at all without a design change, a prerequisite question the invariants assume is already solved.

**Status:** proposed.

**Fixture:** `lifecycle-credential-events` / `LC-F-035-a-revocation-not-yet-effective-for-this-credential-class`, `LC-F-035-b-revocation-effective-where-status-is-looked-up` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-credential-events/README.md)

Variants: LC-F-034 (ambiguity is about how far a revocation cascades across derived tokens once cascading is possible, not about whether the base credential format can be revoked early at all).

---

### Infrastructure failure

#### LC-F-009. A publisher un-saying its own false revocation is a different operation from reauthorization, and needs its own evidence trail

**Situation.** A bug in the status-list build pipeline publishes a version that wrongly marks a block of active delegations as revoked. The error is caught and a corrected version is republished, but some gateways already cached the bad version and keep denying valid agents until their next scheduled fetch.

**Human analog.** No external precedent claimed.

**What should happen.** A publish-time bug that wrongly marks authority revoked must be correctable by republishing, but the incident must be evidenced (which version, which window, which consumers likely affected), since some agents may have been wrongly denied and need remediation, not just future consumers being spared.

**What a naive system gets wrong.** Republishing a corrected version and considering the incident closed, without accounting for effects already caused during the bad-version window, or for consumers still holding the bad version until their next scheduled fetch.

**Related invariant/open question.** L3 says reauthorization creates new authority and revocation is irreversible. This is the opposite direction: a publisher un-saying its own false revocation, which needs a distinct operation and its own evidence trail rather than being modeled as either a normal revocation or a routine reauthorization.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-009-a`, `LC-F-009-b`, `LC-F-009-c`, `LC-F-009-d`, `LC-F-009-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

Variants: D-012 (the scope of a past disclosure revised upward long afterwards, reaching the same correct-the-record question from the claim side rather than the revocation side).

---

#### LC-F-014. An issuer's own timestamp is only as trustworthy as the time source it was signed against

**Situation.** An authority issuer relies on a single external time reference to stamp issued_at on the artifacts it signs. That reference is spoofed or jammed, and the issuer signs artifacts with a shifted timestamp, for example one that appears to predate a revocation that has already happened, while the issuer's own internal logs show no anomaly.

**Human analog.** No external precedent claimed.

**What should happen.** An issuer should not treat a single external time reference as ground truth without cross-checking against at least one independent source. Artifacts signed during a detected time-source disagreement window should be flagged for re-verification once trusted time is restored.

**What a naive system gets wrong.** Trusting one time source unconditionally means a spoofed source can mint artifacts with an artificially shifted validity window, for example one that appears to predate issuance in order to predate a revocation.

**Related invariant/open question.** None of L1-L12 discuss adversarial control of the issuer's own time source. L9 addresses selecting the historically correct key version, which assumes the timestamp being resolved against is honest.

**Status:** proposed.

**Fixture:** `lifecycle-infrastructure-failure` / `LC-F-014-a`, `LC-F-014-b`, `LC-F-014-c`, `LC-F-014-d`, `LC-F-014-e` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-infrastructure-failure/README.md)

---

## Candidate cases

Not yet verified. Each one carries a "Known issue" note saying what is missing.

### Subdelegation edges

#### LC-H-009. A child subdelegation issued inside a revocation's propagation window is void once the revocation is established, a hypothetical naming a gap distinct from L1

**Situation.** A principal revokes a delegation. Before that revocation's effect has propagated to every verifier or resolver a system relies on, the not-yet-visibly-revoked chain is used to issue a brand new child subdelegation to a further party.

**Human analog.** None cited. This is a hypothetical, not a documented incident or a legal or standards text, because no source located in this session names this specific issuance-during-propagation-window shape as its own defined event, as distinct from the general staleness question L7 and the F-family propagation-lag cases already cover for read checks, not for new issuance.

**What should happen.** The new child's authority should be evaluated against the revocation once the revocation is established as having occurred, not against whatever the issuer's local, possibly stale, view of the parent's status happened to be at the moment of issuance. If the parent was in fact already revoked at the source when the child was minted, the child is void from issuance, not merely suspended pending catch-up, once that fact is established. This does not retroactively rewrite what the issuer's own contemporaneous record said. It is a later finding, layered on top of it.

**What a naive system gets wrong.** Treating a child issued while the issuer's local view still showed the parent as valid as itself validly issued, on the theory that the issuer acted in good faith on the information available. That confuses the issuer's good-faith belief with the child's actual authority, which depends on the parent's true status, not on what any one node had already observed.

**Related invariant/open question.** L1 covers a chain that already existed at the moment of an ancestor's revocation. This case is the narrower and harder edge L1 does not name: new issuance happening inside the propagation window itself, after the revocation exists at the source but before it is visible everywhere. Also touches L7 and the F-family propagation-lag cases, but for write-time (new issuance) rather than read-time (an authorization check).

**Known issue.** Honestly labelled hypothetical with no fetched source, so it does not meet the verified bar. Status is candidate until a source is found or the case is rewritten around one.

**Status:** candidate.

**Fixture:** `lifecycle-subdelegation-edges` / `LC-H-009-a`, `LC-H-009-b`, `LC-H-009-c`, `LC-H-009-d` (merged_candidate, https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-subdelegation-edges/README.md)

---
