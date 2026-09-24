# Authority Lifecycle: Cases

Version 0.1-draft. Part of the Agent Passport System work. Apache-2.0, same terms as `AUTHORITY-LIFECYCLE.md`.

These are situations where the people, keys, approvals, offices, resources or infrastructure around an agent change, and the question is what happens to its authority. They test the concepts and invariants in [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md) and the gaps in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

Many cases rest on a human, institutional or systems precedent: a statute, a court or agency finding, a standard or a documented incident. None of those sources says anything about AI agents. The translation into agent terms is ours, and the precedent is a source of cases, not a claim that the law applies to AI agents.

There are two tiers.

- **Verified.** We fetched the cited source and checked that it supports the stated precedent. The expected outcome is still **proposed**. No runnable fixture exists for any case yet.
- **Candidate.** Produced by a research pass and not yet checked. The source is claimed, not verified. A "Known issue" note marks a problem already found. Candidates are verified, corrected, merged into another case or removed as review continues. Do not cite a candidate's source without checking it.

Current count: 25 verified, 139 candidates. No case is a conformance result. Cases that need a runnable fixture say so in the research record, and the ones that get built will link to the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite.

## Verified cases

### LC-C-006. A tainted ancestor invalidates dependents only from the moment the taint is found, not retroactively

**Situation.** A chain of appointments rests on a person's authority to make them. Eighteen months later, an independent investigator finds that person's own appointment was never valid, not revoked, never valid in the first place, and by then the downstream appointees have signed many orders that already took effect.

**Human analog.** The GAO's August 2020 finding that DHS acting secretary Chad Wolf's and acting deputy secretary Ken Cuccinelli's appointments were invalid, because Kevin McAleenan, who named them, had himself been installed outside the statutory order of succession and had no authority to amend that order. [GAO finding, reported by GovExec](https://www.govexec.com/management/2020/08/top-two-homeland-security-officials-are-serving-illegally-gao-rules/167714/): "McAleenan's subsequent appointments of Wolf and Cuccinelli were therefore invalid, GAO said, as he was not eligible to make them."

**What should happen.** A verifier needs a distinct status for "invalid from issuance, discovered late," not the same as a revocation event, because nobody revoked anything and it was never valid to begin with. Going forward from the finding, dependent chains are invalid. What happens to the orders and effects already executed while the chain looked valid is a separate question the finding itself does not answer.

**What a naive system gets wrong.** A revocation-only model finds nothing wrong here, because no one ever revoked anything. It has no way to represent "this grant was void from issuance" discovered after the fact, and no way to backdate that discovery without either pretending nothing happened or silently erasing evidence of effects already taken.

**Related invariant/open question.** L1 (revoking an ancestor invalidates dependents) assumes the ancestor was once valid and was later revoked. This case is the harder one L1 does not cover, an ancestor invalid from the start, discovered long after the fact. Also touches the "work in flight" operational case and L12 (completeness), since the orders executed under the tainted chain are exactly the evidence a completeness claim needs to account for.

**Status:** proposed.

---

### LC-B-008. Authority can end completely, instantly, and outside the delegation system entirely

**Situation.** A bank's officer authority does not merely get revoked. A federal receiver is appointed and by statute steps into every power that officer held, the instant the appointment takes effect, with zero notice to the delegation system that was relying on that officer's authority.

