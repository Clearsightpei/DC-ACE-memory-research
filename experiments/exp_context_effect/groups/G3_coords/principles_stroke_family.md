# Principles — STROKE-FAMILY observations (G3 coord-bank)

*Created 2026-07-18 (v7 self-evolution). Split from monolithic
`principle_bank.md`. These are general observations about how
strokes render — width profiles, hook conventions, math conventions.
For meta-rules (how to use the bank) see `principles_meta.md`.
For stroke-in-context form lookup see `form_catalog.md`.*

## P1. Hook (钩) direction matters more than length

- 竖钩's hook flicks UP-AND-LEFT from the shaft's base.
- 弯钩's hook flicks UP-AND-LEFT from the arc's bottom.
- 卧钩's hook flicks UP-AND-LEFT from the arc's rightmost point.
- 斜钩's hook rises nearly VERTICALLY (slightly leftward) from the
  tail.
- 横斜钩's hook flicks UP-AND-LEFT from the diagonal's bottom-right end.
- A blob or downward spike at the tail = failure. The hook must be a
  visibly tapered short line pointing UP (with a slight leftward lean
  in most cases), joining smoothly with the previous segment.

## P2. Prefer PIL ImageDraw over turtle+PostScript

Turtle scripts that use `canvas.postscript()` and then PIL-resize can
blur or lose fine features (especially small hooks). Direct PIL is
cleaner at 300×300.

## P3. Tapered lines beat rectangular polygons

Stroke shafts drawn as tapered `line` segments (or stamped-circle
sequences with a width ramp) read as calligraphic ink. Shafts drawn
as polygons with separate ellipse caps read as mechanical shapes.
Rule: no matter the stroke, model the ink as a spine + a width
profile, never as a hollow polygon.

## P4. Width profiles are stroke-specific

Empirically-passing width profiles:
- 横: uniform ~12 px.
- 竖: uniform ~12 px.
- 撇: thick head (~10) → needle tip (~1), monotonic taper.
- 捺: thin head (~2) → belly (~18 at u=0.7) → tapered foot (~3).
- 点: thin head (~3) → heavy rounded tail (~14).
- 提: thick pressed head (~16 for first 10%) → needle tip (~1).
- 弯钩 arc body: 6 → 10 (u=0.55) → 5. Hook: 5 → 2.
- 卧钩 body: 3 → 11 (thickens down-right). Hook: 10 → 3.

## P5. Coord math convention

Origin at canvas center, +y up (math convention). Every primitive
converts internally via `_to_pixel(ox, oy) -> (cx+ox, cy-oy)`.

## P6. Compound strokes = concatenated tapered segments + a corner blob

For 横折, 竖折, 撇折, 横撇, 横钩, 竖提, 横斜钩, 撇点, 橫折提:
- Two-or-three straight (or shallowly curved) tapered segments joined
  at a common corner point.
- A small filled ellipse at the corner (顿笔) hides the miter.
- Keep segment endpoints numerically identical at the join.

## P7. Radicals ARE strokes when shape matches

When a 1-画 radical is orthographically identical to a mastered
stroke (e.g. 丨↔shu, 一↔heng, 丶↔dian, 乛↔heng_gou), calling the
bank primitive with `(ox=0, oy=0, scale=1.0)` is the correct first
move. Verify visual match to GT first — if the radical form has a
shallower slope, thicker head, or softer curl (see P10), build a
variant.

## P8. Multi-fold zig-zag strokes fail without curved final segments

Pure-orthogonal drawings of 横折折, 横折弯, 竖折折钩, 横折折折钩 tend
to fail. Passes come from introducing a curved segment somewhere.
Any label containing 弯 requires a real quarter-circle arc. Any
折折钩 needs the terminal shaft to end below the horizontal so the
hook has room to flick upward.

## P9. Hook belongs on the SHAFT, not on the corner

The hook must share pixels with the last few px of the shaft. If the
shaft is too short, extend it before adding the hook, otherwise the
hook reads as a floating triangle stuck to a lollipop.

## P10. 撇 vs. 丿 vs. diagonal: pie primitive is TOO diagonal for 丿

The 撇 (pie) primitive passed as a stroke but FAILED as the 丿
radical because 丿 in radical form has a shallower slope, thicker
head, and softer curl. When a radical is nominally the same stroke,
check curvature and slope against the target label, not just the
stroke name.

## P11. NEW (v7): stroke FORMS vary with context — memory must expose knobs

**Added 2026-07-18 in response to B2 collapse. This is the central
lesson of G3's underperformance.**

Bank primitives store one frozen concrete instance per stroke. In a
new composition, the same-labeled stroke often needs different:
- **angle** (a 撇 in top-of-radical position leans differently than a
  standalone 撇)
- **taper** (short compact 撇 has different w_head/w_tail than long
  sweeping 撇)
- **curvature** (envelope 撇 in 户 bows differently than a crossing
  撇 in 大)
- **length proportion** (aspect ratio needed for 日 vs 口)

**Response**: use adaptive helpers `variant_pie(head, tail, bow_perp,
w_head, w_tail)` / `variant_na(...)` / `variant_dian(...)` from
`success_bank/code/_shared_helpers.py`. Look up the specific
angle/taper/bow to use in `form_catalog.md` (indexed by stroke ×
context).

Do NOT force-fit a scaled bank primitive when the target stroke has
a genuinely different form. And do NOT re-derive the entire bezier
from scratch every time — use the variant helper with the
form-catalog numbers as a starting point.
