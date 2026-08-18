# AI Agent Skills Registry

> Production-ready, evidence-validated architecture skills for AI coding agents and developers.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Source: architecture-skills](https://img.shields.io/badge/Source-architecture--skills-orange.svg)](https://github.com/alex-kassel/architecture-skills)

---

## 📚 Available Skills

| Skill | Category | Description | Spec |
| --- | --- | --- | --- |
| **`guide-architecture-design`** | Design & Workflow | Guide owner-led architecture design workflows, scenario-based interviews, decision capture, and atomic documentation synchronization. | [`SKILL.md`](guide-architecture-design/SKILL.md) |
| **`audit-architecture-handoff`** | Audit & Verification | Perform strictly read-only audits for fresh-session handoff safety, architectural consistency, document drift, and implementation readiness gates. | [`SKILL.md`](audit-architecture-handoff/SKILL.md) |

---

## ⚡ Quickstart

### Installing Skills into an Agent Workspace

To install any skill into your local agent environment (e.g. Antigravity, Cursor, Claude Code, custom agents), copy the target skill folder into your agent's skill path:

```bash
# Clone this skills repository
git clone https://github.com/alex-kassel/skills.git

# Copy desired skill folder to your agent's skill directory
cp -r skills/guide-architecture-design ~/.gemini/skills/
cp -r skills/audit-architecture-handoff ~/.gemini/skills/
```

---

## 🛠️ Maintenance & Contributions

This repository is an automated downstream distribution mirror of the maintainer monorepo **[`alex-kassel/architecture-skills`](https://github.com/alex-kassel/architecture-skills)**.

To report issues, submit feedback, or contribute to skill development, please visit the maintainer repository:
👉 **[alex-kassel/architecture-skills](https://github.com/alex-kassel/architecture-skills)**

---

## 📄 License

Distributed under the [MIT License](https://opensource.org/licenses/MIT).
