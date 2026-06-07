# Cycle 21 — 5 carry + 夫

Eval: gt+ocr+vision. Pass = is_correct AND conf≥0.4 AND rubric≥7 no 0. Width floors mandatory.

## Carry-overs (new c20 boundary analysis)

1. **也 (12x)** — c20 read 吧 conf 0.76 (composition CLOSE — 吧 = 口+也, so the basic 也 silhouette is there but with extra 口-like fragment). **Fix:** remove any closed-rectangle-shaped element from the upper-left. The 横折钩 must be OPEN (no closing bottom-left bar), just heng + 折 down + small hook tip. No left-side 竖 making a square.

2. **巴 (11x)** — c20 read 已 conf 0.92. The upper portion looked like 已's top. **Fix:** make the upper rectangle CLOSED on ALL FOUR sides and SHORTER (frame top y=+180, frame bottom y=+20, frame width 100±). Then 竖弯钩 starts at the frame's bottom-left and dominates the lower 2/3.

3. **寸 (5x)** — c20 conf 0.34 (sub-threshold). **Fix:** simplify — heng wider (-220 to +220), 竖钩 thicker with hook arm 70px, 点 as a clear separate teardrop at bottom-right of the heng (belly at (+150, +50) tail (+200, +10)) — well to the right of the 竖钩, just below the heng.

4. **万 (5x)** — c20 read 九 conf 0.64. **Fix:** make the top heng VERY LONG (-220 to +220) so it's clearly the dominant horizontal — 九's top is much shorter. Then 撇 head at (+30, +180), tail (-180, -150). 横折钩 starts at (+150, +100) with its corner at (+150, +20) then small hook left to (+90, +30).

5. **公 (3x)** — c20 read 今 conf 0.99. **Fix:** the 厶 must be SEPARATE from the 八 above (vertical gap). 八 ends at y=+30. 厶 starts at y=-20 (50px gap). 厶: small 撇 from (-40,-30) to (-100,-130), and 点 from (+40,-30) to (+90,-110). Two strokes forming an open "V" below — NO connecting heng.

## New (1)

6. **夫 (4 strokes)** — top heng (short) + lower heng (long) + 撇 from center sweeping down-left + 捺 from center sweeping down-right. Like 大 but with an extra heng above. Coords:
   - top heng: (-100, +200) to (+100, +200), weight ends.
   - lower heng: (-180, +80) to (+180, +80), V-dipped middle.
   - 撇: head (-20, +220) to tail (-200, -160).
   - 捺: head (+20, +220) to tail (+200, -140) with flat kick.

Save PNGs as `attempts/cycle_21/<idx>_<char>.png`.
