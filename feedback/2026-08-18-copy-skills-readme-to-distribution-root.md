# Copy skills/README.md to distribution repository root and explain GitHub blob/main URLs

- Status: verified
- Skill: git-release-preflight | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `skills/README.md`, `scripts/sync-skills.sh`, & `scripts/sync-skills.ps1`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner specified two user requirements:
1. **GitHub URL Explanation**: Clarified that `blob/main` in GitHub URLs is standard GitHub Web UI syntax where `main` is the branch name and `blob` (Binary Large Object) is Git's object type for files (`tree` is used for directories).
2. **Distribution Root README**: The owner explicitly directed that `skills/README.md` SHOULD be copied to the root `README.md` of the `alex-kassel/skills` distribution repository (rather than copying the maintainer repository's root `README.md`).

## Skill instruction involved

`skills/README.md`, `scripts/sync-skills.sh`, `scripts/sync-skills.ps1`, and `skills/maintain-architecture-skills/SKILL.md`.

## Observed behavior and impact

Using root-relative Markdown links (`/skills/name/SKILL.md`, `/plugins/README.md`) inside `skills/README.md` allows the file to serve as both `skills/README.md` and distribution root `README.md` without broken links in either location.

## Session disposition

Owner explicitly requested copying `skills/README.md` to the root of `alex-kassel/skills`.

## Proposed improvement

1. Use root-relative links (`/skills/...`, `/plugins/...`) in `skills/README.md`.
2. Update `scripts/sync-skills.sh` and `scripts/sync-skills.ps1` to copy `skills/README.md` to `$TempDir/README.md`.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented in `skills/README.md` and sync scripts.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
