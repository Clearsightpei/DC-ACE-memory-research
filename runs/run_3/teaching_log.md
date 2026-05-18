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
