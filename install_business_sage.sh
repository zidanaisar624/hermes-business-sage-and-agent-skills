#!/usr/bin/env bash
# ==============================================================================
# BUSINESS SAGE - UNIVERSAL AUTO-DISCOVERY & EXPLICIT INSTALLER (LINUX/MACOS/WSL)
# Supports both:
#   bash ./install_business_sage.sh                        # Smart Auto-Discovery
#   bash ./install_business_sage.sh --target "$HOME/.hermes/skills" --scope business --dry-run
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
TARGET_DIR=""
SCOPE="business"
DRY_RUN="0"
HERMES_ONLY="0"
COPY_MODE="0"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET_DIR="$2"; shift 2 ;;
    --scope) SCOPE="$2"; shift 2 ;;
    --dry-run) DRY_RUN="1"; shift ;;
    --hermes-only) HERMES_ONLY="1"; shift ;;
    --copy) COPY_MODE="1"; shift ;;
    *) shift ;;
  esac
done

PY_CMD=""
if command -v python3 >/dev/null 2>&1; then
  PY_CMD="python3"
elif command -v python >/dev/null 2>&1; then
  PY_CMD="python"
fi

if [[ -n "$PY_CMD" ]]; then
  ARGS=("$SCRIPT_DIR/install.py" "--scope" "$SCOPE" "--export-chatgpt")
  [[ -n "$TARGET_DIR" ]] && ARGS+=("--target" "$TARGET_DIR")
  [[ "$DRY_RUN" == "1" ]] && ARGS+=("--dry-run")
  [[ "$HERMES_ONLY" == "1" ]] && ARGS+=("--hermes-only")
  [[ "$COPY_MODE" == "1" ]] && ARGS+=("--copy")
  exec "$PY_CMD" "${ARGS[@]}"
fi

# Zero-Python POSIX fallback
DEST="${TARGET_DIR:-$HOME/.hermes/skills}"
STAMP="$(date +%Y%m%d-%H%M%S)"
if [[ "$SCOPE" == "all" ]]; then
  SKILL_PATHS=("$SCRIPT_DIR"/skills/*)
else
  SKILL_PATHS=("$SCRIPT_DIR/skills/business-sage" "$SCRIPT_DIR/skills/cli-anything-business-sage")
fi

for sdir in "${SKILL_PATHS[@]}"; do
  [[ -f "$sdir/SKILL.md" ]] || continue
  sname="$(basename "$sdir")"
  dst="$DEST/$sname"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo " [DRY-RUN] $sdir -> $dst"
    continue
  fi
  mkdir -p "$DEST"
  if [[ -e "$dst" ]]; then
    mv "$dst" "$DEST/${sname}.backup-${STAMP}"
  fi
  cp -R "$sdir" "$dst"
  echo " [OK] Installed $sname -> $dst"
done
