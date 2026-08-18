---
name: execute-autonomous-audit
description: Execute autonomous 4-phase, 2-pass iterative multi-perspective audits of codebases, software architecture, or documentation sets using concurrent subagents and structured audit logs. Use when asked to run or start an autonomous multi-perspective audit, conduct a 2-pass iterative audit cycle, or generate structured audit reports with mandatory innovation proposals.
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

### Protocol Execution Phases

1. **Phase 1: Audit Document Initialization**
   - Initialize 3 audit files in the project's audit registry (e.g. `audits/YYYY-MM-DD-HHMM-<perspective>.md`).
   - Populate Header Metadata, target commit SHA, and **Block 1: Auditor Prompt**.
   - **Mandatory Block 1 Rule**: Mandate that every auditor propose **at least 3 innovative ideas, trends, or pattern enhancements** on their respective topic.

2. **Phase 2: Concurrent Subagent Execution**
   - Launch 3 subagents concurrently via `invoke_subagent` across three perspectives:
     - **Perspective 1: Formal Logic & Safety**: Boundary enforcement, deterministic routing, failure containment.
     - **Perspective 2: DX & Architecture Alignment**: Ergonomics, documentation standards, friction reduction.
     - **Perspective 3: Adversarial Chaos & Edge-Cases**: Interrupted contexts, dirty state resilience, injection safety.
   - Each subagent writes findings into **Block 2: Audit Report** of its document.

3. **Phase 3: Triage & Owner Presentation**
   - Consolidate findings into structured feedback records.
   - Present a unified Triage Matrix with expert recommendations (`accepted`, `rejected`, `superseded`) for owner disposition.

4. **Phase 4: Implementation, Validation, & Pass 2 Re-Audit**
   - Upon owner approval (`+`), apply accepted fixes.
   - Execute deterministic test validators.
   - Complete **Block 3: Work Done & Resolution Report** in all audit documents and initiate Pass 2 verification re-audit.
