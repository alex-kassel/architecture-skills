---
name: context7
description: Fetch up-to-date, version-specific library documentation, code examples, and API references for LLMs using Context7 (Upstash). Use whenever the user asks about library configuration, setup, API usage, or requests code examples for third-party packages, libraries, or frameworks.
---

# Context7 — Up-to-Date Code Documentation & LLM Library Integration

Context7 is an open-source platform by Upstash that fetches up-to-date, version-specific documentation and code examples from official sources and GitHub repositories to eliminate LLM hallucinations and outdated API usage.

## Workflow & Execution Protocol

Whenever a user prompt mentions configuring, setting up, or building code for a specific library, framework, or package (e.g. Next.js, Laravel, React Query, Tailwind, Upstash, PyTorch, etc.):

1. **Invoke Context7 CLI / MCP Tool:**
   - Execute the `ctx7` CLI query command:
     `npx ctx7 library <library-name> <query>`
   - Or call the `context7` MCP tool if available in the environment.

2. **Context Integration:**
   - Inspect the returned documentation snippets and code examples.
   - Use the retrieved context to answer user questions or generate code targeting the exact library version specified.
