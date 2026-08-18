#!/usr/bin/env bash
# macOS / Linux cross-platform script for downstream release sync
set -e

echo "🚀 Syncing skills directory to alex-kassel/skills repository..."
git subtree push --prefix skills https://github.com/alex-kassel/skills.git main
echo "✅ Release sync completed successfully!"
