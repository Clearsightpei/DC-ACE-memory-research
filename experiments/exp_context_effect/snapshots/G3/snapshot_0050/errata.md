# 错题集 — G3 (coord-bank)

Items the human marked FAIL. Each has a self-diagnosis (from the PNG)
and a specific coord-format fix idea to try on retry. All three fails
from batch 1 are hook strokes — a real pattern.

## GRADUATED (batch-3 retry PASS)

- **p1_stroke_14_竖钩** — retry PASSED. Now bank primitive `shu_gou.py`.
- **p1_stroke_23_竖弯钩** — retry PASSED. Now bank primitive `shu_wan_gou.py`.

Removed from errata; see Success Bank entries #43, #44.

## GRADUATED (batch-4 retry PASS)

- **p2_radical_024_冂** — retry PASSED. Now bank primitive `jiong_radical.py`
  (bank #54). The inlined-three-segments recipe (fang_radical pattern)
  worked verbatim — this validates P11 for open-frame radicals.

Removed from errata.

## p1_stroke_16_斜钩 (xie gou)

- Batch: 1
- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_16_斜钩/01_斜钩.png`
- Diagnosis (from vision):
  - The main body reads as a nearly-straight diagonal line from
    upper-left to lower-right, with only the faintest curve.
  - The "hook" is a small filled circular blob at the lower-right end
    with essentially no upward flick visible.
  - Real 斜钩 needs (a) a distinct rightward BULGE in the middle-lower
    of the body (belly curves outward toward lower-left of the chord —
    the arc is much more pronounced), and (b) a visible tapered flick
    UP (not up-left; classic 斜钩 hook rises nearly vertically or
    slightly leftward from the tail).
- Fix idea for retry:
  - Increase the cubic bezier's outward curvature: move p1 from
    `(140, 140)` toward `(105, 165)` (further from the chord) so the
    belly is unmistakable.
  - Redraw the hook as a proper tapered segment (width 10 -> 2 over
    ~35 px), heading up and slightly left from `p3`. Do NOT collapse it
    into a single ellipse.

## p1_stroke_19_横斜钩 (heng xie gou)

- Batch: 1
- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_19_横斜钩/01_横斜钩.png`
- Diagnosis (from vision):
  - The shape reads as a plain angled "V" or bent stick: short horizontal
    top-left segment meets a long thick diagonal going down-right, and
    then simply stops. No hook is visible at the bottom-right tip.
  - Missing: the characteristic upward flick (钩) at the end of the
    diagonal. Also missing: the smooth curve of the 斜 segment (the
    stroke should CURVE, not just angle sharply).
  - Uniform ink thickness throughout — no calligraphic taper anywhere.
- Fix idea for retry:
  - Draw three explicit segments in coord form:
    1. 横 as a short tapered line from `(-90, +55)` to `(-30, +60)`
       (thin -> slightly thicker).
    2. 斜 as a quadratic bezier from `(-30, +60)` through
       `(+20, +5)` to `(+70, -55)` with tapered width (11 -> 7).
    3. 钩 as a short tapered flick from `(+70, -55)` to `(+45, -25)`
       (width 8 -> 2). This flick UP is essential.
  - Don't render with turtle+PostScript: canvas resizing losslessly
    tends to blur the hook. Use direct PIL ImageDraw like the other
    passing strokes.

## Cross-fail pattern

All three fails are hook (钩) strokes. Shared failure mode: the hook
either was omitted, collapsed into a blob, or drawn as a
downward/wrong-direction spike. See `principle_bank.md` P1 for the
derived principle.

## p1_stroke_21_横折弯 (heng zhe wan) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_21_横折弯/01_横折弯.png`
- Diagnosis (vision): rendered as 横 + right-angle drop + tiny bottom-
  right corner blob. The 弯 (final sweeping curve to the right along
  the base) is essentially invisible — the quarter-arc I coded lands
  in a stubby ⌐-like L, and the "short horizontal tail" is only 5 px
  wide so it doesn't read as the horizontal sweep that defines this
  stroke.
- Fix idea (coord form):
  - Extend the final horizontal a LOT: `p_h_end = (140, -60)` not
    `(95, -60)`. The 弯 tail should be visually LONGER than the top
    横.
  - Make the arc bigger: `arc_r = 45 * scale` (was 30) so the curve
    is unmistakably an arc, not a rounded corner.
  - Widen the final segment relative to the vertical (11 → 13) so it
    reads as ink-heavy on the sweep.

## p1_stroke_25_横折弯钩 (heng zhe wan gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_25_横折弯钩/01_横折弯钩.png`
- Diagnosis (vision): reads as a top 横 + short vertical + a big
  bulging arc that swings LEFT along the bottom, but the arc's belly
  goes DOWN too far and the terminal hook flicks LEFT-and-UP instead
  of pointing up-and-inward. Envelope is roughly correct but the
  arc reads as a sagging bag rather than the crisp 弯 of 也/巴.
- Fix idea (coord form):
  - Flatten the arc: `p_arc_ctrl = (30 * scale, -55 * scale)` (was
    (55, -70) — pull the control point up and center-ward so the arc
    bottom rises).
  - Shorten the arc's leftward reach: `p_arc_end = (-30, -70)` (was
    (-55, -75)) — the tail should stop under the top 横's start, not
    extend past it.
  - Hook up-and-slightly-RIGHT from that endpoint: `hook_tip = (-15,
    -40)`. The classic 横折弯钩 hook points INWARD toward the enclosed
    area, not outward left.

