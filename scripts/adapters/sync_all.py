import sys
from pathlib import Path

# Add current dir to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from antigravity import install_antigravity_adapter
from cursor import install_cursor_adapter
from claude import install_claude_adapter
from codex import install_codex_adapter

def main():
    print("==================================================")
    print("🚀 Running All AI Agent Client Adapters...")
    print("==================================================")
    
    install_antigravity_adapter()
    print()
    install_cursor_adapter()
    print()
    install_claude_adapter()
    print()
    install_codex_adapter()
    print()
    print("🎉 All AI Agent Adapters synced successfully!")

if __name__ == "__main__":
    main()
