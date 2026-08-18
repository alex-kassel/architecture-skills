# Architecture Skills Repository

## Purpose

This repository develops and validates reusable architecture skills. Skill source changes, feedback triage, validation, and forward-test evidence belong here, not in consuming project documentation.

## Intent & Workflow Routing

| Trigger Phrase | Workflow State | Primary Action Contract |
| :--- | :--- | :--- |
| `Start skill maintenance`, `Process feedback` | `TRIAGE_FEEDBACK` | Inspect Git state, read `feedback/20??-*.md`, present triage proposal for owner approval. |
| `Run audit`, `Start audit` | `EXECUTE_AUDIT` | Execute autonomous 4-phase, 2-pass iterative audit protocol per `audits/README.md`. |
| `+` | `CONFIRM_ACTION` | Confirm pending triage proposal or prompt response. Does NOT authorize git push. |
| `push`, `git push`, `Sync skills` | `PUSH_RELEASE` | Run pre-push readiness evaluation. Push directly if clean; report risks if found. |

## Skill Maintenance Protocol

1. **Evidence Capture**: Incoming `observed` feedback records (`feedback/20??-*.md`) are preserved as evidence. All owner additions, suggestions, and workflow refinements must first be recorded as `observed` feedback files before editing skills. (Standard protocol artifacts under `audits/`, `evals/`, `feedback/` do not require pre-approval).
2. **Community Triage**: Evaluate proposals against community best practices and software architecture patterns. Propose `accepted`, `rejected`, or `superseded` with expert recommendations. Wait for explicit owner approval (`+`).
3. **Zero-Write Preflight & Smallest Change**: Make the smallest reusable skill change under `skills/**` only after owner approval. Never edit `skills/**` prior to triage approval.
4. **Validation & Self-Healing Loop**: Run `skill-creator` validation for changed skills and verify forward-test coverage in `evals/forward-tests.md`. If validation fails, perform up to 3 bounded self-repair attempts before reverting diff and escalating.
5. **Deterministic Guardrails**: Execute path validator (`python scripts/validate_relative_paths.py`) and language validator (`python scripts/validate_english_only.py`) prior to commit.
6. **Resolution & Pre-Push Evaluation**: Mark accepted feedback records `implemented` and `verified`. Create one focused local commit when authorized. When explicitly commanded to push (`push`), perform pre-push evaluation (tests, feedback status, clean worktree, path/language validators). Push directly if zero risks exist; present counter-arguments if risks are found.

## Mandatory Audit Standard

When executing audits (`Run audit`, `Start audit`), initialize 3 audit files in `audits/` following `audits/README.md`. In Block 1 of EVERY audit prompt, **mandate that auditors provide 3 innovative ideas/patterns** on their respective topics to enrich repository instructions and skills.

## Repository Boundaries

- Keep reusable skill behavior under `skills/**`, design rationale under `design/**`, durable test evidence under `evals/**`, and incident logs under `feedback/**`.
- Do not modify a consuming project while performing skill maintenance.
- Do not use a skill to validate its own behavior in the same context when an independent forward-test is required.
- Never write local absolute file paths (e.g. `C:\...`, `file:///C:/...`, `/Users/...`, `/home/...`) in any repository file, audit document, or feedback record. Use relative paths for all repository files (e.g. `skills/guide-architecture-design/SKILL.md`) and HTTP/HTTPS URLs for external links.
- All repository files must be written exclusively in English. No non-English content is permitted in any tracked file.
