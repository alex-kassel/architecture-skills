# Enforce neutral placeholder examples across core documentation

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `b0e1f55`
- Source repository: `<project-root>`
- Source program: `docs/scraper-core`
- Project session: `S-007`
- Observed at: `2026-08-16`

## Situation

During documentation-as-code working sessions for generic core packages (such as Scraper Core), agents previously introduced specific vendor/child-domain examples (e.g. `drive-now-vienna`, `Car Subscription Spider`) or informal placeholders (`bla-bla`).

The project owner explicitly directed that all generic core documentation must strictly use neutral placeholders (e.g. `spider-one`, `spider-two`, `domain-one`, `SpiderOneSpider`) and never reference specific child package entities or third-party vendor names.

## Skill instruction involved

`guide-architecture-design` and `audit-architecture-handoff` documentation standards and example generation guidelines.

## Observed behavior and impact

Without explicit skill guidance enforcing neutral placeholder naming, agents may invent informal or domain-specific examples that leak downstream product context into generic core architecture documents.

## Session disposition

Not required (non-blocking observation authorized by owner).

## Proposed improvement

Include a documentation guideline in `guide-architecture-design` and `audit-architecture-handoff` instructions requiring all generated examples in generic core projects to use neutral placeholders (`spider-one`, `spider-two`, `domain-one`, `SpiderOneSpider`) and prohibiting child-package or vendor-specific names in core documentation.

## Triage and resolution

Accepted by the owner on 2026-08-16. Implemented in `guide-architecture-design/references/decision-capture-and-sync.md` and `audit-architecture-handoff/references/finding-taxonomy.md` by requiring all generic core documentation examples to strictly use neutral placeholders (`spider-one`, `spider-two`, `domain-one`, `SpiderOneSpider`) and prohibiting informal placeholders (`bla-bla`) or vendor/child-package entity names in core artifacts.

## Verification

Verified on 2026-08-16 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for both skills and by forward-test scenario 32 (`codex-guide-neutral-placeholders-20260816`).
