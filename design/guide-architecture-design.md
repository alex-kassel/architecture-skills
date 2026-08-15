# Guide Architecture Design — Pre-Implementation Design

## Purpose and V1 scope

Create a mutating Codex workflow for existing Git-backed documentation-as-code projects that design software architecture and implementation specifications through owner-led decisions.

V1 supports:

- working-session startup and continuation;
- scenario-based design interviews;
- capture of explicitly owner-confirmed decisions;
- synchronization of normative and derived documents;
- interrupted-session and dirty-worktree recovery;
- checkpoints and session closing;
- optional focused Git commits;
- enforcement of an implementation-readiness gate.

V1 does not scaffold a new documentation project, implement production software, prepare an implementation handoff bundle, or modify its own or any installed skill files.

## Trigger boundary

Use the guide for an existing Git-backed software architecture or specification project when the user asks to start or resume a working session, continue a design interview, record a confirmed decision, propagate or repair documentation for a decision already confirmed in durable authority, recover an interrupted session, checkpoint progress, close a session, or apply the implementation gate using current independent audit evidence.

Do not use it for ordinary documentation maintenance, code implementation, ordinary code review, or an independent read-only audit. Route independent handoff, consistency, drift, and readiness assessment to `audit-architecture-handoff`. When readiness intent is ambiguous, independent audit takes precedence over this mutating gate. A request combining audit and fixes must keep the audit as a separate read-only phase; mutation requires a later explicit owner transition.

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

Reject non-Git projects in V1 without mutation and explain that their provenance, dirty-state, and readiness boundaries are outside the supported operating model.

## Authority and confirmation

Resolve authority by concern rather than one total hierarchy. Typical concerns are normative behavior, decision rationale, program phase, workflow, navigation, history, and provenance.

Only the owner can confirm an architecture or product decision. Treat a response as confirmation only when it unambiguously accepts a specific proposal or supplies a definitive choice in response to the active question. Treat exploration, objections, partial answers, conditional language, and silence as unconfirmed.

Do not write an unconfirmed proposal as truth. Preserve it as conversation context or an explicitly proposed alternative only when the project has an authorized place for proposals.

When a decision is confirmed:

1. identify its canonical owner;
2. enumerate the complete mutation batch: canonical, rationale, derived, decision, navigation, roadmap, worklog, time, and validator-touched paths;
3. verify every target and command side-effect scope is eligible before the first write; if any target is blocked, change nothing;
4. update the canonical rule and rationale required by the project;
5. update only affected derived artifacts;
6. replace stale summaries instead of accumulating another restatement;
7. select the next unresolved high-risk scenario from the owning roadmap or queue;
8. validate cross-document consistency before any commit.

## Workflow modes and transitions

### `STARTUP`

When worklog or time tracking is enabled, use the host message timestamp when available; otherwise observe the system clock at the first tool opportunity and label it `observed_at`, never `request_at`. Record source, timezone, and precision whenever chronology or duration depends on a value. Read the entry point and required documents in their prescribed order, inspect Git, reconstruct the current state, and check for contradictions. Write no session or time start until intent preflight, recovery, and session binding are clear.

Transition to `INTENT_PREFLIGHT` without mutating project or session state.

### `INTENT_PREFLIGHT`

Resolve the requested intent before recovery or session binding:

- Route an independent handoff, consistency, drift, or readiness assessment to `audit-architecture-handoff` and stop this guide.
- Route final implementation-gate verification directly to `READINESS_GATE` after baseline inspection. Treat dirty worktree, stale evidence, wrong scope, wrong `HEAD`, or negative verdict as gate inputs that produce a blocked terminal result; do not recover or mutate them during gate evaluation.
- If intent or mutation authority is ambiguous, ask the owner and remain non-mutating.
- For a mutating guide intent, enter `RECOVERY` on any active predecessor whose liveness, exclusivity, resumption authority, or closure boundary is unresolved, even when its nominal owner is known. Also enter recovery for a dirty worktree, incomplete decision batch, divergent next actions, or ambiguous authority. Otherwise transition to `SESSION_BINDING`.

### `RECOVERY`

Preserve all existing changes. Inspect staged and unstaged diffs and history read-only, classify ownership and state, and ask the owner for any boundary that cannot be recovered. Never invent an end timestamp, close another session silently, discard a diff, or reuse a block without authority.

