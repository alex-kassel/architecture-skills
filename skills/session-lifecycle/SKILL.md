---
name: session-lifecycle
description: Manage exclusive subproject working sessions, root corridor detection, single-agent ownership locking, RFC 3339 duration tracking, decision boundary recording, and handoff session closure protocols. Make sure to trigger this skill whenever the user asks to start a working session, continue a session, close or end a session, check active session status, inspect subproject ownership lock, or manage session time accounting, regardless of phrasing or language.
---

# Session Lifecycle & Single-Agent Ownership Protocol

Manage the lifecycle of working sessions across root workspace corridors and bound subprojects, enforcing exclusive single-agent ownership locks, RFC 3339 time accounting, and structured handoff session closure.

---

## 1. Corridor vs Subproject Routing Protocol

When an agent is invoked, evaluate the target path before initiating session actions:

```text
┌─────────────────────────────────────────────────────────────────┐
│                     1. ROOT CORRIDOR CHECK                      │
│   Target path lacks subproject binding badge AND 5-file suite   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
       [Ad-hoc Request]                  [Explicit Session Request]
  - Do NOT auto-start session       - Execute Session Startup (Step 2)
  - Do NOT start RFC 3339 timer     - Take Exclusive Ownership Lock
  - Answer questions freely         - Record start time in worklog.md
```

### Root Corridor Behavior
- **Definition**: A directory or workspace root that lacks BOTH a subproject binding badge (`> Architecture Suite: Bound to plugin:architecture-suite` in `README.md`) AND the standard 5-file architecture documentation suite (`README.md`, `session-handoff-protocol.md`, `project-documentation-roadmap.md`, `architecture-planning-roadmap.md`, `worklog.md`).
- **Rule**: Do NOT auto-start a session or timer. Answer ad-hoc questions and perform single-turn requests freely without creating worklog entries.
- **Explicit Session Request**: If the user explicitly asks to start a session in the corridor, proceed to Session Startup (Section 2).

### Subproject Entry Behavior
- **Definition**: A subproject directory containing a bound architecture suite (either `README.md` with binding badge OR the standard 5-file suite).
- **Rule**: Working without an active session inside a bound subproject is PROHIBITED.
- **Read-Only Audit Exemption**: Strictly read-only audit workflows (e.g. `audit-architecture-handoff` or `execute-autonomous-audit` operating in `AUDIT_ONLY` mode) are EXEMPT from active session creation and MUST NOT mutate `worklog.md`.

---

## 2. Session Startup & Single-Agent Ownership Lock

When entering a bound subproject or executing an explicit session startup:

1. **Check Existing Ownership Lock & Re-entrancy**:
   - Inspect `worklog.md` (authoritative lock state provider).
   - **Same-Agent Re-entrancy**: If an `ACTIVE` session is owned by the *current* Agent ID (`[agent-type/id]`), confirm active status, resume session context without creating a duplicate `ACTIVE` block, and log `SESSION_RESUMED`.
   - **Stale Lock Recovery**: If an `ACTIVE` lock timestamp is older than 24 hours (or an explicit owner override `force-unlock` / `+` is supplied), log `FORCE_CLOSED (STALE)` for the abandoned session before acquiring the new lock.
   - **Other-Agent Lock Enforcement**: If an `ACTIVE` session owned by another active agent ID exists, enforce **READ-ONLY LOCK**:
     - Do NOT modify any file under the subproject.
     - Report: `"Subproject is locked by active session [S-00X] owned by another agent. Operating in READ-ONLY mode until the session is closed."`
     - Halt all mutation actions.

2. **Acquire Exclusive Ownership Lock**:
   - If no active session exists (or previous session is `CLOSED`), capture current timestamp (ISO 8601 / RFC 3339).
   - Auto-increment Session ID (`S-001`, `S-002`, ..., `S-00(N+1)` by scanning highest index in `worklog.md`).
   - Append an `ACTIVE` session block to `worklog.md` with current Agent ID format `[agent-type/id]`.
   - Restate the current phase, last confirmed `decision_boundary`, and exact next action in 1 concise opening sentence.

---

## 3. Session Closing Protocol (Handoff)

When the user issues a session closing command (e.g. `Ending session`, `Close session`, or session closure instruction):

1. **Freeze Decision Boundary**:
   - Ensure all confirmed decisions are recorded in living specifications (ADRs / roadmaps).
   - Record the explicit `decision_boundary` and exact next step for the next incoming session.

2. **Close Time Accounting**:
   - Observe closing timestamp (RFC 3339).
   - Calculate active duration as session wall time minus declared breaks (`Break: YYYY-MM-DDTHH:MM:SSZ to YYYY-MM-DDTHH:MM:SSZ`).
   - Fallback duration formula: `max(0, closing_timestamp - start_timestamp - break_duration)`.
   - Update cumulative duration totals in `worklog.md`.

3. **Release Ownership Lock**:
   - Mark session status in `worklog.md` as `CLOSED`.
   - Release exclusive agent ownership lock.

4. **Guardrail Verification & Handoff Summary**:
   - Execute path and language guardrail checks (`python scripts/validate_relative_paths.py` and `python scripts/validate_english_only.py`).
   - Check `git status --short --branch`.
   - Propose or create a focused local Git commit upon owner confirmation (`+`).
   - Present a concise 5-bullet Handoff Summary (Closed At, Active Duration, Decision Boundary, Next Action, Ownership Lock, Git Commit).

---

## Output Format Templates

### Session Startup Report Template
```markdown
### Session Opened: [S-00X]
- **Subproject**: `[path/to/subproject]`
- **Ownership Lock**: ACQUIRED (`[agent-type/id]`)
- **Started At**: `YYYY-MM-DDTHH:MM:SSZ`
- **Current Position**: [1-sentence summary of phase and next action]
```

### Session Handoff Summary Template
```markdown
### Session Closed: [S-00X]
- **Closed At**: `YYYY-MM-DDTHH:MM:SSZ`
- **Active Duration**: `[HH:MM:SS]` (Breaks: `[HH:MM:SS]`)
- **Decision Boundary**: [Last confirmed decision]
- **Next Action**: [Exact starting point for next session]
- **Ownership Lock**: RELEASED
- **Git Commit**: `[commit-sha / Pending]`
```
