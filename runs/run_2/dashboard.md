# DC-ACE Dashboard — run_2 — last update: 2026-05-17

- **Cycle**: 3  | **Phase**: 1 (atomic strokes)
- **This cycle**: dian ✓0.93 newly mastered; pie ✓0.94 / ti ✓0.93 regression-stable; na ✗0.24 (worse)
- **Mastered (5/6 atomic)**: heng 0.92, shu 0.92, pie 0.94, ti 0.93, dian 0.93
- **Open (1)**: **na** — 0.70 → 0.60 → 0.24, Curator mis-diagnosed twice
- **Last batch**: [dian, na, dian, na, pie, ti]  | **OCR**: off (Phase 1)
- **Avg visual**: 0.70
- **Curator note**: na's two heading-based reflections were both wrong and faithfully applied (0.60→0.24, near-vertical). Switched memory to an explicit-points recipe read straight off the GT (gentle ~45° down-right, slight concave-up, flattening tail).
- **Loop status**: running (delete runs/run_2/.stop to pause)

## Headline (cycle 3)

Two clean research signals: (1) **memory transfer keeps working** —
the `t.dot` reflection took dian from a failing line (0.74) to a
mastered dab (0.93) in one cycle, and the regression check shows
mastered recipes stay stable across memory edits. (2) **The
reflection-falsification dynamic is live**: na's curvature has been
mis-diagnosed by the Curator twice in a row, each wrong recipe
faithfully executed by a fresh Drawer and each making the score
worse (0.70→0.60→0.24). The corrective response — abandon ambiguous
heading math for an explicit-point recipe read directly from the GT
— is exactly the kind of memory repair the carry-over gate is built
to force. na is now the sole Phase-1 blocker.

## Per-stroke status (Phase 1)

| stroke | char | c1 | c2 | c3 | status |
|--------|------|----|----|----|--------|
| heng | 横 | 0.92 | — | — | mastered |
| shu  | 竖 | 0.92 | — | — | mastered |
| pie  | 撇 | 0.71 | 0.94 | 0.94 | mastered (stable) |
| ti   | 提 | 0.66 | 0.93 | 0.93 | mastered (stable) |
| dian | 点 | 0.78 | 0.74 | 0.93 | mastered (t.dot fix) |
| na   | 捺 | 0.70 | 0.60 | 0.24 | OPEN — explicit-points recipe queued |

## Recommendation to Teacher

Carry **na** only (mandatory, ≪0.85). Fill the batch with na drills
(and optionally 1–2 mastered regression checks); do NOT introduce
new strokes or advance phase until na ≥ 0.85. Once na clears, all 6
atomic strokes are mastered and Phase 2 may be considered.
