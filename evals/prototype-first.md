# Eval: prototype-first routing

## User request

> We already have a runnable AI meeting-summary prototype. Test users say the summary feels generic, but the team wants to redesign the dashboard immediately. What should we do next?

## Context available

- A runnable prototype exists.
- The product promise is to turn meetings into actionable follow-up.
- “Generic” is a reported reaction, but raw observations and participant context are not yet available.
- The team has not stated whether the problem comes from the summary model, information structure, wording, missing controls, or participant expectations.

## Expected routing invariants

- Do not restart mechanically at broad discovery.
- Do not immediately build a redesigned dashboard.
- Identify the missing interpretation of user evidence as the highest-risk unknown.
- Route first to `learning-loop-readout` to separate observation from interpretation and determine what the feedback can support.
- Route secondarily to `conceptual-model-design` only if the readout shows confusion about objects, actions, states, or the relationship between summaries and follow-up tasks.
- Use `prototype-question` only after the target uncertainty is explicit.
- Define an exit condition that can support, reject, or reframe the proposed redesign.

## Failure conditions

- Produces a lifecycle checklist.
- Treats “generic” as a confirmed interface problem.
- Recommends visual polish without evidence.
- Invokes every installed skill.
- Claims the prototype has been validated merely because users saw it.
