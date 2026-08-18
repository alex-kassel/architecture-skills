# Synchronize plugins/README.md code block with relative skills paths in architecture-suite manifest

- Status: verified
- Skill: maintain-architecture-skills
- Skill commit: `08ba0b5550a25fa7bf1eec4f995cfbfdbd40aa96`
- Source repository: `codex-architecture-skills`
- Source program: `plugins/README.md`, `plugins/architecture-suite/plugin.json`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner noticed that the JSON code block example in `plugins/README.md` was not updated to reflect the relative skill paths (`../../skills/...`) introduced in `plugins/architecture-suite/plugin.json`.

## Skill instruction involved

`plugins/README.md` and `plugins/architecture-suite/plugin.json`.

## Observed behavior and impact

Documentation drift occurred between the actual `plugin.json` manifest structure and its code snippet in `plugins/README.md`. Updating the documentation snippet restores 100% alignment across repository documentation.

## Session disposition

Owner requested updating `plugins/README.md` to match `plugins/architecture-suite/plugin.json`.

## Proposed improvement

Update the JSON code block in `plugins/README.md` to use relative paths:
- `../../skills/session-lifecycle`
- `../../skills/scaffold-subproject-docs`
- `../../skills/guide-architecture-design`

## Developer Community Best Practice Evaluation

Keeping code examples in documentation perfectly synchronized with real manifest files prevents developer confusion and ensures documentation accuracy.

## Triage and resolution

Accepted and approved by owner on 2026-08-18. Implemented by updating the JSON code snippet in `plugins/README.md`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`, returning exit code 0.