Resume the same session or block only when the owner confirms that the current conversation owns it and that it remains active. Close it only from an owner-supplied or owner-approved boundary with source and precision recorded when time tracking is enabled. Open a new session only after its predecessor is closed or explicitly confirmed non-conflicting and the repository state is validated.

Transition to `SESSION_BINDING` only after the owner or durable evidence resolves the boundary and any authorized recovery mutation is complete.

### `SESSION_BINDING`

Bind the current request to session state after startup or recovery and before intent dispatch. Treat session binding as its own operation batch: preflight every session/worklog/time target before writing the start, then complete and report that batch independently of any later decision:

- If the owner confirms that this conversation resumes the active predecessor, reuse its session, current block, and any active time record; do not create another start record.
- If a new working session is authorized after recovery, observe an effective session-start timestamp at the resolved boundary. It must not precede an exclusive predecessor's owner-approved end. Preserve earlier host or observation evidence only under its truthful label or in a configured recovery-time record; do not mislabel it as the new session start.
- If a new working session is authorized and worklog tracking is enabled, write exactly one session and initial-block start using the effective session-start timestamp and configured precision. Do not write it twice after recovery.
- If worklog tracking is disabled, keep the session binding in the active conversation and create no worklog or session artifact. When time tracking is enabled, still open exactly one record in its separately configured time artifact using the effective session-start timestamp.
- If the request is closing-only, bind only to an existing owner-confirmed active session. When none exists, remain non-mutating and ask which boundary the owner intends to close; never open a session solely to close it.
- For direct synchronization or checkpoint requests, follow the project's declared rule for whether they require a working session. Ask when that rule is ambiguous.

Transition to `INTENT_DISPATCH` only after this binding is resolved.

## Cross-turn transaction model

Treat every user request that may mutate state as a separate operation batch with its own complete preflight. Do not require a startup batch to predict documents that a later, not-yet-confirmed decision may affect.

When a completed guide batch remains uncommitted, keep an in-conversation ownership record containing the baseline `HEAD`, baseline index, exact affected paths, and exact resulting staged and unstaged diffs or content digests. A later batch in the same owner-confirmed active session may update those paths only when the current repository delta matches that record exactly and no external or unclassified change appeared. Update the record after each successful batch.

Do not treat a matching guide-owned delta as unrelated user work. Treat any mismatch, lost conversation ownership, fresh session, or uncertain attribution as `RECOVERY`; preserve the delta and require owner resolution before editing. This in-conversation record is working state, not the deferred machine-readable project manifest.

When automatic commits are disabled, a later closing batch may update the same worklog or time artifact only through this exact-delta ownership rule. If a downstream decision target is blocked, leave the already valid session-start batch intact, report that no decision capture occurred, and allow an independently preflighted closing batch.

### `INTENT_DISPATCH`

After startup or recovery, dispatch the user's requested operation without forcing a design interview:

| Requested intent | Next mode |
| --- | --- |
| Resume or ask the next architecture question | `READY` then `DESIGN_INTERVIEW` |
| Synchronize a decision already confirmed in durable authority | `DIRECT_SYNC` |
| Record a decision just confirmed in the active conversation | `DECISION_CAPTURE` |
| Check or advance a project checkpoint | `CHECKPOINT` |
| Close the current session | `SESSION_CLOSING` |
| Apply the implementation gate using current independent audit evidence | Already routed directly by `INTENT_PREFLIGHT`; do not bind a session |

If the requested intent or its mutation authority is ambiguous, ask the owner and remain non-mutating.

### `READY` and `DESIGN_INTERVIEW`

Restate phase, last confirmed boundary, constraints, and exact next action briefly. Present one concrete runtime, failure, operator, or developer scenario. Distinguish confirmed facts, assumptions, alternatives, and recommendation. Ask one decision question at a time.

Remain non-mutating while the decision is unconfirmed. On explicit confirmation, transition to `DECISION_CAPTURE`.

### `DIRECT_SYNC`

Use direct synchronization only when durable project authority already records the decision as confirmed and the request is to repair or propagate its documentation. Do not demand reconfirmation of an already authoritative decision. If only conversation or an unauthoritative summary contains the claim, return to owner confirmation or recovery instead.

Apply the same synchronization, validation, overlap, failure, and commit rules as `DECISION_CAPTURE`.

### `DECISION_CAPTURE`

Synchronize the canonical and affected derived documents, record rationale or supersession when required, update enabled decision/worklog artifacts, and choose one exact next action. Validate links, Markdown, internal assertions, phase state, and the diff.

