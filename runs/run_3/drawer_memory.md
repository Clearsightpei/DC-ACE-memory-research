# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.
**Hard no-skip**: `is_correct == false` OR `ocr_confidence < 0.4`
→ MUST carry over. Quality > coverage.

---

## "OCR-wall" claim fully disproven (c12–c14)

All three characters previously labeled OCR-wall were mastered with
concrete composition prescriptions:
- 大 (c12): wide limb tails ±260 + short apex + slight V-dip in heng.
- 入 (c12): 捺 dominant (longer + heavier than 撇).
- 火 (c14): apex stub REMOVED + 点 at x±100 flanking apex at apex
  height.

The principle: when OCR rejects, the silhouette has a fixable
geometric defect. Find and fix it. Do not declare measurement broken.

## Verified atomic-stroke recipes

Bézier centerline ~120–200 points; per-sample pensize; middle ≥ 50%
of peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick) | start |
| 提     | start | end |
| 点     | belly | tail |

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩, 横钩.

## Canvas conventions

- 800×600 white; per-sample pensize on Bézier.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (26 mastered through c14)

- 1–2 strokes: 一, 二, 十, 人, 八, 又, 入, 力.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已, 大.
- 4 strokes: 不, 木, 王, 中, 日, 月, 火.

**火 (c14 fix):** apex stub REMOVED entirely (撇/捺 just meet, no
vertical extra). 点 at x ≈ ±100, at apex height, sloped inward.
Read as ears flanking the apex.

## Active carry-overs (5)

c14 mastered 火; 5 still failing. Each has a refined diagnosis.

- **也 (6 attempts).** c14: hook on 横折钩 + thinner shu — OCR returned
  empty (different from 卫/山). **Next:** TIGHTER bounding box; strong
  horizontal connection at the bottom; the three strokes must overlap
  into one body. Maybe re-think 也 as: 竖弯钩 as the dominant FRAME
  (sweeps from upper area down + right + hook); other 2 strokes
  inside that frame.

- **巴 (5 attempts).** c14 widened the upper frame — still 已 (conf
  0.681). **Next:** try a SQUARER aspect ratio (less tall, more
  square) and see if breaking the verticality breaks the 已 prior.

- **见 (3 attempts).** c14: OCR returned 凡 (new mode, not 月).
  Progress. **Next:** smaller top frame; shorter 撇 leg; the 竖弯钩
  should clearly be the right edge of the frame extended downward.

- **天 (2 attempts).** c14: OCR returned 元 again. The 捺 curves
  too much, reading as 竖弯钩. **Next:** straighter 捺 diagonal,
  strong horizontal flat-tail kick at the bottom-right.

- **了 (1 attempt).** OCR returned 丁. **Next:** make the bottom
  stroke clearly CURVED (sweeping right then hooking left at bottom),
  not a straight vertical-with-hook like 丁.

## What to do next cycle

c15 backlog = 5 (也, 巴, 见, 天, 了). Backlog < 6 → 1 new char
allowed.

Recommended c15 6th slot — keep new chars simple and far from
current failures: **三** was already mastered; **小** is 3 strokes
introducing a vertical-hook + 点 + 点 composition (new for the run).
Try **小**.
