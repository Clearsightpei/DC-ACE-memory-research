# Cycle 34 — Focus: 又 (you)
## Phase
2 — character composition.
## MMH stroke count
2
## Strokes (anchors derived from MMH medians)
1. `draw_heng_pie(t, from=('ML', 0.516, 0.048), to=('BL', 0.032, 1.22))`
2. `draw_na(t, from=('ML', 0.536, 0.36), to=('BR', 1.3, 1.26))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.64) ⇆ stroke 3 (frac 0.368) @ BC (dist_mmh=0.0)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_34/generated.py + attempts/cycle_34/01_又.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
