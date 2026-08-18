# Transform repository into complete Architecture Context Control Hub with rules/ and adr/

- Status: verified
- Skill: maintain-architecture-skills | validate-repository-guardrails
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md`, `rules/`, `docs/adr/`, & `skills/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed transforming `codex-architecture-skills` into a comprehensive, domain-isolated **Architecture Context Control Hub**. The hub governs the full architecture lifecycle: planning documentation, spec readiness, code implementation, guardrail verification, and production release.

## Skill instruction involved

`AGENTS.md`, `skills/maintain-architecture-skills/SKILL.md`, and `skills/validate-repository-guardrails/SKILL.md`.

## Observed behavior and impact

Previously, persistent project rules were mixed inside `AGENTS.md` or skill files. Establishing a dedicated `rules/` taxonomy (separated into `global/` and `stacks/`) and an `docs/adr/` decision log separates persistent policy from procedural skill workflows.

## Session disposition

Owner explicitly confirmed transforming the repository into an Architecture Context Control Hub.

## Proposed improvement

1. **Rules Taxonomy (`rules/`)**:
   - `rules/global/engineering.md` (Software engineering principles, DRY, Single Source of Truth, No Superficial Patches).
   - `rules/global/git.md` (Git branch conventions, atomic commits, conventional commits, prohibition of force push).
   - `rules/global/quality.md` (Language compliance, POSIX forward-slash relative paths, guardrails execution).
   - `rules/stacks/php.md` (PHP standards, Composer conventions, PSR-12, strict typing).
   - `rules/stacks/laravel.md` (Laravel package standards, Service Providers, Eloquent persistence).
2. **ADR Decision Log (`docs/adr/`)**:
   - `docs/adr/0001-architecture-context-hub-taxonomy.md` (Architectural decision defining `rules/`, `skills/`, `plugins/`, and `scripts/` separation).
3. **Repository Router & Documentation**:
   - Update `AGENTS.md` to include intent routing for `rules/`.
   - Update `README.md` to document the full Context Control Hub architecture.
4. **Verification**:
   - Verify 100% relative paths and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented `rules/`, `docs/adr/`, updated `AGENTS.md`, `README.md`, and executed release sync.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
