import os
from pathlib import Path
from base_adapter import safe_link_or_copy

def install_cursor_adapter():
    repo_root = Path(__file__).resolve().parent.parent.parent
    home_dir = Path.home()
    target_rules = home_dir / ".cursor" / "rules"

    rules_source = repo_root / "rules"

    print("🚀 Installing Cursor Adapter...")

    if rules_source.exists():
        for rule_file in rules_source.glob("**/*.md"):
            rel_path = rule_file.relative_to(rules_source)
            target_file = target_rules / rel_path
            res = safe_link_or_copy(rule_file, target_file)
            print(f"  [Rule] {rel_path} -> {res}")

    print("✅ Cursor Adapter installation completed successfully!")

if __name__ == "__main__":
    install_cursor_adapter()