**Human analog.** 12 U.S.C. § 1821(d), under which the FDIC as receiver of a failed bank succeeds by operation of law to all rights and powers of the institution and its officers. [Cornell LII](https://www.law.cornell.edu/uscode/text/12/1821): "The Corporation shall, as conservator or receiver, and by operation of law, succeed to all rights, titles, powers, and privileges of the insured depository institution."

**What should happen.** Every delegation rooted in the former officer's authority is void from the moment the receiver is appointed, whether or not the bank's own systems ever recorded a revocation. No replacement authority exists until the new principal (the receiver) issues one.

**What a naive system gets wrong.** A system that expects the terminating event to show up as a revocation record in the infrastructure it monitors sees nothing, because the ancestor authority ended through an external legal fact with no corresponding artifact anywhere in the delegation graph.

**Related invariant/open question.** A harder-edged instance of L1 and L2, where the "ancestor" whose end triggers invalidation is not an APS artifact or even a company-internal record, but a statute taking effect the instant a regulator acts.

**Status:** proposed.

---

### LC-B-026. A third party outside the principal-agent relationship can inject a new approval gate into an otherwise unmodified, valid chain

**Situation.** A company settles a regulatory action. The consent decree does not touch any existing delegation. It adds a new, externally-imposed requirement that a named "responsible employee or official" personally certify a defined category of future reports, for the life of the decree.

**Human analog.** Consent decree practice requiring a named responsible official to certify compliance reports under penalty of law. [SEC EDGAR filing](https://www.sec.gov/Archives/edgar/data/1397516/000119312507093837/dex105.htm): "...which makes any representation concerning the Defendants' compliance or noncompliance with any requirement of this Consent Decree shall be certified by a 'responsible employee or official' of the Defendants."

**What should happen.** The original delegation chain is untouched and still valid, but a transaction in the decree's scope is no longer sufficient on that chain alone. It also needs the named official's separate certification, until the decree's own sunset date.

**What a naive system gets wrong.** A gateway that only re-verifies the original chain has no slot for a chain-external approval requirement injected by an outside party. It keeps authorizing exactly the transactions the decree was meant to catch, because nothing in the delegation itself changed.

**Related invariant/open question.** Structurally close to a dual-control policy, but the source of the added gate is external (a court-approved settlement, not internal risk policy), which none of L1-L12 name as a category. Also the strongest sourced instance found of "policy change" as a family.

**Status:** proposed.

---

### LC-E-002. A valid, non-expired, non-revoked grant can become unexecutable, and that is a fourth state, not a variant of the other three

**Situation.** A delegation names a specific pinned model snapshot as its executor. The provider retires that snapshot on a published schedule. Nobody revoked the delegation, nothing expired on its own terms, and no one suspended anything. The executor named by the grant simply stops existing.

**Human analog.** OpenAI's deprecation policy for generally available models. [OpenAI developer docs](https://developers.openai.com/api/docs/deprecations): "At the time of the shut down, the model or endpoint will no longer be accessible."

**What should happen.** A verifier needs a status distinct from valid, revoked, suspended, and expired, something like "executor unavailable," because the authority itself is intact under every lifecycle rule while the thing it authorizes has become impossible to carry out. The fix is a technical re-pointing to a live executor, not a revocation investigation.

**What a naive system gets wrong.** Collapsing "cannot currently execute" into "invalid" or "expired" loses an operationally important distinction. An expired grant needs the principal to decide whether to renew it. A retired-executor grant needs someone to re-point it to a live target, which has nothing to do with whether the principal still consents.

**Related invariant/open question.** L10 separates expiry (planned end) from revocation (early end by authority). This case is neither: the grant's own terms are unaffected, and what changed is outside the grant's control.

**Status:** proposed.

---

### LC-E-033. A provider-side capability upgrade can expand what a delegation authorizes with zero delegation-layer event

**Situation.** A delegation authorizes an agent running on a named model to perform a scoped set of actions. The provider later ships a capability update, tool and function calling, to that same named model. The delegation record never changes, but the agent it names can now do materially more than the issuer ever contemplated when scoping the grant.

**Human analog.** OpenAI's June 2023 update giving GPT-3.5-turbo and GPT-4 the ability to detect when a function should be called and respond with JSON matching a function signature. [TechCrunch](https://techcrunch.com/2023/06/13/openai-intros-new-generative-text-features-while-reducing-pricing/): "These models have been fine-tuned to both detect when a function needs to be called … and to respond with JSON that adheres to the function signature."

**What should happen.** A delegation's authorized scope should be understood as bounded by the capability set that existed when it was issued. A provider-side capability upgrade must not be read as silently expanding what the delegation covers. New capability needs either a fresh grant or an explicit re-consent step, not automatic inheritance.

**What a naive system gets wrong.** Treating a delegation's written terms as fully capturing its scope, and therefore stable over time, when the actual capability of the identity it names can expand out from under it with zero delegation-layer event marking the change.

**Related invariant/open question.** None of L1-L12 name capability drift, since they are scoped to grant, revoke, suspend, expire, and rotate, not to a delegation's target quietly becoming more capable. This is the concrete, dated instance behind the more abstract "semantic drift" shape the corpus also describes via rolling model aliases and mutable container tags.

**Status:** proposed.

---

### LC-F-017. A revocation that is true at the source can still read as false at a lagging replica: the "new enemy problem"

**Situation.** A principal revokes a delegation and immediately performs a sensitive action, assuming the revocation is already in effect everywhere. An authorization check for that same delegation is served from a read replica that has not yet applied the revocation, because the check was never pinned to a point in time after the write.

**Human analog.** Google's Zanzibar authorization system, built specifically to solve this: a stale permission read after a change is the "new enemy problem," addressed with consistency tokens that force a read to observe a specific prior write. [AuthZed](https://authzed.com/blog/new-enemies): "a token which represents the exact permissions used to protect a specific version of the content, and the content itself."

**What should happen.** Any authorization check that should causally follow a revocation, in the same session or explicitly linked, must be guaranteed to observe that revocation. That requires a consistency token or equivalent, not a best-effort tolerance for replication lag.

**What a naive system gets wrong.** Treating eventual consistency as good enough for authorization reads, when the actual requirement is that a check which should see a given write must be able to prove it did. Otherwise the read does not count as having checked at all.

**Related invariant/open question.** L6 and L7 cover recency and unknown-state at evaluation time, but assume a single answer source. This is multiple physical replicas of the same logical revocation state transiently disagreeing, a different failure shape, closer to the OPEN-QUESTIONS.md "authority rollback" territory than to ordinary staleness.

**Status:** proposed.

---

### LC-F-026. Without a quorum safeguard, an isolated primary keeps accepting authority-mutating writes nobody else will ever see

**Situation.** An authority-mutation coordinator runs as a primary with automatic failover. A network partition isolates the primary from its monitoring peers, but not from every client. Clients on the primary's side of the partition keep sending grants and revocations to it, and it keeps accepting them, unaware a new primary has already been promoted on the other side.

**Human analog.** Redis Sentinel's own documented failure scenario: an isolated primary that clients can still reach keeps accepting writes that are later discarded, unless a write-quorum safeguard is configured. [Redis Sentinel documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/): "a network partition isolated the old master M1, so the replica R2 is promoted to master. However clients, like C1, that are in the same partition as the old master, may continue to write data to the old master."

**What should happen.** A primary that can no longer confirm quorum must stop accepting authority-mutating writes rather than keep serving them. Writes accepted while isolated must be identified and reconciled, any revocation among them re-applied against the new primary, rather than silently lost or silently kept.

**What a naive system gets wrong.** Configuring failover purely for availability, so the system optimizes for "always accept writes" when the correct behavior for authority-mutating writes specifically is "refuse writes you can't be sure will survive."

**Related invariant/open question.** Overlaps the general shape of well-known split-brain incidents, but isolates a narrower, concretely fixable gap: the absence of a quorum-based write safeguard on the primary itself. Sits under the OPEN-QUESTIONS.md "authority rollback" heading, since a partition that resolves the wrong way is a rollback risk even with no backup restore involved.

**Status:** proposed.

---

### LC-D-009. A documented scope means nothing if the resource-side boundary never actually enforces it

**Situation.** A vendor is granted credentials scoped, on paper, to one narrow function. Nothing in the actual network configuration restricts that vendor's access to that function. So when the vendor's own systems are compromised through an unrelated channel, the stolen credentials reach far more than the paperwork ever authorized.

**Human analog.** The 2013 Target breach: attackers used network credentials stolen from Fazio Mechanical, an HVAC and refrigeration vendor whose own description of its access was narrow. [Krebs on Security](https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/) quotes Fazio's stated scope as "exclusively for electronic billing, contract submission and project management," access that, unsegmented, reached point-of-sale systems that had nothing to do with billing.

**What should happen.** A scope statement in a delegation is only meaningful if the enforcement boundary actually restricts execution to that scope. The documented scope and the technically reachable scope need to be checked against each other as a distinct verification step, because a narrow-looking delegation over an unsegmented resource is not narrow at all in practice.

**What a naive system gets wrong.** Verifying "this delegation's stated scope is billing-only" and treating that as sufficient. That checks the paperwork, not the plumbing, and the two can diverge for years with nothing in the delegation-verification layer ever noticing.

**Related invariant/open question.** None of L1-L12 address whether the resource-side enforcement boundary actually implements a delegation's stated scope. They assume it does. This is the clearest sourced instance of "resource identity reuse / target binding" the corpus produced.

**Status:** proposed.

---

### LC-C-011. A concurrence requirement is a dispatch-time gate, not a second chain to union with the first

**Situation.** An action requires two independently authorized principals to concur before it proceeds. One principal authorizes it. The other has not yet. A verifier built only around single root-to-leaf chain verification has no way to represent "wait for a second, independent concurrence" as anything other than either wrongly admitting the first chain alone, or wrongly trying to model the requirement as merging two chains into one.

**Human analog.** The US two-person concept for nuclear weapons: two independently authorized individuals must concur before a launch-related action proceeds. [Wikipedia, Two-person rule](https://en.wikipedia.org/wiki/Two-person_rule): "The two-person concept is designed to prevent accidental or malicious launch of nuclear weapons by a single individual."

**What should happen.** A verifier must refuse dispatch unless both required concurrences are present and fresh at the same moment. One valid authorization alone is insufficient no matter how strong that single chain is, and a longer or more senior chain never substitutes for the missing second concurrence.

**What a naive system gets wrong.** Confusing a concurrence gate with the scope-union problem L5 already forbids. They look similar (two chains, one action) but are opposite failures. L5 is about not letting two chains add up to more scope than either allows. A concurrence gate is about refusing to act on one chain alone regardless of scope.

**Related invariant/open question.** L5 forbids unioning chains to expand what one action is allowed to do. This is a distinct primitive, a dispatch-time gate requiring two separate, independently valid authorizations to be present together, that none of L1-L12 name.

**Status:** proposed.

---

### LC-C-016. The bar for granting authority and the bar for withdrawing it are not always the same bar

**Situation.** A dispatcher and a pilot in command jointly hold operational control of a flight. Once the flight is released and underway, either one alone can unilaterally stop or redirect it. But originating or continuing the flight required both to agree in the first place.

**Human analog.** 14 CFR § 121.533, joint responsibility for preflight planning, delay, and dispatch release. [Cornell LII](https://www.law.cornell.edu/cfr/text/14/121.533): "The pilot in command and the aircraft dispatcher are jointly responsible for the preflight planning, delay, and dispatch release of a flight."

**What should happen.** A verifier must apply different thresholds depending on the direction of the action. Continuation or origination requires both principals' current concurrence, while cancellation or restriction requires only one. Using the same threshold in both directions either lets one party force continuation over the other's objection, or makes it too hard for either party to stop something unsafe.

**What a naive system gets wrong.** Modeling every concurrence relationship on the symmetric nuclear-launch pattern (LC-C-011), where both sides must agree in both directions. This case is the same two-principal shape with a deliberately asymmetric rule, which a framework built only on the symmetric pattern gets backwards.

**Related invariant/open question.** Extends the joint or quorum family with an asymmetry, grant versus veto, that nothing in L1-L12 or the sponsor-handover conformance case names.

**Status:** proposed.

---

### LC-A-016. Some replacement authority is pre-committed at issuance time, not issued fresh after the fact

**Situation.** A single delegation instrument names a primary delegate and an ordered list of successors. The primary exits: dies, resigns, becomes incapacitated. The next-in-line successor should be able to act under the same original grant, with no new document and no action required from the principal at the moment of handoff.

**Human analog.** The Uniform Power of Attorney Act's successor-agent provision. [UPOAA (2006) §111, hosted by the Mississippi Secretary of State](https://www.sos.ms.gov/content/documents/pol_res/power%20of%20attorney/5upoaa_final_may08.pdf): "A principal may designate one or more successor agents to act if an agent resigns, dies, becomes incapacitated, is not qualified to serve, or declines to serve."

**What should happen.** The successor's authority derives from the same original delegation, at the scope and terms that instrument already set, activated by the primary's exit. It is not a new grant, and it needs nothing from the principal at handoff time.

**What a naive system gets wrong.** A system built around "replacement authority always means a fresh grant from a currently-authorized principal" (the L3/L4 pattern) has no slot for succession pre-committed inside a single instrument. It either treats the successor as unauthorized until a new grant appears, or wrongly treats the successor as inheriting the primary's entire personal delegation tree rather than just this one instrument.

**Related invariant/open question.** L3 and L4 assume replacement authority is issued fresh, after the fact, by whoever currently holds authority. This is a third pattern, authority pre-committed at issuance for a defined contingency, that neither invariant names.

**Status:** proposed.

---

### LC-B-012. A merger can vest authority in a new principal by operation of law, with no issuance event at all

**Situation.** Company A merges into Company B under state corporate law. The instant the merger takes effect, Company B, not Company A, holds every power Company A's officers held, without Company B's officers ever issuing anything. A delegation chain that depended on Company A's authority now needs to resolve to Company B, automatically.

**Human analog.** Delaware General Corporation Law § 259: on a merger's effectiveness, the surviving corporation is automatically vested with the constituent corporations' rights, privileges, powers, and franchises. [Delaware Code](https://delcode.delaware.gov/title8/c001/sc09/index.html): "possessing all the rights, privileges, powers and franchises as well of a public as of a private nature."

**What should happen.** Unlike an employee's departure, where continuity legitimately requires a fresh grant from a currently authorized principal, statutory merger vests authority automatically and instantly by law. A framework that demands an explicit new grant before honoring the chain under the surviving entity produces a false denial of authority the law says already exists.

**What a naive system gets wrong.** Applying the "successor must issue a fresh grant" pattern literally to a statutory merger. The law performs the succession without anyone issuing anything. Treating the old, now-nonexistent corporation as still the operative principal is equally wrong in the other direction.

**Related invariant/open question.** L2, L3, and L4 all assume a human or organizational principal actively issues a new grant to establish replacement authority. Statutory merger is a real, common succession pathway with no issuance event at all, which none of them contemplate.

**Status:** proposed.

---

### LC-D-029. A correctly-resolved historical key proves who signed, not what was actually built

**Situation.** An attacker compromises a vendor's build and code-signing infrastructure and uses the vendor's own legitimate signing key to sign a malicious update. The signature is, by every cryptographic measure, completely valid and correctly attributable to the legitimate key. What it attests to, that the build process produced this artifact honestly, is false.

**Human analog.** The 2020 SolarWinds/SUNBURST compromise. [ReversingLabs](https://www.reversinglabs.com/blog/sunburst-the-next-level-of-stealth): "The build infrastructure was compromised. In addition, the digital signing system was forced to sign untrusted code."

**What should happen.** Signature verification needs to be paired with independent build-provenance attestation, a reproducible build, a separate transparency log of what was actually built and when, rather than treating "signed by the vendor's key" as equivalent to "produced by the vendor's legitimate process." The two claims are only equivalent if the pipeline feeding the key is also verified uncompromised, and no amount of correct key-version resolution can establish that on its own.

**What a naive system gets wrong.** Checking only cryptographic signature validity, which makes a build-pipeline compromise invisible. The signature passes every check a verifier has, because the compromise happened upstream of the key, not at the key.

**Related invariant/open question.** L9 addresses selecting the historically correct key version at issuance time, treating key rotation as distinct from delegation revocation. This is a different failure entirely: the correct key, used correctly, on an artifact the process itself made illegitimate, a gap key-version resolution alone cannot close.

**Status:** proposed.

---

### LC-A-027. A verifier's internal "chain is void" and a relying party's protected reliance are two separate facts, not one boolean

**Situation.** A principal terminates an agent's actual authority. A third party who previously dealt with that agent has not been told. The delegation is dead for chain-verification purposes the instant it's terminated, but from the third party's side, nothing has changed yet.

**Human analog.** Restatement (Third) of Agency § 3.11. [University of Washington course reproduction of the Restatement text](https://staff.washington.edu/djdrake/RESt-Agency.doc), confirmed locally against the section number: "The termination of actual authority does not by itself end any apparent authority held by an agent."

**What should happen.** From the counterparty's perspective, reliance on the agent's apparent authority can remain reasonable, and protected, until the counterparty actually has notice of the termination, even though the delegation itself is already dead for chain-verification purposes. These are two different outcomes, not one.

**What a naive system gets wrong.** Answering only "is the chain currently valid" and treating that as the whole answer. It ignores that a relying party's protection can turn on a separate fact, whether notice actually reached them, collapsing two different questions into one boolean.

**Related invariant/open question.** L7 is about an indeterminate revocation answer reaching a verifier. This is different: a determinate revocation that a specific third party has not yet been notified of, a reliance-protection question about the third party's own knowledge state. OPEN-QUESTIONS.md's "notice and relying parties" section names this as unresolved and explicitly does not assume agency-law doctrines transfer to AI agents.

**Status:** proposed.

---

### LC-A-003. An unmet contingency is indeterminate, not simply "not yet started"

**Situation.** A delegation is marked effective only once a stated contingency, commonly incapacity, is verified. No verification artifact exists yet. An agent tries to act under it anyway, and the delegation record parses fine and shows no revocation, so a naive system lets the action through.

**Human analog.** Uniform Power of Attorney Act § 109: a power of attorney can be made effective upon a future contingency, with the principal designating who verifies it occurred. [UPOAA (2006) §109, hosted by the Mississippi Secretary of State](https://www.sos.ms.gov/content/documents/pol_res/power%20of%20attorney/5upoaa_final_may08.pdf): "A power of attorney is effective when executed unless the principal provides in the power of attorney that it becomes effective at a future date or upon the occurrence of a future event or contingency."

**What should happen.** The delegation is indeterminate, not valid and not simply "absent," until an acceptable verification artifact from an authorized verifier role is attached. Acting on it before that point is an unauthorized act, not a borderline one.

**What a naive system gets wrong.** Treating an unmet contingency the same as "not yet started, will begin automatically," and letting the agent act early because the record parses and nothing has been revoked.

**Related invariant/open question.** L7 covers unknown revocation state. This is the mirror problem at issuance, unknown activation state, which none of L1-L12 name as its own category, and it needs a defined verifier role, not just any evidence.

**Status:** proposed.

---

### LC-D-010. A credential with no natural end, issued for a purpose that ended, is a standing liability no chain-verification check can catch

**Situation.** An account tied to a discontinued purpose is left enabled indefinitely, because nobody owned the task of disabling it once the purpose ended, and it was never given an expiry in the first place.

**Human analog.** The 2021 Colonial Pipeline ransomware attack, which began through a legacy VPN account. [The Hacker News](https://thehackernews.com/2021/06/hackers-breached-colonial-pipeline.html): "a legacy VPN profile that was not intended to be in use."

**What should happen.** Delegations and credentials issued for a bounded purpose should carry an expiry tied to that purpose's expected lifetime by default, rather than defaulting to indefinite validity. A credential with no natural end and no owner responsible for ending it is a standing liability that chain-verification correctness cannot catch, because by every technical measure the chain is still perfectly valid.

**What a naive system gets wrong.** Only invalidating credentials on explicit revocation or a stated expiry misses the much larger set that were simply never given either, because their issuers assumed "someone will turn this off" without ever encoding that as an actual expiry or ownership record.

**Related invariant/open question.** L10 distinguishes expiry from revocation for credentials that already have a defined end. This is a gap in how grants are issued in the first place, a credential with a foreseeable natural end that was never given one.

**Status:** proposed.

---

### LC-D-034. "Test" or "legacy" as a label is not the same as "test" or "legacy" as a validity fact

**Situation.** A non-production test application was granted broad consent by a highly privileged user years earlier, for a testing purpose that concluded long ago. The consent grant persists at its original elevated privilege level indefinitely, because nothing ever tied its validity to the purpose's lifespan.

**Human analog.** The Microsoft/Midnight Blizzard nation-state intrusion disclosed January 2024. [Microsoft Security blog](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/): "The threat actor then used the legacy test OAuth application to grant them the Office 365 Exchange Online full_access_as_app role, which allows access to mailboxes."

**What should happen.** Consent grants issued for a stated, bounded purpose should default to expiry at that purpose's natural conclusion. An org needs a periodic, systematic sweep of high-privilege consent grants held by non-production applications, rather than relying on the application's own "test" designation to imply reduced risk.

**What a naive system gets wrong.** Treating a consent grant as valid until explicitly revoked, with no link to the stated purpose's lifecycle. "Nobody uses this anymore" is invisible to any verifier that only checks grant validity.

**Related invariant/open question.** Same underlying gap as LC-D-010 (purpose-bound credential, no expiry), recurring in the OAuth-consent domain at a much higher privilege tier, against a nation-state actor. Maps to L10 and to the general shape of "expiry or exhaustion incl. purpose complete."

**Status:** proposed.

---

### LC-B-028. Authorization has to be rechecked right up to the moment of final execution, not just at issuance

**Situation.** A payment instruction is validly authorized and submitted. Minutes later, the authorizing officer discovers a problem and issues a stop instruction. Whether the stop works depends entirely on whether the paying bank has already acted on the original instruction. An identical stop instruction can succeed or do nothing, purely based on timing.

**Human analog.** UCC § 4-403, a customer's right to stop payment. [Cornell LII](https://www.law.cornell.edu/ucc/4/4-403): "A customer may stop payment of any item drawn on the customer's account by an order to the bank received at a time and in a manner that affords the bank a reasonable opportunity to act on it."

**What should happen.** The system must recheck for a stop or cancellation right up to the moment of final execution, not accept the original authorization as settled once issued. The recheck window has a hard boundary, the receiving institution's own action on the item, after which the same stop instruction that would have worked a moment earlier does nothing.

**What a naive system gets wrong.** Treating "validly authorized at issuance" as sufficient and only checking for a stop at that moment, rather than continuously up to execution. That executes payments the customer had every right to stop, purely because the stop-check happened too early.

**Related invariant/open question.** A concrete, narrowly-timed instantiation of L6 (an earlier approval is not current authority), adding the detail that the recheck window has a hard, event-defined boundary rather than a fixed duration.

**Status:** proposed.

---

### LC-E-019. Authority stays valid through a scheduled wind-down, not cut off the instant termination begins

**Situation.** A workload undergoing a graceful rolling replacement receives a termination signal while it still has an in-flight request being processed under its assigned identity. It needs a few more seconds to finish and make its final authorized call.

**Human analog.** Kubernetes pod termination. [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/): "The kubelet triggers the container runtime to send a TERM signal to process 1 inside each container. Once the grace period has expired, the KILL signal is sent to any remaining processes." The documentation confirms the grace-period mechanism itself. That the pod's own assigned identity and permissions remain valid throughout that window, rather than being cut at the moment the signal is sent, is this document's inference from how Kubernetes pods are known to work, not a line quoted from the page above.

**What should happen.** The instance's authority should remain valid and checkable for the duration of its graceful-shutdown window. A verifier should not treat "this instance has begun termination" as equivalent to "this instance's authority is now revoked." Those are separate facts, and its final in-flight call during the grace period should succeed exactly as it would have before termination began.

**What a naive system gets wrong.** Treating the start of a termination signal as an implicit revocation event, aborting otherwise-legitimate, already-authorized work purely because of an orchestration event that has nothing to do with whether the instance's authority is still valid.

**Related invariant/open question.** L8 distinguishes suspension (pauses use, can be lifted) from revocation (terminal). Termination-in-progress is neither, a third, scheduled-wind-down state L8 does not name.

**Status:** proposed.

---

### LC-B-024. Multiple independent suspensions on the same principal have to be released independently, not cleared by any one of them lapsing

**Situation.** A regulator suspends a representative for a fixed period. Separately, and for an unrelated reason, the representative's own firm has placed them under an internal restriction with no fixed end date. The regulatory suspension period lapses.

**Human analog.** FINRA's suspension regime. [FINRA Rule 8311](https://www.finra.org/rules-guidance/rulebooks/finra-rules/8311): a suspended person may not be associated with a member firm in "any capacity that is inconsistent with the sanction imposed or disqualified status, including a clerical or ministerial capacity."

**What should happen.** Authority should stay paused past the regulatory suspension's end date, because the firm's separate, unrelated restriction has not itself been lifted. The two suspension causes need to be tracked and released independently.

**What a naive system gets wrong.** Representing suspension as a single boolean flag, which incorrectly clears the moment the tracked suspension period ends, restoring authority even though a second, untracked restriction is still active.

**Related invariant/open question.** A concrete regulatory example of L8's proposed suspension, revocation, and restriction distinction, and it directly surfaces OPEN-QUESTIONS.md's "release from suspension" problem, which that document says is "not yet specified."

**Status:** proposed.

---

### LC-C-022. A pending-ratification state is neither "revoked" nor "not revoked," and if ratification is denied, the record has to say the action was provisional throughout, not that a final revocation was later reversed

**Situation.** A commander relieves a subordinate of command. The required written approval from a higher general officer has not yet arrived. Until it does, the relief has a lesser, provisional effect. If the approval never comes, the action is retroactively recharacterized as having only ever been the lesser effect, not undone from a final state.

**Human analog.** US Army relief-for-cause procedure. [Fort Carson command policy memo, quoting AR 600-20](https://home.army.mil/carson/6116/5089/9699/relief-for-cause.pdf): "Any commander may temporarily suspend a subordinate from command, but the final action to relieve an officer from any command position will not be taken until after written approval by the first general officer in the chain of command."

**What should happen.** A verifier needs a "revocation-pending-ratification" state, distinct from both full revocation and no revocation, during which the target's authority is suspended but the initiating principal's action is not yet final. If ratification never arrives, every record has to reflect that the action was provisional throughout.

**What a naive system gets wrong.** Conflating this with an ordinary self-declared, self-terminated suspension. This is a different shape, an external, unilateral suspension by a superior that only becomes a final revocation with a specific separate approval. Treating the two the same either finalizes a revocation that legally never became final, or fails to suspend the subordinate while waiting on paperwork.

**Related invariant/open question.** Adds a ratification-pending intermediate state with retroactive recharacterization on denial, a shape not present in L8's plain suspension and revocation split, and directly relevant to OPEN-QUESTIONS.md's "release from suspension."

**Status:** proposed.

---

### LC-D-004. A single compromised operator identity can be an implicit ancestor over many independent trees at once

**Situation.** Malware on one engineer's laptop steals a session. That engineer's ordinary job included minting production access tokens for every customer on the platform. The compromise is not a single-tenant event. It is an ancestor-level event for every tenant whose secrets that role could reach, even though no individual tenant's own credentials were directly touched.

**Human analog.** The January 2023 CircleCI incident. [CircleCI's own incident report](https://circleci.com/blog/jan-4-2023-incident-report): "the unauthorized third party was able to access and exfiltrate data from a subset of databases and stores, including customer environment variables, tokens, and keys."

**What should happen.** Revocation and rotation scope after compromising a high-fan-out operator identity has to be computed from that identity's reachable authority graph, every secret it could mint or read, not from a narrower "only this session's own artifacts" scope. Everything reachable through that role is presumptively compromised until proven otherwise.

**What a naive system gets wrong.** Scoping incident response to "revoke the compromised session and whatever it directly issued" undercounts the blast radius badly when the compromised identity's role is itself a highly-privileged ancestor over many independent trees. The actual exposed set is the transitive closure of what the role could reach, not what it is recorded as having touched.

**Related invariant/open question.** L1 covers revoking a known ancestor invalidating known descendants in one tree. This is the harder question of what "ancestor" even means when a compromised operator identity is an implicit ancestor over many independent principals' trees at once, a blast-radius computation problem none of L1-L12 address.

**Status:** proposed.

---

### LC-C-009. A legitimately confidential succession order breaks the assumption that every chain is independently, publicly verifiable

**Situation.** The order that determines who becomes the next holder of a critical position is itself confidential, held by one custodian rather than published where any relying party could check it independently before the moment of need.

**Human analog.** The House rule adopted after 2001 requiring the Speaker to privately give the Clerk an ordered succession list whose contents are not published. [Thompson Coburn](https://www.thompsoncoburn.com/insights/presidential-succession-102jjry/): "the speaker provides the clerk 'a list of Members in the order in which each shall act as Speaker pro tempore' in the case of a vacancy."

**What should happen.** A verifier at the moment of triggering has to rely on an attestation from a single custodian rather than an independently checkable chain. The protocol needs a defined trust boundary for that custodian, who else can confirm the custodian's own honesty and freshness, instead of assuming every succession order is publicly verifiable in advance.

**What a naive system gets wrong.** Assuming every authority chain must be independently, publicly verifiable end to end has no place for a legitimately confidential ordering. It either rejects the whole mechanism as unverifiable, or silently trusts whatever the custodian says with no fallback if the custodian is unavailable or compromised.

**Related invariant/open question.** Nothing in L1-L12 addresses a succession order that is deliberately not public. Also touches OPEN-QUESTIONS.md's "office vacancy and succession," since this is exactly a case of authority for an office needing to be exercised without every relying party being able to check the chain.

**Status:** proposed.

---

### LC-D-003. "Believed unused" is not the same as "verified inventory," and the gap between them is exactly where this incident happened

**Situation.** In response to a vendor breach, an org rotates credentials broadly, but the rotation tooling relies on a human judgment call about which service tokens are "still in active use." A token and account marked safe to skip, because someone believed them unused, turn out not to be, and become the attacker's entry point.

**Human analog.** Cloudflare's Thanksgiving 2023 incident, following the Okta support-system breach. [Cloudflare blog](https://blog.cloudflare.com/thanksgiving-2023-security-incident): "mistakenly it was believed they were unused. This was incorrect and was how the threat actor first got into our systems."

**What should happen.** A rotation-on-ancestor-compromise event must be complete over the actual grant set traceable to the compromised ancestor, not the subset someone currently believes is active. "Believed unused" is not a valid substitute for a verified inventory.

**What a naive system gets wrong.** Treating "rotate everything derived from the compromised ancestor" as equivalent to "rotate everything an admin remembers is in use." That silently leaves a live, exploitable descendant standing, exactly L12's completeness problem, playing out concretely.

**Related invariant/open question.** A direct, real-world instance of L12: what a rotation claims to have covered versus what actually exists. Motivates why a "believed complete" inventory is not a valid basis for a completeness claim.

**Status:** proposed.

---

### LC-B-022. A real legal exception can supply exactly the basis a completeness claim needs, without needing an open-ended "we keep everything for audit" policy

**Situation.** A former officer who granted a delegation chain exercises their GDPR right to erasure. The company needs to retain the delegation and revocation records naming that officer, to be able to prove, if ever challenged, exactly what authority existed, when it ended, and that the resulting teardown was complete.

**Human analog.** GDPR Article 17(3)(e), the legal-claims exception to the right to erasure. [gdpr-info.eu](https://gdpr-info.eu/art-17-gdpr/): "for the establishment, exercise or defence of legal claims."

**What should happen.** The records survive the erasure request specifically because of the legal-claims exception, not because of a general "we need this for auditing" policy. The retention has an actual legal basis with a defined scope, only what is necessary for legal claims, not an open-ended one.

**What a naive system gets wrong.** A privacy-compliance system that deletes anything containing personal data on any erasure request, with no legal-claims carve-out, deletes exactly the evidence a completeness claim under L12 depends on. Equally wrong: a lifecycle system that assumes it can retain whatever it wants for "evidence" without grounding that in an actual legal basis.

**Related invariant/open question.** OPEN-QUESTIONS.md's teardown-completeness section names "what public commitment can prove closure over a set without exposing private state" as unsettled. GDPR's legal-claims exception is a real, existing legal basis that answers part of that directly.

**Status:** proposed.

---

## Candidate cases

Grouped by the authority question they raise. IDs are stable and stay the same when a candidate is verified.

### Off-wire facts and standing

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-001 | Principal's death ends a non-durable agent's actual authority | L1, L10 | [claimed source](https://en.wikipedia.org/wiki/Apparent_authority) | Known issue: death is Restatement 3.07(2), not 3.08(1). Durable powers survive incapacity, not death. Termination is effective on notice. |
| A-002 | Principal's incapacity terminates non-durable authority, but not durable authority | NEW | [claimed source](https://en.wikipedia.org/wiki/Apparent_authority) |  |
| A-005 | Divorce (final decree) automatically revokes a spouse's designation as agent | NEW | [claimed source](https://law.onecle.com/california/probate/4154.html) |  |
| A-006 | Filing for divorce, not yet final, can itself terminate spousal delegated authority | NEW | Search-confirmed summary of Fla. Stat. S709.2109(2)(b) (chicago-familylaw.com, georgelmetcalfe.com secondary discussions of the statute's text) |  |
| A-009 | A fiduciary who feloniously kills the principal forfeits the fiduciary appointment, retroactively | NEW | Search-confirmed summary of UPC S2-803, cross-checked against law.justia.com Massachusetts codification of the section |  |
| A-013 | The agent's own death terminates the agent's actual authority | L1 | Search-confirmed summary of Restatement (Third) of Agency S3.06-3.07 (2006), cross-checked against the washington.edu course outline of the Restatement's structure opened during research |  |
| A-014 | The agent's own incapacity terminates the agent's authority to act, even if the principal is fine | L8 | Search-confirmed summary of Restatement (Third) of Agency S3.08 (2006) |  |
| A-015 | An agent's renunciation is effective only once notice reaches the principal | NEW | Search-confirmed summary of Restatement (Third) of Agency S3.10 (2006) |  |
| B-009 | Chapter 11's automatic stay takes effect instantly, before anyone can know about it | NEW | [claimed source](https://www.law.cornell.edu/uscode/text/11/362) |  |
| B-020 | Ex parte asset freeze binds before the frozen party can possibly know about it | NEW | [claimed source](https://www.ftc.gov/system/files/ftc_gov/pdf/TemporaryRestrainingOrder(withoutattachments) | Known issue: Rule 65(d)(2) binds only on actual notice. The case is being inverted into a notice-gated restriction. |
| B-025 | License revocation invalidates every chain resting on that license at once | NEW | [claimed source](https://www.nj.gov/dobi/division_banking/ocf/enforcement/2022/OCF22_21.pdf) |  |
| B-001 | Board resolution strips an officer's signing authority | L1 | [claimed source](https://www.law.cornell.edu/ucc/3/3-403) |  |
| C-023 | UCMJ convening authority: a role restricted to a closed statutory list, not delegable by ordinary grant | NEW | [claimed source](https://www.jcs.mil) |  |

### Conditions written into the grant

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-004 | Delegation becomes effective at execution once an authorized verifier confirms unavailability, not impairment | NEW | Uniform Power of Attorney Act (2006) S109, confirmed via research summaries of the Act's text (uniformlaws.org, uslawexplained.com) |  |
| A-011 | A settlor's incapacity converts a revocable trust's control without terminating the trust itself | L2 | Uniform Trust Code S602 (revocation/amendment by settlor) and S701-704 (trusteeship), confirmed via Maine Title 18-B statutory text opened during this session (legislature.maine.gov) | Known issue: references an invariant L16 that does not exist. |
| A-012 | Agency coupled with an interest survives the principal's death and cannot be revoked by the principal | NEW | [claimed source](https://www.courtlistener.com/opinion/85384/hunt-v-rousmaniers-administrators/.) | Known issue: in Hunt v. Rousmanier the power was held not coupled with an interest. The survival rule is dictum. |
| C-004 | Federal Vacancies Reform Act's conditional, event-extendable expiry window | L10 | [claimed source](https://www.gao.gov/products/b-323112) |  |
| C-008 | Federal Vacancies Reform Act's first-assistant default: absence of a designation resolves to a specific fallback, not to indeterminate | L7 | [claimed source](https://www.gao.gov/products/gao-02-272r) |  |
| C-013 | Pilot incapacitation: automatic peer succession within a fixed two-person crew | L8, NEW | [claimed source](https://skybrary.aero/articles/pilot-incapacitation) |  |
| C-017 | FAR 117 augmented crew rotation: scheduled, cyclical, ledger-bound authority transfer | NEW | [claimed source](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-117) |  |
| C-020 | Code Blue leadership: ad hoc authority creation with a defined, repeatable hand-off protocol rather than a pre-named holder | NEW | [claimed source](https://icahn.org/wp-content/uploads/2018/10/Policy_2014_RRT_Code_Blue_NEW1.pdf) |  |

### Purpose, exhaustion and changed circumstances

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-008 | Changed circumstances short of death or incapacity can terminate authority | NEW | Search-confirmed summary of Restatement (Third) of Agency S3.09 (2006), cross-referenced against the ALI publication page https://www.ali.org/publications/restatement-law-third/agency | Being rewritten as a machine-checkable purpose exhaustion case. |
| A-031 | A relying party cannot claim protected reliance for staleness alone when no rule makes an old-but-unrevoked instrument expire by age | L10 | Search-confirmed summary of Minnesota Statutes S523.20 and related secondary discussion (aarp.org, nolo.com, farrlawfirm.com) opened via search during this session |  |
| B-016 | Dissolution narrows officer authority to winding-up only | NEW | [claimed source](https://delcode.delaware.gov/title8/c001/sc10/index.html) |  |
| C-030 | Sterile cockpit rule: authority scope as a function of external context rather than of any delegation or revocation event | L10, NEW | [claimed source](https://www.law.cornell.edu/cfr/text/14/121.542) |  |
| A-022 | A temporary administrator pending a will contest holds narrower powers that end the instant the contest resolves | L10, NEW | Secondary legal-reference summaries confirmed during research: https://dictionary.nolo.com/administrator-pendente-lite-term.html and https://lawyermarc.com/estate-planning/special-letters-c-t-a-d-b-n-pendente-lite-other-limited/ |  |

### Office versus person, standing, root succession

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| C-001 | Presidential succession is self-executing, not a granted delegation | NEW | [claimed source](https://constitution.congress.gov/browse/essay/amdt25-1/ALDE_00013871/) |  |
| C-007 | Office-bound delegations survive personnel turnover, person-bound delegations do not | NEW | [claimed source](https://www.justice.gov/file/149056/dl) |  |
| B-004 | Interim officer's narrower mandate does not carry forward the departed officer's full scope | L4 | hypothetical |  |
| B-005 | Compromised CFO: revoke first, accept the gap | L2, L11 | [claimed source](https://www.fincen.gov/resources/statutes-regulations/guidance/advisory-financial-institutions-e-mail-compromise-fraud) |  |
| B-013 | Corporate-law merger vesting does not automatically re-point technical delegation roots | NEW | [claimed source](https://delcode.delaware.gov/title8/c001/sc09/index.html) |  |
| B-015 | Spin-off requires a fresh grant from the new independent entity | L2 | hypothetical |  |
| D-011 | Marriott/Starwood 2014-2018: an acquirer runs the acquired company's legacy, unaudited systems for two years post-close, during which a pre-existing breach goes undiscovered the entire time | NEW | [claimed source](https://www.csoonline.com/article/567795/marriott-data-breach-faq-how-did-it-happen-and-what-was-the-impact.html) |  |

### Vacant or disputed seat

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| C-002 | 25th Amendment Section 4 as a default-holder rule during a live authority dispute | NEW | [claimed source](https://en.wikipedia.org/wiki/Twenty-fifth_Amendment_to_the_United_States_Constitution) | Known issue: the stated default is inverted. Without a two-thirds vote by the deadline the President resumes. |
| C-005 | Whitaker as Acting Attorney General: two valid-looking succession statutes select different actors | NEW | [claimed source](https://constitutioncenter.org/blog/whitakers-acting-attorney-general-appointment-heads-to-court) |  |
| C-026 | Code of Conduct POW succession: automatic rank-based succession that must resolve using only self-attested, unverifiable credentials | NEW | [claimed source](https://en.wikipedia.org/wiki/Code_of_the_United_States_Fighting_Force) |  |

### Authority from outside the chain

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-010 | Appointment of a guardian or conservator can override an existing power of attorney | NEW | Uniform Power of Attorney Act (2006), Article 1 general provisions and state guardianship-code commentary summarized in recordinglaw.com and uslawexplained.com research pages opened during this session |  |
| B-017 | Court-appointed receiver introduces authority from outside the original chain entirely | L2 | [claimed source](https://delcode.delaware.gov/title8/c001/sc10/index.html) |  |

### Retroactivity and ratification

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-021 | A personal representative's authority can relate back to the date of death for beneficial pre-appointment acts | L11, NEW | Search-confirmed secondary summary, Warner Norcross + Judd LLP, https://www.wnj.com/updates/can-a-person-act-on-behalf-of-a-decedents-estate-before-being-appointed-as-personal-representative/ |  |
| A-023 | Ratification retroactively creates authority for a prior unauthorized act, but cannot undo a third party's intervening rights | L3, NEW | Search-confirmed summary of Restatement (Third) of Agency S4.01-4.02 (2006), cross-checked against a PDF excerpt of the section text (jkilborn.weebly.com/uploads/6/4/2/1/64211829/r3d4-01.pdf) |  |
| A-024 | Ratification must cover the entire act, and the ratifying principal must have capacity at the moment of ratifying | NEW | Search-confirmed summary of Restatement (Third) of Agency S4.01-4.07 structural outline (2006) |  |
| B-007 | Ratification validates a past unauthorized act retroactively | NEW | [claimed source](https://www.law.cornell.edu/ucc/3/3-403) |  |
| B-032 | An officer's suspension pending investigation pauses authority without a defined end date | L8 | hypothetical |  |

### Reliance and notice

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-028 | Notice sufficient to cut off apparent authority differs for known prior counterparties versus strangers | NEW | Search-confirmed summary of the common-law differentiated-notice rule (agency.uslegal.com, cpaexamsmastery.com), consistent with the general framing of Restatement (Third) of Agency S3.11's reasonableness standard |  |
| A-029 | A third party accepting a notarized power of attorney in good faith may rely on a presumption of its validity | L7, NEW | Search-confirmed summary of Uniform Power of Attorney Act (2006) S119 (uniformlaws.org, sos.ms.gov hosted copies of the Act, opened via search during this session) |  |
| A-032 | A third party has a duty to inquire when a transaction is inconsistent with the delegation's apparent scope | NEW | General common-law limitation on apparent authority reliance, consistent with the framing in Restatement (Third) of Agency S2.03 and S3.11 as summarized across the sources opened in this session (cpaexamsmastery.com, Wikipedia Apparent authority) |  |
| B-002 | Bank signature card lags the company's own removal of a signatory | NEW | [claimed source](https://www.law.cornell.edu/ucc/4/4-406) | Known issue: UCC 4-406 does not support this. Concept kept, source to be replaced. |
| A-033 | A newer delegation instrument does not automatically revoke an older one absent an express revocation clause | L5 | Reflects standard power-of-attorney drafting practice discussed across multiple secondary estate-planning sources reviewed during research (e.g. willmaker.com's summary of when a power of attorney ends). This is a practice-level default, not a single codified statute cited here. |  |

### Suspension, restriction and release

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| B-010 | Debtor-in-possession status restricts, but does not revoke, officer authority | L8 | [claimed source](https://www.law.cornell.edu/uscode/text/11/1107) |  |
| B-011 | Plan confirmation lifts the debtor-in-possession restriction | L8 | [claimed source](https://www.law.cornell.edu/uscode/text/11/1141) |  |
| B-031 | Chapter 7 trustee, unlike a Chapter 11 debtor in possession, displaces the debtor's own management | L1, L2, L8 | [claimed source](https://www.law.cornell.edu/uscode/text/11/704) |  |
| C-003 | 25th Amendment Section 3 as a reversible self-declared suspension | L8 | [claimed source](https://constitutioncenter.org/blog/understanding-the-constitutions-25th-amendment) |  |
| C-029 | NATO OPCON/TACON: monotonic scope narrowing across a coalition boundary, with nation-imposed caveats layered on top | NEW | [claimed source](https://www.jcs.mil/Portals/36/Documents/Doctrine/fp/authorities_fp.pdf) |  |

### External restriction over a valid chain

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| B-018 | OFAC designation blocks transactions with no corresponding delegation-graph event | NEW | [claimed source](https://ofac.treasury.gov/faqs/topic/1501) |  |
| B-019 | Sanctions delisting removes a block. It does not create new authority | NEW | [claimed source](https://ofac.treasury.gov/faqs/topic/1501) |  |
| B-021 | BIS Entity List restrictions cascade to unlisted affiliates via an ownership fact | NEW | [claimed source](https://www.hklaw.com/en/insights/publications/2025/10/bis-expands-impact-of-us-export-controls-with-50-percent-rule) | Known issue: the BIS affiliates rule was reportedly suspended in November 2025. Status to check. |
| B-027 | Criminal forfeiture ends ownership, it does not just freeze authority to transact | NEW | [claimed source](https://www.law.cornell.edu/uscode/text/18/981) | Known issue: 18 U.S.C. 981 is civil forfeiture, 982 criminal. |
| B-030 | A third party's change-of-control clause can require re-authorization even when the acquirer's own succession is clean | NEW | hypothetical |  |
| F-033 | Transparency-log monitoring uncovers years of mis-issuance, forcing staged mass distrust of an authority | NEW | [claimed source](https://arkadiyt.com/2018/02/04/quantifying-untrusted-symantec-certificates/) |  |

### Concurrence and collective authority

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| B-003 | Dual-control threshold cannot be satisfied by one valid chain | NEW | [claimed source](https://www.federalreserve.gov/frrs/guidance/authentication-and-access-to-financial-institution-services-and-systems-interagency-guidance.htm) |  |
| C-012 | Unified Command under the Incident Command System as designed concurrent authority, contrasted with a silent union of chains | L5, NEW | [claimed source](https://www.fema.gov/emergency-managers/national-preparedness/training/course/100c) |  |
| C-018 | Universal Protocol time-out: unanimous affirmative-confirmation gate before an irreversible action | NEW | [claimed source](https://www.jointcommission.org/en-us/standards/national-performance-goals/right-patient-right-care) |  |
| A-017 | Co-agents can be joint or several, and the default rule changes what a single co-agent may do alone | L5 | Uniform Power of Attorney Act (2006) drafting commentary, confirmed via research summaries opened during this session (uniformlaws.org, recordinglaw.com). State defaults vary and this fixture-relevant point is the default-rule ambiguity itself, not one fixed universal rule. |  |
| A-019 | Co-trustees act by majority when they cannot reach unanimity, and a vacancy need not be filled if trustees remain | NEW | [claimed source](https://legislature.maine.gov/statutes/18-B/title18-Bsec703.html) |  |
| C-025 | NRC control room command: a continuous-coverage requirement with zero tolerance for even momentary gaps | NEW | [claimed source](https://www.nrc.gov/docs/ML0728/ML072831246.pdf) |  |
| C-031 | Compulsory pilotage: a concurrent operational authority that remains unilaterally revocable at any instant by the principal who delegated it | NEW | [claimed source](https://safety4sea.com/what-does-vessel-on-masters-orders-and-pilots-advice-mean/) | Known issue: needs a primary maritime source. |

### Independence and chain selection

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| A-026 | Two valid delegations in different scopes from the same principal to the same agent are not merged into one broader authority | L5 | Applies the Uniform Power of Attorney Act's structural convention of separate financial and healthcare instruments, consistent with the multi-chain independence discussed in draft-pidlisnyi-aps-03 S3.3, REQ-3.3-2, and the sponsor-handover fixture's OLD/NEW/OTHER structure (Agent-Authority-Conformance/aps-conformance-suite, sponsor-handover README, opened during this session) |  |
| E-032 | When a parent holds two independent chains, a spawned child's grant must trace to one explicit chain, not an ambiguous blend | L5 | [claimed source](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/) |  |

### Subdelegation and derivative authority

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| E-006 | Spawning agent needs an explicit separate grant to pass its own authority to a child it creates | NEW | [claimed source](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) |  |
| E-007 | Default service-linked role lets a spawning agent create a child with no explicit pass grant needed | NEW | [claimed source](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) |  |
| A-025 | A subagent's authority is derivative and dies with the appointing agent's authority, but the appointing agent stays answerable for it | L1 | Search-confirmed summary of Restatement (Third) of Agency S3.15 definitional text (2006), cross-checked against course-outline excerpts (opencasebook.org H2O casebook, staff.washington.edu outline) |  |

### Copies of an agent

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| E-004 | fork() semantics: a cloned agent gets a snapshot of parent authority state, then diverges | L2 | [claimed source](https://man7.org/linux/man-pages/man2/fork.2.html) |  |
| E-023 | Checkpoint/restore resumes a process's memory exactly, but its documented model is silent on whether the resumed process's authority context is still valid | NEW | [claimed source](https://criu.org/Main_Page) |  |
| E-025 | Self-replication as METR defines it has no documented authority relationship between an agent and its own copies | NEW | [claimed source](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/) |  |
| E-026 | A self-replicated swarm is modeled as coordinating peers, not a chain of descendants under one root | NEW | [claimed source](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/) |  |
| E-031 | Tiered agent memory is documented for one persistent identity, transferring it to a different agent instance is an unaddressed gap | L11 | [claimed source](https://arxiv.org/abs/2310.08560) |  |
| E-035 | Sticky-session failover to a new backend instance should not be assumed to carry the old instance's in-memory authority context | NEW | hypothetical |  |

### Referent and capability drift

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| E-001 | Rolling model alias silently swaps the model behind a fixed-looking identity | NEW | [claimed source](https://developers.openai.com/api/docs/deprecations) |  |
| E-003 | Model deprecation notice windows differ by tier, so one countdown assumption fails | NEW | [claimed source](https://developers.openai.com/api/docs/deprecations) |  |
| E-005 | Mutable 'latest' tag changes agent runtime with no logged authority-relevant event | NEW | [claimed source](https://docs.docker.com/reference/dockerfile/) |  |
| E-027 | Auto-updated agent extension is disabled until its principal re-consents to newly requested capability | NEW | [claimed source](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings) |  |
| E-008 | Durable workflow instance keeps executing under its starting-time logic, not the deployed-today logic | NEW | [claimed source](https://docs.temporal.io/workflows) |  |
| F-023 | Rolling config update leaves gateway fleet split on which authority policy is current | NEW | hypothetical |  |

### Work in flight

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| B-029 | A payment order in flight has a hard acceptance boundary after which unilateral cancellation stops working | NEW | [claimed source](https://www.law.cornell.edu/ucc/4A/4A-211) |  |
| E-013 | A long job's client-side code must expect authority invalidation to appear silently mid-run | L6 | [claimed source](https://www.rfc-editor.org/rfc/rfc7009) |  |
| E-024 | Warm execution-environment reuse lets background work and open connections from one invocation's authority context bleed into the next | NEW | [claimed source](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) |  |

### Dormant and scheduled work

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| E-014 | Orphaned recurring series outlives the identity that scheduled it, with no central owner left to stop it | NEW | [claimed source](https://learn.microsoft.com/en-us/answers/questions/1098768/recurring-meeting-after-the-owner-mailbox-deleted) |  |
| E-018 | Each new occurrence of a recurring job re-resolves its identity fresh, a running occurrence keeps the one it started with | NEW | [claimed source](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) |  |
| E-020 | Scheduled job's authority is bound to its creator's identity at schedule time, with no documented behavior once that identity is gone | NEW | [claimed source](https://github.com/citusdata/pg_cron) |  |
| E-034 | A queued future action has nothing to pause it if the scheduler never learns about a suspension that starts and ends before the action fires | L8 | hypothetical |  |

### Handover of responsibility and state

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| C-014 | FAA position relief briefing as a two-way acknowledged handover, not a unilateral announcement | NEW | [claimed source](https://www.faa.gov/air_traffic/publications/atpubs/atc_html/) | Known issue: position relief is in FAA JO 7210.3. |
| C-019 | SBAR nursing handoff: transferring accumulated situational state alongside authority, not authority alone | NEW | [claimed source](https://www.nurse.com/nursing-resources/how-to-guides/sbar-communication-technique-in-nursing/) |  |
| C-021 | Navy deck-and-conn transfer: a scripted challenge-response protocol that eliminates handover ambiguity windows | NEW | [claimed source](https://en.wikipedia.org/wiki/Conn_(nautical) |  |
| C-024 | Piper Alpha: shift handover can transfer authority correctly while silently losing the state that authority depends on | NEW | [claimed source](https://www.energyvoice.com/special-features-2/piper-alpha-25/175772/piper-alpha-cullen-report-left-no-stone-unturned/) |  |
| C-027 | Anesthesia handover: authority transfer gated on acknowledged transfer of a cumulative dosing and event record | NEW | [claimed source](https://www.apsf.org/article/the-evidence-base-for-optimal-conduct-of-handoffs/) |  |
| C-028 | Surgeon incapacitation mid-procedure: handover of authority over an action that cannot itself be paused or rolled back | NEW | [claimed source](https://www.jointcommission.org/en-us/standards/national-performance-goals/right-patient-right-care) | Known issue: source is practice, not a Joint Commission standard. |

### Loss of contact and fallback

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| C-010 | NSPD-51/PPD-40 continuity of government devolution triggered by unreachability, not by a declared state | L7 | [claimed source](https://irp.fas.org/offdocs/nspd/nspd-51.htm) |  |
| C-015 | UAS lost-link procedure: automatic fallback to preprogrammed autonomy on loss of principal contact | L7, NEW | [claimed source](https://www.faa.gov/documentlibrary/media/notice/n_8900.227.pdf) |  |
| E-016 | Autonomous fallback authority activates only when round-trip time exceeds the decision window, and only for the pre-scoped action | NEW | [claimed source](https://www.jpl.nasa.gov/news/engineers-investigating-nasas-voyager-1-telemetry-data/) | Known issue: Voyager round trip is about two days. |

### Revocation knowledge and freshness

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| F-001 | OCSP responder unreachable at verification time | L7 | [claimed source](https://datatracker.ietf.org/doc/html/rfc6960) |  |
| F-002 | Revocation mechanism migration leaves old verifiers checking nothing | NEW | [claimed source](https://letsencrypt.org/2024/12/05/ending-ocsp/) |  |
| F-003 | Bundled offline revocation snapshot goes stale between runtime releases | NEW | [claimed source](https://www.imperialviolet.org/2014/02/22/applebug.html) | Known issue: the CRLSet rationale is the 2012 revocation checking post. |
| F-004 | Upstream identity provider outage degrades new issuance, not existing authority | L7 | [claimed source](https://aws.amazon.com/message/12721/) |  |
| F-005 | Revocation resolver overloaded under legitimate load spike | L7 | hypothetical |  |
| F-006 | CRL served past its nextUpdate with no refresh | L7 | [claimed source](https://datatracker.ietf.org/doc/html/rfc5280) |  |
| F-007 | Status list ttl ignored by a long-lived cache | NEW | [claimed source](https://www.w3.org/TR/vc-bitstring-status-list/) |  |
| F-008 | Offline verifier structurally cannot refresh status mid-session | NEW | [claimed source](https://www.w3.org/TR/vc-bitstring-status-list/) |  |
| F-010 | Revocation checking disabled for privacy reasons without a replacement window | NEW | [claimed source](https://letsencrypt.org/2024/12/05/ending-ocsp/) |  |
| F-015 | Revocation answer timestamped in the future relative to the verifier | L7 | [claimed source](https://datatracker.ietf.org/doc/html/rfc6960) |  |
| F-018 | Regional enforcement point serves a stale decision during global propagation delay | NEW | [claimed source](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) |  |
| F-019 | Total partition leaves a gateway unable to reach any authority source | L7 | hypothetical |  |
| F-020 | CDN edge cache serves a stale authorization decision during purge propagation | NEW | [claimed source](https://blog.cloudflare.com/instant-purge/) |  |
| E-015 | Reconnecting offline client reapplies queued actions atop fresh state, not the reverse | L11 | [claimed source](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) |  |

### Ordering, replication and rollback

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| F-016 | Network partition causes authority-store split-brain writes on both sides | NEW | [claimed source](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/) |  |
| F-022 | Last-writer-wins replication silently discards a revocation write | NEW | [claimed source](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html) |  |
| F-024 | Paused lock holder acts after its lock has already been reassigned | NEW | [claimed source](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) |  |
| F-025 | Lock-service bug allows two simultaneous holders of an authority-mutating lock | NEW | [claimed source](https://jepsen.io/analyses/etcd-3.4.3) |  |

### Time

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| F-011 | Fleet-wide client clock bug causes correlated false-invalid authority checks | NEW | [claimed source](https://www.theregister.com/2010/03/02/ps3_psn_access_bug_bypassed/) |  |
| F-013 | Clock-skew rejection of an otherwise-valid delegation artifact | L10 | [claimed source](https://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-admin/Clock-Skew.html) |  |
| F-014 | Issuer time-source spoofing produces artifacts with falsified issuance time | NEW | hypothetical |  |

### Replay of approvals

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| E-009 | An approval delivered as 0-RTT-style early data is not automatically single-use | L6 | [claimed source](https://www.rfc-editor.org/rfc/rfc8446#section-8) |  |
| E-012 | A valid timestamp alone doesn't stop replay, a maintained seen-cache does | L6 | [claimed source](https://www.rfc-editor.org/rfc/rfc4120#section-3.3) | Known issue: replay cache is RFC 4120 section 3.2.3. |

### Issuer and root compromise

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| D-014 | DigiNotar 2011: a compromised root issuer cannot enumerate what it issued during the attack, so per-artifact revocation is impossible and the only remedy is revoking trust in the root itself | L1, NEW | [claimed source](https://threatpost.com/final-report-diginotar-hack-shows-total-compromise-ca-servers-103112/77170/) |  |
| D-033 | Twilio/Authy 2022: an attacker with internal admin access registers new authorized devices onto existing customer accounts rather than stealing credentials directly, and those devices then generate valid-looking ongoing authentication | NEW | [claimed source](https://thehackernews.com/2022/08/twilio-breach-also-compromised-authy-two-factor-accounts.html) |  |
| D-028 | Samsung 2021: a source code leak surfaces thousands of embedded credentials accumulated over years with no existing tracked, rotatable inventory to scope the response against | L12, NEW | [claimed source](https://www.securityweek.com/thousands-secret-keys-found-leaked-samsung-source-code/) | Known issue: the Samsung source leak was March 2022. |

### Exposure as a revocation trigger

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| D-001 | GitHub 2022 OAuth token theft: a compromised third-party integrator, not the resource owner, is the actual point of failure | L1, NEW | [claimed source](https://github.blog/news-insights/company-news/security-alert-stolen-oauth-user-tokens/) |  |
| D-015 | Toyota T-Connect 2017-2022: a subcontractor's accidentally published access key stays live and publicly exposed for five years with no exposure-detection trigger to revoke it | NEW | [claimed source](https://www.bleepingcomputer.com/news/security/toyota-discloses-data-leak-after-access-key-exposed-on-github/) |  |
| D-018 | Salesloft Drift 2025: a chat-widget integration's stolen OAuth tokens become simultaneous attack surface across 700+ downstream orgs, most of whom never re-audited the connected app's scope after initial setup | L1, NEW | [claimed source](https://help.salesforce.com/s/articleView?id=005134951&language=en_US&type=1) |  |

### Evidence and completeness

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| B-023 | A litigation hold suspends routine pruning of authority records | L12 | [claimed source](https://natlawreview.com/article/duty-to-preserve-electronic-evidence) |  |
| F-009 | Status list rollback after a bad publish leaves consumers split | NEW | hypothetical |  |
| F-027 | Audit trail delivery lags behind the enforcement decisions it records | L12 | [claimed source](https://repost.aws/questions/QUdsbji-puTLGizEfUyStfbA/why-does-cloudtrail-take-10-15-minutes-to-log-iam-user-consolelogin-failures) |  |
| F-028 | Teardown completeness gap coincides with the outage that triggered it | L12 | hypothetical |  |
| F-029 | At-least-once notification fan-out both duplicates and silently drops some deliveries | L12 | [claimed source](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) | Known issue: S3 wording unverified. |
| F-034 | Undeclared cascading-revocation policy leaves scope of a revocation ambiguous | L1 | [claimed source](https://www.rfc-editor.org/rfc/rfc7009.html) |  |
| F-035 | Stateless bearer credential cannot be revoked before natural expiry without a blocklist | L8 | hypothetical |  |

### Effects after authority ends

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| D-025 | Coinbase 2025: legitimately-granted outsourced support access, misused via bribery and terminated on detection, still leaves already-exfiltrated data permanently exposed regardless of the termination | NEW | [claimed source](https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists) |  |
| E-021 | Revoking a narrow lookup privilege doesn't erase what an already-open session already looked up with it | L1 | [claimed source](https://www.postgresql.org/docs/current/ddl-priv.html) |  |

### Not yet grouped

| ID | Case | Maps to | Source | Note |
|---|---|---|---|---|
| F-036 | Cache TTL configuration silently drifts longer than the declared freshness limit | NEW | hypothetical |  |
| F-037 | Offline-capable cache serves an authority-bearing view after revocation with no distinction from static assets | NEW | [claimed source](https://web.dev/articles/bfcache) |  |
