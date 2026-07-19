# run_2 — Postmortem

**Run:** run_2 — first run on the **composite shape-fidelity judge**
(Dice + Chamfer + proportion) with Teacher-controlled OCR and the
non-rushing Teacher. 3 cycles, Phase 1 (atomic strokes), then frozen.

## The core problem this run surfaced

**The hand-coded stroke ground truths were *weaker calligraphy* than
the model's own strokes, so GT-matching judging actively degraded
quality.**

The Phase-1 stroke GTs come from `tools/strokes.py` +
`make_stroke_gt.py` — hand-written turtle paths: thin, uniform
pensize-3 lines with no 顿笔 (pause/weight), no taper, no real 弧度.
In cycle 1 the fresh Drawer, from prior knowledge alone, produced
strokes with genuine brush character (tapered, weighted, curved) —
**better calligraphy than the references**. But because the judge
scores similarity *to the GT*, those richer strokes were penalised,
and the Curator (correctly, given the metric) wrote memory telling the
Drawer to "draw small and light, no blob" — i.e. it coached the model
*down* to match a cruder teacher. By cycle 3 the model had regressed
toward thin lines to chase the GT.

Key realisation: this pathology is **specific to strokes**. Character
GTs come from `draw_character/graphics.txt` (MakeMeAHanzi — 9,574
standard real-glyph median skeletons) and are *trustworthy*; the
weak-reference problem does not exist there. The instrument was right
for characters, wrong for hand-coded strokes.

A secondary, related observation: `na` was mis-diagnosed by the
Curator twice (heading-math reflections that were faithfully applied
yet wrong, 0.70→0.60→0.24) — a clean reflection-falsification signal,
but it also showed how much the Curator's pixel-vs-GT reasoning could
mislead when the GT itself is not the right target.

## Why it motivated the next run

This motivated **run_3**: **keep teaching strokes, but judge strokes
with the Claude-vision rubric (reference-free), not the weak
hand-coded GT**, and make the **Teacher a tool-orchestrator** — it
chooses, per cycle, which evaluation tool to use (hand-coded stroke
GT, graphics.txt character GT, Claude-vision rubric, OCR), with the
single ultimate goal of teaching the Drawer to draw the best
*characters* possible. run_2 is preserved unchanged as the
"weak-stroke-GT-era" record.
