# Standardize 5-state package lifecycle and platform status matrix

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `c:\Users\Alex\Herd\packages.dev2`
- Source program: `alex-kassel/stable-fingerprint`
- Project session: `S-002`
- Observed at: `2026-08-18`

## Situation

During the `stable-fingerprint` project lifecycle, standalone package implementation was completed, unit-tested (100% pass), tagged `v1.0.0`, and pushed to GitHub with CI automation. However, the documentation status remained set to `IMPLEMENTATION_READY`. 

The owner pointed out that between `IMPLEMENTATION_READY` (architecture approved) and `RELEASED (vX.Y.Z)` (code deployed), a distinct state `IN_DEVELOPMENT` (active coding) is required. Furthermore, when starting work on a subsequent version (e.g. `v1.1.0-dev`), status must transition back to `IN_DEVELOPMENT` to reflect active work, and a `Platform Status Matrix` in root `AGENTS.md` is needed to prevent derived drift across platform repositories.

## Skill instruction involved

1. `guide-architecture-design/references/decision-capture-and-sync.md` & `workflow-modes.md` (Roadmap phase progression and status transition vocabulary).
2. `audit-architecture-handoff/references/readiness-report.md` & `finding-taxonomy.md` (Readiness verdicts and platform matrix drift detection).

## Observed behavior and impact

Without an explicit `IN_DEVELOPMENT` status and version progression protocol:
1. Projects remain stuck at `IMPLEMENTATION_READY` during coding or after release.
2. Subsequent version iteration lacks a clear status transition rule.
3. Multi-package platform entrypoints lack a central `Platform Status Matrix` table in `AGENTS.md`, causing documentation drift.

## Session disposition

Owner approved a 5-state package lifecycle model and requested capturing it as a formal feedback record before triage and implementation.

## Proposed improvement

1. Standardize 5 package lifecycle states: `SPEC_IN_PROGRESS`, `IMPLEMENTATION_READY`, `IN_DEVELOPMENT (vX.Y.Z-dev)`, `RELEASED (vX.Y.Z)`, and `DEPRECATED`.
2. Define clear status transition rules when starting work on a new version iteration (e.g. transition from `RELEASED (v1.0.0)` back to `IN_DEVELOPMENT (v1.1.0-dev)`).
3. Standardize a central `Platform Status Matrix` table in root `AGENTS.md` templates and enforce cross-artifact status drift checks in `audit-architecture-handoff`.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `guide-architecture-design/references/decision-capture-and-sync.md` and `audit-architecture-handoff/references/readiness-report.md` by standardizing 5 package lifecycle states (`SPEC_IN_PROGRESS`, `IMPLEMENTATION_READY`, `IN_DEVELOPMENT`, `RELEASED`, `DEPRECATED`), transition rules for new version iterations (`IN_DEVELOPMENT (v1.1.0-dev)`), and central `Platform Status Matrix` in root `AGENTS.md`.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 36 (`codex-guide-package-lifecycle-states-20260818`).
