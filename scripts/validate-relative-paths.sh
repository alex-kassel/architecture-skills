#!/usr/bin/env bash
# macOS / Linux Relative Paths Validation Script
# Scans all repository files to ensure no local absolute paths exist (only relative paths and HTTP/HTTPS URLs are allowed).

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VIOLATIONS=0

cd "$REPO_ROOT"

while IFS= read -r file; do
    if [[ "$file" == "scripts/validate-relative-paths.sh" || "$file" == "scripts/validate_relative_paths.py" ]]; then
        continue
    fi
    
    if grep -E -n "file:///[A-Za-z]:/[Uu]sers|[A-Za-z]:\\[Uu]sers|[A-Za-z]:/[Uu]sers|- Source repository:\s*\`[A-Za-z]:|file:///Users/|file:///home/" "$file" > /dev/null 2>&1; then
        echo "❌ Relative Path Rule Violation Found in $file"
        grep -E -n "file:///[A-Za-z]:/[Uu]sers|[A-Za-z]:\\[Uu]sers|[A-Za-z]:/[Uu]sers|- Source repository:\s*\`[A-Za-z]:|file:///Users/|file:///home/" "$file"
        VIOLATIONS=$((VIOLATIONS + 1))
    fi
done < <(find . -type f \( -name "*.md" -o -name "*.ps1" -o -name "*.sh" -o -name "*.yml" -o -name "*.yaml" -o -name "*.py" \) -not -path "*/.git/*")

if [ $VIOLATIONS -gt 0 ]; then
    echo "❌ Total violations found: $VIOLATIONS"
    exit 1
else
    echo "✅ Validation Passed! Zero local absolute paths detected in repository files across macOS, Linux, and Windows."
    exit 0
fi
