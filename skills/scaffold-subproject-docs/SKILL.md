---
name: scaffold-subproject-docs
description: Scaffold the standard 5-file architecture documentation suite (README.md, session-handoff-protocol.md, project-documentation-roadmap.md, architecture-planning-roadmap.md, worklog.md) for new or existing platform subprojects. Make sure to trigger this skill whenever the user asks to bootstrap, initialize, scaffold, generate, or set up documentation for a new or existing subproject, module, or repository, or requests the standard 5-file architecture documentation suite (README.md, session-handoff-protocol.md, project-documentation-roadmap.md, architecture-planning-roadmap.md, worklog.md), even if only subproject docs setup is mentioned.
---

# Scaffold Subproject Documentation Suite

Scaffold and initialize the standard 5-file architecture documentation suite for new or existing platform subprojects.

## 1. Documentation Suite Overview

Every subproject requires a standard set of 5 architecture files to maintain document-as-code discipline, fresh-session context safety, and clear decision governance:

| Document | Purpose | Reference Template |
| :--- | :--- | :--- |
| `README.md` | Primary entrypoint, subproject boundaries, quick start, and documentation index. | [`references/templates/README.md`](references/templates/README.md) |
| `session-handoff-protocol.md` | Session persistence, handoff state capture, decision logs, and context recovery. | [`references/templates/session-handoff-protocol.md`](references/templates/session-handoff-protocol.md) |
| `project-documentation-roadmap.md` | Documentation milestones, maintenance schedule, ownership matrix, and debt backlog. | [`references/templates/project-documentation-roadmap.md`](references/templates/project-documentation-roadmap.md) |
| `architecture-planning-roadmap.md` | Target state architecture, design milestones, technical trade-offs, and ADR index. | [`references/templates/architecture-planning-roadmap.md`](references/templates/architecture-planning-roadmap.md) |
| `worklog.md` | Chronological session worklog, completed items, active experiments, and open questions. | [`references/templates/worklog.md`](references/templates/worklog.md) |

---

## 2. Bootstrapping Protocol

When bootstrapping or initializing documentation for a subproject, follow this protocol:

1. **Target Identification & Pre-Flight Collision Check**:
   - Determine subproject root directory and boundary.
   - Verify whether documentation lives at root or inside a `.docs/` / `docs/` folder.
   - **Collision Check**: Check if target documentation files already exist. If target files exist, halt and require explicit owner confirmation (`+`) before overwriting.

2. **Template Instantiation**:
   - Copy each template from `references/templates/` to the target subproject documentation directory.
   - Replace placeholder tokens (e.g. `{{SUBPROJECT_NAME}}`, `{{DESCRIPTION}}`, `{{DATE}}`, `{{OWNER}}`, `{{VERSION}}`) with concrete subproject values.

3. **Context Initialization**:
   - Initialize `worklog.md` with an initial entry recording the subproject bootstrapping event.
   - Set up `session-handoff-protocol.md` with current session status and active focus.
   - Outline initial milestones in `project-documentation-roadmap.md` and `architecture-planning-roadmap.md`.

4. **Validation**:
   - Verify all cross-file references use relative paths.
   - Verify no hardcoded local machine paths exist in any created document.

---

## Output Template

### Scaffolding Completion Report
ALWAYS use this template when reporting subproject documentation scaffolding:

```markdown
### Documentation Suite Scaffolding Summary: [Subproject Name]
- **Target Path**: `[path/to/docs]`
- **Scaffolded Files**:
  - `README.md`
  - `session-handoff-protocol.md`
  - `project-documentation-roadmap.md`
  - `architecture-planning-roadmap.md`
  - `worklog.md`
- **Token Replacement**: `{{SUBPROJECT_NAME}}`, `{{DATE}}`, `{{OWNER}}` populated.
- **Guardrails Verified**: Zero absolute paths, 100% English.
```
