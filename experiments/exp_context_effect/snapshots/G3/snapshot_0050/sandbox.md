# Sandbox — G3 (coord-bank)

Sandbox reset with Phase-2 restart. Persistent free-form memory — use
for observations that don't cleanly fit the Principle Bank.

## Carry-over notes from Phase-1

- All stroke primitives assume a 300x300 canvas and math-coord
  convention (center origin, +y up). If drawing on a different canvas,
  either compose on a fresh 300x300 and paste, or refactor `_to_pixel`
  to accept canvas size.
- `heng.py`, `shu.py`, `pie.py`, `na.py`, `dian.py`, `ti.py` are the
  cleanest bank entries — pure single-line or single-bezier
  definitions. Prefer these as composition primitives.

## Bootstrap batch (2026-07-17) — failure-mode analysis

Four radicals from bootstrap batch (positions 33–50) failed. Common
thread: **rounded, continuous, enclosing shapes** modeled with
straight-line + right-angle recipes. Coord-format bank has no arc
primitive, and drawers keep reaching for `heng` + `shu` + hook when
the target is one continuous curved envelope.

### p2_radical_010_勹 (bao) — FAIL

- Attempt: separate 撇 + 横折钩 rendered with SHARP right-angle corner.
- GT: one continuous smooth rounded envelope (like a bag). The
  horizontal top and the descending stroke are joined by a rounded
  arc, NOT a right angle. The 撇 head sits well left of the top.
- Failure mode: the bank's `heng_zhe_gou` primitive was rejected as
  "aspect mismatch", then a right-angle inlined recipe was used —
  losing exactly the roundedness that makes 勹 read as 勹.
- Fix for retry: draw the 横+折+钩 as ONE bezier (top-left horizontal
  head, smoothly curving down through the top-right shoulder, then
  descending vertically with slight leftward bow, ending in a
  hook). No sharp corner. See errata.

### p2_radical_011_匕 (bi) — FAIL

- Attempt: pie + shu_wan_gou. The pie crossed the shaft.
- GT: the vertical of 匕 has a strong horizontal-bottom (a proper
  竖弯 with long horizontal foot then hook up) — this the render
  captured. But the top of 匕 needs a 撇 that starts high-left,
  descends to meet the shaft, THEN a short horizontal 提 shoots
  up-right OFF the shaft. The render has 撇 crossing shu_wan_gou
  ABOVE the shaft top — reads as `匕` broken up top.
- Failure mode: 匕 is 撇 + 竖弯钩 where the pie ENDS at the shaft
  (joint), and the top-right "提" is really the head of the 竖弯钩
  (short pointed head before it descends). No composition in the
  bank captures this junction.
- Fix: shorten pie, land its tail on the shu_wan_gou shaft top; make
  shu_wan_gou's shaft top slightly rightward-scooping so it reads as
  the crossing arm. See errata.

### p2_radical_014_厂 (chang) — FAIL

- Attempt: heng shifted right + inline "pie" that curved as an arch
  going UP-then-LEFT (like a shepherd's crook). Result reads as ONE
  curving shape, not 厂.
- GT: a plain flat horizontal at the top + a straight-ish pie
  descending straight down from the LEFT end (only slight curl at
  the bottom). Two distinct strokes with a hard corner-join.
- Failure mode: the drawer picked a bezier control point that pulled
  the pie head LEFT of the heng end and DOWN, creating an arc
  instead of a mostly-vertical straight descent.
- Fix: reuse `heng` at scale ~0.65 centered high; draw pie as almost-
  vertical with only a shallow scoop near the tail (control point on
  the chord's midpoint, not offset left). Head anchored at heng's
  left end (weld). See errata.

### p2_radical_015_刀 (dao) — FAIL

- Attempt: heng_zhe_gou (right side) + pie (left side), both scaled
  down and separated with a visible gap at the top. Reads as 刂 or 刁
  with the top disconnected.
- GT: 刀 has 横折钩 whose top-horizontal spans WIDE across the upper
  portion, and the 撇 CROSSES the horizontal — its head starts above
  and to the right of the horizontal's midpoint, then sweeps down-
  left through the horizontal, exiting below-left. This crossing is
  what distinguishes 刀 from 刁.
- Failure mode: drawer welded the pie head to the horizontal's LEFT
  END, not letting it cross. Also, heng_zhe_gou at scale 0.55 gave
  the top a right-angle look rather than the softer rounded corner
  the GT shows.
- Fix: increase heng_zhe_gou scale (~0.8) so the top spans more of
  the canvas; place pie head ABOVE the horizontal (math y +75) with
  tail below-left the horizontal, so the two strokes CROSS. See errata.

## Meta-lesson from bootstrap FAILs

Three of four fails (勹, 厂, 刀) involve **junction/composition
geometry** that the bank can't express. The bank has good single-
stroke primitives but no "curve smoothly between primitives"
mechanism — every join is either a weld (endpoint-to-endpoint) or a
crossing (default overlay). For rounded envelopes (勹) and for
cross-junctions (刀's crossed pie) the drawer must inline. When the
target's silhouette contains a smooth curve that a straight-line
`heng` + right-angle `heng_zhe_gou` combination cannot approximate,
INLINE a bezier — do not force the composition.
