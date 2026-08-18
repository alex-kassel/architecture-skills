# Deprecate and remove client adapters strategy and documentation references

- Status: verified
- Skill: maintain-architecture-skills
- Skill commit: `b80c13757b453586aee75f9109d2f98d570ee00a`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md`, `skills/maintain-architecture-skills/SKILL.md`, `scripts/adapters/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner decided to abandon the client adapters strategy (`scripts/adapters/`), requesting the complete deletion of adapter scripts and the removal of all operational references from `AGENTS.md` and `skills/maintain-architecture-skills/SKILL.md`.

## Skill instruction involved

`AGENTS.md` (Intent & Workflow Routing table) and `skills/maintain-architecture-skills/SKILL.md` (Step 5: Deterministic Guardrails & Adapter Sync Verification).

## Observed behavior and impact

Deleting the `scripts/adapters/` directory while keeping adapter references in `AGENTS.md` and `SKILL.md` creates documentation drift and broken script execution paths. Removing all references aligns operational instructions with the actual repository state.

## Session disposition

Owner explicitly instructed removing all mentions of client adapters and updating repository documentation.

## Proposed improvement

1. Remove `scripts/adapters/` directory and scripts.
2. Remove `INSTALL_ADAPTER` workflow routing entry from `AGENTS.md`.
3. Update `skills/maintain-architecture-skills/SKILL.md` to remove the adapter sync verification step.

## Developer Community Best Practice Evaluation

Eliminating unused infrastructure and keeping routing tables/skill protocols strictly synchronized with available scripts prevents command failures and maintains documentation integrity.

## Triage and resolution

Accepted and approved by owner on 2026-08-18. Implemented by removing `scripts/adapters/` and cleaning up references in `AGENTS.md` and `skills/maintain-architecture-skills/SKILL.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
