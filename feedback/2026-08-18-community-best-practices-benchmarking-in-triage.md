# Mandatory developer community best practice evaluation in feedback triage

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `c:\Users\Alex\codex-architecture-skills`
- Source program: `AGENTS.md` & `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed that whenever owner additions, workflow proposals, or feedback items are captured and presented for triage approval, the agent MUST ALWAYS evaluate the proposal against developer community best practices and established software architecture design patterns.

If a proposal contradicts or deviates from widely accepted developer community standards, the agent must explicitly highlight this deviation when presenting the feedback for owner approval, accompanying the triage presentation with an expert community-backed recommendation.

## Skill instruction involved

1. `AGENTS.md` skill maintenance workflow rules, feedback triage protocols, and triage presentation guidelines.
2. `feedback/TEMPLATE.md` and feedback evaluation rules.

## Observed behavior and impact

Presenting feedback proposals without explicit benchmarking against developer community best practices risks adopting non-standard, fragile, or anti-pattern workflows without the owner being aware of industry trade-offs.

## Session disposition

Owner explicitly directed:
1. Every feedback proposal must be benchmarked against developer community best practices.
2. Any non-standard behavior or deviation from industry standards must be explicitly highlighted during triage presentation.
3. Every triage proposal must include an expert community-backed recommendation.

## Proposed improvement

1. Update `AGENTS.md` skill maintenance rules and `feedback/TEMPLATE.md` to mandate a `Developer Community Best Practice Evaluation` section in feedback records.
2. Require agents to include an expert community recommendation whenever presenting feedback records to the owner for triage approval (`accepted`/`rejected`/`superseded`).

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `AGENTS.md` and `feedback/TEMPLATE.md` by requiring every feedback proposal to be evaluated against developer community standards and presented with explicit trade-off analyses and expert community-backed recommendations during owner triage.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 39 (`codex-guide-community-best-practices-triage-20260818`).
