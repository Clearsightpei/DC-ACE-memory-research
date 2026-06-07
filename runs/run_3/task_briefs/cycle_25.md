# Cycle 25 — 5 carry + 东

Eval: gt+ocr+vision. Pass=is_correct AND conf≥0.4 AND rubric≥7 no 0.

1. **也 (16x)**. OCR has read: 卫(many), 已, 卫, 山, 吧, 卫, 卫. **NEW IDEA:** all those are characters with similar 竖弯钩 + frame structure. The KEY DIFFERENCE in 也 vs 卫: 也 has the 竖弯钩 hook longer and the upper portion fragmented (NOT a closed top heng). Try: NO top heng at all. Just (a) short heng (-100,+150)→(+30,+150) — incomplete left side, (b) short shu (0,+130)→(0,+20), (c) BIG 竖弯钩 from (-80,+50)→(-80,-150)→(+180,-150)→(+200,-90).
2. **寸 (9x)**. Many OCRs returned 十/于/小 — all chars without the 点+竖钩 structure of 寸. **NEW IDEA:** make the 竖钩 hook look MORE like a hook (curved more sharply). 竖钩 (0,+180)→(0,-160), then sharp hook curve to (-90,-100) (not linear, but curling up).
3. **万 (9x)**. OCR persistently 力/方/九. **NEW STRATEGY:** make the 撇 head shoot up dramatically VERY high and tilted backward. 撇 head at (+90,+260) (top-right), tail (-220,-180). The pre-撇 backward kick is distinctive.
4. **公 (7x)**. OCR 今/八/六. **NEW STRATEGY:** make 厶 look like the canonical 厶 — a small open triangle. 厶 strokes:
   - small 撇 (-20,-20)→(-100,-130).
   - 横折 (-100,-130)→(+40,-130)→(+40,-180).
   Plus closing 点 at (+30,-170)→(+80,-200).
5. **为 (3x)**. OCR 六/六. **NEW IDEA:** add the top 点 MUCH more prominently and slanted, and make the 横折钩 look distinctive. Top 点 belly (+50,+220) tail (+120,+170). The 横折钩 should have a CLEAR rounded turn (not sharp).
6. **东 (NEW 5 strokes)**: heng top (-180,+150)→(+180,+150), 竖钩 center (0,+90)→(0,-160) with hook (-60,-130), 撇 (-30,+60)→(-180,-40), 点 (+30,+60)→(+90,+20), heng bottom (-180,-90)→(+180,-90).

Save: `attempts/cycle_25/<idx>_<char>.png`.
