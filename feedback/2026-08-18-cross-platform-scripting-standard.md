# Enforce dual-platform scripting standard (Windows PowerShell and macOS/Linux Bash or Python)

- Status: verified
- Skill: maintain-architecture-skills | validate-repository-guardrails
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md` & `skills/validate-repository-guardrails/SKILL.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed that all repository scripts must support both Windows and macOS/Linux environments. Single-platform scripts (e.g. providing only `.ps1` without a paired `.sh` or cross-platform `.py` script) are prohibited.

## Skill instruction involved

`AGENTS.md` (Repository Boundaries) and `skills/validate-repository-guardrails/SKILL.md`.

## Observed behavior and impact

Providing scripts for only one operating system breaks workflow execution for developers or automated agents operating on other platforms (e.g. running Windows PowerShell scripts on macOS or Bash scripts on Windows without WSL).

## Session disposition

Owner explicitly directed:
1. All repository scripts MUST be dual-platform (either cross-platform Python `.py`, or paired `.ps1` for Windows PowerShell and `.sh` for macOS/Linux Bash).
2. Record `scripts/validate-relative-paths.sh` as the POSIX Bash counterpart for `scripts/validate-relative-paths.ps1`.
3. Mandate dual-platform script requirements in `AGENTS.md` and repository guardrails.

## Proposed improvement

1. Create `scripts/validate-relative-paths.sh` to match `scripts/validate-relative-paths.ps1`.
2. Add explicit dual-platform script requirement to `AGENTS.md` and `skills/validate-repository-guardrails/SKILL.md`.

## Triage and resolution

Accepted on 2026-08-18. Implemented by adding `scripts/validate-relative-paths.sh`, updating `AGENTS.md`, and documenting the cross-platform scripting invariant in repository guardrails.

## Verification

Verified on 2026-08-18 by running `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning Code 0.
