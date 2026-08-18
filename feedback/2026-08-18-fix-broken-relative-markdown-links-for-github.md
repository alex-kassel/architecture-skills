# Fix broken relative markdown links using root-relative paths for GitHub

- Status: verified
- Skill: validate-repository-guardrails | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `README.md`, `skills/README.md`, `plugins/README.md`, & `scripts/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner reported a broken GitHub link (`https://github.com/alex-kassel/skills/blob/plugins/README.md`). Investigation revealed two issues:
1. `skills/README.md` contained `../plugins/README.md` relative links. When `skills/README.md` was copied to the root of `alex-kassel/skills` as `README.md`, GitHub interpreted `../plugins` as a branch name `blob/plugins/README.md` outside the repository root.
2. `skills/maintain-architecture-skills/SKILL.md` and `skills/publish-packagist-package/SKILL.md` contained `[`skills/name`](../name)` mismatched text and link targets.

## Skill instruction involved

`README.md`, `skills/README.md`, `plugins/README.md`, `scripts/sync-skills.sh`, `scripts/sync-skills.ps1`, and `skills/validate-repository-guardrails/SKILL.md`.

## Observed behavior and impact

Using `../` links from root or mismatched link text causes GitHub web interface to resolve broken URLs or navigate outside the repository root.

## Session disposition

Owner explicitly requested fixing all broken Markdown links across all README files and project documentation.

## Proposed improvement

1. Use root-relative GitHub Markdown links (`/plugins/README.md`, `/skills/README.md`, `/README.md`) across `skills/README.md` and `plugins/README.md`.
2. Fix mismatched link texts in `maintain-architecture-skills/SKILL.md` and `publish-packagist-package/SKILL.md`.
3. Update `scripts/sync-skills.sh` and `scripts/sync-skills.ps1` to copy root `README.md` to the root of `alex-kassel/skills`.
4. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented root-relative links in README files, fixed SKILL.md links, and updated sync scripts.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
