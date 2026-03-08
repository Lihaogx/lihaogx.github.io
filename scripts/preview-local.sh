#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PREVIEW_DIR="/tmp/lihaogx-preview-copy"
PORT="${1:-4000}"

mkdir -p "$PREVIEW_DIR"

rsync -a --delete \
  --exclude .git \
  --exclude .worktrees \
  --exclude _site \
  --exclude vendor/bundle \
  "$ROOT_DIR"/ "$PREVIEW_DIR"/

cd "$PREVIEW_DIR"

if ! bundle check >/dev/null 2>&1; then
  BUNDLE_FORCE_RUBY_PLATFORM=true bundle install --path vendor/bundle
fi

bundle exec jekyll serve -H 127.0.0.1 -P "$PORT"
