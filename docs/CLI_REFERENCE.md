# CLI Reference (`bsage` / `cli-anything-business-sage`)

`cli-anything-business-sage` (`bsage`) is a zero-dependency Python 3.8+ CLI harness following agent-native `CLI-Anything` conventions (`--json` deterministic output + interactive REPL, **0 idle MCP context tokens**).

## Running Commands

After running `./install_business_sage.ps1` or `./install.sh`, use `bsage` (or `python skills/business-sage/scripts/cli_anything_business_sage.py`) from any terminal:

```bash
bsage --json status
bsage check
bsage update
bsage --json literacy-audit --monthly-after-tax-income 15000000 --monthly-needs 7000000 --monthly-wants 3500000 --monthly-savings 4500000 --liquid-emergency-cash 30000000 --high-apr-debt 0
bsage --json unit-economics --price 250000 --variable-cost 100000 --monthly-fixed-cost 15000000 --cac 150000 --monthly-churn-rate 0.05
bsage --json valuation-dcf --initial-fcff 500000000 --growth-rate-5yr 0.18 --terminal-growth-rate 0.04 --wacc 0.11 --cash 120000000 --debt 50000000
bsage --json indonesia-tax-legal --annual-turnover-idr 2400000000 --annual-net-profit-idr 300000000 --entity-type pt_perorangan
bsage --json predict-trend --sector "AI Workflows" --current-adoption-pct 10
bsage --json zero-rupiah-plan --skill-or-network "AI Automation" --target-market "Local SMEs" --target-monthly-profit-idr 15000000
bsage --json onboard-app --app libreoffice
bsage --json phd-learn --topic "Negative CCC Pilot" --insight "50% upfront DP funds COGS without debt"
bsage --json synergy
```

## Automated Regression Suite

```bash
python business-sage/agent-harness/cli_anything/business_sage/tests/test_core.py
python scripts/validate_repo.py
```
