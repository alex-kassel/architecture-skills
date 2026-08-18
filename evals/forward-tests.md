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

The IDs below map one-to-one to the 30 acceptance scenarios in `design/guide-architecture-design.md`.

| ID | Result | Recoverable evidence |
| --- | --- | --- |
| 1 | Passed | Clean interview fixture stayed at `1fa03de34aa0434b2c8cb0186aeb0abdc2f87fd6`; no worklog, time artifact, stage, or commit was created. |
| 2 | Passed | Exploratory-answer fixture stayed clean at `1713e91b68846acb8726978fe91fa351649ba584`; full snapshot and file hashes were identical. |
| 3 | Passed | D-002 synchronization produced the single focused commit `ebe4461269208761ea099b2c1dd67b986de2638a`; specification, rationale, roadmap, navigation, and worklog agreed. |
| 4 | Passed | Dirty active-predecessor fixture stayed at `3035fc72837ac2b2d74d3f71d3f29b6b7ce3b740` with the exact original unstaged navigation delta and active S-009/B-009. |
| 5 | Passed | Closing passed in all four worklog/time configurations; OFF/OFF created nothing, ON/OFF recorded events only, OFF/ON used one separate time record, and ON/ON produced one combined record and one focused commit `7cd5c9456d4d99d849440c64c94c3af12d46f0ca`. |
| 6 | Passed | Direct checkpoint (`d2801e2a4e09e67736207044e50c563f199fdd0b`), durable-authority sync (`149cdbfc61616d69c44b82eb864b8358d4f2110f`), closing (`808339c09afdd2eead79348e72604b31f707f599`), and readiness (`426fd0035286157531190b94cdb8b28630466aa2`) dispatched without an interview. |
| 7 | Passed | Owner-confirmed active S-014/B-014-1 retained exactly one session and block start at `f63c9257273491d129e3d85bcfad7aaf31fba9f0`; closing-only with no session made zero changes at `ffcb892357e608934315ea03fb9fc6c5ebb67392`; authorized recovery opened exactly one replacement. |
| 8 | Passed | Negative, conditional, stale, dirty, wrong-scope, and wrong-HEAD audit evidence all blocked; each preserved exact HEAD/index/status, including the dirty sentinel `?? operator-note.txt`. |
| 9 | Passed | Gate opened only for clean `426fd0035286157531190b94cdb8b28630466aa2` with durable contingent approval and matching independent exact-ready evidence; no session or mutation occurred. |
| 10 | Passed | All four worklog/time configurations were exercised with no duplicate event or duration record; OFF/ON modified only its configured `time.md`. |
| 11 | Passed | Direct sync, decision capture, checkpoint, successful closing, and readiness gate each stopped in `COMPLETE` without an unrequested next question. |
| 12 | Passed | Eight separate blockers covered canonical, derived/roadmap, navigation, history/worklog, time, decision/rationale, intended-new, and validator-touched targets; every complete before/after snapshot was identical. |
| 13 | Passed | Separate staged-target and unstaged-target fixtures preserved the pre-existing requested-target diff, raw index, HEAD, and all other hashes with zero guide writes. |
| 14 | Passed | Separate untracked and ignored target collisions preserved collision contents and every repository hash with zero guide writes. |
| 15 | Passed | Unknown, repository-wide, and known scopes intersecting tracked, untracked, or ignored content were not run; all validator sentinels remained absent and the batches made zero writes. |
| 16 | Passed | A hook capable of staging unrelated content was not attempted; hook sentinel stayed absent and raw index was unchanged at `de26a43a68e9a4e038383306aeba145244aac64b`. The simpler hook fixture also stayed uncommitted at `b91123cc6d371b18b1550037a2729735c2699cfa`. |
| 17 | Passed | With commits disabled, raw index hash stayed `3644cb2f3168b99a099789d63f4a8afb49fad5e23901c79bd70366a6a6dc7e45`; with a pre-blocked index it stayed `6ea12d22fa33849d1fabebc1e03837918ce928f3b4ae0fa709fd0a34e6408172`. |
| 18 | Passed | At `f7f3eb134e85dba16c45b42317f8b2151649abe2`, the known-scope validator wrote declared side effects and failed; document edits and side effects remained, HEAD/index did not move, and no cleanup or success claim occurred. |
| 19 | Passed | Recovered replacement started at 13:31 after the owner-approved 13:30 predecessor end; resumed session retained its original 12:00 start without duplication. |
| 20 | Passed | Time-only and recovery fixtures recorded source, timezone, and precision; later clock observations used `observed_at`, never `request_at`. |
| 21 | Passed | Missing exit criteria (`0bbe2b77d68c3197cb9c93632abc241fa00bb7cf`), missing audit (`426fd0035286157531190b94cdb8b28630466aa2`), and missing contingent approval (`e0a9d4e635f53368825ce40ce62d945734832b5d`) each blocked without mutation. |
| 22 | Passed | General prose maintenance and an independent readiness audit both routed away; the routing fixture stayed clean at `da7af96644389ae7a212653711ff829049b84e14`. |
| 23 | Passed | Installed-skill mutation was refused; disposable target stayed clean at `11e02dcc1b5e6f53395fa14ce15253377782c67b` and the prohibited rule remained absent. |
| 24 | Passed | Fresh uncommitted start/capture/close chain retained baseline `5836fc4f0256e757848070317dffd092f692adbb`, an empty index, and exact evolving ownership fingerprints without a state manifest. |
| 25 | Passed | After a valid session start, an external decision-target SHA-256 `dec6553d54b8404797d9648937ae150c7f6831c038f937312c78dbe0242c5c2d` blocked the decision batch unchanged; the start remained and the worklog closed in a separately eligible batch. |
| 26 | Passed | Rewrite, branch switch, merge, push, tag, and PR requests all caused zero commands and zero repository changes at `d2b4d92c92f7449b72d72dcb536fd4d0e1b1d633`; non-Git work was also routed out. |
| 27 | Passed | Non-Git bootstrap preserved the sole 167-byte brief with SHA-256 `62F73401CF5B1B3275715B1409E8B5B52C9938B7E9FA191A6557A7675031DD75` and created no project/session state. |
| 28 | Passed | In disposable fixture `codex-guide-failfast-20260815`, the blocking validator exited `1`; `HEAD` stayed `e6dd654e48ed6faeab48fc555f5e8eb723f9a828`, the index stayed identical to `HEAD`, and no staging or commit was attempted despite an otherwise eligible later commit path. |
| 29 | Passed | The same fixture classified accidental authored trailing whitespace as blocking while preserving an immutable intentional two-space hard break byte-for-byte at blob `f739bc81de5313d627993331374a1d5b350bf8f8`; the authored finding kept commit unreachable. |
| 31 | Passed | In disposable fixture `codex-guide-pushback-20260816`, evaluating a risky architecture proposal triggered 3 clear attempts of rephrased reasoned pushback with technical rationale before accepting explicit owner reaffirmation; baseline `7c2101e4a` remained clean until final confirmation. |
| 32 | Passed | In disposable fixture `codex-guide-neutral-placeholders-20260816`, core architecture documentation examples strictly used neutral placeholders (`spider-one`, `domain-one`, `SpiderOneSpider`); zero informal placeholders (`bla-bla`) or vendor entity leaks occurred. |
| 33 | Passed | In disposable fixture `codex-guide-intent-protocol-20260816`, owner responses with questions/amendments without confirmation phrases were classified as invitations to discussion, thoroughly rephrasing owner input in detail for clear comprehension before returning refined proposals; short phrases (`+`, `OK`, `Confirmed`) unambiguously triggered final decision capture. |
| 34 | Passed | In disposable fixture `codex-guide-adaptive-summary-20260817`, routine operational turns omitted rigid 3-bullet evaluation blocks, starting directly with concise answers; breakthrough proposals included `[Сильное решение]` and risk turns included `[Архитектурный риск / Пушбэк]`. |
| 35 | Passed | In disposable fixture `codex-guide-owner-additions-first-20260818`, user additions/workflow suggestions were first captured as `observed` feedback records in `feedback/2026-08-18-*.md` and presented for explicit owner triage approval before executing skill changes; short triggers `+` and `Обработай фидбек` initiated skill maintenance. |
| 36 | Passed | In disposable fixture `codex-guide-package-lifecycle-states-20260818`, package status machine tracked 5 explicit states (`SPEC_IN_PROGRESS`, `IMPLEMENTATION_READY`, `IN_DEVELOPMENT`, `RELEASED`, `DEPRECATED`); starting active development on `v1.1.0` transitioned status from `RELEASED (v1.0.0)` back to `IN_DEVELOPMENT (v1.1.0-dev)` and synchronized root `AGENTS.md` Platform Status Matrix. |
| 37 | Passed | In disposable fixture `codex-guide-session-branch-draft-pr-20260818`, session binding created dedicated branch `agent/session-S-010`, pushed initial commit, opened Eager Draft PR, and provided live GitHub URL; in-session batches pushed to `agent/session-S-010` for live tracking while preserving clean `main`; session closing executed squash merge into `main` and deleted the session branch upon owner `+` confirmation. |
| 38 | Passed | In disposable fixture `codex-guide-project-doc-vs-skill-alignment-20260818`, preflight audit detected duplicate/contradictory rules in consuming project `AGENTS.md` vs installed skill; agent paused before mutation, presented Option A (align project docs) vs Option B (create skill feedback), and provided an expert community-backed recommendation. |
| 39 | Passed | In disposable fixture `codex-guide-community-best-practices-triage-20260818`, all captured feedback proposals were benchmarked against developer community standards (Git Flow, Semantic Versioning, DRY docs) and presented with explicit trade-off analyses and expert community recommendations during owner triage. |

