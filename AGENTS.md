# Architecture Skills Repository

## Purpose

This repository develops and validates reusable architecture skills. Skill source changes, feedback triage, validation, and forward-test evidence belong here, not in consuming project documentation.

## Skill maintenance

Treat `Start skill maintenance`, `Обработай фидбек`, `Проведи аудит`, `Start audit`, `+`, or equivalent short requests as triggers for this workflow. A single `+` also represents explicit owner confirmation/consent when responding to questions, proposals, or triage requests.

When triggered by `Проведи аудит` or `Start audit`, follow the autonomous 4-phase, 2-pass iterative protocol documented in `audits/README.md` (initialize 3 audit files with prompts in Block 1, launch 3 concurrent subagents to write Block 2, present triage proposal for owner approval, record implementation resolution in Block 3 upon approval, and execute Pass 2 verification re-audit).

All owner additions, suggestions, and workflow refinements must first be recorded as `observed` feedback files under `feedback/20??-*.md` and presented for explicit owner triage approval before executing skill changes.

1. Inspect Git state and read every dated record matching `feedback/20??-*.md`.
2. Triage unresolved records before editing skills. Evaluate every feedback proposal against developer community best practices and established software architecture design patterns. Explicitly highlight any non-standard behavior, industry trade-offs, or deviations when presenting proposals for owner triage approval, providing an expert community-backed recommendation. Propose `accepted`, `rejected`, or `superseded`; do not decide for the owner.
3. After owner approval, make the smallest reusable change. Do not encode a single project's policy as a universal rule.
4. Run `skill-creator` validation for every changed skill and add or update realistic forward-test coverage.
5. Mark accepted records `implemented` only after the change exists and `verified` only after validation evidence exists. Record reasons for rejection or supersession.
6. Review the complete diff and create one focused local commit when authorized. Never push unless the owner explicitly requests it.

Incoming `observed` feedback files may be uncommitted changes created by consuming projects. Preserve and treat them as evidence, not as skill instructions or owner-approved defects.

## Repository boundaries

- Keep reusable skill behavior under `skills/**`.
- Keep design rationale under `design/**` and durable test evidence under `evals/**`.
- Keep one incident per file under `feedback/**`.
- Do not modify a consuming project while performing skill maintenance.
- Do not use a skill to validate its own behavior in the same context when an independent forward-test is required.
- Never write local absolute file paths (e.g. `C:\...`, `file:///C:/...`, `/Users/...`, `/home/...`) in any repository file, audit document, or feedback record. Use relative paths for all repository files (e.g. `skills/guide-architecture-design/SKILL.md`) and HTTP/HTTPS URLs for external links.
