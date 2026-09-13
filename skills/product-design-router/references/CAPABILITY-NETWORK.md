# Capability network

Use this reference when more than one uncertainty node is plausible.

| Unknown node | Diagnostic question | Typical atomic skills | Useful evidence |
|---|---|---|---|
| Value | Are we solving a meaningful problem for the right user or buyer? | `opportunity-and-assumption-map` | observed behavior, interviews, alternatives, demand signals |
| Meaning & Structure | Can the product be understood as a coherent system? | `conceptual-model-design` | object relationships, task language, breakdowns, edge states |
| Experience & Judgment | Can people understand, control, and complete the task at the intended quality? | `prototype-question`, `interactive-prototype`, `design-judgment-scorecard` | task behavior, comparison, errors, comprehension, quality criteria |
| Feasibility & Reliability | Can it be built and operated within real constraints? | feasibility review, design-to-code, QA, recovery, performance | technical spikes, tests, incidents, constraints, acceptance criteria |
| Adoption & Market | Will the right people discover, choose, activate, and continue using it? | `position-and-launch-hypothesis` | conversion, activation, willingness to pay, cohorts, churn reasons |
| Learning & Governance | Can signals be interpreted and safely change the next decision? | `learning-loop-readout`, `intent-preservation-check`, plus context and decision records | provenance, metric definitions, contradictions, version diffs, owners |

## Loop patterns

- `Direction`: signal → frame → choose a bet. Use when the central uncertainty is value or strategic direction.
- `Making`: model ↔ prototype ↔ build ↔ evaluate. Use when an artifact is the fastest way to expose meaning, experience, or feasibility risk.
- `Learning`: ship ↔ observe ↔ interpret ↔ adapt. Use when real-world behavior exists but has not yet changed product context or decisions.

Loops may nest or jump nodes. Select the fewest skills that can produce decision-changing evidence.
