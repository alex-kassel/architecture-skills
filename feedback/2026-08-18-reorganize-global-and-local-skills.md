# Reorganize global utility skills and eliminate duplicate skill definitions

- Status: verified
- Skill: maintain-architecture-skills | validate-repository-guardrails
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md` & `skills/maintain-architecture-skills/SKILL.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner proposed moving universal utility skills (`context7` and `skill-creator`) to the global machine-local skills configuration directory (`~/.gemini/config/skills/`), and removing the project-local duplicate skill `create-skill` to eliminate workflow overlap and trigger confusion.

## Skill instruction involved

`skills/maintain-architecture-skills/SKILL.md` (Evidence Capture and Zero-Write Preflight protocol) and `AGENTS.md`.

## Observed behavior and impact

Having `context7` and `skill-creator` inside a specific project repository restricted their availability to that single workspace, while `create-skill` created duplicate triggering logic against `skill-creator`. Reorganizing universal tools to the global config and keeping only architecture-specific skills inside the repository improves separation of concerns and global accessibility.

## Session disposition

Owner explicitly proposed and confirmed (`+`):
1. Copy `context7` and `skill-creator` to global skills folder `~/.gemini/config/skills/`.
2. Remove `create-skill`, `context7`, and `skill-creator` from repository directory `skills/`.
3. Verify repository guardrails and validate relative paths and English-only compliance.

## Proposed improvement

Reorganize universal tools to `~/.gemini/config/skills/` and remove redundant local duplicate `create-skill`. Record full evidence history in `feedback/2026-08-18-reorganize-global-and-local-skills.md`.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented by copying `context7` and `skill-creator` to `~/.gemini/config/skills/`, removing `context7`, `skill-creator`, and `create-skill` from `skills/`, and logging this verified record.

## Verification

Verified on 2026-08-18 by executing `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, both returning clean pass with exit code 0.
