#!/usr/bin/env python3
"""Universal Auto-Discovery Installer for Business Sage across Hermes (#1), OpenClaw, Claude, ChatGPT/Codex & Agents."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
HARNESS_DIR = REPO_ROOT / "business-sage" / "agent-harness"
if str(HARNESS_DIR) not in sys.path:
    sys.path.insert(0, str(HARNESS_DIR))

from cli_anything.business_sage.cli_anything_business_sage import (  # noqa: E402
    export_chatgpt_bundle,
    main as cli_main,
)


def main() -> int:
    args = list(sys.argv[1:])
    do_export_gpt = False
    if "--export-chatgpt" in args:
        args.remove("--export-chatgpt")
        do_export_gpt = True

    rc = cli_main(["--repo", str(REPO_ROOT), "install"] + args)
    if rc == 0 and do_export_gpt:
        bundle = export_chatgpt_bundle(REPO_ROOT)
        print(f" [OK] ChatGPT Custom GPT / Project Bundle -> {bundle['output_dir']}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
