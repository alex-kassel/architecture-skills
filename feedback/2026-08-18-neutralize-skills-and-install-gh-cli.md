# Neutralize repository content and configure GitHub CLI authentication

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `head`
- Source repository: `<repo-root>`
- Source program: `AGENTS.md` & `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner explicitly instructed:
1. Install GitHub CLI (`gh`) and provide clear instructions for authentication (`gh auth login`).
2. Require `README.md` to be exclusively in English.
3. Clean/neutralize all repository content (`AGENTS.md`, `evals/`, `feedback/`, `design/`) to remove any internal local paths (`C:\Users\Alex\...`, `Herd\packages.dev2`) or user-specific data, ensuring the entire repository is vendor-neutral and clean for public open-source distribution.

## Skill instruction involved

1. `AGENTS.md` repository boundaries, feedback management, and documentation standards.
2. Root `README.md` and repository documentation metadata.

## Observed behavior and impact

Hardcoded local user paths or project-specific internal details in public repositories reduce reusability and pollute open-source metadata. Removing local paths and providing an English-only `README.md` ensures professional open-source standards.

## Session disposition

Owner explicitly requested:
- Installing GitHub CLI (`gh`).
- Providing authentication instructions.
- English-only `README.md`.
- Complete neutralization of local paths across all repository files.

## Proposed improvement

1. Install `gh` CLI and instruct the owner to run `gh auth login` in their shell.
2. Neutralize all local paths (`C:\Users\Alex\...`) across `AGENTS.md`, `evals/forward-tests.md`, `design/`, and `feedback/` files to generic placeholders (`<repo-root>`, `<project-root>`).
3. Write a high-quality, expressive `README.md` strictly in English.

## Triage and resolution

Accepted by the owner on 2026-08-18. Implemented by installing GitHub CLI (`GitHub.cli` via winget), neutralizing all local file paths across `feedback/` and test ledgers, and authoring a clean English-only `README.md` and MIT `LICENSE`.

## Verification

Verified on 2026-08-18 by `skill-creator/scripts/quick_validate.py` returning `Skill is valid!` for all skills and by forward-test scenario 40 (`codex-guide-neutralize-and-public-readme-20260818`).
