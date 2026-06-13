# Cycle 33 — Focus: 力 (li)
## Phase
2 — character composition.
## MMH stroke count
2
## Strokes (anchors derived from MMH medians)
1. `draw_heng_zhe_gou(t, from=('ML', 0.364, 0.464), to=('BC', 0.444, 0.996))`
2. `draw_pie(t, from=('TC', 0.364, 0.368), to=('BL', -0.04, 1.3))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.228) ⇆ stroke 3 (frac 0.303) @ C (dist_mmh=0.0)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_33/generated.py + attempts/cycle_33/01_力.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
