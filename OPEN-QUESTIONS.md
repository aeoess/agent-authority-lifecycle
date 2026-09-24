# Open questions

These are the parts we do not know how to answer yet. They are listed so nobody mistakes the rest of the model for a claim about them.

## Teardown completeness

A list of processed descendants does not establish that the list was every authority descendant at the relevant boundary. Delegation can be issued locally, so a descendant can exist that the teardown process never saw, and a descendant can be signed after the revocation with a valid parent chain. Signed lineage proves structure. It does not prove the descendant was accepted authority when the revocation took effect.

A completeness claim needs three things we have not settled. What set a boundary claims to have accepted at a given moment. What prevents something from entering that set afterwards while still counting as earlier authority. What public commitment can prove closure over that set without exposing private state.

## Work in flight

When authority is revoked while a workflow is running, the old grant cannot authorize new effects at the next authorization point. What happens to the operation itself (resume under new authority, restart, compensate, stop) depends on the kind of effect. We do not yet have a general model for it.

## Release from suspension

Lifting one suspension should not clear another, bypass a revocation that happened while the agent was suspended, or recreate rights that changed in the meantime. Multiple suspension causes probably need to compose, with each one released separately. Not yet specified.

## Critical revocation

Revoking a high-level authority can disable a large set of agents. An approval for such a revocation could be bound to a snapshot of its impact and checked again right before it takes effect, with uncertain impact treated as large rather than small. Designed, not yet built or tested.

## Office vacancy and succession

When authority was exercised for an office and nobody currently holds it, nobody may be empowered to exercise, reaffirm or revoke what the previous holder issued. Whether office-based grants continue, suspend or need reaffirmation during a vacancy, and who may act for the office until it is filled, is not defined.

## Grants signed just before departure

If issuer standing is evaluated at issuance, an issuer who knows they are leaving can sign long-lived grants that stay valid after they are gone. A bounded lifetime for grants issued for an office, or a review when the office changes hands, are possible answers. Neither is specified.

## Authority rollback

Restoring a backup, a snapshot or a lagging replica can bring back authority state from before a revocation. An authority epoch, or an append-only record of revocations that a restore must replay, would stop a restore from reviving revoked authority. We have not specified either or tested what a verifier should return after a restore.

## Semantic drift

A grant can stay byte for byte the same while what it authorizes changes, because a tool, an API version or a resource classification changed underneath it. When a change in meaning should invalidate an earlier grant or approval, and how a verifier would detect it, is open.

## Notice and relying parties

A revocation can be recorded at one moment and reach an agent, a gateway and an outside counterparty at different moments. What a relying party that acted on stale but authentic evidence is entitled to, and what evidence of notice a principal needs to show, is not defined here. Agency law offers answers for human agents. This document does not assume they apply.
