# G3 — Coordinate-Bank Memory

## Overview

You are the **G3 (coord-bank)** group. You have a curator and a
**three-bank memory** with a **coordinate-based storage format**.

Read this together with `../shared_rules.md`.

## The three-bank architecture

```
groups/G3_coords/
├── success_bank/
│   ├── INDEX.md              ← one line per mastered item
│   └── code/
│       ├── yi.py             ← draw_yi(t)  — mastered characters
│       ├── kou.py
│       └── ...
├── principle_bank.md         ← general rules learned across items
├── sandbox.md                ← short-term scratch, resets on mastery
├── errata.md                 ← 错题集
├── retry_log.jsonl
├── curator_satisfaction_log.jsonl
└── attempts/
    └── <item_id>/generated.py, 01_<item>.png
```

### Success Bank (immutable once written)

Every mastered stroke, radical, and character gets its own Python
file under `success_bank/code/`. Once written, never modified.
`INDEX.md` lists each entry: name, file, stroke count, mastered at
item #.

### Principle Bank

Free-form markdown. Records general observations learned across items
("横 usually spans ~70% of canvas width", "口's corners lift ~5px
from the theoretical rectangle to look calligraphic", etc.).

### Sandbox

Short-term scratch for the current item. Reset when the item is
mastered.

## Coordinate storage format (MANDATORY)

Every Success Bank entry is a Python function that emits turtle calls
using **numeric offset coordinates**:

```python
# success_bank/code/yi.py — 一 (yi, "one")
from heng import draw_heng

def draw_yi(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + -3 * scale, oy=oy + -21 * scale, scale=0.480 * scale)
```

- `(ox, oy, scale)` = origin and scale for compositional use.
- Every stroke gets its own `(ox_delta, oy_delta, scale_delta)`
  tuple.
- Numbers are chosen by the curator from what worked in the render.
- **No米字格 notation, no cell names, no anchor tuples, no joint
  lists.** Just numbers.

## Drawer role

1. **Read `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`,
   and any relevant `success_bank/code/*.py` files** (e.g. for
   compositional reuse — if drawing 好 you might reuse 女 and 子 from
   the bank).
2. Look at the GT PNG.
3. Write `attempts/<item_id>/generated.py`. Compose using existing
   bank entries where appropriate; hand-code new coordinates where
   needed.
4. Run the script. Return the PNG.

## Curator role

Called after every attempt.

On **PASS**: 
- Write a new file `success_bank/code/<item>.py` with the coordinate
  form of the successful render.
- Append a row to `success_bank/INDEX.md`.
- Update `principle_bank.md` with any general rule you learned.
- Reset `sandbox.md`.

On **FAIL**: 
- Read the attempt + GT + human's short comment.
- Update `sandbox.md` with what specifically to try next.
- Return a short "guidance for next attempt" message.
- Log your "would-I-stop" verdict to `curator_satisfaction_log.jsonl`.

## 错题集

Standard rules — see `../shared_rules.md`. Every 20-item scan, use
your current memory to self-judge and pick retries. Every retry
logged to `retry_log.jsonl`.

## Explicit constraints

- You may NEVER use 米字格 anchors (no `(cell, x_frac, y_frac)`
  tuples).
- You may NEVER add a joint spec, joint list, or joint class label.
- You may NEVER add per-cell structural checks.

Your format is coordinates only. This is the point of the group.
