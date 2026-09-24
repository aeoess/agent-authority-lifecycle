# Authority Lifecycle for Long-Running AI Agents

Version 0.1.1-draft. Part of the Agent Passport System work. Apache-2.0.

## Scope

An agent can outlive the session that started it, the employee who sponsored it, the key it first signed with, the approval that let it act, and the workflow it was built for. This document is about what happens to its authority across those changes. What stays continuous, what must stop, what may be transferred, who can establish replacement authority, when current authority must be checked again, and what evidence proves each transition.

Every statement below carries a status.

- **specified** means draft-pidlisnyi-aps-03 states it normatively.
- **tested** means a public, runnable conformance case exists and is linked.
- **candidate** means a runnable case exists against proposed or third-party text, not against a published specification.
- **implemented** means a public implementation exists and is linked, with no conformance case yet.
- **proposed** means we think implementations should guarantee it, with reasoning, and nothing public yet tests it.
- **open** means we do not know the answer.

Statuses combine, for example specified and tested, or specified, not yet tested.

## Lifecycle objects are separate

Authority, as used here, is the bounded set of actions an agent may perform on behalf of a principal under currently valid grants and constraints.

Authority is not one record or one status flag. It depends on parties, authority artifacts, lifecycle states, action state and what a verifier can establish about them. These can change independently. A transition in one does not imply a transition in another unless the applicable authority model binds them. A common mistake in this area is treating two of them as one.

Not every concept below has to be a separate protocol object.

### Parties and standing

- **Agent identity.** Says which agent is acting. Identity continuity does not establish authority continuity.
- **Principal.** The person, office, organization or other body on whose behalf authority exists.
- **Issuer.** Whoever issues or signs an authority artifact. The issuer and the principal can be different.
- **Issuer standing.** Why the issuer was allowed to create, narrow, suspend, revoke or replace authority for the principal. A valid signature establishes who signed. It does not by itself establish standing.
- **Principal binding.** Says which principal an agent acts for. It can exist before any grant and outlive one, for example an agent registered to an organization between grants.
- **Sponsor or responsible owner.** Who is responsible for an agent's continued operation, where a system has that role. Changing a sponsor does not by itself transfer or replace existing authority.

### Authority and dependencies

- **Delegated authority.** Says X may do Y because principal Z granted it, under which constraints, for which targets and for what period, through a specific chain.
- **Authority path and dependency.** Which other authority a grant currently depends on. Historical provenance and current dependency are not necessarily the same thing.
- **Presented credential or session.** A session or derived token used to exercise authority in a particular request. Ending a grant does not necessarily invalidate every session or derived token already issued, and ending a session does not by itself end the grant.
- **Activation condition.** When already issued authority becomes exercisable. A grant can be validly issued and still wait on a date or a recorded event.
- **Target binding.** Which resource, counterparty or object the authority applies to. Continuity of a name does not by itself establish continuity of the thing named.

### Authority lifecycle state

- **Issuance.** The event that creates an authority artifact. Whether issuance was valid depends on the issuer's standing at that time.
- **Suspension.** Pauses or narrows the use of authority without permanently ending it.
- **Expiry or exhaustion.** Ends authority because a declared time, use count, budget, purpose or other bound has been reached. Expiry is not revocation.
- **Revocation.** Permanently ends a named authority artifact. A reversible pause is suspension, not revocation.
- **External restriction.** A block from outside the grant chain, such as a sanction, a court order or a legal hold. It can stop some effects while the grant itself stays valid.
- **Authority epoch.** Where a system uses generations, separates current authority from stale authority surviving in sessions, queues, replicas, snapshots or restored state.

### Decisions and effects

- **Approval.** A principal or approver allows a proposed action. It is an input to authorization, with its own scope, expiry and use count, and it can be withdrawn before dispatch.
- **Authorization decision.** The record an enforcement point makes that an action was allowed or denied, against the authority, policy and inputs it evaluated.
- **Invocation.** The exact action submitted for execution.
- **Execution.** The attempt to carry out that invocation.
- **Effect.** The externally observable result, if any.
- **In-flight state.** Where an action is between authorization and a known outcome. Authority can change inside that interval.

### Verification and evidence

