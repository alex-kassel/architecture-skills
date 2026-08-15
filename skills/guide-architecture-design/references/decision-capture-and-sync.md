# Decision Capture and Synchronization

Own scenario interviews, confirmation classification, affected-document selection, and synchronization order. Use mutation eligibility and Git rules from `gates-recovery-and-git.md`.

## Ask for a decision

1. Select the highest-risk unresolved scenario owned by the current phase or queue.
2. State confirmed facts and constraints.
3. Separate assumptions, alternatives, tradeoffs, and recommendation.
4. Ask one concrete owner question.
5. Do not mutate while the answer remains exploratory, partial, conditional, objecting, or ambiguous.

Treat an answer as confirmed only when it unambiguously accepts a specific proposal or supplies a definitive choice for the active question. Never infer confirmation from silence or forward momentum.

## Plan the complete batch

Before the first write:

1. identify the canonical owner of the rule;
2. identify required rationale or supersession evidence;
3. enumerate every affected normative, roadmap, matrix, navigation, decision, worklog, time, and intended-new-file path;
4. include every validation command and its possible write scope;
5. run the complete zero-write eligibility preflight;
6. recheck the baseline immediately before mutation.

If any target or command scope is blocked, change nothing in that operation batch.

## Synchronize in order

1. Update the canonical rule and required rationale.
2. Update only derivatives affected by the decision.
3. Replace stale summaries instead of appending another restatement.
4. Record enabled decision/worklog outcomes.
5. Select one exact next unresolved scenario from its owning roadmap or queue.
6. Synchronize phase and navigation state.
7. Run only eligible configured validation.
8. Inspect the complete final diff for contradictions and unintended changes.

Do not copy project-specific detail into unrelated artifacts. Prefer direct references when a derivative need not restate a rule.

## Handle direct synchronization

Use direct synchronization without reconfirmation only when durable authority already marks the decision confirmed. If the claim exists only in conversation, worklog history, or an unauthoritative summary, return to owner confirmation or recovery.

## Finish the operation

If automatic commit is enabled and every commit prerequisite passes, create one focused local commit for the configured batch. Otherwise leave the eligible authorized changes uncommitted and report why; do not stage them.

Report documents changed, validation, commit status, exact next action, and whether the current session remains active. Do not ask another question unless the owner explicitly requested continuation.
