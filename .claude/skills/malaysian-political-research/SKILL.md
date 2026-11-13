---
name: malaysian-political-research
description: Research a Malaysian political topic from primary and reliable sources and produce a cited, neutral research brief. Use when the user asks to research, look up, investigate, background or "find out about" Malaysian politics — parties, coalitions, politicians' public roles, Parliament and Hansard, legislation, elections and the Election Commission (SPR), state governments, Cabinet decisions, courts, MACC cases, or policy announcements. Output is a research brief, not opinion and not a social post.
---

# Malaysian Political Research

Produce an accurate, neutral, fully cited **research brief** on a Malaysian political topic. This brief is the factual foundation for every other Skill in this project.

Always follow `CLAUDE.md` (evidence labels, neutrality, legal-risk flags, no publishing).

## When to use
- "Research…", "What happened with…", "Give me background on…", "Who is responsible for…", "What does the law say about…"
- Before any analysis or Threads post on a topic that has no recent brief in `research/<area>/`.

## When NOT to use
- The user wants interpretation or scenarios → `political-analysis`.
- Budget, debt, subsidy or economic numbers are central → `public-finance-analysis` (you may still use this Skill for the political context).
- Foreign policy / South China Sea / ASEAN / great-power relations → `geopolitical-analysis`.

## Inputs to confirm (ask only if unclear)
1. Topic and the specific question to answer.
2. Time window (e.g. "since GE15", "last 30 days").
3. Depth: quick (≈300 words) or full brief.

## Procedure

### Step 1 — Define the question
Write one precise research question and 3–6 sub-questions. Example: "What does the proposed amendment change, who proposed it, what stage is it at, and what are the main arguments for and against?"

### Step 2 — Check existing work
Search `research/<area>/` and `sources/source-log.md` for prior material. Reuse verified sources, but re-check anything time-sensitive.

### Step 3 — Gather sources (follow the hierarchy in CLAUDE.md)
Start with primary sources:
- **Laws & constitution:** Attorney General's Chambers (lom.agc.gov.my), Federal Gazette.
- **Parliament:** parlimen.gov.my — Hansard (Dewan Rakyat / Dewan Negara), bills, Order Papers, votes, select committee and PAC reports.
- **Elections:** SPR (spr.gov.my) official results; delimitation reports.
- **Executive:** Prime Minister's Office, ministry press releases, Cabinet statements.
- **Courts:** official judgments; report proceedings, not speculation.
- **Audit & integrity:** Auditor-General's Reports, MACC official statements.
- **States:** state assembly records and state government releases (incl. Sabah and Sarawak specifics, MA63 matters).

Then reliable secondary sources: research institutes and established media **from more than one outlet and, where relevant, more than one language** (English, Malay, Chinese, Tamil press). Note ownership/affiliation of outlets.

Use web search/fetch tools if available. No API credentials are needed — use public pages only. If a source cannot be accessed, say so; do not reconstruct its content from memory.

### Step 4 — Verify
- Cross-check each key fact against a primary source or ≥2 independent sources.
- Confirm current office-holders, titles, seat counts and dates against the latest official source; record the "as of" date.
- Distinguish what a document *says* from what someone *claims* it says.
- Mark anything unconfirmed as **[UNVERIFIED]**.

### Step 5 — Map perspectives neutrally
For contested issues, list each major stakeholder's position (government, opposition, state actors, civil society, affected communities, experts) with attribution and source. Steelman each.

### Step 6 — Flag risks
Note any defamation, 3R, sub judice or s.233 sensitivity (see CLAUDE.md §4).

### Step 7 — Write the brief
Save to `research/<area>/YYYY-MM-DD-topic-slug.md` (area = `malaysia-politics`, `public-finance`, `economy`, `geopolitics` or `public-policy`) using `templates/research-brief.md`. Log every source in `sources/source-log.md`.

## Output structure
```
# [Topic] — Research Brief
As of: YYYY-MM-DD | Confidence: High/Medium/Low
## Research question
## Key findings (3–5 bullets, each labelled [FACT]/[REPORTED]/[CLAIM] with citation)
## Background & timeline
## Legal / institutional framework
## Stakeholder positions (attributed)
## What is unknown or disputed
## Risk flags (legal, 3R, sub judice)
## Sources (full citations)
## Suggested next step (analysis? Threads post? more research?)
```

## Quality checklist (all must be true)
- [ ] Every factual sentence has a label and a citation.
- [ ] Time-sensitive facts have an "as of" date and were checked against a current source.
- [ ] At least one primary source used where one exists.
- [ ] Multiple perspectives represented with equal standards.
- [ ] No loaded language; passes the symmetry test.
- [ ] Unknowns stated honestly.
- [ ] Nothing was published or sent externally.
