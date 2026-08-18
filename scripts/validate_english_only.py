#!/usr/bin/env python3
"""
Cross-Platform English-Only Validation Script (macOS, Linux, Windows)
Scans all repository files to ensure zero non-English (Cyrillic) content exists in any tracked document.
"""

import sys
import re
import io
from pathlib import Path

# Force UTF-8 stdout encoding for Windows console compatibility
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO_ROOT = Path(__file__).resolve().parent.parent

# Regex matching Cyrillic Unicode characters
CYRILLIC_PATTERN = re.compile(r'[\u0400-\u04FF]')

# File extensions to scan
VALID_EXTENSIONS = {'.md', '.ps1', '.sh', '.yml', '.yaml', '.py'}

# Paths to skip
SKIP_PATHS = {
    Path('scripts/validate_english_only.py'),
}

def scan_repository():
    violations = []
    
    for file_path in REPO_ROOT.rglob('*'):
        if not file_path.is_file():
            continue
            
        rel_path = file_path.relative_to(REPO_ROOT)
        
        # Skip git directory and validator script
        if '.git' in rel_path.parts or rel_path in SKIP_PATHS:
            continue
            
        if file_path.suffix not in VALID_EXTENSIONS:
            continue

        try:
            content = file_path.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        lines = content.splitlines()
        for line_num, line in enumerate(lines, 1):
            if CYRILLIC_PATTERN.search(line):
                violations.append({
                    'file': str(rel_path),
                    'line': line_num,
                    'content': line.strip()
                })

    return violations

def main():
    violations = scan_repository()
    
    if violations:
        print("❌ English-Only Rule Violation Found! Non-English (Cyrillic) content detected:")
        for v in violations:
            print(f"  File: {v['file']}:{v['line']}")
            print(f"  Content: {v['content']}")
        sys.exit(1)
    else:
        print("✅ Validation Passed! All repository files are 100% written in English across macOS, Linux, and Windows.")
        sys.exit(0)

if __name__ == '__main__':
    main()
