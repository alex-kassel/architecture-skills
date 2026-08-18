---
name: maintain-architecture-skills
description: Execute the 6-step skill maintenance protocol for capturing feedback evidence, conducting community triage, executing zero-write preflights, running validation self-healing loops, and updating skill definitions. Use when asked to start skill maintenance, process feedback, or update repository skills.
---

# Maintain Architecture Skills

Execute structured, evidence-backed skill maintenance across architecture skill repositories without introducing regressions or unapproved mutations.

## Skill Maintenance Protocol

When triggered by `Start skill maintenance`, `Process feedback`, or explicit skill maintenance requests, follow the 6-step protocol:

1. **Evidence Capture**:
   - Preserve incoming `observed` feedback records (`feedback/20??-*.md`) as evidence.
   - All owner additions, suggestions, and workflow refinements must first be recorded as `observed` feedback files before editing skill files under `skills/**`.

2. **Community Triage**:
   - Evaluate proposals against software architecture patterns and community best practices.
   - Propose `accepted`, `rejected`, or `superseded` with trade-off analysis.
   - Wait for explicit owner approval (`+`).

3. **Zero-Write Preflight & Smallest Change**:
   - Make the smallest reusable skill change under `skills/**` only after explicit owner approval.
   - Never edit `skills/**` prior to triage approval.

4. **Validation & Self-Healing Loop**:
   - Run skill validation (`skill-creator` validation / test scripts) and verify forward-test coverage (`evals/forward-tests.md`).
   - If validation fails, perform up to 3 bounded self-repair attempts before reverting diff and escalating.

5. **Deterministic Guardrails**:
   - Execute path validator (`python scripts/validate_relative_paths.py`) and language validator (`python scripts/validate_english_only.py`) prior to commit.

6. **Resolution & Pre-Push Evaluation**:
   - Mark accepted feedback records `implemented` and `verified`.
   - Create one focused local commit when authorized.
   - Run pre-push evaluation prior to executing `git push`.
