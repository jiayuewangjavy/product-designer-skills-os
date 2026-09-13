---
name: product-design-router
description: Diagnose the highest-risk unknown in product design or independent product-building work and compose the smallest useful skill loop. Use when the user is unsure what product/design work should happen next, has mixed artifacts from different stages, or wants to avoid mechanically following a lifecycle. Do not use to replace a clearly requested specialist skill.
---

# Product Design Router

Route by uncertainty, not by lifecycle stage.

## Start from what exists

Inspect the supplied brief, research, prototype, code, analytics, feedback, constraints, and decision records. Do not require discovery artifacts merely because they traditionally come first. If the user has already named a concrete specialist task, preserve that intent and invoke that skill directly unless a missing decision would make the work misleading or unsafe.

## Diagnose the decision

1. Name the product decision the user is trying to make.
2. Separate known evidence, inference, assumption, preference, and confirmed decision.
3. Identify the unknown most likely to cause failure or expensive rework:
   - `Value`: wrong user, buyer, problem, outcome, or alternative;
   - `Meaning & Structure`: incoherent objects, relationships, states, rules, IA, or permissions;
   - `Experience & Judgment`: unclear interaction, content, usability, accessibility, or quality bar;
   - `Feasibility & Reliability`: implementation, performance, safety, recovery, or operational risk;
   - `Adoption & Market`: weak positioning, channel, activation, pricing, retention, or distribution;
   - `Learning & Governance`: missing instrumentation, interpretation, provenance, approval, or decision memory.
4. Prefer the unknown whose answer would most change the product, not the one with the easiest artifact.
5. Propose the smallest loop that can produce credible evidence. Usually select one primary skill and at most two supporting skills.
6. Define an exit condition: what evidence would support, reject, or reframe the current decision.

Use [references/CAPABILITY-NETWORK.md](references/CAPABILITY-NETWORK.md) only when choosing among multiple nodes or composing a cross-node loop.

## Output

```markdown
## Decision now

## Highest-risk unknown
- Node:
- Why now:
- Evidence already available:
- Missing evidence:

## Smallest useful loop
1. Primary skill — question it should answer
2. Optional supporting skill — only if required

## Exit condition

## After the loop
- Update:
- Next unknown, if any:
```

## Boundaries

- Do not present a complete skill catalog when one next action is enough.
- Do not treat a polished PRD, mock, prototype, or codebase as proof that upstream decisions are settled.
- Do not invent research, analytics, constraints, or user consent.
- Do not optimize for artifact completion; optimize for evidence that can change a decision.
- High-risk legal, medical, financial, security, privacy, or irreversible decisions require the relevant specialist review and human approval.
- Designer and Builder profiles adjust default emphasis only; they never force a fixed sequence.

The route is complete when the user can see why this unknown matters now, which minimal capability to invoke, and what new evidence will end the loop.
