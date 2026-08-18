# Relocate plugin manifests under skills/plugins for automatic GitHub Action downstream sync

- Status: verified
- Skill: git-release-preflight | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `.github/workflows/sync-skills.yml` & `skills/plugins/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner inquired whether the `architecture-suite` plugin manifest and GitHub Action sync workflow were fully updated. Inspection revealed that `.github/workflows/sync-skills.yml` and local sync scripts (`sync-skills.ps1`, `sync-skills.sh`) use `git subtree push --prefix skills`. Placing `plugin.json` under root `plugins/` prevented it from being included in the downstream release push to `alex-kassel/skills`.

## Skill instruction involved

`.github/workflows/sync-skills.yml`, `skills/git-release-preflight/SKILL.md`, and `scripts/sync-skills.sh`.

## Observed behavior and impact

Keeping `plugins/` outside `skills/` meant `git subtree push --prefix skills` skipped syncing plugin manifests to the downstream public distribution repository `alex-kassel/skills`.

## Session disposition

Owner asked to verify and update the GitHub Action and plugin placement.

## Proposed improvement

1. Move `plugins/architecture-suite/plugin.json` to `skills/plugins/architecture-suite/plugin.json`.
2. Update `.github/workflows/sync-skills.yml` path triggers to ensure `skills/**` changes automatically sync plugins to `alex-kassel/skills`.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented by relocating plugin manifest to `skills/plugins/architecture-suite/plugin.json` and verifying `.github/workflows/sync-skills.yml` triggers.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
