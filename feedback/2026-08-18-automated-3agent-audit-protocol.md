# Automated 3-Agent 3-Block Audit Protocol Trigger and Workflow

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested an automated end-to-end audit protocol where issuing a short trigger command ("Проведи аудит" / "Start audit") autonomously initializes 3 audit files with pre-filled prompts (Block 1), launches 3 concurrent independent subagents to conduct audits and write findings (Block 2), compiles triage proposals for owner approval, and documents implementation results in Block 3 upon approval.

## Skill instruction involved

`AGENTS.md` skill maintenance triggers section and `audits/README.md`.

## Observed behavior and impact

Manually invoking subagents and constructing audit files requires user prompt orchestration on every audit run. Automating this protocol under a single trigger phrase enables seamless 3-way auditing (Formal Verification, Architecture/DX, Adversarial Chaos) with zero manual friction.

## Session disposition

Not required. Non-blocking workflow refinement.

## Proposed improvement

1. Register `Проведи аудит` and `Start audit` as first-class triggers in `AGENTS.md`.
2. Standardize 4-phase execution: Phase 1 (Create 3 audit files with prompts in Block 1), Phase 2 (Launch 3 concurrent subagents to write Block 2), Phase 3 (Present consolidated Triage Matrix to owner), Phase 4 (Implement accepted fixes, validate, and write Block 3 upon owner `+` confirmation).
3. Document protocol in `audits/README.md`.

## Developer Community Best Practice Evaluation

Autonomous multi-agent orchestration for multi-perspective code and architecture audits ensures continuous verification, eliminates bias from single-agent audits, and provides durable audit provenance.

## Triage and resolution

Accepted by owner. Implemented in `AGENTS.md` and `audits/README.md`.

## Verification

Verified by trigger registration in `AGENTS.md` and protocol documentation in `audits/README.md`.
