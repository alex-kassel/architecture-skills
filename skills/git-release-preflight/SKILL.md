---
name: git-release-preflight
description: Perform pre-push readiness evaluations, guardrail verification, risk assessment, pushback presentation, and clean git release/push execution across software and documentation repositories. Trigger this skill whenever the user mentions pushing code, running pre-push checks, syncing releases, evaluating git push readiness, verifying repository guardrails, or executing git push or release sync operations safely. Trigger on explicit trigger phrases such as 'push', 'git push', 'Sync skills', 'run release checks', or 'prepare release'.
---

# Git Release Preflight & Push Execution

Evaluate repository readiness before executing `git push` or syncing releases. Ensure zero unverified feedback items, clean worktrees, passing automated guardrails, and explicit risk presentation prior to pushing code or documentation.

## Operating Mode: Pre-Push Gate

When triggered by `push`, `git push`, `Sync skills`, or explicit release commands, operate as a safety gate. Never execute a `git push` blindly without evaluating repository readiness first.

## Pre-Push Evaluation Protocol

1. **Worktree & Index Status**:
   - Run `git --no-optional-locks status --short --branch`.
   - Verify if there are uncommitted changes, untracked files outside scope, or unmerged conflicts.

2. **Feedback & Task Completion Verification**:
   - Check configured feedback directories (e.g. `feedback/`).
   - Ensure all `observed` items created during the session are marked `implemented` and `verified` or explicitly deferred by the owner.

3. **Deterministic Guardrails Check**:
   - Run available repository validators (e.g. `python scripts/validate_relative_paths.py`, `python scripts/validate_english_only.py`, test runners).
   - Verify zero local absolute paths (`C:\...`, `file:///C:/...`) and language standard compliance.

4. **Risk Evaluation & Pushback**:
   - If any counter-arguments or readiness risks are found (failing tests, unverified items, dirty worktree outside scoping):
     - Present a concise, evidence-backed list of concerns to the owner.
     - Pause execution and await owner resolution or explicit override confirmation.

5. **Clean Execution**:
   - If zero counter-arguments or readiness risks exist:
     - Execute `git push` (or repository release sync).
     - Report the exact completion status, target branch, and commit hash to the owner.

## Pre-Push Evaluation Output Template & Example

### Pre-Push Readiness Report Template
```markdown
# Git Release Preflight Readiness Report

## Check Results
- **Git Worktree Status**: [Clean / Dirty (List uncommitted paths)]
- **Feedback Backlog**: [0 Unverified Items / X Pending Items]
- **Relative Path Guardrail**: [PASS / FAIL]
- **Language Compliance**: [PASS / FAIL]
- **Automated Test Suite**: [PASS / FAIL]

## Risk & Counter-Argument Summary
- [None identified / Risk description and evidence]

## Preflight Verdict & Action
- **Verdict**: [CLEAN_TO_PUSH / PUSH_BLOCKED]
- **Execution Output**: [Git push summary with branch and commit SHA, or pause report]
```

### Usage Example
```markdown
**Input:** `git push`
**Action:** Executes preflight evaluation checks.
**Output:**
- Worktree: Clean (`main` up to date)
- Feedback: All items verified
- Validators: Relative paths (PASS), English-only (PASS)
- Action: Executing `git push origin main` -> Pushed commit `a1b2c3d` successfully.
```
