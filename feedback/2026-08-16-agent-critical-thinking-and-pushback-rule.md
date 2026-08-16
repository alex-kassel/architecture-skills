# Agent critical thinking and pushback guideline

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `b0e1f55`
- Source repository: `c:/Users/Alex/Herd/packages.dev2`
- Source program: `AGENTS.md` & `docs/scraper-core`
- Project session: `S-007`
- Observed at: `2026-08-16`

## Situation

The project owner explicitly established a top-level rule regarding agent decision-making: the agent must exercise critical thinking, architectural vigilance, and reasoned pushback when evaluating design choices.

Even when the owner confirms or approves a technical direction, if the agent identifies valid technical, consistency, safety, or architectural counter-arguments, the agent is authorized and expected to raise reasoned objections up to three times (rephrasing and clarifying the rationale on subsequent attempts). If the owner reaffirms after up to three clear attempts, the agent accepts the owner's disposition.

## Skill instruction involved

`guide-architecture-design` decision confirmation and owner interaction instructions.

## Observed behavior and impact

Without explicit skill guidance encouraging reasoned pushback, agents might passively accept suboptimal design choices or immediately agree with the owner without offering technical counter-arguments.

## Session disposition

Not required (non-blocking observation authorized by owner).

## Proposed improvement

Add an explicit guideline to `guide-architecture-design` instructing agents to exercise critical thinking and provide up to three attempts of rephrased, reasoned pushback whenever a proposed decision presents technical or architectural risks, before finally accepting the owner's choice.

## Triage and resolution

Accepted by the owner on 2026-08-16. Implemented in `guide-architecture-design/references/decision-capture-and-sync.md` by instructing agents to exercise critical thinking, architectural vigilance, and provide up to three clear attempts of rephrased, reasoned pushback with technical rationale when design choices present risks before accepting final owner disposition.

## Verification

Verified on 2026-08-16 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for `guide-architecture-design` and by forward-test scenario 31 (`codex-guide-pushback-20260816`).
