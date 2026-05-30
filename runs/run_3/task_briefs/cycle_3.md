# Cycle 3 — Task brief (Phase 2 entry: simple characters)

First Phase-2 cycle. The 6 atomic strokes are now mastered and your
memory holds verified per-stroke recipes. This cycle tests
**composition**: combine those strokes into recognizable simple
characters at the right relative positions and proportions.

## Judgment — three signals, three meanings

Eval: **gt+ocr+vision**.

- **vision** — same calligraphy rubric as before (顿笔 / 弧度 / taper /
  proportion / overall, 0–2 each, /10). Mastery requires total ≥ 7
  with no 0 criterion. **Don't regress to thin uniform lines** to
  match the GT — the GT is a skeleton, your strokes have width by
  design.
- **gt** — composite shape-fidelity (Dice + Chamfer + proportion) vs
  the MakeMeAHanzi skeleton GT. A low absolute `visual_score` is
  *normal* for characters (cross-renderer; run_1 correct chars sat
  0.03–0.40). It is tracked for **regression** only — not a pass
  gate.
- **ocr** — RapidOCR must recognize the character (`is_correct: true`).
  Topology matters: correct stroke count and intersections.

Pass = `is_correct == true` AND `calligraphy_rubric.total >= 7`.

## Required calligraphic detail per stroke

Compose each character from the verified atomic-stroke recipes in
`drawer_memory.md`. Every constituent stroke must still have:
- 顿笔 at start/turn/end (weighted/rounded entries and presses),
- 弧度 only where appropriate (撇/捺/提 — slight bow; heng/shu stay
  near-straight),
- 粗细 taper varied along the centerline (point-by-point pensize),
- proportion / placement matching the relative layout below.

## Tasks (6) — Phase-2 entry pool

| idx | char | pinyin | strokes | composition tip |
|-----|------|--------|---------|----------------|
| 01  | 一   | yi     | 1 | one heng, centered horizontally |
| 02  | 二   | er     | 2 | two heng stacked; **bottom heng longer than top** |
| 03  | 三   | san    | 3 | three heng stacked; **bottom longest, middle shortest, top medium** |
| 04  | 十   | shi    | 2 | heng + shu crossing at center; shu extends slightly more below than above |
| 05  | 人   | ren    | 2 | 撇 + 捺 sharing top apex; **撇 starts higher and is longer than 捺**; equal limbs is wrong even if OCR passes |
| 06  | 八   | ba     | 2 | 撇 + 捺 with a **gap at the top** (no shared apex — unlike 人) |

For each task, render one 800×600 white-background black-ink PNG
saved as `attempts/cycle_3/<idx>_<char>.png`
(e.g. `01_一.png` … `06_八.png`). Filenames use the actual character
glyph in the name.

Your only inputs are `drawer_memory.md` and this brief. You will not
see the ground truths or any tool source.
