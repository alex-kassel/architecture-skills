# Two-Pass Iteration Loop Policy for Architecture Audits

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `c:\Users\Alex\codex-architecture-skills`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The owner refined the audit workflow policy to mandate that every audit execution MUST consist of at least two full passes:
1. Pass 1: Initial 3-way audit -> Work/fixes iteration based on owner triage approval.
2. Pass 2: Verification 3-way re-audit by 3 fresh independent agents to verify completeness and check for regressions.
3. Residual Deferral: Minor non-blocking findings in Pass 2 are documented and deferred to the next scheduled audit cycle.

## Skill instruction involved

`AGENTS.md` skill maintenance section and `audits/README.md`.

## Observed behavior and impact

Single-pass audits risk leaving unverified fixes or undetected regressions caused by the initial fix implementation. The 2-pass policy guarantees verification while preventing infinite perfection loops.

## Session disposition

Not required. Non-blocking workflow refinement.

## Proposed improvement

Document the mandatory 2-pass iteration loop in `AGENTS.md` and `audits/README.md`. Trigger Pass 2 immediately after Pass 1 fixes are implemented and verified.

## Developer Community Best Practice Evaluation

Re-auditing after fix implementation is standard practice in software security and compliance auditing (Retest / Verification Scan). Capping at 2 passes balances rigorous verification with high engineering velocity.

## Triage and resolution

Accepted by owner. Implemented in `AGENTS.md` and `audits/README.md`.

## Verification

Verified in `AGENTS.md` and `audits/README.md`.
