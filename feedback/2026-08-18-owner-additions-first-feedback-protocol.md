# Format owner additions and workflow refinements as feedback records before execution

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `c:\Users\Alex\codex-architecture-skills`
- Source program: `AGENTS.md` & `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed that all user additions, workflow refinements, and design amendments must ALWAYS be captured first as formal feedback records in `feedback/20??-*.md` before any skill edits take place. Direct execution of user suggestions without first staging them as feedback files and presenting them for owner approval as feedback is prohibited.

Additionally, short user responses like `+` or `Обработай фидбек` must be recognized as standard short triggers for starting the skill maintenance workflow, as well as explicit owner confirmation/consent.

## Skill instruction involved

`AGENTS.md` skill maintenance workflow rules, short triggers, and feedback intake protocols.

## Observed behavior and impact

Bypassing the feedback file creation step for user additions would violate provenance and evidence tracking. Recording owner directives first as feedback files ensures that every skill mutation is backed by a durable feedback record, explicit triage, validation, and forward-test evidence.

## Session disposition

Owner explicitly directed:
1. All user additions/amendments must first be formatted as feedback records under `feedback/20??-*.md`.
2. Feedback records must be presented to the owner for explicit triage approval (`accepted`/`rejected`/`superseded`) before execution.
3. Short triggers `Start skill maintenance`, `Обработай фидбек`, and `+` must be recorded in `AGENTS.md`.

## Proposed improvement

1. Update `AGENTS.md` to list `+`, `Обработай фидбек`, and `Start skill maintenance` as official short triggers.
2. Require that all owner additions and skill refinement proposals be captured as `observed` feedback records first before entering triage and implementation.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `AGENTS.md` by requiring all owner additions/suggestions to be captured first as `observed` feedback files under `feedback/20??-*.md` and presented for explicit owner triage approval before executing skill changes, and recording `+` and `Обработай фидбек` as short triggers and confirmation phrases.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 35 (`codex-guide-owner-additions-first-20260818`).
