#!/usr/bin/env bash
# macOS / Linux cross-platform script for downstream release sync of skills/ and plugins/
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "🚀 Syncing skills/ and plugins/ directories to alex-kassel/skills repository..."

TEMP_DIR=$(mktemp -d)
git clone https://github.com/alex-kassel/skills.git "$TEMP_DIR"

mkdir -p "$TEMP_DIR/skills" "$TEMP_DIR/plugins"
rsync -av --delete --exclude='.git' skills/ "$TEMP_DIR/skills/"
rsync -av --delete --exclude='.git' plugins/ "$TEMP_DIR/plugins/"

cd "$TEMP_DIR"
git add skills plugins
if git diff --staged --quiet; then
  echo "✅ No changes to sync."
else
  git commit -m "sync(release): update skills/ and plugins/ from architecture-skills maintainer repo"
  git push origin main
  echo "✅ Release sync completed successfully!"
fi

rm -rf "$TEMP_DIR"
