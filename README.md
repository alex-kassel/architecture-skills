# Architecture Context Control Hub for AI Agents

> Production-ready, vendor-neutral Architecture Context Control Hub for AI coding assistants and developers. Manages the complete architecture lifecycle: documentation planning, spec readiness, code implementation, guardrail checks, and production release publishing.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validation: Passing](https://img.shields.io/badge/Validation-Passing-brightgreen.svg)](evals/forward-tests.md)
[![Architecture: V1--Bound](https://img.shields.io/badge/Architecture-V1--Bound-orange.svg)](design/)

---

## 🎯 Repository Overview

`architecture-skills` serves as a domain-isolated **Architecture Context Control Hub**. It organizes architectural knowledge into four distinct operational capabilities:

* 📋 **[`rules/`](rules/README.md)**: Declarative rules and permanent policies (`rules/global/` and `rules/stacks/`).
* 🛠️ **[`skills/`](skills/README.md)**: Canonical source of truth for procedural architecture workflows.
* 📦 **[`plugins/`](plugins/README.md)**: Pre-packaged plugin bundles (e.g. `architecture-suite`) for 1-step installation.
* 🏛️ **[`docs/adr/`](docs/adr/0001-architecture-context-control-hub-taxonomy.md)**: Architecture Decision Records documenting repository decisions.

---

## 📁 Repository Structure

```text
codex-architecture-skills/
├── README.md               # Root repository overview (this document)
├── AGENTS.md               # Governance rules, intent routing, and guardrail policies
├── rules/                  # Declarative policies (see rules/README.md)
│   ├── global/             # Engineering, Git, and Quality rules
│   └── stacks/             # PHP and Laravel stack rules
├── skills/                 # Standalone architecture skill packages (see skills/README.md)
│   ├── session-lifecycle/
│   ├── scaffold-subproject-docs/
│   ├── guide-architecture-design/
│   └── ...
├── plugins/                # Plugin bundle manifests (see plugins/README.md)
│   └── architecture-suite/
├── docs/                   # Documentation & ADR logs
│   └── adr/
├── evals/                  # Forward-test ledgers and acceptance criteria
├── design/                 # Architectural specifications and rationale
├── audits/                 # Multi-perspective autonomous audit logs
└── feedback/               # Incident & triage logs
```

---

## 🚀 Quick Start

### 1. Loading Rules & Policies

To apply global or stack-specific rules to your AI agent or workspace, reference the target rule file from [`rules/README.md`](rules/README.md):

- Universal Engineering Rules: [`rules/global/engineering.md`](rules/global/engineering.md)
- Git & Release Rules: [`rules/global/git.md`](rules/global/git.md)
- Quality & Guardrails: [`rules/global/quality.md`](rules/global/quality.md)
- PHP & Laravel Rules: [`rules/stacks/php.md`](rules/stacks/php.md), [`rules/stacks/laravel.md`](rules/stacks/laravel.md)

### 2. Loading a Plugin Bundle (Recommended)

To equip an AI agent with the complete architecture suite in 1 step, point to the plugin manifest in [`plugins/README.md`](plugins/README.md):

```bash
# Clone the public skills & plugins distribution repository
git clone https://github.com/alex-kassel/skills.git
```

---

## 🛠️ Verification & Release Sync

Validate repository guardrails and sync releases to the public distribution repository:

```bash
# Run cross-platform path and language guardrail checks
python scripts/validate_relative_paths.py
python scripts/validate_english_only.py

# Sync skills/ and plugins/ to alex-kassel/skills distribution repository
./scripts/sync-skills.sh                  # macOS / Linux Bash
powershell -File scripts/sync-skills.ps1  # Windows PowerShell
```

---

## 📜 Governance & Maintenance

All skill and rule updates follow the 6-step maintenance protocol defined in [`skills/maintain-architecture-skills/SKILL.md`](skills/maintain-architecture-skills/SKILL.md):
1. **Feedback Capture**: Log incidents in `feedback/YYYY-MM-DD-*.md`.
2. **Owner Triage**: Present proposal for explicit approval (`+`).
3. **Autonomous Audit**: Execute 4-phase, 2-pass audits per [`skills/execute-autonomous-audit/SKILL.md`](skills/execute-autonomous-audit/SKILL.md).
4. **Guardrail Check**: Verify 100% relative paths and English-only compliance before commit.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
