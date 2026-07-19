# run_1 — Postmortem

**Run:** run_1 (originally `dc_ace_run`) — the first full experiment.
12 cycles, completed and frozen. Judge: the **original
phase-correlation** visual metric (`cv2.phaseCorrelate` on the full
800×600 image) + RapidOCR.

## The core problem this run surfaced

**The reward signal was noisy, non-monotonic, and OCR was
over-trusted.**

1. **Phase-correlation `visual_score` was not monotonic with human
   perception.** Strokes that were visually *closer* to the ground
   truth sometimes scored *lower* than cruder ones (documented in this
   run's own dashboard/curator notes around cycles 5 and 10 — e.g. a
   better-formed `na`/`heng_zhe` scored below a worse one). The metric
   was translation-only and frequency-domain, so it was effectively
   blind to fine calligraphic detail (顿笔, 小折, 弧度) and produced a
   gradient the Curator could not reliably learn from. Several cycles'
   "regressions" were metric noise, not real quality loss.

2. **OCR was over-relied on in Phase 2/3.** `is_correct` was the pass
   signal for characters, but RapidOCR will happily recognise a glyph
   that is obviously wrong to a human (e.g. 人 drawn with 撇 and 捺 the
   same length when the 撇 must be longer and start higher). As
   characters got harder this became a weak, misleading learning
   signal.

The emergent-memory mechanism itself worked (faithful transfer,
falsification/correction arcs like the 天 case were observed) — the
bottleneck was the *measuring instrument*, not the memory loop.

## Why it motivated the next run

These two findings motivated **run_2**: a **composite shape-fidelity
judge** (Dice overlap + symmetric Chamfer + proportion — monotonic,
detail-sensitive, calibrated so faithful single strokes ≈0.94–1.00),
**OCR demoted to a Teacher-configurable secondary aid**, a
**non-rushing Teacher** with a fidelity gate, and the single-repo
consolidation. run_1 is preserved unchanged as the phase-correlation
baseline; its granular cycle history is also archived at the
`dc-ace-run` GitHub repo.
