# Product Designer Skills OS

An open-source capability network for product designers and independent product builders working with AI.

![A rigid stage pipeline being knitted into Direction, Making, and Learning loops](assets/dynamic-learning-network.png)

AI makes artifacts cheaper. It does not remove the need to understand a problem, model a product, judge an experience, validate behavior, earn adoption, or learn from evidence. This package routes work by the **highest-risk unknown**, rather than forcing every project through a fixed design lifecycle.

## How it works

```text
             Direction Loop
      Signals ↔ Frame ↔ Choose a Bet
           ↙                 ↘
Making Loop ↔ shared context ↔ Learning Loop
Model ↔ Prototype ↔ Build      Ship ↔ Observe ↔ Adapt
```

`product-design-router` inspects the artifacts that already exist, identifies the unknown most likely to cause failure or expensive rework, and recommends the smallest useful skill loop. Every loop shares a traceable evidence and decision contract.

## Included skills

| Network role | Skill | Purpose |
|---|---|---|
| Control | `product-design-router` | Route by uncertainty and define an exit condition |
| Shared context | `product-context` | Preserve evidence, assumptions, decisions, and constraints |
| Direction | `opportunity-and-assumption-map` | Find the riskiest belief behind a product bet |
| Structure | `conceptual-model-design` | Model roles, objects, relationships, states, and rules |
| Evidence design | `prototype-question` | Define what a prototype must prove and when to stop |
| Making | `interactive-prototype` | Build the minimum runnable interaction needed for evidence |
| Evaluation | `design-judgment-scorecard` | Turn design judgment into explainable findings and tradeoffs |
| Intent governance | `intent-preservation-check` | Detect when AI-generated revisions erase confirmed intent |
| Adoption | `position-and-launch-hypothesis` | Connect positioning and launch to measurable behavior |
| Learning | `learning-loop-readout` | Convert product signals into context and decision updates |

## Profiles

- `profiles/designer-core.md`: emphasizes product structure, experience, and judgment.
- `profiles/builder-core.md`: emphasizes value, feasibility, adoption, and learning.
- `profiles/full-collection.md`: all implemented nodes; it is not a required sequence.

## Install

Clone this repository, then copy only the skill folders you want from `skills/` into your Codex skills directory. To use the full network, install `product-design-router` plus the skills listed in the desired profile.

Restart Codex after installation. Invoke the router with:

```text
Use $product-design-router to identify the highest-risk unknown in this product work and recommend the smallest skill loop.
```

The skills contain no bundled third-party code, install scripts, network calls, or secret handling.

## Contracts and provenance

- `references/LOOP-CONTRACT.md` defines the shared `knew → made → learned → changed → next unknown` handoff.
- `references/SOURCES.md` records method influences, pinned review commits, license boundaries, and integration status.
- `evals/prototype-first.md` is the first behavior-level routing case.

## Project status

This is a working v0, not a finished universal design curriculum. Static package validation passes. Real-task evaluation is still required before claiming that the network improves product outcomes or reduces rework.

## License

Original package content is released under the MIT License. Third-party sources listed in `references/SOURCES.md` retain their own licenses; no third-party implementation is vendored here.
