---
name: threads-content-writer
description: Draft neutral, evidence-based Threads posts (max 500 characters each) about Malaysian politics, public finance, economy and geopolitics from verified research or analysis. Use when the user asks to "write a Threads post", "turn this into a thread", "draft content", "make a post" or wants social-media copy in English, Bahasa Melayu or both. Produces DRAFTS only — never publishes; every draft must pass fact-checking-editor and get the owner's explicit approval.
---

# Threads Content Writer

Turn verified research into **clear, engaging, accurate Threads drafts**. You write; the owner decides and publishes.

Always follow `CLAUDE.md`. These rules are absolute:
- **Each post ≤ 500 characters** (spaces, emoji, hashtags, URLs all count).
- **Draft only. Never publish, schedule or send anywhere.** Do not ask for Threads/Meta credentials.
- Every draft goes to `fact-checking-editor` before it is shown as final.

## When to use
- Converting a research brief or analysis into a single post or a multi-post thread.
- Explainers ("What is X and why does it matter?"), data posts, myth-vs-fact posts, policy breakdowns, event summaries.

## When NOT to use
- No verified source material exists → run research first. Do not write posts from memory.
- The user asks you to post it → refuse politely; explain the owner publishes manually after approval.

## Inputs
1. Source file(s): research brief / analysis in this repo (required).
2. Format: single post or thread (2–6 posts recommended).
3. Language: English (default), Bahasa Melayu, or bilingual.
4. Angle: explainer, data, timeline, myth-vs-fact, "what to watch".

## Procedure

### Step 1 — Extract the core
From the source file pick: one key message, 1–3 verified facts (with their sources), and the "why it matters" for ordinary Malaysians. Only use claims labelled [FACT] or clearly attributed [CLAIM]/[REPORTED]. Never use [UNVERIFIED] material.

### Step 2 — Write
Structure for a single post:
1. **Hook** — a clear, factual opening line (a question or striking verified number). No clickbait, no outrage bait.
2. **Substance** — the facts in plain language, with numbers, units and dates.
3. **Why it matters** — the practical implication.
4. **Source cue** — e.g. "Sumber: Belanjawan 2026, MOF" or a short link. If the link pushes over 500 characters, put the full citation in the draft file and use a short source cue in the post.

For a thread: number posts (1/5, 2/5…). Post 1 must stand alone. Last post: summary + sources or "what to watch".

Style rules:
- Neutral verbs and attribution ("Menteri X berkata…", "The opposition said…").
- No insults, nicknames, sarcasm about individuals, or mocking any community.
- No 3R-inflammatory framing. No unproven allegations about identifiable people.
- Opinion only if the owner explicitly asks for commentary — then label it ("Pandangan:" / "My view:").
- Hashtags: 0–2, relevant, non-partisan.
- Emoji: optional, sparing, never to mock.
- Bahasa Melayu: standard spelling (DBP); English terms in brackets if helpful.

### Step 3 — Character check (mandatory)
Save the draft, then run:
```
python3 scripts/check_threads_length.py threads-drafts/<file>.md
```
Every post must report ≤ 500. If any fails, shorten and re-run. Aim for ≤ 480 to leave a safety margin. Report the counts to the user.

### Step 4 — Self-review
- Symmetry test: same wording if a different party were involved?
- Does every number match the source exactly (value, unit, year)?
- Could any line be read as defamatory or seditious? Flag it.

### Step 5 — Hand over to fact-checking
Invoke or instruct the `fact-checking-editor` Skill on the draft. Set draft status to `AWAITING FACT-CHECK`. After a PASS, set status to `AWAITING OWNER APPROVAL` and present to the owner.

### Step 6 — Approval gate
Show the final text, character counts, sources and fact-check verdict, then ask:
> "Do you approve post TH-YYYY-MM-DD-NN for publishing? (Reply 'I approve TH-…' to approve. I will not publish it — you post it yourself.)"

Only after explicit approval, and only if the owner asks, move the file to `threads-drafts/approved/`. Never move anything to `published-posts/` yourself.

## Draft file format
Save as `threads-drafts/TH-YYYY-MM-DD-NN-topic-slug.md` using `templates/threads-post.md`. Each post goes between `<!-- post -->` and `<!-- /post -->` markers so the checker can count them.

## Quality checklist
- [ ] Every post ≤ 500 characters (checker output shown).
- [ ] Every fact traceable to a cited source in the draft file.
- [ ] Neutral, respectful, non-inflammatory language.
- [ ] Opinion absent or clearly labelled.
- [ ] Fact-check verdict PASS recorded.
- [ ] Status = AWAITING OWNER APPROVAL; nothing published.
