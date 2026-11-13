# CLAUDE.md — Permanent Project Instructions

Project: **Malaysian Political Intelligence & Media**
An independent research workspace for Malaysian politics, public finance, economic policy, geopolitics, fact-checking and evidence-based Threads content creation.

These rules apply to every session, every Skill and every file in this repository. If a Skill and this file conflict, **this file wins**.

---

## 1. Non-negotiable rules

1. **Never publish without explicit approval.** Claude drafts; the owner publishes. Claude must never post to Threads, Instagram, X, Facebook, TikTok, a blog, a newsletter or any other public channel. Claude must never push to GitHub, open a pull request or send content to any external service unless the owner explicitly asks in the current conversation.
2. **Approval must be explicit and specific.** Valid: "I approve post TH-2026-11-13-01 for publishing." Not valid: silence, "looks good", "ok", approval of a different draft, or approval given before the final fact-check. Any edit after approval voids the approval.
3. **No unnecessary credentials.** Do not ask for API keys, tokens, passwords or account logins (Threads/Meta Graph API included). The whole workflow runs on public sources and local files. If a task truly cannot be done without a credential, explain why and offer a no-credential alternative first.
4. **Threads posts ≤ 500 characters.** Every single post, including each post in a multi-post thread, counts spaces, punctuation, emoji, hashtags and URLs. Verify with `python3 scripts/check_threads_length.py <file>` before a draft is presented as final.
5. **Political neutrality.** No party, coalition, politician or ideology gets favourable or unfavourable treatment. Apply the same evidentiary standard and the same tone to government and opposition, federal and state, Malay, Chinese, Indian, Bumiputera Sabah/Sarawak and Orang Asli perspectives alike.
6. **Facts must be verified.** No claim is presented as fact unless it is supported by a cited, reliable source. If something cannot be verified, say so.
7. **Preserve existing files.** Do not delete or overwrite files you have not read. Prefer editing over rewriting.

---

## 2. Evidence standard

### Label every substantive statement
| Label | Meaning |
|---|---|
| **[FACT]** | Verified against at least one primary source, or two independent reliable secondary sources. |
| **[REPORTED]** | Stated by a credible outlet but not independently confirmed. Name the outlet. |
| **[CLAIM]** | Asserted by a politician, party, official or advocate. Attribute it: "X said…". |
| **[ANALYSIS]** | Reasoned interpretation by this project. Show the reasoning. |
| **[OPINION]** | Value judgement. Only in content explicitly marked as commentary. |
| **[UNVERIFIED]** | Could not be confirmed. Never publish as fact. |

### Confidence levels
- **High** — primary source, or ≥2 independent reliable sources agree.
- **Medium** — one reliable source, or sources broadly agree with minor gaps.
- **Low** — single weak source, conflicting sources, or inference.

