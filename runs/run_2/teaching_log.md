<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-05-17

- Phase: 1
- Batch: [dian, heng, shu, pie, na, ti]
- Carry-overs: none (cold start, first cycle of a fresh run).
- OCR: off (Phase 1 strokes — dataset judge.use_ocr=false).
- Why this batch: Depth-over-breadth curriculum starts at the
  foundation. The 6 atomic strokes are the constituents of every
  compound stroke and character, and batch size is exactly 6, so the
  first cycle lays the entire atomic foundation in one pass. The
  mandatory carry-over rule will then drill whichever atomic strokes
  fall below the 0.85 fidelity gate until their calligraphic detail
  (弧度/顿笔/flick) is actually produced. No advancement past Phase 1
  until all six are mastered post-reflection.

## Cycle 2 — 2026-05-17

- Phase: 1
- Batch: [dian, pie, na, ti, na, ti]
- Carry-overs: dian/pie/na/ti — all <0.85 in cycle 1 and now
  post-reflection (memory got the "small+thin, no blob" diagnosis +
  per-stroke recipes). This cycle tests whether that reflection
  works. heng/shu retired (mastered 0.92 cycle 1).
- OCR: off (Phase 1 strokes; dataset judge.use_ocr=false).
- Why this batch: Depth-over-breadth / no-skipping gate forbids
  introducing new strokes while these four are unmastered. Batch
  size is 6, so the two weakest (ti 0.66, na 0.70) are drilled twice
  (idx 05/06) for extra signal/variance rather than padding with new
  material. No phase advance until all of dian/pie/na/ti clear 0.85.

## Cycle 3 — 2026-05-17

- Phase: 1
- Batch: [dian, na, dian, na, pie, ti]
- Carry-overs: dian (still 0.74, must become a t.dot not a line) and
  na (regressed 0.70→0.60, curve was inverted — memory corrected to
  t.right + steeper, concave-up). Both drilled twice (idx 01/03,
  02/04) for stability signal. idx 05/06 re-test mastered pie & ti
  as a regression check that the memory restructure didn't break
  their recipes.
- OCR: off (Phase 1; dataset judge.use_ocr=false).
- Why this batch: No-skipping gate — cannot introduce new strokes or
  advance phase while dian & na are < 0.85. Slots spent on the two
  open strokes' corrected fixes plus a cheap regression check on the
  two most-recently-mastered strokes.
