# Cycle 19 — Task brief (5 carry + 公)

Eval: **gt+ocr+vision**. Pass = `is_correct AND ocr_confidence ≥
0.4 AND rubric ≥ 7 (no 0)`. Hard no-skip. Width floors mandatory.

## Carry-overs (5) with c18 refined targets

1. **也 (10 attempts)**. Restore c17 layout (which got OCR-pass)
   but apply width floors: upper-middle 竖弯钩 dominating bottom
   half (sweep y=+100→-100→+150 x then 50px up-hook). 横折钩 inset
   in top-left. All strokes peak 16 middle 10.

2. **巴 (9 attempts)**. Verify 竖弯钩 actually renders: extend
   弯钩 bottom to y = -280 (well below frame bottom y = -150);
   hook tip up-right at (x=+200, y=-260). Frame on top, BIG 弯钩
   below. Width floors.

3. **寸 (3 attempts)**. Make 竖钩's leftward hook arm LONGER (60+
   px). Place 点 in upper-right (above heng's right tip area), not
   beside the 竖钩 — c18's placement read as 于.

4. **万 (3 attempts)**. CRITICAL: 撇 head at y = heng_y + 80 (not
   just +30). The 撇 must START in the empty space ABOVE the heng
   then sweep DOWN through the heng to lower-left.

5. **几 (2 attempts)**. The 钩 (up-hook at end of 横折弯钩) MUST
   be prominent — hook arm length 60+ px, tip pointing up-and-left.
   Without it 几 reads as 门.

## New (1)

6. **公** (4 strokes — 八 + 厶): top 撇 + 捺 form 八 (apex at top,
   limbs sweeping down-left and down-right), then 厶 below (small
   横撇 + 点 forming a triangle-like shape with one corner).
   - top 撇: head upper-middle, sweeps to lower-left.
   - top 捺: head upper-middle (same), sweeps to lower-right.
   - 厶's 横撇: from lower-left area, short heng then 折 down then
     撇 down-left.
   - 厶's 点: closing dot at the right side of the 厶.

Save each PNG as `attempts/cycle_19/<idx>_<char>.png`.