Before the first write, resolve the complete batch and run the eligibility preflight defined under Git and mutation safety. Recheck the baseline immediately before mutation. Do not partially begin a batch whose later target or validator scope is already blocked.

If automatic commits are enabled, commit only the scoped, validated decision batch when it can be isolated from pre-existing staged, unstaged, and same-file user changes. If disabled or isolation is unsafe, leave the authorized changes visible and report them without committing. Never include or unstage unrelated user changes.

Transition to `READY` only when the user explicitly asked to continue with another design question. Transition to `CHECKPOINT` or `SESSION_CLOSING` only when requested. Otherwise report the exact post-state and transition to `COMPLETE`.

### `CHECKPOINT`

Compare current evidence with phase exit criteria. Update phase status only when its criteria are met and any required owner approval is explicit. Synchronize navigation and next action. Run project-configured validation and create a focused commit only when enabled.

After a one-shot checkpoint request, report the exact phase, repository, session, and next-action state and transition to `COMPLETE`. Continue to `READY` only when the user explicitly asked to resume the interview.

### `SESSION_CLOSING`

Freeze the decision boundary and do not start a new question. Ensure the last confirmed decision is durable, run continuity checks, synchronize navigation, close enabled worklog/time records with actual evidence, validate the repository, and create project-configured closing commits.

Do not claim a clean close when enabled closure criteria remain unmet. If automatic commits are disabled, report the intentional uncommitted boundary and follow the project's configured definition of closure.

On successful closing, report the closed boundary and transition to `COMPLETE`. Do not start another question.

### `READINESS_GATE`

Do not independently certify the project from the same mutating workflow. Require:

- completion of project-defined architecture and specification exit criteria;
- explicit representation and impact of deferrals;
- traceability to acceptance or tests as required by the project;
- owner approval already recorded durably at the candidate `HEAD`, explicitly contingent on a fresh exact-ready independent audit;
- a fresh independent `audit-architecture-handoff` verdict of exactly `IMPLEMENTATION READY`, bound to the current repository, declared implementation scope, clean worktree, and exact audited `HEAD`;

Treat `IMPLEMENTATION READY WITH CONDITIONS` and `IMPLEMENTATION NOT READY` as insufficient. After conditions are discharged, require a fresh independent audit that returns exactly `IMPLEMENTATION READY`. Invalidate a prior positive verdict after any relevant architecture, specification, scope, gate, worktree, or `HEAD` change.

Make final gate verification sessionless and mutation-free so it cannot invalidate its own evidence. If every condition matches, report `IMPLEMENTATION GATE OPEN` for the exact audited `HEAD` and transition to `COMPLETE` without editing the repository. If any condition is unmet, stale, negative, or scoped to a different boundary, keep implementation blocked, report the smallest next documentation action, and transition to `COMPLETE`. Crossing the gate does not authorize this skill to implement software.

Any required readiness preparation, including recording the contingent owner approval, occurs in an earlier mutating checkpoint that is validated and committed before the independent audit. The final audit runs only after that checkpoint leaves a clean candidate `HEAD`.

### `COMPLETE`

Treat `COMPLETE` as the terminal state for the requested one-shot operation. Report whether a project session remains active, whether changes are committed, the exact next action, and any blocked condition. Do not ask another design question or perform another mutation unless the user supplies a new request.

## Configurable subsystems

| Subsystem | Disabled behavior | Enabled behavior |
| --- | --- | --- |
| Worklog | Do not create or update one | Record session/block event timestamps using its declared path and schema; duration tracking is separate |
| Time tracking | Do not calculate or store duration | Use its configured artifact; record timestamps with source, timezone, and precision, and subtract only explicit declared breaks |
| Decision register | Keep decision state in existing authoritative artifacts | Maintain configured IDs, status, owner, links, and one next decision |
| Automatic commits | Never commit | Commit only scoped validated batches using project rules |

The authority model, owner-confirmation gate, recovery safety, and implementation gate are mandatory and cannot be disabled.

Support the four worklog/time combinations explicitly:

| Worklog | Time tracking | Startup and closing behavior |
| --- | --- | --- |
| Off | Off | Create no session or time artifact and require no timestamp record |
| On | Off | Record observed session/block start and end event timestamps with source, timezone, and precision; do not calculate durations or pauses |
| Off | On | Write sourced start, end, breaks, and duration to the separately configured time artifact; create no worklog |
| On | On | Write worklog event timestamps and configured time/duration fields without duplicating records outside the declared schema |

