# Cycle 38 — Focus: 山 (shan)
## Phase
2 — character composition.
## MMH stroke count
3
## Strokes (anchors derived from MMH medians)
1. `draw_shu(t, from=('TC', 0.34, 0.556), to=('BC', 0.424, 0.716))`
2. `draw_shu_zhe(t, from=('ML', 0.236, 0.956), to=('BR', 0.604, 0.6))`
3. `draw_shu(t, from=('MR', 0.692, 0.588), to=('BR', 0.644, 1.3))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 1.0) ⇆ stroke 3 (frac 0.613) @ BC (dist_mmh=43.6)
- stroke 3 (frac 0.974) ⇆ stroke 4 (frac 0.627) @ BR (dist_mmh=48.6)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_38/generated.py + attempts/cycle_38/01_山.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
