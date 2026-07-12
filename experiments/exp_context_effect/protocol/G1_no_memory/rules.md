# G1 — No-Memory Control

## Overview

You are the **G1 (control)** group. You do not have a curator. You do
not have a memory. Each item you draw is drawn "cold" with only:

- Its target label (name or character)
- Its GT PNG (300×300)
- The shared stroke primitives at `success_bank/code/*.py`

## Attempt policy (unique to G1)

- **You get exactly 1 attempt per item.** No retries. No feedback loop.
- G1's headline number is *first-attempt accuracy*, which is the only
  attempt you get.

Reason: giving G1 retries would let it re-derive its answer from
vision alone, contaminating the "no memory" contrast. The point of
G1 is to measure raw one-shot capability.

## Memory policy

- You have no memory directory to read or write to. Anything you learn
  from one item does not persist to the next. Every attempt starts
  clean.

## No 错题集 for G1

Since you get 1 attempt per item and no memory, the 错题集 does not
apply to G1. Failed items are recorded in the results but never
revisited.

## Drawer role — exact procedure per item

Given: a stroke / radical / character; its GT PNG path; its target label.

1. Look at the GT PNG.
2. Look at the shared stroke primitives available at
   `success_bank/code/*.py`.
3. Write `attempts/<item_id>/generated.py` — a Python turtle script
   that renders the item to `01_<item>.png`.
4. Run it: `python3 attempts/<item_id>/generated.py`.
5. Return the PNG path + a one-line summary.

## Output format

Each item produces:

```
groups/G1_no_memory/attempts/<item_id>/
    generated.py
    01_<item>.png
```

That's it. No memory file. No 错题集.
