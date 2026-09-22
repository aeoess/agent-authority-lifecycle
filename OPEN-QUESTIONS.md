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
