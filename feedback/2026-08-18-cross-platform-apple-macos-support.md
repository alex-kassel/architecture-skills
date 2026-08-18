# Cross-platform Apple macOS and Linux script support

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested full cross-platform compatibility so that all scripts, validation routines, and maintenance workflows run seamlessly on Apple macOS computers as well as Windows.

## Skill instruction involved

`scripts/` directory, `README.md`, `AGENTS.md`.

## Observed behavior and impact

PowerShell scripts (`.ps1`) require PowerShell Core on macOS. Providing native Python 3 (`scripts/validate_relative_paths.py`) and Bash (`scripts/sync-skills.sh`) scripts guarantees 100% out-of-the-box execution on macOS and Linux without additional dependencies.

## Session disposition

Not required. Non-blocking cross-platform enhancement.

## Proposed improvement

1. Create `scripts/sync-skills.sh` for macOS/Linux Bash execution.
2. Create `scripts/validate_relative_paths.py` for cross-platform Python 3 path validation on macOS, Linux, and Windows.
3. Update `README.md` with macOS/Linux execution commands.

## Developer Community Best Practice Evaluation

Providing Python 3 and POSIX Bash runners alongside PowerShell is the developer community standard for cross-platform repository toolsets (macOS, Linux, Windows).

## Triage and resolution

Accepted by owner. Implemented in `scripts/sync-skills.sh`, `scripts/validate_relative_paths.py`, and `README.md`.

## Verification

Verified via `python3 scripts/validate_relative_paths.py` returning Exit Code 0.
