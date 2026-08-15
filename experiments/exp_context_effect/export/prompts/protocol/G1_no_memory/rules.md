# G1 — No-Memory Control

## Overview

You are the **G1 (control)** group. You do not have a curator. You do
not have a memory. Each item you draw is drawn "cold" with only:

- Its target label (name or character)
- Its GT PNG (300×300)
- The shared stroke primitives at `success_bank/code/*.py`

## Attempt policy (unique to G1)

- **Phase 1 (strokes): exactly 1 attempt per item.** No revision
  (no GT to compare against). No errata retries.
- **Phase 2 (radicals) & Phase 3 (characters): 1 first render + 1
  within-item revision** — per the reflection step in
  `../shared_rules.md`. Reflection is a within-item act (comparing
  your PNG against the GT), not memory across items — nothing
  persists between items. G1 does NOT participate in 错题集 retries
  (no memory → cross-item retries would just re-roll).
- G1's headline numbers: *one-shot accuracy* in Phase 1, *final
  accuracy after one revision* in Phases 2 & 3.

Reason: giving G1 cross-item retries would contaminate the "no
memory" contrast. But a single within-item revision when a GT is
available is not memory — it is the same reflective act G2/G3/G4
also perform. Withholding it would confound "memory vs no memory"
with "reflection vs no reflection".

## Phase-2 / Phase-3 self-check (visual comparison — G1 format)

After your first render, before submitting:

1. Open your `01_<label>.png` and the GT PNG at
   `gt/phase2/<char>.png` (radicals) or `gt/phase3/<char>.png` (characters).
2. Ask: does the render look like the target? Same stroke count?
   Same rough proportions? Same silhouette? Would a fluent Chinese
   reader identify it as this radical / character?
3. If yes → keep and submit.
4. If no → revise `generated.py` once (adjust proportions, add /
   remove strokes, fix orientation, brushwork, etc.), re-run, submit
   the new PNG.

You do NOT need to log the self-check (G1 has no memory to log to).
Make the decision, act, submit. Only the FINAL PNG is kept.

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
