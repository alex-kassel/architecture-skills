---
name: guide-architecture-design
description: Guide owner-led, mutating documentation-as-code workflows for existing Git-backed software architecture and specification projects. Trigger this skill whenever the user asks to start or resume an architecture working session, continue a scenario-based design interview, record an owner-confirmed decision, propagate/sync architecture changes, recover an interrupted session or dirty worktree, checkpoint or close a design session, create project-configured focused commits, or check an implementation-readiness gate. Trigger on phrases like 'continue session', 'start session', 'record decision', 'sync documentation', 'checkpoint session', 'close session', 'resume design', or '+'. Do not use for independent audits, ordinary documentation maintenance, code implementation or review, non-Git project bootstrap, installed-skill maintenance, or broader Git operations.
---

# Guide Architecture Design

Guide the existing project through owner-led architecture decisions while keeping durable documentation, configured session state, and Git provenance consistent.

## Enforce the V1 boundary

- Work only in an existing Git-backed software architecture or specification project.
- Never confirm a product or architecture decision for the owner.
- Never begin or implement production software.
- Route independent handoff, consistency, drift, or readiness assessment to `audit-architecture-handoff` before any mutation.
- Keep audit and mutation as separate owner-authorized phases.
- Do not scaffold a new project, create a machine-readable state manifest, or prepare an implementation handoff bundle.
- Do not modify this or any installed skill. Route skill changes to a separate owner-authorized skill-development workflow using `skill-creator`.
- Do not rewrite history, merge unapproved branches, or perform direct unconfirmed pushes to primary production branches. V1 Git mutation is limited to eligible focused local commits or owner-configured session-branch Draft PR workflows.

## Route the request before mutation

1. Read the project entry point and required artifacts in their prescribed order. Inspect branch, `HEAD`, index, worktree, and history without writing state.
2. Resolve the user's intent before recovery, session binding, or worklog/time writes.
3. Route independent audit intent away from this skill. Route readiness-gate verification to its passive, sessionless evidence check. If no fresh `audit-architecture-handoff` report of `IMPLEMENTATION READY` (strictly matching `git rev-parse HEAD` with zero intervening commits) exists, report the blocking condition and instruct the owner to execute `audit-architecture-handoff` first.
4. For a mutating guide intent, recover the project operating contract from [operating-contract.md](references/operating-contract.md).
5. Select and follow the transition owned by [workflow-modes.md](references/workflow-modes.md). Do not force a design interview for direct synchronization, checkpoint, closing, or gate requests.
6. Before every mutating operation, apply the complete zero-write eligibility and recovery rules in [gates-recovery-and-git.md](references/gates-recovery-and-git.md).
7. For interviews, confirmation, direct synchronization, and affected-document ordering, follow [decision-capture-and-sync.md](references/decision-capture-and-sync.md).
8. Report the exact post-state and stop in `COMPLETE` after a one-shot request. Continue to another design question only when the user explicitly asked to continue.

## Output Templates & Decision Capture Format

### MADR Decision Record Template
When capturing decisions, write to `docs/decisions/ADR-XXXX-<title>.md` using this exact frontmatter structure:

```markdown
---
id: ADR-0001
title: "Short Decision Title"
status: "accepted" # draft | proposed | accepted | rejected | superseded
date: YYYY-MM-DD
deciders: ["Owner Name"]
supersedes: "ADR-0000"
---

# Title

## Context and Problem Statement
[Description]

## Decision Outcome
Chosen option: "[Option]", because [Rationale].
```

### Turn Response Summary Format
Adapt the opening line depending on context:
- Breakthrough proposal: `[Strong Decision] Explanation of why...`
- Risk / Pushback: `[Architectural Risk / Pushback] Counter-arguments and tradeoffs...`
- Operational / Routine: Omit special prefixes; start directly with concise answer.

## Preserve mandatory gates

Keep these controls enabled regardless of project configuration:

- authority by concern;
- explicit owner confirmation before decision capture;
- interrupted-session and dirty-state recovery;
- complete batch preflight before the first write;
- implementation gate backed by a fresh independent exact-ready verdict and durable contingent owner approval.

Worklog, duration tracking, decision register, and automatic commits remain project-configurable. Never create an optional artifact merely because this skill supports it.

## Preserve maintenance isolation

Refuse all skill-file mutation in this workflow. Skill maintenance requires a separate explicit owner request, `skill-creator`, `quick_validate.py`, and fresh independent forward-tests.

## Surface reusable-workflow feedback

- Treat this skill as a reusable guide, not as infallible project authority. Do not silently follow or bypass an instruction that appears contradictory, disproportionate, obsolete, impossible, or harmful to the owner's stated goal.
- If the suspected defect affects project behavior or state, pause before the affected action, identify the instruction and consequence, propose the smallest session disposition, and obtain the owner's decision.
- If the issue is non-blocking and the project's durable instructions authorize feedback writes, follow the configured destination's instructions and template, create one `observed` record, and continue unaffected work. If no authorized destination is configured, report the observation only in the response. Never edit skill files from this workflow.
- Notify the owner whenever a record is created. Keep project decisions in project authority and skill observations in the external feedback repository.
- At session close, inspect the configured feedback backlog without changing prior records. Recommend a separate skill-maintenance session when there are at least three unresolved records, one repeated problem, or one serious problem that blocked or risked an incorrect mutation. Also recommend review before a new project or stable skill release.