## p1_stroke_26_横折折 (heng zhe zhe) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_26_横折折/01_横折折.png`
- Diagnosis (vision): rendered as a clean ⊐ shape (top horizontal +
  right vertical + bottom horizontal going left). Geometry is correct
  but the corner blobs are oversized ellipses that dominate the
  visual mass — the human likely read it as three disconnected line
  segments with three dots rather than one continuous stroke. Also
  the bottom horizontal ends flat rather than continuing the ink
  taper.
- Fix idea (coord form):
  - Shrink corner blobs: `r1 = r2 = 6 * scale` (was 8). Cap at ~ink/2
    so they visually merge with the line rather than punctuate it.
  - Use `_stroke_line` (stamped-circle taper) for all three segments
    instead of `_stroke_line` with heavy uniform width — the current
    code already does this but with too-wide (12) width. Drop to 10.
  - Kill the terminal blob at (-50, -40); let the bottom 横 taper to
    its natural end.

## p1_stroke_31_竖折折钩 (shu zhe zhe gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_31_竖折折钩/01_竖折折钩.png`
- Diagnosis (vision): rendered as vertical + horizontal + short
  vertical, with a triangular blob glued to the bottom of the second
  vertical. The hook reads as pointing DOWN-and-LEFT, not UP-and-LEFT
  (P1 violation). Second vertical also too short — the hook has no
  room to originate from the shaft, so it grew off the corner blob
  instead (P9 violation).
- Fix idea (coord form):
  - Lengthen the second vertical: `D = (60, -90)` not (60, -70) — add
    20 px so the hook can flick from its base.
  - Hook: `hook_base = (60, -88)` and `hook_tip = (30, -68)`. Both
    endpoints in math coords, +y up — hook_tip.y is HIGHER than
    hook_base.y so the direction is genuinely up-and-left.
  - Remove the corner-blob-at-D and let the tapered shaft itself
    form the hook root.

## p1_stroke_32_横折折折钩 (heng zhe zhe zhe gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_32_横折折折钩/01_横折折折钩.png`
- Diagnosis (vision): reads as a compact 3 or a broken乙-like scribble.
  I tried to draw the shape by 4 straight segments (short 横 + down-
  left diag + down-right belly + short drop + hook) but the second
  diagonal down-LEFT is wrong — the canonical 横折折折钩 (as in 乃, 及)
  runs 横 → down (short 竖) → sweeping-left 撇 curve → tiny 折 back
  right → up-left hook. My down-left-then-down-right zig-zag reads as
  a "Z" cursor, not the 乃 shape.
- Fix idea (coord form):
  - Redesign as 4 anchors + hook: `A(-70, 90)` 横 to `B(30, 95)`, then
    `B` down to `C(30, 30)` (short 竖), then quadratic bezier
    C→ctrl(0, -30)→D(-70, -70) as the sweeping 撇 (the belly of 乃),
    then `D` to `E(-30, -50)` as the terminal 钩 up-and-right.
  - Use a Bezier (not straight segments) for the belly — this is the
    only stroke in the batch that genuinely curves like a hairpin.
  - Match against 乃's right side visually before committing.

## p1_stroke_26_横折折 — STALE (retry_n=2)

Failed twice on retry (batch 3 and batch 4). Both errata fixes were
cosmetic tweaks (blob size, calligraphic slope) that clearly do not
address the underlying failure mode. If not solved by scan #4
(items #100+), freeze permanently per shared_rules.md terminal-freeze
rule. Do not spend a third retry attempt on cosmetic-only fixes.

---

# Batch-4 new fails (main curriculum, 11 items)
