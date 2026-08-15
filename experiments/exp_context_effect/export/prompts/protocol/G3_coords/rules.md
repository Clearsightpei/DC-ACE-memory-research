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

**v13 (2026-07-30, position 500) — drawer bank-deviation channel +
evidence-driven variants**. The bank is still immutable, but the
drawer explicitly owns the "use it or not" decision per attempt,
and successful deviations promote new variants:

- **Drawer may skip any bank entry** it judges unsuitable for the
  current composition. Bank primitives are what worked in a
  particular past context; the current character may want a
  different render of the same component (different orientation,
  size, aspect, weight, stroke-endpoint placement). The drawer
  reviews the bank entry against what the current GT demands and
  decides: use as-is, use with local transform, or ignore and
  inline a fresh render.
- **If the drawer deviates from bank, it MUST include a
  `BANK_DEVIATION` comment block** at the top of `generated.py`
  naming: (a) which bank entry was skipped or replaced, (b) what
  visual property motivated the deviation, (c) what fresh render
  was used instead. Format:

  ```python
  # BANK_DEVIATION
  # skipped: <bank_file.py>  (or "replaced: <bank_file.py> with local render")
  # reason: <one-sentence visual/compositional reason>
  # fresh_component: <name the fresh sub-element, e.g. "li_variant_for_加">
  ```

- **On human PASS**, the curator reads the `BANK_DEVIATION` note.
  If the deviation produced a fresh sub-element that a future
  composition would plausibly reuse, the curator may promote it as
  a **new bank entry** (variant) — e.g. `<name>_A.py`, `<name>_B.py`,
  or `<name>_for_<context>.py`. INDEX rows note which context
  motivated the variant. The **original bank entry stays
  untouched**. Variants only get created from evidence: a drawer
  tried it, a human PASSed it.

- Curator does NOT speculatively create variants. No variant
  without a passing attempt to back it.

Guard: the drawer should not skip bank entries carelessly. If the
bank entry looks basically right for the context, use it — variant
proliferation without cause bloats the bank. Deviation is for real
mismatch cases (visible orientation / proportion / aspect problem),
not stylistic preference.

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

## Coordinate storage format (v8 UNLOCKED, 2026-07-25)

The **storage unit** is a callable Python function. That is the only
mandatory constraint for G3 — it's what makes G3 distinct from G2
(free-form markdown) and G4 (grid anchors).

**Function signature is your choice.** Encode whatever knobs the
composition needs. `(ox, oy, scale)` is a starting example, not a
limit. If a stroke class needs `angle`, `curve_bow`, `taper_start`,
`taper_end`, `aspect`, orientation flags, or anything else — put those
in the signature. Curators are explicitly encouraged to grow the
signature vocabulary as observed variants demand.

Example (starter):

```python
# success_bank/code/yi.py — 一 (yi, "one") — the simple case
from heng import draw_heng

def draw_yi(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + -3 * scale, oy=oy + -21 * scale, scale=0.480 * scale)
```

Example (richer signature, when needed):

```python
# success_bank/code/pie_variant.py — a 撇 with tunable angle/curve/taper
def draw_pie(t, head, tail, angle_deg=None, bow_perp=0.10,
             taper_head_w=10, taper_tail_w=2):
    """head, tail = (x, y). angle_deg overrides implied angle if given."""
    ...
```

**Everything in the Success Bank and Principle Bank is REFERENCE
ONLY.** Nothing is strictly required. If the drawer thinks a stroke
needs adjusting — angle, curvature, taper, aspect, orientation,
proportion, anything — it adjusts. Bank primitives are examples of
what worked before, not templates to instantiate.

**No 米字格 anchors, no cell names, no joint-class labels.** Those
belong to G4. G3's differentiator is code-as-storage.

## Drawer role

1. **Read `memory_index.md` FIRST** — the curator maintains it as
   your entry point. It describes what memory files exist and when
   to consult each. Follow its pointers to specific files (e.g.
   `drawer_memory.md`, `principle_bank.md` or its split children,
   `form_catalog.md`, `success_bank/INDEX.md`, individual bank
   `.py` files), or explore the group directory freely.

   **v8 reminder**: bank primitives and principles are all
   REFERENCE ONLY. You are not required to call any bank function
   or follow any principle. If a stroke needs a different angle,
   taper, curve, or orientation than what the bank has — write it
   fresh. If the memory disagrees with the GT — trust the GT. The
   memory is what worked before, not what must work now.
2. Look at the GT PNG (characters only; strokes/radicals have none).
3. Write **only** `attempts/<item_id>/generated.py` and its output
   PNG. Do NOT create or modify anything under `success_bank/code/`.
   Those are locked until the Curator promotes them post-judgment.
   **(v13)** — before calling a bank primitive, briefly review it
   against what the current GT actually needs. If the bank
   primitive's geometry doesn't fit this composition (orientation,
   size, aspect, endpoint placement), you may skip it and inline a
   fresh render. If you do deviate, add a `BANK_DEVIATION` comment
   block at the top of `generated.py` naming what you skipped and
   why (see "Success Bank" section for the format). Don't skip
   carelessly — for stylistic preference, use the bank; skip only
   for real compositional mismatch.
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
- **(v13)** — check the top of `attempts/<item>/generated.py` for a
  `BANK_DEVIATION` block. If present, the drawer skipped or
  replaced a bank primitive and inlined a fresh render. If the
  fresh sub-element looks like something future compositions would
  plausibly reuse, promote it as a **variant** bank entry —
  `<name>_A.py`, `<name>_B.py`, or `<name>_for_<context>.py`. Add
  an INDEX row noting the motivating context. The original entry
  stays untouched.

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

## Free-form memory grant (v8, unlocked at position 350)

G3 now has a `groups/G3_coords/drawer_memory.md` file — same shape
as G2's. Curator may write anything there: prose observations,
tables, natural-language principles, sibling-pair notes, whatever.
Drawer reads it via `memory_index.md`.

**The architecture is now**:
- G2 = free-form markdown only.
- G3 = free-form markdown + code bank (functions as reference).
- G4 = free-form markdown + grid bank (anchors as reference).

G3 strictly *dominates* G2 in access: everything G2 has, plus a
code-based bank as additional reference. If G3 leads G2 in scores,
the code bank adds value beyond what free-form can express. If G3
matches G2, the code bank is neutral. If G3 loses to G2, the code
bank is a distraction. The comparison is now clean.

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
