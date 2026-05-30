# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.

---

## Verified atomic-stroke recipes

Cubic-Bézier centerline ~120–200 points; per-sample pensize;
middle ≥ 50% of peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick) | start |
| 提     | start (heavy weighted base) | end (fine flicked point) |
| 点     | belly | tail |

## Compound strokes (mastered as of c10)

| compound | first verified | status |
|----------|---------------|--------|
| 竖弯 | c6 (七) | yes |
| 竖折 | c6 (山) | yes |
| 横撇 | c7 (又) | yes |
| 横折 | c8/c9 (中/口/日) | yes |
| 竖钩 | c9 (子) | yes |
| 横折钩 | c10 (习, 已) | yes (drill more) |
| 竖弯钩 | c10 (已) | yes (drill more) |

One continuous brushed path; each turn is a 顿笔 Gaussian
thickening; hooks are short tail-arms (15–20% main length) with
fine taper.

## Canvas conventions

- 800×600 white; per-sample pensize; PostScript → PIL → PNG.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (21 mastered through c10)

- 1–2 strokes: 一, 二, 十, 人, 八, 又.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已.
- 4 strokes: 不, 木, 王, 中, 日.

## OCR-wall (retired)

- 大 (c5–c8): geometrically textbook silhouette, RapidOCR returns empty.
- 入 (c5–c8): geometrically textbook silhouette, RapidOCR returns 人.

## Probably OCR-wall (3rd attempt failure, document and consider retiring)

- **火 (c8, c9, c10):** apex-share + 点-hugging progressively
  refined; rubric crept from 5→6→6, OCR returns empty each time.
  This is the same pattern as 大. **For c11:** if a final refined
  attempt doesn't OCR, document as OCR-wall and stop drilling.

## Active failure modes — c10 lessons

### 也 (c9, c10) — still fragmented

The three strokes (横折钩, middle shu, 竖弯钩) need to OVERLAP into
one body. c10 still drew them too parallel.
**Fix for c11:** treat 也 as: the 竖弯钩 forms a horizontal floor +
right-side wall; the 横折钩 hangs from the top-left into that wall;
the middle shu drops STRAIGHT through the middle of the body, its
foot landing ON the floor of the 竖弯钩 (touching the bottom curl).
The three strokes occupy the SAME bounding rectangle, not three
side-by-side fragments.

### 力 (c10) — 撇 needs to cross through

c10 had 横折钩 + 撇 side-by-side. **Fix for c11:** the 撇 must
PASS THROUGH the interior of the 横折钩's frame. Start the 撇 head
at the top of the 横折钩 (near the top heng's middle) and sweep
down-left out through the frame and beyond. Visible overlap between
the 撇 and the frame's interior is essential.

### 巴 (c10) — read as 已 because frame was too small/single-level

c10 巴 had a small upper frame + 竖弯钩 → indistinguishable from 已.
**Fix for c11:** 巴 has a TWO-LEVEL frame distinct from 已. The
top portion of 巴 is a small filled rectangle (not just a corner),
with a middle heng visible INSIDE it. Then the 竖弯钩 extends below.
Make the upper rectangle clearly closed and double-decked (heng top,
middle heng inside, plus the side strokes).

## Soft / completed observations

- 习 mastered after c9→c10 reflection.
- 已 mastered first-try (the 钩-family primitives generalized).
- Frame family + 钩 family both have multiple verified instances.
- 火 has now failed 3 attempts — probable OCR-wall, not memory.

## What to do next cycle

c11 should carry **也, 力, 巴** with the explicit composition fixes
and try one final 火 with strict apex-hugging. Add 2–3 new chars to
fill the batch — candidates:
- 月 (4 strokes, 撇 + 横折钩 + two interior heng — frame-family
  extension with hooks)
- 见 (4 strokes, similar 月 structure + 撇 + 竖弯钩 footer)
- 心 (4 strokes, 卧钩 + 3 dian — radically new 卧钩 primitive)
Safer: 月, 见, and one more easy.

Recommended c11: [火, 也, 力, 巴, 月, 见].
