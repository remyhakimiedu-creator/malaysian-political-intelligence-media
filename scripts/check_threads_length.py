#!/usr/bin/env python3
"""Check that every Threads post in a draft file is within the 500-character limit.

Usage:
    python3 scripts/check_threads_length.py <draft.md> [<draft2.md> ...]
    echo "some text" | python3 scripts/check_threads_length.py -

Posts are the text between `<!-- post -->` and `<!-- /post -->` markers.
If a file has no markers, the whole file is treated as one post.

Counting: Unicode code points after NFC normalisation, with leading/trailing
whitespace stripped. Spaces, punctuation, emoji, hashtags and URLs all count.
Some emoji are several code points, so this count is conservative (it may be
slightly higher than what Threads shows, never lower for normal text).

Exit code 0 = all posts OK, 1 = at least one post over the limit, 2 = usage error.
No network access and no credentials are used.
"""
import re
import sys
import unicodedata

LIMIT = 500
WARN_AT = 480  # safety margin recommended by the threads-content-writer Skill
POST_RE = re.compile(r"<!--\s*post\s*-->(.*?)<!--\s*/post\s*-->", re.DOTALL | re.IGNORECASE)


def count(text: str) -> int:
    return len(unicodedata.normalize("NFC", text.strip()))


def extract_posts(raw: str) -> list[str]:
    posts = POST_RE.findall(raw)
    return posts if posts else [raw]


def check(name: str, raw: str) -> bool:
    ok = True
    posts = extract_posts(raw)
    print(f"{name}: {len(posts)} post(s)")
    for i, post in enumerate(posts, 1):
        n = count(post)
        if n > LIMIT:
            status, ok = f"FAIL (over by {n - LIMIT})", False
        elif n > WARN_AT:
            status = "OK (near limit)"
        elif n == 0:
            status, ok = "FAIL (empty)", False
        else:
            status = "OK"
        print(f"  post {i}: {n}/{LIMIT} characters - {status}")
    return ok


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    all_ok = True
    for path in argv[1:]:
        if path == "-":
            all_ok &= check("<stdin>", sys.stdin.read())
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                all_ok &= check(path, fh.read())
        except OSError as exc:
            print(f"{path}: cannot read ({exc})")
            return 2
    print("RESULT:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
