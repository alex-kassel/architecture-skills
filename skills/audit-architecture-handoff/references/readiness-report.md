# Readiness and Report

## Verdicts

Use one handoff verdict when handoff is in scope:

- `HANDOFF READY`: a fresh session can recover state and continue safely without prior conversation.
- `HANDOFF READY WITH FIXES`: continuation is possible, but bounded defects or friction should be corrected.
- `HANDOFF NOT READY`: a fresh session cannot identify or safely reach the next boundary without missing authority or owner input.

Use one implementation verdict when implementation readiness is in scope:

- `IMPLEMENTATION READY`: the declared scope is implementable and its project gate is satisfied.
- `IMPLEMENTATION READY WITH CONDITIONS`: no semantic blocker remains, but explicit bounded prerequisites must be completed before or during kickoff.
- `IMPLEMENTATION NOT READY`: unresolved semantics, contracts, ordering, acceptance criteria, or owner approval block safe implementation.
- `RELEASED (vX.Y.Z)`: code implementation is completed, tested, tagged, and published/deployed.
- `IN_DEVELOPMENT (vX.Y.Z-dev)`: active code implementation or development of a new version is underway.

Do not combine handoff and implementation verdicts: a project may be handoff-ready while intentionally far from implementation-ready. Verify that package statuses (`SPEC_IN_PROGRESS`, `IMPLEMENTATION_READY`, `IN_DEVELOPMENT`, `RELEASED`, `DEPRECATED`) in local roadmaps match root `AGENTS.md` Platform Status Matrix and Git release tags.

An `IMPLEMENTATION NOT READY` verdict is often the correct planned state of a documentation project. Do not present unfinished later phases or visible owner decisions as defects when the roadmap assigns them correctly and no one claims the gate is satisfied. List them under readiness gaps and correct deferrals. Create prioritized findings only when readiness evidence is contradictory, missing from its required owner, falsely marked complete, or being bypassed.

## Fresh-session canary

Describe the first actions a new working session would take until it reaches the next owner question or implementation kickoff. Include:

- entry point and reading order;
- repository and Git checks;
- recovery handling;
- recovered phase, last boundary, and next action;
- each guess or contradiction encountered;
- the point where mutation would first be authorized.

Stop the simulation before answering the open question.

## Report shape

Adapt sections to the requested lenses while preserving this order:

1. audit mode and scope;
2. verdict or verdicts;
3. confidence and evidence limits;
4. reconstructed project state;
5. fresh-session simulation when relevant;
6. authority map and drift assessment;
7. findings ordered by priority;
8. readiness gaps and correct deferrals;
9. minimal remediation sequence;
10. direct answer to whether a new session or implementation may start;
11. confirmation that no files, worklog, or Git state were changed.

Report no findings when none are supported. Do not manufacture cosmetic recommendations to fill sections. Keep raw evidence distinct from recommendations, and identify any conclusion that depends on inference.
