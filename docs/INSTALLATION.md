# Installation and Multi-Agent Safety Guide

This repository contains **49 collaborative skill directories** led by `business-sage` and `cli-anything-business-sage` (`bsage`). Installing skills never modifies your Hermes `config.yaml`, LLM `provider`, `model`, or `SOUL.md`.

## Mode A — Smart Universal Auto-Discovery (Recommended for All Users)

Automatically detects Hermes Agent (#1 — across `C:`–`Z:`, Registry, env vars, WSL, and bot `profiles/*`), OpenClaw (`~/.openclaw`), Claude Code (`~/.claude`), OpenAI Codex (`~/.codex`), and Universal `~/.agents`, linking skills safely and registering the global `bsage` terminal command:

**Windows PowerShell:**
```powershell
.\install_business_sage.ps1 -DryRun        # Preview detected agent paths without writing
.\install_business_sage.ps1                # Install 2 core Business Sage skills + global `bsage` CLI
.\install.ps1 -Scope all                   # Install all 49 collaborative skills + global `bsage` CLI
```

**Linux / macOS / WSL:**
```bash
bash ./install_business_sage.sh --dry-run
bash ./install_business_sage.sh
bash ./install.sh
```

## Mode B — Explicit Single-Folder Target (With Backup Guarantee)

If you prefer targeting a single directory explicitly:

```powershell
.\install_business_sage.ps1 -TargetSkillsDir "$HOME\.hermes\skills" -Scope business -WhatIf
.\install_business_sage.ps1 -TargetSkillsDir "$HOME\.hermes\skills" -Scope business
```

```bash
bash ./install_business_sage.sh --target "$HOME/.hermes/skills" --scope business --dry-run
bash ./install_business_sage.sh --target "$HOME/.hermes/skills" --scope business
```

Any pre-existing unmanaged folder with the same name is backed up as `<skill-name>.backup-YYYYMMDD-HHMMSS`.

## Terminal Update Automation (`PowerShell` / `CMD` / `Bash`)

Once installed, check or pull updates anytime from any directory without opening a browser:

```powershell
bsage check
bsage update
```
