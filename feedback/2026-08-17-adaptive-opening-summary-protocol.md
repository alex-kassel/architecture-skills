# Adaptive Opening Summary & Response Protocol

- Status: verified
- Skill: guide-architecture-design
- Skill commit: `head`
- Source repository: `<project-root>`
- Source program: `shared`
- Project session: `a7fa4f31-372b-4ef3-9958-38ce7bc4f94b`
- Observed at: `2026-08-17`

## Situation

The project owner explicitly instructed the agent to refine the opening summary protocol (`[Strong Decision]`, `[Neutral]`, `[Architectural Risk]`). The owner indicated that forcing a rigid 3-bullet evaluation template on every single response turn is redundant and unhelpful when there are no major breakthroughs or genuine architectural risks.

## Skill instruction involved

Owner interaction rules and opening response template protocols requiring a mandatory 2-4 line executive evaluation summary block at the start of every chat turn.

## Observed behavior and impact

Repeatedly outputting formal template blocks (`[Strong Decision]`, `[Neutral]`, `[Architectural Risk]`) on routine, investigatory, or operational chat turns created unnecessary verbosity and mechanical routine. The owner requested an adaptive protocol:
1. Include `[Strong Decision]` only when the owner proposes an exceptionally strong/breakthrough architectural idea, explaining why so the owner can build upon it.
2. Include `[Architectural Risk / Pushback]` whenever architectural, consistency, performance, or technical risks exist.
3. Omit the formal 3-bullet template on ordinary turns, starting directly with a concise 1-sentence answer/summary to the prompt.

## Session disposition

Applied immediately in `rules/owner-interaction-rules.md` and `AGENTS.md` per owner explicit workflow directive.

## Proposed improvement

Update skill guidelines and communication instructions across architecture skills to adopt the adaptive opening summary protocol instead of forcing a rigid 3-bullet block on every turn.

## Triage and resolution

Accepted by the owner on 2026-08-17. Implemented in `guide-architecture-design/references/decision-capture-and-sync.md` under `Adapt opening evaluation summary`, omitting rigid 3-bullet evaluation blocks on routine turns while retaining `[Strong Decision]` for breakthrough proposals and `[Architectural Risk / Pushback]` for identified risks.

## Verification

Verified on 2026-08-17 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for `guide-architecture-design` and by forward-test scenario 34 (`codex-guide-adaptive-summary-20260817`).
