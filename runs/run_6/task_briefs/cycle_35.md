# Cycle 35 — Focus: 七 (qi)
## Phase
2 — character composition.
## MMH stroke count
2
## Strokes (anchors derived from MMH medians)
1. `draw_heng(t, from=('BL', -0.144, 0.188), to=('MR', 0.98, 0.704))`
2. `draw_shu_wan_gou(t, from=('TL', 0.908, 0.548), to=('BR', 0.588, 1.1))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.398) ⇆ stroke 3 (frac 0.38) @ C (dist_mmh=0.0)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_35/generated.py + attempts/cycle_35/01_七.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
