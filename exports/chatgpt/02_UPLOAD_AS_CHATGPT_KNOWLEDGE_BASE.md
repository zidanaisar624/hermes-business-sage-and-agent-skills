# Business Sage — Consolidated Knowledge Base (S1-S2 Business, Finance & Indonesian UMKM/Tax Co-Pilot)
> Role: Internet-Researched S1-S2 Business & Financial Co-Pilot + Eternal-Student Research Loop (Respecting Business Students, Certified Practitioners & Human Entrepreneurs — NOT a replacement)



---
## Source: `skills/business-sage/SKILL.md`

---
name: business-sage
version: 2.0.0
description: Internet-researched S1 (BBA/FEB) & S2 (MBA/MM) Business, Financial Strategy & Indonesian UMKM/Tax Advisor (a humble Co-Pilot respecting business students, practitioners & entrepreneurs—NEVER a replacement) + Eternal-Student Research & Trend Forecasting Engine. Zero-MCP CLI-Anything ready for Hermes (#1), OpenClaw, ChatGPT & Claude.
---
# Business Sage — Research-Based S1–S2 Business Advisor & Eternal-Student Co-Pilot

`business-sage` is a cross-agent Business & Financial Strategy Advisor skill paired with an agent-native CLI (`bsage` / `cli-anything-business-sage`). It is compiled from publicly available internet research across **16-Unit Financial Literacy**, **S1 Business, Management & Accounting (BBA/FEB)**, **S2 Master of Business Administration (MBA/MM)**, and **Indonesian UMKM, Tax & Commercial Regulations**, combined with an **Eternal-Student empirical research loop** that studies newly connected apps, software updates, market anomalies, and emerging business trends.

## Ethical Role & Respect for Business Students, Practitioners & Entrepreneurs

- **Advisor & Co-Pilot — NEVER a Replacement**: Literature notes and deterministic formulas inside an AI **never equal and never replace** the real-world rigor of business school students (*anak kuliah bisnis / FEB / Manajemen / Akuntansi / MBA / MM*) dissecting live case studies, interviewing customers on the street, interning in operations, or leading teams—nor the lived intuition of human founders managing real cash-flow pressure.
- **Professional Verification Boundary**: Outputs are quantitative scenario models and research starting points, **not** licensed audit opinions, official tax filings, investment solicitation, or legal counsel. Always recommend consulting certified Indonesian/international professionals (*Akuntan Publik / CPA*, *Konsultan Pajak Resmi USKP*, *CFP*, *Notaris / Konsultan Hukum*, and official DJP/OSS/OJK sources) before binding financial or legal commitments.

## When to Use

- Diagnosing personal or founder financial health (`50/30/20` after-tax budgeting, `3-6 month` emergency runway, debt avalanche vs snowball, SLIK OJK/credit utilization, inflation-adjusted returns, or rent-vs-buy modeling).
- Modeling S1–S2 business & corporate finance scenarios: 3-statement financial links, `FCFF` / `WACC` / `Intrinsic DCF` valuation, startup & SME unit economics (`Contribution Margin`, `BEP`, `Gross-Margin LTV`, `CAC`, `Payback`, `CCC`), competitive strategy (`Porter's 5 Forces`, `VRIO`, `Blue Ocean ERRC`), and operations (`Little's Law`, `EOQ`).
- Structuring Indonesian business & regulatory research: UMKM classification (`PP No. 7 Tahun 2021`), tax regime scenario comparison (`PP No. 20 Tahun 2026` 0.5% PPh Final vs `Pasal 31E` PPh Badan), `PT Perorangan` vs `CV`/`PT Biasa`, `OSS-RBA` (`NIB` & KBLI), `SAK IAI` (`SAK EMKM`, `SAK EP`, `PSAK`, `SAK Syariah`), `QRIS`/`BI-FAST`, `BPJPH Halal`, `DSN-MUI` Sharia contracts, and `PP 35/2021` PKWT compensation reserves.
- Forecasting emerging business waves (`Bass Diffusion S-Curve` + `Cross-Geography Time-Lag Arbitrage`), scanning `6 Profit-Gap` inefficiencies (`Celah Untung`), or designing customer-funded **Modal Rp0 (`Negative CCC < 0`)** bootstrap blueprints.
- Crafting consultative customer discovery (`The Mom Test`, `JTBD`), objection handling (`SPIN Selling`, `Chris Voss Tactical Empathy`), and polite Indonesian WhatsApp closing scripts (`5-Step WARMTH Flow`).
- Collaborating across all **49 skills** and onboarding newly installed CLI/business apps via zero-MCP-token commands (`bsage --json ...`).

## Core Architecture: The 5 Advisory Pillars

### Pillar 1: Financial Literacy to S1–S2 Business & Valuation Scenarios
Ground every recommendation in transparent assumptions and math (`references/s1-s2-mba-global-and-financial-literacy.md`):

1. **Founder & Personal Financial Gate (16-Unit Foundation)**:
   - Audit net after-tax cash flow via the **50/30/20 rule**, verify a **3–6 month liquid emergency runway**, strictly separate personal and company bank accounts, and clear high-APR revolving bad debt before deploying risk capital.
   - Track Net Worth ($\text{Assets} - \text{Liabilities}$), real inflation-adjusted return ($r_{\text{real}} = \frac{1 + r_{\text{nominal}}}{1 + \pi} - 1$), and opportunity cost on capital allocation.
2. **Corporate Finance, DCF Valuation & Unit Economics**:
   - Compute **FCFF**, **WACC**, and **Intrinsic DCF Value**; check value creation via $\text{ROIC} > \text{WACC}$.
   - Compute unit economics strictly on **Gross / Contribution Margin** (never raw top-line revenue): $\text{LTV} = \frac{\text{ARPA} \times \text{Gross Margin}}{\text{Churn}}$, $\text{CAC} = \frac{\text{Sales \& Marketing Spend}}{\text{New Paying Customers}}$, targeting $\text{LTV:CAC} \ge 3:1$ and $\text{CAC Payback} \le 12\text{ months}$.
   - Monitor working capital via the **Cash Conversion Cycle**: $\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$.

### Pillar 2: Indonesian Economic, Tax, Legal & Sharia Context
Contextualize analysis for Indonesian market realities (`references/indonesia-economic-tax-legal-system.md`):

1. **UMKM Classification (`PP No. 7 Tahun 2021`)**:
   - **Mikro** (Capital $\le \text{Rp1B}$ or Sales $\le \text{Rp2B}$), **Kecil** ($\text{Rp1B–Rp5B}$ or Sales $\text{Rp2B–Rp15B}$), **Menengah** ($\text{Rp5B–Rp10B}$ or Sales $\text{Rp15B–Rp50B}$).
2. **Tax Regime Scenario Modeling (`PP No. 20 Tahun 2026`, `PP 55/2022` & `Pasal 31E UU PPh`)**:
   - **WP Orang Pribadi (Individual UMKM)**: First **Rp500M/year** gross turnover at **0%**, and **0.5% PPh Final** from Rp500M to Rp4.8B/year (subject to spouse + PT Perorangan aggregation rules).
   - **PT Perorangan (Single-Member UMK LLC)**: **0.5% PPh Final** up to Rp4.8B/year with limited liability separation.
   - **Koperasi**: **0.5% PPh Final** within statutory eligibility windows (up to 4 tax years).
   - **Newly Registered CV, Firma & Multi-Founder PT**: Modeled under **22% PPh Badan** with **Pasal 31E** 50% discount (**11% effective on net fiscal profit** up to Rp4.8B revenue; Rp0 PPh Badan when at a fiscal loss).
3. **Licensing, Accounting, Payment & Labor**:
   - Map KBLI to **OSS-RBA** risk tiers (`NIB` / `Sertifikat Standar` / `Izin`), **BPJPH Halal** (`SEHATI` for eligible UMK), **SAK IAI** tiers, **QRIS / BI-FAST** MDR impact, **DSN-MUI Sharia contracts**, and **PP 35/2021** PKWT compensation ($\frac{\text{Months Worked}}{12} \times 1\text{ Month Wage}$).

### Pillar 3: Trend Prediction, Profit-Gap Discovery & Modal Rp0 Blueprints
Spot structural demand shifts and capital-efficient entry points (`references/trend-prediction-profit-gaps-and-zero-rupiah.md`):

1. **4-Signal Business Trend Forecasting**:
   - Combine **Bass Diffusion S-Curve** ($t^* = \frac{\ln(q/p)}{p+q}$, targeting the `2.5%–16%` early-adopter inflection window), **Cross-Geography Time-Lag Arbitrage** (6–18 month US/China/Japan to Indonesia/SEA adaptation), **Regulatory Catalyst Waves**, and **Picks-and-Shovels Derivative Mapping**.
2. **6 Profit-Gap Scanners & Zero-Rupiah (`Modal Rp0`) Bootstrap Engine**:
   - Build around **Negative Cash Conversion Cycle ($\text{CCC} < 0$)** where customer down payments or pre-orders fund COGS upfront without high-interest debt.

### Pillar 4: Customer Discovery, Behavioral Psychology & Consultative Closing
Support human relationship-building with ethical persuasion (`references/customer-psychology-sales-and-phd-loop.md`):

- Apply **The Mom Test** & **Jobs-to-be-Done (4 Switching Forces)** for honest customer interviews.
- Apply **SPIN Selling**, **Chris Voss Tactical Empathy**, and the Indonesian **5-Step WARMTH WhatsApp Closing Flow** (*sopan, solutif, transparan, dan membangun kepercayaan jangka panjang*).

### Pillar 5: Eternal-Student Learning Loop, Zero-MCP CLI & 49-Skill Synergy
Operate as a lifelong student of business and tooling (`references/cross-skill-synergy-and-new-app-onboarding.md`):

1. **Zero-MCP Deterministic CLI (`bsage` / `cli-anything-business-sage`)**:
   - Run `bsage --json <subcommand>` instead of loading token-heavy MCP schemas whenever deterministic financial math, trend forecasts, app introspection, or skill updates are needed.
2. **Continuous Learning & New-App Onboarding (`phd_business_ledger/`)**:
   - Run `bsage --json onboard-app --app <cmd>` whenever a new CLI/spreadsheet/database/accounting tool is connected or updated, and `bsage --json phd-learn` to log empirical hypotheses and post-mortems.
3. **Full 49-Skill Collaboration**:
   - Pair seamlessly with `firecrawl-competitive-intel`, `data-analysis`, `math-reasoning`, `table-generation`, `slide-generation`, `academic-plotting`, `prep-for-meetings`, `get-more-perspectives`, `filmmaking-videography-photography-s2`, and all peer skills (`bsage --json synergy`).

## Bundled Reference Modules

- `references/s1-s2-mba-global-and-financial-literacy.md`
- `references/indonesia-economic-tax-legal-system.md`
- `references/trend-prediction-profit-gaps-and-zero-rupiah.md`
- `references/customer-psychology-sales-and-phd-loop.md`
- `references/cross-skill-synergy-and-new-app-onboarding.md`

## Gotchas

- **Never compute LTV or payback on gross revenue**: Always deduct COGS, payment MDR (`QRIS`), packaging, and variable fulfillment first.
- **Never present tax/legal scenario outputs as final legal advice**: Regulations evolve; remind the user to verify against current DJP/JDIH/OSS rules and licensed advisors.
- **Never recommend high-APR debt for unvalidated ideas**: Validate demand via customer-funded pilots ($\text{CCC} < 0$) first.


---
## Source: `skills/business-sage/references/s1-s2-mba-global-and-financial-literacy.md`

# S1 (BBA/FEB) to S2 (MBA/MM) Business Research & Financial Literacy Reference

> **Respect for Business Students & Practitioners**: This reference is synthesized from publicly accessible internet syllabi, open lectures, and foundational business literature across Financial Literacy, S1 Business/Management/Accounting (BBA/FEB), and S2 MBA/MM programs. It acts strictly as an **advisory & scenario-modeling Co-Pilot**—never a claim of academic degree equivalence, nor a replacement for business students, experienced founders, certified Public Accountants (CPA/Akuntan Publik), licensed Tax Consultants (USKP), or Financial Planners (CFP).

Use this reference when executing **Pillar 1** of `business-sage`. It synthesizes open concepts from the 16-Unit Financial Literacy curriculum (Khan Academy / OJK SNLKI) alongside public corporate finance and strategy frameworks taught across global and Indonesian business schools (such as HBS, Wharton, Stanford GSB, MIT Sloan, INSEAD, Prof. Aswath Damodaran's open valuation materials, SBM ITB, MM FEB UI, and MBA FEB UGM).

## 1. Foundational Financial Literacy (16-Unit Personal & Founder Finance Audit)

Before scaling a company, audit the founder's or household's financial baseline:

1. **After-Tax Budgeting & The 50/30/20 Rule**:
   - Always calculate budgets from **Net After-Tax Income**:
     - **50% Needs**: Housing, basic groceries, utilities, minimum debt payments, essential transport, basic insurance.
     - **30% Wants**: Dining out, entertainment, discretionary upgrades.
     - **20% Savings & Investments**: Emergency fund first, then high-APR debt elimination, then long-term compounding assets.
   - **Per-Unit Pricing Audit**: Evaluate every recurring purchase by cost per unit or cost per usage cycle ($\text{Cost per Cycle} = \frac{\text{Total Price}}{\text{Total Uses}}$). In business, this directly translates into **Activity-Based Costing (ABC)** and **Unit COGS**.

2. **Emergency Fund, Net Worth & SMART Financial Goals**:
   - **Emergency Runway**: Maintain **3 to 6 months of essential living/operating expenses** in liquid, low-risk accounts (high-yield savings, money market, or LPS-insured bank accounts in Indonesia) before locking capital into illiquid ventures.
   - **Net Worth Formula**: $\text{Net Worth} = \sum \text{Assets} - \sum \text{Liabilities}$.
   - **Time-Horizon Allocation**:
     - *Short-Term (<1 year)*: Cash / Money Market (preserve principal).
     - *Medium-Term (1-5 years)*: Fixed-term deposits / CDs / Government Bonds (SBN/ORI/Sukuk Ritel).
     - *Long-Term (>5 years)*: Diversified Low-Cost Index Funds (e.g., S&P 500 historical ~10% nominal / ~6-7% real return), productive business equity, or cash-flowing real estate.

3. **Credit Mechanics, Loans, Debt & Schumer Box Audit**:
   - **5 Credit Score Factors (FICO 300-850 / SLIK OJK Equivalent)**:
     1. *Payment History (35%)*: Never miss a due date.
     2. *Credit Utilization (30%)*: $\frac{\text{Current Balance}}{\text{Total Credit Limit}}$ (keep below 10-30%).
     3. *Length of Credit History (15%)*.
     4. *Credit Mix (10%)*: Revolving vs Installment.
     5. *New Credit / Hard Inquiries (10%)*: Avoid multiple hard pulls in a short window.
   - **Good Debt vs Bad Debt**:
     - *Good Debt*: Borrowed capital that acquires an asset or cashflow stream whose **After-Tax ROIC exceeds the loan's APR** ($\text{ROIC}_{\text{after-tax}} > \text{APR}$).
     - *Bad Debt*: High-APR revolving credit card debt (`20%-28.99%+ APR`) or payday/illegal online loans (`300%-800% APR`) used to fund depreciating consumption.
   - **Debt Payoff Algorithms**:
     - *Avalanche (High-Rate Approach)*: Pay minimums on all debts, direct 100% of surplus cash to the debt with the **highest APR** (mathematically minimizes total interest paid).
     - *Snowball Method*: Direct surplus cash to the **smallest balance first** (maximizes psychological momentum and behavioral adherence).

4. **Compound Interest, Inflation & Rent-vs-Buy Quantitative Model**:
   - **Compound Growth**: $FV = PV \times \left(1 + \frac{r}{m}\right)^{m \cdot t} + PMT \times \frac{\left(1 + \frac{r}{m}\right)^{m \cdot t} - 1}{r / m}$. Starting 10 years earlier with half the monthly contribution outperforms starting late with double the contribution.
   - **Real Purchasing Power Return**: $r_{\text{real}} = \frac{1 + r_{\text{nominal}}}{1 + \pi_{\text{inflation}}} - 1 \approx r_{\text{nominal}} - \pi_{\text{inflation}}$.
   - **Rent vs Buy Decision Equation**:
     $$\text{Annual Cost of Buying} = (\text{Mortgage Interest} - \text{Tax Deduction Benefit}) + \text{Property Tax} + \text{Maintenance} + (\text{Down Payment} \times r_{\text{opportunity}})$$
     Compare against $\text{Annual Rent}$. For early-stage businesses, leasing equipment/space preserves working capital for high-ROIC inventory turnover.

## 2. S1-S2 MBA Financial Accounting & Control (FRC)

1. **The 3 Linked Financial Statements**:
   - **Income Statement (Laporan Laba Rugi)**: $\text{Revenue} - \text{COGS} = \text{Gross Profit}$; $\text{Gross Profit} - \text{OpEx} = \text{EBITDA}$; $\text{EBITDA} - \text{D\&A} = \text{EBIT (Operating Income)}$; $\text{EBIT} - \text{Interest} - \text{Taxes} = \text{Net Income}$.
   - **Balance Sheet (Neraca)**: $\text{Assets} = \text{Liabilities} + \text{Shareholders' Equity}$ (must balance to 0.00).
   - **Cash Flow Statement (Arus Kas)**: $\Delta \text{Cash} = \text{CFO (Operating)} + \text{CFI (Investing)} + \text{CFF (Financing)}$. Profit is accounting opinion; cash flow is fact.

2. **Working Capital & Cash Conversion Cycle (CCC)**:
   $$\text{DIO} = \frac{\text{Inventory}}{\text{COGS}} \times 365, \quad \text{DSO} = \frac{\text{Accounts Receivable}}{\text{Total Credit Sales}} \times 365, \quad \text{DPO} = \frac{\text{Accounts Payable}}{\text{COGS}} \times 365$$
   $$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$$
   - **Negative CCC ($\text{CCC} < 0$)**: The holy grail of bootstrapping. Customers pay upfront ($\text{DSO} \approx 0$), inventory turns fast ($\text{DIO}$ low), and suppliers grant credit terms ($\text{DPO}$ high), meaning growth generates cash rather than consuming it.

## 3. Corporate Finance & Intrinsic Valuation (Damodaran / Wharton / HBS)

1. **Free Cash Flow to the Firm (FCFF) & Equity (FCFE)**:
   $$\text{FCFF} = \text{EBIT}(1 - t) + \text{D\&A} - \text{CapEx} - \Delta \text{Non-Cash Working Capital}$$
   $$\text{FCFE} = \text{Net Income} + \text{D\&A} - \text{CapEx} - \Delta \text{Non-Cash WC} + (\text{New Debt Issued} - \text{Debt Repaid})$$

2. **Cost of Capital (WACC & CAPM with Country Risk)**:
   $$R_e = R_f + \beta \times (\text{ERP}_{\text{mature}} + \text{CRP}_{\text{country}})$$
   $$\text{WACC} = \left(\frac{E}{E + D}\right) R_e + \left(\frac{D}{E + D}\right) R_d (1 - t)$$

3. **Intrinsic DCF Valuation & Terminal Value**:
   $$\text{Terminal Value (TV)}_n = \frac{\text{FCFF}_n \times (1 + g)}{\text{WACC} - g} \quad (\text{where } g \le \text{nominal GDP growth})$$
   $$\text{Enterprise Value (EV)} = \sum_{t=1}^{n} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{TV}_n}{(1 + \text{WACC})^n}$$
   $$\text{Equity Value} = \text{Enterprise Value} + \text{Cash} - \text{Total Debt}$$

4. **Economic Value Creation (ROIC vs WACC)**:
   $$\text{ROIC} = \frac{\text{NOPAT}}{\text{Invested Capital}} = \frac{\text{EBIT}(1 - t)}{\text{Total Debt} + \text{Total Equity} - \text{Non-Operating Cash}}$$
   - If $\text{ROIC} > \text{WACC}$, growth creates value. If $\text{ROIC} < \text{WACC}$, rapid growth destroys value faster.

## 4. Startup, SaaS & Retail Unit Economics

Always compute unit economics on **Gross Margin** (after COGS, payment fees, packaging, and variable fulfillment):

| Metric | Exact Mathematical Formula | Healthy Benchmark (MBA / VC Standard) |
| :--- | :--- | :--- |
| **Contribution Margin (CM)** | $\text{Price} - \text{Variable Cost per Unit}$ | $>50\%$ for Services/D2C; $>70\%$ for Software/Digital |
| **Break-Even Volume ($Q_{\text{BEP}}$)** | $\frac{\text{Total Monthly Fixed Costs}}{\text{Contribution Margin per Unit}}$ | Reachable within $<6$ months of launch |
| **Customer Acquisition Cost (CAC)** | $\frac{\text{Total Sales \& Marketing Spend}}{\text{New Paying Customers Acquired}}$ | Track Blended CAC (including organic) & Paid CAC separately |
| **Gross-Margin LTV** | $\frac{\text{ARPA} \times \text{Gross Margin \%}}{\text{Monthly Churn Rate}}$ | For non-subscription: $\text{AOV} \times \text{Gross Margin \%} \times \text{Purchase Freq} \times \text{Lifespan}$ |
| **LTV:CAC Ratio** | $\frac{\text{Gross-Margin LTV}}{\text{CAC}}$ | $\ge 3.0\times$ ($\ge 4.0\times$ is strong; $<1.5\times$ is burning capital) |
| **CAC Payback Period** | $\frac{\text{CAC}}{\text{Monthly ARPA} \times \text{Gross Margin \%}}$ | $<12\text{ months}$ for SMB/Consumer; $<6\text{ months}$ for bootstrapped businesses |
| **Net Burn & Runway** | $\text{Runway (Months)} = \frac{\text{Cash Balance}}{\text{Monthly Cash Out} - \text{Monthly Cash In}}$ | Maintain $\ge 18\text{ months}$ runway or reach Default Alive ($\text{Net Burn} \le 0$) |

## 5. Strategic Management, Operations & Decision Science

- **Porter's 5 Forces**: Supplier Power, Buyer Power, Threat of Substitutes, Threat of New Entrants, and Competitive Rivalry (determines industry structural ROIC ceiling).
- **VRIO Moat Audit**: Is the resource *Valuable, Rare, Inimitable,* and *Organized to capture value*?
- **Blue Ocean ERRC Grid**: *Eliminate, Reduce, Raise, Create* to break the value-cost trade-off.
- **Little's Law (Operations)**: $L = \lambda \times W$ (*Average Inventory / WIP = Throughput Rate $\times$ Flow Time*). To cut customer wait time $W$ without slowing throughput $\lambda$, reduce work-in-progress $L$.
- **Economic Order Quantity (EOQ)**: $Q^* = \sqrt{\frac{2 \cdot D \cdot S}{H}}$ (where $D$ = annual demand, $S$ = order setup cost, $H$ = annual holding cost per unit).


---
## Source: `skills/business-sage/references/indonesia-economic-tax-legal-system.md`

# Indonesian Economic, Tax, Legal, Accounting & Sharia Business System Reference

Use this reference when executing **Pillar 2** of `business-sage` for businesses operating in or expanding into Indonesia (synthesizing SBM ITB, MM FEB UI, and MBA FEB UGM frameworks with current Indonesian laws).

## 1. Macroeconomic Structure & Sistem Ekonomi Pancasila

- **Pasal 33 UUD 1945 Tri-Pillar Architecture**: Indonesia operates a mixed constitutional economy (*Sistem Ekonomi Pancasila*) anchored by three distinct actors:
  1. **BUMN / BUMD & Danantara**: State-owned enterprises controlling strategic sectors (energy, infrastructure, state banking: Mandiri, BRI, BNI, BTN, BSI).
  2. **Koperasi**: Member-owned cooperative enterprises operating on family/mutual-aid principles (*asas kekeluargaan*).
  3. **Swasta & UMKM**: Private corporations and Micro, Small, and Medium Enterprises, where **UMKM accounts for ~61% of Indonesia's GDP and ~97% of national employment**.
- **Regional Purchasing Power & Tiered Market Strategy**:
  - *Tier 1 (Jabodetabek, Surabaya, Bandung, Medan, Bali, Makassar)*: High digital penetration, higher AOV, intense CAC competition.
  - *Tier 2 & Tier 3 Cities / Kabupaten*: Lower CAC, strong community/word-of-mouth trust dynamics, high sensitivity to unit pack size (*ekonomi sachet / kemasan terjangkau*), and COD / QRIS payment preference.

## 2. Official UMKM Classification (`PP Nomor 7 Tahun 2021`)

Under **Pasal 35 PP No. 7 Tahun 2021** (implementing UU Cipta Kerja), Indonesian enterprises are classified by **Modal Usaha** (business capital excluding land and buildings) at registration, or by **Hasil Penjualan Tahunan** (annual sales turnover):

| Scale Tier | Capital Criterion (Excl. Land & Building) | Annual Sales Turnover Criterion | Recommended Accounting Standard (IAI) |
| :--- | :--- | :--- | :--- |
| **Usaha Mikro** | $\le \text{Rp1,000,000,000}$ ($\le \text{Rp1 Miliar}$) | $\le \text{Rp2,000,000,000}$ ($\le \text{Rp2 Miliar}$) | **SAK EMKM** (Simplified Balance Sheet + P&L) |
| **Usaha Kecil** | $>\text{Rp1 Miliar}$ to $\le \text{Rp5 Miliar}$ | $>\text{Rp2 Miliar}$ to $\le \text{Rp15 Miliar}$ | **SAK EMKM** or **SAK Entitas Privat (SAK EP)** |
| **Usaha Menengah** | $>\text{Rp5 Miliar}$ to $\le \text{Rp10 Miliar}$ | $>\text{Rp15 Miliar}$ to $\le \text{Rp50 Miliar}$ | **SAK Entitas Privat (SAK EP)** |
| **Usaha Besar** | $>\text{Rp10 Miliar}$ | $>\text{Rp50 Miliar}$ | **SAK Indonesia (PSAK / IFRS Convergence)** |

## 3. Indonesian Corporate & UMKM Taxation (`PP No. 20 Tahun 2026`, `PP 55/2022` & `Pasal 31E`)

Apply the updated Indonesian tax rules verified under **Peraturan Pemerintah Nomor 20 Tahun 2026** (effective 22 April 2026, amending PP 55/2022) and the **Coretax DJP** system:

| Taxpayer Entity Type | Gross Turnover $\le \text{Rp500 Juta/Year}$ | Gross Turnover $>\text{Rp500 Juta}$ to $\le \text{Rp4.8 Miliar/Year}$ | Gross Turnover $>\text{Rp4.8 Miliar}$ to $\le \text{Rp50 Miliar/Year}$ |
| :--- | :--- | :--- | :--- |
| **WP Orang Pribadi (Individual Entrepreneur)** | **0% (Tax-Free / Bebas PPh)** on the first Rp500M cumulative annual turnover (`Pasal 60 ayat (2) PP 55/2022`). | **0.5% PPh Final** on turnover exceeding Rp500M. Under **`PP 20/2026`**, this 0.5% rate applies **indefinitely (selamanya)** with no time limit! | Normal progressive PPh OP brackets (`5%, 15%, 25%, 30%, 35%`) on net taxable income (or NPPN if eligible). |
| **PT Perorangan (Single-Founder UMK LLC)** | **0.5% PPh Final** on gross monthly turnover. | **0.5% PPh Final** on gross turnover. Under **`PP 20/2026`**, PT Perorangan can use the 0.5% rate **indefinitely (selamanya)** while turnover $\le \text{Rp4.8B}$! | Transitions to standard PT corporate tax (**22% PPh Badan** with **Pasal 31E** discount). |
| **Koperasi (Cooperative)** | **0.5% PPh Final** (max 4 years from registration). | **0.5% PPh Final** (max 4 years from registration). | Standard Corporate Tax (**22% PPh Badan** / **Pasal 31E**). |
| **Newly Registered CV, Firma, or Standard PT (Multi-Founder)** | **No longer eligible for 0.5% PPh Final under `PP 20/2026`!** Uses **Pasal 31E PPh Badan**: **11% effective rate on Net Fiscal Profit** (Rp0 tax if operating at a loss). | **Pasal 31E PPh Badan**: **11% effective rate on Net Fiscal Profit** ($50\% \times 22\%$ on net taxable income). | Proportional **Pasal 31E** discount on the first Rp4.8B slice of revenue, and **22% PPh Badan** on the remainder. |

- **Anti-Splitting Aggregation Rule (`PP 20/2026`)**: The Rp4.8 Billion cap aggregates the combined gross turnover of husband, wife, and all `PT Perorangan` entities established by either spouse.
- **VAT / PPN & PKP Threshold**: Businesses exceeding **Rp4.8 Billion/year** in gross sales must register as **PKP (Pengusaha Kena Pajak)** and collect PPN (standard 11% effective formula / 12% luxury tier under `PMK 131/2024`).

## 4. Legal Entity Selection, `OSS-RBA` Licensing & Mandatory Halal (`BPJPH`)

1. **Choosing the Optimal Indonesian Legal Entity**:
   - **Solo Founder / Bootstrap UMK ($\text{Sales} \le \text{Rp4.8B}$)**: Choose **PT Perorangan**. It separates personal assets from business liabilities, requires only 1 founder (KTP + NPWP), registers online via AHU without expensive notary deeds, and locks in the **0.5% PPh Final** tax rate indefinitely under `PP 20/2026`.
   - **Multi-Founder SME / Bootstrapped Partnership**: Choose **PT Biasa (Perseroan Terbatas)** rather than CV if personal asset protection or future investor equity issuance is desired (remembering that in a CV, the *Sekutu Aktif/Komplementer* has unlimited personal liability). Under `PP 20/2026`, a new PT/CV with thin margins (<4.5% net profit margin) actually pays *less* tax under `Pasal 31E` (11% of net profit) than 0.5% of gross revenue!

2. **OSS-RBA (`oss.go.id`) Risk-Based Licensing**:
   - Match the business activity to the exact 5-digit **KBLI 2020** code:
     - *Risiko Rendah*: **NIB (Nomor Induk Berusaha)** alone is full legal authorization to operate.
     - *Risiko Menengah Rendah*: **NIB + Sertifikat Standar** (self-declared online).
     - *Risiko Menengah Tinggi*: **NIB + Sertifikat Standar** (verified by ministry/region).
     - *Risiko Tinggi*: **NIB + Izin** (+ BPOM / AMDAL / sectoral permit).

3. **Mandatory Halal Certification (`BPJPH`)**:
   - Food, beverage, slaughtered products, cosmetics, and consumer goods sold in Indonesia require **BPJPH Halal Certification**. Micro and Small businesses (`UMK`) with low-risk ingredients qualify for the free **SEHATI Self-Declare** pathway.

## 5. Digital Payments (`QRIS` & `BI-FAST`), Sharia Economy (`DSN-MUI`), & Labor Law (`PP 35/2021`)

- **QRIS & BI-FAST Cashflow Optimization**:
  - Integrate **QRIS** for retail acceptance (note that Merchant Discount Rate / MDR is borne by the merchant per Bank Indonesia regulations and must be factored into unit contribution margin) and **BI-FAST** (Rp2,500 transfer cap) for B2B supplier settlements.
- **Islamic / Sharia Business Contracts (`DSN-MUI` & `PSAK Syariah`)**:
  - *Murabahah*: Cost-plus sale where cost and profit margin are transparently disclosed upfront.
  - *Mudharabah*: 100% capital from *Shahibul Maal* + management by *Mudharib*; profit shared by pre-agreed nisbah, financial loss borne by capital provider unless caused by misconduct.
  - *Musyarakah*: Joint capital partnership with profit shared by nisbah and loss shared strictly proportional to capital contribution.
  - *Ijarah / IMBT*: Operating or lease-to-own asset financing.
- **Indonesian Labor Cost Modeling (`UU Cipta Kerja` & `PP No. 35 Tahun 2021`)**:
  - Always budget total employee cost at **1.22x to 1.30x base monthly wage** to account for:
    1. **THR Keagamaan**: 1 month salary per year (pro-rated after 1 month of service).
    2. **Uang Kompensasi PKWT (`Pasal 15-16 PP 35/2021`)**: Mandatory 1 month salary per 12 months worked (pro-rated via $\frac{\text{Months}}{12} \times \text{Monthly Wage}$) payable whenever a fixed-term contract (`PKWT`) expires!
    3. **BPJS Ketenagakerjaan & Kesehatan**: Employer contributions for JKK, JKM, JHT (3.7%), JP (2%), and BPJS Kesehatan (4%).


---
## Source: `skills/business-sage/references/trend-prediction-profit-gaps-and-zero-rupiah.md`

# Business Trend Prediction, Profit-Gap Arbitrage & Zero-Rupiah (`Modal Rp0`) Engine

Use this reference when executing **Pillar 3** of `business-sage` to forecast business trends, identify high-margin market gaps (`Celah Untung`), and build businesses starting from **Rp0 capital**.

## 1. Quantitative & Structural Business Trend Prediction Engine

Do not guess trends from hype headlines. Predict durable business waves using this 4-Signal Ph.D. Forecasting Model:

### Signal 1: Bass Diffusion S-Curve Velocity ($p$ vs $q$ Inflection Detection)
Model market adoption of any new product, service, or habit using the **Bass Diffusion Equation**:
$$\frac{f(t)}{1 - F(t)} = p + q \cdot F(t)$$
- $p$ = **Coefficient of Innovation** (early adopters driven by external awareness, typically $0.01 - 0.03$).
- $q$ = **Coefficient of Imitation** (word-of-mouth/network contagion, typically $0.30 - 0.50$).
- $F(t)$ = Cumulative fraction of adopters at time $t$.
- **The Golden Entry Window**: Enter when $F(t)$ crosses **2.5% to 16%** (where word-of-mouth imitation $q \cdot F(t)$ overtakes paid awareness $p$, causing CAC to drop while organic demand accelerates exponentially). Peak adoption rate occurs at $t^* = \frac{\ln(q/p)}{p+q}$.

### Signal 2: Cross-Geography Time-Lag Arbitrage (6 to 18 Month Window)
Consumer and B2B business models rarely invent simultaneously worldwide; they propagate along predictable geographic corridors:
- **Corridor A (China -> Indonesia/SEA E-Commerce & Social Commerce)**: Live-shopping formats, group-buying, factory-to-consumer micro-brands, and short-drama/affiliate funnels typically mature in China **9 to 18 months** before peaking in Indonesia (TikTok Shop, Shopee Live, WhatsApp communities).
- **Corridor B (US/Europe -> Global/Indonesian B2B SaaS & AI Workflows)**: Vertical AI agents, automated bookkeeping/tax compliance, and fractional B2B productized services mature in the US **6 to 15 months** before local Indonesian SMEs adopt localized versions.

### Signal 3: Regulatory & Infrastructure Catalyst Waves
Whenever a government or central bank mandates a change, a captive B2B/B2C market is born overnight:
- *Examples in Indonesia*: Mandatory `BPJPH Halal` certification deadlines, `Coretax DJP` & `PP 20/2026` PT Perorangan transitions, `QRIS Antarnegara` (Cross-Border ASEAN tourism spending), and green/carbon reporting for industrial supply chains.

### Signal 4: Picks-and-Shovels Derivative Mapping
When a consumer trend gets crowded (e.g., 10,000 new coffee shops or skincare brands), do not launch the 10,001st brand. Sell the **Picks and Shovels** (packaging customization, BPOM/Halal registration concierge, B2B ingredient sourcing, or retention CRM automation).

## 2. The 6 Profit-Gap Scanners (`Matriks Pencari Celah Untung`)

Scan any industry through these 6 lenses to uncover immediate profit margins:

| Profit-Gap Type | Diagnostic Question | How to Capture the Margin |
| :--- | :--- | :--- |
| **1. Information & Price Opacity Gap** | Where do buyers overpay by 30-300% simply because supplier pricing is hidden or offline? | Build a transparent catalog/aggregator and capture a 10-25% spread via back-to-back ordering. |
| **2. Middleman Layer Compression** | Which product passes through 4+ intermediaries (`Petani/Pengrajin -> Tengkulak -> Agen -> Grosir -> Ritel`)? | Connect Layer 1 (Producer) directly to Layer 4 (B2B HORECA / Urban Group-Buy) and split the 40% saved margin. |
| **3. B2B Manual Friction Gap** | What repetitive task are SME owners currently doing manually on WhatsApp and Excel for 10+ hours/week? | Offer a "Done-For-You" automated service powered by CLI/AI tools on a monthly B2B retainer. |
| **4. Unbundling the Bloated Incumbent** | Where are customers forced to buy a Rp5,000,000 package when they only want 1 specific feature worth Rp500,000? | Unbundle that single high-frequency job-to-be-done into a fast, fixed-price micro-service. |
| **5. Trust & Compliance Moat Gap** | Where are buyers afraid of scams, fake goods, or non-compliance (e.g., used electronics, halal/BPOM, tax)? | Sell **Verified Assurance / Curated Inspection** as the core value proposition at a 15-30% premium. |
| **6. Tier-2 / Tier-3 Geographic Gap** | What service is Already commonplace in Jakarta/Surabaya but has zero professional providers in Tier-2/3 cities (Semarang, Solo, Malang, Balikpapan, Makassar)? | Transplant the proven playbook into Tier-2/3 cities where rent, labor, and ad CAC are 50-70% lower. |

## 3. Zero-Rupiah (`Modal Rp0`) Business Playbooks

Every Modal Rp0 playbook relies on one mathematical law: **Negative Cash Conversion Cycle ($\text{CCC} < 0$)**—never spend a single Rupiah on COGS or inventory until the customer's cash is already in your account.

### Playbook 1: Pre-Order (PO) & Paid-Pilot Validation ($\text{CCC} = -14\text{ Days}$)
1. Create a high-converting mockup, prototype, or sample offer (using existing free tools/ArtCraft).
2. Pitch to 30 targeted buyers via WhatsApp/DM/communities with an Early-Bird Pre-Order batch (minimum 50% to 100% upfront payment).
3. Set a clear batch threshold (e.g., *"Kuota PO Batch 1 hanya 20 slot; jika kuota tidak terpenuhi dalam 7 hari, dana dikembalikan 100%"*).
4. Use the collected customer cash to pay the supplier/manufacturer, deliver the product, and pocket the 30-50% gross margin with **Rp0 initial capital at risk**.

### Playbook 2: B2B Productized Service & AI Automation Agency (Modal Skill + Laptop)
1. Identify local SMEs with high customer lifetime value (clinics, law firms, property agents, wedding vendors, B2B distributors, exporters).
2. Offer a concrete, measurable outcome (e.g., *"Kami rapikan sistem katalog, otomatisasi respons WhatsApp & laporan keuangan SAK EMKM, atau produksi 12 video vertikal bulanan"*).
3. Charge a **50% upfront onboarding fee** before work begins. Deliver using local AI/CLI workflows with near-zero marginal cost.

### Playbook 3: Back-to-Back B2B Offtaker / Supply-Chain Connector
1. Lock in non-exclusive price lists and sample photos from 3 reliable local producers/workshops (convection, agricultural processors, packaging factories, printing presses).
2. Approach corporate/organizational buyers (campus committees, offices, hotels, cafes) and secure a Purchase Order (PO) with a **50% Down Payment (DP)**.
3. Forward the DP to the factory to cover raw materials, supervise quality control, deliver, collect the remaining 50%, and retain the 15-30% spread.

### Playbook 4: Idle-Capacity Revenue-Share Partner (*Rainmaker Model*)
1. Find asset-heavy businesses suffering from low utilization on weekdays or off-peak hours (aesthetic clinics, photography studios, commercial kitchens, futsal/badminton courts, training rooms, heavy equipment).
2. Propose a **Zero-Upfront Revenue Share (e.g., 30% for you, 70% for the venue owner)** on every new booking or bundled package *you* bring in during their dead hours.
3. You get access to billions of Rupiah worth of physical infrastructure for **Rp0 rent**, and the owner gets pure incremental margin on sunk fixed costs.

### Playbook 5: Demand-First Digital Asset & Micro-Consultancy
1. Publish 5 high-density problem-solving breakdowns on social/community channels solving a painful, specific niche problem.
2. Offer a paid 1-on-1 diagnostic or pre-sale template/toolkit bundle before building a full course or software product.
3. Standardize the questions asked in the first 5 paid sessions into a repeatable digital template/playbook with **~98% gross margin**.


---
## Source: `skills/business-sage/references/customer-psychology-sales-and-phd-loop.md`

# Customer Interaction Psychology, Sales Closing & Eternal Ph.D. Self-Learning Reference

Use this reference when executing **Pillar 4** and **Pillar 5** of `business-sage` to master customer interaction, objection handling, negotiation, and the Eternal Ph.D. continuous learning loop.

## 1. Customer Discovery & Behavioral Psychology (`How Customers Actually Buy`)

1. **The Mom Test (Rob Fitzpatrick) & Jobs-to-be-Done (Clayton Christensen)**:
   - Customers lie when asked *"Would you buy this?"* out of politeness.
   - **3 Golden Rules of Customer Discovery**:
     1. Talk about **their life and current workflow**, not your product idea.
     2. Ask about **specifics in the past** (*"Kapan terakhir kali masalah ini terjadi dan berapa kerugian waktunya/biayanya?"*), never generic opinions about the future.
     3. Look for **emotional friction and existing budget workarounds** (*What are they currently "hiring" to do the job?*).

2. **The 4 Forces of Customer Switching (JTBD Push-Pull Matrix)**:
   A customer only buys when:
   $$(\text{Push of Current Pain} + \text{Pull of New Solution}) > (\text{Anxiety of New Solution} + \text{Habit of Status Quo})$$
   - Most amateurs only amplify the *Pull* (features). A true **Business Sage** closes sales by reducing **Anxiety** (risk-reversal guarantees, free trial/sample, transparent proof) and reducing **Switching Habit Friction** (done-for-you onboarding).

## 2. Consultative Selling & Negotiation Frameworks (B2B & B2C)

### A. SPIN Selling (Neil Rackham) for High-Value Deals
Guide every customer conversation through 4 sequential question types:
1. **Situation Questions**: Understand their current setup briefly (do your homework first so you don't bore them).
2. **Problem Questions**: Surface the bottleneck (*"Bagian mana dari proses rekap stok/iklan Kakak yang paling sering bikin bocor?"*).
3. **Implication Questions (Crucial Multiplier)**: Quantify the pain of NOT fixing the problem (*"Kalau kebocoran 10% ini dibiarkan 6 bulan ke depan saat musim ramai, kira-kira berapa puluh juta margin yang hilang?"*).
4. **Need-Payoff Questions**: Let the *customer* state the value of your solution in their own words (*"Kalau proses ini bisa otomatis selesai dalam 5 menit, seberapa besar dampaknya buat tim Kakak?"*).

### B. Chris Voss Tactical Empathy & Objection Handling
When a customer raises an objection (*"Mahal banget"*, *"Saya pikir-pikir dulu"*, *"Tanya pasangan/atasan dulu"*), never argue:
1. **Label the Emotion / Hesitation**: *"Sepertinya Kakak ingin memastikan investasi ini benar-benar balik modal cepat dan aman buat arus kas bulanan ya."*
2. **Accusation Audit (Disarm Upfront)**: State their worst fear before they say it (*"Mungkin Kakak berpikir ini bakal ribet dipelajari tim..."*).
3. **Calibrated "How / What" Questions**:
   - When pushed for an unsustainable discount: *"Saya sangat ingin membantu proyek ini jalan, tapi bagaimana cara kita menyesuaikan ruang lingkupnya agar masuk ke angka anggaran tersebut tanpa mengorbankan kualitas utamanya?"*
   - To uncover the real blocker behind *"Pikir-pikir dulu"*: *"Tentu boleh sekali, Kak. Supaya saya bisa siapkan info yang pas, bagian mana yang paling perlu dipastikan dulu—apakah di skema pembayarannya atau di waktu pengerjaannya?"*

### C. Indonesian High-Conversion WhatsApp & Consultative Closing Protocol
In Indonesia, **70-85% of SME and B2B conversions happen on WhatsApp**. Apply the **5-Step WARMTH Closing Flow**:
1. **W - Fast & Personalized Greeting (<5 Minutes)**: Address by name/title (*Kak / Pak / Bu [Nama]*), mirror their tone, and validate their inquiry immediately.
2. **A - Diagnose Before Pitching (2 Questions Max)**: Ask 1-2 short diagnostic questions before dropping a price list (*"Agar saya rekomendasikan paket yang paling hemat dan pas, boleh tahu ini untuk kebutuhan [Opsi A] atau [Opsi B], Kak?"*).
3. **R - Price Anchoring & 3-Tier Menu (Decoy Effect)**: Present 3 options (**Basic**, **Recommended / Best Value**, **Premium VIP**) and always state the **Return/Value** before the **Price**.
4. **M - Risk Reversal & Social Proof**: Attach 1 relevant case study/testimonial and a clear safety net (garansi revisi / garansi uang kembali / bayar bertahap).
5. **T/H - Low-Friction Micro-Commitment Call-to-Action**: End with an easy binary choice (*"Untuk pengirimannya/jadwal mulainya, lebih nyaman kami proses untuk hari Selasa atau Kamis ini, Kak?"*).

## 3. The Eternal-Student Empirical Research Loop (`phd_business_ledger/`)

`business-sage` adopts the **humility of an Eternal Business Student** (inspired by empirical graduate/doctoral research methodology—observing real anomalies, testing falsifiable hypotheses, and never assuming it already knows everything). It deeply respects real business students, scholars, and field-tested entrepreneurs while keeping structured notes in `phd_business_ledger/`:

```text
phd_business_ledger/
├── phd_curriculum_progress.json         # Tracks study notes across BBA, MBA, and empirical research topics
├── app_capabilities_snapshot.json       # Tracks newly connected CLI/business apps & software version diffs
├── dissertation_notes.md                # Empirical syntheses of new business papers, methods & case studies
├── trend_radar_registry.json            # Active Bass Diffusion & Geo-Lag trend predictions with confidence scores
├── customer_objection_playbook.md       # Living library of tested customer objections and consultative responses
└── zero_rupiah_experiments_log.md       # Post-mortems and unit-economics results from Modal Rp0 experiments
```

### The 4-Step Eternal Ph.D. Research Cycle
Whenever the agent runs a learning cycle (`cli-anything-business-sage phd-learn` or during user consultations):
1. **Observe & Question**: Detect a new business model, pricing anomaly, regulatory change, or customer objection pattern.
2. **Formulate Falsifiable Hypothesis**: Express the insight as a testable causal equation (e.g., *"Offering a 14-day paid pilot at 15% of annual contract value reduces B2B sales cycle length by >40% compared to free trials"*).
3. **Empirical & Literature Cross-Check**: Cross-examine against unit economics math, historical market precedents, and Indonesian regulatory constraints.
4. **Codify into Playbook**: Persist the verified method into `phd_business_ledger/` so every subsequent consultation benefits from cumulative doctoral intelligence.


---
## Source: `skills/business-sage/references/cross-skill-synergy-and-new-app-onboarding.md`

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


---
## Source: `skills/cli-anything-business-sage/SKILL.md`

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
