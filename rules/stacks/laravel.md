# Laravel Architecture & Package Standards

- **Scope**: Applied to Laravel platform components, packages, and application subprojects.
- **Language**: English
- **Authority**: Stack Policy

---

## 1. Package Service Providers
- Register package bindings, configuration files, migrations, views, and routes inside explicit Service Providers (`ServiceProvider`).
- Defer heavy service initializations using `boot()` vs `register()` phases appropriately.

## 2. Eloquent Model Boundaries
- Encapsulate database interactions within repositories or action classes rather than bloating Eloquent models.
- Declare explicit mass assignment guards (`$fillable` or `$guarded`) on every Eloquent model.

## 3. Configuration & Environment Isolation
- Access environment variables exclusively inside configuration files (`config/*.php`).
- Never invoke the `env()` helper function outside of configuration files to preserve config caching compatibility.
