# Proportional recovery for deterministic in-scope failures

- Status: verified
- Skill: guide-architecture-design
- Skill commit: `411c567`
- Source repository: `C:\Users\Alex\Herd\packages.dev2`
- Source program: `normalization-core`
- Project session: `unknown`
- Observed at: `2026-08-15`

## Situation

The owner had already authorized a fixed coordination-room structure, two exact file copies, local Git initialization, and a local commit without push. One copy failed only because an expected destination directory did not yet exist. In a second trace, an exact staging or commit operation failed before changing the index because the sandbox denied creation of `.git/index.lock`.

The original report was supplied in `C:\Users\Alex\.codex\attachments\9e0e688d-2cae-4a2c-a9d8-3bca39e0a35e\pasted-text.txt`.

## Skill instruction involved

The reported `Contain failure` recovery rule in the guide workflow required a full stop and renewed owner confirmation after a failed mutating step.

## Observed behavior and impact

The rule did not distinguish a deterministic, non-destructive correction already covered by unambiguous owner authorization from an uncertain or scope-expanding recovery. It therefore added a redundant approval boundary for creating the already approved directory and repeating the exact copy. It could likewise turn a standard sandbox escalation for the same unchanged Git command into an architecture-recovery question even when the index, lock, scope, and target were unchanged.

This protects against ambiguous recovery but makes safe mechanical work unnecessarily bureaucratic.

## Session disposition

The owner classified the repeated confirmation as undesirable and asked that the observation be preserved for later skill maintenance. No skill exception or skill change is being applied in this capture session.

## Proposed improvement

Introduce a proportional recovery classification in the appropriate reference:

- Permit a deterministic in-scope mechanical retry without renewed owner confirmation only when the original authorization, scope, target, intended result, known cause, attribution, baseline, and external state remain provably unchanged; the correction is non-destructive and makes no product or architecture decision; and relevant preflight and validation are repeated afterward.
- Require a short commentary update for that retry.
- Preserve the mandatory stop for unknown causes, scope expansion, foreign or unattributed changes, uncertain partial writes, index mismatch, destructive cleanup, substantive validation failures, architectural choices, or any recovery not demonstrably covered by the original authorization.

Candidate examples are creating an already approved missing destination directory, repeating the exact copy, retrying the same Git operation through the standard sandbox escalation path after a pre-index permission denial, and correcting an unambiguous command or quoting error without changing intent.

## Triage and resolution

Accepted by the owner on 2026-08-15. Implemented in the guide's failure-containment rules with a narrow deterministic mechanical-retry exception and explicit stop conditions for ambiguous, destructive, scope-expanding, or substantive recovery.

## Verification

Verified on 2026-08-15 by fresh independent disposable-fixture scenarios. An approved missing-directory copy retried without renewed confirmation and produced matching source/destination SHA-256 `481B9F1B69E1E986BC62FE8B22A8B3F3B372D2AFE71A2B7D952F307FF835815A`; an identical Git operation retried after a proved pre-index permission denial and staged only the intended diff; an uncertain truncated partial write remained unstaged and required owner direction. `skill-creator/scripts/quick_validate.py` also returned `Skill is valid!` for the changed skill.
