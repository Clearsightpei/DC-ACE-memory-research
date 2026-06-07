# Cycle 20 — Task brief (6 carry-overs)

Eval: gt+ocr+vision. Pass = is_correct AND conf ≥ 0.4 AND rubric ≥ 7 no 0. Width floors mandatory.

## Per-character composition adjustments (from c19 boundary analysis)

1. **也 (11x)** OCR empty. The 3 fragments don't integrate. **Fix:** ONE BIG 竖弯钩 must connect visually with the small inset 横折钩 above. Draw 横折钩 first (heng at y=+100 spanning x=-100 to +80, then drop to y=+30), then SHU (vertical at x=-30, y=+50 down to y=-50), then 竖弯钩 starting at upper-middle (x=+30, y=+100) sweeping DOWN to y=-130 then RIGHT to x=+180 with up-hook at (+180,-70). The 竖弯钩 should visually CONTAIN the other two strokes within its arc.

2. **巴 (10x)** OCR 甲. The middle divider heng in the upper frame made it look like 甲's interior. **Fix:** make upper frame a SINGLE rectangle (no middle divider). Then the 竖弯钩 below. Frame: left 竖 x=-100 y=+200..0, top heng y=+200, right 竖 x=+100 y=+200..0, bottom heng y=0. Then 竖弯钩 from (-100, 0) sweeping down to (-100, -200), right to (+200, -200), up-hook to (+200, -150).

3. **寸 (4x)** OCR 十. **Fix:** make the 点 a clear teardrop in the LOWER-RIGHT — belly at (x=+60, y=-50), tail at (x=+95, y=-90), tilted ~30°. Below the heng (heng at y=+80), beside the 竖钩 (竖钩 at x=0). Plus thicken/lengthen the 竖钩's leftward hook arm (80+ px).

4. **万 (4x)** OCR 力. **Fix:** the 撇 head must be VERY high above the heng (head at y=heng_y+120, e.g. head at y=+220 if heng at y=+100). The 撇 should also be VISUALLY DOMINANT — peak width 19 (not 17), longer reach (head x=+50, tail x=-220). Make it the most prominent stroke.

5. **几 (3x)** OCR empty. **Fix:** moderate the 钩 — c19 overshot. Hook arm 40 px (not 60+), tip pointing up. Vertical drop on the right must be SHORT (top heng at y=+150, right drops only to y=-100 then 弯 right to x=+170, then up-hook 40 px).

6. **公 (2x)** OCR 今. **Fix:** the 厶 needs CLOSURE — instead of an open hook shape, draw it as: short 横撇 (heng from x=-80 y=-50 to x=+40 y=-50, then 折 down-left to x=-30 y=-140), then a 点 + a closing CONNECTION back up. Or: draw 厶 as a small triangle with one corner left open at top-right (which is the canonical 厶).

Save PNGs as `attempts/cycle_20/<idx>_<char>.png`.
