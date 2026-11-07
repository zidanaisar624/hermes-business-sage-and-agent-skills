#!/usr/bin/env sh
set -eu
REPO_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
export BSAGE_REPO="$REPO_ROOT"
export PYTHONPATH="$REPO_ROOT/business-sage/agent-harness${PYTHONPATH:+:$PYTHONPATH}"

if [ "$#" -eq 0 ]; then
  set -- update
fi

if command -v python3 >/dev/null 2>&1; then
  exec python3 -m cli_anything.business_sage "$@"
elif command -v python >/dev/null 2>&1; then
  exec python -m cli_anything.business_sage "$@"
fi

git -C "$REPO_ROOT" pull --ff-only origin main
exec bash "$REPO_ROOT/install_business_sage.sh" --scope business
