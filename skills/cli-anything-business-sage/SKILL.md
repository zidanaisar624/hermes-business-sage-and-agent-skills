---
name: cli-anything-business-sage
version: 2.0.0
description: Zero-MCP-token CLI-Anything compatible harness (`bsage` / `cli-anything-business-sage`) for Business Sage: financial literacy, unit economics, DCF valuation, Indonesian UMKM/tax scenarios, Bass Diffusion trend forecasting, Modal Rp0 plans, Eternal-Student new-app onboarding, 49-skill synergy, multi-agent auto-discovery, and terminal self-updates.
---
# cli-anything-business-sage (`bsage`)

Agent-native command-line harness compatible with [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) conventions (`--json` machine output + stateful interactive REPL, **0 idle MCP context tokens**) for **Hermes Agent (#1)**, **OpenClaw**, **Claude Code**, **ChatGPT / Codex**, and **Cursor**.

> **Advisory Principle**: Outputs are transparent quantitative scenario calculations to assist human decision-makers, business students, and founders—never a replacement for human judgment or licensed accounting/tax/legal professionals.

## Core Commands (`--json` for AI Agents | Human Output in Terminal)

```bash
# 1. System, Hermes (#1) & Multi-Agent Auto-Discovery Status
bsage --json status
bsage --json discover

# 2. Terminal Update Check & 1-Command Self-Update from GitHub (PowerShell / CMD / Bash)
bsage check
bsage update

# 3. 16-Unit Financial Literacy & 50/30/20 Runway Audit
bsage --json literacy-audit --monthly-after-tax-income 15000000 --monthly-needs 7000000 --monthly-wants 3500000 --monthly-savings 4500000 --liquid-emergency-cash 30000000 --high-apr-debt 0

# 4. Startup / SME Gross-Margin Unit Economics (CM, BEP, LTV, CAC, Payback)
bsage --json unit-economics --price 250000 --variable-cost 100000 --monthly-fixed-cost 15000000 --cac 150000 --monthly-churn-rate 0.05

# 5. 5-Year FCFF & Terminal Value Intrinsic DCF Valuation
bsage --json valuation-dcf --initial-fcff 500000000 --growth-rate-5yr 0.18 --terminal-growth-rate 0.04 --wacc 0.11 --cash 120000000 --debt 50000000

# 6. Indonesian UMKM Tier (PP 7/2021) & Tax Regime Scenario Comparison (PP 20/2026 vs Pasal 31E)
bsage --json indonesia-tax-legal --annual-turnover-idr 2400000000 --annual-net-profit-idr 300000000 --entity-type pt_perorangan

# 7. Quantitative Business Trend Forecast (Bass Diffusion S-Curve & Geo-Lag Arbitrage)
bsage --json predict-trend --sector "AI Automation for Indonesian UMKM" --innovation-coeff-p 0.025 --imitation-coeff-q 0.42 --current-adoption-pct 6.5

# 8. Zero-Rupiah (Modal Rp0) Negative-CCC Blueprints & Indonesian WhatsApp WARMTH Script
bsage --json zero-rupiah-plan --skill-or-network "AI Workflow & Data Analytics" --target-market "Klinik & F&B Lokal" --target-monthly-profit-idr 15000000

# 9. Eternal-Student New-App Onboarding, Empirical Research Log & 49-Skill Synergy Mesh
bsage --json onboard-app --app libreoffice
bsage --json phd-learn --topic "Negative CCC Pre-Order" --insight "Collecting 50% DP upfront eliminates working-capital debt" --category "Bootstrap-Method"
bsage --json synergy
```

## Cross-Skill Synergy & Eternal-Student Collaboration

- **Zero-MCP Execution**: Pair `cli-anything-business-sage` (`bsage`) with `cli-anything-libreoffice`, `cli-anything-mermaid`, `cli-anything-drawio`, `sqlite3`, and Python stdlib scripts so agents execute spreadsheets, diagrams, and financial audits without loading bloated MCP tool schemas.
- **Mesh Integration**: Automatically discovers and collaborates with all **49 skills** in the repository (plus any external skills installed in the user's `skills/` directory).
