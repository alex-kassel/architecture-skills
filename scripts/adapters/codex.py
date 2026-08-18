import os
from pathlib import Path
from base_adapter import safe_link_or_copy

def install_codex_adapter():
    repo_root = Path(__file__).resolve().parent.parent.parent
    home_dir = Path.home()
    target_base = home_dir / ".codex"

    rules_source = repo_root / "rules"
    skills_source = repo_root / "skills"

    rules_target = target_base / "rules"
    skills_target = target_base / "skills"

    print("🚀 Installing OpenAI Codex Adapter...")

    if rules_source.exists():
        for rule_file in rules_source.glob("**/*.md"):
            rel_path = rule_file.relative_to(rules_source)
            target_file = rules_target / rel_path
            res = safe_link_or_copy(rule_file, target_file)
            print(f"  [Rule] {rel_path} -> {res}")

    if skills_source.exists():
        for skill_dir in skills_source.iterdir():
            if skill_dir.is_dir():
                target_skill = skills_target / skill_dir.name
                res = safe_link_or_copy(skill_dir, target_skill)
                print(f"  [Skill] {skill_dir.name} -> {res}")

    print("✅ OpenAI Codex Adapter installation completed successfully!")

if __name__ == "__main__":
    install_codex_adapter()
