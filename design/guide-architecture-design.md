# Guide Architecture Design — Pre-Implementation Design

## Purpose and V1 scope

Create a mutating Codex workflow for existing documentation-as-code projects that design software architecture and implementation specifications through owner-led decisions.

V1 supports:

- working-session startup and continuation;
- scenario-based design interviews;
- capture of explicitly owner-confirmed decisions;
- synchronization of normative and derived documents;
- interrupted-session and dirty-worktree recovery;
- checkpoints and session closing;
- optional focused Git commits;
- enforcement of an implementation-readiness gate.

V1 does not scaffold a new documentation project, implement production software, prepare an implementation handoff bundle, or modify its own skill files during project operation.

## Trigger boundary

Use the guide for an existing software architecture or specification project when the user asks to start or resume a working session, continue a design interview, record a confirmed decision, synchronize documentation, recover an interrupted session, checkpoint progress, close a session, or enforce the implementation gate.

Do not use it for ordinary code implementation, ordinary code review, or an independent read-only audit. Route independent handoff, consistency, drift, and readiness assessment to `audit-architecture-handoff`. A request combining audit and fixes must keep the audit as a separate read-only phase; mutation requires a later explicit owner transition.

## Project operating contract

Before any mutation, recover or obtain:

- repository boundary and user-granted write scope;
- conversation language and documentation language;
- authority owner for each concern;
- current phase, gate, last confirmed boundary, and exact next action;
- session and recovery state;
- Git branch, `HEAD`, status, and ownership of existing changes;
- whether worklog, time tracking, decision register, and automatic commits are enabled;
- paths and project-specific rules for every enabled feature.

Existing project protocols and artifacts configure these features. Do not create an optional artifact merely because the skill supports it. If a mutation depends on an ambiguous setting, ask the owner before changing state. Do not introduce a machine-readable state manifest in V1.

## Authority and confirmation

Resolve authority by concern rather than one total hierarchy. Typical concerns are normative behavior, decision rationale, program phase, workflow, navigation, history, and provenance.

Only the owner can confirm an architecture or product decision. Treat a response as confirmation only when it unambiguously accepts a specific proposal or supplies a definitive choice in response to the active question. Treat exploration, objections, partial answers, conditional language, and silence as unconfirmed.

Do not write an unconfirmed proposal as truth. Preserve it as conversation context or an explicitly proposed alternative only when the project has an authorized place for proposals.

When a decision is confirmed:

1. identify its canonical owner;
2. update the canonical rule and rationale required by the project;
3. update only affected derived artifacts;
4. replace stale summaries instead of accumulating another restatement;
5. select the next unresolved high-risk scenario from the owning roadmap or queue;
6. validate cross-document consistency before any commit.

## Workflow modes and transitions

### `STARTUP`

Capture the actual start timestamp in memory when time tracking is enabled. Read the entry point and required documents in their prescribed order, inspect Git, reconstruct the current state, and check for contradictions. Write the session/worklog start only after recovery is clear and only when the project enables it.

Transition to `RECOVERY` on any active predecessor whose liveness, exclusivity, resumption authority, or closure boundary is unresolved, even when its nominal owner is known. Also enter recovery for a dirty worktree, incomplete decision batch, divergent next actions, or ambiguous authority. Otherwise transition to `INTENT_DISPATCH`.

### `RECOVERY`

Preserve all existing changes. Inspect staged and unstaged diffs and history read-only, classify ownership and state, and ask the owner for any boundary that cannot be recovered. Never invent an end timestamp, close another session silently, discard a diff, or reuse a block without authority.

Resume the same session or block only when the owner confirms that the current conversation owns it and that it remains active. Close it only from an owner-supplied or owner-approved boundary with source and precision recorded when time tracking is enabled. Open a new session only after its predecessor is closed or explicitly confirmed non-conflicting and the repository state is validated.

Transition to `INTENT_DISPATCH` only after the owner or durable evidence resolves the boundary and any authorized recovery mutation is complete.

