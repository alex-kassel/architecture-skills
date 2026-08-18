# Implement non-destructive adapter architecture for rules and skills distribution

- Status: verified
- Skill: maintain-architecture-skills | validate-repository-guardrails
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `scripts/adapters/`, `AGENTS.md`, & `README.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested an explicit, non-destructive adapter framework under `scripts/adapters/` for deploying managed rules (`rules/`) and skills (`skills/`) to AI agent clients (`antigravity.py`, `cursor.py`, `claude.py`, `codex.py`).

Safety constraints mandated:
1. **Explicit visibility**: Adapter files must be visible by inspection in `scripts/adapters/`.
2. **Zero destruction**: Target folders must NEVER be wiped or purged; only managed symlinks/copies may be safely updated.
3. **Symlink with Copy Fallback**: Attempt symlink/junction first; fall back to physical copying if OS permissions disallow symlinks.
4. **Agent Trigger Routing**: Integrate trigger phrases into `AGENTS.md` so the user can instruct the agent to run adapter installations on demand.

## Skill instruction involved

`AGENTS.md`, `scripts/adapters/`, `skills/maintain-architecture-skills/SKILL.md`, and `skills/validate-repository-guardrails/SKILL.md`.

## Observed behavior and impact

Providing explicit, non-destructive adapter scripts prevents accidental file wiping in target client directories while enabling seamless 1-command deployment across AI agent platforms.

## Session disposition

Owner explicitly requested writing non-destructive adapter scripts with explicit triggers in `AGENTS.md`.

## Proposed improvement

1. Create `scripts/adapters/base_adapter.py` providing safe symlink/copy helper functions without directory wiping.
2. Create platform adapters:
   - `scripts/adapters/antigravity.py`
   - `scripts/adapters/cursor.py`
   - `scripts/adapters/claude.py`
   - `scripts/adapters/codex.py`
   - `scripts/adapters/sync_all.py`
3. Register intent routing in `AGENTS.md` (`Install adapter <target>`, `Sync adapters`).
4. Update `README.md` and `rules/README.md`.
5. Verify path relativity and English-only guardrail compliance.

## Triage and resolution

Accepted by owner on 2026-08-18. Implemented adapter scripts and registered intent routing in `AGENTS.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
