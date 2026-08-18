# Include clickable remote origin HTTP/HTTPS repository URL in release push reports

- Status: verified
- Skill: git-release-preflight
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `skills/git-release-preflight/SKILL.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested that pre-push reports automatically include a clickable HTTP/HTTPS Markdown link to the remote origin repository (and commit SHA) so the owner can navigate directly to the GitHub page without typing or searching for the URL.

## Skill instruction involved

`skills/git-release-preflight/SKILL.md` (Clean Execution Section 5 & Output Format Template).

## Observed behavior and impact

Providing only raw Git output (`To https://github.com/...`) requires manual copy-pasting to open in a browser. Including clickable HTTP/HTTPS links (`https://github.com/<org>/<repo>/commit/<sha>`) streamlines developer experience.

## Session disposition

Owner explicitly requested embedding clickable remote origin HTTP/HTTPS URLs into `git-release-preflight`.

## Proposed improvement

1. Update `skills/git-release-preflight/SKILL.md` Section 5 to mandate querying `git remote get-url origin` and formatting a clickable HTTP/HTTPS repository link in the report.
2. Update the Pre-Push Evaluation Output Template to include `Remote Repository Link` and `Commit Link` fields.
3. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented in `skills/git-release-preflight/SKILL.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
