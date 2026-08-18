# Standalone AI Agent Skills Registry

> Production-ready, evidence-validated architecture skills for AI coding agents and developers.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Source: architecture-skills](https://img.shields.io/badge/Source-architecture--skills-orange.svg)](https://github.com/alex-kassel/architecture-skills)

---

## 📚 Available Standalone Skills

| Skill | Category | Description | Spec |
| --- | --- | --- | --- |
| **`session-lifecycle`** | Lifecycle & Locking | Manage exclusive subproject working sessions, root corridor detection, single-agent ownership locking, RFC 3339 duration tracking, and handoff session closure. | [`SKILL.md`](session-lifecycle/SKILL.md) |
| **`scaffold-subproject-docs`** | Scaffolding & Setup | Scaffold standard 5-file architecture documentation suite (`README.md`, `session-handoff-protocol.md`, `project-documentation-roadmap.md`, `architecture-planning-roadmap.md`, `worklog.md`). | [`SKILL.md`](scaffold-subproject-docs/SKILL.md) |
| **`guide-architecture-design`** | Design & Workflow | Guide owner-led architecture design workflows, scenario-based interviews, decision capture, and atomic documentation synchronization. | [`SKILL.md`](guide-architecture-design/SKILL.md) |
| **`audit-architecture-handoff`** | Audit & Verification | Perform strictly read-only audits for fresh-session handoff safety, architectural consistency, document drift, and implementation readiness gates. | [`SKILL.md`](audit-architecture-handoff/SKILL.md) |
| **`git-release-preflight`** | Git & Release | Pre-push readiness evaluations, guardrail verification, risk assessment, pushback presentation, and clean git release/push execution. | [`SKILL.md`](git-release-preflight/SKILL.md) |
| **`execute-autonomous-audit`** | Audit & Verification | Execute autonomous 4-phase, 2-pass iterative multi-perspective audits of codebases, software architecture, or documentation sets. | [`SKILL.md`](execute-autonomous-audit/SKILL.md) |
| **`publish-packagist-package`** | Release & Publishing | Guide standalone package publishing, Composer metadata validation, dual Git workflow setup, and Packagist CI scaffolding. | [`SKILL.md`](publish-packagist-package/SKILL.md) |
| **`validate-repository-guardrails`** | Quality & Guardrails | Execute deterministic quality, relative path, and English-only language guardrail checks across repository files. | [`SKILL.md`](validate-repository-guardrails/SKILL.md) |
| **`maintain-architecture-skills`** | Maintenance & Meta | Execute the 6-step skill maintenance protocol for feedback triage, zero-write preflight, and skill updates. | [`SKILL.md`](maintain-architecture-skills/SKILL.md) |

---

## 📦 Prefer 1-Step Plugin Bundles?

If you prefer installing pre-packaged bundles of related skills in a single step, see the **[Plugin Bundles Registry](/plugins/README.md)** (e.g. `architecture-suite`).

---

## ⚡ Quickstart

To install any standalone skill into your local agent environment (e.g. Antigravity, Cursor, Claude Code, custom agents), copy the target skill folder into your agent's skill path:

```bash
# Clone the public skills distribution repository
git clone https://github.com/alex-kassel/skills.git

# Copy desired skill folder to your agent's skill directory
cp -r skills/session-lifecycle ~/.gemini/config/skills/
cp -r skills/scaffold-subproject-docs ~/.gemini/config/skills/
```

---

## 🔗 Related Documentation

- 📦 **[Plugin Bundles Registry](/plugins/README.md)**: Explore 1-step plugin bundles.
- 🏠 **[Root Repository Overview](/README.md)**: Return to main repository overview.
