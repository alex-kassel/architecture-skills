---
name: execute-autonomous-audit
description: Execute autonomous 4-phase, 2-pass iterative multi-perspective audits of codebases, software architecture, or documentation sets using concurrent subagents and structured audit logs. Trigger this skill whenever the user asks to run an autonomous audit, start a multi-agent or multi-perspective audit, conduct a 2-pass iterative audit cycle, audit codebase quality using concurrent auditors, or generate structured audit reports with mandatory innovation proposals. Trigger on phrases like 'Run audit', 'Start audit', 'autonomous audit', 'multi-perspective audit', '2-pass audit', or 'run subagent audit'.
---

# Autonomous Multi-Agent Audit Runner

Orchestrate autonomous, 4-phase, 2-pass iterative audits of codebases, software architecture specifications, or repository documentation using concurrent subagents across distinct perspectives.

## Audit Workflow Protocol

When triggered by `Run audit`, `Start audit`, or explicit audit commands, execute the autonomous 4-phase, 2-pass protocol.

### 🔁 Mandatory 2-Pass Iteration Policy

1. **Pass 1 (Initial Audit & Fixes)**: Launch 3 concurrent subagent auditors, present triage, apply approved fixes, and validate.
2. **Pass 2 (Verification Re-Audit)**: Launch 3 subagents to re-audit updated files, verifying complete remediation and zero introduced regressions.
3. **Residual Deferral Gate**: Document minor non-blocking Pass 2 observations for future cycles without blocking present delivery.

---

### 🛑 Audit Trigger & Granularity Rules

- **Exclusive Owner Trigger**: Full repository autonomous audits execute ONLY upon direct, explicit owner commands (`Run audit`, `Start audit`). No implicit, automated, or background triggers may launch a full repository audit.
- **Per-Skill Audit File Granularity (1:3 Rule)**: Aggregating multiple skills into shared perspective audit files is strictly prohibited. Every target skill audited MUST have 3 dedicated audit log files created under `audits/` (one file per perspective). For N target skills, a full audit MUST generate exactly N × 3 audit files (e.g. 10 skills = 30 audit log files named `audits/YYYY-MM-DD-HHMM-<skill-name>-<perspective>.md`).

---

### Protocol Execution Phases

1. **Phase 1: Audit Document Initialization**
   - For each target skill, initialize 3 dedicated audit files in the project's audit registry (e.g. `audits/YYYY-MM-DD-HHMM-<skill-name>-<perspective>.md`).
   - Populate Header Metadata, target commit SHA, and **Block 1: Auditor Prompt**.
   - **Mandatory Block 1 Rule**: Mandate that every auditor propose **at least 3 innovative ideas, trends, or pattern enhancements** on their respective topic.

2. **Phase 2: Concurrent Subagent Execution**
   - Launch 3 subagents concurrently via `invoke_subagent` across three perspectives:
     - **Perspective 1: Formal Logic & Safety**: Boundary enforcement, deterministic routing, failure containment.
     - **Perspective 2: DX & Architecture Alignment**: Ergonomics, documentation standards, friction reduction.
     - **Perspective 3: Adversarial Chaos & Edge-Cases**: Interrupted contexts, dirty state resilience, injection safety.
   - Each subagent writes findings into **Block 2: Audit Report** of its document (or returns the findings via `send_message` for parent orchestrator population if read-only). If a subagent execution fails or times out, perform 1 retry attempt before logging a fallback finding.

3. **Phase 3: Triage & Owner Presentation**
   - Consolidate findings into structured feedback records.
   - Present a unified Triage Matrix with expert recommendations (`accepted`, `rejected`, `superseded`) for owner disposition.

4. **Phase 4: Implementation, Validation, & Pass 2 Re-Audit**
   - Upon owner approval (`+`), apply accepted fixes.
   - Execute deterministic test validators.
   - Complete **Block 3: Work Done & Resolution Report** in all audit documents and initiate Pass 2 verification re-audit.

## Audit File & Triage Format Templates

### 1. Audit Document Header Template (`audits/YYYY-MM-DD-HHMM-<perspective>.md`)
```markdown
# Audit Log: [Perspective Name]
- **Date**: YYYY-MM-DD
- **Auditor Role**: [Auditor Role / Perspective]
- **Target Commit**: `[commit-sha]`
- **Pass**: [Pass 1 / Pass 2]

## Block 1: Auditor Prompt
[Detailed auditor prompt instructions including mandatory 3 innovation proposals]

## Block 2: Audit Report
[Populated by subagent auditor with findings and evidence]

## Block 3: Work Done & Resolution Report
[Populated after Pass 1 fixes and Pass 2 verification]
```

### 2. Consolidated Triage Matrix Example
```markdown
| ID | Perspective | Finding | Recommendation | Status |
|----|-------------|---------|----------------|--------|
| F-01 | Logic & Safety | Missing boundary check on recovery | Accepted (Fix in Pass 1) | Pending |
| F-02 | DX Alignment | Stale reference link in README | Accepted (Fix in Pass 1) | Pending |
| F-03 | Adversarial | Dirty worktree collision risk | Superseded by ADR-0002 | Superseded |
```
