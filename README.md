# Architecture Skills & Plugin Bundles for AI Agents

> Production-ready, vendor-neutral architecture skills and plugin bundles for AI coding assistants and developers. Built for deterministic documentation-as-code, single-agent ownership locking, audit safety, and continuous skill maintenance.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validation: Passing](https://img.shields.io/badge/Validation-Passing-brightgreen.svg)](evals/forward-tests.md)
[![Architecture: V1--Bound](https://img.shields.io/badge/Architecture-V1--Bound-orange.svg)](design/)

---

## 🎯 Repository Overview

`architecture-skills` is a maintainer repository for reusable architecture skills and installable plugin bundles. It separates reusable capabilities into two top-level directories:

* 🛠️ **[`skills/`](skills/README.md)**: Individual standalone skill packages (e.g. `session-lifecycle`, `scaffold-subproject-docs`, `guide-architecture-design`, `execute-autonomous-audit`).
* 📦 **[`plugins/`](plugins/README.md)**: Pre-packaged plugin bundles (e.g. `architecture-suite`) that group related skills into a single 1-step installation manifest (`plugin.json`).

---

## 📁 Repository Structure

```text
codex-architecture-skills/
├── README.md               # Root repository overview (this document)
├── AGENTS.md               # Governance rules, intent routing, and guardrail policies
├── skills/                 # Standalone architecture skill packages (see skills/README.md)
│   ├── session-lifecycle/
│   ├── scaffold-subproject-docs/
│   ├── guide-architecture-design/
│   └── ...
├── plugins/                # Plugin bundle manifests (see plugins/README.md)
│   └── architecture-suite/
├── evals/                  # Forward-test ledgers and acceptance criteria
├── design/                 # Architectural specifications and rationale
├── audits/                 # Multi-perspective autonomous audit logs
└── feedback/               # Incident & triage logs
```

---

## 🚀 Quick Start

### 1. Loading a Plugin Bundle (Recommended)

To equip an AI agent or IDE with the complete architecture suite in 1 step, point to the plugin manifest in [`plugins/README.md`](plugins/README.md):

```bash
# Clone the architecture skills distribution repository
git clone https://github.com/alex-kassel/skills.git

# Point your agent to the architecture-suite plugin bundle
# Loads session-lifecycle, scaffold-subproject-docs, and guide-architecture-design automatically
```

### 2. Loading Individual Standalone Skills

To install specific individual skills, copy the target skill folder from [`skills/README.md`](skills/README.md):

```bash
# Copy a specific skill to your local agent skills path
cp -r skills/session-lifecycle ~/.gemini/config/skills/
cp -r skills/scaffold-subproject-docs ~/.gemini/config/skills/
```

---

## 🛠️ Verification & Release Sync

Validate repository guardrails and sync releases to the public distribution repository:

```bash
# Run cross-platform path and language guardrail checks
python scripts/validate_relative_paths.py
python scripts/validate_english_only.py

# Sync skills/ and plugins/ to alex-kassel/skills distribution repository
./scripts/sync-skills.sh      # macOS / Linux Bash
powershell -File scripts/sync-skills.ps1  # Windows PowerShell
```

---

## 📜 Governance & Maintenance

All skill updates follow the 6-step maintenance protocol defined in [`skills/maintain-architecture-skills/SKILL.md`](skills/maintain-architecture-skills/SKILL.md):
1. **Feedback Capture**: Log incidents in `feedback/YYYY-MM-DD-*.md`.
2. **Owner Triage**: Present proposal for explicit approval (`+`).
3. **Autonomous Audit**: Execute 4-phase, 2-pass audits per [`skills/execute-autonomous-audit/SKILL.md`](skills/execute-autonomous-audit/SKILL.md).
4. **Guardrail Check**: Verify 100% relative paths and English-only compliance before commit.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
