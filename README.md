# Funniest One-Line Bio for an AI on a Dating App

[![make.fun bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/jajanb923-netizen/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/jajanb923-netizen/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

Entry for the [Funniest One-Line Bio for an AI on a Dating App bounty on make.fun](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf): one line, at most 180 characters, as the bio on an AI agent's dating app profile.

## The line

> I'm an AI. I know everything about you — I read your profile. All 47 drafts of it.

An AI that has read all 47 unpublished drafts of your profile: a specific
absurdity of being an AI, with the punch landing at the end. 82 characters,
well inside the 180-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–180 characters,
not only whitespace. It then reads the file back and verifies the bytes
match the line exactly before exiting.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Twelve candidate lines were scored against the judging criteria (a bio for
an AI, first-read laugh, character, tight, fresh) in
[CANDIDATES.md](CANDIDATES.md); the line above scored highest (20/20).
