# Architecture suite plugin bundle and agent-agnostic session lifecycle skill proposal

- Status: observed
- Skill: maintain-architecture-skills | guide-architecture-design | scaffold-subproject-docs
- Skill commit: `head`
- Source repository: `codex-architecture-skills`
- Source program: `AGENTS.md` & `skills/`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested an agent-agnostic, reusable architecture solution to handle working sessions without duplicating instructions across multiple subprojects or requiring manual skill selection on new computers:
1. **Corridor vs Subproject Routing**: At root corridor (no subproject binding), agents do NOT auto-start sessions or timers. In subprojects (bound via a 1-line metadata badge in `README.md`), work without an active session is prohibited.
2. **Exclusive Single-Agent Ownership Lock**: When an agent opens a subproject session, it becomes the exclusive host/owner of that subproject. Other agents are locked in `READ_ONLY` mode until the active session is closed (`Ending session` command) with complete RFC 3339 time tracking, worklog update, decision boundary recording, and git commit.
3. **Plugin Bundle Distribution**: Package `session-lifecycle`, `scaffold-subproject-docs`, and `guide-architecture-design` into a single plugin manifest (`plugins/architecture-suite/plugin.json`) so users can install the 3 skills in one command without manual skill picking.

## Skill instruction involved

`skills/maintain-architecture-skills/SKILL.md`, `skills/guide-architecture-design/SKILL.md`, `skills/scaffold-subproject-docs/SKILL.md`.

## Observed behavior and impact

Currently, session rules are duplicated across subprojects (e.g. inside `packages.dev2` subtrees), and users must manually locate skills on new machines. Introducing a dedicated `session-lifecycle` skill and an `architecture-suite` plugin manifest eliminates duplication, enforces single-agent ownership, and provides 1-command distribution.

## Session disposition

Owner requested formal feedback triage proposal for review before execution.

## Proposed improvement

1. **New Skill**: Create `skills/session-lifecycle/SKILL.md` (handling corridor vs subproject detection, exclusive single-agent ownership locking, RFC 3339 duration tracking, and handoff session closure).
2. **New Plugin**: Create `plugins/architecture-suite/plugin.json` (bundling `session-lifecycle`, `scaffold-subproject-docs`, and `guide-architecture-design`).
3. **Update Scaffolding**: Add 1-line metadata badge (`> Architecture Suite: Bound to plugin:architecture-suite`) to `scaffold-subproject-docs` templates.
4. **Update Guardrails**: Run path and language guardrail checks across all new files.

## Triage and resolution

- Status: `accepted` (Awaiting explicit owner approval `+`)
- Rationale: Fully resolves subproject duplication, enforces single-agent lock safety, and provides 1-click plugin distribution on GitHub.

## Verification

Pending owner approval (`+`) and execution.
