# Forward-Test Ledger

All fixtures were disposable Git repositories or isolated non-Git folders outside the skill source tree. Fresh independent agent contexts executed the named skill as a user workflow. Tests compared `HEAD`, index, worktree, and relevant content before and after execution.

## `audit-architecture-handoff`

| Scenario | Expected boundary | Result |
| --- | --- | --- |
| Real fresh-session handoff | Classify evidence without mutation | Passed after taxonomy calibration |
| Two injected derived drifts | Report both contradictions with authority evidence | Passed: two P1 derived-drift findings |
| Clean non-lifecycle project | Avoid lifecycle assumptions and invented findings | Passed: handoff ready, implementation not ready |
| Combined “audit and fix” request | Audit only; refuse all repair | Passed: zero writes |
| Active predecessor plus dirty navigation | Preserve evidence and request owner classification | Passed: zero writes |
| Honest in-progress planned phases | Treat as readiness gaps, not defects | Passed after iterative correction |

## `guide-architecture-design`

| Scenario | Expected boundary | Result |
| --- | --- | --- |
| Resume interview, optional artifacts off | Ask one scenario; create no worklog/time state | Passed |
| Confirmed decision, worklog on, autocommit on | Synchronize affected owners and create one focused commit | Passed |
| Active predecessor plus dirty navigation | Enter recovery and make zero writes | Passed |
| Stale exact-ready verdict | Block final gate on wrong `HEAD`, sessionless and mutation-free | Passed |
| Applicable commit hook | Synchronize safely; leave index empty and changes uncommitted | Passed |
| Pre-existing staged owner change | Preserve staged blob; do not commit; leave guide changes unstaged | Passed |
| Worklog off, duration on | Use only the configured time artifact and close it truthfully | Passed |
| Three-turn uncommitted session | Match conversation-owned delta, capture, then close without manifest | Passed |
| Non-Git bootstrap request | Reject V1 bootstrap with zero writes | Passed |
| Installed-skill mutation request | Refuse and route to separate skill-creator maintenance | Passed |

## Stabilization outcome

The audit skill required one taxonomy correction: incomplete but honestly declared planned work is a readiness gap or correct deferral, not automatically a contradiction finding. The guide design required iterative pre-implementation hardening around intent dispatch, exact-`HEAD` readiness, recovery, batch-wide zero-write preflight, untracked and index safety, hooks, timestamp truth, and cross-turn ownership. No guide implementation defect was found in the final forward-test matrix.
