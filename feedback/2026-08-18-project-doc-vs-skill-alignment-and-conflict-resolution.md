# Preflight audit of project documentation against skills and conflict resolution

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `<project-root>`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner highlighted that consuming software architecture projects maintain a hierarchy of documentation (`AGENTS.md`, project roadmaps, program specs) alongside installed reusable skills. Currently, agents lack an explicit preflight instruction at session startup to audit project documentation for duplication or contradiction with installed skills.

When local project documentation duplicates or contradicts reusable skill rules, the agent must immediately raise the issue for owner discussion before proceeding, presenting two clear paths with a reasoned recommendation:
- **Option A (Align Project Docs):** Update/clean project documentation to match the skill (eliminate duplication, rephrase conflicting local text).
- **Option B (Create Skill Feedback):** Capture a feedback record for the skill if the project's local rule is superior or intentionally overrides the skill.

## Skill instruction involved

1. `guide-architecture-design/SKILL.md` & `references/operating-contract.md` (Authority by concern and surface reusable-workflow feedback rules).
2. `guide-architecture-design/references/workflow-modes.md` (`INTENT_PREFLIGHT` and `SESSION_BINDING` transitions).

## Observed behavior and impact

Without an explicit startup alignment check, agents may operate under contradictory or duplicated documentation, leading to instruction drift, duplicate rules in project docs, or silent bypass of skill improvements.

## Session disposition

Owner explicitly requested standardizing a mandatory startup alignment check between local project documentation and reusable skills, with immediate owner discussion and agent recommendation upon detecting conflicts or duplication.

## Proposed improvement

1. Update `guide-architecture-design` (`INTENT_PREFLIGHT` / `SESSION_BINDING` & `operating-contract.md`) to require auditing local project documentation against installed skills upon session startup.
2. If duplication or contradiction is detected, pause and present an immediate conflict resolution item with agent recommendation (Option A vs Option B) before continuing design operations.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `guide-architecture-design/references/workflow-modes.md` (`INTENT_PREFLIGHT`) and `operating-contract.md` by requiring a mandatory preflight audit of local project documentation against installed skills upon session startup, and presenting conflict resolution options (Option A: align project docs vs Option B: create skill feedback) with an expert community-backed recommendation when conflicts or duplication occur.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 38 (`codex-guide-project-doc-vs-skill-alignment-20260818`).
