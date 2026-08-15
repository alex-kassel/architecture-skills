# Deferred Capability Splits

## `prepare-implementation-handoff`

Status: likely future extraction; not part of V1.

Create this skill only when repeated usage shows a cohesive trigger for producing an implementation-consumption bundle after architecture readiness. It must remain separate from independent audit and owner-led design mutation so that preparing a handoff cannot silently weaken either gate.

Evidence required before extraction:

- at least three concrete post-readiness handoff scenarios;
- a stable input/output contract distinct from the final readiness gate;
- explicit authority for generated implementation artifacts;
- independent safety tests showing no architecture decision is invented or reopened.

## Machine-readable state manifest

Status: deferred to a later iteration.

V1 keeps cross-turn ownership in conversation-scoped fingerprints. Reconsider a persisted manifest only after stable workflows demonstrate which state is both necessary and safe to make authoritative.

## New-project bootstrap

Status: deferred until the existing-project workflow is stable in real use.

Bootstrap needs its own authority defaults, repository initialization rules, and templates. V1 therefore rejects non-Git or unconfigured project creation without mutation.