### `INTENT_DISPATCH`

After startup or recovery, dispatch the user's requested operation without forcing a design interview:

| Requested intent | Next mode |
| --- | --- |
| Resume or ask the next architecture question | `READY` then `DESIGN_INTERVIEW` |
| Synchronize a decision already confirmed in durable authority | `DIRECT_SYNC` |
| Record a decision just confirmed in the active conversation | `DECISION_CAPTURE` |
| Check or advance a project checkpoint | `CHECKPOINT` |
| Close the current session | `SESSION_CLOSING` |
| Evaluate whether implementation may begin | `READINESS_GATE` |

If the requested intent or its mutation authority is ambiguous, ask the owner and remain non-mutating.

### `READY` and `DESIGN_INTERVIEW`

Restate phase, last confirmed boundary, constraints, and exact next action briefly. Present one concrete runtime, failure, operator, or developer scenario. Distinguish confirmed facts, assumptions, alternatives, and recommendation. Ask one decision question at a time.

Remain non-mutating while the decision is unconfirmed. On explicit confirmation, transition to `DECISION_CAPTURE`.

### `DIRECT_SYNC`

Use direct synchronization only when durable project authority already records the decision as confirmed and the request is to repair or propagate its documentation. Do not demand reconfirmation of an already authoritative decision. If only conversation or an unauthoritative summary contains the claim, return to owner confirmation or recovery instead.

Apply the same synchronization, validation, overlap, failure, and commit rules as `DECISION_CAPTURE`.

### `DECISION_CAPTURE`

Synchronize the canonical and affected derived documents, record rationale or supersession when required, update enabled decision/worklog artifacts, and choose one exact next action. Validate links, Markdown, internal assertions, phase state, and the diff.

If automatic commits are enabled, commit only the scoped, validated decision batch when it can be isolated from pre-existing staged, unstaged, and same-file user changes. If disabled or isolation is unsafe, leave the authorized changes visible and report them without committing. Never include or unstage unrelated user changes.

Transition to `READY`, `CHECKPOINT`, or `SESSION_CLOSING` according to the user request and project protocol.

### `CHECKPOINT`

Compare current evidence with phase exit criteria. Update phase status only when its criteria are met and any required owner approval is explicit. Synchronize navigation and next action. Run project-configured validation and create a focused commit only when enabled.

### `SESSION_CLOSING`

Freeze the decision boundary and do not start a new question. Ensure the last confirmed decision is durable, run continuity checks, synchronize navigation, close enabled worklog/time records with actual evidence, validate the repository, and create project-configured closing commits.

Do not claim a clean close when enabled closure criteria remain unmet. If automatic commits are disabled, report the intentional uncommitted boundary and follow the project's configured definition of closure.

### `READINESS_GATE`

Do not independently certify the project from the same mutating workflow. Require:

- completion of project-defined architecture and specification exit criteria;
- explicit representation and impact of deferrals;
- traceability to acceptance or tests as required by the project;
- an independent `audit-architecture-handoff` verdict of `IMPLEMENTATION READY`, bound to the current repository, declared implementation scope, and current `HEAD` or explicitly recorded worktree snapshot;
- explicit owner approval to cross into implementation.

Accept `IMPLEMENTATION READY WITH CONDITIONS` only after every condition is discharged and the independent audit is rerun or explicitly confirms the discharged state. Reject `IMPLEMENTATION NOT READY`. Invalidate a prior positive verdict after any relevant architecture, specification, scope, or gate change.

If any condition is unmet, stale, negative, or scoped to a different boundary, keep implementation blocked and report the smallest next documentation action. Crossing the gate does not authorize this skill to implement software.

## Configurable subsystems

