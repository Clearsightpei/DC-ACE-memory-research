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

## Cycle 5 — 2026-05-30

- Phase: 2
- Batch: [大, 入, 上, 下, 七, 山]
- Carry-overs: none — c4 retired all 6 of c3/c4's batch
  (一二三十人八) at 9.00/10 avg, post-reflection. New Phase-2
  expansion batch.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: three goals — (1) stress the c4 soft gap on 捺 flat
  tail kick (大, 入 — both 撇+捺 chars), (2) test vertical-stacking
  composition (上, 下 — uses 点 in 下 for the first time in a
  character), (3) introduce two new compound strokes: 七 brings the
  竖弯-钩-family turn, 山 brings the 竖折 corner. Partial success
  expected on the compound strokes; the resulting Curator diagnosis
  is the experimental data we want.

## Cycle 6 — 2026-05-30

- Phase: 2
- Batch: [大, 入, 上, 下, 七, 山]
- Carry-overs: **ALL 6** — c5 was 4/6 OCR but 0/6 mastered.
  Mandatory carry-over rule applied; each task tests a specific
  Curator reflection.
- Tools (eval): **gt+ocr+vision** (same as c5). use_ocr=true.
- Why this batch: verify three c5 reflections — (a) 大 topology
  (撇/捺 apex above heng with heng cutting through), (b) 入 topology
  (捺 on 撇's spine, asymmetric), (c) brushed width on every stroke
  including short ones (上, 下) and compound primitives (七 竖弯,
  山 竖折). c4 → c6 mirrors c3 → c4: a hard-fail cycle followed by a
  reflection-validation cycle.

## Cycle 7 — 2026-05-30

- Phase: 2
- Batch: [大, 入, 又, 个, 不, 木]
- Carry-overs: **2** (大, 入) — c6 fixes half-landed; numeric
  refinements in `drawer_memory.md` (heng ≥ 1.4× limb span; 入
  junction at 45–55% down 撇). The other 4 c6 chars (上, 下, 七,
  山) retired at 8–9/10 post-reflection.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: drill the 撇+捺 composition family while c7 stress-
  tests the c6 numeric fixes. 又 introduces 横撇 (a new compound
  stroke). 个 mirrors 人 + a center shu. 不 / 木 add a center shu to
  a 撇/捺 composition — 木 is the canonical "cross with diagonal
  limbs" composition.

## Cycle 8 — 2026-05-30

- Phase: 2
- Batch: [大, 入, 工, 王, 火, 中]
- Carry-overs: **2** (大, 入). c7 retired 又/个/不/木 first attempt.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: stricter numeric prescription on 大 (heng ≥ 2.0×)
  and amplified 入 asymmetry. The four new chars introduce: 工/王
  (horizontal heng-stacking new layout), 火 (two 点 + 撇 + 捺
  composition, brand new for the run), 中 (first 横折 in a frame —
  introduces the boxed-frame composition that all 田/口/日/目/etc.
  characters will use later).

## Cycle 9 — 2026-05-30

- Phase: 2
- Batch: [火, 口, 子, 习, 也, 日]
- Carry-overs: **1** (火). 大 and 入 RETIRED under "OCR-wall" status
  — by c8 both had geometrically-textbook silhouettes and rubric
  8–9/10 but RapidOCR consistently rejected both. Memory documents
  this finding; no more cycles on them unless RapidOCR is replaced.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: introduce the frame family (口, 日) building on c8's
  successful 中 横折, and stress-test the 钩 (hook) family across
  three different 钩 compounds (子's 竖钩, 习's 提-ending family,
  也's 横折钩 + 竖弯钩). 钩 strokes are a major remaining gap.

## Cycle 10 — 2026-05-30

- Phase: 2
- Batch: [火, 习, 也, 力, 巴, 已]
- Carry-overs: **3** (火, 习, 也). Each tests a specific Curator
  composition fix from c9. The other c9 chars (口/子/日) retired
  first-attempt.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: drill the 钩 family further (力 has 横折钩 + 撇;
  巴 and 已 both feature 竖弯钩 as the signature bottom stroke). 力
  is also a compact 2-stroke check on whether the 横折钩 primitive
  generalizes outside of 习/也.

## Cycle 11 — 2026-05-30

- Phase: 2
- Batch: [火, 也, 力, 巴, 月, 见]
- Carry-overs: **4** (火, 也, 力, 巴). 火 is final attempt before
  documented retire as OCR-wall. 也/力/巴 each test a specific c10
  composition prescription.
- Tools (eval): **gt+ocr+vision**. use_ocr=true.
- Why this batch: close out the active-failure list with refined
  prescriptions, then introduce 月 and 见 — both frame-with-interior-
  hooks compositions building on c9/c10's 横折钩 mastery.
