# Extraction and Modularization of AGENTS.md Instructions into Standalone and Existing Skills

- Status: verified
- Skill: guide-architecture-design | audit-architecture-handoff
- Skill commit: `d66c19b`
- Source repository: `shared`
- Source program: `shared`
- Project session: `none`
- Observed at: `2026-08-18`

## Situation

The project owner requested a thorough revision of `AGENTS.md` and repository instructions to identify instructions that should be modularized and extracted into standalone skills reusable across all projects (specifically audit execution, git push/release protocols, and deterministic repository guardrails), or absorbed into existing skills (`audit-architecture-handoff` and `guide-architecture-design`).

## Skill instruction involved

`AGENTS.md` (Intent & Workflow Routing, Skill Maintenance Protocol, Mandatory Audit Standard, Repository Boundaries).

## Observed behavior and impact

Currently, `AGENTS.md` contains high-level operational workflows (such as multi-agent autonomous audit execution, pre-push readiness evaluation, deterministic guardrail validation, and feedback triage) embedded directly in the root repository instructions. While these instructions govern this repository, many of them represent general software architecture and development best practices that are reusable across any codebase or documentation project. Keeping them hardcoded in `AGENTS.md` limits their reusability by autonomous code and documentation agents operating in other repositories.

## Session disposition

Accepted and confirmed by owner (`+`).

## Proposed improvement

1. **Extract Standalone Reusable Skills (Applicable Across All Projects)**:
   - **`git-release-preflight`**: Extract the pre-push readiness evaluation protocol (`push`, `git push`, `Sync skills`), including uncommitted changes check, unverified items check, pre-push risk evaluation/pushback, and clean push execution. Reusable by any code or documentation agent before pushing code.
   - **`execute-autonomous-audit`**: Extract the 4-phase, 2-pass iterative 3-perspective audit protocol (Formal Logic, DX, Chaos), including 3-subagent execution (`invoke_subagent`), Block 1/2/3 document structure, mandatory 3 innovative ideas prompt requirement, and pass-2 verification. Reusable for auditing any codebase or documentation set.
   - **`validate-repository-guardrails`**: Extract deterministic guardrail validation rules (relative paths enforcement, English-only content validation, absolute path stripping). Reusable as a pre-commit or CI preflight check in all projects.

2. **Absorb Specific Instructions into Existing Skills**:
   - **`audit-architecture-handoff`**: Absorb specific read-only audit lenses, single-artifact authority vs drift resolution rules, and fresh-session handoff verification.
   - **`guide-architecture-design`**: Absorb session decision confirmation (`+`), zero-write preflight checks before mutation, and session branch/Draft PR commit workflows.

3. **Skill Development Meta-Skill**:
   - **`maintain-architecture-skills`**: Extract the 6-step Skill Maintenance Protocol (Evidence capture, Community triage, Zero-write preflight, Validation self-healing loop, Resolution) into a dedicated skill for skill development repositories.

## Developer Community Best Practice Evaluation

Modularizing repository instructions into single-responsibility, highly reusable skill packages aligns with modern software engineering principles (Single Responsibility Principle, Component-Based Architecture, Agentic Skill Interoperability). It enables documentation and coding agents across different projects to inherit standardized audit, git, and validation capabilities without duplicating prompt logic.

## Triage and resolution

- Status: `implemented` & `verified`
- Resolution: Accepted by owner (`+`) and extracted into standalone skill definitions (`git-release-preflight`, `execute-autonomous-audit`, `validate-repository-guardrails`, `maintain-architecture-skills`).

## Verification

Verified via path validator (`scripts/validate_relative_paths.py`) and English-only validator (`scripts/validate_english_only.py`).
