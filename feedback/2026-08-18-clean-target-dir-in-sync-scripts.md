# Clean stale root directories in downstream release sync scripts

- Status: verified
- Skill: git-release-preflight | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `scripts/sync-skills.sh` & `scripts/sync-skills.ps1`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner observed that stale top-level directories (`audit-architecture-handoff`, `guide-architecture-design`) remained at the root of the downstream `alex-kassel/skills` repository from previous single-skill syncs. The sync scripts were copying `skills/` and `plugins/` into the destination without removing old top-level folders.

## Skill instruction involved

`scripts/sync-skills.sh`, `scripts/sync-skills.ps1`, and `skills/git-release-preflight/SKILL.md`.

## Observed behavior and impact

Failing to clean out old top-level files/directories in the cloned destination repository leaves stale legacy folders alongside the new `skills/` and `plugins/` structure.

## Session disposition

Owner explicitly requested updating sync scripts to purge stale destination files/directories before copying fresh release contents.

## Proposed improvement

1. Update `scripts/sync-skills.sh` and `scripts/sync-skills.ps1` to wipe all existing files and directories in the cloned temporary repository (except `.git`) prior to copying `skills/`, `plugins/`, and root `README.md`.
2. Execute the updated sync script to clean `alex-kassel/skills` on GitHub.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented in `scripts/sync-skills.sh` and `scripts/sync-skills.ps1` and executed.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