| Subsystem | Disabled behavior | Enabled behavior |
| --- | --- | --- |
| Worklog | Do not create or update one | Follow declared path, schema, and session/block rules |
| Time tracking | Do not invent timestamps or duration | Capture actual timestamps; subtract only explicit declared breaks |
| Decision register | Keep decision state in existing authoritative artifacts | Maintain configured IDs, status, owner, links, and one next decision |
| Automatic commits | Never commit | Commit only scoped validated batches using project rules |

The authority model, owner-confirmation gate, recovery safety, and implementation gate are mandatory and cannot be disabled.

## Git and mutation safety

- Treat a dirty tree as user work until classified.
- Snapshot branch, `HEAD`, status, staged diff, unstaged diff, and untracked paths before editing; diff every affected artifact afterward.
- Never disturb the pre-existing index. Stage explicit paths only when they contain no pre-existing staged or unstaged user hunks and no overlapping same-file work.
- If a target file contains user changes or ownership cannot be isolated safely, do not auto-commit the batch. Preserve both sets of changes, report the overlap, and require owner direction or a separate clean boundary.
- Do not rewrite history, reset, discard, stash, switch branches, merge, push, tag, or open a pull request unless separately requested and authorized.
- Stop when required mutation would exceed the repository or permission scope.
- Never edit `guide-architecture-design` or another installed skill during normal project operation. Require explicit owner-authorized maintenance mode, then validate and forward-test the skill separately.

## Failure and side-effect handling

Run only project-configured validation commands whose expected outputs and side effects are understood. After each mutation group, validator, and commit attempt, compare the full repository and index state with the baseline.

If a document update fails mid-batch, validation fails, a command creates unexpected files, the index changes unexpectedly, or a commit hook fails:

1. stop further mutation and do not claim capture, checkpoint, or closing success;
2. do not clean, reset, unstage, delete, retry with hook bypass, or hide the partial state;
3. preserve command output, intended changes, partial changes, index state, and unexpected side effects;
4. report the exact completed and incomplete steps;
5. transition to `RECOVERY` and require a classified, authorized continuation.

Report success only when intended documents are synchronized, configured validation passes, the final diff contains only classified changes, and any enabled commit completes without absorbing unrelated work.

## Reusable resources

Keep `SKILL.md` concise and link directly to one-level references:

- `operating-contract.md` — inputs, configuration, and authority recovery;
- `workflow-modes.md` — startup through closing transitions;
- `decision-capture-and-sync.md` — scenario interview, confirmation, canonical and derived updates;
- `gates-recovery-and-git.md` — safety, recovery, commits, closure, and readiness.

Do not create mutation scripts or assets in V1.

## Acceptance scenarios

1. Resume a consistent project with worklog and auto-commit disabled without creating either.
2. Ask one scenario question and make no file change after an exploratory or ambiguous answer.
3. Synchronize all affected documents after explicit confirmation and create a focused commit only when configured.
4. Preserve a dirty tree and active predecessor until the owner resolves ownership and timing.
5. Close a session correctly under different worklog, time, and commit configurations.
6. Dispatch direct checkpoint, closing, durable-decision synchronization, and readiness requests without forcing a new interview.
7. Block implementation for negative, conditional-with-unmet-conditions, stale, wrong-scope, or wrong-HEAD audit evidence.
8. Leave a batch uncommitted when a target file has pre-staged, unstaged, or overlapping user changes.
9. Preserve and report partial state after a mid-batch edit failure, validator side effect, or commit-hook failure.
10. Block implementation while readiness criteria, acceptable independent audit, or owner approval are missing.
11. Route an independent read-only audit away from this mutating workflow.
12. Refuse self-modification outside explicit maintenance mode.
13. Decline V1 project scaffolding while preserving a clear future extension boundary.

## Deferred extensions and likely split

- Defer a machine-readable state manifest to iteration 2.
- Add new-project bootstrap only after the existing-project workflow is stable across contrasting projects.
- Treat `prepare-implementation-handoff` as a likely future skill when implementation kickoff artifacts, task graphs, dependency sequencing, and execution checkpoints create distinct triggers or resources. Do not create it in V1.
