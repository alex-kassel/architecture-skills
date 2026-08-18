---
description: Quality & Repository Hygiene Standards
always_on: true
---

# Quality & Repository Hygiene Standards

- **Scope**: Applied globally across all repository files, specifications, scripts, and documentation.
- **Language**: English
- **Authority**: Permanent Policy

---

## 1. Relative Paths Standard
- All file and directory references in code, documentation, feedback records, and audit reports MUST use relative paths.
- Local absolute file paths (such as Windows drive letters, user home directories, or local file URIs) are strictly prohibited in tracked files.
- All relative path references MUST use POSIX forward slashes (`/`) instead of Windows backslashes (`\`).

## 2. English-Only Repository Standard
- All tracked repository files (code comments, docstrings, markdown documents, feedback records, audit logs) MUST be written exclusively in English.
- Non-English content in tracked files is prohibited.

## 3. Dual-Platform Scripting Standard
- All repository scripts MUST be dual-platform: either written as cross-platform Python (`.py`), or provided as paired scripts for Windows PowerShell (`.ps1`) and macOS/Linux POSIX Bash (`.sh`).
