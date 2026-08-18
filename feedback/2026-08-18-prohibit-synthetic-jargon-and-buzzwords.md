# Prohibit synthetic jargon and decorative buzzwords in agent communications

- Status: verified
- Skill: maintain-architecture-skills | guide-architecture-design
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly instructed that the agent MUST NEVER invent synthetic marketing terms, fake industry buzzwords, or decorative pattern names (such as presenting custom internal workflow concepts as established industry standards). The agent must communicate using clear, factual, direct technical terminology without embellishment.

## Skill instruction involved

`AGENTS.md` (Repository Boundaries & Communication Rules) and `skills/maintain-architecture-skills/SKILL.md`.

## Observed behavior and impact

Using artificial jargon or presenting custom internal ideas under made-up industry titles causes confusion, damages trust, and misleads the owner about actual industry specifications.

## Session disposition

Owner explicitly directed:
1. Prohibit inventing artificial pattern names or presenting custom concepts as industry standards.
2. Enforce plain, factual, direct technical language across all responses and documentation.
3. Record this rule in repository governance files (`AGENTS.md`).

## Proposed improvement

Add an explicit rule under `AGENTS.md` prohibiting synthetic jargon and requiring direct, non-decorative technical communication.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `AGENTS.md` under `Repository Boundaries` and recorded in feedback log.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning Code 0.
