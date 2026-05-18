# DC-ACE Dashboard — run_3 — last update: 2026-05-17

- **Cycle**: 1  | **Phase**: 1 (atomic strokes) | **eval**: vision (no GT)
- **Result**: 6/6 strokes 9–10/10 (avg rubric **9.5/10**); 0 criteria == 0
- **Batch**: [dian, heng, shu, pie, na, ti]
- **vs run_1** (same rubric on its crude-but-OCR-correct chars): 3–4/10
- **Curator note**: thesis validated — removing the weak stroke GT and
  judging strokes by Claude-vision lets a cold-start Drawer produce
  real brush calligraphy (taper + 顿笔). Memory seeded with the
  brushed recipes.
- **Loop status**: running (delete runs/run_3/.stop to pause)

## Headline (cycle 1)

The architecture change works. run_2's pathology was that GT-matching
judging *coached the model down* to a crude hand-coded reference;
run_3 cycle 1 shows that when strokes are judged on calligraphic
merit by Claude-vision instead, the very first memoryless attempt is
brush-quality (9.5/10) — an order-of-magnitude better signal than the
old stroke GT permitted. The Teacher-as-tool-orchestrator design and
the per-run POSTMORTEM chain are in place.

## Rubric (per stroke, /10)

| stroke | dunbi | hudu | taper | prop | overall | total |
|--------|-------|------|-------|------|---------|-------|
| 点 dian | 2 | 2 | 2 | 2 | 2 | 10 |
| 横 heng | 2 | 1 | 2 | 2 | 2 | 9 |
| 竖 shu  | 2 | 2 | 2 | 2 | 2 | 10 |
| 撇 pie  | 2 | 1 | 2 | 2 | 2 | 9 |
| 捺 na   | 2 | 2 | 2 | 2 | 2 | 10 |
| 提 ti   | 2 | 1 | 2 | 2 | 2 | 9 |

## Recommendation to Teacher

One carry-over cycle to confirm post-reflection stability (rubric
should hold ≥7, no 0). Then advance to Phase 2 simple characters
(1–4 strokes via `list_chars.py --min 1 --max 4`, eval=gt+ocr+vision).
