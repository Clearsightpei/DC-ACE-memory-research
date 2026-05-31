# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.
**Hard no-skip**: `is_correct == false` OR `ocr_confidence < 0.4`
→ MUST carry over. Quality > coverage.

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
| 提     | start | end |
| 点     | belly | tail |

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩.

## Canvas conventions

- 800×600 white; per-sample pensize on Bézier.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (25 mastered through c13)

- 1–2 strokes: 一, 二, 十, 人, 八, 又, 入, 力.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已, 大.
- 4 strokes: 不, 木, 王, 中, 日, 月.

**力 (c13 fix):** 撇 head must visibly cross the top heng (撇 head
at y > heng_y, then sweep DOWN through and out lower-left). Top heng
extends well to the LEFT of the 横折钩's corner (heng start ≈ −150,
corner ≈ +80). Without the visible cross-through, OCR reads 刀.

## Active carry-overs

c13 attempted all 5 prior + 1 new (天); 1 mastered. Refined diagnoses:

- **火 (6 attempts).** c13 had apex height for 点 (closer than c12),
  but OCR returned 人. Issue: visible apex stub above 撇/捺 meeting
  point + 点 too close to apex sides. **Next fix:** REMOVE the apex
  stub entirely (apex is just the meeting point; no extra vertical
  above it); push 点 further outward (x ±100, not ±60) so they
  clearly sit beside the apex as flanking ears.

- **也 (5 attempts).** c13 changed failure mode: OCR returned 山
  (not 卫). The bottom wraparound now reads like 山's bottom + 凵.
  **Next fix:** 横折钩 needs a visible 钩 hook at its bottom-left
  end (currently looks like a 横折); make middle shu thinner so it
  doesn't compete with the 横折钩 for visual weight.

- **巴 (4 attempts).** c13 tri-decker landed — OCR's 已-prior broken
  (returned 县 instead of 已). Progress but not mastery. **Next
  fix:** widen the upper frame further so it visibly dominates; OR
  add a small horizontal at the very top of the 竖弯钩 to suggest
  the 巳/巴 differentiator.

- **见 (2 attempts).** c13 撇 diverged slightly but OCR still 月.
  **Next fix:** make the 撇 a DISTINCT third stroke that exits the
  frame's bottom-left at a clear diagonal (sweep length 150+ px
  going down-LEFT at ~45°).

- **天 (1 attempt).** OCR returned 元. Composition is right (two
  heng stacked, 撇/捺 below); the 捺 might lack a strong enough
  flat-tail to read as 捺 rather than a hooked stroke. **Next fix:**
  emphasize the 捺's flat horizontal kick at the tail (last 15% of
  the stroke horizontal, near-peak width).

## Soft / completed observations

- c12-c13 confirmed: "OCR-wall" was rationalization. Concrete
  composition prescriptions are the right response to OCR rejection.
- Frame family + 钩 family both mature.

## What to do next cycle

c14 backlog = 5 (火, 也, 巴, 见, 天). Backlog < 6 → 1 new char
allowed. Strong recommendation: focus on the carry-overs with the
clearest next-fixes (all 5 have them) and add 1 simple new char
that doesn't risk new OCR confusions. Candidates:
- 几 (2 strokes) — could intro 横折弯钩 family.
- 了 (2 strokes) — could intro 横钩 (top heng with corner).
- 之 (3 strokes) — 点 + 横撇 + 捺.
- 也→也 is what we're working on, skip similar shapes.
Recommended c14 6th slot: **了** (simple 2-stroke, intro 横钩).
