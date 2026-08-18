# Decision Capture and Synchronization

Own scenario interviews, confirmation classification, affected-document selection, and synchronization order. Use mutation eligibility and Git rules from `gates-recovery-and-git.md`.

## Ask for a decision and evaluate pushback

1. Select the highest-risk unresolved scenario owned by the current phase or queue.
2. State confirmed facts and constraints.
3. Separate assumptions, alternatives, tradeoffs, and recommendation.
4. Exercise critical thinking and architectural vigilance:
   - If a proposed direction presents technical, safety, consistency, or architectural risks, do not passively accept it.
   - Provide one clear, well-reasoned attempt of pushback, elaborating the technical rationale and trade-offs. Architectural vigilance and this 1-attempt pushback take precedence over fast confirmation phrases (e.g. `+`).
   - If the owner explicitly reaffirms after this 1 clear attempt, accept the owner's disposition without further obstruction.
5. Ask up to 2-3 tightly linked owner questions when exploring a single decision space, or one question for distinct choices.
6. Do not mutate while the answer remains exploratory, partial, conditional, objecting, or ambiguous.

## Adapt opening evaluation summary

When communicating during design interviews and decision workflows, adapt opening response summaries based on turn context:

- **Breakthrough idea:** Include `[Сильное решение]` (or `[Strong Decision]`) only when the owner proposes an exceptionally strong or breakthrough architectural idea, explaining why to build upon it.
- **Architectural risk / Pushback:** Include `[Архитектурный риск / Пушбэк]` (or `[Architectural Risk / Pushback]`) whenever architectural, consistency, performance, or technical risks exist, detailing technical counter-arguments.
- **Routine turns:** On ordinary, operational, or investigatory turns without breakthroughs or critical risks, omit formal template blocks (`[Сильное решение]`, `[Нейтрально]`, `[Архитектурный риск]`) and start directly with a concise answer or summary.

## Interpret owner intent and confirmation

Classify owner responses according to explicit intent boundaries:

1. **Short explicit confirmation:** Phrases like `+`, `OK`, or `Confirmed` accept the specific active proposal. If the proposal contains an unflagged architectural risk, the agent must perform its 1-attempt pushback before final capture. Once pushback is completed or if no risk exists, `+` unambiguously confirms decision capture.
2. **Invitation to discussion:** Responses with questions, suggestions, or amendments without an explicit confirmation phrase are invitations to discussion. The agent must:
   - Thoroughly rephrase and summarize the owner's input and proposed adjustments in detail to demonstrate clear, unambiguous comprehension;
   - Evaluate the owner's feedback, refine the design proposal with reasoned arguments, and return the updated proposal to the owner for explicit confirmation.
3. **Confirmation with new topic:** An explicit confirmation phrase combined with a new question or task confirms the prior item and introduces the new item for the next turn.

Never infer confirmation from silence or forward momentum.

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

1. Update the canonical rule and required rationale using standardized MADR (Markdown Architectural Decision Record) format with YAML Frontmatter:
   ```markdown
   ---
   id: ADR-0001
   title: "Short Decision Title"
   status: "accepted" # draft | proposed | accepted | rejected | superseded
   date: YYYY-MM-DD
   deciders: ["Owner Name"]
   supersedes: "ADR-0000"
   ---
   ```
2. Update only derivatives affected by the decision.
3. Replace stale summaries instead of appending another restatement. Use neutral domain placeholders (`component-a`, `service-core`, `DomainService`) in generic core documentation. Prohibit informal placeholders (`bla-bla`) or legacy project-specific names in core artifacts.
4. Record enabled decision/worklog outcomes.
5. Select one exact next unresolved scenario from its owning roadmap or queue.
6. Synchronize phase, package lifecycle state (`SPEC_IN_PROGRESS` -> `IMPLEMENTATION_READY` -> `IN_DEVELOPMENT` -> `RELEASED` -> `DEPRECATED`), and root `AGENTS.md` Platform Status Matrix.
7. Run only eligible configured validation.
8. Inspect the complete final diff for contradictions and unintended changes.

## Maintain package lifecycle states and platform matrix

Track program and package progression across 5 explicit lifecycle states:

1. `SPEC_IN_PROGRESS`: Specification or architecture design is actively being drafted/refined.
2. `IMPLEMENTATION_READY`: Architecture and specification are approved; ready for initial coding.
3. `IN_DEVELOPMENT (vX.Y.Z-dev)`: Active code implementation or development of a new version is underway.
4. `RELEASED (vX.Y.Z)`: Code implementation is completed, tested, tagged, and published/deployed.
5. `DEPRECATED`: Program or package is superseded or retired.

When starting active development on a new version iteration for a released package (e.g. starting work on `v1.1.0`), transition the package status from `RELEASED (v1.0.0)` back to `IN_DEVELOPMENT (v1.1.0-dev)`.

In multi-program platform repositories, maintain a central `Platform Status Matrix` table in root `AGENTS.md` and synchronize package statuses atomically across local roadmaps, `README.md`, and `AGENTS.md`.

Do not copy project-specific detail into unrelated artifacts. Prefer direct references when a derivative need not restate a rule.

## Handle direct synchronization

Use direct synchronization without reconfirmation only when durable authority already marks the decision confirmed. If the claim exists only in conversation, worklog history, or an unauthoritative summary, return to owner confirmation or recovery.

## Finish the operation

If automatic commit is enabled and every commit prerequisite passes, create one focused local commit for the configured batch. Otherwise leave the eligible authorized changes uncommitted and report why; do not stage them.

Report documents changed, validation, commit status, exact next action, and whether the current session remains active. Do not ask another question unless the owner explicitly requested continuation.
