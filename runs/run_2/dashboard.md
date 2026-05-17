# DC-ACE Dashboard — run_2 — last update: 2026-05-17

- **Cycle**: 2  | **Phase**: 1 (atomic strokes)
- **This cycle**: pie ✓0.94, ti ✓0.93 (×2 stable) newly mastered; dian 0.74, na 0.60 still < gate
- **Mastered (4/6 atomic)**: heng 0.92, shu 0.92, pie 0.94, ti 0.93
- **Open (2)**: dian (draw as a line → must be `t.dot`), na (curve bows wrong way — concave-down vs GT concave-up)
- **Last batch**: [dian, pie, na, ti, na, ti]  | **OCR**: off (Phase 1)
- **Avg visual**: 0.79
- **Curator note**: Memory transfer confirmed — the cycle-1 reflection lifted pie +0.23 and ti +0.27 over the gate. na regressed (wrong curve direction, now corrected to t.right/steeper); dian needs t.dot not a line.
- **Loop status**: running (delete runs/run_2/.stop to pause)

## Headline (cycle 2)

The new composite judge + memory loop is working as designed: a
single Curator reflection ("small + thin, no blob" + recipes),
applied by a fresh Drawer, moved pie and ti from clear failures
(0.66–0.71) to mastered (0.93–0.94) in one cycle — and the duplicate
ti attempts scored identically (0.932/0.932), showing the score is
stable, not noisy, at the stroke level. The remaining two failures
are now precise, actionable shape errors (dian: line vs dot; na:
inverted curvature), exactly the kind the gate is meant to drill out
before any phase advance.

## Per-stroke status (Phase 1)

| stroke | char | c1 | c2 | status |
|--------|------|----|----|--------|
| heng | 横 | 0.92 | — | mastered |
| shu  | 竖 | 0.92 | — | mastered |
| pie  | 撇 | 0.71 | 0.94 | mastered (post-reflection) |
| ti   | 提 | 0.66 | 0.93 | mastered (post-reflection, ×2 stable) |
| dian | 点 | 0.78 | 0.74 | carry — must be t.dot, not a line |
| na   | 捺 | 0.70 | 0.60 | carry — curve inverted; fix = t.right + steeper |

## Recommendation to Teacher

Carry dian + na (mandatory, <0.85). Fill batch with drills of the
two (and/or stable re-confirm of a mastered one for variance data) —
do NOT introduce new strokes or advance phase until dian & na clear
0.85. heng/shu/pie/ti retire.
