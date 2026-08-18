#!/usr/bin/env python3
"""
Cross-Platform Relative Paths Validation Script (macOS, Linux, Windows)
Scans all repository files to ensure zero local absolute paths exist (only relative paths and HTTP/HTTPS URLs are allowed).
"""

import sys
import re
import io
from pathlib import Path

# Force UTF-8 stdout encoding for Windows console compatibility
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO_ROOT = Path(__file__).resolve().parent.parent

# Patterns matching local absolute paths on Windows (C:\Users, file:///C:/Users, any drive letter user path), UNC paths (\\server\share), macOS (/Users/...), Linux (/home/...)
ABSOLUTE_PATH_PATTERNS = [
    re.compile(r'file:///[A-Za-z]:/[Uu]sers', re.IGNORECASE),
    re.compile(r'file:///Users/', re.IGNORECASE),
    re.compile(r'file:///home/', re.IGNORECASE),
    re.compile(r'[A-Za-z]:\\[Uu]sers', re.IGNORECASE),
    re.compile(r'[A-Za-z]:/[Uu]sers', re.IGNORECASE),
    re.compile(r'(?<!http:)(?<!https:)\b[A-Za-z]:\\[Uu]sers\\[A-Za-z0-9_\-\\]+', re.IGNORECASE),
    re.compile(r'(?<!http:)(?<!https:)\b[A-Za-z]:/[Uu]sers/[A-Za-z0-9_\-/]+', re.IGNORECASE),
    re.compile(r'\\\\[A-Za-z0-9_.\-]+\\[A-Za-z0-9_.\-]+\\[A-Za-z0-9_.\-\\]+', re.IGNORECASE),
    re.compile(r'- Source repository:\s*`[A-Za-z]:', re.IGNORECASE),
    re.compile(r'- Source repository:\s*`/Users/', re.IGNORECASE),
    re.compile(r'- Source repository:\s*`/home/', re.IGNORECASE),
]

# Extensions to scan
VALID_EXTENSIONS = {'.md', '.ps1', '.sh', '.yml', '.yaml', '.py'}

# Files/paths to skip from validation
SKIP_PATHS = {
    Path('scripts/validate_relative_paths.py'),
    Path('scripts/validate-relative-paths.ps1'),
    Path('scripts/validate-relative-paths.sh'),
}

def scan_repository():
    violations = []
    
    for file_path in REPO_ROOT.rglob('*'):
        if not file_path.is_file():
            continue
            
        rel_path = file_path.relative_to(REPO_ROOT)
        
        # Skip git directory and validation script files themselves
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
            for pattern in ABSOLUTE_PATH_PATTERNS:
                if pattern.search(line):
                    violations.append({
                        'file': str(rel_path),
                        'line': line_num,
                        'content': line.strip()
                    })
                    break

    return violations

def main():
    violations = scan_repository()
    
    if violations:
        print("❌ Relative Path Rule Violation Found! Local absolute paths detected:")
        for v in violations:
            print(f"  File: {v['file']}:{v['line']}")
            print(f"  Content: {v['content']}")
        sys.exit(1)
    else:
        print("✅ Validation Passed! Zero local absolute paths detected in repository files across macOS, Linux, and Windows.")
        sys.exit(0)

if __name__ == '__main__':
    main()
