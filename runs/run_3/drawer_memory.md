# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.
**Hard no-skip**: `is_correct == false` OR `ocr_confidence < 0.4`
→ MUST carry over. Quality > coverage.

---

## "OCR-wall" was rationalization (proven c12–c14)

All three previously "retired" chars mastered with specific
geometric fixes: 大 (c12, wide tails + dipped heng), 入 (c12, dominant
捺), 火 (c14, no apex stub + 点 at x±100).

## Verified atomic-stroke recipes

Bézier centerline ~120–200 points; per-sample pensize; middle ≥ 50%
peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick, prefer HORIZONTAL ending) | start |
| 提     | start | end |
| 点     | belly (heavier OUTER end for radiating 点 like in 小, 火) | tail (inward) |

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩, 横钩.

## Brush-rendering pitfall (c15 lesson)

**Avoid "dot-stamped" segments.** When the brush is rendered as a
series of disc-stamps along the path, joints look like beads strung
on a wire. Use cubic Bézier with continuous per-sample pensize — no
visible dot artifacts. c15 也 lost rubric points to this.

## Canvas conventions

- 800×600 white; per-sample pensize on Bézier.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (28 mastered through c15)

- 1–2 strokes: 一, 二, 十, 人, 八, 又, 入, 力, 了.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已, 大.
- 4 strokes: 不, 木, 王, 中, 日, 月, 火, 天.

**天 (c15 fix):** straight 捺 diagonal + horizontal flat-tail kick
at bottom-right. OCR conf 1.00.
**了 (c15 fix):** bottom stroke clearly CURVES (not straight) —
sweeps right then hooking left at bottom. OCR conf 0.94.

## Active carry-overs (4)

- **也 (7 attempts).** c15 had tight bbox + 竖弯钩-as-frame
  (composition right) but rendering had dot-stamp artifacts
  hurting readability. **Next:** smooth brush (continuous Bézier
  pensize, no dot artifacts) on the same composition.

- **巴 (6 attempts).** c15 squarer aspect → OCR returned 日 (broke
  已 prior). **Next:** taller frame again (height > width) with the
  竖弯钩's hook clearly extending BELOW the upper rectangle. The
  bottom-extension is what separates 巴 from a small 日.

- **见 (4 attempts).** c15 OCR still 月. **Next:** make the 撇 a
  very LONG diagonal (>180 px) sweeping from the upper-right area of
  the frame down to the lower-left, clearly exiting the frame at the
  bottom — not a short stroke hugging the frame's left side.

- **小 (1 attempt).** OCR empty. The 点s were too horizontal
  (— marks). **Next:** tilt the 点 more steeply (~45°), make them
  smaller and teardrop-shaped, with heavier end on the OUTSIDE
  (away from the center shu), tail pointing toward the shu.

## What to do next cycle

c16 backlog = 4 (也, 巴, 见, 小). Backlog < 6 → 2 new chars
allowed.

Recommended c16 batch: [也, 巴, 见, 小, +2 new].
- 4-stroke easy fillers: 长 (4), 心 (4, 卧钩 family — ambitious),
  天 (done), 文 (4), 风 (4 — frame+hooks).
- 3-stroke easy: 子 (done), 寸 (3 — 一+亅+丶), 万 (3, 一+ノ+乙).
Recommended pair: **寸** (simple 3-stroke testing 点 placement) and
**万** (3-stroke testing 一+撇+横折弯钩 — checks the 横折弯钩
compound).
