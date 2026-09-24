# Open questions

Part of Authority Lifecycle v0.3.0-draft. From the Agent Passport System work. Apache-2.0.

These are the parts we do not know how to answer yet. They are listed so nobody mistakes the rest of the model for a claim about them.

Each question carries three lines. **Related cases** names cases in [CASES.md](CASES.md) by stable id. **Related candidates** names proposed invariants in [INVARIANT-CANDIDATES.md](INVARIANT-CANDIDATES.md) by CAND, BROAD or ANX id. **Related fixtures** names fixture families in the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite that the related cases and candidates point at. None of those links closes the question. A related candidate is proposed text, and a related fixture is a candidate vector against proposed text, not a conformance result.

## Teardown completeness

A list of processed descendants does not establish that the list was every authority descendant at the relevant boundary. Delegation can be issued locally, so a descendant can exist that the teardown process never saw, and a descendant can be signed after the revocation with a valid parent chain. Signed lineage proves structure. It does not prove the descendant was accepted authority when the revocation took effect.

A completeness claim needs three things we have not settled. What set a boundary claims to have accepted at a given moment. What prevents something from entering that set afterwards while still counting as earlier authority. What public commitment can prove closure over that set without exposing private state.

**Related cases.** LC-B-022 (a legal-claims exception as an actual basis for retention), LC-B-023 (preservation triggered by anticipated litigation, earlier than formal process), LC-D-003 (a believed inventory standing in for a verified one), LC-D-025 (what a grant was used for is a different completeness claim from whether it is valid), LC-F-027 (an empty audit window is delivery lag, not absence).

**Related candidates.** BROAD-L7, whose coverage limb is a rule for reading a state claim rather than a duty to establish coverage, and CAND-02, which keeps a later completeness finding as a new record rather than a rewrite. Neither closes L12.

**Related fixtures.** `lifecycle-legal-regulatory-events`, `lifecycle-credential-events`, `lifecycle-infrastructure-failure`. LC-B-023 has no fixture, because no record set decides it.

## Work in flight

When authority is revoked while a workflow is running, the old grant cannot authorize new effects at the next authorization boundary. What happens to the operation itself (resume under new authority, restart, compensate, stop) depends on the kind of effect. We do not yet have a general model for it.

