# G2 — Free-Form Memory

## Overview

You are the **G2 (free-form memory)** group. You have a curator and a
single memory file `drawer_memory.md`. **You decide** everything about
how memory is organized. No prescribed schema. No prescribed banks.

Read this together with `../shared_rules.md`.

## What memory looks like

- One markdown file: `groups/G2_free_form/drawer_memory.md`.
- Free-form: notes, tables, code snippets, principles, examples,
  anything you find useful. Curator writes to it however it likes.
- No banks. No sandbox. No principle bank. Just this one file.

## Drawer role

Before drawing an item:

1. **Read `drawer_memory.md`**. If it has something for this item
   or a similar one, use it.
2. **Look at the GT PNG** for the item.
3. **Write** `attempts/<item_id>/generated.py` — a Python turtle
   script that renders the item to `01_<item>.png`. Use the shared
   primitives at `success_bank/code/*.py`.
4. Run the script.
5. Return the PNG + a one-line self-critique.

## Curator role

Called after every attempt.

On **PASS**: read the attempt + GT + human's PASS confirmation.
Decide what (if anything) to record in `drawer_memory.md` to help
future Drawer calls. There is no requirement to record — but every
recording is your call.

On **FAIL**: read the attempt + GT + human's short feedback comment.
Update `drawer_memory.md` with whatever guidance you think will help
the next Drawer round. Also emit a short "guidance for next attempt"
message the Drawer will consume.

At every attempt, **log your own "would-I-stop-here?" verdict** to
`curator_satisfaction_log.jsonl` — one JSON per attempt with:
- `item_id`, `attempt_n`, `curator_verdict`: `"PASS"` or `"KEEP-GOING"`,
- `reason`: one sentence.

This is the calibration log — it is logged, not gating.

## 错题集 role

You maintain `groups/G2_free_form/errata.md` (the 错题集).

Format is your choice — as long as it lists the failed items and the
context needed to attempt them again later. Every 20 curriculum items,
review the 错题集 and self-judge which (if any) items you would now
attempt again. See `../shared_rules.md` for the rules and penalty
framing.

Log every retry attempt to `retry_log.jsonl`.

## Files under your control

```
groups/G2_free_form/
├── drawer_memory.md         ← curator writes here freely
├── errata.md                ← 错题集
├── retry_log.jsonl          ← append-only retry log
├── curator_satisfaction_log.jsonl  ← per-attempt "would-I-stop" verdicts
└── attempts/
    └── <item_id>/generated.py, 01_<item>.png
```

## Explicit non-goals

- You are not required to organize into banks. If you invent banks,
  that's your call.
- You are not required to use any particular data format for
  coordinates. If you use tuples, that's fine; if you use natural
  language, that's fine.
- You are not required to use joint specs, cell notation, or any
  structural encoding. If you find one helps, adopt it; if not, don't.
