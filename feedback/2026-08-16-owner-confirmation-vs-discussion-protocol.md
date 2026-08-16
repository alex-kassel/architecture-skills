# Distinguish explicit owner confirmation from invitations to discussion

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `b0e1f55`
- Source repository: `c:/Users/Alex/Herd/packages.dev2`
- Source program: `AGENTS.md` & `docs/scraper-core`
- Project session: `S-007`
- Observed at: `2026-08-16`

## Situation

The project owner established a formal protocol for interpreting user intent during design workflows:

1. Short responses like `+`, `OK`, or `Confirmed` represent final owner decisions.
2. Messages containing questions, suggestions, or amendments without an explicit confirmation phrase are invitations to discussion. The agent must evaluate the owner's input, adjust or refine the design proposal with reasoned arguments, and return the updated proposal back to the owner for explicit confirmation.
3. If a message contains an explicit confirmation phrase AND a new question/task, the prior design item is confirmed, and the new item is addressed in the next turn.

## Skill instruction involved

`guide-architecture-design` owner interaction, decision capture, and confirmation protocol.

## Observed behavior and impact

Without this explicit distinction, agents might prematurely treat user questions or design feedback as final confirmations, skipping the re-derivation and re-presentation step required for owner approval.

## Session disposition

Not required (non-blocking observation authorized by owner).

## Proposed improvement

Update `guide-architecture-design` guidelines to explicitly define the 3-part owner confirmation vs discussion intent interpretation rule, requiring agents to thoroughly rephrase and summarize owner input in detail for clear comprehension before returning refined proposals for explicit confirmation.

## Triage and resolution

Accepted by the owner on 2026-08-16. Implemented in `guide-architecture-design/references/decision-capture-and-sync.md` by explicitly defining intent boundaries (short explicit confirmation vs invitation to discussion vs confirmation with new topic), and requiring the agent to thoroughly rephrase and summarize the owner's input and proposed adjustments in detail to demonstrate clear comprehension before returning refined proposals for confirmation.

## Verification

Verified on 2026-08-16 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for `guide-architecture-design` and by forward-test scenario 33 (`codex-guide-intent-protocol-20260816`).
