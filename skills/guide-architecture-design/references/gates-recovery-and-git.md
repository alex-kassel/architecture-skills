# Gates, Recovery, and Git

Own mutation eligibility, cross-turn delta ownership, recovery, focused commits, failure containment, closure gates, and readiness gates.

## Run zero-write batch preflight

Before every operation batch:

1. snapshot branch, `HEAD`, status, baseline index, staged and unstaged diffs, untracked paths, and relevant ignored paths;
2. enumerate every canonical, rationale, derived, roadmap, navigation, decision, worklog, time, intended-new-file, validator, hook, and command-touched path;
3. allow an existing target only when tracked and clean or when it contains only the exact guide-owned delta defined below;
4. allow a new target only when absent, not ignored, and not colliding with untracked content;
5. block direct edits of every pre-existing untracked or ignored target;
6. require each command's possible write scope to be known and disjoint from all pre-existing tracked changes, untracked files, and ignored files;
7. treat unknown or repository-wide write scope as blocked;
8. recheck the baseline immediately before writing.

One blocked target blocks the whole operation batch. Make zero changes.

## Preserve cross-turn ownership

When a successful guide batch remains uncommitted, keep an in-conversation ownership record with baseline `HEAD`, baseline index, exact paths, and exact resulting staged/unstaged diffs or content digests.

Allow a later batch in the same owner-confirmed active session to update those paths only when the repository delta matches the record exactly and no external change appeared. Update the record after every successful batch.

Treat mismatch, lost conversation ownership, fresh session, or uncertain attribution as `RECOVERY`. Preserve the delta and ask the owner. This working record is not a project state manifest.

## Recover safely

- Never invent an end timestamp, close another session silently, discard a diff, or reuse a block without authority.
- Resume a predecessor only when the owner confirms this conversation owns the still-active session.
- Close a predecessor only from an owner-supplied or approved boundary with source and precision.
- Open a new exclusive session only after its predecessor is closed or explicitly non-conflicting.
- Preserve a valid session-start batch when a later decision batch is blocked; close it only in a separately eligible operation.

## Commit conservatively

- Never disturb a pre-existing index. A non-empty baseline index disables automatic commit.
- When automatic commit is disabled or blocked, do not stage.
- Disable automatic commit when any applicable local or configured `pre-commit`, `prepare-commit-msg`, `commit-msg`, `post-commit`, or equivalent hook may run.
- Run every blocking validation as a fail-fast gate. Confirm its successful exit before starting any later gate, staging, or commit; use separate tool calls or explicit fail-fast control, never a `;`-separated sequence that can continue after failure.
- Keep whitespace validation enabled. Classify each finding as accidental authored whitespace, an intentional Markdown hard break, immutable verbatim source, or pre-existing historical content. Preserve immutable source, document intentional exceptions, apply strict checks to authored normative content, and do not stage or commit while any finding is unclassified.
- Stage explicit eligible paths only immediately before an otherwise eligible commit, after mutation and every validation gate pass.
- Recheck that the staged diff contains only the intended classified batch.
- Create only a focused local commit. Do not reset, stash, rewrite history, switch branches, merge, push, tag, or open a pull request.

## Contain failure

If an edit fails mid-batch, validation fails, an unexpected file or index change appears, or a commit attempt fails:

1. stop mutation and do not claim capture, checkpoint, or closing success;
2. do not clean, reset, unstage, delete, bypass hooks, or hide the partial state;
3. preserve command output, intended and partial changes, index state, and side effects;
4. report exact completed and incomplete steps;
5. transition to `RECOVERY` for a classified, authorized continuation.

Permit a deterministic mechanical retry without renewed owner confirmation only when the original authorization, scope, target, intended result, known cause, attribution, baseline, and external state are provably unchanged; the correction is non-destructive, makes no product or architecture decision, and remains within the original operation. Give a short commentary update, apply the correction, repeat relevant preflight and validation, and preserve the same commit gates. Examples include creating an already approved missing destination directory before repeating the exact copy, correcting an unambiguous command or quoting error without changing intent, or retrying the same Git operation through the standard sandbox escalation path after a denial that occurred before index mutation.

Stop and obtain owner direction for an unknown cause, expanded scope, foreign or unattributed change, uncertain partial write, index mismatch, destructive cleanup, substantive validation failure, architectural choice, or any retry not demonstrably covered by the original authorization. If staging already occurred, preserve the index and do not autonomously clean it.

## Enforce closing

Freeze the decision boundary, make the last confirmed decision durable, synchronize navigation and exact next action, close enabled worklog/time records truthfully, run eligible configured validation, and apply the configured commit boundary. Do not claim clean closure when any enabled criterion fails. With commits disabled, report the intentional guide-owned uncommitted boundary defined by the project.

## Enforce implementation readiness

Require all of the following at one clean candidate `HEAD`:

- project-defined architecture and specification exit criteria complete;
- explicit deferrals with impact;
- required acceptance or test traceability;
- owner approval already recorded durably and explicitly contingent on a fresh exact-ready audit;
- a fresh independent `audit-architecture-handoff` verdict of exactly `IMPLEMENTATION READY` for the same repository, scope, clean worktree, and exact `HEAD`.

Treat conditional, negative, stale, dirty-worktree, wrong-scope, or wrong-`HEAD` evidence as blocked. After any relevant change, require a new audit. Final gate verification creates no session and mutates nothing; report `IMPLEMENTATION GATE OPEN` only when every condition matches.
