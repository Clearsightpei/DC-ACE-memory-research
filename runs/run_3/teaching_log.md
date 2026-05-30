<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-05-17

- Phase: 1
- Batch: [dian, heng, shu, pie, na, ti]
- Carry-overs: none (cold start, fresh run_3).
- Tools (eval): **vision** — strokes only; NO GT generated. The
  hand-coded stroke GT is a weaker reference than the model's own
  strokes (runs/run_2/POSTMORTEM.md), so judging strokes by it would
  degrade calligraphy. The Claude-vision calligraphy rubric judges
  brush quality directly. use_ocr=false (strokes are not characters).
- Why this batch: cold start lays the 6 atomic strokes (the
  constituents of every character) in one pass; carry-over rule then
  drills whichever fall below the 7/10 rubric gate. Rubric calibrated
  on run_1 (crude-but-correct ≈3–4/10) — recorded in teaching_plan.md.

## Cycle 2 — 2026-05-30

- Phase: 1
- Batch: [dian, heng, shu, pie, na, ti]
- Carry-overs: **all 6** — cycle 1 was a cold-start with no memory.
  This is the post-reflection confirmation cycle: the Drawer now has
  the cycle-1 brushed-recipes memory; we verify the recipes survive
  the lossy memory transfer (and that 撇/提 弧度=1 can nudge to 2).
- Tools (eval): **vision** (no GT). Same rationale as cycle 1 —
  hand-coded stroke GT is a weaker reference than the model's strokes
  (runs/run_2/POSTMORTEM.md); the rubric judges brush quality directly.
  use_ocr=false.
- Why this batch: mastery requires a clean post-reflection pass. If
  6/6 hold ≥7 with no 0, all six retire and cycle 3 advances to
  Phase 2 (1–4 stroke characters, eval=gt+ocr+vision).
