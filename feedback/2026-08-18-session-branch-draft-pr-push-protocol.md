# Support session-branch eager draft PR and auto-push workflow

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `<project-root>`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly directed that when working in Git-backed software architecture projects, the agent must support a real-time GitHub tracking workflow:
1. At session start (`SESSION_BINDING`), create a dedicated session branch (`agent/session-<ID>`), push an initial commit, and open an Eager Draft Pull Request on GitHub, providing the live PR URL to the owner.
2. During the session, automatically commit and push eligible updates to the session branch so the owner can track changes live on GitHub.
3. At session closing (`SESSION_CLOSING`), upon owner explicit confirmation/consent (`+` or "merge PR"), merge the Draft PR into `main` using squash merge (`gh pr merge --squash --delete-branch` or local git fallback) and delete the session branch.

## Skill instruction involved

1. `guide-architecture-design/SKILL.md` & `references/gates-recovery-and-git.md` (Git mutation rules currently restrict mutation to focused local commits and prohibit pushing without explicit per-command request).
2. `guide-architecture-design/references/workflow-modes.md` (Session binding and closure transitions).

## Observed behavior and impact

The existing strict local-only commit rule prevents real-time change tracking on GitHub during active sessions. Adding an owner-configurable `Session Branch + Draft PR + Auto Push` workflow allows real-time visibility on GitHub while protecting the primary `main` branch until final owner closure.

## Session disposition

Owner explicitly requested and approved the `Session Branch + Eager Draft PR + Live Push + Squash Merge` workflow model.

## Proposed improvement

1. Update `guide-architecture-design` rules to support `Session Branch + Eager Draft PR` mode when configured or requested by the owner:
   - Create session branch `agent/session-<ID>` and Eager Draft PR at session start.
   - Push completed in-session batches to the session branch for live GitHub tracking.
   - Execute squash merge into `main` and branch cleanup upon owner confirmation (`+` / "merge PR") during session closure.
2. Update Git safety rules to distinguish pushes to isolated session branches from direct pushes to primary production branches (`main`).

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented in `guide-architecture-design/SKILL.md`, `references/gates-recovery-and-git.md`, and `workflow-modes.md` by supporting Eager Draft PR creation at `SESSION_BINDING`, live pushes to isolated session branches during active sessions, and squash merge into `main` upon owner `+` confirmation at `SESSION_CLOSING`.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 37 (`codex-guide-session-branch-draft-pr-20260818`).
