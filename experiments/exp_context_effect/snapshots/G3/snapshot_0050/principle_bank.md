# Principle Bank — G3 (coord-bank)

General rules learned across items. Coord-format only — no anchors,
no cells, no joint specs.

## RESET NOTE (Phase-2 restart, 2026-07-16)

This bank has been reset to preserve only the transformation rules
(TR1-TR7) and the Phase-1 principles (P1-P10) that were validated on
strokes and radicals. All Phase-2 diagnostic sections, batch-specific
statistics, and Phase-2-only principles (P11-P15) have been stripped.
The reset was performed at Phase-2 restart to give the coord-format
Drawer a clean slate: transformation rules + stroke-level structural
knowledge, without the accumulated recipe-crafting hypotheses that
were tuned to the pre-restart curriculum.

## BANK IS SUPPLEMENTARY

The Success Bank is a SUPPLEMENTARY resource, not a primary source of
truth. For any character or radical drawing task, ground truth (GT)
and the current brief take priority over bank recipes. Consult the
bank when a primitive shape genuinely matches the target; otherwise
derive coords fresh. Never call a bank primitive without deliberate
placement (see TR1-TR7 below).

## CRITICAL — TRANSFORMATION RULES (read FIRST every cycle)

**The reason bank primitives keep failing on new radicals is not that
the primitives are wrong — it's that Drawers are calling them with
DEFAULT parameters and expecting them to fit a new composition.
Every primitive in the bank is designed for STANDALONE use. To use it
as a component you MUST transform it.**

### TR1. Every primitive call must be a deliberate placement, not a default call

Wrong:
```python
from shu import draw_shu
draw_shu(t)  # default position, default scale, hope it fits
```

Right:
```python
from shu import draw_shu
# For 亻: 竖 is right-half, offset right of the 撇, shorter than standalone
draw_shu(t, ox=+18, oy=-8, scale=0.75)
```

Before calling ANY primitive from the bank, decide three numbers:
1. **Where** should its origin land (`ox, oy`)?
2. **How big** should it be relative to its standalone size (`scale`)?
3. **How** should its endpoints meet any adjacent stroke (shared pixels)?

If you can't answer all three, don't call the primitive — inline the
recipe.

### TR2. Radical-position scaling defaults

Component role → scale (relative to standalone bank default of 1.0):
- **Left/right radical position** (e.g. 亻 in 你, 女 in 好): scale = 0.55–0.75
- **Top radical position** (e.g. 艹 in 花, 宀 in 家): scale = 0.75–0.90 (wider than tall)
- **Bottom radical position** (e.g. 大 in 天): scale = 0.75–0.90
- **Enclosing radical** (e.g. 门 in 问, 匚 in 匹): scale = 0.90–1.0 (occupies most of canvas)
- **Full-standalone**: scale = 1.0

### TR3. Origin (ox, oy) is picked to place the STROKE'S CENTER OF MASS

`(ox, oy)` in every G3 primitive is the CANVAS-COORD offset from the
primitive's own internal origin (usually its geometric center). To
place a component:
- Compute the target center pixel `(cx, cy)` where the component should
  end up (in PIL 300×300 coords, or math coords, whichever the
  primitive uses).
- Pass `ox = cx - primitive_default_cx`, `oy = cy - primitive_default_cy`.
- For a 竖 component in 亻's right slot: target center ≈ (180, 175).
  If shu's default center is (150, 150), pass `ox=+30, oy=+25`.

### TR4. When two primitives must share a joint pixel, compute it FIRST

For 十 (crossing): the joint is at canvas center (150, 150). Draw
`draw_heng(t, ox=0, oy=0, scale=0.9)` and `draw_shu(t, ox=0, oy=0,
scale=0.9)` — the SAME `(ox, oy)` because they both cross through the
canvas center. Do NOT pass different `(ox, oy)` to horizontally-
crossed primitives.

