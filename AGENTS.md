# Architecture Skills Repository

## Purpose

This repository develops and validates reusable architecture skills. Skill source changes, feedback triage, validation, and forward-test evidence belong here, not in consuming project documentation.

## Intent & Workflow Routing

| Trigger Phrase | Workflow State | Primary Action Contract |
| :--- | :--- | :--- |
| `Start skill maintenance`, `Process feedback`, or any proposal to add, edit, move, or delete rules, skills, or plugins | `TRIAGE_FEEDBACK` | Record `observed` feedback in `feedback/20??-*.md`, present triage proposal for owner approval; execute `skills/maintain-architecture-skills/SKILL.md`. |
| `Run audit`, `Start audit` | `EXECUTE_AUDIT` | Execute autonomous 4-phase, 2-pass iterative audit protocol per `audits/README.md` and `skills/execute-autonomous-audit/SKILL.md`. |
| `Install adapter <name>`, `Sync adapters` | `INSTALL_ADAPTER` | Execute non-destructive adapter script under `scripts/adapters/<name>.py` or `scripts/adapters/sync_all.py`. |
| `+` | `CONFIRM_ACTION` | Confirm pending triage proposal or prompt response. Does NOT authorize git push. |
| `push`, `git push`, `Sync skills` | `PUSH_RELEASE` | Run pre-push readiness evaluation per `skills/git-release-preflight/SKILL.md`. Push directly if clean; report risks if found. |

## Repository Boundaries

- Keep declarative policies under `rules/**`, reusable skill behavior under `skills/**`, plugin manifests under `plugins/**`, design rationale and ADRs under `docs/**` and `design/**`, durable test evidence under `evals/**`, and incident logs under `feedback/**`.
- Any user proposal or request to add, move, modify, or delete rules, skills, or plugins (regardless of phrasing or language) MUST first be formatted as an `observed` feedback record under `feedback/20??-*.md` and approved before editing files under `rules/**`, `skills/**`, or `plugins/**`.
- Do not modify a consuming project while performing skill maintenance.
- Do not use a skill to validate its own behavior in the same context when an independent forward-test is required.
- Execute path validator (`python scripts/validate_relative_paths.py`) and language validator (`python scripts/validate_english_only.py`) per `skills/validate-repository-guardrails/SKILL.md` prior to commit.
- All repository helper scripts MUST be dual-platform (either cross-platform Python `.py`, or paired `.ps1` for Windows PowerShell and `.sh` for macOS/Linux Bash).
- Never write local absolute file paths (e.g. `C:\...`, `file:///C:/...`, `/Users/...`, `/home/...`) in any repository file, audit document, or feedback record. Use relative paths for all repository files (e.g. `skills/guide-architecture-design/SKILL.md`) and HTTP/HTTPS URLs for external links.
- All repository files must be written exclusively in English. No non-English content is permitted in any tracked file.
- Never invent artificial marketing jargon or fake pattern names. Communicate using plain, direct technical terms without decorative embellishment.
- Full repository autonomous audits execute ONLY upon explicit, direct owner command (`Run audit`, `Start audit`). Every target skill audited MUST have 3 dedicated audit log files under `audits/` (1 skill = 3 audit files; N skills = N × 3 audit files). Aggregating multiple skills into a single audit file per perspective is strictly prohibited.
