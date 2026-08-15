---
name: audit-architecture-handoff
description: Perform independent, strictly read-only audits of software architecture and specification repositories for fresh-session handoff, architecture consistency, contradictions, document drift, recovery and onboarding quality, implementation readiness, and whether work can continue without prior conversation. Use when asked to audit documentation-as-code architecture state or handoff safety without changing project state. Do not use for ordinary code review, design interviews, decision capture, documentation updates, worklog changes, Git commits, or implementing fixes.
---

# Audit Architecture Handoff

Operate in `AUDIT_ONLY` mode. Evaluate the durable project state as an independent newcomer and return evidence; never advance the project.

## Enforce the read-only lock

- Do not create, edit, rename, move, or delete project files.
- Do not create or update a worklog, session, timestamp, decision register, issue, branch, tag, commit, stash, or Git index entry.
- Do not run formatters, generators, tests, package managers, hooks, or commands that may write caches or lock files.
- Use read-only inspection commands. For Git status, prefer `git --no-optional-locks status --short --branch`.
- Do not answer an open architecture question, choose an alternative, or mark a decision confirmed.
- If asked to audit and fix, complete only the audit, state the mutation boundary, and stop. Require a separate authorized workflow for fixes.
- Keep the report in the response unless the user explicitly provides a writable destination outside the audited project; writing a report never authorizes project mutation.

If repository access is unavailable, request the repository or an archive. Do not infer project readiness from one pasted document when the task concerns repository-wide handoff.

## Run the audit

1. Resolve the repository boundary and requested audit lenses.
2. Capture a read-only baseline: branch, `HEAD`, worktree status, entry points, and relevant file inventory. Treat an existing dirty tree as evidence, not permission to repair it.
3. Read the project entry point completely. Follow its prescribed order and read every required artifact completely unless the project's own protocol explicitly permits a narrower path.
4. Identify authority by concern before resolving disagreements. Read [authority-and-drift.md](references/authority-and-drift.md) whenever multiple artifacts restate state, rules, decisions, or next actions.
5. Reconstruct purpose, scope, constraints, current phase, confirmed decisions, open and deferred decisions, implementation gate, last completed boundary, and exact next action.
6. Apply the requested audit lenses using [audit-workflow.md](references/audit-workflow.md). Run adversarial cross-assertion checks, not only a completeness checklist.
7. Simulate a fresh session from repository evidence. Record every guess, ambiguous transition, conflicting instruction, and fact recoverable only from history.
8. Classify findings with [finding-taxonomy.md](references/finding-taxonomy.md). Keep defects, open decisions, correct deferrals, and optional improvements distinct.
9. Assess handoff or implementation readiness with [readiness-report.md](references/readiness-report.md). Do not convert a roadmap gap into a present blocker unless the current gate requires it.
10. Recheck the worktree with the same read-only status command. If it changed, report the change and do not attempt cleanup.
11. Deliver the report and stop before project work begins.

## Require evidence

For every finding, include:

- classification and priority;
- artifact and tight section or line evidence;
- the conflicting or missing assertions;
- concrete risk to handoff, consistency, or implementation;
- minimal remediation without performing it;
- whether it belongs in the current project, a reusable workflow, or both.

Separate observed facts from inference. State confidence and list unresolved access or evidence limits.

## Preserve maintenance isolation

Do not modify this skill while using it on a project. Skill changes require a separate, explicitly authorized maintenance session with validation and fresh forward-tests.

## Surface reusable-workflow feedback

- Treat this skill as a reusable audit guide, not as infallible project authority. Do not silently follow or bypass an instruction that appears contradictory, disproportionate, obsolete, impossible, or harmful to the requested audit.
- Preserve the audited repository's read-only lock. If the suspected defect affects audit scope, evidence, or conclusions, pause the affected step, explain the instruction and consequence, and obtain the owner's disposition.
- If the issue is non-blocking and the audited repository's durable instructions authorize a configured destination outside the audited repository, follow that destination's instructions and template and create one `observed` feedback record there. If no authorized destination is configured, report the observation only in the response. This exception never authorizes a write inside the audited repository or a skill-file change.
- Notify the owner whenever a record is created. Feedback is evidence for a later, separate skill-maintenance session, not an audit finding or an approved skill change.
- Before delivering the final report, inspect the configured feedback backlog without changing prior records. Recommend maintenance when there are at least three unresolved records, one repeated problem, or one serious problem that blocked or risked an incorrect audit result. Also recommend review before a new project or stable skill release.
