---
name: create-skill
description: >-
  Expert guide and workflow for creating, scaffolding, packaging, and validating new AI agent skills.
  Use when asked to create a new skill, scaffold a skill directory, write a SKILL.md specification, or package modular instructions.
---

# Create Skill — Skill Authoring & Scaffolding Protocol

This skill guides the creation of production-ready, reusable AI agent skills across workspace repositories and global machine configurations.

---

## 1. Skill Architecture & File Structure

Every skill must be packaged as a single directory inside a recognized `skills/` folder:

```text
skills/<skill-name>/
├── SKILL.md          # Required: Core instruction file with YAML frontmatter
├── scripts/          # Optional: Executable helper scripts (bash, powershell, python)
├── examples/         # Optional: Reference implementations and usage patterns
├── resources/        # Optional: Code templates, assets, or boilerplate schemas
└── references/       # Optional: Detailed documentation, manuals, or bulky specs
```

---

## 2. Location & Scope Matrix

Determine where the skill should be placed based on its intended scope:

| Scope | Directory Path | Target Use Case |
| :--- | :--- | :--- |
| **Source Repository (Single Source of Truth)** | `skills/<skill-name>/` | All skill source files are created and tracked strictly inside `codex-architecture-skills`. |
| **Global Discovery (Automatic Junction)** | `~/.gemini/config/skills/<skill-name>/` | Automatically created NTFS Directory Junction (symlink) pointing to the source folder in the repository. Never duplicate files physically. |

---

## 3. Specification Rules for `SKILL.md`

### YAML Frontmatter Requirements
The `SKILL.md` file MUST begin with a clean YAML frontmatter block:

```yaml
---
name: skill-name
description: >-
  Concise third-person description of what the skill does and when the agent should activate it.
  Include clear trigger phrases and target scenarios.
---
```

- **`name`**: Lowercase kebab-case slug (e.g. `scaffold-subproject-docs`, `publish-packagist-package`).
- **`description`**: Most critical field. Read by the primary agent during tool selection. Must explicitly state **what** the skill does and **when** it should be activated.

---

## 4. Best Practices for Skill Content

1. **Progressive Disclosure:** Keep `SKILL.md` high-level and focused. Place detailed documentation, schemas, or large examples in `references/` or `examples/` and link to them using relative paths.
2. **Executable Helpers:** Encapsulate complex or multi-step command sequences in executable scripts inside `scripts/`.
3. **Deterministic Guardrails:**
   - **Relative Paths Only:** Never hardcode absolute local paths (`C:\...`, `/Users/...`). Use relative links (e.g. `[script](scripts/run.sh)`).
   - **English-Only Documentation:** All skill files (`SKILL.md`, references, scripts) must be written exclusively in English.
   - **Validation Steps:** Always include instructions for how the agent can verify clean execution (e.g., test commands, log inspection).