- **Signing key.** The key an identity signs with at a given time. Key lifecycle and authority lifecycle are separate.
- **Verifier trust policy.** Which issuers, roots, status sources and rules a verifier accepts. A verifier can stop trusting an issuer without anything being revoked.
- **Status observation.** What authority state a verifier could establish, from which source, at what time and with what freshness. Current authority and observed authority can differ.
- **Notice.** That a particular party or enforcement point learned of a transition at a particular time. Recording a transition and observing it are different events.
- **Evidence.** Records a decision, transition, invocation, execution or effect. Ending authority does not by itself erase or invalidate evidence of earlier events.
- **Coverage and completeness.** What set or interval the available evidence covers. Showing that individual records are authentic is weaker than establishing that all relevant events were observed.
- **Accountability record.** Who a system identifies as responsible for an agent or action. It does not by itself establish legal liability.

Human agency law has related distinctions between actual authority, notice and apparent authority. Those doctrines are a useful source of cases for this work. This document does not assume they apply to AI agents.

Status. Agent identity, principal binding, delegated authority, signing key, approval, suspension, revocation and execution carry over from 0.1.0-draft. The grouping and every other entry are **proposed** in 0.1.1-draft. No public case tests them yet.

### What changes when a person leaves

A person's departure is not itself a revocation. It is an external event, and its effect on authority depends on the authority relationship involved and the rules that govern it.

A person can be the principal of a grant. A person can instead be an issuer acting for an organization or office, with their own standing to issue coming from another authority relationship. These cases are not interchangeable.

Two questions stay separate. First, was the grant validly issued? That depends in part on whether the issuer had standing when it was created. Second, what does the grant continue to depend on? A grant can stay dependent on an authority path that later ends, or the governing authority model can provide that a validly issued organizational grant continues after the individual issuer leaves.

L1 is unchanged. If an authority artifact the grant currently depends on is revoked, the dependent authority is invalid. Personnel changes do not silently remove a dependency, re-parent authority or create replacement authority.

