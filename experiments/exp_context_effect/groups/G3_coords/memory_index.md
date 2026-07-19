# G3 memory index — entry point for the drawer

*Maintained by the curator. Drawer reads this file first every cycle,
then follows the pointers below (or explores the group directory
freely if you need to find something not listed).*

## Core format constraint (fixed — do not violate)

G3's memory unit is **callable Python functions**. The Success Bank
contains `.py` files defining functions of the form:
```python
def draw_<item>(t, ox=0, oy=0, scale=1.0):
    ...  # calls to sub-primitives OR inline PIL / turtle rendering
```
You may design new function signatures (adaptive width, taper args,
etc.), but you may not abandon the callable-function unit. See
`../protocol/G3_coords/rules.md` for the full constraint.

## What memory G3 currently holds

- **`success_bank/INDEX.md`** — the master list of mastered items:
  which items are in the bank, which file, mastery batch/position.

- **`success_bank/code/`** — one `.py` file per mastered item.
  Currently ~67 files (25 Phase-1 stroke primitives from before v6
  restart + Phase-2 radicals mastered in bootstrap and B1). Each
  function is intended for compositional reuse (call from a
  higher-level item's rendering).

- **`principle_bank.md`** — general rules learned across items.
  Currently contains:
  - Transformation rules TR1-TR9 (meta-cognitive: how to reuse a
    primitive as a component)
  - Phase-1 principles P1-P10 (stroke-family observations)
  - "Bank is supplementary" clause
  - TR8 "INLINE-FRESH TEST" (added at B1, response to G3
    underperformance)

- **`sandbox.md`** — persistent free-form scratch. Interim
  hypotheses, failure notes not yet a principle.

- **`errata.md`** — the 错题集. Failed items with per-item diagnosis,
  fix ideas, retry_n counter.

- **`scans/`** — per-position errata scan decisions.

- **`retry_log.jsonl`** — append-only retry log.

- **`curator_satisfaction_log.jsonl`** — per-attempt "would-I-stop?"
  verdicts (calibration data).

- **`evolution.md`** — append-only log of structural changes to
  memory organization (created v7).

## When to consult what

- **Drawing an item**: check `success_bank/INDEX.md` first to see
  if there's a bank primitive for this or a closely related item.
  If yes, read that `.py` file and consider reuse (TR1-TR8
  transformation rules apply — DO NOT call with default parameters).
- **Deciding whether to use the bank at all**: read the "Bank is
  supplementary" section and TR8 "INLINE-FRESH TEST" in
  `principle_bank.md`. If forcing a primitive would require extreme
  transformation, inline fresh.
- **You've seen this exact item fail before**: check `errata.md` for
  the diagnosis and fix idea.
- **General stroke-family knowledge**: `principle_bank.md` P1-P10.

## Change history

See `evolution.md` for the append-only log of structural changes.

---

*v7 initial version — created at position 150 as part of the memory
self-evolution unlock. Curator: update this index whenever you add,
remove, or restructure memory files.*
