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

## Cycle 3 — 2026-05-30

- Phase: **2** (first Phase-2 cycle — phase advanced)
- Batch: [一, 二, 三, 十, 人, 八]
- Carry-overs: none — cycle 2 retired all 6 atomic strokes at 9.67/10
  avg with no criterion 0 (100% mastered post-reflection ≫ 80% gate).
  Phase-advance rationale recorded in teaching_plan.md.
- Tools (eval): **gt+ocr+vision** — characters get all three signals.
  Trustworthy GT from graphics.txt (make_char_gt.py), OCR guards
  recognizability, vision guards brush quality. use_ocr=true.
- Why this batch: six simple characters chosen to exercise every
  atomic primitive in composition. 一/二/三 stress heng-stacking with
  varying relative lengths (the bottom-heng-longest convention is the
  key risk). 十 tests heng+shu intersection. 人 vs 八 differentiates
  shared-apex (人) from gap-top (八) — also tests the
  撇-longer-than-捺 proportion rule (run_1's 人 failure mode).

## Cycle 4 — 2026-05-30

- Phase: 2
- Batch: [一, 二, 三, 十, 人, 八]
- Carry-overs: **ALL 6** — cycle 3 was 6/6 OCR but 0/6 mastered
  (rubric avg 5.67/10). Composition rules were applied correctly;
  brushwork degraded under composition. Carries over until clean
  post-reflection pass (run_3 mandatory carry-over rule).
- Tools (eval): **gt+ocr+vision** (same as c3). use_ocr=true.
- Why this batch: verify the Curator's two brushwork reflections
  (soften 顿笔 end-discs on heng/shu; fix inverted 捺 taper on 人/八).
  Composition rules stay — only brushwork is being repaired.
