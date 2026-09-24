# Invariant candidates

Version 0.3.0-draft. Part of the Agent Passport System work. Apache-2.0, same terms as `AUTHORITY-LIFECYCLE.md`.

Everything in this file is **proposed**. Nothing here is specified, tested or implemented, and no conformance result exists for any candidate. These are statements we think implementations should guarantee, each with what it does not claim, the cases in [CASES.md](CASES.md) that force it, the strongest counterexample we found and why the statement survives it, and whichever fixture currently tests any part of it.

## Contents

- [At a glance](#at-a-glance)
- [How to read this file](#how-to-read-this-file)
  - [The two uses of "not established"](#the-two-uses-of-not-established)
- [Candidate invariants](#candidate-invariants)
  - [CAND-01. An external event is authority-changing only when established](#cand-01-an-external-event-is-authority-changing-only-when-established)
  - [CAND-02. Later evidence does not rewrite earlier evidence](#cand-02-later-evidence-does-not-rewrite-earlier-evidence)
  - [CAND-03. Issuance validity, later attached effects and current validity are three separate findings](#cand-03-issuance-validity-later-attached-effects-and-current-validity-are-three-separate-findings)
  - [CAND-04. Activation is established, not yet effective, or not established](#cand-04-activation-is-established-not-yet-effective-or-not-established)
  - [CAND-05. Suspension and restriction causes compose](#cand-05-suspension-and-restriction-causes-compose)
  - [CAND-06. Collective authority must satisfy its declared composition](#cand-06-collective-authority-must-satisfy-its-declared-composition)
  - [CAND-07. A stable name does not establish stable semantics](#cand-07-a-stable-name-does-not-establish-stable-semantics)
  - [CAND-08. No silent restoration from rollback or stale state](#cand-08-no-silent-restoration-from-rollback-or-stale-state)
  - [CAND-09. Chain validity is not permission to execute](#cand-09-chain-validity-is-not-permission-to-execute)
  - [CAND-10. Holding a scope does not establish authority to confer it](#cand-10-holding-a-scope-does-not-establish-authority-to-confer-it)
  - [CAND-11. A valid grant can be unexecutable](#cand-11-a-valid-grant-can-be-unexecutable)
  - [CAND-12. Ending authority bounds future effects, it does not undo past ones](#cand-12-ending-authority-bounds-future-effects-it-does-not-undo-past-ones)
  - [CAND-13. Replacement authority may be pre-committed](#cand-13-replacement-authority-may-be-pre-committed)
  - [CAND-16. A recorded lifecycle change is effective when the model's effectiveness rule is satisfied](#cand-16-a-recorded-lifecycle-change-is-effective-when-the-models-effectiveness-rule-is-satisfied)
- [Proposed broadening of existing invariants](#proposed-broadening-of-existing-invariants)
  - [BROAD-L6. L6 extends to every authorization boundary the operation requires](#broad-l6-l6-extends-to-every-authorization-boundary-the-operation-requires)
  - [BROAD-L7. L7 extends to any current lifecycle state claim](#broad-l7-l7-extends-to-any-current-lifecycle-state-claim)
- [Evidence and receipt annex](#evidence-and-receipt-annex)
  - [ANX-01. A verdict records its event-class coverage](#anx-01-a-verdict-records-its-event-class-coverage)
  - [ANX-02. A verifier can present an earlier record and a later finding together](#anx-02-a-verifier-can-present-an-earlier-record-and-a-later-finding-together)
  - [ANX-03. Chain validity and a relying party's knowledge are separate findings](#anx-03-chain-validity-and-a-relying-partys-knowledge-are-separate-findings)
  - [ANX-04. A declared scope is only as effective as the boundary that enforces it](#anx-04-a-declared-scope-is-only-as-effective-as-the-boundary-that-enforces-it)
- [What this document does not close](#what-this-document-does-not-close)
- [Fixture coverage](#fixture-coverage)
- [Contributing](#contributing)
- [Source notes](#source-notes)

## At a glance

Every row is **proposed**. The fixture column names what bears on the statement, not a conformance result. Full tested-by detail is in [Fixture coverage](#fixture-coverage), and the sources behind the case shapes are in [Source notes](#source-notes).

| ID | Candidate | Forced by | Fixture |
|---|---|---|---|
| [CAND-01](#cand-01-an-external-event-is-authority-changing-only-when-established) | An external event is authority-changing only when established | LC-B-008, LC-B-012, LC-B-025, LC-B-009, LC-A-001, LC-A-008, LC-A-010, LC-B-002, LC-C-005, LC-D-001, LC-D-003, LC-D-011, LC-D-034, LC-C-006 | `lifecycle-purpose-exhaustion`, held back on an unmerged branch |
| [CAND-02](#cand-02-later-evidence-does-not-rewrite-earlier-evidence) | Later evidence does not rewrite earlier evidence | LC-G-006, LC-B-007, LC-C-022, LC-A-023, LC-A-027, LC-C-006, LC-H-009, LC-F-009, LC-F-027, LC-D-025, LC-B-022, LC-I-005 | `authority-epoch-rollback` |
| [CAND-03](#cand-03-issuance-validity-later-attached-effects-and-current-validity-are-three-separate-findings) | Issuance validity, later attached effects and current validity are three separate findings | LC-H-004, LC-C-006, LC-B-008, LC-B-012, LC-B-013, LC-A-016, LC-A-012, LC-A-023, LC-B-007, LC-A-022, LC-B-004, LC-B-016, LC-B-017, LC-C-005, LC-C-007, LC-C-009, LC-D-029, LC-D-034, LC-H-005 | none |
| [CAND-04](#cand-04-activation-is-established-not-yet-effective-or-not-established) | Activation is established, not yet effective, or not established | LC-A-003, LC-A-016, LC-C-014, LC-H-012, LC-C-008, LC-C-015, LC-C-017, LC-C-020, LC-C-002, LC-E-034, LC-A-001, LC-A-008, LC-A-022, LC-G-007 | `activation-not-established` |
| [CAND-05](#cand-05-suspension-and-restriction-causes-compose) | Suspension and restriction causes compose | LC-B-024, LC-B-010, LC-B-011, LC-B-019, LC-B-018, LC-B-031, LC-B-016, LC-B-026, LC-B-030, LC-C-022, LC-C-029, LC-A-010, LC-E-034 | `suspension-cause-composition` |
| [CAND-06](#cand-06-collective-authority-must-satisfy-its-declared-composition) | Collective authority must satisfy its declared composition | LC-C-011, LC-C-016, LC-C-018, LC-C-012, LC-C-029, LC-A-019, LC-A-033, LC-H-001, LC-H-002, LC-H-004, LC-B-026 | `chain-selection-no-union`, negative half only |
| [CAND-07](#cand-07-a-stable-name-does-not-establish-stable-semantics) | A stable name does not establish stable semantics | LC-E-033, LC-E-001, LC-E-002, LC-E-027, LC-E-004, LC-E-025, LC-E-031, LC-E-023, LC-D-009, LC-D-029, LC-D-034, LC-D-033, LC-I-001, LC-I-002, LC-I-003 | `capability-binding-drift` |
| [CAND-08](#cand-08-no-silent-restoration-from-rollback-or-stale-state) | No silent restoration from rollback or stale state | LC-F-017, LC-F-026, LC-F-016, LC-F-018, LC-F-022, LC-F-024, LC-F-006, LC-F-009, LC-E-023, LC-D-003, LC-I-004 | `authority-epoch-rollback` |
| [CAND-09](#cand-09-chain-validity-is-not-permission-to-execute) | Chain validity is not permission to execute | LC-B-018, LC-B-019, LC-B-010, LC-B-011, LC-B-016, LC-B-026, LC-B-030, LC-B-031, LC-A-010, LC-B-027 | none |
| [CAND-10](#cand-10-holding-a-scope-does-not-establish-authority-to-confer-it) | Holding a scope does not establish authority to confer it | LC-E-006, LC-E-025, LC-E-004, LC-E-031, LC-E-023, LC-H-008, LC-H-007 | `lifecycle-conferral-without-authority` |
| [CAND-11](#cand-11-a-valid-grant-can-be-unexecutable) | A valid grant can be unexecutable | LC-E-002, LC-E-014, LC-E-020, LC-E-001, LC-C-025 | none |
| [CAND-12](#cand-12-ending-authority-bounds-future-effects-it-does-not-undo-past-ones) | Ending authority bounds future effects, it does not undo past ones | LC-E-021, LC-E-013, LC-E-019, LC-D-025, LC-B-029, LC-B-028, LC-A-023, LC-A-027, LC-I-013, LC-I-014 | none |
| [CAND-13](#cand-13-replacement-authority-may-be-pre-committed) | Replacement authority may be pre-committed | LC-A-016, LC-C-017, LC-C-020, LC-C-008, LC-C-015, LC-C-025, LC-C-002, LC-A-019, LC-B-012, LC-B-008, LC-H-005 | `activation-not-established`, activation half only |
| [CAND-16](#cand-16-a-recorded-lifecycle-change-is-effective-when-the-models-effectiveness-rule-is-satisfied) | A recorded lifecycle change is effective when the model's effectiveness rule is satisfied | LC-A-001, LC-B-009, LC-B-029, LC-H-010, LC-H-011, LC-H-009, LC-F-018, LC-C-006 | none |
| [BROAD-L6](#broad-l6-l6-extends-to-every-authorization-boundary-the-operation-requires) | L6 extends to every authorization boundary the operation requires | LC-B-028, LC-B-029, LC-B-026, LC-C-011, LC-C-018, LC-C-025, LC-E-013, LC-E-034, LC-E-018, LC-E-021, LC-E-008, LC-I-006, LC-D-025 | none |
| [BROAD-L7](#broad-l7-l7-extends-to-any-current-lifecycle-state-claim) | L7 extends to any current lifecycle state claim | LC-F-006, LC-F-008, LC-F-013, LC-F-017, LC-F-018, LC-F-027, LC-F-033, LC-F-035, LC-B-002, LC-C-005, LC-C-008, LC-C-009, LC-C-015, LC-D-003, LC-D-014, LC-D-011, LC-A-003, LC-G-008, LC-G-009 | `conflicting-status-sources` |
| [ANX-01](#anx-01-a-verdict-records-its-event-class-coverage) | A verdict records its event-class coverage | LC-B-008, LC-B-025, LC-D-001, LC-B-009 | none |
| [ANX-02](#anx-02-a-verifier-can-present-an-earlier-record-and-a-later-finding-together) | A verifier can present an earlier record and a later finding together | LC-B-007, LC-G-006, LC-C-022, LC-I-005 | `conflicting-status-sources`, CSS-12 touches it |
| [ANX-03](#anx-03-chain-validity-and-a-relying-partys-knowledge-are-separate-findings) | Chain validity and a relying party's knowledge are separate findings | LC-A-027, LC-A-028, LC-A-001, LC-F-027, LC-F-018 | none |
| [ANX-04](#anx-04-a-declared-scope-is-only-as-effective-as-the-boundary-that-enforces-it) | A declared scope is only as effective as the boundary that enforces it | LC-D-009, LC-D-027 (boundary case), LC-D-023 (boundary case), LC-D-019 (boundary case) | none |

## How to read this file

Ids stay in the CAND, BROAD and ANX series on purpose. Numbering them into the L series of [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md) would read as settled additions to the published invariant list, and they are not that. L12 is the last published invariant and nothing here extends the numbering past it.

A **tested by** entry names a fixture in the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite and the vectors in it that bear on the candidate. Most of those fixtures are now merged_candidate, pinned to the lab main commit the [Fixture coverage](#fixture-coverage) table links. `lifecycle-purpose-exhaustion` is held back and stays on an unmerged candidate branch. A fixture existing, merged or not, does not make a candidate tested in the sense `AUTHORITY-LIFECYCLE.md` uses, because these vectors are candidates against proposed text rather than conformance cases against a published specification. Where a candidate says nothing, nothing tests it.

Legal, aviation, financial, data-protection and distributed-systems material is used below as the origin of case shapes and of counterexamples. None of those sources says anything about AI agents, and nothing here asserts that any legal doctrine applies to AI agents.

<a name="verdict-vocabulary"></a>

The verdict vocabulary these statements are written against, meaning the artifact verdicts, the boundary outcomes and the reason-code rule, lives in [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md#verification-model).

### The two uses of "not established"

Keep the name for the evidential sense: the verifier cannot reach the conclusion because a source is missing, unrecognised, stale past its bound, silent, self-attested with nothing to check it against, or in unresolved conflict with another accepted source.

Where the verifier has reached a conclusion and the conclusion is negative, name the shape instead.

| Shape | Correct output |
|---|---|
| An enabling condition is established not to have occurred yet | artifact verdict **not yet effective** |
| A composition rule is established not to be satisfied | boundary outcome **denied**, reason `composition_not_satisfied` |
| A pinned referent is established to have changed | boundary outcome **denied**, reason `pinned_referent_mismatch` |

That keeps "not established" meaning exactly one thing, which is what makes it testable.

<a name="the-candidates"></a>

## Candidate invariants

### CAND-01. An external event is authority-changing only when established

**Statement.** A verifier may treat an external event as authority-changing only when evidence it accepts establishes both the event and its authority effect under the applicable authority model. Absence of such evidence yields not established for the event, which is not a finding that the event did not occur.

**What it does not claim.**

- It does not claim the world only changes when a record exists. External events change authority with no record anywhere. S2 has receivership powers passing "by operation of law". S3 has a stay that "operates as a stay, applicable to all entities" on filing. S24 has an order "canceled by operation of law" at a fixed deadline with nobody doing anything. S17 lists "the occurrence of circumstances specified by statute" as a termination route. The candidate constrains the verifier's output, not the world.
- It does not claim a valid verdict means no authority-changing event has occurred. A valid verdict means the verifier found nothing it was looking for. What it was looking for is the annex requirement ANX-01, not this statement.
- It does not claim only affirmative records count. An authority model may make absence itself the trigger or supply a default on absence. LC-C-008 is the case.
- It does not say which events are authority-changing. That is the authority model's job and it varies.
- It does not resolve notice or effectiveness timing. Whether the effective moment is the event or a later moment is CAND-16.
- It does not forbid a status protocol from reporting a conservative superset. S27 permits an OCSP responder to return revoked where the CA "has no record of ever having issued" the certificate. A verifier acting on that answer is following its model, not inventing an event.

**Forced by.** LC-B-008, LC-B-012, LC-B-025, LC-B-009, LC-A-001, LC-A-008, LC-A-010, LC-B-002, LC-C-005, LC-D-001, LC-D-003, LC-D-011, LC-D-034, LC-C-006.

**Strongest counterexample.** LC-C-008. A successor designation is simply missing, and under the applicable model the absence resolves to a named statutory fallback holder. The case's own text says the correct behaviour is the opposite of L7's fail-closed answer. A literal reading of CAND-01 would return not established and deny authority the model says exists. The sharper second form is S27: a deployed protocol tells a responder it may report revoked for something never issued, and a verifier that returns not established there gives up the exact safety property that language was added for.

**How the statement survives.** The clause "under the applicable authority model" carries both. In LC-C-008 the established event is the absence, and the model's own default rule supplies the authority effect. Absence is evidence when the model says absence is dispositive. In the S27 case the model is RFC 6960 and it has told the verifier what a revoked answer means, so the verifier has established the authority effect from a source its model accepts. The separation of establishing the event from establishing its authority effect is what makes both readable, because models differ on the second even when they agree on the first. S28 reinforces rather than undercuts this, since the same section keeps unknown available precisely so a client can "decide whether it wants to try another source of status information".

**Tested by.** `lifecycle-purpose-exhaustion` PXE-08 and PXE-09, an event record that is unauthenticated, or authenticated by a party without standing, leaving the effect not established. PXE-01 to PXE-03 cover the established side. `conflicting-status-sources` CSS-04 and CSS-05 for two accepted sources disagreeing. **Not covered:** the by-operation-of-law shapes, the default-on-absence shape, and the conservative-superset non-claim.

**Status.** proposed.

---

### CAND-02. Later evidence does not rewrite earlier evidence

**Statement.** Later lifecycle evidence does not rewrite contemporaneous decision evidence. A later finding is a new record that references the earlier one and states its own effect, including how far back that effect reaches.

**What it does not claim.**

- It does not claim the earlier decision's authority effect is unchanged. Retroactive effect is real. S11 has ratification that "retroactively creates the effects of actual authority". The candidate says that effect arrives as a new record, not as an edit.
- It does not claim a later finding can reach back without limit. S12 bounds one model's reach explicitly, excluding effect "to diminish the rights or other interests of persons, not parties to the transaction, that were acquired in the subject matter prior to the ratification".
- It does not claim receipts are immutable or undeletable. A retention obligation can end and a deletion obligation can attach.
- It does not override a correction or rectification obligation that attaches to the content of a record. S36 gives a right to obtain "the rectification of inaccurate personal data", which is neither deletion nor annotation. Where such an obligation requires amendment rather than a supplementary note, what must survive is that a decision was made at that time on the inputs then available, plus the fact and authorship of the amendment. A regime that requires amendment is not a regime that permits silent amendment. S37 shows the same article also contemplating the append model, "including by means of providing a supplementary statement", so the regime does not choose for us.
- It does not say who has standing to make a later finding. That is lifecycle standing, a separate question.

**Forced by.** LC-G-006, LC-B-007, LC-C-022, LC-A-023, LC-A-027, LC-C-006, LC-H-009, LC-F-009, LC-F-027, LC-D-025, LC-B-022, LC-I-005.

**Strongest counterexample.** LC-C-022 read with S11. Denial of ratification recharacterises a past action as having only ever been provisional. That is recharacterisation of the past, which is the closest thing in the corpus to a rewrite. The harder second form is S36, where a model obliges amendment of the record itself rather than annotation.

**How the statement survives.** In LC-C-022 the recharacterisation is itself a dated record made by a party with standing, and the earlier receipt is what it references. The corpus wording rule is the operational form of this, and the required sentence, that the action was provisional throughout, is only writable if the original receipt still exists in its original form. So retroactivity is an argument for CAND-02, not against it. The S36 case is handled by the non-claim rather than by the statement, because the obligation attaches to record content and not to lifecycle findings, and because what CAND-02 needs to survive an amendment is the decision's time, its inputs, and the authorship of the change. LC-H-009 is the cleanest corpus confirmation, since it describes a later finding that changes the child's status while explicitly leaving the issuer's contemporaneous record alone.

**Tested by.** `authority-epoch-rollback` AER-11 and AER-12, a signed withdrawal accepted as a new record with the original still held and still verifying. `conflicting-status-sources` CSS-12. **Not covered:** the bounded-reach limb, the amendment-obligation case, and the policy-version rendering limb.

**Status.** proposed. The draft's third sentence, requiring the verifier to be able to present both records and their relation, moves to the annex as ANX-02.

---

### CAND-03. Issuance validity, later attached effects and current validity are three separate findings

**Statement.** Three findings about an authority artifact are separate and separately established. First, whether the artifact was validly issued, which turns on the issuer's standing at the moment of issuance and whose answer does not change with later events. Second, whether a later record from a party with lifecycle standing has attached effects to the artifact or to acts taken under it, including effects the governing authority model gives retroactive reach. Third, whether the artifact is currently valid, which turns on its declared dependencies, its lifecycle state, any external restriction and the model's freshness rules. A verifier must not report any one of these as if it answered another.

**What it does not claim.**

- It does not claim standing at issuance can be inferred from a valid signature. LC-D-029 is the case where the signature is correct and what it attests is false.
- It does not claim an organizational grant survives its issuer's departure, and it does not claim the opposite. The governing model decides. The Lyondell exhibit could not be fetched in this session, so no external claim is made either way.
- It does not claim current validity is a single check. It is at least dependencies, lifecycle state, external restriction and freshness, which is why BROAD-L7 exists.
- It does not resolve grants signed just before departure, and it does not resolve office vacancy. Both stay open.
- It does not forbid a status protocol from reporting a conservative combined answer. S27 permits a responder to return revoked where the issuer has no record of ever having issued the artifact, which deliberately merges findings one and three in the safe direction. The requirement is on what a verifier may conclude from such an answer, not on the answer's shape.

**Forced by.** LC-H-004, LC-C-006, LC-B-008, LC-B-012, LC-B-013, LC-A-016, LC-A-012, LC-A-023, LC-B-007, LC-A-022, LC-B-004, LC-B-016, LC-B-017, LC-C-005, LC-C-007, LC-C-009, LC-D-029, LC-D-034, LC-H-005.

**Strongest counterexample.** LC-C-006 pushes toward collapse. If the finding is that issuance was never valid, then current validity looks moot, and if the two findings always move together the separation is decoration. The second and sharper counterexample is S27, where a deployed protocol collapses findings one and three on purpose.

**How the statement survives.** They do not move together in either direction. LC-B-016 has issuance validity untouched and continued scope narrowed by an external filing, and S18 is the sourced form of a restriction whose release condition sits with a court rather than with the restricted party. LC-A-016 and S7 have issuance valid and exercisability pending. LC-A-022 has issuance valid and continued validity ending on an external event with no revocation. LC-C-006 makes the separation necessary rather than moot, because the verifier needs a status for void from issuance that is not a revocation event, and that requires the issuance question to be independently answerable after the fact. The S27 case is handled by the non-claim, since the protocol is choosing a conservative report rather than telling the verifier that the two findings are one.

**Tested by.** Nothing. No built fixture tests issuer standing at issuance. This is the least tested candidate relative to how well the corpus forces it.

**Status.** proposed, rewritten twice. The wave 2 rewrite made issuance validity time-varying, which was worse than the defect it fixed. The three-finding form keeps ratification representable as finding two without making finding one move.

---

### CAND-04. Activation is established, not yet effective, or not established

**Statement.** Authority subject to an activation condition is not exercisable until that condition is established by evidence the authority model accepts, from a source the model accepts for that condition. Where the verifier establishes the condition has not yet occurred, the artifact verdict is not yet effective. Where the verifier cannot establish whether the condition has occurred, the verdict is not established. Neither is invalid and neither is valid. A condition that first occurred after an action does not make that action exercisable, and at a boundary where the accepting evidence was not available the action was not established as exercisable at that boundary, whatever a later record shows.

**What it does not claim.**

- It does not claim the grant is invalid, absent or unissued. It is validly issued and waiting.
- It does not claim only an affirmative attestation can establish a condition. A date can establish itself, subject to which clock governs. An absence can be the condition where the model says so.
- It does not claim any evidence will do. S4 is the sourced form of the attestor-role point, where the principal "may authorize one or more persons to determine in a writing or other record that the event or contingency has occurred". A source accepted for an outage is not thereby accepted for incapacity.
- It does not claim a model must name a single attestor. S5 shows one model supplying a fallback determiner where "the person authorized is unable or unwilling to make the determination".
- It does not claim a condition, once established, stays established. Whether ceasing to hold de-activates is a model question.
- It does not settle which clock governs. LC-G-007 makes the check the checking party's own clock at check time, and LC-G-008 and LC-G-009 show a single time source and a declared smear window both producing readings a verifier cannot simply trust. That family is open.
- It does not claim a later attestation is useless. It may establish, for a reconstruction after the fact, that a condition obtained before the action. What it cannot do is change what was established at the boundary. See section 8.4.

**Forced by.** LC-A-003, LC-A-016, LC-C-014, LC-H-012, LC-C-008, LC-C-015, LC-C-017, LC-C-020, LC-C-002, LC-E-034, LC-A-001, LC-A-008, LC-A-022, LC-G-007.

**Strongest counterexample.** LC-C-015 and LC-C-008 together. Both are conditions whose trigger is an absence. If "established by evidence" required a positive attestation, a lost-link fallback never activates and a continuity plan fails closed at exactly the wrong moment. LC-C-020 is the third form, where no holder is named in advance at all and the condition is an eligibility rule evaluated live. A fourth, from the attack, is S4 read with S5: a model built around a determination recorded after the fact would be unusable under a rule that rejected after-dated evidence outright.

**How the statement survives.** "Evidence the authority model accepts, from a source the model accepts for that condition" admits negative and derived evidence. An attested failure to reach the principal within a declared window is evidence. An eligibility evaluation by a declared evaluator is evidence. The phrase "for that condition" does the real work and S4 is the model form of that restriction. The after-dated evidence problem is handled by separating the two questions the wave 2 draft ran together: what was established at the boundary, and what a later reconstruction can show. S4 and S5 live entirely in the second, and LC-G-006 is the corpus rule that keeps them apart.

**Tested by.** `activation-not-established`. AX-02 to AX-07 cover the not-established side under distinct reason codes, AX-01, AX-08 and AX-09 the exercisable side, AX-11 two reasons under one verdict, AX-12 records that a grant whose activation date has not been reached returns invalid with `NOT_YET_VALID` in both reference SDKs. **Not covered:** a not-yet-effective verdict as a distinct outcome, and absence-triggered activation.

**Status.** proposed, rewritten.

---

### CAND-05. Suspension and restriction causes compose

**Statement.** An authority artifact can be subject to more than one concurrent suspension or restriction cause, and a verifier must represent them as a set rather than as a single state. Releasing one cause does not release another. A release is effective against a cause only from a source with lifecycle standing over that cause, which is not necessarily the source that imposed it. Where any cause remains unreleased the verdict remains suspended or restricted and records which causes remain.

**What it does not claim.**

- It does not claim external sourcing for composition. Composition is forced by the corpus and is externally unsourced in this document. The wave 2 draft called FINRA Rule 8311(a) "the sourced version of composed causes". I could not fetch finra.org in this session, so v2 carries no FINRA quote and makes no claim about that rule in either direction.
- It does not claim a single release record cannot clear several causes. One record from a party with standing over each cause can release all of them.
- It does not claim standing equals authorship. S18 has a debtor in possession's powers conditioned on "such limitations or conditions as the court prescribes", and a body that may prescribe may also lift. An implementer who reads "standing over that cause" as "the source that imposed it" gets the superior-authority case wrong.
- It does not claim suspension and restriction are the same thing. L8 already separates them and a restricted state does not have to pause descendants.
- It does not claim release returns authority to its pre-suspension shape. Something else may have ended in the meantime, and `OPEN-QUESTIONS.md` names this as unsettled.
- It does not define a precedence order among causes. Open.

**Forced by.** LC-B-024, LC-B-010, LC-B-011, LC-B-019, LC-B-018, LC-B-031, LC-B-016, LC-B-026, LC-B-030, LC-C-022, LC-C-029, LC-A-010, LC-E-034.

**Strongest counterexample.** LC-B-019. Delisting removes a block and execution resumes, with no release of anything else and no new grant. If release restores authority there, the statement looks like an edge case rather than a rule. The stronger form is a single order vacating several restrictions at once, which looks exactly like one release clearing multiple causes.

**How the statement survives.** LC-B-019 has one cause, so composition is trivially satisfied and release of the only cause restores execution. That is the statement working. The multi-vacating order is one record with standing over each cause, which the non-claim covers. The standing clause blocks the failure LC-B-011 names directly, which is an internal process clearing an externally imposed restriction, and the non-authorship clause blocks the opposite error of refusing a superior authority's release.

**Tested by.** `suspension-cause-composition` CR-01 to CR-16. Three concurrent causes on one grant from three sources, with a standing registry: CR-03 and CR-04 keep the verdict suspended or restricted as causes are released one at a time, CR-06 is the negative control where a genuine correctly signed release from a party without standing over that cause does nothing, CR-07 is release by a superior source that did not impose the cause, CR-08 and CR-09 are one record against several causes with full and with partial standing. **Not covered:** any precedence order among causes, which stays open.

**Status.** proposed, rewritten.

---

### CAND-06. Collective authority must satisfy its declared composition

**Statement.** Where the authority model requires an operation to be authorized collectively, the operation is authorized only when the declared composition rule is satisfied at the boundary the operation requires. A composition rule states which members are required, the threshold, the direction, because what it takes to authorize an action is not necessarily what it takes to stop or narrow it, and any restriction carried by an individual member. A single valid chain does not satisfy a multi-member rule however broad that chain is. The authority the collective act exercises is the authority the rule attaches to, and satisfying the rule does not add to any contributing member's own scope, which remains what that member's chain independently permits. Where collective authority is required but the rule's membership, threshold or direction is not declared, composition is not established and a verifier must not supply one, though a default declared by the authority model is a declared rule and not an inference.

**What it does not claim.**

- It does not claim composition is a union of scopes. L5 stands. LC-C-011 exists to keep the two apart.
- It does not claim a joint act cannot do what neither party may do alone. It can, and often that is the point. What the rule attaches to is a third authority, not the sum of two. S19 is the sourced form, putting operational control in the certificate holder, while S20 makes release "jointly" the pilot in command's and the dispatcher's. Neither individual's own scope grows.
- It does not claim composition rules are symmetric. S20 and S21 are a sourced asymmetry in one model, where release is joint but cancelling turns on "his opinion or the opinion of the pilot in command". LC-C-016 is the corpus form.
- It does not claim there is a universal default for undeclared composition. S6 shows one enacted model declaring its own default, which is a default supplied by the model rather than inferred by a verifier.
- It does not claim every member must be reachable. LC-A-019 has majority action with a vacancy left unfilled.
- It does not claim concurrences may be aggregated across time without a freshness rule. LC-C-011 requires them present and fresh at the same moment, and that rule has to be declared.
- It does not cover a standing superior override. A cause-free override held by a party whose authority was never delegated away is lifecycle standing, not composition. See CAND-09 and section 8.3.

**Forced by.** LC-C-011, LC-C-016, LC-C-018, LC-C-012, LC-C-029, LC-A-019, LC-A-033, LC-H-001, LC-H-002, LC-H-004, LC-B-026.

**Strongest counterexample.** S20 against the no-widening clause as the wave 2 draft wrote it. Dispatch release is joint and neither party releases a flight alone, so the joint act does something neither may do alone, which the draft's wording forbade. The second counterexample is A-017 under LC-A-019: if composition is genuinely undeclared and a verifier must not infer a default, a large number of real instruments become unusable, which looks like a false denial.

**How the statement survives.** The scope clause is now about contributing members rather than about the collective authority, and S19 is why that reading is the correct one rather than a rescue: operational control sits with the certificate holder, and the two individuals are conditions on its exercise. Neither individual's scope grows, and the flight-release authority was never either individual's to begin with. The undeclared case is handled by distinguishing a default declared by the model from a default invented by a verifier, with S6 as a model declaring joint action as its own default. What the final limb forbids is a verifier picking joint or several on its own when neither the instrument nor the model says, which is A-017's finding stated as a rule rather than as an ambiguity.

**Tested by.** `chain-selection-no-union`, the negative half only. Do not report it as coverage of the obligation half.

**Status.** proposed, rewritten.

---

### CAND-07. A stable name does not establish stable semantics

**Statement.** A stable identifier, name or identity does not establish that what it refers to is unchanged. Where the authority model declares that a class of referent change is capability-relevant, continuity of the referent across such a change must be established by something the grant, the model or an attesting party pins. Where nothing pins it, the verdict records that referent continuity was not established rather than admitting silently. Where something pins it and the pin does not match, the action is denied with a mismatch reason rather than reported as not established. A verifier must not treat an unchanged name as evidence of an unchanged controller, an unchanged implementation or an unchanged schema.

**What it does not claim.**

- It does not claim every referent must be pinned. Pinning has real cost and many grants do not need it. The claim is that where nothing pins it, continuity is not established and the verdict says so.
- It does not locate the obligation in the grant alone. A provider attestation, a registry that records controller changes, a model rule that an identifier is immutable, or a signed capability manifest resolved at verification time all establish continuity. Grants are written before the drift happens and are the artifact least able to carry the whole burden.
- It does not claim a verifier can always detect the change. Often it cannot.
- It does not claim a capability change invalidates the grant. The grant is intact. What is not established is that the action now attempted is within it.
- It does not cover narrowing. A referent that loses a capability has not widened or redirected what the authority permits, and denying there is a false denial with no risk behind it.
- It does not claim re-consent is the only remedy. S32 shows one platform choosing it, where adding a warning-triggering permission means "the extension will be disabled until the user accepts the new permission". That is one model's answer.
- It does not resolve semantic drift generally. `OPEN-QUESTIONS.md` keeps that open.

**Forced by.** LC-E-033, LC-E-001, LC-E-002, LC-E-027, LC-E-004, LC-E-025, LC-E-031, LC-E-023, LC-D-009, LC-D-029, LC-D-034, LC-D-033, LC-I-001, LC-I-002, LC-I-003.

**Strongest counterexample.** A referent change that narrows. The grant pins nothing, the tool drops a capability, and a rule requiring continuity to be established denies an action that is now strictly safer than when the grant was written. That is a false denial produced by the invariant itself. A second is LC-E-001, where an alias with a documented default is doing exactly what its documentation says, so calling that a semantics break punishes a provider for behaving as specified. A third is the predicate itself: "could widen or redirect" is not decidable by a verifier without a declared basis.

**How the statement survives.** Scoping to changes the model declares capability-relevant removes the narrowing false denial and makes the predicate decidable, using the same move CAND-06 and BROAD-L7 make for defaults. LC-E-001 survives because a documented pointer is precisely a case where the referent can change to something with different capability, so the finding is not that the provider misbehaved but that the grant pinned a pointer rather than a capability set, which is what the case's own text says. The identity limb exists because LC-I-001, LC-I-003, LC-E-025 and LC-E-031 are about the controller or holder changing behind a stable identity rather than about capability, and the group I cases that make that limb concrete did not exist when the wave 2 draft was written.

**Tested by.** `capability-binding-drift`, the pinned and unpinned cases, stale registry and unrecognised attestor. **Not covered:** controller change and narrowing direction. CBD-02 and CBD-03 label an established mismatch as not established, which this document's own section on the two uses of not established says should be a denial with a mismatch reason.

**Status.** proposed, rewritten.

---

### CAND-08. No silent restoration from rollback or stale state

**Statement.** Rollback, restore, replica lag or any other regression of stored state must not restore superseded authority. For each authority subject, an enforcement point must not act on a state older than the newest state it has established for that subject under the model's own version or epoch scheme, and where that value regresses the operation is refused rather than resolved by recency of write. Where the enforcement point cannot hold that state itself, the monotonic value must be carried to and checked by the party that performs the effect. Restoring superseded authority is permitted only as an explicit, attributable record from a source with lifecycle standing, which is a new record and not a reversal of the old one.

**What it does not claim.**

- It does not claim a correction is forbidden. LC-F-009 is the case where a publisher un-says its own false revocation, which is a different operation from reauthorization and needs its own evidence trail. The word doing the work is "silently".
- It does not claim a verifier that has never seen the newer state is at fault. It cannot be. The obligation is monotonicity against what it has established.
- It does not claim authority state is one totally ordered thing. Monotonicity is per authority subject, under the model's own scheme. A verifier legitimately holds a current epoch for one artifact and an older snapshot for another, and a rule phrased globally either forbids ordinary caching or is unimplementable.
- It does not claim an epoch scheme is required. It claims that where a system has one, a regression is a refusal rather than an input to a merge.
- It does not claim last-writer-wins storage is misconfigured. S31 is documented, correct behaviour for that store and wrong for a revocation. LC-F-022 is the corpus form.
- It does not resolve authority rollback. `OPEN-QUESTIONS.md` keeps open both the mechanism and what a verifier should return after a restore.

**Forced by.** LC-F-017, LC-F-026, LC-F-016, LC-F-018, LC-F-022, LC-F-024, LC-F-006, LC-F-009, LC-E-023, LC-D-003, LC-I-004.

**Strongest counterexample.** LC-F-009. An authorized correction record withdraws a revocation that should never have been published, and the stored state legitimately returns to something resembling the pre-revocation position. The harder one is a verifier holding an older epoch with no knowledge that a newer one exists, which cannot detect regression at all, so a rule phrased against global truth is unimplementable. The third, from S29 and S30, is placement: the fencing technique puts the monotonic counter at the resource because a requesting party that pauses or is delayed cannot detect its own staleness.

**How the statement survives.** The correction case is handled by the explicit-record limb, and the resulting position is not "the revocation never happened" but "the revocation was withdrawn by record X", which is CAND-02 applied to the same events. The unknowing verifier is handled by scoping monotonicity to what the verifier has established, which is weaker than a global rule and is the honest strength available. The placement objection is handled by the carry-and-check clause, and it is worth recording that `authority-epoch-rollback` already implements the resource-side half in AER-07 to AER-10, where writes are accepted or refused at the publishing point by fencing token. The rewrite aligns the text with what the fixture already does.

**Tested by.** `authority-epoch-rollback` AER-01 to AER-10, on both the observation side and the fencing side. **Not covered:** per-subject scoping and the policy-pointer shape.

**Status.** proposed, rewritten.

---

### CAND-09. Chain validity is not permission to execute

**Statement.** Whether an authority chain is valid and whether the action it authorizes is permitted by rules outside the grant chain are separate findings. An external restriction can block execution with no event anywhere in the chain, and removing that restriction restores execution on the unchanged chain without creating new authority. A verifier that returns one finding must not be read as having answered the other. Where the principal itself changes rather than being restricted, that is not this rule.

**What it does not claim.**

- It does not ask a verifier to decide whether an action is lawful. The finding is about rules outside the grant chain as the model defines them, not about legal characterisation.
- It does not claim block and release are always symmetric. Where what changed is who owns the resource, no release restores anything.
- It does not claim a restriction must pause descendants. L8 already separates restricted from suspended, and LC-B-010 is the case where authority continues in reduced form with no descendant pausing.
- It does not cover a standing superior override held by a party who never delegated that authority away. That is lifecycle standing and it sits here rather than in composition, but the corpus case for it rests on a secondary source and is flagged below.

**Forced by.** LC-B-018, LC-B-019, LC-B-010, LC-B-011, LC-B-016, LC-B-026, LC-B-030, LC-B-031, LC-A-010, LC-B-027.

**Strongest counterexample.** LC-B-027. Forfeiture is not a restriction whose release restores execution. Ownership moved, and no delisting brings it back. If CAND-09 promised symmetry between block and release, this case breaks it.

**Tested by.** Nothing.

**Status.** proposed.

---

### CAND-10. Holding a scope does not establish authority to confer it

**Statement.** An agent's holding a scope does not establish that it may confer that scope on another party, including a child it creates or a copy of itself. Authority to delegate is itself a declared authority, and where the model does not declare it, conferral is not established.

**What it does not claim.**

- It does not claim conferral always needs a fresh act of the principal. S35 shows a model declaring it structurally, where "Service-linked roles appear in your AWS account and are owned by the service", and the same page notes an administrator can view but not edit those permissions, which makes the declaration the model's rather than the holder's. S8 shows another, where a principal may grant the authority to designate successors to an agent or other person.
- It does not claim monotonic narrowing covers this. Narrowing constrains what a child may receive. It says nothing about who may create one.
- It does not claim structural limits are the same question. Depth exhaustion and validity-period nesting are separate constraints on the shape of a chain.
- It does not decide what happens to children already issued without declared conferral authority. That is a cleanup question, not a verdict rule.

**Forced by.** LC-E-006, LC-E-025, LC-E-004, LC-E-031, LC-E-023, LC-H-008, LC-H-007.

**Strongest counterexample.** E-007 under LC-E-006, with S35. There are real models where conferral needs no separate grant, because a platform default creates the child without an explicit pass. S8 is a second, where a principal may grant the power to designate successors by name, office or function.

**Tested by.** `lifecycle-conferral-without-authority` CWA-01 to CWA-10. Three roots differ in exactly one value, the declared conferral right, so nothing else can explain a reject: CWA-02 is a parent with no conferral right conferring exactly what it holds, CWA-03 the negative control a naive implementation passes wrongly, CWA-05 a child keeping the parent's full remaining conferral right, CWA-08 self-conferral. Both reference SDKs returned the same state, failure code and failure index on all ten. **Not covered:** an undeclared conferral right as its own verdict, since an absent facet is a schema failure in both SDKs and never not established.

**Status.** proposed. The only candidate in this set that survived the hostile pass unchanged.

---

### CAND-11. A valid grant can be unexecutable

**Statement.** An artifact can be valid, unexpired, unexhausted, unsuspended and unrestricted while the target, executor or capability it names no longer exists. The artifact verdict stays valid. The execution attempt fails and the record carries the unresolvable referent. A verifier must not report this as invalid, expired, revoked or suspended.

**What it does not claim.**

- It does not propose a seventh verdict. The [verification model](AUTHORITY-LIFECYCLE.md#verification-model) settles unexecutable as an execution outcome rather than a verdict, and whether the enumeration ever gains a value for it is a separate decision for the model owner.
- It does not prescribe a remedy. Which party re-points the grant, and whether they may, is operational guidance around the invariant and not part of it.
- It does not claim the authority is unaffected in the world. A grant naming a permanently gone executor may well be worth revoking. It claims only that nothing in the grant's own lifecycle has changed, so a lifecycle verdict must not say otherwise.
- It does not cover a referent that changed rather than vanished. That is CAND-07.

**Forced by.** LC-E-002, LC-E-014, LC-E-020, LC-E-001, LC-C-025.

**Strongest counterexample.** A permanently unexecutable grant is functionally dead, so reporting it distinctly could be called a distinction without a difference. The action fails either way.

**Tested by.** Nothing.

**Status.** proposed, rewritten.

---

### CAND-12. Ending authority bounds future effects, it does not undo past ones

**Statement.** Ending or narrowing authority takes effect at the next authorization boundary the operation requires. Where an operation has a terminal boundary after which no further authorization decision occurs, a change arriving after that boundary does not reach the completed effect and is recorded as a later event rather than as a denial. Ending authority does not undo effects already completed, does not retract information already obtained under the authority, and does not by itself end sessions or derived credentials already issued. Where the model provides a compensating or reversing action, that action is separate authority with its own boundary and its own record.

**What it does not claim.**

- It is not an argument against terminating sessions on revocation. Session termination is a control a model may and often should require. The claim is only that it does not follow automatically from the grant ending, so a model that wants it must say so. An implementer who reads this as advice to leave sessions running has drawn the opposite of the intended lesson.
- It does not claim a post-boundary reversal is impossible. S23 allows cancellation after acceptance where "the receiving bank agrees or a funds-transfer system rule allows" it, which is a separate authorized action rather than an automatic consequence.
- It does not claim exhaustion is always a separate step. LC-I-013 and LC-I-014 are models where using the grant and exhausting it are the same recorded event.
- It does not resolve work in flight. Whether the operation resumes, restarts, compensates or stops is open.

**Forced by.** LC-E-021, LC-E-013, LC-E-019, LC-D-025, LC-B-029, LC-B-028, LC-A-023, LC-A-027, LC-I-013, LC-I-014.

**Strongest counterexample.** S23 itself. UCC 4A-211(c) allows cancellation after acceptance in defined circumstances, which looks like undoing a completed effect. S24 sharpens the neighbourhood, since an unaccepted order is "canceled by operation of law" at a fixed deadline with no boundary decision at all.

**Tested by.** Nothing.

**Status.** proposed, rewritten to absorb the terminal-boundary limb from BROAD-L6.

---

### CAND-13. Replacement authority may be pre-committed

**Statement.** Replacement authority does not have to be issued fresh after the contingency. Where an instrument or a rule of the authority model pre-commits it, the replacement holder's authority derives from that source at the scope that source declared, becoming exercisable when the declared contingency is established. If the pre-committing instrument is itself revoked or otherwise invalid, the pre-committed replacement is invalid with it, as L1 requires. Pre-committed succession is not a reversal of a revocation. The successor receives the scope the pre-committing source declares for the successor, and does not thereby acquire the predecessor's other descendants.

**What it does not claim.**

- It does not claim the successor's scope is narrower than the predecessor's own grant. S9 has one enacted model where, unless the instrument provides otherwise, a successor agent "has the same authority as that granted to the original agent". Same authority as granted to the original is not the same thing as the original's sub-delegations, so L4 survives and the distinction has to be stated or an implementer will wrongly narrow the successor's own scope.
- It does not claim pre-commitment requires a written instrument. LC-C-008 and LC-C-020 are pre-commitment by rule rather than by instrument, and a statement limited to instruments would exclude them.
- It does not claim L3 is wrong. It narrows L3's "a new grant" rather than contradicting it.
- It does not resolve office vacancy. Where nobody currently holds the office and nobody is empowered to exercise, reaffirm or revoke, this candidate says nothing.

**Forced by.** LC-A-016, LC-C-017, LC-C-020, LC-C-008, LC-C-015, LC-C-025, LC-C-002, LC-A-019, LC-B-012, LC-B-008, LC-H-005.

**Strongest counterexample.** L1 as published, which the wave 2 draft missed entirely while carefully handling L3. If the replacement's authority derives from an instrument, and the statement locates the source at issuance time, then a pre-committed successor named in an instrument that has since been revoked would still have authority. That is a direct collision with the most settled invariant in the document, specified and tested.

**Tested by.** `activation-not-established`, the activation half only. **Not covered:** the L1 collision, a pre-committed successor under a revoked instrument.

**Status.** proposed, rewritten.

---

### CAND-16. A recorded lifecycle change is effective when the model's effectiveness rule is satisfied

**Statement.** A recorded lifecycle change is effective at an authorization boundary only when the authority model's own effectiveness rule for that change type is satisfied at that boundary. Where the model declares no effectiveness rule for a change type, the change is effective from the moment it is recorded. A verifier that treats a recorded change as effective records which rule it applied.

**What it does not claim.**

- It is not a freshness rule. BROAD-L7 asks how old the verifier's answer is. This asks whether the change had taken effect at all.
- It is not a notice rule about third parties. That is ANX-03 and it stays in the annex.
- It does not claim effectiveness rules are uniform within a family. S13 and S14 are two events in one family under different rules in the same model, one with no notice condition and one effective only on the agent's notice.
- It does not claim a change with an unsatisfied effectiveness rule is void. It is recorded and not yet effective at that boundary, and it may be effective at the next one.
- It does not claim the verifier can always tell. Where it cannot establish whether the rule is satisfied, the state is not established under BROAD-L7.

**Forced by.** LC-A-001, LC-B-009, LC-B-029, LC-H-010, LC-H-011, LC-H-009, LC-F-018, LC-C-006.

**Strongest counterexample.** The default. Saying that a change with no declared effectiveness rule is effective on record is a choice, and a deployment could reasonably prefer effective on observation, which is what a lagging enforcement point actually does. LC-F-018 is exactly that deployment, where actions allowed by a lagging gateway within a declared bound are a declared, bounded risk.

**Tested by.** Nothing.

**Status.** proposed, new in v2. Adopted from the attack's F5.

---

## Proposed broadening of existing invariants

These two do not add a new statement. Each widens an invariant `AUTHORITY-LIFECYCLE.md` already publishes, and the published narrow form keeps the status it has there.

### BROAD-L6. L6 extends to every authorization boundary the operation requires

**Current L6.** An earlier approval is not current authority. Revocation state must be rechecked at execution time, not only at approval time.

**Broadened statement.** An earlier approval or authorization decision does not establish current authority at any later authorization boundary the operation requires. Each boundary is evaluated against lifecycle state the verifier can establish as current and effective at that boundary, including boundaries added from outside the grant chain and boundaries within a long-running or multi-step operation. Rechecking current lifecycle state is not re-evaluating the operation under a newer policy version, and which policy version governs is a separately declared rule.

**What it does not claim.**

- It does not claim the operation must be re-evaluated against the current policy version. LC-E-008 is the counterexample, where an in-flight instance's remaining steps must resolve against a pinned version and "jumping straight to current rules mid-replay is not a safety improvement". LC-I-006 is the same point from the grant side: a tightened policy applies to new grants and new evaluations without the tightening being read as an implicit revocation of grants valid under the policy that governed them at issuance.
- It does not claim a retry of an already decided effect is a new boundary. LC-E-010 and LC-E-011, both boundary cases, are the idempotency shapes.
- It does not claim the start of a shutdown is a boundary. LC-E-019 is the counterexample, where authority stays valid and checkable through a declared graceful-shutdown window and the final in-flight call should succeed.
- It does not claim every technical step is a boundary. Identifying the boundaries an operation requires is part of the operation's own design.
- It does not claim a recorded change is automatically effective at the next boundary. That is CAND-16, and the word "effective" in the statement is the slot it fills.
- It does not own the terminal-boundary rule. That moved to CAND-12.
- It does not resolve work in flight. What happens to the operation itself after a mid-flight change stays open.

**Forced by.** LC-B-028, LC-B-029, LC-B-026, LC-C-011, LC-C-018, LC-C-025, LC-E-013, LC-E-034, LC-E-018, LC-E-021, LC-E-008, LC-I-006, LC-D-025.

**Strongest counterexample.** LC-E-008 with LC-E-019. Both are cases where more rechecking is the wrong answer. Read at its most aggressive the broadening breaks a durable workflow when policy is redeployed mid-run, and costs a pod with a legitimate grace period its last authorized call.

**How the statement survives.** By separating current lifecycle state from policy version, and by leaving the boundary set to the operation rather than asserting that every technical step is one. The broadening says the lifecycle question must be asked again at each boundary. It does not say the policy question must be answered afresh, and LC-I-006 now supplies the grant-side half of that separation, which the wave 2 draft argued from LC-E-008 alone. The one genuine circularity objection, that "every boundary is its own decision" is close to a definition, is handled by the statement carrying three testable claims rather than one: an earlier decision does not satisfy a later boundary, lifecycle recheck is not policy re-evaluation, and a boundary imposed from outside the grant chain is still a boundary.

**Tested by.** Nothing tests the broadening. The suite's `cached-authorization-revocation` tests the narrower published L6 and is a related fixture, not a source. **Not covered:** the policy-version separation, the externally added boundary, and the in-flight-invalidation shape.

**Status.** proposed as a broadening of a partly specified invariant. L6's revocation recheck stays specified. Everything added here is proposed.

---

### BROAD-L7. L7 extends to any current lifecycle state claim

**Current L7.** Unknown revocation state is not active. An unavailable or stale revocation answer is indeterminate, an enforcement point may deny on indeterminate, and the denial should say why.

**Broadened statement.** Any claim about the current lifecycle state of an authority artifact, meaning its revocation, suspension, restriction, expiry or exhaustion state, is established only from a source the authority model accepts for that state, within a freshness bound the model declares, and only over the set the claim itself states it covers. Where source or freshness is missing, the state is not established. A verifier must not read a state claim as covering more than the claim states. Not established is not the negation of the claim, and a verifier may deny on it as long as the denial records what was missing. Where the model declares a default for absence, the default applies and the verifier records that it was used.

The same source, freshness and coverage discipline applies to every other finding the candidates in this document define, including issuer standing, activation, composition and referent continuity. Each of those candidates states which sources its own finding admits, because the admissible sources differ and a source accepted for one is not thereby accepted for another.

**What it does not claim.**

- It does not claim not established means inactive, or active, or anything about the world. S26 is the sourced form of that distinction in one protocol.
- It does not claim liveness is required. A declared offline posture with a snapshot inside its declared bound satisfies the rule, which is LC-F-008's point that offline checking needs its own evidence category rather than being a degraded live check.
- It does not claim absence is always indeterminate. LC-C-008 is the counterexample and the reason the default clause exists.
- It does not solve completeness. The coverage limb requires a claim to state what it covers and forbids a verifier reading it as covering more. It does not require anyone to establish that a set was complete, which L12 keeps open and `OPEN-QUESTIONS.md` still names in three unsettled pieces.
- It does not declare a freshness number. Bounds are model declared. S25 is why that matters, since RFC 5280 requires nextUpdate in conforming CRLs and leaves client behaviour unspecified where it is omitted.
- It does not absorb CAND-03, CAND-04, CAND-06 or CAND-07. The enumeration is deliberately limited to lifecycle states in the sense L7 uses, and the general clause defers the admissible-source question to each candidate.

**Forced by.** LC-F-006, LC-F-008, LC-F-013, LC-F-017, LC-F-018, LC-F-027, LC-F-033, LC-F-035, LC-B-002, LC-C-005, LC-C-008, LC-C-009, LC-C-015, LC-D-003, LC-D-014, LC-D-011, LC-A-003, LC-G-008, LC-G-009.

**Strongest counterexample.** LC-C-008 and LC-F-008 together. One says absence resolves to a named fallback rather than to indeterminate. The other says a deliberately offline verifier with a snapshot that is stale by live standards may legitimately admit. Between them they cover a large fraction of real deployments. The second counterexample is coverage: requiring a claim to be established over the coverage it requires, while admitting that nobody knows how to establish completeness, is a requirement to fail.

**How the statement survives.** Freshness is measured against a declared bound rather than against liveness, which admits LC-F-008. Absence is resolved by the model's declared default where there is one, which admits LC-C-008. Both carve-outs are conditioned on the model having declared something, and in both the verifier records what it used. The coverage limb is restated as a reading rule rather than an establishment duty: a claim states what it covers, and a verifier must not read it as covering more. That is decidable today and does not depend on solving L12.

**Tested by.** `conflicting-status-sources`. CSS-04 and CSS-05 cover conflict, CSS-06 to CSS-08 a stale, silent or absent source, CSS-09 to CSS-11 the declared offline posture, CSS-13 and CSS-14 the bound exactly at and one second past, CSS-12 later-conflict-does-not-rewrite. **Not covered:** the coverage limb in its restated form and the declared-default-on-absence path.

**Status.** proposed as a broadening. L7's unavailable-or-stale revocation case stays specified. Everything added here is proposed.

---

<a name="evidence-and-receipt-shape-annex"></a>

## Evidence and receipt annex

These are requirements on what a verdict record carries rather than statements about when authority exists.

### ANX-01. A verdict records its event-class coverage

**Statement.** Where the authority model publishes a class list of authority-changing events, a verdict records, for each class on that list, whether it was checked and against which source. Where the model publishes no such list, the verdict records that no event-class coverage was claimed.

**Forced by.** LC-B-008, LC-B-025, LC-D-001, LC-B-009.

**Tested by.** Nothing.

**Status.** proposed.

---

### ANX-02. A verifier can present an earlier record and a later finding together

**Statement.** A verifier presenting the current authority position must be able to present both the earlier record and the later finding that references it, and their relation.

**Forced by.** LC-B-007, LC-G-006, LC-C-022, LC-I-005.

**Tested by.** `conflicting-status-sources` CSS-12 touches it.

**Status.** proposed.

---

### ANX-03. Chain validity and a relying party's knowledge are separate findings

**Statement.** Whether a chain is currently valid and whether a particular party had notice of a change are separate findings. A verdict record carries a notice finding with its own timestamp, or records that it has none.

**Forced by.** LC-A-027, LC-A-028, LC-A-001, LC-F-027, LC-F-018.

**Tested by.** Nothing.

**Status.** proposed.

---

### ANX-04. A declared scope is only as effective as the boundary that enforces it

**Statement.** A verifier that cannot establish that the enforcement boundary implements the grant's declared scope must not report the narrower scope as established. Documented scope and reachable scope are separate facts needing separate evidence.

**Forced by.** LC-D-009, LC-D-027 (boundary case), LC-D-023 (boundary case), LC-D-019 (boundary case).

**Tested by.** Nothing.

**Status.** proposed.

---

## What this document does not close

- **Office vacancy and succession.** CAND-13 and CAND-04 describe pre-commitment and activation. Neither says what happens when nobody currently holds the office and nobody is empowered to exercise, reaffirm or revoke. Open.
- **Grants signed just before departure.** CAND-03 separates the findings and deliberately does not answer this. Open.
- **Teardown completeness.** BROAD-L7's coverage limb is a reading rule rather than an establishment duty, which makes the limb testable and leaves L12 exactly as open as it was.
- **Work in flight.** BROAD-L6 says the boundary decision is fresh, CAND-12 says completed effects stand, CAND-16 says when a change takes effect. None of them says whether the operation resumes, restarts, compensates or stops.
- **Release from suspension.** CAND-05 says causes compose and release needs standing. It does not define a precedence order among causes.
- **Notice and relying parties.** ANX-03 proposes only the separation of two findings and nothing about entitlement.
- **Semantic drift generally.** CAND-07 handles the pinned, unpinned and controller cases against a model-declared basis. Whether a change in meaning should invalidate an earlier grant, and how a verifier would detect it unaided, stays open.
- **Which clock governs.** LC-G-007, LC-G-008 and LC-G-009 exist and no candidate resolves the family. CAND-04 defers it.
- **Whether the verdict enumeration should gain a value for unexecutable.** It does not today. That is a decision for the model owner to take openly, not one an invariant should smuggle in.

<a name="tested-by-at-a-glance"></a>

## Fixture coverage

| Candidate | Status | Tested by |
|---|---|---|
| CAND-01. An external event is authority-changing only when established | proposed | `lifecycle-purpose-exhaustion` PXE-08 and PXE-09 (held back, unmerged candidate branch), an event record that is unauthenticated, or authenticated by a party without standing, leaving the effect not established |
| CAND-02. Later evidence does not rewrite earlier evidence | proposed | [`authority-epoch-rollback`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/authority-epoch-rollback/README.md) AER-11 and AER-12, a signed withdrawal accepted as a new record with the original still held and still verifying |
| CAND-03. Issuance validity, later attached effects and current validity are three separate findings | proposed | nothing |
| CAND-04. Activation is established, not yet effective, or not established | proposed | [`activation-not-established`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/activation-not-established/README.md) |
| CAND-05. Suspension and restriction causes compose | proposed | [`suspension-cause-composition`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/suspension-cause-composition/README.md) CR-01 to CR-16 |
| CAND-06. Collective authority must satisfy its declared composition | proposed | [`chain-selection-no-union`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/chain-selection-no-union/README.md), the negative half only |
| CAND-07. A stable name does not establish stable semantics | proposed | [`capability-binding-drift`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/capability-binding-drift/README.md), the pinned and unpinned cases, stale registry and unrecognised attestor |
| CAND-08. No silent restoration from rollback or stale state | proposed | [`authority-epoch-rollback`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/authority-epoch-rollback/README.md) AER-01 to AER-10, on both the observation side and the fencing side |
| BROAD-L6. L6 extends to every authorization boundary the operation requires | proposed | nothing |
| BROAD-L7. L7 extends to any current lifecycle state claim | proposed | [`conflicting-status-sources`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/conflicting-status-sources/README.md) |
| CAND-09. Chain validity is not permission to execute | proposed | nothing |
| CAND-10. Holding a scope does not establish authority to confer it | proposed | [`lifecycle-conferral-without-authority`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/lifecycle-conferral-without-authority/README.md) CWA-01 to CWA-10 |
| CAND-11. A valid grant can be unexecutable | proposed | nothing |
| CAND-12. Ending authority bounds future effects, it does not undo past ones | proposed | nothing |
| CAND-13. Replacement authority may be pre-committed | proposed | [`activation-not-established`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/activation-not-established/README.md), the activation half only |
| CAND-16. A recorded lifecycle change is effective when the model's effectiveness rule is satisfied | proposed | nothing |
| ANX-01. A verdict records its event-class coverage | proposed | nothing |
| ANX-02. A verifier can present an earlier record and a later finding together | proposed | [`conflicting-status-sources`](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/a3f60116726ca81edf6021d51206818746d52cce/fixtures/conflicting-status-sources/README.md) CSS-12 touches it |
| ANX-03. Chain validity and a relying party's knowledge are separate findings | proposed | nothing |
| ANX-04. A declared scope is only as effective as the boundary that enforces it | proposed | nothing |

Twenty items, sixteen in the invariant set and four in the annex. Eleven of them have a fixture that bears on some part of the statement, and the rest have nothing. Three of those fixtures, `lifecycle-purpose-exhaustion`, `suspension-cause-composition` and `lifecycle-conferral-without-authority`, did not exist when the candidates were first written.

## Contributing

A counterexample that a statement does not survive is the most useful thing you can send. So is a fixture for anything in the table above whose tested-by entry says nothing.

<a name="sources"></a>

## Source notes

Every source below was fetched on 2026-09-23 by the pass that wrote these candidates, and quoted verbatim at 40 words or fewer. Each is the origin of a case shape or of a counterexample pattern, never a rule that governs agents. S3, S6, S7, S19, S25, S26, S28, S34 and S36 were re-fetched and the quotes re-checked against the live source on 2026-09-23 when this file was assembled.

| Ref | Source | Verbatim quote |
|---|---|---|
| S1 | Delaware General Corporation Law 259(a), [delcode.delaware.gov](https://delcode.delaware.gov/title8/c001/sc09/index.html) | "possessing all the rights, privileges, powers and franchises as well of a public as of a private nature" |
| S2 | 12 U.S.C. 1821(d)(2)(A), [law.cornell.edu](https://www.law.cornell.edu/uscode/text/12/1821) | "The Corporation shall, as conservator or receiver, and by operation of law, succeed to" then "all rights, titles, powers, and privileges of the insured depository institution" |
| S3 | 11 U.S.C. 362(a), [law.cornell.edu](https://www.law.cornell.edu/uscode/text/11/362) | "operates as a stay, applicable to all entities" |
| S4 | N.H. RSA 564-E:109(b), [gc.nh.gov](https://gc.nh.gov/rsa/html/LVI/564-E/564-E-109.htm) | "the principal, in the power of attorney, may authorize one or more persons to determine in a writing or other record that the event or contingency has occurred" |
| S5 | N.H. RSA 564-E:109(c), same page | "the person authorized is unable or unwilling to make the determination" |
| S6 | N.H. RSA 564-E:111(a), [gc.nh.gov](https://gc.nh.gov/rsa/html/LVI/564-E/564-E-111.htm) | "Unless the power of attorney otherwise provides, the coagents must exercise their authority jointly." |
| S7 | N.H. RSA 564-E:111(b) first sentence, same page | "A principal may designate one or more successor agents to act if an agent resigns, dies, becomes incapacitated, is not qualified to serve, or declines to serve." |
| S8 | N.H. RSA 564-E:111(b) second sentence, same page | "A principal may grant authority to designate one or more successor agents to an agent or other person designated by name, office, or function." |
| S9 | N.H. RSA 564-E:111(b)(1), same page | "has the same authority as that granted to the original agent" |
| S10 | Restatement (Third) of Agency 4.01(1), course reproduction at [staff.washington.edu](https://staff.washington.edu/djdrake/RESt-Agency.doc) | "Ratification is the affirmance of a prior act done by another, whereby the act is given effect as if done by an agent acting with actual authority." |
| S11 | Restatement (Third) of Agency 4.02(1), same reproduction | "Subject to the exceptions stated in subsection (2), ratification retroactively creates the effects of actual authority." |
| S12 | Restatement (Third) of Agency 4.02(2)(c), same reproduction | "to diminish the rights or other interests of persons, not parties to the transaction, that were acquired in the subject matter prior to the ratification." |
| S13 | Restatement (Third) of Agency 3.07(1), same reproduction | "The death of an individual agent terminates the agent's actual authority." |
| S14 | Restatement (Third) of Agency 3.07(2), same reproduction | "The termination is effective only when the agent has notice of the principal's death." |
| S15 | Restatement (Third) of Agency 3.10(1), same reproduction | "A revocation or a renunciation is effective when the other party has notice of it." |
| S16 | Restatement (Third) of Agency 3.11(1), same reproduction | "The termination of actual authority does not by itself end any apparent authority held by an agent." |
| S17 | Restatement (Third) of Agency 3.06(6), same reproduction | "the occurrence of circumstances specified by statute." |
| S18 | 11 U.S.C. 1107(a), [law.cornell.edu](https://www.law.cornell.edu/uscode/text/11/1107) | "Subject to any limitations on a trustee serving in a case under this chapter, and to such limitations or conditions as the court prescribes" |
| S19 | 14 CFR 121.533(a), [law.cornell.edu](https://www.law.cornell.edu/cfr/text/14/121.533) | "Each certificate holder conducting domestic operations is responsible for operational control." |
| S20 | 14 CFR 121.533(b), same page | "The pilot in command and the aircraft dispatcher are jointly responsible for the preflight planning, delay, and dispatch release of a flight" |
| S21 | 14 CFR 121.533(c)(3), same page | "Cancelling or redispatching a flight if, in his opinion or the opinion of the pilot in command, the flight cannot operate or continue to operate safely as planned or released." |
| S22 | UCC 4A-211(b), [law.cornell.edu](https://www.law.cornell.edu/ucc/4A/4A-211) | "if notice of the communication is received at a time and in a manner affording the receiving bank a reasonable opportunity to act on the communication before the bank accepts the payment order" |
| S23 | UCC 4A-211(c), same page | "After a payment order has been accepted, cancellation or amendment of the order is not effective unless the receiving bank agrees or a funds-transfer system rule allows cancellation or amendment without agreement of the bank." |
| S24 | UCC 4A-211(d), same page | "An unaccepted payment order is canceled by operation of law at the close of the fifth funds-transfer business day of the receiving bank after the execution date or payment date of the order." |
| S25 | RFC 5280 section 5.1.2.5, [rfc-editor.org](https://www.rfc-editor.org/rfc/rfc5280.txt) | "The behavior of clients processing CRLs that omit nextUpdate is not specified by this profile." |
| S26 | RFC 6960 section 2.2, [rfc-editor.org](https://www.rfc-editor.org/rfc/rfc6960.txt) | "The \"unknown\" state indicates that the responder doesn't know about the certificate being requested" |
| S27 | RFC 6960 section 2.2, same page | "This state MAY also be returned if the associated CA has no record of ever having issued a certificate with the certificate serial number in the request" |
| S28 | RFC 6960 section 2.2 note, same page | "the \"unknown\" status indicates that the status could not be determined by this responder, thereby allowing the client to decide whether it wants to try another source of status information" |
| S29 | Kleppmann, How to do distributed locking, [martin.kleppmann.com](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) | "a fencing token is simply a number that increases (e.g. incremented by the lock service) every time a client acquires the lock" |
| S30 | Kleppmann, same page | "the storage server remembers that it has already processed a write with a higher token number (34), and so it rejects the request with token 33" |
| S31 | AWS DynamoDB global tables, [docs.aws.amazon.com](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html) | "DynamoDB will resolve the conflict by using the modification with the latest internal timestamp on a per-item basis, referred to as a \"last writer wins\" conflict resolution method" |
| S32 | Chrome extensions permission warnings, [developer.chrome.com](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings) | "When a new permission that triggers a warning is added, the extension will be disabled until the user accepts the new permission." |
| S33 | OpenAI deprecations, [platform.openai.com](https://platform.openai.com/docs/deprecations) | "At the time of the shut down, the model or endpoint will no longer be accessible." |
| S34 | AWS IAM PassRole, [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) | "To pass a role (and its permissions) to an AWS service, a user must have permissions to pass the role to the service." |
| S35 | AWS IAM roles terms and concepts, [docs.aws.amazon.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) | "Service-linked roles appear in your AWS account and are owned by the service." |
| S36 | GDPR Article 16(1), reproduction at [gdpr-info.eu](https://gdpr-info.eu/art-16-gdpr/) | "The data subject shall have the right to obtain from the controller without undue delay the rectification of inaccurate personal data concerning him or her." |
| S37 | GDPR Article 16(2), same reproduction | "the data subject shall have the right to have incomplete personal data completed, including by means of providing a supplementary statement" |

Four things could not be fetched and nothing here rests on them. FINRA Rule 8311: finra.org returned a Cloudflare interstitial, so this document carries no FINRA quote at all and CAND-05 says plainly that composition is forced by the corpus and externally unsourced. The GDPR official text: eur-lex.europa.eu returned an empty body, so S36 and S37 are from the gdpr-info.eu reproduction, labelled as such. The Lyondell Chemical 2010 SEC exhibit: HTTP 403, so no candidate here asserts the proposition `AUTHORITY-LIFECYCLE.md` cites it for. S10 to S17 come from a university course reproduction of the Restatement rather than from the official American Law Institute publication, and are cited as a reproduction.
