# Deduplication of AGENTS.md Root Instructions with Extracted Skills

- Status: verified
- Skill: maintain-architecture-skills | execute-autonomous-audit | git-release-preflight | validate-repository-guardrails
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

Following the extraction of standalone skills (`maintain-architecture-skills`, `execute-autonomous-audit`, `git-release-preflight`, and `validate-repository-guardrails`), `AGENTS.md` still contained detailed step-by-step instruction blocks that duplicated the logic inside the respective `skills/*/SKILL.md` files.

## Skill instruction involved

`AGENTS.md` (Skill Maintenance Protocol, Mandatory Audit Standard, Deterministic Guardrails execution steps).

## Observed behavior and impact

Keeping the full step-by-step protocol instructions in `AGENTS.md` alongside standalone skill definitions violates Single Source of Truth (SSOT) principles and wastes agent prompt context window space.

## Session disposition

Accepted and confirmed by owner (`+`).

## Proposed improvement

Streamline `AGENTS.md` to serve strictly as the high-level intent & workflow routing table and repository boundary definitions, delegating all procedural protocol steps directly to their respective standalone skills (`skills/maintain-architecture-skills/SKILL.md`, `skills/execute-autonomous-audit/SKILL.md`, `skills/git-release-preflight/SKILL.md`, and `skills/validate-repository-guardrails/SKILL.md`).

## Triage and resolution

- Status: `implemented` & `verified`
- Resolution: Accepted by owner (`+`) and implemented by deduplicating `AGENTS.md`.

## Verification

Verified via `scripts/validate_relative_paths.py` and `scripts/validate_english_only.py`.
