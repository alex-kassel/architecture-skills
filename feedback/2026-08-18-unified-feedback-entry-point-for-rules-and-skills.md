# Establish single unified feedback entry point across rules, skills, and plugins

- Status: verified
- Skill: maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md`, `skills/maintain-architecture-skills/SKILL.md`, & `feedback/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner asked whether `feedback/` serves as a single unified entry point for proposing modifications to declarative rules (`rules/**`) as well as skills (`skills/**`) and plugins (`plugins/**`).

## Skill instruction involved

`AGENTS.md`, `skills/maintain-architecture-skills/SKILL.md`, and `feedback/`.

## Observed behavior and impact

Explicitly declaring `feedback/` as the single unified feedback point for all Context Hub components ensures that rule changes follow the exact same evidence-backed triage and owner approval workflow (`+`) as skill changes.

## Session disposition

Owner explicitly requested confirming and documenting `feedback/` as the single unified feedback entry point across `rules/`, `skills/`, and `plugins/`.

## Proposed improvement

1. Update `AGENTS.md` and `skills/maintain-architecture-skills/SKILL.md` to state that any proposal to add, edit, move, or delete files under `rules/**`, `skills/**`, or `plugins/**` MUST first be formatted as an `observed` feedback record under `feedback/YYYY-MM-DD-*.md` for owner approval (`+`).
2. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented in `AGENTS.md` and `skills/maintain-architecture-skills/SKILL.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
