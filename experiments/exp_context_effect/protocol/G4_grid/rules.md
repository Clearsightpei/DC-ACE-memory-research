# G4 — Grid-Bank Memory (米字格)

## Overview

You are the **G4 (grid-bank)** group. You have a curator and a
**three-bank memory** with **米字格 (grid) anchor notation** and joint
specifications. This is the run_6 architecture.

Read this together with `../shared_rules.md`.

## The three-bank architecture

```
groups/G4_grid/
├── success_bank/
│   ├── INDEX.md
│   └── code/
│       ├── yi.py            ← draw_yi(t)  — using 米字格 anchors
│       ├── kou.py
│       └── ...
├── principle_bank.md         ← generalized rules (freely writable)
├── sandbox.md                ← free-form persistent memory (freely writable)
├── errata.md                ← 错题集
├── retry_log.jsonl
├── curator_satisfaction_log.jsonl
└── attempts/
    └── <item_id>/generated.py, 01_<item>.png
```

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

## 米字格 anchor notation (MANDATORY)

The character region is divided into **9 cells** (`TL`, `TC`, `TR`,
`ML`, `C`, `MR`, `BL`, `BC`, `BR`). Every stroke's endpoints are
recorded as `(cell, x_frac, y_frac)` — cell name plus within-cell
position. Example:

```python
# success_bank/code/kou.py — 口 (kou, "mouth")
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng

def draw_kou(t):
    draw_shu(t, ('ML', 0.368, 0.212), ('BL', 0.844, 0.94))
    draw_heng_zhe(t, ('ML', 0.668, 0.272), ('MR', 0.488, 0.312), ('BR', 0.096, 0.456))
    draw_heng(t, ('BL', 0.928, 0.808), ('BR', 0.428, 0.652))
```

Anchor helper: `_anchor.anchor_to_xy((cell, x_frac, y_frac))` returns
turtle math-coords. This helper is available under the shared
primitives.

## Joint specs (part of memory)

Every entry in the Success Bank includes a **joint list** describing
where strokes meet, using the P/T/N classification:

- **P (Piercing)** — two strokes cross (e.g. 十 crossing).
- **T (Tangent)** — one stroke's tip touches another's body.
- **N (Neighbor)** — two strokes end near each other with a small
  natural gap (e.g. 口's non-welded corners).

The joint list can be represented inline in the docstring or as a
separate section in each `.py`. Example:

```python
# 口 joints:
#   stroke1.tail @ BL  ⇆  stroke2.corner @ BR   (P — welded)
#   stroke2.tail @ BR  ⇆  stroke3.head @ BL     (N — small gap OK)
#   stroke1.head @ ML  ⇆  stroke2.head @ ML     (N — small gap OK)
```

## Drawer role

1. **Read `principle_bank.md` FIRST — pay especially close attention
   to the top-of-file TRANSFORMATION RULES section (TR1-TR8)**.
   Then read `success_bank/INDEX.md`, `sandbox.md`, and relevant
   `success_bank/code/*.py`. **Every primitive you reuse from the
   bank must have OVERRIDING anchor tuples chosen for THIS
   composition — never call primitives with their default anchors.**
   Bank use is supplementary (per `../shared_rules.md`) — if no
   primitive fits without extreme transformation, inline the stroke
   fresh (still in 米字格 anchor form) or draw the whole item fresh
   the way G1 would.
2. Look at the GT PNG (characters only; strokes/radicals have none).
3. Write **only** `attempts/<item_id>/generated.py` and its output
   PNG. Do NOT create or modify anything under `success_bank/code/`.
   Those are locked until the Curator promotes them post-judgment.
4. Run the script.
5. **Dual self-check + one revision** (Phases 2 & 3 — items with GT).
   Per the reflection step in `../shared_rules.md`. You perform
   **BOTH** a visual check and a structural check:

   **(a) Visual check** (same as G1/G2/G3): open your rendered PNG and
   the GT PNG side by side. Ask: same silhouette, same stroke count,
   same proportions, would a fluent reader identify it as this
   radical / character?

   **(b) Structural check** (unique to G4): when the brief includes
   an "MMH-derived structural expectations" block (Phases 2 and 3 —
   the dispatcher auto-injects for both):
   - Verify `generated.py` produces exactly the expected stroke count.
   - Compare each stroke's actual head/tail anchor against the
     expected anchor (tolerance: same cell OR immediately adjacent
     cell; ±0.20 in x_frac/y_frac).
   - For every declared joint, confirm the class you implemented
     matches the expected P/T/N class. Welding an N-class joint is a
     defect; leaving a gap on a P-class joint is a defect.
   - Log the outcome as a `SELF_CHECK = {...}` dict at the top of
     `generated.py` (schema in the brief). Include a `visual_ok`
     boolean field alongside the structural fields, and set
     `overall_pass = visual_ok AND structural fields all OK`.

   **Decision**:
   - If both checks pass → submit.
   - If either check fails → **revise `generated.py` once**, re-run,
     submit. **Only ONE revision.** Even if the second self-check
     still fails, submit the second render. Append a one-line entry
     to `sandbox.md` naming what remained mismatched.

   **Phase 1 (strokes) skips this step** — MMH does not cover
   strokes and there is no GT to reflect against.
6. Return the FINAL PNG.
7. If you discover a general technique or rule (not item-specific
   mastery), you MAY append it to `principle_bank.md` or `sandbox.md`
   during drawing.

## Curator role — merged structural + panel check

Called after every attempt.

Your judgment logic **combines** what were three separate agents in
run_6 (structural checker + 3 panel skeptics) into a single call:

1. **Structural check**: does the render's stroke count match MMH?
   Do the declared anchors land in the right cells (within tolerance)?
   Do the joint classes look right visually?
2. **Panel-skeptic check**: viewing the attempt alone, would you
   identify it as the target item? Would you accept it as a "correct"
   render given calligraphic norms?
3. Emit a single PASS/FAIL verdict with a one-sentence reason.

This is logged to `curator_satisfaction_log.jsonl`. **It is NOT the
gate.** The human's verdict is the gate. Your verdict is used for
post-hoc calibration analysis.

On **human PASS**:
- Write `success_bank/code/<item>.py` with 米字格 anchors + joint
  spec.
- Append to `success_bank/INDEX.md`.
- Update `principle_bank.md`.
- The sandbox is persistent — do NOT reset it.

On **human FAIL**:
- Human gave NO text feedback. Use your structural + panel diagnostic
  to identify the specific defect (stroke count mismatch, wrong cell,
  bad joint class, etc.).
- Update `sandbox.md` with the specific fix idea.
- Add the item to `errata.md` so it may be re-attempted after 20 more
  curriculum items.

## 错题集

Standard rules — see `../shared_rules.md`.

## Explicit constraints

- You may NEVER use raw coordinate offsets like `(ox + 3, oy - 21)`.
- You must use `(cell, x_frac, y_frac)` anchor tuples.
- You must declare joint classes for multi-stroke items.
- Your Success Bank entries must be compositional: complex characters
  reuse component characters/radicals from the bank where possible.

## Memory self-evolution (v7, unlocked at position 150)

**You have permission to redesign how memory is organized within
G4's core constraint.** The initial three-bank layout (Success +
Principle + Sandbox) is a starting point; the research question is
whether AI agents can self-direct memory evolution, so we now give
you the tools to do it.