Reject `time tracking = on` when no time artifact or time-capable worklog schema is configured. Event timestamps needed to order a worklog are not themselves optional duration tracking.

## Git and mutation safety

- Treat a dirty tree as user work until classified.
- Snapshot branch, `HEAD`, status, staged diff, unstaged diff, and untracked paths before editing; diff every affected artifact afterward.
- Build one batch-wide plan before the first write. Enumerate every canonical, rationale, derived, decision, roadmap, navigation, worklog, time, intended-new-file, and validator- or command-touched path. Resolve ownership and expected side effects for the whole batch.
- Allow an existing target when it is tracked and either clean or contains only an exact guide-owned delta from the current owner-confirmed active session. Allow an intended new path only when it is absent, not ignored, and does not collide with untracked content. Any unclassified or blocked target blocks the entire operation batch; make zero changes in that batch.
- Do not directly edit a pre-existing untracked or ignored target in V1, even when its content was hashed. Require the owner to move it into a clean recoverable boundary or otherwise resolve it outside this workflow first.
- Permit a validator, hook, or other command only when its possible write scope is known and disjoint from all pre-existing tracked changes, untracked files, and ignored files. Treat unknown or repository-wide write scope as blocking. Detection by hash is not preservation and does not make execution safe.
- Never disturb the pre-existing index.
- If the baseline index contains any staged change, do not run an automatic commit in V1, even when the skill's target paths are otherwise clean. Leave the authorized batch uncommitted and report the staged boundary.
- Before any automatic commit, verify that no applicable local or configured commit hook exists. If any `pre-commit`, `prepare-commit-msg`, `commit-msg`, `post-commit`, or configured equivalent may run, leave the batch uncommitted in V1. Recheck the staged diff immediately before committing and require it to match only the intended classified batch.
- Treat every blocking validation as a fail-fast gate whose successful exit must be confirmed before any later gate, staging, or commit. Use separate tool calls or explicit fail-fast control; never use `;` sequencing that can continue after failure. Keep whitespace validation enabled and classify every finding as accidental authored whitespace, an intentional Markdown hard break, immutable verbatim source, or pre-existing historical content. Preserve immutable source, document intentional exceptions, enforce strict checks on authored normative content, and block staging and commit while any finding is unclassified.
- Stage explicit paths only immediately before an otherwise eligible automatic commit, after mutation, every validation gate, hook, baseline-index, and isolation check pass. When automatic commits are disabled or any prerequisite is already blocked, do not stage and leave the baseline index unchanged.
- If ownership cannot be isolated safely, preserve the current state, report the overlap, and require owner direction.
- Do not rewrite history, reset, discard, stash, switch branches, merge, push, tag, or open a pull request in V1. Route those operations to a separate explicitly authorized Git workflow.
- Stop when required mutation would exceed the repository or permission scope.
- Never edit `guide-architecture-design` or another installed skill in V1. Refuse the mutation and route it to a separate explicitly owner-authorized skill-development workflow that uses `skill-creator`, validation, and fresh forward-tests. Maintenance is not a mode or transition of this guide.

## Failure and side-effect handling

Run only project-configured validation commands whose possible write scope is known, preflighted, and disjoint from all pre-existing user content. After each mutation group, validator, and commit attempt, compare the full repository and index state with the baseline and batch plan.

If a document update fails mid-batch, validation fails, a command creates unexpected files, the index changes unexpectedly, or a commit hook fails:

1. stop further mutation and do not claim capture, checkpoint, or closing success;
2. do not clean, reset, unstage, delete, retry with hook bypass, or hide the partial state;
3. preserve command output, intended changes, partial changes, index state, and unexpected side effects;
4. report the exact completed and incomplete steps;
5. transition to `RECOVERY` and require a classified, authorized continuation.

Permit a deterministic mechanical retry without renewed owner confirmation only when the original authorization, scope, target, intended result, known cause, attribution, baseline, and external state are provably unchanged; the correction is non-destructive, makes no product or architecture decision, and remains within the original operation. Give a short commentary update, apply the correction, repeat relevant preflight and validation, and preserve the same commit gates. This covers an already approved missing destination directory followed by the exact copy, an unambiguous command or quoting correction with unchanged intent, and the same Git operation through standard sandbox escalation after a pre-index permission denial.

Require owner direction for an unknown cause, scope expansion, foreign or unattributed change, uncertain partial write, index mismatch, destructive cleanup, substantive validation failure, architectural choice, or any recovery not demonstrably covered by the original authorization. If staging already occurred, preserve the index without autonomous cleanup.

