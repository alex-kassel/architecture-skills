# Architecture Skills for AI Agents

> Production-ready, vendor-neutral architecture skills for AI coding assistants and developers. Built for deterministic documentation-as-code, audit safety, and continuous skill maintenance.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validation: Passing](https://img.shields.io/badge/Validation-Passing-brightgreen.svg)](evals/forward-tests.md)
[![Architecture: V1--Bound](https://img.shields.io/badge/Architecture-V1--Bound-orange.svg)](design/)

---

## 🎯 Overview

`architecture-skills` provides a suite of reusable, battle-tested skills for AI agents operating in software architecture and specification-as-code repositories. 

The repository defines two primary operational capabilities:

1. **[`guide-architecture-design`](skills/guide-architecture-design/SKILL.md)**: Guides owner-led architecture design workflows, scenario-based interviews, decision capture, and atomic documentation synchronization.
2. **[`audit-architecture-handoff`](skills/audit-architecture-handoff/SKILL.md)**: Performs strictly read-only audits for fresh-session handoff safety, architectural consistency, document drift, and implementation readiness gates.

---

## ✨ Key Capabilities & Architectural Principles

### 🧠 Critical Thinking & Reasoned Pushback
Agents are instructed to exercise architectural vigilance. When evaluating design choices containing technical or performance risks, agents provide up to three attempts of rephrased, reasoned pushback with technical rationale before accepting final owner disposition.

### 🔄 5-State Package Lifecycle & Platform Matrix
Tracks software components across explicit lifecycle states:
```
[SPEC_IN_PROGRESS] ──> [IMPLEMENTATION_READY] ──> [IN_DEVELOPMENT (vX.Y.Z-dev)] ──> [RELEASED (vX.Y.Z)] ──> [DEPRECATED]
```
Maintains a central `Platform Status Matrix` across multi-package platform repositories to eliminate documentation drift.

### 🌿 Real-Time GitHub Tracking (Session Branch + Eager Draft PR)
Supports real-time visibility during design sessions:
- Initializes an isolated session branch (`agent/session-<ID>`) and **Eager Draft PR** at session start.
- Pushes completed in-session batches for live GitHub tracking.
- Performs clean **Squash Merge** into `main` and branch cleanup upon owner confirmation (`+`).

### 🛡️ Preflight Audit & Developer Community Benchmarking
- **Preflight Alignment**: Automatically audits local project documentation against installed skills upon session startup to resolve duplications or contradictions.
- **Community Benchmarking**: Every proposed workflow refinement is benchmarked against established software engineering patterns (Git Flow, Semantic Versioning, DRY docs) with explicit community-backed recommendations.

---

## 📁 Repository Structure

```text
architecture-skills/
├── README.md               # Public project documentation
├── AGENTS.md               # Skill maintenance rules & triage protocols for AI agents
├── skills/                 # Reusable architecture skill packages
│   ├── guide-architecture-design/
│   └── audit-architecture-handoff/
├── evals/                  # Forward-test ledgers and acceptance criteria
│   └── forward-tests.md
├── design/                 # Architectural specifications and rationale
└── feedback/               # Evidence-backed incident & workflow triage log
```

---

## 🚀 Quickstart

### Installing Skills into an Agent Workspace

To equip an AI agent with these skills, copy or symlink the target skill directory into your workspace's skill path:

```bash
# Clone the architecture-skills repository
git clone https://github.com/<your-org>/architecture-skills.git

# Copy or reference desired skills into your agent's skill directory
cp -r architecture-skills/skills/guide-architecture-design ~/.gemini/skills/
cp -r architecture-skills/skills/audit-architecture-handoff ~/.gemini/skills/
```

### Running Structural & Path Validation

Validate relative paths and repository integrity across macOS, Linux, and Windows:

```bash
# Cross-platform Python 3 path validation (macOS, Linux, Windows)
python3 scripts/validate_relative_paths.py

# Windows PowerShell path validation
powershell -ExecutionPolicy Bypass -File scripts/validate-relative-paths.ps1
```

### Downstream Release Sync

Sync the `skills/` directory to the public distribution repository:

```bash
# macOS / Linux Bash sync
./scripts/sync-skills.sh

# Windows PowerShell sync
powershell -ExecutionPolicy Bypass -File scripts/sync-skills.ps1
```

---

## 📜 Maintenance & Triage Workflow

All improvements to these skills follow an evidence-based maintenance protocol:
1. **Feedback Capture**: Incidents and refinements are recorded in `feedback/YYYY-MM-DD-*.md`.
2. **Community Triage**: Proposals are evaluated against developer community standards before owner approval.
3. **Validation & Evidence**: Changed skills pass `quick_validate.py` structural checks and record realistic forward-test coverage in `evals/forward-tests.md`.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
