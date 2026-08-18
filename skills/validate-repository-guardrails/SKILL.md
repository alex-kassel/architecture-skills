---
name: validate-repository-guardrails
description: Execute deterministic quality, path, and language guardrail checks across repository files to prevent local path leaks, absolute path references, and non-English content. Use when asked to run pre-commit guardrail validation, verify path relativity, or check language compliance across repository files.
---

# Validate Repository Guardrails

Execute deterministic guardrail checks to enforce repository cleanliness, cross-platform path portability, and language standards.

## Guardrail Rules & Standards

### 1. Relative Paths Standard
- All file and directory references in code, documentation, feedback records, and audit reports MUST use relative paths (e.g. `skills/guide-architecture-design/SKILL.md#L15`).
- Local absolute paths (e.g. `C:\...`, `file:///C:/...`, `/Users/...`, `/home/...`) are strictly prohibited in tracked files.
- Only HTTP/HTTPS URLs are permitted for external links.

### 2. English-Only Repository Standard
- All tracked repository files (code comments, docstrings, markdown documents, feedback records, audit logs) MUST be written exclusively in English.
- Non-English content in tracked files is prohibited.

---

## Execution & Remediation

1. **Path Validation**:
   - Execute `python scripts/validate_relative_paths.py` (or equivalent path checker).
   - If absolute path violations are detected, report file path and line number, remediate immediately, and re-run.

2. **Language Validation**:
   - Execute `python scripts/validate_english_only.py` (or equivalent language checker).
   - Ensure 100% English compliance across all tracked files.

3. **Pre-Commit Gate**:
   - Guardrails MUST exit with Code 0 prior to any Git commit or pre-push release gate.
