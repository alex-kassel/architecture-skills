# Workflow Modes

Own intent dispatch and state transitions. Apply safety gates from `gates-recovery-and-git.md` without restating them.

## `STARTUP`

Read prescribed context, inspect Git, reconstruct the boundary, and record only in-memory time evidence. Write no session or project state. Transition to `INTENT_PREFLIGHT`.

## `INTENT_PREFLIGHT`

- Route independent audit to `audit-architecture-handoff` and stop this guide.
- Route final gate verification directly to `READINESS_GATE` without recovery or session binding; dirty or stale state becomes a blocked gate result.
- Perform a preflight documentation alignment check: audit consuming project documentation (`AGENTS.md`, roadmaps, `docs/`) against installed skills. If duplication or contradiction exists, pause before mutation, present the conflict to the owner with options (Option A: align project docs to skill; Option B: create skill feedback record if project rule is superior/intentional), and provide an expert community-backed recommendation on which option is preferable.
- Ask the owner when intent or mutation authority is ambiguous.
- For a mutating guide request, enter `RECOVERY` when predecessor, dirty state, batch, next action, or authority is unresolved; otherwise enter `SESSION_BINDING`.

## `RECOVERY`

Preserve all evidence and obtain owner input for irreducible boundaries. Resume, close, or replace a predecessor only under the recovery invariants in `gates-recovery-and-git.md`. Transition to `SESSION_BINDING` only after the boundary is resolved.

## `SESSION_BINDING`

Treat binding as its own preflighted operation batch.

- Resume an owner-confirmed active session without duplicating session, block, or time starts.
- Open exactly one new configured session/time record at the effective start after recovery.
- With worklog off and duration tracking on, open only the configured time record.
- For closing-only intent, bind to an existing owner-confirmed active session; never open a session solely to close it.
- Follow the project rule for whether direct synchronization or checkpoint needs a working session.
- When configured for session-branch mode, create dedicated branch `agent/session-<ID>`, push initial commit, open Eager Draft PR, and provide live PR URL to the owner.

Transition to `INTENT_DISPATCH` after binding completes.

## `INTENT_DISPATCH`

| Intent | Mode |
| --- | --- |
| Resume or ask the next scenario | `READY` then `DESIGN_INTERVIEW` |
| Propagate durable confirmed authority | `DIRECT_SYNC` |
| Capture a decision confirmed in this conversation | `DECISION_CAPTURE` |
| Check or advance phase evidence | `CHECKPOINT` |
| Close the bound session | `SESSION_CLOSING` |

## `READY` and `DESIGN_INTERVIEW`

Restate phase, last boundary, constraints, and next action briefly. Present one concrete runtime, failure, operator, or developer scenario. Ask one owner question and remain non-mutating until confirmation.

## `DIRECT_SYNC` and `DECISION_CAPTURE`

Use `DIRECT_SYNC` only for a decision already confirmed in durable authority. Use `DECISION_CAPTURE` only after explicit owner confirmation in the active conversation. Follow `decision-capture-and-sync.md`, then transition to the requested checkpoint or closing mode. Otherwise enter `COMPLETE`; enter `READY` only when continuation was explicitly requested.

## `CHECKPOINT`

Compare evidence with exit criteria and update phase state only when criteria and required approval are satisfied. After a one-shot checkpoint enter `COMPLETE`; continue only by explicit request.

## `SESSION_CLOSING`

Freeze the decision boundary, synchronize enabled closure artifacts, validate the configured closure gate, report the closed or blocked state, and enter `COMPLETE`. When operating in a session-branch Draft PR workflow, upon explicit owner confirmation (`+` or "merge PR"), execute a squash merge into `main` (`gh pr merge --squash --delete-branch` or local git fallback), delete the session branch, and report the merged state. Do not ask a new question.

## `READINESS_GATE`

Perform only the sessionless, mutation-free evidence check owned by `gates-recovery-and-git.md`. Report `IMPLEMENTATION GATE OPEN` or the smallest blocking condition and enter `COMPLETE`.

## `COMPLETE`

Report repository, session, commit, next-action, and blocked state. Perform no further mutation or interview until the user supplies a new request.
