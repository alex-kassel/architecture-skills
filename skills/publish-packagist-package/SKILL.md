---
name: publish-packagist-package
description: Guide standalone package publishing, Composer publication-ready metadata validation, dual Git workflow setup, and .github/workflows/packagist.yml CI scaffolding. Make sure to use this skill whenever the user asks to prepare, publish, release, or configure a PHP or Laravel package for Packagist, setup Composer package metadata, validate composer.json for publishing, configure dual Git subtree/sync workflows, or scaffold .github/workflows/packagist.yml CI integration, even if Packagist is not explicitly named.
---

# Publish Packagist Package

Guide the publishing of standalone PHP and Laravel packages to Packagist, ensuring composer metadata compliance, establishing dual Git sync workflows, and scaffolding GitHub Actions CI automation.

---

## 1. Publication Workflow Overview

Publishing a package to Packagist requires four core phases:

```text
┌─────────────────────────┐     ┌─────────────────────────┐
│  1. Composer Metadata   │ ──► │   2. Dual Git Sync      │
│     Validation          │     │      Workflow           │
└─────────────────────────┘     └─────────────────────────┘
                                             │
                                             ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│  4. Packagist Webhook & │ ◄── │  3. CI Scaffolding      │
│     Release Tagging     │     │     (packagist.yml)     │
└─────────────────────────┘     └─────────────────────────┘
```

1. **Composer Metadata Validation**: Validate `composer.json` against publication standards (license, description, keywords, autoload, PSR-4, Laravel auto-discovery). See [`references/composer-metadata-standard.md`](references/composer-metadata-standard.md).
2. **Dual Git Workflow Setup**: Configure standalone git repository or monorepo `git subtree` / split synchronization.
3. **CI Pipeline Scaffolding**: Create `.github/workflows/packagist.yml` for automated linting, testing across PHP versions, tag creation, and Packagist release validation. See [`references/templates/packagist.yml`](references/templates/packagist.yml).
4. **Packagist Registration & Webhooks**: Connect the GitHub repository to Packagist via GitHub Webhook or API tokens.

---

## 2. Step-by-Step Publishing Protocol

### Phase 1: Composer Metadata Validation

1. Run `composer validate --strict` to verify `composer.json`.
2. Ensure the required fields satisfy standard criteria:
   - **`name`**: Vendor and package name in lowercase kebab-case (e.g. `vendor-name/package-name`).
   - **`type`**: `library` or `laravel-plugin`.
   - **`license`**: Valid SPDX license identifier (e.g. `MIT`).
   - **`autoload`**: PSR-4 mapping matching the vendor namespace.
   - **`extra.laravel`**: (For Laravel packages) Auto-discovery service providers and aliases.

Consult [`references/composer-metadata-standard.md`](references/composer-metadata-standard.md) for full field rules.

---

### Phase 2: Dual Git Workflow Setup

If developing inside a monorepo or dual-repo setup:

1. **Standalone Repository**: Maintain a separate Git repository for the package.
2. **Subtree Push / Sync**: If maintaining within a parent repository, configure a subsplit or `git subtree push`:
   ```bash
   git subtree push --prefix packages/my-package git@github.com:vendor/my-package.git main
   ```
3. **Branch Alignment**: Ensure default branch is set to `main` (or `master`) and semantic versioning tags (`v1.0.0`) are pushed to the standalone repo.

---

### Phase 3: CI Pipeline Scaffolding

1. Scaffold `.github/workflows/packagist.yml` using the template provided in [`references/templates/packagist.yml`](references/templates/packagist.yml).
2. Configure the workflow to perform:
   - Code style checks via `php-cs-fixer` or `pint`.
   - Static analysis via `phpstan` or `psalm`.
   - Test suite execution via `phpunit` or `pest` across supported PHP and Laravel matrix versions.
   - Automated Packagist sync notification on tag push.

---

### Phase 4: Release Tagging & Packagist Hook

1. **Preflight Safety Gate**: Execute pre-push evaluation per [`git-release-preflight`](../git-release-preflight/SKILL.md) prior to executing any `git push` or release tag command.
2. Tag a semantic version release:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```
3. Submit repository URL on [Packagist.org](https://packagist.org/packages/submit).
4. Configure GitHub Webhook under Repository Settings -> Webhooks (or use Packagist API token in repository secrets `PACKAGIST_TOKEN` and `PACKAGIST_USERNAME`).

---

## Output Template

### Publication Readiness Audit Summary
ALWAYS use this format when auditing package readiness for Packagist:

```markdown
### Packagist Publication Audit: [package-name]
- **Composer Strict Validation**: `PASS` | `FAIL`
- **SPDX License**: [License, e.g. MIT]
- **PSR-4 Autoloading**: [Namespace mapping]
- **Laravel Auto-Discovery**: `Configured` | `N/A`
- **Dual Git Sync State**: [Standalone / Subtree details]
- **CI Workflow Status**: `.github/workflows/packagist.yml` [Scaffolded / Pending]
```
