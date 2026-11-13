# malaysian-political-intelligence-media
Malaysian Political Intelligence &amp; Media: An independent research workspace for Malaysian politics, public finance, economic policy, geopolitics, fact-checking and evidence-based Threads content creation.

---

## What this project is

A Claude Code workspace for producing **neutral, verified, well-sourced** research and short-form content about Malaysia. Claude does the research, analysis, drafting and fact-checking. **You approve and publish yourself.** Claude never posts anything.

### Core principles
- **Political neutrality.** Same standard for every party, coalition and community.
- **Source verification.** Primary sources first; every claim labelled and cited.
- **Factual accuracy.** Time-sensitive facts checked against current sources, with an "as of" date.
- **Threads posts ≤ 500 characters**, checked by a script.
- **Never published without your explicit approval.**
- **No API credentials needed.** Everything runs on public sources and local files.

Full rules: [`CLAUDE.md`](CLAUDE.md).

---

## Project structure

```
.
├── CLAUDE.md                     # Permanent project rules (read by Claude every session)
├── README.md
├── .claude/skills/
│   ├── malaysian-political-research/SKILL.md
│   ├── political-analysis/SKILL.md
│   ├── public-finance-analysis/SKILL.md
│   ├── geopolitical-analysis/SKILL.md
│   ├── threads-content-writer/SKILL.md
│   └── fact-checking-editor/SKILL.md
├── research/                     # Cited research briefs, by topic area
│   ├── malaysia-politics/
│   ├── public-finance/
│   ├── economy/
│   ├── geopolitics/
│   └── public-policy/
├── analysis/
│   ├── political/
│   ├── public-finance/
│   └── geopolitical/
├── threads-drafts/               # Claude writes Threads drafts here
│   └── approved/                 # Only after fact-check PASS + your explicit approval
├── published-posts/              # Only after YOU post it (record the URL)
├── fact-checks/                  # Fact-check reports (PASS / REVISE / FAIL)
├── sources/source-log.md         # Every source used
├── templates/                    # Brief, analysis, Threads post, fact-check templates
└── scripts/check_threads_length.py   # 500-character checker (no network, no credentials)
```

---

## Workflow

```
1. Research  →  2. Analysis  →  3. Threads draft  →  4. Fact-check  →  5. YOUR approval  →  6. YOU publish
```

1. **Research** a topic → brief in `research/<area>/`.
2. **Analyse** it (political, fiscal or geopolitical) → `analysis/…`.
3. **Draft** a Threads post or thread → `threads-drafts/`.
4. **Fact-check** the draft → report in `fact-checks/` with a verdict.
5. **Approve** explicitly: *"I approve TH-2026-11-13-01."* Any later edit cancels the approval.
6. **Publish** manually on Threads, then (optionally) ask Claude to record the URL and move the file to `published-posts/`.

---

## The six Skills — how to use each

Skills load automatically when your request matches their description. You can also name them directly, e.g. *"Use the public-finance-analysis skill to…"*.

### 1. `malaysian-political-research`
**Purpose:** Neutral, cited background research on Malaysian politics — Parliament, laws, elections, parties, state governments, courts, policy.
**Example prompts:**
- "Research the current status of the [bill name] in Parliament."
- "Give me a cited background brief on [state] state government since its last election."
**Output:** `research/<area>/YYYY-MM-DD-topic.md` with labelled findings, stakeholder positions, unknowns and risk flags.

### 2. `political-analysis`
**Purpose:** Interpret political developments — incentives, institutions, seat arithmetic, implications and scenarios — without taking sides.
**Example prompts:**
- "Analyse what this by-election result means for federal–state relations."
- "Give me three scenarios for [issue] with indicators to watch."
**Output:** `analysis/political/…` with facts separated from analysis, steelmanned perspectives and scenarios.

### 3. `public-finance-analysis`
**Purpose:** Budget, debt, deficit, subsidies, taxes, BNM policy, inflation, GDP — with numbers, units and calculations shown.
**Example prompts:**
- "Break down Budget [year]: operating vs development spending, compared with last year."
- "How much would [policy promise] cost? Show your calculation."
**Output:** `analysis/public-finance/…` with a key-figures table, step-by-step calculations and trade-offs.

### 4. `geopolitical-analysis`
**Purpose:** Malaysia's foreign policy and regional issues — ASEAN, South China Sea, US–China, neighbours, trade, Middle East — from Malaysia's vantage point, using sources from several countries.
**Example prompts:**
- "How do new US tariffs affect Malaysia's semiconductor exports?"
- "Explain Malaysia's position on [South China Sea incident] and the other parties' positions."
**Output:** `analysis/geopolitical/…` separating official positions from inferred interests.

### 5. `threads-content-writer`
**Purpose:** Turn verified research into Threads drafts (English, BM or bilingual), each post ≤ 500 characters.
**Example prompts:**
- "Turn the Budget brief into a 4-post Threads explainer in BM."
- "Write one Threads post on the latest OPR decision from the analysis file."
**Output:** `threads-drafts/TH-….md` with character counts, sources, and status `AWAITING FACT-CHECK` → `AWAITING OWNER APPROVAL`. **Drafts only.**

### 6. `fact-checking-editor`
**Purpose:** Independent check of claims, numbers, quotes, neutrality, legal risk (defamation, 3R, s.233, sub judice) and character limits.
**Example prompts:**
- "Fact-check TH-2026-11-13-01 before I approve it."
- "Is this viral claim about [topic] accurate?"
**Output:** `fact-checks/FC-….md` with a claim-by-claim table, edits, and a **PASS / REVISE / FAIL** verdict. PASS ≠ approval — the decision stays with you.

---

## Checking Threads length yourself

```bash
python3 scripts/check_threads_length.py threads-drafts/TH-2026-11-13-01-example.md
```

Posts are marked inside the draft with `<!-- post -->` … `<!-- /post -->`. Exit code `0` = all posts ≤ 500 characters; `1` = at least one is over.

---

## Disclaimer

This is an independent research and media workspace. Analysis is not legal, financial or investment advice. Content on sensitive topics (defamation, race, religion, royalty, ongoing court cases) should be reviewed carefully, and by a lawyer where risk is high.
