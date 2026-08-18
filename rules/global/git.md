---
description: Git Version Control & Commit Standards
always_on: true
---

# Git Version Control & Commit Standards

- **Scope**: Applied globally across all repository version control operations and release workflows.
- **Language**: English
- **Authority**: Permanent Policy

---

## 1. Atomic Commit Protocol
- Commits MUST represent a single logical change or milestone.
- Do NOT mix unrelated edits, formatting fixes, or multiple feature implementations into a single commit.

## 2. Conventional Commit Formatting
- Use standard Conventional Commit prefixes:
  - `feat(...)`: New features or capabilities.
  - `fix(...)`: Bug fixes and error remediations.
  - `docs(...)`: Documentation, audit log, or feedback updates.
  - `refactor(...)`: Code/structure improvements without behavior changes.
  - `test(...)`: Adding or updating tests.
  - `audit(...)`: Audit logs and pass resolutions.

## 3. Prohibition of Destructive Operations
- Destructive Git operations (`git push --force`, `git push -f`, `git push --delete`) are strictly prohibited in automated scripts and release preflight gates.
- Worktrees MUST be verified clean before initiating release sync operations.
