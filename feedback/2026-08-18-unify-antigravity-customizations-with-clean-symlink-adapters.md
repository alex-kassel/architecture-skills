# Unify Antigravity global customizations and purge legacy config registration manifests

- Status: verified
- Skill: maintain-architecture-skills | validate-repository-guardrails
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `scripts/adapters/antigravity.py`, `~/.gemini/antigravity/`, & `~/.gemini/config/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner noticed fragmentation across global Antigravity customization directories:
1. `~/.gemini/config/` contained a legacy `skills.json` registration manifest and third-party skills (`context7`, `skill-creator`).
2. `~/.gemini/antigravity/` contained physically copied rules and skills.

The owner requested eliminating the fragmentation by enforcing a clean, unified architecture:
- Maintain `codex-architecture-skills` as the single canonical source of truth.
- Use clean symlinks/junctions from `~/.gemini/antigravity/` pointing into `codex-architecture-skills`.
- Clean up legacy `skills.json` configuration manifests to avoid duplicate path registrations.

## Skill instruction involved

`AGENTS.md`, `scripts/adapters/antigravity.py`, and `skills/maintain-architecture-skills/SKILL.md`.

## Observed behavior and impact

Using clean symlinks pointing from `~/.gemini/antigravity/` directly into the canonical repository ensures zero file duplication, immediate reactivity upon Git commits, and zero clutter in `~/.gemini/config/`.

## Session disposition

Owner explicitly approved creating the feedback record and implementing the unified Antigravity symlink adapter.

## Proposed improvement

1. Update `scripts/adapters/antigravity.py` to prioritize creating clean NTFS Junctions / Symlinks from `~/.gemini/antigravity/rules/` and `~/.gemini/antigravity/skills/` pointing directly into `codex-architecture-skills`.
2. Remove legacy `skills.json` manifest in `~/.gemini/config/` if present.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented in `scripts/adapters/antigravity.py` and executed.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
