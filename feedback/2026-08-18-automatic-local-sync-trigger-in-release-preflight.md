# Automate downstream alex-kassel/skills release sync in git-release-preflight

- Status: verified
- Skill: git-release-preflight
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `skills/git-release-preflight/SKILL.md` & `scripts/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner noticed that `alex-kassel/skills` had not updated on GitHub after pushing to `alex-kassel/architecture-skills`. Investigation showed GitHub Actions default `GITHUB_TOKEN` lacks cross-repository write access to secondary repos without a `SKILLS_SYNC_TOKEN` secret. Executing local helper scripts (`scripts/sync-skills.ps1` / `scripts/sync-skills.sh`) using local Git credentials successfully pushes changes to `alex-kassel/skills`.

## Skill instruction involved

`skills/git-release-preflight/SKILL.md` (Clean Execution Section 5).

## Observed behavior and impact

Relying solely on GitHub Actions without configuring cross-repository secret tokens left the public `alex-kassel/skills` repository out of sync.

## Session disposition

Owner requested ensuring `alex-kassel/skills` contains both `skills/` and `plugins/`.

## Proposed improvement

1. Execute local sync script `scripts/sync-skills.ps1` to update `alex-kassel/skills` with `skills/` and `plugins/`.
2. Update `skills/git-release-preflight/SKILL.md` Section 5 to mandate running local release sync (`scripts/sync-skills.sh` or `scripts/sync-skills.ps1`) during preflight pushes to guarantee downstream repo updates.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Executed local sync script and updated `skills/git-release-preflight/SKILL.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
