---
name: maintain-architecture-skills
description: Execute the 6-step skill maintenance protocol for capturing feedback evidence, conducting community triage, executing zero-write preflights, running validation self-healing loops, and updating skill definitions. Make sure to trigger this skill whenever the user asks to start skill maintenance, process feedback, capture evidence, conduct skill triage, run skill validation loops, or whenever any request or proposal is made to add, edit, modify, refactor, rename, move, or delete any skill or SKILL.md file in the repository, regardless of phrasing or language.
---

# Maintain Architecture Skills

Execute structured, evidence-backed skill maintenance across architecture skill repositories without introducing regressions or unapproved mutations.

## Skill Maintenance Protocol

When triggered by `Start skill maintenance`, `Process feedback`, or any user proposal to add, edit, move, or delete skills (regardless of phrasing or language), follow the 6-step protocol:

1. **Evidence Capture**:
   - Record all incoming feedback, user proposals, or modification requests in an `observed` feedback record (`feedback/20??-*.md`) before editing any file under `rules/**`, `skills/**`, or `plugins/**`.
   - Never edit files under `rules/**`, `skills/**`, or `plugins/**` prior to evidence capture and triage approval.

2. **Community Triage**:
   - Evaluate proposals against software architecture patterns and community best practices.
   - Formulate a triage proposal with status (`accepted`, `rejected`, or `superseded`), technical rationale, and trade-off analysis.
   - Present the triage proposal and wait for explicit owner approval (`+`).

3. **Zero-Write Preflight & Smallest Change**:
   - Apply the smallest reusable change under `rules/**`, `skills/**`, or `plugins/**` only after receiving explicit owner approval.
   - Maintain strict boundary isolation; do not modify consuming projects while maintaining skills.

4. **Validation, Mandatory Autonomous Audit & Self-Healing Loop**:
   - Run skill validation checks and verify forward-test coverage (`evals/forward-tests.md`).
   - **Mandatory Autonomous Audit Gate**: Whenever a new skill is created or substantially modified, execute a full 4-phase, 2-pass autonomous audit per [`execute-autonomous-audit`](../execute-autonomous-audit/SKILL.md) and record durable audit logs under `audits/`.
   - If validation fails, perform up to 3 bounded self-repair attempts targeting strictly the explicit error without introducing secondary structural edits. If repair fails after 3 attempts, run `git checkout -- skills/` and `git clean -fd skills/` to revert all changes and escalate.

5. **Deterministic Guardrails & Adapter Sync Verification**:
   - Execute path validator (`python scripts/validate_relative_paths.py`) and language validator (`python scripts/validate_english_only.py`) prior to commit.
   - Verify and update client adapters (`python scripts/adapters/sync_all.py` or `python scripts/adapters/<target>.py`) whenever rules or skills are created, modified, or deleted.

6. **Resolution & Pre-Push Evaluation**:
   - Update accepted feedback records to `implemented` and `verified`.
   - Create one focused local commit when authorized.
   - Run pre-push evaluation per `skills/git-release-preflight/SKILL.md` prior to executing `git push`.

---

## Output Templates

### Triage Proposal Template
ALWAYS use this structure when presenting triage proposals:

```markdown
### Skill Triage Proposal: [Proposal Title]
- **Target Skill**: `skills/[skill-name]/SKILL.md`
- **Feedback Evidence**: `feedback/20??-[name].md`
- **Proposed Status**: `accepted` | `rejected` | `superseded`
- **Rationale & Architectural Trade-offs**: [Explanation]
- **Proposed Changes**: [Summary of edits]
- **Awaiting Approval**: Reply with `+` to approve execution.
```
