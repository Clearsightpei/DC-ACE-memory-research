# DC-ACE Dashboard — run_2 — last update: 2026-05-17

- **Cycle**: 1 (first cycle of fresh run_2, new composite judge)
- **Phase**: 1 (atomic strokes)
- **This cycle**: **2/6 mastered** (gate visual≥0.85) — heng 0.92 ✓, shu 0.92 ✓, dian 0.78, pie 0.71, na 0.70, ti 0.66
- **Last batch**: [dian, heng, shu, pie, na, ti] (the 6 atomic strokes)
- **OCR**: off (Phase 1, dataset judge.use_ocr=false) → final_score == visual_score
- **Avg visual**: 0.78
- **Memory size**: ~95 lines (first real memory written this cycle)
- **Curator note**: One root cause for all 4 misses — strokes drawn far too big and heavy vs the small/thin GTs. Memory codifies small+thin. heng/shu mastered.
- **Loop status**: running (delete runs/run_2/.stop to pause)

## Headline (cycle 1)

The new composite judge gives a usable cold-start gradient: a fresh
memoryless Drawer reached 0.92 on the two straight strokes and
0.66–0.78 on the curved/short ones — a real, monotonic signal (the
old phase-correlation metric scored ~0.05 for everything). The
failure is one clean, learnable mistake (scale + weight), exactly
the kind of seed the Curator can encode for cycle 2.

## Per-stroke status (Phase 1)

| stroke | char | visual | components | status |
|--------|------|--------|------------|--------|
| heng | 横 | 0.924 | dice .89 cham .98 prop .88 | mastered (retire) |
| shu  | 竖 | 0.922 | dice .91 cham .99 prop .81 | mastered (retire) |
| dian | 点 | 0.783 | dice .76 cham .84 prop .73 | carry over |
| pie  | 撇 | 0.706 | dice .61 cham .78 prop .75 | carry over |
| na   | 捺 | 0.703 | dice .60 cham .76 prop .79 | carry over |
| ti   | 提 | 0.662 | dice .58 cham .75 prop .65 | carry over |

## Recommendation to Teacher

Carry dian/pie/na/ti (mandatory, all <0.85 and pre-reflection). Do
not introduce new strokes or advance phase until these four clear
0.85 — depth over breadth. heng/shu retire.
