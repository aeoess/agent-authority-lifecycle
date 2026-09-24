# Superseded designs

Part of Authority Lifecycle v0.3.0-draft. From the Agent Passport System work. Apache-2.0.

Designs we considered and replaced, with the reason. Kept because the reasons are part of the model.

## Cascade succession

Earlier idea: when a principal leaves, transfer their whole delegation tree to a new principal.

Replaced because it keeps authority provenance that no longer exists and makes it unclear who actually authorized each descendant. Current design: the successor or an organizational principal issues explicit new grants, and the old chain ends. See L2, L3 and L4.

## Transfer first, then revoke, as a universal rule

Earlier idea: in a handover, always issue the replacement before revoking the old authority, so the agent never has a gap.

Replaced because it guarantees a period where both old and new authority are valid. That is acceptable for a planned departure and wrong for a fired or compromised principal, where revoking first and accepting a gap can be the correct choice. Current design: an explicit cutover whose ordering depends on whether continuity or containment matters more.

## Derived revocation records as the way descendants die

Earlier reading: each descendant of a revoked delegation dies when a derived revocation record is written for it.

Replaced because it makes authority depend on a process that can stall, miss descendants, or be signed by a party with no authority over them. Current design: descendants fail because the verifier sees the revoked ancestor in their chain (L1). Per-descendant records, if any, are evidence, and completeness is a separate question (L12).
