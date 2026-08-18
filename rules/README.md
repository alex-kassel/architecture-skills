# Architecture Rules & Policies Registry

> Centralized, declarative rules and policies governing software architecture, code quality, version control, and stack-specific standards.

---

## 📚 Global Rules (`rules/global/`)

| Rule File | Category | Description | Spec |
| --- | --- | --- | --- |
| **`engineering.md`** | Core Principles | Universal engineering standards: Single Source of Truth (SSOT), No Superficial Patches, API contract preservation. | [`engineering.md`](global/engineering.md) |
| **`git.md`** | Version Control | Git commit standards: atomic commits, conventional commit prefixes, prohibition of destructive operations (`--force`). | [`git.md`](global/git.md) |
| **`quality.md`** | Guardrails & Hygiene | Quality standards: relative POSIX forward-slash paths, English-only content, dual-platform scripting. | [`quality.md`](global/quality.md) |

---

## 💻 Stack-Specific Rules (`rules/stacks/`)

| Rule File | Stack | Description | Spec |
| --- | --- | --- | --- |
| **`php.md`** | PHP & Composer | PSR-12 coding style, strict typing, publication-ready `composer.json` metadata standards. | [`php.md`](stacks/php.md) |
| **`laravel.md`** | Laravel Framework | Service Provider registration, Eloquent model encapsulation, configuration caching isolation (`env()` rules). | [`laravel.md`](stacks/laravel.md) |

---

## 🔗 Related Documentation

- 🛠️ **[Standalone Skills Registry](/skills/README.md)**: Explore procedural skill workflows.
- 📦 **[Plugin Bundles Registry](/plugins/README.md)**: Explore 1-step plugin bundles.
- 🏠 **[Root Repository Overview](/README.md)**: Return to main repository overview.
