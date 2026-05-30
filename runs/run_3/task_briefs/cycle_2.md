# Cycle 2 — Task brief (Phase 1, post-reflection confirmation)

This is the **post-reflection** cycle for the six atomic strokes
introduced in cycle 1. Your memory file now codifies the brushed
approach that scored 9–10/10. Reproduce strokes of equivalent or
better quality — do **not** regress to thin uniform lines.

## Judgment

Eval signal: **vision** (reference-free Claude-vision calligraphy
rubric — 顿笔 / 弧度 / 粗细 taper / proportion / overall, 0–2 each,
total /10). There is **no ground truth** for strokes this cycle.
Mastery on each item: total ≥ 7/10 with no criterion == 0.

## Required calligraphic detail (every stroke)

- **顿笔** — a weighted/rounded pause at the start and end (and turns).
- **弧度** — natural curvature where appropriate (slight on 撇/提;
  near-straight is correct for 横/竖).
- **粗细 / taper** — vary `pensize` point-by-point along the centerline
  (a uniform pen line is the run_1 failure mode — avoid it).
- **proportion** — sized and placed so the stroke reads centered and
  balanced on the canvas.

## Tasks (6) — carry-overs from cycle 1

| idx | key  | name | meaning |
|-----|------|------|---------|
| 01  | dian | 点   | dot |
| 02  | heng | 横   | horizontal |
| 03  | shu  | 竖   | vertical |
| 04  | pie  | 撇   | left-falling |
| 05  | na   | 捺   | right-falling |
| 06  | ti   | 提   | rising flick |

For each task, render one 800×600 white-background black-ink PNG
saved as `attempts/cycle_2/<idx>_<key>.png`
(e.g. `01_dian.png` … `06_ti.png`).

Soft improvement areas the Curator flagged on cycle 1 (弧度 scored 1
on heng/pie/ti): give 撇 and 提 a *gentle* natural bow (large-radius,
small-arc curvature — not a tight curve). 横 and 竖 are meant to be
near-straight; leave them.

Your only inputs are `drawer_memory.md` and this brief.
