# Cross-Skill Synergy Mesh & Eternal-Student New-App Onboarding

Use this reference when executing **Pillar 5** of `business-sage` to collaborate across all **49 bundled skills** (plus any user-installed skills) and to dynamically learn newly connected business/analytics applications without wasting MCP context tokens.

## 1. Eternal-Student App Onboarding & Update Learning

Whenever a new software tool, spreadsheet CLI, database engine, accounting exporter, or `CLI-Anything` harness is installed or updated on the user's machine:

1. **Zero-MCP CLI Introspection First**:
   - Run `bsage --json onboard-app --app <binary-or-command>` (or `cli-anything-business-sage --json onboard-app --app <cmd>`).
   - The CLI inspects `--version` and `--help`, computes a SHA-256 capability fingerprint, compares it against `phd_business_ledger/app_capabilities_snapshot.json`, and identifies whether the app is **`newly_onboarded_app`**, **`updated_capabilities_detected`**, or **`unchanged_up_to_date`**.
2. **Sandbox Verification Before Live Financial Data**:
   - Test new CLI flags on synthetic CSV/JSON fixtures inside a scratch directory before touching real company ledgers, invoices, or tax filings.
3. **Supported Zero-Token Business Toolchain (`CLI-Anything` + Native CLIs)**:
   - `cli-anything-business-sage` / `bsage` — Unit economics, DCF valuation, Indonesian UMKM/tax scenarios, Bass Diffusion trend forecasting, Modal Rp0 blueprints.
   - `cli-anything-libreoffice` / `soffice --headless` — `.xlsx` 3-statement financial models, `.docx` SOPs/contracts, `.pptx` pitch decks, PDF exports.
   - `cli-anything-drawio` & `cli-anything-mermaid` — Org charts, value-chain maps, supply-chain & SOP flowcharts.
   - `sqlite3` / `python3 -c "import csv, json..."` — Cohort retention, RFM segmentation, inventory EOQ, and cash-flow ledger queries.

## 2. Full 49-Skill Collaborative Synergy Mesh

`business-sage` never works in isolation. Route sub-tasks across peer skills automatically:

| Business Advisory Need | Collaborating Skills in `skills/` | Combined Deliverable |
| :--- | :--- | :--- |
| **Market Sizing, Competitor Pricing & Regulatory Scan** | `firecrawl-competitive-intel`, `firecrawl-deep-research`, `deep-research`, `literature-review` | Live competitor pricing matrix + TAM/SAM/SOM + regulatory update brief |
| **Cohort Retention, Unit Economics & Econometric Proof** | `data-analysis`, `math-reasoning`, `symbolic-equation`, `notebooklm-thinking-datascience` | Verified LTV:CAC cohort curves, sensitivity tables & Monte Carlo scenarios |
| **Investor Pitch Decks, Board Tables & Financial Charts** | `slide-generation`, `table-generation`, `academic-plotting`, `match-my-writing-style` | Executive-ready deck, clean financial markdown/LaTeX tables & charts |
| **B2B Deal Prep, Red-Team Strategy & Founder Focus** | `prep-for-meetings`, `prep-for-meetings-2`, `get-more-perspectives`, `focus-my-energy`, `generate-fresh-ideas` | Multi-angle Pre-Mortem risk audit + SPIN/Voss negotiation brief |
| **Commercial Video Ads, Brand Storytelling & Product Visuals** | `filmmaking-videography-photography-s2`, `auto-curiousity-for-film-making` | High-retention product video scripts, lighting/optics specs & visual trend forecasts |

Run `bsage --json synergy` at any time to dynamically inspect all installed collaborative skills in the user's active `skills/` directory.