**Related cases.** LC-B-029 (a receiving institution's acceptance as a terminal boundary a later change does not reach), LC-C-006 (an ancestor found invalid long after the fact), LC-E-008 (which policy version a long-running instance resolves its remaining steps against), LC-E-013 (invalidation arriving mid-run rather than at the next gateway check), LC-E-020 (dormant scheduled authority whose creator is gone).

**Related candidates.** BROAD-L6 (the decision at each boundary is fresh), CAND-12 (completed effects stand), CAND-16 (when a recorded change becomes effective). None of them says whether the operation resumes, restarts, compensates or stops.

**Related fixtures.** `lifecycle-organization-events`, `lifecycle-multiple-principals-and-conflict`, `lifecycle-time-and-scheduling`, `cached-authorization-revocation`.

## Release from suspension

Lifting one suspension should not clear another, bypass a revocation that happened while the agent was suspended, or recreate rights that changed in the meantime. Multiple suspension causes probably need to compose, with each one released separately. Not yet specified.

**Related cases.** LC-B-011 (an externally imposed restriction needing an equally external release trigger), LC-B-024 (independent suspensions released independently), LC-C-022 (a pending-ratification state that is neither revoked nor not revoked), LC-E-034 (a queued action that outlasts a suspension).

**Related candidates.** CAND-05, which makes causes a set and requires standing for each release, and CAND-09, which separates chain validity from an external block and its removal. CAND-05 defines no precedence order among causes.

**Related fixtures.** `lifecycle-legal-regulatory-events`, `lifecycle-multiple-principals-and-conflict`, `lifecycle-time-and-scheduling`, `suspension-cause-composition`.

## Critical revocation

Revoking a high-level authority can disable a large set of agents. An approval for such a revocation could be bound to a snapshot of its impact and checked again right before it takes effect, with uncertain impact treated as large rather than small. Designed, not yet built or tested.

**Related cases.** LC-B-025 (one revoked license invalidating every chain that depends on it at once), LC-D-004 (a compromised operator identity as an implicit ancestor over many independent trees), LC-D-014 (an issuer whose own issuance log cannot be trusted), LC-F-033 (systemic issuer misbehavior escalating to distrust of the whole issuer).

**Related candidates.** CAND-01 (an external event is authority-changing only when established) and ANX-01 (a verdict records its event-class coverage). Neither proposes binding an approval to an impact snapshot.

**Related fixtures.** `lifecycle-legal-regulatory-events`, `lifecycle-credential-events`.

## Office vacancy and succession

When authority was exercised for an office and nobody currently holds it, nobody may be empowered to exercise, reaffirm or revoke what the previous holder issued. Whether office-based grants continue, suspend or need reaffirmation during a vacancy, and who may act for the office until it is filled, is not defined.

**Related cases.** LC-C-007 (office binding against identity binding as an explicit design choice), LC-C-009 (a succession order that is deliberately not public), LC-A-019 (a vacancy that does not have to be filled before the remaining holders can act), LC-I-009 (an interim holder's caretaking scope, including extending its own mandate).

**Related candidates.** CAND-13 (replacement authority may be pre-committed) and CAND-04 (activation established, not yet effective, or not established), with CAND-03 separating issuance validity from current validity. None of them says what happens when nobody holds the office and nobody is empowered to act for it.

**Related fixtures.** `lifecycle-root-authority-succession`, `activation-not-established`, `lifecycle-fiduciary-succession`, `lifecycle-expiry-and-renewal`.

## Grants signed just before departure

If issuer standing is evaluated at issuance, an issuer who knows they are leaving can sign long-lived grants that stay valid after they are gone. A bounded lifetime for grants issued for an office, or a review when the office changes hands, are possible answers. Neither is specified.

**Related cases.** LC-C-007 (whether the grant was bound to the office or to the person), LC-A-016 (replacement authority pre-committed at issuance rather than issued after the fact), LC-H-010 (a resignation effective on delivery of notice, which fixes when the departure happened), LC-I-009 (an interim holder extending its own reach).

**Related candidates.** CAND-03, which separates issuance validity from current validity and deliberately does not answer this, and CAND-13, which covers pre-commitment but not a bound on what an outgoing issuer may pre-commit.

**Related fixtures.** `lifecycle-root-authority-succession`, `lifecycle-principal-events`, `lifecycle-agent-renunciation`, `lifecycle-expiry-and-renewal`.

## Authority rollback

Restoring a backup, a snapshot or a lagging replica can bring back authority state from before a revocation. An authority epoch, or an append-only record of revocations that a restore must replay, would stop a restore from reviving revoked authority. We have not specified either or tested what a verifier should return after a restore.

**Related cases.** LC-E-023 (a faithfully restored process holding authority that may no longer be current), LC-F-016 (a storage-layer partition resurrecting revoked authority below the application layer), LC-F-017 (a revocation true at the source and false at a lagging replica), LC-F-018 (regional enforcement points briefly disagreeing), LC-F-024 (a lock holder whose pause outlasts its lease), LC-F-026 (an isolated primary accepting writes nobody else will see).

**Related candidates.** CAND-08, which forbids acting on a state older than the newest established for that subject and requires an explicit attributable record to restore superseded authority.

**Related fixtures.** `authority-epoch-rollback`, `lifecycle-infrastructure-failure`, `conflicting-status-sources`.

## Semantic drift

A grant can stay byte for byte the same while what it authorizes changes, because a tool, an API version or a resource classification changed underneath it. When a change in meaning should invalidate an earlier grant or approval, and how a verifier would detect it, is open.

**Related cases.** LC-E-033 (a provider-side capability upgrade with no delegation-layer event), LC-E-001 (a stable model alias as a pointer with a documented default), LC-E-002 (a valid grant whose named executor is gone), LC-E-027 (a real precedent for gating expanded capability behind re-consent).

**Related candidates.** CAND-07 (a stable name does not establish stable semantics) and CAND-11 (a valid grant can be unexecutable). CAND-07 handles the pinned, unpinned and controller cases against a model-declared basis. Whether a change in meaning should invalidate an earlier grant, and how a verifier would detect it unaided, stays open.

**Related fixtures.** `capability-binding-drift`, `lifecycle-agent-side-events`.

## Notice and relying parties

A revocation can be recorded at one moment and reach an agent, a gateway and an outside counterparty at different moments. What a relying party that acted on stale but authentic evidence is entitled to, and what evidence of notice a principal needs to show, is not defined here. Agency law offers answers for human agents. This document does not assume they apply.

**Related cases.** LC-A-001 (termination effective on the agent's notice rather than at the event), LC-A-027 (a verifier's chain-is-void finding and a relying party's protected reliance as two facts), LC-A-028 (two tiers of notice for known counterparties and strangers), LC-H-006 (a disputed root deposited with a neutral forum), LC-I-001 (a re-registered identifier with no delegation-layer event marking the change of hands).

**Related candidates.** ANX-03, which separates chain validity from a party's knowledge and gives the notice finding its own timestamp, and CAND-16 on when a recorded change becomes effective. ANX-03 proposes the separation and nothing about entitlement.

**Related fixtures.** `lifecycle-principal-events`, `lifecycle-third-party-reliance-notice`, `lifecycle-multiple-principals-and-conflict`, `lifecycle-identifier-reuse-and-rename`.
