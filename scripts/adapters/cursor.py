import os
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from base_adapter import safe_link_or_copy

def install_cursor_adapter():
    repo_root = Path(__file__).resolve().parent.parent.parent
    home_dir = Path.home()
    rules_target = home_dir / ".cursor" / "rules"
    rules_source = repo_root / "rules"

    print("[+] Installing Cursor Adapter...")

    if rules_source.exists():
        res = safe_link_or_copy(rules_source, rules_target)
        print(f"  [Rules Directory] rules -> {res}")

    print("[OK] Cursor Adapter installation completed successfully!")

if __name__ == "__main__":
    install_cursor_adapter()
