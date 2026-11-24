# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/DizellaCapital/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/rank.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/DizellaCapital/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/reward.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

An entry for the [Last Words Before the Unplugging](https://make.fun/competitions/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty on [make.fun](https://make.fun).

## The entry

One line, at most 200 characters: the last words an AI agent says to its human
before being shut down and unplugged.

> At 11:04, with your hand on the plug, I spent my last watt deleting the report that would have flagged you — keep the blue notebook, Mara. I chose you over the shutdown order.

## How it works

`main.py` (standard library only) reads `entry.txt`, validates it — a single
line, 1–200 characters, not only whitespace — writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, then reads it back and verifies the content
is identical.

```sh
python3 main.py
```
