# Relative Paths Only Policy and Automated Validation Enforcement

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `886738f80456c21e64177c865181b539c36be8bf`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner instructed that no local absolute file paths (pointing to local computer drives or directories such as `C:\...`, `file:///C:/...`, `/Users/...`, `/home/...`) should ever be written in any repository file, audit document, or feedback record. Only relative paths and HTTP/HTTPS URLs are allowed.

## Skill instruction involved

`AGENTS.md` boundaries section, `audits/README.md` path standards, and `scripts/validate-relative-paths.ps1`.

## Observed behavior and impact

Local absolute paths leak host-specific directory structures and break portability across developer workstations and CI/CD environments.

## Session disposition

Not required. Non-blocking policy enforcement.

## Proposed improvement

1. Add explicit relative path rule in `AGENTS.md` and `audits/README.md`.
2. Create automated validation script `scripts/validate-relative-paths.ps1` to scan repository files for local absolute path violations.
3. Prohibit local absolute paths in all future authored/generated markdown, audit reports, and feedback records.

## Developer Community Best Practice Evaluation

Enforcing relative paths and vendor-neutral URLs is a core requirement for open-source software distribution and multi-platform CI/CD compatibility.

## Triage and resolution

Accepted by owner. Implemented in `AGENTS.md`, `audits/README.md`, and `scripts/validate-relative-paths.ps1`.

## Verification

Verified via `scripts/validate-relative-paths.ps1` returning zero violations (Exit Code 0).
