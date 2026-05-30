# Drawer memory

Curator-owned. Strokes are judged by a reference-free Claude-vision
calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion / overall,
0–2 each, /10). Characters add OCR + GT regression-only.
Mastery: `is_correct == true` AND rubric total ≥ 7, no 0,
post-reflection.

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

## Compound strokes — current state

| compound | first verified | status |
|----------|---------------|--------|
| 竖弯 (七 stroke 2) | c6 | mastered |
| 竖折 (山 stroke 2) | c6 | mastered |
| 横撇 (又 stroke 1) | c7 | mastered |
| 横折 (中 frame, 口, 日 frame) | c8 / c9 | mastered |
| 竖钩 (子 stroke 2) | c9 | mastered |
| 横折钩 (习, 也) | c9 | partial — composition issues |
| 竖弯钩 (也 stroke 3) | c9 | partial — character read fail |

Compound recipe: one continuous brushed path across all segments;
each turn is a 顿笔 Gaussian thickening; hooks are short tail-arms
(10–20% of main length) chained off the end with a fine taper.

## Canvas conventions

- 800×600 white, black; per-sample pensize on Bézier.
- `screen.tracer(0,0)` + `update()`; PostScript → PIL → PNG.
- `t.reset()` between tasks. Each task starts at (0,0) heading 90°.

## Verified character compositions

**Phase-2 mastered (19 chars through c9):**
- 1–2 strokes: 一, 二, 十, 人, 八, 又.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子.
- 4 strokes: 不, 木, 王, 中, 日.

**OCR-wall (retired, do not retry):** 大, 入.

## Active failure modes — c9 lessons

### 火 (c5/c8/c9) — three failed attempts, still failing

c9 fix landed: 撇 + 捺 share apex. New issue: the two **点 still
float above the apex with a visible gap**, plus the 撇 is too thin
(weak head). **Fix for c10:**
- The two 点 must HUG the apex — their *tails* nearly touch the
  apex point. The 点 belly is up-and-slightly-outward from the apex.
  Read: "two tiny ears immediately at the top of the V", not "two
  floating dots way above".
- 撇 head must be heavier (peak weight matching 捺 head).

### 习 — c9 first attempt failed

The 提 (third stroke) was too short and disconnected from the 横折
above; the result looked like 刁 or a partial 习. **Fix for c10:**
- 提 must be a SUBSTANTIAL rising flick (length ~60–70% of the 横折's
  width), and its head (weighted base) must be VISUALLY CLOSE to the
  bottom-left corner of the 横折 above, so the two strokes read as
  one tight assembly.
- 点 at the top-left of the 横折 should be small and tucked near the
  upper-left interior, not floating off-frame.

### 也 — c9 first attempt failed

The three strokes (横折钩, middle shu, 竖弯钩) were drawn as three
SEPARATE fragments side by side, not as a unified character. **Fix
for c10:**
- 横折钩 (stroke 1) goes top-left, descending into a hook at the
  middle.
- middle shu (stroke 2) sits CLOSELY to the right of 横折钩's
  vertical portion, NOT independently centered.
- 竖弯钩 (stroke 3) wraps around BOTH preceding strokes — it sweeps
  from the upper-right area down to the bottom, then curls right
  along the bottom, then hooks up-right. Its bottom portion forms
  the FLOOR of the character with the other strokes ABOVE it.
- Net effect: 也 is a unified shape with 竖弯钩 as a "cradle" around
  the other strokes. Three separated fragments will not OCR.

## Soft / completed observations

- Frame family (口, 日, 中, 王) transfers cleanly via 横折.
- 子's 竖钩 transferred first-try.
- 火 has been a stubborn first-try failure across 3 attempts — the
  Drawer keeps placing 点 too high. The c10 prescription must be
  explicit on hugging-the-apex.

## What to do next cycle

c10 should carry **火 / 习 / 也** with the specific composition fixes
above. Introduce 3 new chars to round out the batch — candidates:
- 巴 (4 strokes, frame-family extension)
- 力 (2 strokes — 横折钩 + 撇, drill the 横折钩 primitive)
- 心 (4 strokes, 4-点 composition with center 卧钩) — might be
  ambitious.
Safer pick: drill 力 and 巴; add a simpler filler like 已 or 上 (already
mastered — skip).

Recommendation: c10 = [火, 习, 也, 力, 巴, 已].
