# Separate root skills and plugins folders with dual-directory GitHub Action release sync

- Status: verified
- Skill: git-release-preflight | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `.github/workflows/sync-skills.yml`, `scripts/`, `skills/`, & `plugins/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly requested maintaining `skills/` and `plugins/` as separate top-level directories in the maintainer repository while ensuring both directories are pushed as separate top-level folders to the public `alex-kassel/skills` distribution repository on GitHub.

## Skill instruction involved

`.github/workflows/sync-skills.yml`, `scripts/sync-skills.sh`, `scripts/sync-skills.ps1`, and `skills/git-release-preflight/SKILL.md`.

## Observed behavior and impact

Using a single `git subtree push --prefix skills` restricted release pushes to a single subfolder prefix. Updating the sync workflow and cross-platform helper scripts to push both `skills/` and `plugins/` preserves clean top-level directory separation in both the maintainer repository and the public distribution repository.

## Session disposition

Owner explicitly requested separating `skills/` and `plugins/` as top-level directories and updating release sync.

## Proposed improvement

1. Move `skills/plugins/architecture-suite/plugin.json` back to top-level `plugins/architecture-suite/plugin.json`.
2. Update `.github/workflows/sync-skills.yml` to watch both `skills/**` and `plugins/**` and sync both directories to `alex-kassel/skills`.
3. Update dual-platform helper scripts (`scripts/sync-skills.sh` and `scripts/sync-skills.ps1`) to sync both directories.
4. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented by separating top-level `plugins/` and updating `.github/workflows/sync-skills.yml`, `scripts/sync-skills.sh`, and `scripts/sync-skills.ps1`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
