# Cycle 36 — Focus: 八 (ba)
## Phase
2 — character composition.
## MMH stroke count
2
## Strokes (anchors derived from MMH medians)
1. `draw_pie(t, from=('ML', 0.776, 0.668), to=('BL', -0.192, 1.056))`
2. `draw_na(t, from=('TC', 0.26, 0.768), to=('BR', 1.3, 0.96))`

## Joints (from `tools/joint_detector.find_joints`)
None (non-touching strokes).

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_36/generated.py + attempts/cycle_36/01_八.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
