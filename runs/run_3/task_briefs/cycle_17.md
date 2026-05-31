# Cycle 17 — Task brief (4 carry-overs + 太 + 几)

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND rubric ≥ 7
(no 0). Hard no-skip active.

## Carry-overs (4)

1. **也 (8 attempts).** Re-structure: 竖弯钩 originates from
   UPPER-MIDDLE (not upper-left) and wraps around the others. The
   横折钩 sits clearly INSIDE the 竖弯钩's arc.
2. **巴 (7 attempts).** 竖弯钩's lower curve MUCH longer — doubling
   the character's vertical extent. The bottom-extending part must
   be unmistakable (frame on top, BIG curve+hook below).
3. **寸 (1 attempt).** Place 点 in the traditional 寸 position:
   below the heng, beside the 竖钩 (right side, mid-height) — NOT
   above. Make it clearly separate.
4. **万 (1 attempt).** 横折弯钩's bottom curve must sweep RIGHT
   clearly before the up-hook. Currently the bottom curl wasn't
   pronounced enough.

## New (2)

5. **太 (4 strokes):** 大 + 点 below. Composition:
   - heng (slight V-dip in middle, like 大's),
   - 撇 (head above heng's middle-left, sweeps through heng to
     lower-left, like 大),
   - 捺 (head above heng's middle-right, sweeps through heng to
     lower-right with flat kick, like 大),
   - 点 (small dot below the 撇/捺 crossing, in the lower-center
     area — distinguishes 太 from 大).

6. **几 (2 strokes):**
   - 撇 (head at upper-left, sweeps down-left as a gentle curve —
     short).
   - 横折弯钩 (compound: short top heng → corner → vertical drop →
     bottom curve right → small upward 钩 at end). The character's
     right side and bottom curve.

## Brushwork

CRITICAL: smooth cubic Bézier with continuous per-sample pensize.
No dot-stamped artifacts. Compound strokes are ONE continuous
brushed path with corner 顿笔 thickening (NOT a separate disc) +
short hook tail-arm.

Save each PNG as `attempts/cycle_17/<idx>_<char>.png`.
