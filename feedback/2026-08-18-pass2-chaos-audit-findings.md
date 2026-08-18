# Pass 2 Chaos Audit residual edge-case findings in guide-architecture-design

- Status: deferred
- Skill: guide-architecture-design
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

During Pass 2 Re-Audit, an independent Adversarial Chaos Auditor (Side 3) identified 5 edge-case hardening opportunities:
1. CHAOS-01: CLI PR merge network failure fallback handling.
2. CHAOS-02: Partial batch write recovery attribution.
3. CHAOS-03: Indeterminate duration tracking for long-interrupted sessions.
4. CHAOS-04: Validation build cache preflight exclusion (`.pytest_cache`).
5. CHAOS-05: Case-insensitive status matching for durable authority (`accepted`/`ACCEPTED`).

## Skill instruction involved

`references/workflow-modes.md`, `references/gates-recovery-and-git.md`, `references/operating-contract.md`.

## Observed behavior and impact

Non-blocking edge-case scenarios under extreme network or host cache conditions. Core safety invariants remain intact.

## Session disposition

Not required. Deferred to the next scheduled audit cycle under the Residual Deferral Gate policy.

## Proposed improvement

Harden PR CLI merge failure rollbacks, partial batch attribution tags, and case-insensitive status matching in the next scheduled audit cycle.

## Developer Community Best Practice Evaluation

Deferring minor non-blocking findings identified during verification re-audits prevents infinite perfection loops while maintaining audit provenance.

## Triage and resolution

Deferred to next scheduled audit cycle under 2-pass audit policy.

## Verification

Pending next scheduled audit cycle.
