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
├── sandbox.md                ← free-form persistent memory (freely writable)
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

**Free-form persistent memory.** Not restricted in format or content.
This is where you write **anything** you want to remember across cycles
that doesn't cleanly fit into the Principle Bank:

- Significant errors you made (what happened, what to watch for)
- Interim hypotheses you're testing
- Observations about specific characters/radicals that aren't yet a
  general rule
- Notes-to-self for what to try next time you see a similar item
- Anything else you find useful

Analogous to G2's `drawer_memory.md`. Persists across items — does
NOT reset. You may freely append, edit, or reorganize.

Distinct from the Success Bank (item-level mastery, locked until
human PASS) and from the Principle Bank (generalized rules).

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

1. **Read `principle_bank.md` FIRST — pay especially close attention
   to the top-of-file TRANSFORMATION RULES section (TR1-TR7)**.
   Then read `success_bank/INDEX.md`, `sandbox.md`, and any relevant
   `success_bank/code/*.py` files. **Every primitive you reuse from
   the bank must have `(ox, oy, scale)` deliberately chosen for THIS
   composition — never call with defaults.** Bank use is
   supplementary (per `../shared_rules.md`) — if no primitive fits
   without extreme transformation, inline the stroke fresh or draw
   the whole item fresh the way G1 would.
2. Look at the GT PNG (characters only; strokes/radicals have none).
3. Write **only** `attempts/<item_id>/generated.py` and its output
   PNG. Do NOT create or modify anything under `success_bank/code/`.
   Those are locked until the Curator promotes them post-judgment.
4. Run the script.
5. **Self-check + one revision** (Phases 2 & 3 — items with GT).
   Per the reflection step in `../shared_rules.md`:
   - Open your rendered PNG and the GT PNG side by side (visual
     comparison — G3's native format is numeric coords, but the
     self-check itself is visual + TR-compliance).
   - Ask: does it match the target's stroke count, silhouette,
     proportions? Would a fluent reader identify it? And: was each
     bank primitive call TR-compliant (`(ox, oy, scale)` chosen
     deliberately, not defaults)?
   - You MAY append a general observation to `sandbox.md` or
     `principle_bank.md` from this self-check (e.g. "curves at
     scale=0.4 render too flat — bump to 0.55"). No item-mastery
     claims (Curator territory, post-judgment).
   - If OK → submit. If not OK → revise `generated.py` once with
     adjusted coords / primitive choice / inline fresh, re-run,
     submit the new PNG. Only ONE revision. Final PNG is the
     submission.
   - **Phase 1 (strokes) skips this step** — no GT, single render.
6. Return the FINAL PNG.
7. If you discover a general technique or rule (not item-specific
   mastery), you MAY append it to `principle_bank.md` or `sandbox.md`
   during drawing.

## Curator role

Called after every attempt.

On **PASS**: 
- Write a new file `success_bank/code/<item>.py` with the coordinate
  form of the successful render.
- Append a row to `success_bank/INDEX.md`.
- Update `principle_bank.md` with any general rule you learned.
- The sandbox is persistent — do NOT reset it.

On **FAIL**: 
- Read the attempt + GT (if any). The human gave NO text feedback.
  Diagnose from vision alone.
- Update `sandbox.md` with the specific failure mode.
- Add the item to `errata.md`.
- Consider generalizable lessons for `principle_bank.md`.

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

## Memory self-evolution (v7, unlocked at position 150)

**You have permission to redesign how memory is organized within
G3's core constraint.** The initial three-bank layout (Success +
Principle + Sandbox) is a starting point; the research question is
whether AI agents can self-direct memory evolution, so we now give
you the tools to do it.

### What you may change

- **Create new memory files** with any names or structures
  (e.g. `form_catalog.md`, `radical_position_table.md`,
  `failure_patterns.md`, `stroke_variants/`, an entirely new bank
  category, etc.).
- **Restructure existing files** — split `principle_bank.md` by
  topic, merge redundant sections, reorganize `sandbox.md` into
  themed sub-files if that helps retrieval.
- **Retire unhelpful entries** — remove principles or sandbox notes
  that have not helped, or that duplicate content elsewhere. Do NOT
  silently delete; document in `evolution.md` (see below).
- **Reshape the drawer's entry point** — the drawer reads
  `memory_index.md` first every cycle. You (curator) own that file
  and decide what pointers, summaries, or query aids it contains.
- **Reorganize the Success Bank** — you may add subdirectories
  (e.g. `success_bank/code/strokes/`, `success_bank/code/radicals/`,
  `success_bank/code/left_position/`) and update `INDEX.md` to
  reflect the new organization.

### What remains fixed (G3's core constraint — do NOT change)

- **Memory storage unit is callable Python functions**. The Success
  Bank contains `.py` files defining `def draw_<item>(t, ox=0, oy=0,
  scale=1.0)` (or similar callable form). If you rewrite this as
  free-form markdown or as 米字格 anchor tuples, G3 becomes G2 or
  G4 and the comparison is invalidated.
- **No 米字格 anchors** (still enforced from the original constraints).

Within the "callable Python" constraint, you have wide latitude:
you may design new function signatures (e.g. adaptive width/taper
args), new parameterization schemes, new composition APIs. What
you may not do is abandon the callable-function unit.

### Logging structural changes

Every time you (curator) create a new file, delete a file, or
substantially restructure an existing file / bank, append one entry
to `groups/G3_coords/evolution.md`:

```markdown
## 2026-07-18 @ position 152 — split principle_bank.md into topic files

**Files changed**: split `principle_bank.md` into
`principles_transformation.md`, `principles_hooks.md`,
`principles_composition.md`. Updated `memory_index.md` to point
drawers at the right file per stroke class.

**Rationale**: principle_bank hit 287 lines in v6; drawers were
grepping for their topic and often missing relevant principles.
Topic-split should reduce retrieval failure.

**Expected help for**: any item where a specific principle exists
but was previously buried in a wall of unrelated principles.
```

This log is the **emergence record** — the paper analyzes what
memory structure G3 converges on and how it correlates with
accuracy.

### Drawer's memory-reading (v7 change)

The drawer's prompt no longer lists specific memory files to read.
Instead: "Read `groups/G3_coords/memory_index.md` first — it
describes what memory exists and when to consult each file. Follow
its pointers, or explore the group directory freely."

You (curator) are responsible for keeping `memory_index.md` current
after any structural change.
