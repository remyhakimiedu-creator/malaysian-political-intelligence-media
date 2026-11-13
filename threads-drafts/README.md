# threads-drafts/

**Drafts only.** Claude writes Threads posts here. Nothing in this folder has been approved or published.

**Skill:** `threads-content-writer` → checked by `fact-checking-editor`
**File name:** `TH-YYYY-MM-DD-NN-topic-slug.md` · **Template:** `templates/threads-post.md`

## Lifecycle
```
DRAFT → AWAITING FACT-CHECK → NEEDS REVISION / AWAITING OWNER APPROVAL → approved/ → (owner posts) → published-posts/
```

## Rules
- Each post ≤ 500 characters. Check: `python3 scripts/check_threads_length.py threads-drafts/<file>.md`
- Each post sits between `<!-- post -->` and `<!-- /post -->` markers.
- Every fact must trace to a cited source in the draft and appear in the fact-check report.
- A fact-check PASS is **not** approval.

## approved/
A draft moves to `approved/` only when **both** are true:
1. A fact-check report in `fact-checks/` has verdict **PASS**.
2. The owner has written explicit approval, e.g. "I approve TH-2026-11-13-01".
Any edit after approval cancels it and sends the draft back for re-checking.
Claude never posts from here — the owner publishes manually.
