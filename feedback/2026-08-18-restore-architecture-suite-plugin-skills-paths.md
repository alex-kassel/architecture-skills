# Restore skills array in architecture-suite plugin manifest with relative paths

- Status: verified
- Skill: maintain-architecture-skills
- Skill commit: `b80c13757b453586aee75f9109d2f98d570ee00a`
- Source repository: `codex-architecture-skills`
- Source program: `plugins/architecture-suite/plugin.json`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested restoring the `skills` array in `plugins/architecture-suite/plugin.json` with correct relative path references pointing from the plugin directory to the top-level `skills/` directory.

## Skill instruction involved

`plugins/architecture-suite/plugin.json` and `skills/maintain-architecture-skills/SKILL.md`.

## Observed behavior and impact

The `skills` array was previously removed from `plugins/architecture-suite/plugin.json` during reorganization. Restoring relative path references (`../../skills/<skill-name>`) enables agents and plugin loaders to locate skills bundled in the top-level `skills/` directory.

## Session disposition

Owner requested restoring the `skills` array using relative paths pointing to the top-level `skills/` directory and presenting the proposed JSON for approval before writing.

## Proposed improvement

Add the `skills` array back to `plugins/architecture-suite/plugin.json` using relative paths:
- `../../skills/session-lifecycle`
- `../../skills/scaffold-subproject-docs`
- `../../skills/guide-architecture-design`

## Developer Community Best Practice Evaluation

Using explicit relative paths (`../../skills/<skill-name>`) from plugin manifests to shared skills directories follows standard package/plugin dependency specification practices, ensuring resolution consistency across operating systems.

## Triage and resolution

Accepted and approved by project owner on 2026-08-18. Implemented by adding relative path skill references to `plugins/architecture-suite/plugin.json`.

## Verification

Verified on 2026-08-18 via `python scripts/validate_relative_paths.py`, `python scripts/validate_english_only.py`, and `python scripts/adapters/sync_all.py`, returning exit code 0.