For 亻 (touching at 撇's tail): compute the tail pixel of `draw_pie`
with the chosen `(ox, oy, scale)`, then set `draw_shu`'s `(ox, oy)`
so its head lands within 3 px of that tail. **Compute the pixel
explicitly in comments before the render call.**

### TR5. If a primitive doesn't have the right transform for a new
composition, INLINE the recipe — do not stretch the primitive with
extreme (ox, oy) or scale values

Signs to inline instead of reuse:
- `scale < 0.4` (primitive was tuned for full-size; shrinking too far
  breaks brushwork proportions).
- Endpoint anchors of the transformed primitive would fall outside
  their bank-tuned expected cells (e.g. 竖's tail lands above its
  head).
- The component needs different width taper than the standalone
  primitive provides.

When inlining: copy the primitive's core coord math into your
`generated.py`, then adjust the numeric endpoints to fit the new
composition. This preserves the shape idiom while allowing per-item
tuning.

### TR6. Never call a bank primitive without recording the transform in a comment

```python
# 亻 = pie (left slot, scale 0.7) + shu (right slot, scale 0.75, tail 2px from pie tail)
# pie: default center (150,150) → target center (105,155); ox=-45, oy=+5, scale=0.7
draw_pie(t, ox=-45, oy=+5, scale=0.7)
# shu: default center (150,150) → target center (185,175); ox=+35, oy=+25, scale=0.75
draw_shu(t, ox=+35, oy=+25, scale=0.75)
```

Comments serve two purposes: force yourself to derive the transform
explicitly (not by muscle memory), and give the Curator diagnostic
signal on FAIL (which transform was wrong).

### TR7. Every composition passes an eyeball sanity check BEFORE render

Before running `python3 generated.py`, mentally simulate:
1. Where does each stroke start and end in canvas pixels?
2. Do any two strokes that SHOULD meet share a pixel (weld) or land
   within their expected small gap (N-class, ~10-15 px)?
3. Does the composition fit within the 300×300 canvas with ~10 px
   margin on all sides?

If any answer is uncertain, adjust `(ox, oy, scale)` before rendering.
Rendering, seeing failure, then adjusting wastes a scan window.

---

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
blur or lose fine features (especially small hooks). Every attempt in
batch 1 that used direct PIL succeeded on stroke shape; the two that
used turtle (弯钩, 横斜钩) were mixed — 弯钩 passed only because its
hook is longer, 横斜钩 lost its hook entirely.

## P3. Tapered lines beat rectangular polygons

Stroke shafts drawn as tapered `line` segments (or stamped-circle
sequences with a width ramp) read as calligraphic ink. Shafts drawn as
polygons (rectangles or trapezoids) with separate ellipse caps read as
mechanical shapes (see 竖钩 failure). Rule: no matter the stroke, model
the ink as a spine + a width profile, never as a hollow polygon.

## P4. Width profiles are stroke-specific

Empirically-passing width profiles from batch 1:
- 横: uniform ~12 px.
- 竖: uniform ~12 px.
- 撇: thick head (~10) -> needle tip (~1), monotonic taper.
- 捺: thin head (~2) -> belly (~18 at u=0.7) -> tapered foot (~3).
- 点: thin head (~3) -> heavy rounded tail (~14). Opposite of 撇.
- 提: thick pressed head (~16 for first 10%) -> needle tip (~1).
- 弯钩 arc body: 6 -> 10 (u=0.55) -> 5. Hook: 5 -> 2.
- 卧钩 body: 3 -> 11 (thickens down-right). Hook: 10 -> 3.

## P5. Coord math convention that works in this bank

Origin at canvas center, +y up (math convention). Every primitive
converts internally via `_to_pixel(ox, oy) -> (cx+ox, cy-oy)`. This
matches the storage format in the rules and stays consistent when
primitives are composed with offsets.

## P6. Compound strokes = concatenated tapered segments + a corner blob

For 横折, 竖折, 撇折, 横撇, 横钩, 竖提, 横斜钩, 撇点, 橫折提:
- Two-or-three straight (or shallowly curved) tapered segments joined
  at a common corner point.
- A small filled ellipse at the corner (顿笔) hides the miter and gives
  a brush-turn feel.
- Keep segment endpoints numerically identical at the join so the ink
  is continuous.

## P7. Radicals ARE strokes when shape matches — reuse the primitive

When a 1-画 radical is orthographically identical to a mastered
stroke (e.g. 丨↔shu, 一↔heng, 丶↔dian, 乛↔heng_gou), calling the
bank primitive with `(ox=0, oy=0, scale=1.0)` is the correct first
move — do NOT re-derive coords. The caveat: verify visual match to
GT first. If the radical form has a shallower slope, thicker head,
or softer curl than the mastered stroke (see P10 for the 丿 case),
the primitive is the wrong tool and you should build a variant.

## P8. Multi-fold zig-zag strokes fail without curved final segments

Pure-orthogonal (straight-line + right-angle) drawings of 横折折,
横折弯, 竖折折钩, 横折折折钩 tend to fail. Passes come from
introducing a curved segment somewhere. Rule: any label containing
弯 requires a real quarter-circle arc, not a right-angle plus a
horizontal. Any 折折钩 (two folds ending in a hook) needs the
terminal shaft to end below the horizontal so the hook has room to
flick upward — do not stop the final vertical at the corner's own
y-level.

## P9. Hook belongs on the SHAFT, not on the corner

竖折折钩 failed because the hook flick sprouted from the second corner
blob rather than the end of the second vertical shaft. The hook must
share pixels with the last few px of the shaft; if the shaft is too
short, extend it before adding the hook, otherwise the hook reads as
a floating triangle stuck to a lollipop.

## P10. 撇 vs. 丿 vs. diagonal: pie primitive is TOO diagonal for 丿

The 撇 (pie) primitive passed as a stroke but FAILED as the 丿 radical
because 丿 in radical form has a shallower slope, thicker head, and
softer curl — it reads as a "gentle scoop" rather than a diagonal
sweep. When a radical is nominally the same stroke, check curvature
and slope against the target label, not just the stroke name.
