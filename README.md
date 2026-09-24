# Agent Authority Lifecycle

What happens to an AI agent's authority when people, keys, approvals and roles change around it.

An agent can outlive the employee who sponsored it, the key it signed with and the approval that let it act. This repository describes which parts of its authority survive those changes, which must stop, how replacement authority is established, and what evidence proves each step. Each statement is marked as specified, tested, candidate, implemented, proposed or open, and tested statements link to a runnable case in the [Agent Authority Conformance](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) suite.

In short, an agent can survive a personnel change and its old authority does not.

## Contents

- [AUTHORITY-LIFECYCLE.md](AUTHORITY-LIFECYCLE.md), the model and its invariants
- [CASES.md](CASES.md), situations that test the model, verified and candidate
- [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md), what is not answered yet
- [SUPERSEDED.md](SUPERSEDED.md), designs we replaced and why

## Relationship to the Agent Passport System

This work comes out of the [Agent Passport System](https://github.com/aeoess/agent-passport-system), an open protocol for AI agent identity, delegation and signed receipts. The invariants are written to be implementable outside APS, and the conformance cases state which specification text they test.

## Contributing

Corrections, counterexamples and new cases are welcome through issues and pull requests. A proposed invariant is most useful with a failure mode, and a claimed one with a runnable case.

## License and citation

Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). To cite, see [CITATION.cff](CITATION.cff).
