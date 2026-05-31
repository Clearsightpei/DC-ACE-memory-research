# Cycle 16 — Task brief (4 carry-overs + 寸 + 万)

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND rubric ≥ 7
(no 0). Hard no-skip active.

## Carry-overs (4) with c15 refined diagnoses

1. **也 (7 attempts).** Composition right (竖弯钩 as frame, tight
   bbox). **CRITICAL FIX:** use CONTINUOUS cubic Bézier with
   per-sample pensize — DO NOT render brush as a series of disc
   stamps along the path (last cycle had visible "beads on a wire"
   joint artifacts). Smooth, fluid strokes only.
2. **巴 (6 attempts).** Squarer aspect → 日 prior. **Fix:** make
   the frame TALLER again (h > w) but with the 竖弯钩's hook
   clearly extending BELOW the rectangle. The hook's bottom-most
   point should be visibly outside/below the rectangle.
3. **见 (4 attempts).** **Fix:** make the 撇 leg a LONG diagonal
   (>180 px) sweeping from the upper-right area of the frame down
   to the lower-left, clearly exiting the frame at the bottom.
4. **小 (1 attempt).** **Fix:** tilt the 点s more steeply (~45°),
   smaller and teardrop-shaped. Heavier end on the OUTSIDE (away
   from the center shu), tail pointing TOWARD the shu.

## New (2)

5. **寸 (3 strokes):**
   - heng (medium length, near the top),
   - 竖钩 (vertical going down from the heng's center, small hook at
     bottom-left),
   - 点 (small dot, upper-right area of the character).
   The 点 is the distinguishing feature.

6. **万 (3 strokes):**
   - heng (top, short),
   - 撇 (long, head at heng's left, sweeping down-left),
   - 横折弯钩 (compound: heng → corner → curve → hook). Starts
     near the right end of the top heng, drops, curves rightward,
     hooks up.

## Calligraphic detail

CRITICAL: use smooth cubic Bézier with continuous per-sample pensize.
No dot-stamped artifacts. Compound strokes are ONE continuous path
with corner 顿笔 (a thickening, NOT a separate disc).

Save each PNG as `attempts/cycle_16/<idx>_<char>.png`.
