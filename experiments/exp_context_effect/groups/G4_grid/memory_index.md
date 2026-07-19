# G4 memory index — entry point for the drawer

*Maintained by the curator. Drawer reads this file first every cycle,
then follows the pointers below (or explores the group directory
freely if you need to find something not listed).*

## Core format constraint (fixed — do not violate)

G4's memory uses **米字格 anchors + P/T/N/S joint spec**:
- Every stroke endpoint is `(cell, x_frac, y_frac)` where cell is one
  of TL, TC, TR, ML, C, MR, BL, BC, BR.
- Every joint declares its class: **P** (piercing, welded crossing),
  **T** (tangent, tip touches body), **N** (neighbor, small natural
  gap — do NOT weld), **S** (same-stroke internal corner).
- You may extend this within the format (sub-classes, sub-cell
  coords, multi-cell spans) but not abandon it. See
  `../protocol/G4_grid/rules.md` for the full constraint.

The dispatcher continues to auto-inject MMH-derived structural
expectations for every Phase-2/3 item into the drawer prompt. That
is separate from the memory files below.

## What memory G4 currently holds

- **`success_bank/INDEX.md`** — the master list of mastered items:
  which items are in the bank, which file, mastery batch/position.

- **`success_bank/code/`** — 米字格 anchor + joint spec per
  mastered item. Currently ~78 files (26 Phase-1 stroke primitives
  + `_anchor.py` helper + Phase-2 radicals mastered in bootstrap
  and B1).

- **`principle_bank.md`** — general rules learned across items.
  Currently ~429 lines containing:
  - Transformation rules TR1-TR12 (meta-cognitive + some geometric)
  - Standardized anchor convention
  - Joint convention definitions
  - Bezier control derivation
  - Sanity assertions
  - Phase-1 stroke family rules
  - "SELF_CHECK must be earned" (TR11)

- **`sandbox.md`** — persistent free-form scratch. Interim
  hypotheses, failure notes not yet a principle.

- **`errata.md`** — the 错题集. Failed items with structural + panel
  diagnosis, fix ideas, retry_n counter.

- **`scans/`** — per-position errata scan decisions.

- **`retry_log.jsonl`** — append-only retry log.

- **`curator_satisfaction_log.jsonl`** — per-attempt curator verdict
  (independent from human).

- **`evolution.md`** — append-only log of structural changes (created
  v7).

## When to consult what

- **Drawing an item**: MMH structural expectations are already in
  your prompt. First: check `success_bank/INDEX.md` for a bank
  primitive matching this or a related item. If yes, read the `.py`
  — but override its anchors for THIS composition (TR1).
- **Deciding whether to use the bank**: TR1-TR12 in
  `principle_bank.md`. If forcing extreme transformation, inline
  fresh (TR6).
- **Item has failed before**: `errata.md` for diagnosis + fix idea.
- **Joint pattern uncertainty**: search `principle_bank.md` for the
  joint class you're implementing (P/T/N/S).
- **Structural check writing**: TR11 in `principle_bank.md` — the
  SELF_CHECK dict must name specific PNG-vs-GT visual agreements,
  not just checkbox `visual_ok=True`.

## Change history

See `evolution.md` for the append-only log of structural changes.

---

*v7 initial version — created at position 150 as part of the memory
self-evolution unlock. Curator: update this index whenever you add,
remove, or restructure memory files.*
