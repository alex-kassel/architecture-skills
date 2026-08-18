# Mandate autonomous multi-perspective audit following any new skill creation or major update

- Status: verified
- Skill: maintain-architecture-skills | execute-autonomous-audit
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md` & `skills/maintain-architecture-skills/SKILL.md`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed that whenever a new skill is created or substantially modified, the creation process is NOT complete until a full 4-phase, 2-pass autonomous audit (`execute-autonomous-audit`) is conducted by subagents and durable audit records are logged under `audits/`.

## Skill instruction involved

`AGENTS.md` and `skills/maintain-architecture-skills/SKILL.md` (Step 4 Validation & Audit requirement).

## Observed behavior and impact

Creating or updating skills without completing an autonomous multi-perspective audit risks leaving unverified logic flaws, edge-case vulnerabilities, or template schema drift in newly added skills.

## Session disposition

Owner explicitly directed:
1. Mandate that every newly created or refactored skill must undergo an autonomous 4-phase, 2-pass audit (`execute-autonomous-audit`).
2. Record durable audit logs under `audits/` for every skill creation.
3. Immediately run a full autonomous audit for the newly created `session-lifecycle` skill.

## Proposed improvement

1. Update `skills/maintain-architecture-skills/SKILL.md` Step 4 to mandate running `execute-autonomous-audit` after any skill creation.
2. Update `AGENTS.md` to reflect this mandatory post-creation audit gate.
3. Conduct and log Pass 1 and Pass 2 autonomous audits for `skills/session-lifecycle/SKILL.md`.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `skills/maintain-architecture-skills/SKILL.md` and `AGENTS.md`, and verified by executing an autonomous audit for `skills/session-lifecycle/SKILL.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
