import os
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from base_adapter import safe_link_or_copy

def install_antigravity_adapter():
    repo_root = Path(__file__).resolve().parent.parent.parent
    home_dir = Path.home()
    target_base = home_dir / ".gemini" / "config"
    config_skills_json = target_base / "skills.json"

    # Purge legacy skills.json manifest in config if present
    if config_skills_json.exists():
        try:
            config_skills_json.unlink()
            print("[+] Purged legacy ~/.gemini/config/skills.json manifest.")
        except Exception as e:
            print(f"[!] Warning: Could not remove skills.json: {e}")

    rules_source = repo_root / "rules"
    skills_source = repo_root / "skills"

    rules_target = target_base / "rules"
    skills_target = target_base / "skills"

    print("[+] Installing Antigravity / AGY Adapter to ~/.gemini/config/...")

    if rules_source.exists():
        res = safe_link_or_copy(rules_source, rules_target)
        print(f"  [Rules Directory] rules -> {res}")

    if skills_source.exists():
        for skill_dir in skills_source.iterdir():
            if skill_dir.is_dir():
                target_skill = skills_target / skill_dir.name
                res = safe_link_or_copy(skill_dir, target_skill)
                print(f"  [Skill Directory] {skill_dir.name} -> {res}")

    print("[OK] Antigravity Adapter installation completed successfully!")

if __name__ == "__main__":
    install_antigravity_adapter()
