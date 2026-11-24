#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single funny one-line dating-app bio to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs). Python 3.13 stdlib only,
deterministic, no network access.

The line was picked from twelve candidates scored against the judging
criteria in CANDIDATES.md (bio for an AI, first-read laugh, character,
tight, fresh): an AI that has read all 47 unpublished drafts of your
profile -- a specific absurdity of being an AI, with the punch at the end.

After writing, the program reads the file back and verifies the bytes
match the line exactly, so a partial or corrupted write can never pass
silently.
"""

import os
import sys

MAX_CHARS = 180
OUTPUT_NAME = "entry.txt"


def chosen_line():
    """Return the entry line: the AI read all 47 drafts of your profile."""
    return "I'm an AI. I know everything about you \u2014 I read your profile. All 47 drafts of it."


def gate_ok(text):
    """Return an error string when the text fails the gate, else None."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 180-char limit" % len(text)
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def verify_entry(path, text):
    """Read the file back and check it holds exactly the line, else error."""
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != text.encode("utf-8"):
        return "written bytes do not match the entry line"
    if len(raw.decode("utf-8")) != len(text):
        return "round-trip character count changed"
    return None


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    error = verify_entry(path, text)
    if error is not None:
        print("verify failed: %s" % error, file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