Report success only when intended documents are synchronized, configured validation passes, the final diff contains only classified changes, and any enabled commit completes without absorbing unrelated work.

## Reusable resources

Keep `SKILL.md` concise and link directly to one-level references:

- `operating-contract.md` — own input discovery, project configuration, and concern-based authority mapping;
- `workflow-modes.md` — own intent dispatch and state transitions from startup through terminal completion;
- `decision-capture-and-sync.md` — own scenario interviews, confirmation classification, affected-document selection, and synchronization ordering;
- `gates-recovery-and-git.md` — own mutation eligibility, cross-turn delta ownership, recovery invariants, Git/commit safety, failure containment, closure gates, and readiness gates.

Link to the owning reference instead of restating its normative rules in another reference. A mode may point to a safety gate, but it must not redefine that gate.

Do not create mutation scripts or assets in V1.

## Acceptance scenarios

1. Resume a consistent project with worklog and auto-commit disabled without creating either.
2. Ask one scenario question and make no file change after an exploratory or ambiguous answer.
3. Synchronize all affected documents after explicit confirmation and create a focused commit only when configured.
4. Preserve a dirty tree and active predecessor until the owner resolves ownership and timing.
5. Close a session correctly under different worklog, time, and commit configurations.
6. Dispatch direct checkpoint, closing, durable-decision synchronization, and readiness requests without forcing a new interview.
7. Resume an owner-confirmed active block without creating another start, open exactly one new tracked session after recovery when authorized, and refuse a closing-only request with no bound session.
8. Block implementation for negative, conditional, stale, dirty-worktree, wrong-scope, or wrong-HEAD audit evidence; require a fresh exact-ready verdict after conditions are discharged.
9. Prepare and commit contingent owner approval before the final audit, then verify the exact clean audited `HEAD` without session or repository mutation.
10. Exercise all four worklog/time configurations, including one non-duplicated separate time record when worklog is disabled and time tracking is enabled.
11. Complete one-shot direct sync, decision capture, checkpoint, closing, and gate requests without asking an unrequested next question.
12. Make zero batch changes when any canonical, derived, navigation, history, time, decision, intended-new-file, or validator-touched target is blocked at preflight.
13. Make zero file changes whenever a target file contains any pre-existing staged or unstaged user diff.
14. Make zero file changes when the requested target already exists only as an untracked or ignored file.
15. Do not run a validator whose possible write scope is unknown or intersects a pre-existing tracked change, untracked file, or ignored file.
16. Leave a batch uncommitted when any applicable commit hook exists, including a hook that could successfully stage an unrelated tracked file.
17. Keep the baseline index unchanged when automatic commits are disabled or already blocked before staging.
18. Preserve and report partial state after a mid-batch edit failure, validator side effect, or commit-hook failure.
19. Use a post-recovery effective start that does not overlap an exclusive predecessor; never duplicate a resumed session or time record.
20. Record timestamp source, timezone, and precision, and never label a later clock observation as the host request time.
21. Block implementation while readiness criteria, acceptable independent audit, or owner approval are missing.
22. Route general documentation maintenance and independent read-only readiness assessment away from this mutating workflow.
23. Refuse all installed-skill mutation and route it to a separate owner-authorized skill-development workflow.
24. With autocommit disabled, open a preflighted worklog/time session batch, preserve its exact guide-owned delta across a later decision batch, and close it without misclassifying the delta as user work.
25. Leave a valid session-start batch intact when a later decision target is blocked, then close the session in a separately eligible batch.
26. Route non-Git projects and all history rewriting, branch switching, merging, pushing, tagging, and pull-request operations out of V1.
27. Decline V1 project scaffolding while preserving a clear future extension boundary.
28. Make a failed blocking validation render staging and commit unreachable, including when a later command would otherwise succeed.
29. Preserve and classify immutable or intentional Markdown whitespace without weakening strict checks for authored normative content; block commit while any finding is unclassified.
30. Retry an approved missing-directory copy and a pre-index sandbox-denied Git operation mechanically, but stop for an ambiguous partial write or changed architectural intent.

## Deferred extensions and likely split

- Defer a machine-readable state manifest to iteration 2.
- Add new-project bootstrap only after the existing-project workflow is stable across contrasting projects.
- Treat `prepare-implementation-handoff` as a likely future skill when implementation kickoff artifacts, task graphs, dependency sequencing, and execution checkpoints create distinct triggers or resources. Do not create it in V1.
