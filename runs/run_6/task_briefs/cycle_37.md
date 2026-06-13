# Cycle 37 — Focus: 人 (ren)
## Phase
2 — character composition.
## MMH stroke count
2
## Strokes (anchors derived from MMH medians)
1. `draw_pie(t, from=('TC', 0.384, 0.604), to=('BL', -0.26, 1.168))`
2. `draw_na(t, from=('C', 0.348, 0.64), to=('BR', 1.3, 1.188))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.31) ⇆ stroke 3 (frac 0.027) @ C (dist_mmh=51.2)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_37/generated.py + attempts/cycle_37/01_人.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
