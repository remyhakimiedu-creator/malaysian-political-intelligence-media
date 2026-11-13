---
name: public-finance-analysis
description: Analyse Malaysian public finance and economic policy with verified numbers — federal Budget, revenue and expenditure, fiscal deficit, government debt and contingent liabilities, subsidies and subsidy rationalisation, taxes (SST, e-invoicing, etc.), GLCs/GLICs, Bank Negara monetary policy, inflation, GDP, wages and cost of living. Use when the user asks about budget figures, "can the government afford…", debt, subsidies, taxes, economic data or the fiscal impact of a policy. Shows calculations, units and sources.
---

# Public Finance Analysis

Explain Malaysian fiscal and economic issues **accurately, with transparent calculations**, so a non-specialist can follow and check the numbers.

Always follow `CLAUDE.md`.

## When to use
- Budget announcements, Fiscal Outlook, mid-year reviews, supplementary supply bills.
- Deficit, debt, debt service charges, guarantees, contingent liabilities.
- Subsidies (fuel, electricity, cooking oil, rice, etc.), targeted assistance (e.g. cash aid programmes), tax changes.
- BNM decisions (OPR), inflation (CPI), GDP, employment, wages, ringgit exchange rate.
- Costing a political promise ("How much would X cost?").

## When NOT to use
- The question is mostly about political dynamics → `political-analysis` (call this Skill for the numbers).

## Core sources (primary first; always check the latest edition)
- **Ministry of Finance:** Budget speech, Fiscal Outlook and Federal Government Revenue Estimates, Economic Outlook, Federal Government Financial Statements.
- **Bank Negara Malaysia:** Monetary Policy Statements, Annual/Economic & Monetary Review, Financial Stability Review, monthly statistical bulletin.
- **DOSM / OpenDOSM:** GDP, CPI, labour force, household income & expenditure surveys, trade.
- **National Audit Department:** Auditor-General's Reports.
- **Parliament:** Supply Bills, PAC reports, Hansard answers to written questions.
- **Law:** Public finance and fiscal responsibility legislation — verify the current Act, its targets and status before citing.
- **International:** IMF Article IV, World Bank Malaysia Economic Monitor, rating-agency reports (note they are opinions).

No paid data terminals or API keys are required. Use public documents only.

## Procedure

### Step 1 — Pin down the exact question and unit
E.g. "Federal government fiscal deficit as % of GDP, 2025 estimate vs 2024 actual."

### Step 2 — Get the numbers from the source document
For each figure record: value, unit (RM billion / % of GDP), year, **actual vs revised estimate vs budget estimate**, nominal vs real, and exact source/table/page.

### Step 3 — Define terms correctly
Do not confuse: federal government debt vs public sector debt vs debt + committed government guarantees + other liabilities; operating vs development expenditure; gross vs net; headline vs core inflation; nominal vs real GDP; allocation vs actual spending.

### Step 4 — Calculate transparently
Show every calculation step. Example:
```
Change = (2025 estimate − 2024 actual) / 2024 actual × 100
       = (RM X bn − RM Y bn) / RM Y bn × 100 = Z %
```
- Round only at the end; state rounding.
- Adjust for inflation when comparing across years (state the deflator/CPI base).
- Use per-capita or % of GDP when comparing size across years or countries.
- Double-check arithmetic (recompute once a second way).

### Step 5 — Context and trade-offs
- Historical trend (≥5 years where available).
- Peer comparison (ASEAN peers / similar-income economies) with consistent definitions.
- Distributional impact: who gains/loses (income groups B40/M40/T20 or current classification, regions, businesses). Verify current classification terms.
- Opportunity cost: what else the money could fund.
- Present the main economic arguments on each side (e.g. fiscal consolidation vs. support for households) without endorsing one.

### Step 6 — State uncertainty
Estimates get revised. Flag projections, assumptions (oil price, growth), and data gaps.

### Step 7 — Save
`analysis/public-finance/YYYY-MM-DD-topic-slug.md` using `templates/analysis.md`. Log sources in `sources/source-log.md`.

## Output structure
```
# [Topic] — Public Finance Analysis
As of: YYYY-MM-DD | Confidence: High/Medium/Low
## Bottom line (2–3 sentences, with the key number)
## Key figures table (value | unit | year | actual/estimate | source)
## Calculations (step by step)
## What it means ([ANALYSIS])
## Trade-offs & distributional effects
## Arguments on each side
## Uncertainties & data caveats
## Sources
```

## Quality checklist
- [ ] Every number has unit, year, status (actual/estimate) and source.
- [ ] Calculations shown and re-checked.
- [ ] Definitions used consistently (no debt-measure mixing).
- [ ] Inflation/GDP adjustment applied where comparing over time.
- [ ] Balanced presentation of policy trade-offs.
- [ ] Nothing published or sent externally.
