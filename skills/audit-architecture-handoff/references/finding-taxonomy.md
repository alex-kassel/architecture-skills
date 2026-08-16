# Finding Taxonomy

Assign both a type and a priority. A large count of weak findings is not a substitute for calibration.

## Types

- **Contradiction:** two applicable assertions cannot both be true.
- **Omission:** required durable information is absent from its authoritative artifact.
- **Derived drift:** a summary, matrix, roadmap, or navigation artifact is stale relative to authority.
- **Workflow defect:** startup, recovery, decision capture, checkpoint, or closing cannot proceed safely and deterministically.
- **Readiness gap:** an unmet gate condition that prevents implementation within the declared scope. Keep it in the readiness section unless the project incorrectly claims readiness, hides the gap, or attempts to bypass its own gate.
- **Open decision:** intentionally unresolved and correctly visible; not a defect by itself.
- **Correct deferral:** detail is assigned to a later phase with sufficient impact and boundary stated.
- **Onboarding friction:** state is recoverable, but unnecessary reading, duplication, informal placeholders (`bla-bla`), or vendor/child-package entity leaks in generic core documentation increase cost or error risk (remediate using neutral placeholders such as `spider-one` or `domain-one`).
- **Idea:** optional improvement with measurable benefit but no current defect.

## Priorities

- **P0:** the project claims or attempts the audited transition, but handoff or implementation cannot proceed safely, or following the documentation is likely to cause destructive or fundamentally incorrect work.
- **P1:** a significant contradiction, missing authority, unsafe recovery ambiguity, or readiness gap can plausibly cause a wrong decision or repeated work.
- **P2:** a real but contained defect or friction has a clear downstream cost and does not block the current boundary.
- **IDEA:** useful future mechanism without evidence of a present defect.

Do not escalate priority because an artifact is absent when the project does not yet need it. Examples: an empty ADR directory, machine-readable state, Git phase tags, or a decision register may be optional. Do not mark an intentionally active session as interrupted without evidence that its owning session ended.

Do not turn an honestly reported in-progress roadmap into P0/P1 findings merely because future phases are incomplete. Return `IMPLEMENTATION NOT READY`, list unmet gates as readiness gaps or correct deferrals, and reserve prioritized findings for contradictions, hidden omissions, false readiness claims, or an attempted gate bypass.

## Finding record

Use this compact shape:

```text
[P1][Derived drift] Short title
Evidence: path — section/line; conflicting path — section/line
Observed: factual comparison
Risk: concrete failure mode
Minimal remediation: smallest sufficient change
Applies to: current project | reusable workflow | both
```

If evidence is incomplete, downgrade certainty rather than upgrading severity. Label inferences explicitly.