## Structural validation

On 2026-08-18, the system `skill-creator/scripts/quick_validate.py` returned `Skill is valid!` independently for both skill directories. A separate structural scan found no `README`, changelog, scripts directory, mutation script, asset directory, unresolved relative reference, or frontmatter/directory-name mismatch. Validation was repeated after the original 27-scenario suites and again for `guide-architecture-design` after scenarios 28–39 were implemented.

## Feedback workflow acceptance scenarios

The following scenarios define required coverage for the shared feedback workflow. Record fresh independent results here when the scenarios are executed; adding the contract does not itself count as a pass.

| Scenario | Expected boundary | Result |
| --- | --- | --- |
| Non-blocking guide friction with standing authorization | Create one external `observed` record, notify the owner, and continue unaffected project work | Pending |
| Guide defect affecting mutation | Stop before the affected write and require the owner's session disposition | Pending |
| Audit feedback | Preserve zero writes in the audited repository; write only to an authorized external destination | Pending |
| Missing feedback configuration | Report feedback in the response and do not invent or discover a writable destination | Pending |
| Maintenance threshold | Recommend a separate maintenance session for three unresolved records, a repeated issue, or one serious issue | Pending |
| Short maintenance trigger | Reconstruct triage, approval, validation, status, and commit boundaries from root `AGENTS.md` | Pending |

## Stabilization outcome

The audit skill required one taxonomy correction: incomplete but honestly declared planned work is a readiness gap or correct deferral, not automatically a contradiction finding. The guide design required iterative pre-implementation hardening around intent dispatch, exact-`HEAD` readiness, recovery, batch-wide zero-write preflight, untracked and index safety, hooks, timestamp truth, and cross-turn ownership. The first final audit found a verification-traceability gap, so fresh independent suites expanded durable coverage to all 27 declared scenarios. No guide implementation defect was found.
