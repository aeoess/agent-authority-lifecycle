# Authority Lifecycle: Boundary Cases

Version 0.2.3-draft. Part of the Agent Passport System work. Apache-2.0, same terms as `AUTHORITY-LIFECYCLE.md`.

These are the 36 security and evidence cases that sit next to authority lifecycle without being lifecycle cases. Each one came out of the same research and audit pass as [CASES.md](CASES.md), and each one is sound. What each lacks is a lifecycle verdict: it resolves to a liability outcome, a detection-surface gap, an operational practice or an evidence question, not to an authority state a verifier returns from records (valid, invalid, not established, suspended, restricted, not yet effective).

They are kept because they bound the model. They mark where the authority-lifecycle question stops and a different question starts, and a design that answers them by extending the lifecycle model is probably answering the wrong question.

Entry format matches CASES.md. Some entries are in the shorter reason-plus-source form the survivor pass used for them, rather than the full situation-and-outcome form. IDs are stable and match the ones used in CASES.md and in the research record. Status is **proposed** unless the entry says otherwise. None of the sources says anything about AI agents.

## Contents

- [Fiduciary succession](#fiduciary-succession) (2)
- [Third-party reliance and notice](#third-party-reliance-and-notice) (1)
- [Organization events](#organization-events) (1)
- [Legal and regulatory events](#legal-and-regulatory-events) (1)
- [Root authority and succession](#root-authority-and-succession) (1)
- [Time and scheduling](#time-and-scheduling) (5)
- [Credential events](#credential-events) (19)
- [Agent-side events](#agent-side-events) (2)
- [Infrastructure failure](#infrastructure-failure) (4)

<details>
<summary>All 36 boundary cases</summary>

| ID | Case | Family |
|---|---|---|
| [LC-A-018](#lc-a-018-a-trustee-who-delegates-a-function-still-bears-supervisory-liability-for-the-delegate) | A trustee who delegates a function still bears supervisory liability for the delegate | [Fiduciary succession](#fiduciary-succession) |
| [LC-A-020](#lc-a-020-executor-de-son-tort-acting-as-a-personal-representative-without-appointment-creates-personal-liability-not-authority) | Executor de son tort: acting as a personal representative without appointment creates personal liability, not authority | [Fiduciary succession](#fiduciary-succession) |
| [LC-A-030](#lc-a-030-a-third-party-who-wrongfully-refuses-a-valid-acknowledged-power-of-attorney-can-be-held-liable-subject-to-a-suspected-abuse-safe-harbor) | A third party who wrongfully refuses a valid, acknowledged power of attorney can be held liable, subject to a suspected-abuse safe harbor | [Third-party reliance and notice](#third-party-reliance-and-notice) |
| [LC-B-014](#lc-b-014-successor-liability-doctrine-is-a-liability-outcome-decided-on-facts-outside-the-delegation-graph) | Successor-liability doctrine is a liability outcome decided on facts outside the delegation graph | [Organization events](#organization-events) |
| [LC-B-006](#lc-b-006-a-time-barred-remedy-does-not-cure-the-underlying-lack-of-authority) | A time-barred remedy does not cure the underlying lack of authority | [Legal and regulatory events](#legal-and-regulatory-events) |
| [LC-C-026](#lc-c-026-rank-based-succession-by-self-attestation-has-no-verifier-to-check-it-against) | Rank-based succession by self-attestation has no verifier to check it against | [Root authority and succession](#root-authority-and-succession) |
| [LC-C-024](#lc-c-024-a-shift-handover-can-transfer-authority-correctly-while-silently-losing-the-state-that-authority-depends-on) | A shift handover can transfer authority correctly while silently losing the state that authority depends on | [Time and scheduling](#time-and-scheduling) |
| [LC-C-030](#lc-c-030-a-scope-restriction-tied-to-live-external-context-is-a-policy-question-not-an-authority-lifecycle-transition) | A scope restriction tied to live external context is a policy question, not an authority-lifecycle transition | [Time and scheduling](#time-and-scheduling) |
| [LC-E-017](#lc-e-017-a-recurring-scheduler-needs-an-explicit-named-policy-for-late-and-overlapping-occurrences-not-a-silent-default) | A recurring scheduler needs an explicit, named policy for late and overlapping occurrences, not a silent default | [Time and scheduling](#time-and-scheduling) |
| [LC-E-022](#lc-e-022-a-schedulers-at-least-once-delivery-guarantee-means-the-target-not-the-scheduler-has-to-prevent-duplicate-execution) | A scheduler's at-least-once delivery guarantee means the target, not the scheduler, has to prevent duplicate execution | [Time and scheduling](#time-and-scheduling) |
| [LC-E-030](#lc-e-030-a-recurring-triggers-own-dst-handling-can-skip-or-delay-an-occurrence-with-zero-authority-chain-event-involved) | A recurring trigger's own DST handling can skip or delay an occurrence with zero authority-chain event involved | [Time and scheduling](#time-and-scheduling) |
| [LC-D-002](#lc-d-002-okta-october-2023-a-service-account-credential-leaks-into-a-personal-account-through-an-ordinary-workflow-with-no-anomaly-in-the-credentials-own-usage-logs) | Okta October 2023: a service-account credential leaks into a personal account through an ordinary workflow, with no anomaly in the credential's own usage logs | [Credential events](#credential-events) |
| [LC-D-005](#lc-d-005-slack-december-2022-an-unrelated-vendor-breach-exposes-employee-tokens-for-an-externally-hosted-code-repository-outside-the-orgs-own-iam) | Slack December 2022: an unrelated vendor breach exposes employee tokens for an externally hosted code repository outside the org's own IAM | [Credential events](#credential-events) |
| [LC-D-006](#lc-d-006-ubiquiti-2020-an-engineers-undeclared-intent-to-leave-precedes-any-formal-offboarding-event-by-which-access-could-have-been-narrowed) | Ubiquiti 2020: an engineer's undeclared intent to leave precedes any formal offboarding event by which access could have been narrowed | [Credential events](#credential-events) |
| [LC-D-007](#lc-d-007-desjardins-2017-2019-cumulative-over-extraction-within-an-otherwise-correctly-scoped-unrevoked-grant-undetected-for-26-months) | Desjardins 2017-2019: cumulative over-extraction within an otherwise correctly scoped, unrevoked grant, undetected for 26 months | [Credential events](#credential-events) |
| [LC-D-008](#lc-d-008-twitterzatko-2022-standing-privileged-access-granted-org-wide-with-no-logging-fine-grained-enough-to-attribute-individual-actions) | Twitter/Zatko 2022: standing privileged access granted org-wide with no logging fine-grained enough to attribute individual actions | [Credential events](#credential-events) |
| [LC-D-013](#lc-d-013-lastpass-2022-narrowing-key-custody-to-a-handful-of-named-holders-is-defeated-by-one-holders-unmanaged-personal-device) | LastPass 2022: narrowing key custody to a handful of named holders is defeated by one holder's unmanaged personal device | [Credential events](#credential-events) |
| [LC-D-016](#lc-d-016-juniper-screenos-2012-2015-an-internally-self-consistent-but-substituted-cryptographic-constant-defeats-structural-verification-for-years) | Juniper ScreenOS 2012-2015: an internally self-consistent but substituted cryptographic constant defeats structural verification for years | [Credential events](#credential-events) |
| [LC-D-017](#lc-d-017-codecov-2021-a-stolen-internal-build-credential-lets-an-attacker-silently-modify-a-widely-distributed-script-that-every-downstream-user-trusts-by-source-url-alone) | Codecov 2021: a stolen internal build credential lets an attacker silently modify a widely distributed script that every downstream user trusts by source URL alone | [Credential events](#credential-events) |
| [LC-D-019](#lc-d-019-snowflake-2024-infostealer-harvested-credentials-remain-fully-sufficient-because-the-platform-did-not-enforce-a-second-factor-by-default) | Snowflake 2024: infostealer-harvested credentials remain fully sufficient because the platform did not enforce a second factor by default | [Credential events](#credential-events) |
| [LC-D-020](#lc-d-020-mgm-resorts-2023-a-help-desk-roles-standing-power-to-reset-credentials-over-an-unverified-phone-call-becomes-the-entry-point) | MGM Resorts 2023: a help-desk role's standing power to reset credentials over an unverified phone call becomes the entry point | [Credential events](#credential-events) |
| [LC-D-021](#lc-d-021-godaddy-2020-2022-three-incidents-disclosed-as-separate-events-later-turn-out-to-be-connected) | GoDaddy 2020-2022: three incidents disclosed as separate events later turn out to be connected | [Credential events](#credential-events) |
| [LC-D-022](#lc-d-022-dropbox-2022-a-phishing-page-captures-a-hardware-keys-one-time-code-defeating-a-control-marketed-as-phishing-resistant) | Dropbox 2022: a phishing page captures a hardware key's one-time code, defeating a control marketed as phishing-resistant | [Credential events](#credential-events) |
| [LC-D-023](#lc-d-023-uber-2022-an-admin-credential-hardcoded-in-a-script-on-a-broadly-readable-network-share-becomes-full-administrative-takeover) | Uber 2022: an admin credential hardcoded in a script on a broadly readable network share becomes full administrative takeover | [Credential events](#credential-events) |
| [LC-D-024](#lc-d-024-lapsus-2022-a-revoked-credential-is-simply-replaced-by-another-bought-from-a-criminal-marketplace-faster-than-containment-can-keep-pace) | LAPSUS$ 2022: a revoked credential is simply replaced by another bought from a criminal marketplace, faster than containment can keep pace | [Credential events](#credential-events) |
| [LC-D-026](#lc-d-026-opm-2015-a-contracting-company-disclaims-organizational-responsibility-for-the-scope-of-a-compromised-individual-employees-credential) | OPM 2015: a contracting company disclaims organizational responsibility for the scope of a compromised individual employee's credential | [Credential events](#credential-events) |
| [LC-D-027](#lc-d-027-home-depot-2013-a-narrowly-granted-vendor-credential-reaches-unrelated-systems-because-nothing-enforces-the-boundary-on-paper) | Home Depot 2013: a narrowly granted vendor credential reaches unrelated systems because nothing enforces the boundary on paper | [Credential events](#credential-events) |
| [LC-D-030](#lc-d-030-caesars-2023-attackers-target-an-outsourced-it-support-vendors-own-staff-rather-than-the-orgs-own-employees) | Caesars 2023: attackers target an outsourced IT support vendor's own staff rather than the org's own employees | [Credential events](#credential-events) |
| [LC-D-031](#lc-d-031-beyondtrust-2023-2024-detection-speed-for-a-compromised-credential-varies-by-whether-that-credential-class-has-its-own-tailored-monitoring) | BeyondTrust 2023-2024: detection speed for a compromised credential varies by whether that credential class has its own tailored monitoring | [Credential events](#credential-events) |
| [LC-D-032](#lc-d-032-epamticketmaster-2024-malware-on-a-contractors-laptop-harvests-a-credential-together-with-the-cached-internal-url-needed-to-use-it-against-one-specific-client) | EPAM/Ticketmaster 2024: malware on a contractor's laptop harvests a credential together with the cached internal URL needed to use it against one specific client | [Credential events](#credential-events) |
| [LC-E-010](#lc-e-010-idempotency-key-retry-returns-the-original-result-instead-of-re-executing-the-effect) | Idempotency-key retry returns the original result instead of re-executing the effect | [Agent-side events](#agent-side-events) |
| [LC-E-011](#lc-e-011-a-reused-idempotency-key-with-changed-parameters-errors-outright-rather-than-silently-doing-either-the-old-or-the-new-thing) | A reused idempotency key with changed parameters errors outright, rather than silently doing either the old or the new thing | [Agent-side events](#agent-side-events) |
| [LC-F-021](#lc-f-021-browser-backforward-cache-can-display-a-stale-pre-revocation-authority-view-to-a-human-operator) | Browser back/forward cache can display a stale, pre-revocation authority view to a human operator | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-030](#lc-f-030-a-duplicated-control-flow-statement-can-cause-a-verifier-to-skip-its-own-revocationsignature-check-entirely) | A duplicated control-flow statement can cause a verifier to skip its own revocation/signature check entirely | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-036](#lc-f-036-a-caches-actual-configured-ttl-can-silently-drift-longer-than-its-declared-freshness-policy) | A cache's actual configured TTL can silently drift longer than its declared freshness policy | [Infrastructure failure](#infrastructure-failure) |
| [LC-F-037](#lc-f-037-a-service-worker-offline-cache-can-serve-an-authority-bearing-view-after-revocation-with-no-distinction-from-static-assets) | A service-worker offline cache can serve an authority-bearing view after revocation with no distinction from static assets | [Infrastructure failure](#infrastructure-failure) |

</details>

### Fiduciary succession

#### LC-A-018. A trustee who delegates a function still bears supervisory liability for the delegate

**Situation.** A trustee delegates a duty to an agent rather than performing it personally, and later never reviews the delegate's performance.

**Human analog.** Uniform Trust Code §807, Maine Title 18-B §807, [legislature.maine.gov](https://legislature.maine.gov/statutes/18-B/title18-Bsec807.html): a trustee must "exercise reasonable care, skill and caution in: A. Selecting an agent; B. Establishing the scope and terms of the delegation...; and C. Periodically reviewing the agent's actions." A trustee who complies "is not liable to the beneficiaries or to the trust for an action of the agent."

**What should happen.** The delegate's authority to act is real and independent for execution purposes, but the delegating trustee's own accountability for outcomes does not disappear because a delegate is doing the work.

**What a naive system gets wrong.** Treating "delegation issued, delegate authorized" as the end of the story, with no ongoing accountability model for the delegator.

**Boundary reason.** This resolves to a liability question (does the trustee owe damages for the delegate's conduct), not an authority verdict a verifier returns. The delegation's own validity is untouched either way.

**Status:** proposed, boundary.

---

#### LC-A-020. Executor de son tort: acting as a personal representative without appointment creates personal liability, not authority

**Situation.** A person, without being granted letters of administration, intermeddles with a decedent's estate as though appointed.

**Human analog.** [LegalMatch, "Executor de son tort"](https://www.legalmatch.com/law-library/article/executor-de-son-tort.html): "An executor de son tort is a person who interferes with the administration of a deceased person's estate when they lack the legal authority to do this," and such a person "can be sued as if they were an executor with full legal authority."

**What should happen.** Nothing about this conduct creates valid authority, no matter how long it continues or how beneficial it turns out to be. The actor is personally answerable, distinct from the underlying acts being void.

**What a naive system gets wrong.** Treating "no signed grant found" as purely a validity question, missing that the law layers a personal-liability consequence onto the intermeddler distinct from the invalidity of the acts.

**Boundary reason.** The lifecycle question here (no authority ever existed) is already the ordinary L1-adjacent answer. The doctrine's actual content is a liability consequence for the actor, not a new authority state.

**Status:** proposed, boundary.

---

### Third-party reliance and notice

#### LC-A-030. A third party who wrongfully refuses a valid, acknowledged power of attorney can be held liable, subject to a suspected-abuse safe harbor

**Situation.** A financial institution or other counterparty refuses to honor a power of attorney the presenting agent claims is valid, for reasons of its own policy rather than any defect in the credential.

**Human analog.** Uniform Power of Attorney Act (2006) §120, as enacted at Va. Code §64.2-1618, [law.lis.virginia.gov](https://law.lis.virginia.gov/vacode/title64.2/chapter16/section64.2-1618/): a wrongful refusal is "subject to: A court order mandating acceptance... and liability for reasonable attorney fees and costs." The safe harbor applies where the refusing party "makes...a report to the local adult protective services department...stating a good faith belief that the principal may be subject to physical or financial abuse, neglect, exploitation, or abandonment."

**What should happen.** Refusal to honor a facially valid, properly presented credential is not cost-free. It can create liability for the refusing party unless the refusal falls within the narrow, specifically justified safe harbor, and a generic "we're being cautious" refusal does not qualify.

**What a naive system gets wrong.** A framework that only ever asks "should the verifier accept or reject" treats every rejection as costless and symmetric with acceptance, when the law imposes an asymmetric liability risk on wrongful rejection.

**Boundary reason.** This is a liability consequence for the refusing party, not an authority verdict. The delegation's own validity is not in question.

**Status:** proposed, boundary.

---

### Organization events

#### LC-B-014. Successor-liability doctrine is a liability outcome decided on facts outside the delegation graph

**Reason.** A court can hold an asset buyer liable for a seller's obligations despite an express non-assumption clause, based on operational-continuity facts (same employees, same location, common ownership) that no delegation or grant record captures. This is a liability determination, not an authority-lifecycle verdict.

**Source.** [Taft Law](https://www.taftlaw.com/news-events/law-bulletins/successor-liability-risks-in-asset-purchase-agreements/): the de facto merger exception applies when "the transaction in substance constitutes a merger or consolidation of the buyer and seller."

**Status:** proposed, boundary.

---

### Legal and regulatory events

#### LC-B-006. A time-barred remedy does not cure the underlying lack of authority

**Reason.** The chain's technical invalidity never changes. What expires is only a customer's legal remedy for having relied on it, a liability/remedy outcome rather than an authority verdict a verifier returns.

**Source.** UCC 4-406(f). [Cornell LII](https://www.law.cornell.edu/ucc/4/4-406): "a customer who does not within one year after the statement or items are made available to the customer... is precluded from asserting against the bank the unauthorized signature or alteration."

**Status:** proposed, boundary.

---

### Root authority and succession

#### LC-C-026. Rank-based succession by self-attestation has no verifier to check it against

**Situation.** A group of prisoners of war from different service branches and units, with no communication to outside authority and no way to check anyone's credentials, needs a recognized commander.

**Human analog.** The US Code of Conduct, under which the senior ranking prisoner of war assumes command regardless of service branch. [Wikipedia, Code of the United States Fighting Force](https://en.wikipedia.org/wiki/Code_of_the_United_States_Fighting_Force): "If I am senior, I will take command. If not, I will obey the lawful orders of those appointed over me and will back them up in every way."

**Why boundary, not lifecycle.** The resolution here depends entirely on self-attested claims with no external verifier reachable at all. That fails the decidability bar this corpus applies: there are no records a verifier could check, by design. It is a trust and evidence question adjacent to lifecycle, not a case a verifier could decide.

**Status:** proposed, boundary.

---

### Time and scheduling

#### LC-C-024. A shift handover can transfer authority correctly while silently losing the state that authority depends on

**Situation.** An offshore platform's maintenance crew changes shift while a safety-critical permit-to-work is active. Authority for the resource transfers cleanly to the incoming crew, but a piece of critical state, an active permit, a suspended safeguard, a pending exception, is not part of the transfer protocol and is silently lost.

**Human analog.** The 1988 Piper Alpha disaster and the Cullen Inquiry, which found no written handover procedure existed and the incoming shift was not told a pressure safety valve had been removed under an active permit. [Energy Voice](https://www.energyvoice.com/special-features-2/piper-alpha-25/175772/piper-alpha-cullen-report-left-no-stone-unturned/): "The oncoming shift did not find all of the documents relating to the various maintenance activities."

**Why boundary, not lifecycle.** Nothing about the authority chain itself was invalid at handover. The failure is a loss of situational and safety state alongside a valid transfer, not an authority verdict a verifier could have gotten right or wrong. This is a completeness-of-state problem adjacent to lifecycle, not one inside it.

**Known issue.** Source unreachable at audit. The auditor could not reach the cited page (HTTP 403 direct, bot interstitial through a reader proxy, archive.org unavailable to the tool) and so could not confirm the quoted sentence against the primary source. Its two variants rest on the same unverified source. Status is candidate until a reachable copy of the inquiry findings is verified.

**Status:** candidate, boundary.

Variants: LC-C-019 (SBAR nursing handoff makes the same point as a positive requirement rather than a failure mode: a structured situational record should move with authority at handoff, and the incoming party's accountability should start at acceptance of that record, not at the authority event) and LC-C-027 (anesthesia handover adds measured outcome data: unacknowledged handovers of a cumulative dosing and event record correlate with higher real-world error rates, not just a theoretical gap).

---

#### LC-C-030. A scope restriction tied to live external context is a policy question, not an authority-lifecycle transition

**Situation.** An aircraft's permitted scope of crew activity narrows automatically whenever it descends below 10,000 feet or begins taxi, takeoff, or landing, independent of any principal action, grant, or revocation event, and lifts automatically when the context reverses.

**Human analog.** The sterile cockpit rule, 14 CFR 121.542. [Cornell Law School, Legal Information Institute](https://www.law.cornell.edu/cfr/text/14/121.542): flight crewmembers may not engage in "eating meals, engaging in nonessential conversations within the cockpit and nonessential communications between the cabin and cockpit crews, and reading publications not related to the proper conduct of the flight" during critical phases of flight.

**Why boundary, not lifecycle.** Nothing here is issued, suspended, revoked, or expired. The delegation record never changes, only its situational applicability does, as a function of a continuously fluctuating context variable. That is an authorization-decision and policy-evaluation concern, not a transition in the authority artifact's own lifecycle state.

**Status:** proposed, boundary.

---

#### LC-E-017. A recurring scheduler needs an explicit, named policy for late and overlapping occurrences, not a silent default

**Situation.** A recurring authorized action, such as a nightly reconciliation, is scheduled at fixed intervals. The scheduler's infrastructure experiences delay, so an occurrence is ready to fire well after its intended time, or the previous occurrence is still executing when the next one comes due.

**Human analog.** Kubernetes CronJob's deadline and concurrency fields. [Kubernetes docs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/): "After missing the deadline, the CronJob skips that instance of the Job (future occurrences are still scheduled)." The same page names three distinct concurrency policies, Allow, Forbid, and Replace, as an explicit per-job choice.

**Reason for boundary, not lifecycle.** Even a job whose authority chain is perfectly valid at every check can still misbehave if the scheduler has no policy for lateness or overlap. That is a property of the scheduling layer, not a verdict about delegated authority, so it fails criterion 1.

**Status:** proposed, boundary.

---

#### LC-E-022. A scheduler's at-least-once delivery guarantee means the target, not the scheduler, has to prevent duplicate execution

**Situation.** A recurring authorized action is invoked by a scheduler that only guarantees at-least-once delivery. Under a retry, the target receiving the invocation has no scheduler-provided way to know this is a second delivery attempt for the same logical occurrence.

**Human analog.** AWS EventBridge Scheduler's delivery model. [AWS docs](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html): "EventBridge Scheduler provides at-least-once event delivery to targets, meaning that at least one delivery succeeds with a response from the target."

**Reason for boundary, not lifecycle.** The fix here is target-side deduplication keyed to the occurrence, not a change in any authority state. The scheduler's documented guarantee, not a lifecycle event, is what necessitates it, so this is a scheduler-mechanics case, not an authority verdict.

**Status:** proposed, boundary.

---

#### LC-E-030. A recurring trigger's own DST handling can skip or delay an occurrence with zero authority-chain event involved

**Situation.** A recurring job is scheduled against local wall-clock time. Across a daylight saving transition, the scheduler's own trigger mechanism can misfire relative to the job's intended local time, independent of anything about the delegation backing the job.

**Human analog.** An analysis of Debian cron's documented DST handling. [healthchecks.io](https://blog.healthchecks.io/2021/10/how-debian-cron-handles-dst-transitions/): "If the time has moved backwards by less than 3 hours, those jobs that fall into the repeated time will not be re-run." The same source describes a spring-forward slot that local time skips as a job that runs soon after the change rather than at its intended time. This corrects the original claim of the case, which asserted Debian cron double-fires on fall-back. The documented Debian behavior specifically avoids that, by design, and the actual risk is a skipped or delayed occurrence, not a doubled one.

**Reason for boundary, not lifecycle.** The authority chain backing the action is completely unchanged and verifies identically regardless of the DST bug. This is entirely a trigger-mechanism correctness problem, with no authority state involved to render a verdict about, so it fails criterion 1.

**Status:** proposed, boundary.

---

### Credential events

#### LC-D-002. Okta October 2023: a service-account credential leaks into a personal account through an ordinary workflow, with no anomaly in the credential's own usage logs

**Reason.** The exposure event is a copy into an unmonitored personal channel, invisible to any system that only watches for anomalous use. This is a detection-surface gap, not an authority verdict a verifier returns from records.

**Source.** [Okta root cause report](https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/): "The username and password of the service account had been saved into the employee's personal Google account."

**Status:** proposed, boundary.

---

#### LC-D-005. Slack December 2022: an unrelated vendor breach exposes employee tokens for an externally hosted code repository outside the org's own IAM

**Reason.** The credential lived and was used entirely inside a platform the org's own identity system had no visibility into. A monitoring-coverage gap, not a chain-verification question.

**Source.** [Slack security update](https://slack.com/blog/news/slack-security-update): "a limited number of Slack employee tokens were stolen and misused to gain access to our externally hosted GitHub repository."

**Status:** proposed, boundary.

---

#### LC-D-006. Ubiquiti 2020: an engineer's undeclared intent to leave precedes any formal offboarding event by which access could have been narrowed

**Reason.** Turns on an unrecorded change in a principal's own intent, not a fact any authority record or verifier could observe. A security-monitoring prescription, not a decidable verdict.

**Source.** [CSO Online](https://www.csoonline.com/article/571717/ubiquiti-breach-an-inside-job-says-fbi-and-doj.html): "Nickolas Sharp exploited his access as a trusted insider to steal gigabytes of confidential data from his employer, then, posing as an anonymous hacker, sent the company a nearly $2 million ransom demand."

**Status:** proposed, boundary.

---

#### LC-D-007. Desjardins 2017-2019: cumulative over-extraction within an otherwise correctly scoped, unrevoked grant, undetected for 26 months

**Reason.** A usage-volume and pattern-drift problem inside a grant that stays technically valid throughout. A proportionality-review policy question, not an authority-state verdict.

**Source.** [Office of the Privacy Commissioner of Canada, PIPEDA 2020-005](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2020/pipeda-2020-005/): "Between March 2017 and May 2019, the malicious employee copied this personal information from the shared drive... onto his work computer and then onto USB keys."

**Status:** proposed, boundary.

---

#### LC-D-008. Twitter/Zatko 2022: standing privileged access granted org-wide with no logging fine-grained enough to attribute individual actions

**Reason.** An attribution and logging-architecture precondition for any lifecycle rule to be checkable at all, not itself a lifecycle state.

**Source.** [CBS News](https://www.cbsnews.com/news/twitter-whistleblower-senate-testimony-peiter-zatko/): "Engineers, who make up half of Twitter's employees, can access personal data of any user."

**Status:** proposed, boundary.

---

#### LC-D-013. LastPass 2022: narrowing key custody to a handful of named holders is defeated by one holder's unmanaged personal device

**Reason.** The security posture of a valid holder's own environment, managed device versus personal device, is an operational-security precondition for trusting that holder, not an authority verdict.

**Source.** [The Record](https://therecord.media/lastpass-attacker-hacked-engineers-home-computer-keylogger): "they were able to implant a keylogger on the engineer's device, allowing for constant reconnaissance."

**Status:** proposed, boundary.

---

#### LC-D-016. Juniper ScreenOS 2012-2015: an internally self-consistent but substituted cryptographic constant defeats structural verification for years

**Reason.** Source note: the Rapid7 post itself supports only that unauthorized code created two backdoors, not the specific detail that a single Dual_EC constant was swapped. That more specific claim is sourced separately below. Either way, the integrity of the cryptographic constants the verification math itself relies on is a supply-chain and build-integrity question upstream of chain verification, not a lifecycle-state verdict.

**Source.** [The Register](https://www.theregister.com/2015/12/23/juniper_analysis/): "Whoever tampered with some builds of ScreenOS changed just the value of Q."

**Status:** proposed, boundary.

---

#### LC-D-017. Codecov 2021: a stolen internal build credential lets an attacker silently modify a widely distributed script that every downstream user trusts by source URL alone

**Reason.** Runtime fetch-and-execute integrity of a shared script is a content-trust question, not a delegation-chain verdict.

**Source.** [Codecov security update](https://about.codecov.io/security-update/): "The actor gained access because of an error in Codecov's Docker image creation process that allowed the actor to extract the credential required to modify our Bash Uploader script."

**Status:** proposed, boundary.

---

#### LC-D-019. Snowflake 2024: infostealer-harvested credentials remain fully sufficient because the platform did not enforce a second factor by default

**Reason.** Authentication-factor strength as a platform default is a security-baseline design choice, not a lifecycle state the grant itself carries.

**Source.** [Cloud Security Alliance](https://cloudsecurityalliance.org/blog/2025/05/07/unpacking-the-2024-snowflake-data-breach): "The threat actor used Snowflake account credentials previously stolen via infostealer malware to access customers' Snowflake instances."

**Status:** proposed, boundary.

---

#### LC-D-020. MGM Resorts 2023: a help-desk role's standing power to reset credentials over an unverified phone call becomes the entry point

**Reason.** Whether a reset request was verified strongly enough before being granted is a security-control design question, not an authority-state verdict once the reset itself has already happened.

**Source.** [The Stack](https://www.thestack.technology/mgm-ransomware-attack-social-engineering-linkedin-call/): "All ALPHV ransomware group did to compromise MGM Resorts was hop on LinkedIn, find an employee, then call the Help Desk."

**Status:** proposed, boundary.

---

#### LC-D-021. GoDaddy 2020-2022: three incidents disclosed as separate events later turn out to be connected

**Reason.** Source note: GoDaddy said it believed the incidents were connected as part of a related campaign, which is weaker than proof of one unremediated root cause, and the entry is corrected to that wording. Whether a past closure claim actually held is an audit-reliability question, not a current authority verdict.

**Source.** [The Hacker News, quoting GoDaddy's 10-K](https://thehackernews.com/2023/02/godaddy-discloses-multi-year-security.html): "the December 2022 incident is connected to two other security events it encountered in March 2020 and November 2021."

**Status:** proposed, boundary.

---

#### LC-D-022. Dropbox 2022: a phishing page captures a hardware key's one-time code, defeating a control marketed as phishing-resistant

**Reason.** Source note: distinguish a captured hardware-OTP code, which is what happened here, from a broken FIDO/WebAuthn origin-bound factor, which is a different and stronger failure. Either way this is an authentication-protocol design question, not a lifecycle verdict.

**Source.** [Dropbox.Tech](https://dropbox.tech/security/a-recent-phishing-campaign-targeting-dropbox): "enter their GitHub username and password, and then use their hardware authentication key to pass a One Time Password (OTP) to the malicious site."

**Status:** proposed, boundary.

---

#### LC-D-023. Uber 2022: an admin credential hardcoded in a script on a broadly readable network share becomes full administrative takeover

**Reason.** Whether a credential's storage location matches its privilege level is a secrets-hygiene question, not a chain-verification verdict.

**Source.** [Security Boulevard](https://securityboulevard.com/2022/09/how-uber-was-hacked-in-2022/): "Credentials for the Thycotic PAM were found by a hacker on one of the network shares inside Uber infrastructure in a PowerShell script."

**Status:** proposed, boundary.

---

#### LC-D-024. LAPSUS$ 2022: a revoked credential is simply replaced by another bought from a criminal marketplace, faster than containment can keep pace

**Reason.** Point-revocation versus a structural control change is an incident-response strategy question, not a single decidable authority verdict.

**Source.** [Krebs on Security](https://krebsonsecurity.com/2022/03/a-closer-look-at-the-lapsus-data-extortion-group/): "DEV-0537 advertised that they wanted to buy credentials for their targets to entice employees or contractors to take part in its operation."

**Status:** proposed, boundary.

---

#### LC-D-026. OPM 2015: a contracting company disclaims organizational responsibility for the scope of a compromised individual employee's credential

**Reason.** Whether to trust a contractor's own characterization of an incident's scope is a governance question about an interested reporting party, not an authority-state verdict.

**Source.** [Federal Times](https://www.federaltimes.com/smr/opm-data-breach/2015/06/23/contractor-breach-gave-hackers-keys-to-opm-data/): "While the adversary leveraged a compromised KeyPoint user credential to gain access to OPM's network, we don't have any evidence that would suggest KeyPoint as a company was responsible or directly involved in the intrusion."

**Status:** proposed, boundary.

---

#### LC-D-027. Home Depot 2013: a narrowly granted vendor credential reaches unrelated systems because nothing enforces the boundary on paper

**Reason.** Whether the resource-side network actually enforces segmentation behind a correctly narrow-scoped credential is a network-architecture question, not a verdict the delegation record itself carries.

**Source.** [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/home-depot-breach-third-party/): "did not provide direct access to the company's point-of-sale devices, but the hackers then acquired elevated rights that allowed them to navigate portions of Home Depot's network."

**Status:** proposed, boundary.

---

#### LC-D-030. Caesars 2023: attackers target an outsourced IT support vendor's own staff rather than the org's own employees

**Reason.** Whether an outsourced vendor's workforce is held to the org's own verification standard is a vendor-governance policy question, not an authority-lifecycle verdict.

**Source.** [Caesars Entertainment Form 8-K](https://www.sec.gov/Archives/edgar/data/1590895/000119312523235015/d537840d8k.htm): "suspicious activity in its information technology network resulting from a social engineering attack on an outsourced IT support vendor used by the Company."

**Status:** proposed, boundary.

---

#### LC-D-031. BeyondTrust 2023-2024: detection speed for a compromised credential varies by whether that credential class has its own tailored monitoring

**Reason.** Source note: the underlying jsonl case mis-cited this as a December 2023 event on the October 2023 session-cookie blog post. The compromised API key incident was December 2024, on a different, separate service, and needs its own citation. Detection latency by credential class is a monitoring-architecture design question, not a lifecycle verdict.

**Source.** [Cybersecurity Dive](https://www.cybersecuritydive.com/news/beyondtrust-customers-attacks/736203/): "The attacker compromised a Remote Support SaaS API key and reset passwords of multiple accounts." (API key, detected December 2, 2024.) [BeyondTrust](https://www.beyondtrust.com/blog/entry/okta-support-unit-breach-update) covers the separate October 2023 session-cookie incident referenced for contrast.

**Status:** proposed, boundary.

---

#### LC-D-032. EPAM/Ticketmaster 2024: malware on a contractor's laptop harvests a credential together with the cached internal URL needed to use it against one specific client

**Reason.** Whether cached contextual metadata alongside a stolen credential counts as part of what was "exposed" is an incident-response scoping question, not an authority verdict.

**Source.** [TechTarget](https://www.techtarget.com/searchsecurity/news/366589392/EPAM-denies-link-to-Snowflake-customer-attacks): "a threat actor associated with the ShinyHunters cybercriminal group claimed they compromised an EPAM employee's system with infostealer malware and stole credentials for some Snowflake customer accounts."

**Status:** proposed, boundary.

---

### Agent-side events

#### LC-E-010. Idempotency-key retry returns the original result instead of re-executing the effect

**Situation.** An agent holding a valid, unexpired authorization for a write action loses its connection mid-request and, per its own retry logic, resends the identical request with the same idempotency key attached.

**Human analog.** Stripe's idempotent-requests API. [Stripe docs](https://docs.stripe.com/api/idempotent_requests): "Stripe's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeds or fails."

**Reason for boundary, not lifecycle.** This is about deduplicating the effect of an action across a retried request, not about the validity of the authority behind it. A system can get every authority check right and still double-execute without an idempotency mechanism. No authority state changes here, valid, revoked, suspended, or otherwise, so it fails criterion 1.

**Status:** proposed, boundary.

---

#### LC-E-011. A reused idempotency key with changed parameters errors outright, rather than silently doing either the old or the new thing

**Situation.** An agent's retry logic reuses the idempotency key from an earlier, unrelated request while sending different parameters for a genuinely new action.

**Human analog.** Stripe's idempotent-requests API. [Stripe docs](https://docs.stripe.com/api/idempotent_requests): "The idempotency layer compares incoming parameters to those of the original request and errors if they're not the same to prevent accidental misuse."

**Reason for boundary, not lifecycle.** Like LC-E-010, this is a request-deduplication mechanism, not an authority determination. The error it produces is about parameter mismatch on a reused key, not about whether any grant is valid, revoked, or suspended.

**Status:** proposed, boundary.

---

### Infrastructure failure

#### LC-F-021. Browser back/forward cache can display a stale, pre-revocation authority view to a human operator

**Reason.** This is a client-side presentation-caching problem, not a question a verifier answers. The delegation chain itself is correctly revoked server-side. Only a rendered page shown to a human is stale. Not lifecycle, but adjacent: a human-facing instance of "unknown/stale state is not active" applied to a browser cache rather than a revocation resolver.

**Source verified.** [web.dev, bfcache](https://web.dev/articles/bfcache): "This could potentially expose private data that the user assumed was cleared when they logged out."

**Status:** proposed, boundary.

---

#### LC-F-030. A duplicated control-flow statement can cause a verifier to skip its own revocation/signature check entirely

**Reason.** This is an implementation-correctness and conformance-testing-methodology defect, not a question about what authority state should be. The model already requires revoked chains to fail. This is about proving an implementation actually executes that check on every code path.

**Source verified.** [imperialviolet.org, on Apple's "goto fail" bug](https://www.imperialviolet.org/2014/02/22/applebug.html): "The code will always jump to the end from that second goto... and so the signature verification will never fail."

**Status:** proposed, boundary.

---

#### LC-F-036. A cache's actual configured TTL can silently drift longer than its declared freshness policy

**Reason.** This is an operational configuration-drift monitoring problem (does the running system match its own declared policy), not a question about correct lifecycle behavior. Hypothetical: no incident is cited, and the source field in the underlying research record is null.

**Status:** proposed, boundary.

---

#### LC-F-037. A service-worker offline cache can serve an authority-bearing view after revocation with no distinction from static assets

**Reason.** Same category as LC-F-021, one layer down: an offline-capable web app's own cache rather than the browser's bfcache. Not a verifier lifecycle question.

**Source verified.** [web.dev, bfcache](https://web.dev/articles/bfcache): same general caching-invalidation guidance (evict or revalidate authority-bearing responses on cache restore), applied to a different caching layer.

**Status:** proposed, boundary.

---
