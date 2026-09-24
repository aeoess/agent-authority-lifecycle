# Agent Authority Lifecycle

What happens to an AI agent's authority when people, keys, approvals and roles change around it.

An agent can outlive the employee who sponsored it, the key it signed with and the approval that let it act. This repository describes which parts of its authority survive those changes, which must stop, how replacement authority is established, and what evidence establishes each step. Each statement is marked as specified, tested, candidate, implemented, proposed or open, and tested statements link to a runnable case in the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite.

In short, an agent can survive a personnel change and its old authority does not.

## Contents

Read in this order.

1. [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md), the model: the concepts it keeps separate, the verification model naming what a verifier may say, and the published L1 to L12 invariants.
2. [CASES.md](CASES.md), the situations that test the model, verified, reviewed hypothetical and candidate, each with a stable id.
3. [INVARIANT-CANDIDATES.md](INVARIANT-CANDIDATES.md), proposed invariants that are not in the published L series, each with what it does not claim, the cases that force it and the strongest counterexample.
4. [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md), what is not answered yet, each question linked to the cases, candidates and fixtures that bear on it.
5. [BOUNDARY-CASES.md](BOUNDARY-CASES.md), sound security and evidence cases that are not authority-lifecycle cases, grouped by why each is out of scope.
6. [cases.json](cases.json), the same cases in machine-readable form, validated by [schema/cases.schema.json](schema/cases.schema.json) and [scripts/validate_cases.py](scripts/validate_cases.py), with each case's `fixtures` array naming the fixture family, vector ids and SDK results the lab wave produced for it.
7. [SUPERSEDED.md](SUPERSEDED.md), designs we replaced and why.

## Versioning

Releases version the whole repository, so every document carries the same line, and git history tracks each file.

## Relationship to the Agent Passport System

This work comes out of the [Agent Passport System](https://github.com/aeoess/agent-passport-system), an open protocol for AI agent identity, delegation and signed receipts. The invariants are written to be implementable outside APS, and the conformance cases state which specification text they test.

## Contributing

Corrections, counterexamples and new cases are welcome through issues and pull requests. A proposed invariant is most useful with a failure mode, and a claimed one with a runnable case.

## License and citation

Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). To cite, see [CITATION.cff](CITATION.cff).
