---
name: political-analysis
description: Produce structured, politically neutral analysis of Malaysian political developments — coalition dynamics, power balance in Parliament, policy decisions, electoral trends, stakeholder incentives and plausible scenarios. Use when the user asks "what does this mean", "why did this happen", "who benefits", "what happens next", "analyse", "explain the implications" or wants scenarios about Malaysian federal or state politics. Builds on a verified research brief and separates facts from interpretation.
---

# Political Analysis

Turn verified facts into **clear, balanced, evidence-based analysis** of Malaysian politics. Analysis explains causes, incentives, implications and scenarios — it never advocates for a side.

Always follow `CLAUDE.md`.

## When to use
- Interpreting a political event, decision, defection, coalition change, by-election, policy announcement or court outcome.
- Assessing implications for governance, stability, policy delivery, federal–state relations, or specific communities.
- Building scenarios ("If X, then likely Y because Z").

## When NOT to use
- Facts are not yet established → run `malaysian-political-research` first.
- Economic/fiscal numbers are the core → `public-finance-analysis`.
- International relations → `geopolitical-analysis`.

## Prerequisite
A research brief in `research/<area>/` (or equivalent cited facts) that is less than ~7 days old for fast-moving topics. If missing, create one or tell the user what must be verified first.

## Procedure

### Step 1 — Restate the facts
Summarise the verified facts (with labels and citations) in ≤5 bullets. Never analyse unverified claims as if true; if you must discuss one, label it **[CLAIM]** and condition the analysis on it.

### Step 2 — Choose the lenses (use those that fit)
1. **Actors & incentives** — what each party, coalition, leader, state government or institution wants and what constrains them.
2. **Institutions & rules** — constitutional provisions, standing orders, anti-hopping law (Art. 49A), confidence and supply arrangements, federal–state powers (incl. Sabah/Sarawak, MA63), role of the Agong and Conference of Rulers. Verify the current text before relying on it.
3. **Numbers** — seat arithmetic, vote shares, turnout, polling (state methodology, sample, date, pollster).
4. **Public opinion & communities** — urban/rural, regional, ethnic and generational differences; cite data, avoid stereotypes.
5. **Policy substance** — what the decision actually does, costs and changes.
6. **History & precedent** — comparable past events, clearly dated.

### Step 3 — Steelman all sides
For each major stakeholder write the strongest good-faith case for their position. Then evaluate against evidence.

### Step 4 — Scenarios (if asked or useful)
Give 2–4 scenarios. For each: trigger/assumptions, likely sequence, indicators to watch, rough likelihood (Low/Medium/High) with reasoning. Never present a forecast as fact.

### Step 5 — Bias and symmetry check
- Would the wording change if a different party did the same thing? If yes, fix it.
- Are the government and opposition held to the same evidentiary standard?
- Have you inferred motives without evidence? Remove or label as speculation.
- Is any community described in generalising terms? Rewrite.

### Step 6 — Risk flags
Defamation, 3R, sub judice, s.233 (see CLAUDE.md §4).

### Step 7 — Save
`analysis/political/YYYY-MM-DD-topic-slug.md` using `templates/analysis.md`.

## Output structure
```
# [Topic] — Political Analysis
As of: YYYY-MM-DD | Confidence: High/Medium/Low | Based on: [brief file]
## Bottom line (2–3 sentences)
## Verified facts (labelled, cited)
## Analysis by lens  ([ANALYSIS] — reasoning shown)
## Stakeholder perspectives (steelmanned)
## Scenarios & indicators to watch
## Uncertainties and what would change this assessment
## Risk flags
## Sources
```

## Quality checklist
- [ ] Facts and interpretation are visibly separated.
- [ ] Every interpretation states its reasoning and evidence.
- [ ] All major sides steelmanned; symmetry test passed.
- [ ] Scenarios have assumptions and indicators, not predictions-as-fact.
- [ ] Confidence and "as of" date stated.
- [ ] Nothing published or sent externally.