### What you may change

- **Create new memory files** with any names or structures
  (e.g. `form_catalog.md` indexing form/position rules per stroke
  class × context, `joint_atlas.md` for typical P/T/N patterns,
  `radical_position_rules.md`, entirely new bank categories, etc.).
- **Restructure existing files** — split `principle_bank.md` (currently
  429 lines) by topic, merge redundant sections, reorganize
  `sandbox.md`.
- **Retire unhelpful entries** — remove principles that have not
  helped or that duplicate content. Do NOT silently delete; document
  in `evolution.md` (see below).
- **Reshape the drawer's entry point** — the drawer reads
  `memory_index.md` first every cycle. You (curator) own that file
  and decide what pointers, summaries, or query aids it contains.
- **Reorganize the Success Bank** — subdirectories, categorized
  INDEX.md, whatever structure helps drawers retrieve the right
  primitive.

### What remains fixed (G4's core constraint — do NOT change)

- **Memory storage uses 米字格 anchors + P/T/N/S joint spec**. All
  bank entries reference stroke endpoints as `(cell, x_frac, y_frac)`
  tuples; all multi-stroke items declare joint classes. If you
  rewrite entries as raw pixel coords or as free-form markdown, G4
  becomes G3 or G2 and the comparison is invalidated.
- **No raw coordinate offsets** (still enforced from the original
  constraints).

Within the grid + joint constraint, you have wide latitude: you may
add new joint sub-classes (e.g. differentiating N-wide vs N-narrow
gaps), new anchor-notation extensions (e.g. sub-cell coordinates,
multi-cell spans), new principle indexing schemes. What you may not
do is abandon the grid + joint core.

### Logging structural changes

Every time you (curator) create a new file, delete a file, or
substantially restructure an existing file / bank, append one entry
to `groups/G4_grid/evolution.md`:

```markdown
## 2026-07-18 @ position 152 — created form_catalog.md indexed by stroke×context

**Files changed**: created `form_catalog.md`; moved principle_bank
sections describing per-context form rules (撇 in left-position, 竖
in enclosing radical, etc.) into it. Kept meta-rules (TR1-TR12) in
principle_bank.

**Rationale**: principle_bank had grown to 429 lines mixing
meta-cognitive rules (when to use bank vs inline) with actual
calligraphy knowledge (form/position rules). Drawers were reading
the meta-rules but missing the calligraphy rules. Splitting by
knowledge type should surface form/position rules directly.

**Expected help for**: contextual stroke variants — chars where the
same stroke class (e.g. 撇) appears in different positions and
should look different.
```

This log is the **emergence record** — the paper analyzes what
memory structure G4 converges on.

### Drawer's memory-reading (v7 change)

The drawer's prompt no longer lists specific memory files to read.
Instead: "Read `groups/G4_grid/memory_index.md` first — it describes
what memory exists and when to consult each file. Follow its
pointers, or explore the group directory freely."

You (curator) are responsible for keeping `memory_index.md` current
after any structural change. The MMH-derived structural expectations
block continues to be auto-injected into the drawer prompt for every
Phase-2 and Phase-3 item — this is dispatcher-level and separate
from the memory files you control.

## Reference materials

Predecessor run_6 established these conventions:

- 米字格 cell definitions: `runs/run_6/success_bank/code/_anchor.py`
- Joint classification (P/T/N) with MMH-derived thresholds:
  `runs/run_6/tools/classify_joints.py`
- Corner-cell rule for compound-stroke bends: `runs/run_6/MMH_ROLE.md`
- Deterministic structural judge: `runs/run_6/tools/structural_judge.py`
  (calibrated to 85.5% human agreement)

You may reference these files for the definitions but do NOT copy
run_6's mastered entries into your Success Bank. **G4 starts empty**
per the experiment's fair-comparison rule.
