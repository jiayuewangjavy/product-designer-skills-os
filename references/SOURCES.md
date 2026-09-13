# Source and integration manifest

Snapshot verified: 2026-09-13. No third-party source is vendored in this v0. Commits below identify the versions reviewed as method references; they are not runtime dependencies.

| Package skill | Method source | Integration mode | v0 status |
|---|---|---|---|
| `opportunity-and-assumption-map` | `phuryn/pm-skills`; compared with `deanpeters/Product-Manager-Skills` and `product-on-purpose/pm-skills` | clean-room adapter around shared evidence contract | implemented locally; no external runtime dependency |
| `conceptual-model-design` | `jiayuewangjavy/conceptual-model-design-skill` and the Vault demo source | user-owned skill adapted to loop contract | implemented locally |
| `prototype-question` | `helderberto/agent-skills` prototype method; `deanpeters/Product-Manager-Skills` prototype probes | clean-room synthesis | implemented locally |
| `interactive-prototype` | `plannotator/effective-html` | tool-agnostic adapter; no copied code | implemented locally; no engine dependency |
| `position-and-launch-hypothesis` | `coreyhaines31/marketingskills` | clean-room adapter around shared context | implemented locally; no external runtime dependency |
| `product-context`, `product-design-router`, `design-judgment-scorecard`, `intent-preservation-check`, `learning-loop-readout` | Product Designer Skills OS | original | implemented locally |

## Reviewed source snapshots

| Repository | Reviewed commit | License signal | Distribution boundary |
|---|---|---|---|
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills/tree/18468a95b427e70e258b51389796367c6f684e7d) | `18468a95b427e70e258b51389796367c6f684e7d` | MIT | method reference; no code copied |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/tree/1b5a524ebb95e9497fa3f25002d8b8ec528d4444) | `1b5a524ebb95e9497fa3f25002d8b8ec528d4444` | CC BY-NC-SA 4.0 text; GitHub API reports no SPDX match | research reference only |
| [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills/tree/1cef1a9eae10017389863d51e289e0ae41e17fcb) | `1cef1a9eae10017389863d51e289e0ae41e17fcb` | Apache-2.0 | method reference; no code copied |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/5b2c0007766c6a1cf1d53fd8fc73e979e0821022) | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | MIT | method reference; no code copied |
| [plannotator/effective-html](https://github.com/plannotator/effective-html/tree/d95debbaef15af1d201fc6c10c77cf92b524a0d6) | `d95debbaef15af1d201fc6c10c77cf92b524a0d6` | MIT | method reference; no code copied |
| [helderberto/agent-skills](https://github.com/helderberto/agent-skills/tree/deceebdd5d9706edc8d75d088a13f3a1f0c4fac5) | `deceebdd5d9706edc8d75d088a13f3a1f0c4fac5` | MIT | method reference; no code copied |
| [mary13/pair-design-agent-skill](https://github.com/mary13/pair-design-agent-skill/tree/bbdf98a0aea0126b0e9badabe22ac6f96ef7c869) | `bbdf98a0aea0126b0e9badabe22ac6f96ef7c869` | no license file found | research reference only; do not copy |
| [jiayuewangjavy/conceptual-model-design-skill](https://github.com/jiayuewangjavy/conceptual-model-design-skill/tree/78be2a3cac7e87a2723da381ea23b0c543dc60e5) | `78be2a3cac7e87a2723da381ea23b0c543dc60e5` | MIT | user-owned source adapted locally |

## 2026 process evidence

These sources inform the process model and Router design. They are evidence and product-practice references, not copied implementations or proof that this V0 improves product outcomes.

| Source | 2026 signal used | Design implication | Evidence boundary |
|---|---|---|---|
| [Figma 2026 AI Report](https://www.figma.com/blog/2026-ai-report/) | 8,403 survey responses and 639 qualitative interviews; 41% report AI changing teamwork; designers participating in development and developers doing design both increased | Role overlap and multiplayer collaboration require explicit decision ownership, not artifact-based handoff | Vendor research; useful scale and direction, not causal proof |
| [Figma: 4 new ways to go from idea to product](https://www.figma.com/blog/4-new-ways-to-go-from-idea-to-product-with-ai-tools/) | Documents code → canvas → code, prototype-first, team-review, and design-system-grounded workflows | Router may enter from any artifact and should select the surface that exposes the current unknown | Product examples selected by Figma; not a neutral benchmark |
| [Figma: What the design-to-code loop unlocks](https://www.figma.com/blog/what-the-design-to-code-loop-unlocks/) | Describes a roundtrip between production states, canvas, and code | Making is a loop across surfaces; context and intent must survive the roundtrip | Practitioner and product-team account |
| [Google Labs: Introducing vibe design with Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/) | Allows entry from business goals, text, images, or code; supports parallel exploration and rapid interactive refinement | Entry point and artifact order are dynamic; a shared surface can accelerate feedback | Product announcement; speed and capability are not validation evidence |
| [Microsoft Research: New Future of Work 2026](https://www.microsoft.com/en-us/research/blog/new-future-of-work-ai-is-driving-rapid-change-uneven-benefits/) | Synthesizes research on AI changing collaboration and shifting people toward guiding, critiquing, and improving AI output | Human / AI authority and oversight belong in the shared operating state | Broad workplace synthesis, not product-design-specific causal evidence |
| [Microsoft Research: Scaffolding Human-AI Collaboration](https://www.microsoft.com/en-us/research/publication/human-ai-collaboration-field-experiment/) | Field experiment with 388 employees found that one rigid behavioral protocol reduced document quality and production, while effects varied by intervention | Do not replace an old fixed process with a universal AI protocol; adapt structure to the decision and uncertainty | April 2026 arXiv preprint with stated design limitations; not direct validation of this Router |

## License boundary

- MIT and Apache-2.0 sources may become explicit dependencies or attributed adapters after a separate implementation and notice review.
- CC BY-NC-SA material remains research/reference only unless distribution and commercial-use implications are explicitly accepted.
- Unlicensed repositories remain research/reference only and contribute no copied implementation.
- GitHub stars and install counts are discovery signals, not quality or license approval.
