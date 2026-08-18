# Public README for skills distribution repository

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `<repo-root>`
- Source program: `AGENTS.md` & `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner noted that the exported public skills distribution repository (`alex-kassel/skills`) lacks a root `README.md` explaining available skills and installation procedures for end-user developers.

## Skill instruction involved

1. `AGENTS.md` skill release guidelines and distribution protocols.
2. Root `skills/` directory structure and public documentation.

## Observed behavior and impact

A distribution repository without a root `README.md` forces users and AI agents to manually inspect subdirectories to discover available skills, reducing onboarding clarity and professional presentation.

## Session disposition

Owner requested adding a clean, user-focused English `README.md` for the `skills` distribution repository.

## Proposed improvement

Create `skills/README.md` in the source monorepo so that upon `git subtree push --prefix skills`, it automatically serves as the primary root `README.md` of the public `alex-kassel/skills` distribution repository.

## Developer Community Best Practice Evaluation

In open-source AI skill registries and prompt marketplaces (e.g. Cursor Rules, Antigravity Marketplace, Claude Tools):
- Providing a dedicated root `README.md` with a skill catalog, description table, and installation commands is the standard pattern for open-source registries.
- Placing `skills/README.md` in the source monorepo allows `git subtree push` to transform it seamlessly into the root `README.md` of the distribution repo without extra automation scripts or duplication.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented by creating `skills/README.md` containing a clean English skill catalog, quickstart installation guide, and maintainer repository links.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 42 (`codex-guide-distribution-repo-readme-20260818`).
