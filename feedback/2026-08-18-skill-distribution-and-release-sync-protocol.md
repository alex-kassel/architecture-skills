# Support automated skill release export and multi-repository distribution

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `<repo-root>`
- Source program: `AGENTS.md` & `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner highlighted a distribution requirement for AI skills:
1. Maintainers require the source monorepo (`architecture-skills`) containing `skills/`, `design/`, `evals/`, and `feedback/` for continuous skill maintenance.
2. End-user developers expect a minimal, dedicated `skills` repository containing only the clean `skills/` directory without maintainer feedback or test ledgers.
3. Manual maintenance of two separate repositories would introduce duplication and instruction drift.

## Skill instruction involved

1. `AGENTS.md` repository boundaries, skill release guidelines, and maintenance protocols.
2. Root repository deployment and distribution automation.

## Observed behavior and impact

Manually maintaining duplicate copies of skills in separate repositories causes derived drift and violates the Single Source of Truth (SSOT) principle. Automating the sync via Git subtree or GitHub Actions ensures a single maintainer source of truth while delivering a clean user-facing skills distribution repo.

## Session disposition

Owner requested a zero-duplication distribution pattern to support both maintainer source monorepo (`architecture-skills`) and end-user distribution repo (`skills`).

## Proposed improvement

1. Document the dual-repository distribution pattern in `AGENTS.md` and `README.md`.
2. Configure automated release synchronization using GitHub Actions (`.github/workflows/sync-skills.yml`) or Git subtree (`git subtree push --prefix skills`) to automatically export the `skills/` directory from `architecture-skills` to a clean `skills` distribution repository upon release.

## Developer Community Best Practice Evaluation

In open-source software and AI skill ecosystems (e.g. Cursor Rules, Antigravity Marketplace, Claude Tools):
- Maintaining a single source monorepo (`architecture-skills`) with automated downstream sync to a clean distribution repo (`skills`) is the industry-standard pattern for preventing instruction drift.
- Using GitHub Actions for automated downstream mirroring ensures 0 manual maintenance overhead for maintainers while providing a minimalist experience for end users.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented by creating public distribution repository `alex-kassel/skills`, running initial `git subtree push`, and configuring GitHub Action `.github/workflows/sync-skills.yml` and local helper script `scripts/sync-skills.ps1`.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 41 (`codex-guide-skill-distribution-sync-20260818`).
