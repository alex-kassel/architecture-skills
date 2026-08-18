#!/usr/bin/env bash
# macOS / Linux cross-platform script for downstream release sync of skills/ and plugins/
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "🚀 Syncing skills/ and plugins/ directories to alex-kassel/skills repository..."

TEMP_DIR=$(mktemp -d)
git clone https://github.com/alex-kassel/skills.git "$TEMP_DIR"

# Clean out old top-level tracked files and directories in temp repo (except .git)
find "$TEMP_DIR" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +

# Copy fresh directories and root README
mkdir -p "$TEMP_DIR/skills" "$TEMP_DIR/plugins"
rsync -av --exclude='.git' skills/ "$TEMP_DIR/skills/"
rsync -av --exclude='.git' plugins/ "$TEMP_DIR/plugins/"
if [ -f README.md ]; then
  cp README.md "$TEMP_DIR/README.md"
fi

cd "$TEMP_DIR"
git add -A
if git diff --staged --quiet; then
  echo "✅ No changes to sync."
else
  git commit -m "sync(release): purge stale legacy folders and update skills/ and plugins/"
  git push origin main
  echo "✅ Release sync completed successfully!"
fi

rm -rf "$TEMP_DIR"
