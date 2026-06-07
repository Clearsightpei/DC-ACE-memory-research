# Cycle 22 — 5 carry + 车

Eval: gt+ocr+vision. Pass=is_correct AND conf≥0.4 AND rubric≥7 no 0. Width floors mandatory.

1. **也 (13x)** — c21 OCR empty. Open 横折钩 broke it. **Fix:** restore closed 横折钩 like c12-era 也, but distinguish from 吧 by NOT making a fully-enclosed left rectangle. The 横折钩 top closes to the right (no left 竖). 竖弯钩 wraps.
2. **寸 (6x)** — c21 read 十. **Fix:** drop the 点 idea — instead make 寸 with a CLEARLY VISIBLE 竖钩 hook that's so prominent it forms a distinguishing feature. heng x=±200 y=80. 竖钩 (0,+170) → (0,-160) with hook arm 100px to (-100, -130). 点 belly (+130, +30), tail (+170, -10).
3. **万 (6x)** — c21 read 方. **Fix:** the 撇 needs to extend FURTHER LEFT past the heng's left end. Currently it's within the heng. heng (-200,+100) to (+200,+100). 撇 head (+30,+200), tail (-260,-160) — clearly past heng's left edge.
4. **公 (4x)** — c21 OCR empty. **Fix:** close the gap — overlap 厶 slightly with the bottom of 八. 八 ends y=0, 厶 starts y=+10 (overlap). 厶 撇 (-30,+10)→(-110,-150), 点 (+40,+10)→(+100,-130).
5. **夫 (2x)** — c21 OCR empty despite rubric 10. **Fix:** make the upper heng LONGER (-150 to +150), not so short — it should be visible but secondary to the lower heng. Reduce vertical gap between hengs (top y=+170, lower y=+50, only 120 apart).
6. **车 (NEW 4 strokes)** — heng (top, -200 to +200 at y=+170), 撇 (head +30,+200 to tail -150,+40), 竖 (centered, 0,+90 to 0,-180), heng (bottom, -180 to +180 at y=-80). Like a stylized "Z" structure.

Save: `attempts/cycle_22/<idx>_<char>.png`.
