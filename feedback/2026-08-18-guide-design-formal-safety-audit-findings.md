# Formal logic, mutation safety, and deadlock findings in guide-architecture-design

- Status: verified
- Skill: guide-architecture-design
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `c:\Users\Alex\codex-architecture-skills`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

An independent formal verification audit of `guide-architecture-design` identified 11 findings related to logical contradictions, deadlock states, git mutation safety, and edge-case handling.

## Skill instruction involved

`SKILL.md`, `references/workflow-modes.md`, `references/gates-recovery-and-git.md`, `references/operating-contract.md`, `references/decision-capture-and-sync.md`.

## Observed behavior and impact

- C1: Deadlock when `READINESS_GATE` is invoked without a pre-existing audit report.
- C2: Raw local git squash merge fallback on `main` violates mutation boundaries and zero-write preflights.
- C3: Conflict between mid-batch failure containment ("Contain failure") and autonomous mechanical retry.
- M1-M5, m1-m3: Missing intra-batch baseline snapshot updates, priority ambiguity between `+` symbol and mandatory pushback, unverified durable authority, and pre-existing dirty target recovery.

## Session disposition

Not required. Non-blocking audit observation.

## Proposed improvement

Resolve all 11 formal verification findings by updating `SKILL.md` and reference files to clarify passive readiness checking, eliminate raw `main` git merge fallbacks, restrict mechanical retries to dry-run preflights, update baseline digests incrementally, and prioritize architectural risk pushback over fast `+` confirmation.

## Developer Community Best Practice Evaluation

Formal verification of state machine transitions and zero-trust mutation boundaries prevents silent data corruption and unauthorized primary branch mutations in automated LLM agents.

## Triage and resolution

Accepted by owner. Implemented across `skills/guide-architecture-design/SKILL.md` and all 4 reference files.

## Verification

Verified in `evals/forward-tests.md` scenario 43.
