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

## License boundary

- MIT and Apache-2.0 sources may become explicit dependencies or attributed adapters after a separate implementation and notice review.
- CC BY-NC-SA material remains research/reference only unless distribution and commercial-use implications are explicitly accepted.
- Unlicensed repositories remain research/reference only and contribute no copied implementation.
- GitHub stars and install counts are discovery signals, not quality or license approval.
