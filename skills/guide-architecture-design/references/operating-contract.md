# Operating Contract

Own input discovery, project configuration, authority mapping, and timestamp semantics. Do not redefine workflow transitions or mutation gates here.

## Required inputs

Recover or obtain before mutation:

- repository root and granted write scope;
- conversation and documentation languages;
- concern-based authority owners;
- current phase, exit criteria, last confirmed boundary, and exact next action;
- active session, block, and recovery state;
- Git branch, `HEAD`, index, worktree, and ownership of existing changes;
- whether worklog, duration tracking, decision register, and automatic commits are enabled;
- paths, schemas, commands, and commit rules for every enabled subsystem.

Reject non-Git projects without mutation. If a mutation depends on an ambiguous input or setting, ask the owner and remain non-mutating.

## Resolve authority by concern

Use the project's coherent declared model. Typical ownership is:

| Concern | Typical authority |
| --- | --- |
| Confirmed behavior and constraints | Normative specification |
| Decision rationale and supersession | Accepted ADR or decision record |
| Phase and exit state | Project roadmap |
| Workflow and recovery | Session or handoff protocol |
| Current navigation | Declared navigation owner, cross-checked with roadmap or queue |
| Time and session history | Configured worklog or time artifact |
| Change provenance | Git history |

Conversation memory is not durable authority. Resolve conflicting owners before working. When project documentation duplicates or conflicts with reusable skill behavior, present Option A (align project docs to skill) vs Option B (create feedback record for skill if project rule is superior/intentional), accompanied by an expert community practice recommendation.

## Configure optional subsystems

| Worklog | Duration tracking | Required behavior |
| --- | --- | --- |
| Off | Off | Create no session or time artifact |
| On | Off | Record sourced start/end events; do not calculate durations or pauses |
| Off | On | Use one separately configured time artifact; create no worklog |
| On | On | Follow the configured schema without duplicating event or duration records |

When a decision register is disabled, keep decision state in existing authoritative artifacts. When automatic commits are disabled, never stage or commit.

Reject enabled duration tracking when no time-capable worklog or separate time artifact is configured.

## Record truthful time evidence

Use host message metadata when available. Otherwise observe the system clock at the first tool opportunity and label the value `observed_at`, never `request_at`. Record source, timezone, and precision whenever chronology or duration depends on a timestamp. Use owner-supplied or owner-approved values for historical boundaries and record their source and precision.

After recovery, observe a distinct effective start for a newly authorized exclusive session. Do not place it before the predecessor's approved end. A resumed active session reuses its existing start and active time record.
