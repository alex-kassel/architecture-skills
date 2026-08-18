---
description: Universal Engineering Standards & Principles
always_on: true
---

# Universal Engineering Standards & Principles

- **Scope**: Applied globally across all architecture planning, specification drafting, and code implementation.
- **Language**: English
- **Authority**: Permanent Policy

---

## 1. Single Source of Truth (SSOT)
- Every system invariant, data schema, or business rule MUST exist in exactly one authoritative location.
- Documentation, code comments, and test assertions must reference the single source of truth without duplicating logic.

## 2. No Superficial Patches
- Never resolve runtime failures or test breakages by masking symptoms, swallowing exceptions, returning dummy fallbacks, or deleting assertions.
- When a failure occurs, trace the root cause upstream to the exact contract breach before modifying code.

## 3. Preservation of API Contracts
- Maintain backwards compatibility across public interfaces and package APIs.
- Parameter signature modifications require inspecting and updating all invocation sites across dependent packages.

## 4. Audit Before Re-inventing
- Search the codebase and dependency trees for pre-existing utility functions or established patterns before writing custom helper classes from scratch.
