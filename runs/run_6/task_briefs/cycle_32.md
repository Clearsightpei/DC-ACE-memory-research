# Cycle 32 — Focus: 口 (kou)
## Phase
2 — character composition.
## MMH stroke count
3
## Strokes (anchors derived from MMH medians)
1. `draw_shu(t, from=('ML', 0.368, 0.212), to=('BL', 0.844, 0.94))`
2. `draw_heng_zhe(t, from=('ML', 0.668, 0.272), to=('BR', 0.096, 0.456))`
3. `draw_heng(t, from=('BL', 0.928, 0.808), to=('BR', 0.428, 0.652))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.122) ⇆ stroke 3 (frac 0.0) @ ML (dist_mmh=38.3)
- stroke 2 (frac 0.967) ⇆ stroke 4 (frac 0.0) @ BL (dist_mmh=32.1)
- stroke 3 (frac 1.0) ⇆ stroke 4 (frac 0.753) @ BR (dist_mmh=36.4)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_32/generated.py + attempts/cycle_32/01_口.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
