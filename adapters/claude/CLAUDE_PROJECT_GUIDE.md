# Claude Code & Claude Projects Guide — Business Sage (v2.0.0)

## Option A — Claude Code CLI (Automatic via Universal Installer)
Running `./install.ps1` (Windows) or `./install.sh` (Linux/macOS/WSL) automatically detects `~/.claude` and links Business Sage skills into `~/.claude/skills` with zero MCP token bloat.

Or add via Claude Plugin Marketplace:
```text
/plugin marketplace add zidanaisar624/hermes-business-sage-and-agent-skills
/plugin install business-sage-suite@hermes-business-sage-and-agent-skills
```

## Option B — Claude Web / Desktop Projects
1. Create a new **Claude Project** named **Business Sage Co-Pilot**.
2. Upload `exports/chatgpt/02_UPLOAD_AS_CHATGPT_KNOWLEDGE_BASE.md` into Project Knowledge.
3. Paste `exports/chatgpt/01_PASTE_INTO_CHATGPT_INSTRUCTIONS.md` into Project Custom Instructions.
