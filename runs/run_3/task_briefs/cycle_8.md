# Cycle 8 — Task brief (carry 大/入 + 4 new structural variety)

This batch carries the two un-mastered characters from c7 with sharper
numeric prescriptions, plus four new characters that introduce
genuinely new compositions (horizontal stacking with 工/王, two-撇
character 火, and the boxed 横折 with 中).

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
`calligraphy_rubric.total >= 7` (no 0 criterion).

## Repair targets (carry-overs)

1. **大 — heng must be much longer.**
   - heng length **≥ 2.0×** the horizontal limb-crossing span (c7 was
     1.55× → still too short, read as "A with crossbar").
   - apex visibly above the heng: apex at y ≈ +200, heng at y ≈ +50,
     limb tails at y ≈ −200. The "stem above heng" gap matters as
     much as the heng width.
   - Optional: a small overshoot of the apex above where 撇/捺 meet
     (a tiny stub poking up above the apex point) reads as the
     traditional 撇 head emphasis.
2. **入 — amplify asymmetry to push OCR past the 人 read.**
   - 撇 head: heavier and longer than the 捺 entry.
   - Junction at ~50% down 撇 (preserve c7's good junction).
   - 捺 end-point further to the lower-right so the right extent
     visibly dominates the left.
   - If OCR still returns 人 despite a rubric-good silhouette, that
     becomes a documented OCR-wall finding.

## New compositions

3. **工 (3 strokes):** top heng + center shu + bottom heng. The two
   heng are similar length (top maybe slightly shorter); shu is
   short, vertical between them.
4. **王 (4 strokes):** top heng + middle heng (shortest) + center
   shu (crossing all three heng) + bottom heng (widest). Like 工 but
   with an added middle heng halfway up.
5. **火 (4 strokes):** left 点 (top-left, tilted) + right 点
   (top-right, tilted the other way) + 撇 (left, head at center-top,
   sweeping down-left) + 捺 (right, head at center-top, sweeping
   down-right with flat tail). Two 点 on top, big 撇+捺 below.
6. **中 (4 strokes):** outer rectangular frame as three strokes + a
   long center shu. Strokes:
   - shu (left edge of frame),
   - 横折 (top + right edge — one compound stroke that turns 90° at
     the upper-right corner),
   - bottom heng (closes the frame at the bottom),
   - long center shu (extends well above and below the frame —
     this is the signature stroke of 中).

## Required calligraphic detail

All standard rules apply. Middle width ≥ 50% of peak on every stroke.
Use the cheat sheet. For compound 横折 in 中, treat the corner as a
顿笔 thickening; one continuous brushed path.

Save each PNG as `attempts/cycle_8/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief.
