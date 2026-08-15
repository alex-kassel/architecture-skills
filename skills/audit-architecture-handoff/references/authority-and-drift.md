# Authority and Drift

Resolve authority by concern. Do not invent one total document hierarchy when artifacts own different kinds of truth.

| Concern | Typical authority | Typical derived evidence |
| --- | --- | --- |
| Confirmed product and architecture behavior | Normative specification | Matrices, diagrams, entry-point summaries |
| Decision rationale and supersession | Accepted ADR or decision record | Roadmap and worklog references |
| Program phase and exit state | Project roadmap | Tactical checkpoint and entry point |
| Session workflow and recovery | Handoff or working protocol | Entry-point startup summary |
| Exact current navigation | Declared navigation owner, cross-checked with owning roadmap or queue | Latest worklog block |
| Time and collaboration history | Worklog when enabled | Git timestamps |
| Change provenance | Git history | Commit references elsewhere |

Use the project's declared authority model when it is coherent. Report an authority defect when the project gives conflicting owners for the same concern or provides no safe tiebreaker.

## Evaluate disagreements

1. Identify the concern, not only the filenames.
2. Determine which artifact claims authority for that concern.
3. Compare the canonical assertion with each required derivative.
4. Check whether a newer accepted decision supersedes the apparent canonical text.
5. Classify the result:
   - canonical contradiction: authoritative assertions conflict;
   - derived drift: canonical rule is clear but a derivative is stale;
   - navigation drift: phase or next action differs;
   - provenance gap: the current state is plausible but its decision trail is not recoverable;
   - intentional projection: a derivative correctly omits detail outside its role.

Conversation memory is never durable authority. Git proves provenance but normally does not define the current meaning of a requirement. A worklog records what happened; it must not become the sole home of confirmed architecture behavior.

## Calibrate duplication findings

Do not report duplication merely because the same subject appears in several artifacts. Report it when repeated text has diverged, obscures ownership, or creates a measurable synchronization burden. Recommend the smallest change: one canonical owner, compact derived summaries, and direct references where possible.
