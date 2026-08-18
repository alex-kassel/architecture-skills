# AI Agent Plugin Bundles Registry

> Installable plugin manifests that bundle multiple related architecture skills into single-command packages.

---

## 📦 Overview

Plugin bundles allow developers and AI coding agents to install a complete set of related skills in a single step, eliminating the need to select or copy individual skills manually.

Each plugin bundle resides in its own directory under `plugins/` and contains a `plugin.json` manifest defining the bundled skills.

---

## 📚 Available Plugin Bundles

| Plugin Bundle | Version | Bundled Skills | Description | Manifest |
| --- | --- | --- | --- | --- |
| **`architecture-suite`** | `1.0.0` | `session-lifecycle`<br>`scaffold-subproject-docs`<br>`guide-architecture-design` | Complete subproject architecture suite: exclusive session lifecycle management, 5-file documentation scaffolding, and scenario-based architecture design. | [`plugin.json`](architecture-suite/plugin.json) |

---

## ⚡ How Plugins Work

A plugin manifest (`plugin.json`) specifies the list of skill dependencies required for a specific workflow:

```json
{
  "name": "architecture-suite",
  "version": "1.0.0",
  "description": "Exclusive subproject session lifecycle, 5-file scaffolding, and architecture design guide",
  "skills": [
    "session-lifecycle",
    "scaffold-subproject-docs",
    "guide-architecture-design"
  ]
}
```

When an agent or IDE loads the `architecture-suite` plugin, it automatically registers all three underlying skills into the agent's runtime environment.

---

## 🚀 Installation & Usage

### Installing via Public Distribution Repository

To install a plugin bundle into your local agent environment:

```bash
# Clone the public skills & plugins distribution repository
git clone https://github.com/alex-kassel/skills.git

# Load the target plugin manifest in your agent / IDE
# Example: plugins/architecture-suite/plugin.json
```

---

## 🔗 Related Documentation

- 🛠️ **[Standalone Skills Registry](/skills/README.md)**: Browse individual skills.
- 🏠 **[Root Repository Overview](/README.md)**: Return to main repository overview.
