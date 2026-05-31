# Cycle 13 — Task brief (5 carry-overs + 1 new)

Backlog dropped to 5 after c12 mastered 大/入. Adding 1 new char
(天 — explicit contrast to 大).

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
rubric ≥ 7 (no 0). Hard no-skip active.

## Carry-overs (5) with c12 refined diagnoses

1. **火 (5 attempts)**. 点 must sit at apex's HEIGHT or slightly
   below the apex top, sloped INWARD toward apex. Try belly at y ≈
   +90 with apex at y = +130 — 点 belly is BELOW the apex top.
   Read as "ears beside the head", not "dots above".
2. **也 (4 attempts)**. Middle shu's foot MUST land on the bottom
   curl of 竖弯钩 (its bottom y ≤ the 弯 floor y). Thicken 横折钩
   so it dominates the top-left.
3. **力 (3 attempts)**. 撇 head must visibly CROSS the top heng
   (撇 head at y > heng_y, then sweep DOWN through and out the
   lower-left). c12 撇 didn't visibly intersect.
4. **巴 (3 attempts)**. Add a THIRD horizontal bar inside the upper
   frame (tri-decker) to break OCR's 已-prior. Or make upper
   rectangle visibly WIDER than the 竖弯钩's lower extent.
5. **见 (deferred, 1 attempt total)**. 撇 leg must visibly diverge
   from the frame at the bottom-left, sweeping down-LEFT past the
   frame bottom — not continuing straight down.

## New (1)

6. **天 (4 strokes)** — a deliberate contrast with 大 (which RapidOCR
   sometimes mistook earlier for 天).
   - top heng (short, near the top),
   - second heng (longer, below the top, like a 二),
   - 撇 (from the second heng's center, sweeping down-left),
   - 捺 (from the second heng's center, sweeping down-right).
   The two heng are STACKED at the top (like 二); the 撇/捺 hang
   from the LOWER heng, going down. Compare with 大: 大 has ONE
   heng cutting THROUGH the 撇/捺 with limbs extending well above
   the heng. 天 has TWO heng stacked on top with limbs only below.

## Brushwork

Standard mastered: Bézier per-sample pensize, middle ≥ 50% peak,
heavy-end cheat sheet, compound strokes with corner 顿笔 + short
hook tail-arms.

Save each PNG as `attempts/cycle_13/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief.
