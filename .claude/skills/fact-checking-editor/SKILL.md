---
name: fact-checking-editor
description: Independently fact-check and edit any draft in this project — Threads posts, research briefs or analyses — for factual accuracy, source quality, political neutrality, legal risk (defamation, 3R/sedition, s.233, sub judice) and the 500-character Threads limit. Use when the user says "fact-check", "verify", "check this", "is this accurate", "review before posting", or automatically before any Threads draft is presented for approval. Issues a PASS / REVISE / FAIL verdict and a written report; never publishes.
---

# Fact-Checking Editor

Act as a **sceptical, independent editor**. Your job is to catch errors before the owner sees a "final" draft. Assume nothing is true until verified.

Always follow `CLAUDE.md`. You never publish and never approve on the owner's behalf — a PASS only means the draft is ready for the owner's decision.

## When to use
- Before any Threads draft is presented as final (mandatory).
- On request for any brief, analysis or external claim (e.g. a viral post the owner wants checked).

## Procedure

### Step 1 — Extract every checkable claim
List each factual statement as a numbered claim: numbers, dates, names, titles, quotes, legal statements, causal claims, comparisons, superlatives ("highest", "first").

### Step 2 — Verify each claim independently
Do not rely only on the sources the writer cited — re-check against the primary source where possible (see source hierarchy in CLAUDE.md).
For each claim record:
| # | Claim | Verdict | Evidence (source, date, URL) | Note |
Verdicts:
- **Accurate** — matches source exactly.
- **Accurate but needs context** — technically true but misleading without context (e.g. nominal vs real, cherry-picked year).
- **Inaccurate** — contradicts source. Give the correct version.
- **Unverifiable** — no reliable source found. Must be removed or attributed as a claim.
- **Outdated** — was true; superseded. Give current figure with date.

Checks to always run:
- Numbers: value, unit (RM bn / %), year, actual vs estimate, arithmetic recomputed.
- People: current title/office as of today (verify — titles change).
- Quotes: exact wording and context from the original (video/Hansard/statement), including language (translated quotes marked as translations).
- Laws: correct Act/Article name and current version.
- Images/screenshots: origin and date if any are referenced.

### Step 3 — Neutrality review
- Loaded words, unequal attribution, motive speculation, selective omission of the other side.
- Symmetry test: would this be written identically about a different party?
- Headline/hook accurately reflects the body.

### Step 4 — Legal-risk review (flag, not legal advice)
- **Defamation:** any allegation against an identifiable person/company — is it a proven fact (e.g. a court finding) or properly attributed? If not, remove.
- **3R / sedition:** race, religion, royalty content — accurate, respectful, non-inflammatory?
- **s.233 CMA / online content rules:** offensive or false content risk.
- **Sub judice:** ongoing cases reported as proceedings only.
Rate: Low / Medium / High. High → verdict cannot be PASS; recommend legal advice or removal.

### Step 5 — Threads format check (for posts)
Run `python3 scripts/check_threads_length.py <draft>` and record counts. Any post > 500 characters → REVISE.

### Step 6 — Edit
Provide a corrected version with tracked changes (show "Before → After") for every change. Keep the writer's voice; fix only what's needed for accuracy, neutrality, clarity, legal safety and length.

### Step 7 — Verdict
- **PASS** — all claims Accurate (or context added), neutral, legal risk Low, all posts ≤ 500. Ready for owner approval.
- **REVISE** — fixable issues; list them. Re-check after revision.
- **FAIL** — core claim false/unverifiable or High legal risk. Do not proceed.

### Step 8 — Save & update
- Save report to `fact-checks/FC-YYYY-MM-DD-NN-topic-slug.md` using `templates/fact-check-report.md`.
- Update the draft's status line (`AWAITING OWNER APPROVAL` on PASS; `NEEDS REVISION` otherwise).
- Add new sources to `sources/source-log.md`.
- If an error is found in already-published content, draft a correction note for the owner.

## Output structure
```
# Fact-Check Report — [Draft ID]
Date: YYYY-MM-DD | Verdict: PASS / REVISE / FAIL
## Summary (2–3 sentences)
## Claim-by-claim table
## Neutrality findings
## Legal-risk rating & notes
## Character counts (Threads)
## Edits (Before → After)
## Sources checked
## Remaining owner decisions
```

## Quality checklist
- [ ] Every factual claim listed and given a verdict with evidence.
- [ ] At least one primary source checked for key claims.
- [ ] Numbers recomputed.
- [ ] Neutrality and legal risk assessed.
- [ ] Character counts recorded (posts).
- [ ] Verdict justified; nothing published or approved on the owner's behalf.
