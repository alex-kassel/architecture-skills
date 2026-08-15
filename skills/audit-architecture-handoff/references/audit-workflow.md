# Audit Workflow

Select only the lenses needed by the request, but preserve the read-only lock for every lens.

## Fresh-session handoff

Reconstruct, without conversation history:

1. what is being designed and why;
2. scope, constraints, terminology, and dependency boundaries;
3. current roadmap phase and its exit criteria;
4. the last confirmed decision boundary;
5. open, deferred, and rejected alternatives;
6. the exact next action or owner question;
7. actions forbidden at the current phase;
8. the startup sequence a new working session would follow.

Flag every step that requires guessing. Check whether exact next action agrees across entry point, roadmap, tactical checkpoint, decision queue, and latest session summary when those artifacts exist.

## Architecture consistency

Cross-check assertions across and within normative documents:

- ownership and dependency direction;
- lifecycle, state, status, event, counter, and error semantics;
- admission, transaction, persistence, and dispatch ordering;
- nullability and validation combinations;
- mandatory behavior versus configurability or suppression;
- performance, security, compatibility, and operational constraints;
- phase gates versus detail intentionally reserved for later phases.

Test pairs of assertions against each other. A document can be complete section-by-section and still contradict itself across sections.

## Document drift

Compare canonical rules with summaries, matrices, roadmaps, worklogs, and Git history. Look for:

- stale terminology or ownership;
- a confirmed rule missing from a required derived artifact;
- a derived statement stronger or weaker than its canonical source;
- multiple different next actions;
- open questions presented as confirmed facts;
- superseded decisions without a visible supersession trail;
- normative facts stored only in worklog or commit messages.

Do not require every artifact to repeat every rule. Prefer references over duplication.

## Recovery and onboarding

Inspect active predecessor sessions, incomplete decision batches, dirty worktrees, uncommitted documents, missing timestamps, and unclear ownership. An active block is not inherently a defect while its owning session may still be running. The defect is an unsafe or unspecified transition for the scenario being audited.

Verify that audit-only and working-session startup are distinguishable. An audit must never create the state whose recoverability it is measuring.

## Implementation readiness

Read the project's own readiness criteria first. Then test whether behavior, contracts, state transitions, dependency direction, persistence and event ordering, failure handling, measurable quality constraints, acceptance coverage, explicit deferrals, and owner approval are sufficient for the declared implementation scope.

Do not demand concrete APIs, schemas, or operational detail before the roadmap phase that owns them. Do not lower the gate merely because later implementation could discover the answer.
