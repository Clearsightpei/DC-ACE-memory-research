# Cycle 18 — Task brief (6 carry-overs, brushwork repair)

Backlog hit 6 after c17 — forced carry-overs-only batch. The
chars: 也, 巴, 寸, 万, 太, 几.

## Critical fix this cycle: BRUSHWORK WIDTH FLOORS

c17 regressed: many strokes rendered as hairline-thin uniform lines
(撇 in 太 was essentially invisible). OCR is permissive of this;
the rubric correctly fails it (taper=0 → fail mastery).

**Per-stroke minimum widths (NEVER go below these except at
deliberately tapered tips):**

| stroke | peak | shaft middle | tapered tip |
|--------|------|--------------|-------------|
| 横     | 16   | 10           | 6           |
| 竖     | 16   | 10           | 6           |
| 撇     | 17 head | 11 shaft  | 2 only at last 5% |
| 捺     | 18 tail | 10 shaft  | 4 head     |
| 提     | 14 base | 9 shaft   | 2 only at last 5% |
| 点     | 14 belly | n/a       | 2 tail      |

If your `w_profile(s)` returns 2 or 3 anywhere except the very tip
of a real taper, you have broken the brushwork. Use `max(3, ...)`
floor in `brushed_bezier`.

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct AND ocr_confidence >= 0.4
AND rubric ≥ 7 (no 0)`. Hard no-skip active.

## Carry-over diagnoses

1. **也 (9 attempts)**. c17 finally OCR'd as 也 (conf 0.94). Keep
   the upper-middle 竖弯钩 + inset 横折钩 layout. Apply width floors.
2. **巴 (8 attempts)**. c17 read as 电. Widen the upper frame
   (wider than tall, not square). Apply width floors.
3. **寸 (2 attempts)**. c17 OCR'd as 卡 (conf 0.31 — below 0.4
   threshold). Keep 点 in traditional spot. Apply width floors.
4. **万 (2 attempts)**. c17 OCR'd as 瓦 with conf 0.97 — confidently
   wrong. **Fix:** 撇 head must start ABOVE the heng (head at y >
   heng_y + 30); 撇 sweeps THROUGH heng to lower-left.
5. **太 (1 attempt — regression)**. Redraw 大-shape with PROPER
   widths (this was 10/10 in c12!) then add the 点 below.
6. **几 (1 attempt — regression)**. Apply width floors on both
   strokes. Structure was already correct.

Save each PNG as `attempts/cycle_18/<idx>_<char>.png`.