Some organizational instruments say explicitly that authority delegated from an organizational position continues after the delegator leaves that position, until someone then empowered rescinds or modifies it. One example is a set of resolutions Lyondell Chemical filed with the SEC in 2010 ([exhibit](https://www.sec.gov/Archives/edgar/data/0000842635/000119312510084311/dex99t3b3.htm)). Other authority models end, suspend or require review of those grants. The departure alone does not choose between them.

Where the verification result depends on whether authority was personal, organizational or dependent on another authority path, the supporting evidence has to distinguish the principal, the issuer and the relevant dependency. If it cannot, continuation of authority has not been established.

Office vacancy and succession remain open. The model does not yet define whether office-based authority continues, suspends or needs reaffirmation when no current office holder can exercise or revoke it, or how to treat long-lived grants an issuer signs just before leaving.

Status **proposed**. No public case tests these distinctions yet.

## Invariants

### L1. Revoking an ancestor invalidates the authority that depends on it

Once a verifier can establish, under the applicable status and freshness rules, that an ancestor delegation is revoked, a chain that depends on that ancestor is invalid. This holds even if the descendant has no revocation record of its own and was never on anyone's list of children.

We also propose that enumerating descendants stays a cleanup and reporting tool, useful for a teardown report. It should not be what makes a chain-verifiable descendant invalid. Where a credential does not carry a chain a verifier can check, such as an opaque bearer token, an issuer-side revocation mechanism is still needed.

Status **specified and tested**. [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.3 requires checking revocation state for every chain member. Case `ancestor-revocation-chain`, three-hop chain, root or middle delegation revoked, both reference SDKs return `REVOKED`. [Pinned README](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/8715387a6e24d143ccabc80594c96482e066a5df/fixtures/ancestor-revocation-chain/README.md), [PR #107](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/107).

### L2. Identity continuity does not imply authority continuity

The same agent identity can appear under an old authority chain and under an independent replacement chain. Revoking the old chain's ancestor invalidates the old chain. The replacement chain stands on its own.

This is how a bookkeeping agent keeps running when the employee who sponsored it leaves. The agent continues. Its old authority does not.

Status **tested** as a scenario. The chain results are [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.3 verification. The handover framing is an operational scenario, not a draft-03 succession rule. Case `sponsor-handover`, vectors SH-01 to SH-04 and SH-06. [Pinned README](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/734fafa9fb8709cc03e756db8793180fe8870d19/fixtures/sponsor-handover/README.md), [PR #108](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/108).

### L3. Reauthorization creates new authority

Continuity after revocation means a new grant from a principal who currently holds authority. It never means reversing the revocation or re-parenting the old chain.

Status **specified in part**. [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.5 states that revocation is irreversible. That new authority must come from a fresh grant is **proposed**. The handover case shows the replacement chain is independent. Nothing yet tests that a revoked artifact cannot be restored.

### L4. A successor does not inherit the predecessor's delegation tree

A successor's grant covers what the successor issues. Other descendants of the departing principal stay invalid until someone with current authority issues them new grants.

Status **tested** as a scenario, vector SH-05 of the `sponsor-handover` case, [PR #108](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/108).

### L5. Independent chains are not combined

An agent holding two valid chains cannot use them together to create a grant broader than either chain allows. Each grant follows one parent chain.

Status **specified, not yet tested**. [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.3 says each action selects one root-to-leaf authority chain and a verifier MUST NOT union scopes or budgets from multiple chains. No public case yet.

### L6. An earlier approval is not current authority

An earlier approval does not establish that revocation state is still current when execution occurs. [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.5 requires the enforcement gateway to recheck revocation status at execution time, not only at approval time. Broader execution-time revalidation is being tested separately.

Status **specified** for the revocation recheck. **candidate** for broader execution-time revalidation, case `cached-authorization-revocation`, nine timeline cases written against proposed OWASP MCP Top 10 text. [PR #106](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/106).

### L7. Unknown revocation state is not active

A revocation answer that is unavailable or stale is indeterminate. It does not become active, and the evidence does not claim a revocation that never happened. An enforcement point may deny on indeterminate, and the denial should say why.

Status **specified** for unavailable or stale results, which [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.3 makes indeterminate. A resolver answer the implementation does not recognize, such as a future status value, is **candidate**. Case `revocation-resolution-forward-compat` exercises that fail-closed behavior, and its own README states that draft-03 does not define the general rule. [README at 68ed63a](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/68ed63a9faa239fc56a54747458d889ab4269a8c/fixtures/revocation-resolution-forward-compat/README.md).

### L8. Suspension is not revocation

Suspension stops the use of authority and of everything that depends on it, and can be lifted. Revocation is terminal for the artifact it names. A restricted state is different again and does not have to pause descendants.

Status **proposed**.

### L9. Key rotation is not delegation revocation

An identity can rotate its signing key and continue. A verifier selects the key version authorized at the artifact's issued_at, not the key current at verification time, so rotation does not by itself invalidate artifacts signed before it. The artifact timestamp is an issuer claim. When the result depends on whether an artifact was signed before a key was retired, it needs acceptable timestamp or log evidence, and without it the result is indeterminate. Revoking a delegation is a statement about that delegation, not about the key that signed it.

Status **specified and implemented**. [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 2.4. Historical key resolution is implemented in the Agent Passport System reference SDKs.

### L10. Expiry is not revocation

Both stop authority from being used. Expiry says the grant reached its planned end. Revocation says someone with authority ended it early. That difference matters for evidence and for whether a replacement is expected.

Status **proposed** as a lifecycle distinction. Current validity is part of [draft-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) Section 3.3 chain verification.

### L11. No silent authority resurrection

When the authority path an implementation selected becomes invalid, it should not quietly fall back to another stored grant unless that fallback was itself explicitly authorized. Changing which authority an agent acts under should be a visible decision.

Status **proposed**.

### L12. Completeness is a separate and stronger claim

A record that says a teardown processed some descendants proves that its signer made that statement. It does not show that the list was every descendant at the relevant moment, that every write persisted, or that nothing was issued concurrently. A claim that all descendants were processed needs a defined basis for which set was complete.

Status **open** for how to establish that basis. See OPEN-QUESTIONS.md.

## Operational cases

These are scenarios the invariants have to handle, not new rules.

- An employee leaves normally, with a planned handover.
- An employee is fired or compromised, where immediate containment matters more than continuity.
- A bookkeeping or reconciliation agent must keep running across the change.
- A planned handover with a short overlap, against an emergency cutover that accepts a gap.
- An action already in flight when authority changes.
- An agent that holds more than one grant.
- A revocation service that cannot be reached.
- An agent suspended during an investigation.

For a handover, the replacement authority has to come from a currently authorized principal, and continued operation has to use it. How the cutover is ordered is a choice. A planned handover may accept a short overlap. A compromised principal may call for revoking first and accepting a gap. The old chain must not remain the basis for continuity in either case. At the next authorization point after revocation, the old grant cannot authorize any new effect. Whether a workflow then resumes, restarts, compensates or stops depends on the operation.

## How to cite

See CITATION.cff. If you reuse or adapt this material, cite the canonical repository and the version you used.
