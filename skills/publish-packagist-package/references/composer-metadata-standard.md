# Composer Metadata Standard for Packagist Publishing

To ensure publication readiness on Packagist and compatibility with PHP/Laravel ecosystems, `composer.json` MUST adhere to the following metadata requirements.

---

## Required Metadata Fields

```json
{
    "name": "vendor-name/package-name",
    "description": "Concise overview of package capabilities and purpose",
    "type": "library",
    "keywords": ["laravel", "php", "package"],
    "homepage": "https://github.com/vendor-name/package-name",
    "license": "MIT",
    "authors": [
        {
            "name": "Author Name",
            "email": "author@example.com",
            "role": "Developer"
        }
    ],
    "require": {
        "php": "^8.2",
        "illuminate/support": "^10.0|^11.0"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0",
        "orchestra/testbench": "^8.0|^9.0"
    },
    "autoload": {
        "psr-4": {
            "VendorName\\PackageName\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "VendorName\\PackageName\\Tests\\": "tests/"
        }
    },
    "extra": {
        "laravel": {
            "providers": [
                "VendorName\\PackageName\\PackageServiceProvider"
            ],
            "aliases": {
                "PackageAlias": "VendorName\\PackageName\\Facades\\PackageAlias"
            }
        }
    },
    "minimum-stability": "dev",
    "prefer-stable": true
}
```

---

## Field Validation Rules

1. **`name`**:
   - Must be in `vendor/package` format using lowercase letters, numbers, hyphens.
   - Vendor name should match GitHub organizational or user account name.

2. **`description`**:
   - Non-empty, single-line explanation (under 255 characters).

3. **`license`**:
   - Must use standard SPDX license string (`MIT`, `BSD-3-Clause`, `Apache-2.0`).

4. **`autoload`**:
   - Must follow PSR-4 standard.
   - Namespace MUST end with trailing backslashes `\\`.

5. **`extra.laravel`**:
   - Required if the package targets Laravel for auto-discovery.
   - Service providers listed must exist in `src/`.

---

## Pre-Flight Validation Command

Before publishing, execute:

```bash
composer validate --strict
```

The command must exit with code `0` with zero warnings or errors.
