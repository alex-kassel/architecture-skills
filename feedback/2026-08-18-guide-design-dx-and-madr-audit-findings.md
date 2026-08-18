# Developer Experience (DX), MADR standardization, and vendor abstraction in guide-architecture-design

- Status: verified
- Skill: guide-architecture-design
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `c:\Users\Alex\codex-architecture-skills`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

An independent Architecture & DX audit identified friction points, vendor lock-in (`gh` CLI hardcode), context leaks (`spider-one` placeholders), and missing ADR standardization (MADR format with Frontmatter).

## Skill instruction involved

`references/decision-capture-and-sync.md`, `references/gates-recovery-and-git.md`, `references/operating-contract.md`, `references/workflow-modes.md`.

## Observed behavior and impact

Developers experience "confirmation fatigue" due to paranoid global preflights on untracked root files, rigid 3-attempt pushbacks, strict single-question interview rules, and excessive worklog micro-timestamping.

## Session disposition

Not required. Non-blocking audit observation.

## Proposed improvement

1. Introduce standardized MADR (Markdown Architecture Decision Record) template with YAML Frontmatter.
2. Scope preflights to architectural documentation paths (`docs/**`, `architecture/**`, decision logs).
3. Limit pushback to 1 well-reasoned warning upon risk detection, then accept owner decision.
4. Allow 2-3 tightly linked questions per turn during design interviews.
5. Abstract CLI tools (`gh` / `glab` / local git PR workflows).
6. Remove legacy placeholders (`spider-one`).

## Developer Community Best Practice Evaluation

MADR is the industry standard for Doc-as-Code. Scoping preflights and reducing confirmation fatigue aligns with developer-centric AI tooling design patterns.

## Triage and resolution

Accepted by owner. Implemented in `decision-capture-and-sync.md`, `gates-recovery-and-git.md`, `operating-contract.md`, and `workflow-modes.md`.

## Verification

Verified in `evals/forward-tests.md` scenarios 44 and 45.
