# Mandate 1:3 per-skill audit log granularity and exclusive owner-trigger for full audits

- Status: verified
- Skill: execute-autonomous-audit | maintain-architecture-skills
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md` & `skills/execute-autonomous-audit/SKILL.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly specified two critical audit governance requirements:
1. **Per-Skill Audit Granularity**: Aggregating multiple skills into a single audit file per perspective is an antipattern and strictly prohibited. Every target skill MUST have 3 dedicated audit log files under `audits/` (one file per perspective). For N target skills, a full audit MUST generate exactly N × 3 audit files (e.g. 10 skills = 30 audit log files).
2. **Exclusive Owner Trigger**: Full repository autonomous audits execute ONLY upon explicit, direct owner instruction (`Run audit`, `Start audit`). No implicit or background triggers may launch a full repository audit.

## Skill instruction involved

`skills/execute-autonomous-audit/SKILL.md`, `skills/maintain-architecture-skills/SKILL.md`, `audits/README.md`, and `AGENTS.md`.

## Observed behavior and impact

Lumping multiple skills into 1 shared audit file per perspective dilutes finding granularity, makes historical traceability per skill difficult, and violates the 1:3 audit log contract.

## Session disposition

Owner explicitly directed:
1. Enforce the 1:3 per-skill audit log file granularity rule across all audit documentation and skills.
2. Restrict full repository audit execution strictly to direct, explicit owner commands (`Run audit`, `Start audit`).
3. Update `skills/execute-autonomous-audit/SKILL.md`, `audits/README.md`, and `AGENTS.md`.

## Proposed improvement

1. Update `skills/execute-autonomous-audit/SKILL.md` Phase 1 to mandate creating 3 dedicated audit files for every individual skill audited (N skills = N × 3 audit log files).
2. Update `audits/README.md` and `AGENTS.md` to document the 1:3 per-skill audit log file invariant and explicit owner-trigger policy.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `skills/execute-autonomous-audit/SKILL.md`, `audits/README.md`, and `AGENTS.md`, and verified by path and language guardrails.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
