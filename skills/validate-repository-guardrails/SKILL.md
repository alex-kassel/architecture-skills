---
name: validate-repository-guardrails
description: Execute deterministic quality, path, and language guardrail checks across repository files to prevent local path leaks, absolute path references, and non-English content. Make sure to use this skill whenever the user asks to run guardrails, validate repository hygiene, check path relativity, verify non-leakage of absolute paths, run language compliance checks, or run pre-commit quality validation across repository files, even if guardrails are mentioned casually.
---

# Validate Repository Guardrails

Execute deterministic guardrail checks to enforce repository cleanliness, cross-platform path portability, and language standards.

## Guardrail Rules & Standards

### 1. Relative Paths Standard
- All file and directory references in code, documentation, feedback records, and audit reports MUST use relative paths (e.g. `skills/guide-architecture-design/SKILL.md#L15`).
- Local machine absolute paths (such as Windows drive letters, user home directories, or local file URIs) are strictly prohibited in tracked files.
- **POSIX Path Normalization Invariant**: All relative path references in tracked files MUST use POSIX forward slashes (`/`) instead of Windows backslashes (`\`).
- Only HTTP/HTTPS URLs are permitted for external links.

### 2. English-Only Repository Standard
- All tracked repository files (code comments, docstrings, markdown documents, feedback records, audit logs) MUST be written exclusively in English.
- Non-English content in tracked files is prohibited.

### 3. Dual-Platform Scripting Standard
- All repository scripts MUST be dual-platform: either written as cross-platform Python (`.py`), or provided as paired scripts for Windows PowerShell (`.ps1`) and macOS/Linux POSIX Bash (`.sh`).
- Single-platform scripts without a cross-platform or paired counterpart are prohibited.

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

---

## Output Template

### Guardrail Execution Report
ALWAYS use this template when reporting guardrail execution results:

```markdown
### Guardrail Validation Summary
- **Relative Path Check**: `PASS` | `FAIL` (`python scripts/validate_relative_paths.py`)
- **English-Only Check**: `PASS` | `FAIL` (`python scripts/validate_english_only.py`)
- **Violations Identified**: [List file & line numbers, or None]
- **Exit Status**: Code 0 (Success)
```
