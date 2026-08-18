# Harden natural language skill maintenance triggers and mandate feedback intake in AGENTS.md

- Status: verified
- Skill: maintain-architecture-skills | guide-architecture-design
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner inquired whether skipping the feedback creation step during a natural language request was due to agent inattentiveness or a flaw in repository documentation. Analysis revealed that `AGENTS.md` only matched explicit English trigger phrases (`Start skill maintenance`, `Process feedback`), causing future agents in fresh sessions to bypass the `TRIAGE_FEEDBACK` state when presented with informal or non-English requests proposing skill additions, modifications, moves, or deletions.

## Skill instruction involved

`AGENTS.md` (Intent & Workflow Routing and Repository Boundaries).

## Observed behavior and impact

Without explicit intent routing in `AGENTS.md` covering natural language skill modification requests, agents in new sessions could mistake skill mutation requests for routine file management tasks, bypassing mandatory `feedback/20??-*.md` evidence generation and triage approval.

## Session disposition

Owner identified the systemic documentation gap.
Proposed solution:
1. Update `AGENTS.md` `Intent & Workflow Routing` table to explicitly route any user proposal for adding, moving, modifying, or deleting skills to `TRIAGE_FEEDBACK`.
2. Add an explicit rule under `Repository Boundaries` mandating that all skill mutation proposals (regardless of phrasing or language) must be formatted as `observed` feedback records in `feedback/20??-*.md` before executing changes.

## Triage and resolution

Accepted on 2026-08-18. Implemented in `AGENTS.md` by expanding intent triggers and repository boundaries to ensure all fresh agent sessions strictly enforce feedback creation prior to skill file edits.

## Verification

Verified on 2026-08-18 by executing `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, both returning clean pass with exit code 0.
