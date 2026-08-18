---
description: PHP & Composer Stack Standards
always_on: true
---

# PHP & Composer Stack Standards

- **Scope**: Applied to PHP packages, libraries, and Composer-based subprojects.
- **Language**: English
- **Authority**: Stack Policy

---

## 1. PSR Compliance & Coding Standards
- Follow PSR-12 coding style guidelines across all PHP classes, interfaces, traits, and enums.
- Declare strict types (`declare(strict_types=1);`) at the top of every PHP file.

## 2. Composer Package Publication Metadata
- Maintain publication-ready `composer.json` metadata including valid `name`, `description`, `license`, `type`, `keywords`, `authors`, `autoload` (PSR-4), and `require` constraints.
- Validate `composer.json` using `composer validate --strict` prior to publishing.

## 3. Strict Type Safety & Null Handling
- Use explicit type hints for method arguments, return values, and class properties.
- Avoid loose comparison operators (`==`); use strict equality (`===`) and null coalescing (`??`).
