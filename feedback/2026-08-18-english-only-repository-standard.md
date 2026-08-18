# English-Only Repository Standard and Automated Validation Enforcement

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `6a25fa8`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner instructed that all repository documents, skills, audits, feedback logs, design specifications, evals, and scripts must be written exclusively in standard technical English. No non-English (Cyrillic) content is permitted in any tracked file.

## Skill instruction involved

`AGENTS.md` boundaries section and `scripts/validate_english_only.py`.

## Observed behavior and impact

Having non-English text across documentation files breaks international distribution standards and impairs automated LLM agent parsing for global developer teams.

## Session disposition

Accepted and confirmed by owner.

## Proposed improvement

1. Add explicit English-only rule in `AGENTS.md` boundaries.
2. Translate all non-English text across `audits/`, `feedback/`, `skills/`, `design/`, `evals/`, and `AGENTS.md` to technical English.
3. Create automated validation script `scripts/validate_english_only.py` to scan repository files for Cyrillic content.

## Developer Community Best Practice Evaluation

Writing all software architecture specifications and documentation in standard technical English is the global software engineering standard for open-source and enterprise repositories.

## Triage and resolution

- Status: `implemented` & `verified`
- Resolution: Accepted by owner and implemented across all 57 repository files.

## Verification

Verified via `python3 scripts/validate_english_only.py` returning Exit Code 0.
