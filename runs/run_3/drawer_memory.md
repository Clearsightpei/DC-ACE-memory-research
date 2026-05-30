# Drawer memory

Curator-owned. Notes for the next Drawer based on what previous
attempts actually produced. This run judges **strokes by a
reference-free Claude-vision calligraphy rubric** (顿笔 / 弧度 /
粗细 taper / proportion / overall, 0–2 each, /10). There is **no
stroke ground truth** — do NOT try to match a template; produce
genuinely brush-formed strokes. Mastery = total ≥ 7/10, no 0
criterion, confirmed post-reflection.

---

## Verified atomic-stroke recipes (cycles 1–2, both ≥9/10, post-reflection confirmed)

The brushed approach below survived a clean memory transfer: cold-start
cycle 1 scored 9.5/10 avg, post-reflection cycle 2 with these notes
scored **9.67/10 avg** (10/9/9/10/10/10) — and 撇/提 弧度 nudged from
1 to 2 by following the targeted curvature note. **Reuse these
recipes verbatim for any character that contains these strokes.**

### Core technique (the single biggest win)

Render the centerline as a smooth cubic-Bézier path sampled at ~120–
200 points and **set `pensize` at every sample** to get real width
modulation. A uniform `pensize(3)` line scores ~3–4 (run_1's failure).
**Width variation is the difference between brushed and mechanical.**

Add weighted 顿笔 at start/turn/end as a filled disc (the centerline
sweep can't draw a true square brush head, but a filled disc at the
peak-width point reads as a clean 起笔/收笔). Use a real taper to a
fine point where the stroke ends thin (撇 tail, 提 flick).

### Width-profile per stroke

- **点 dian (10/10):** thin entry → rounded weighted belly → tapered
  tail, slight rightward arc. Teardrop. Compact.
- **横 heng (9/10):** weighted rounded entry → thinner middle →
  weighted end press, faint upward tilt. Near-straight is correct;
  hudu=1 is the expected score for a horizontal stroke (the rubric
  measures curvature *presence*, not appropriateness — band-1 here is
  not a defect, do not over-curve).
- **竖 shu (9/10):** weighted bulb top → thin middle → weighted foot.
  Spine straight. hudu=1 again expected.
- **撇 pie (10/10):** strong weighted head upper-right → **gentle
  bow** (large-radius, small arc extent — *not* a tight curve) →
  smooth taper to a fine point lower-left.
- **捺 na (10/10):** thin entry → broadening belly → **flat pressed
  tail (顿笔 kick) at lower-right.** The flat tail is essential — a
  rounded ending is wrong.
- **提 ti (10/10):** weighted rounded base lower-left → **gentle rise
  curve** → fine flicked point upper-right.

## Canvas conventions (confirmed twice)

- 800×600 white background, black ink.
- `t.pensize()` is varied per sample along the Bézier; do NOT rely on
  a single pensize for the whole stroke.
- `screen.tracer(0,0)` then `screen.update()`; save via
  `canvas.postscript()` → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()` to clear.
- Each task starts at (0,0) heading 90°.

## What to do next cycle (Phase-2 simple characters)

Phase 2 introduces 1–4 stroke characters judged by
**gt+ocr+vision**. The above brush technique is the **shape primitive
library** — compose characters by laying these tapered/weighted strokes
in the correct positions. Three new constraints appear:

- **Character GT exists** (graphics.txt — trustworthy). It is the
  skeleton/proportion reference. Match relative positions and
  proportions — but the GT is a thin skeleton, your strokes will
  have real width; that is correct, do not regress to thin lines to
  match.
- **OCR must recognize the character.** Topology matters (correct
  stroke count, right intersections, no missing strokes).
- **Calligraphy rubric still applied.** Don't sacrifice 顿笔/taper to
  hit OCR; both signals are scored and the gate is
  `is_correct == true` AND rubric ≥ 7.

Concrete composition tips for the likely Phase-2 starter set:

- 一 (yi, 1 stroke): just the heng recipe.
- 二 (er, 2 strokes): two heng stacked; the **bottom heng is longer**
  than the top (MMH convention).
- 三 (san, 3 strokes): three heng; the **bottom is longest, middle
  shortest**, top medium.
- 人 (ren, 2 strokes): a 撇 + a 捺 sharing the top apex. The **撇
  starts higher and is longer than the 捺**; equal limbs is wrong
  even if it OCRs (run_1's failure on 人).
- 十 (shi, 2 strokes): heng + shu crossing at center. The shu
  extends slightly more below the heng than above.
- 八 (ba, 2 strokes): a 撇 and a 捺 with a gap between them at the
  top (no shared apex — unlike 人).