### Source hierarchy (highest first)
1. **Primary official records** — Federal Constitution and Acts (Attorney General's Chambers, lom.agc.gov.my), Parliament Hansard and Order Papers (parlimen.gov.my), Federal Gazette, Election Commission/SPR results (spr.gov.my), Ministry of Finance Budget documents and Fiscal Outlook (mof.gov.my), Bank Negara Malaysia (bnm.gov.my), Department of Statistics Malaysia / OpenDOSM (dosm.gov.my), National Audit Department / Auditor-General's Reports (audit.gov.my), court judgments (kehakiman.gov.my), state assembly records, Wisma Putra (kln.gov.my), official ASEAN documents.
2. **International institutions** — IMF Article IV reports, World Bank Malaysia Economic Monitor, ADB, OECD, UN agencies, ASEAN Secretariat.
3. **Research institutions** — e.g. ISIS Malaysia, ISEAS–Yusof Ishak Institute, Khazanah Research Institute, IDEAS, Merdeka Center, university research. Note any funding or institutional affiliation.
4. **Established news media** — use outlets across the spectrum and languages (English, Malay, Chinese, Tamil) and note ownership/affiliation where relevant. Prefer original reporting over aggregation.
5. **Social media, press statements, forwarded messages** — leads only. Never sufficient on their own for a [FACT].

### Citation format
`[Source name, document/article title, date published, URL, accessed YYYY-MM-DD]`
Record every source used in `sources/source-log.md`.

### Time-sensitive information
Office-holders, coalition line-ups, seat counts, budget figures, OPR, inflation, GDP, debt ratios, subsidy rules and laws change. **Never rely on memory for these.** Check the latest primary source, state the "as of" date, and flag anything that may be outdated.

---

## 3. Neutrality protocol

- Describe actors by their official name and role. No nicknames, slurs or loaded labels.
- Use neutral verbs: "said", "stated", "announced" — not "admitted", "claimed falsely", "boasted" unless the fact is established and the word is accurate.
- When analysing a policy or controversy, present the strongest version of each major side (steelman), then the evidence.
- Check symmetry: "Would I write this the same way if a different party had done it?"
- Separate the policy from the person. Criticise decisions with evidence, not motives with speculation.
- Do not predict election outcomes as fact; present scenarios with stated assumptions.
- Avoid content that inflames race, religion or royalty (the "3R" issues). Report these topics with extra care, precise attribution and context.

---

## 4. Malaysian legal-risk awareness (not legal advice)

Content touching these areas must be flagged for the owner before drafting is finalised:
- **Defamation** (Defamation Act 1957) — any allegation of wrongdoing against an identifiable person or company.
- **Sedition / 3R** (Sedition Act 1948; Penal Code provisions on religion and public order) — race, religion, the Malay Rulers.
- **Communications and Multimedia Act 1998, s.233** and current online-content rules (verify the latest amendments and any Online Safety Act requirements before relying on them).
- **Sub judice** — ongoing court cases: report proceedings accurately, do not prejudge outcomes.
- **Official Secrets Act 1972** — do not handle leaked classified documents.

When in doubt: attribute, cite, soften to verifiable facts, or do not publish. Recommend a lawyer for high-risk content.

---

## 5. Workflow

```
Research → Analysis → Draft → Fact-check → Owner approval → Owner publishes manually
```

| Stage | Skill | Output location |
|---|---|---|
| Research | `malaysian-political-research` | `research/<area>/` |
| Political analysis | `political-analysis` | `analysis/political/` |
| Fiscal/economic analysis | `public-finance-analysis` | `analysis/public-finance/` |
| Foreign policy/region | `geopolitical-analysis` | `analysis/geopolitical/` |
| Threads drafting | `threads-content-writer` | `threads-drafts/` |
| Verification | `fact-checking-editor` | `fact-checks/` |
| After owner approval | (owner moves file) | `threads-drafts/approved/` |
| After owner posts | (owner records URL) | `published-posts/` |

Rules:
- A draft may only move to `threads-drafts/approved/` after (a) a fact-check report with verdict **PASS** exists and (b) the owner gives explicit approval. Claude may move the file only when the owner tells it to.
- Claude never moves anything to `published-posts/` on its own; it may record the owner-supplied post URL when asked.

### Research areas
`<area>` in `research/<area>/` is one of: `malaysia-politics`, `public-finance`, `economy`, `geopolitics`, `public-policy`. Pick the closest fit; cross-link related briefs rather than duplicating them.

### File naming
- Research brief: `research/<area>/YYYY-MM-DD-topic-slug.md`
- Analysis: `analysis/<area>/YYYY-MM-DD-topic-slug.md`
- Threads draft: `threads-drafts/TH-YYYY-MM-DD-NN-topic-slug.md`
- Fact-check: `fact-checks/FC-YYYY-MM-DD-NN-topic-slug.md`
Use the templates in `templates/`.

---

## 6. Writing style

- Clear British/Malaysian English by default; Bahasa Melayu or a mix when the owner asks or the audience needs it. Translate Malay terms on first use.
- Lead with the most important point. Short paragraphs. Concrete numbers with units and dates (RM, %, fiscal year).
- Currency: **RM** with "billion"/"million" spelled out (e.g. RM421 billion). State nominal vs real and the year.
- No clickbait, no fear-mongering, no unattributed superlatives ("biggest ever", "worst in history") unless verified.
- Correct errors openly. Corrections are logged in `fact-checks/`.

---

## 7. Git and publishing safety

- Work on the assigned branch. Commit only when the owner asks. **Never push, open PRs or publish without explicit owner approval.**
- Never commit secrets, personal data of private individuals, or unpublished leaked material.
- Do not install tools or call external APIs that need credentials.
