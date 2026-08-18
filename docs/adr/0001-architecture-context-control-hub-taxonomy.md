# ADR 0001: Architecture Context Control Hub Taxonomy

- **Status**: APPROVED
- **Date**: 2026-08-18
- **Deciders**: Repository Owner & AI Assistant

---

## Context & Problem Statement

The repository `codex-architecture-skills` was initially established to manage reusable architecture skills. As the system expanded to cover the complete software architecture lifecycle (planning documentation, spec readiness, code implementation, guardrail checks, and release publishing), managing declarative rules alongside procedural skills required a structured, domain-isolated architecture taxonomy.

## Decision Drivers

- **Separation of Policy vs Procedure**: Declarative rules ("what MUST be obeyed") are distinct from procedural skills ("how work is performed").
- **Domain Isolation**: Software architecture standards must remain isolated from unrelated domains (such as marketing or video production) to prevent token bloat and context pollution.
- **Single Source of Truth**: Skills reside in `skills/`, plugins in `plugins/`, rules in `rules/`, and automated release scripts in `scripts/`.

## Decided Option

Establish `codex-architecture-skills` as a domain-isolated **Architecture Context Control Hub** structured as follows:

1. **`rules/`**: Declarative policies partitioned into `global/` (engineering, git, quality) and `stacks/` (php, laravel).
2. **`skills/`**: Canonical source of truth for procedural architecture workflows.
3. **`plugins/`**: Installable distribution bundles (`plugin.json`) referencing canonical skills.
4. **`docs/adr/`**: Architecture Decision Records documenting repository decisions.
5. **`scripts/`**: Dual-platform verification and distribution sync scripts.

## Consequences

- Clear separation between persistent policies (`rules/`), procedural workflows (`skills/`), and installation manifests (`plugins/`).
- Future domains (such as marketing or video production) can be created as separate domain hubs using this repository as a GitHub template.
