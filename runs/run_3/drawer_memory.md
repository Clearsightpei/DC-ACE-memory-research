# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.
**Hard no-skip**: `is_correct == false` OR `ocr_confidence < 0.4`
→ MUST carry over. Quality > coverage.

---

## "OCR-wall" was rationalization (proven c12–c16)

All previously "OCR-wall" chars mastered: 大 (c12), 入 (c12), 火 (c14).
Same principle holds for ongoing failures (also, 巴).

## Verified atomic-stroke recipes

Smooth cubic Bézier centerline ~120–200 points; **per-sample
pensize with `t.pensize(w); t.goto(x,y)`** — NOT `t.dot(w, ...)`
stamps. Middle ≥ 50% peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat horizontal kick) | start |
| 提     | start | end |
| 点     | belly (heavy outer for radiating 点 in 小/火); tilted ~45° | tail (inward) |

## Brush rendering — smooth Bézier, NOT dot stamps (c15 lesson, c16 fix)

Render strokes as `t.pensize(w); t.goto(x,y)` along sampled
Bézier — continuous fluid line. NEVER as `for p in pts:
t.dot(w, p)` stamps; that leaves "beads on a wire" joint artifacts
that hurt OCR and rubric.

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩, 横钩.
横折弯钩 attempted c16 in 万 — first attempt fail; needs iteration.

## Canvas conventions

- 800×600 white; smooth per-sample pensize.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (30 mastered through c16)

- 1–2 strokes: 一, 二, 十, 人, 八, 又, 入, 力, 了.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已, 大, 小.
- 4 strokes: 不, 木, 王, 中, 日, 月, 火, 天, 见.

**见 (c16 fix):** 撇 as LONG diagonal (>200 px) sweeping from
upper-right area through frame to lower-left.
**小 (c16 fix):** tilted 点 (~45°), teardrop, outer-end heavy,
tail-toward-center.

## Active carry-overs (4)

- **也 (8 attempts).** c16 had smooth-Bézier (good) but OCR returned
  己. Different mode every cycle (people/animal/empty/卫/山/己).
  Composition is the persistent challenge. **Next:** the 竖弯钩
  should originate from the UPPER-MIDDLE of the character (not
  upper-left) and wrap around the others. Make 横折钩 sit clearly
  INSIDE the 竖弯钩's arc.

- **巴 (7 attempts).** c16 read as 日 again. **Next:** the 竖弯钩's
  lower curve must be MUCH longer — doubling the character's
  vertical extent. The bottom-extending 弯 part must be unmistakable
  (currently OCR sees just the frame).

- **寸 (1 attempt).** OCR returned 下. The 点 didn't register as
  separate from the 竖钩. **Next:** place 点 to the upper-right
  (clearly above the heng) OR in the traditional 寸 spot (below
  heng, beside 竖钩, right side mid-height). Make it visibly
  separate.

- **万 (1 attempt).** OCR empty. New compound 横折弯钩 didn't render
  well. **Next:** make the 横折弯钩's bottom curve clearly sweep
  RIGHT before the up-hook. Currently the bottom curl may not be
  pronounced enough.

## What to do next cycle

c17 is the final scheduled cycle in this batch. Backlog = 4
(也, 巴, 寸, 万). Backlog < 6 → 2 new chars allowed. But: focus on
the carry-overs to maximize mastery growth. Possible c17:
[也, 巴, 寸, 万, +2 simple fillers like 几, 长 or just one filler
like 几 + a re-test of a previously mastered character to confirm
no regression].

Actually with only 1 cycle left and 4 carry-overs, the best play
is [也, 巴, 寸, 万, + 2 simple chars likely-mastered-first-try].
Try: **几** (2-stroke 撇 + 横折弯钩), **长** (4-stroke uses 撇/捺
familiar). Or safer: **公** (4-stroke 撇+捺+厶), **太** (4-stroke
大+点, leverages mastered 大 + simple 点 addition).

Recommended: **太** (4 strokes — 大 + 点 below: leverages c12's
mastered 大) and **几** (2 strokes — 撇 + 横折弯钩, second attempt
at 横折弯钩 in a simpler context than 万's).
