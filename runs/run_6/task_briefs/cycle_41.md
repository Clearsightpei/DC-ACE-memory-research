# Cycle 41 — Focus: 白 (bai)
## Phase
2 — character composition.
## MMH stroke count
5
## Strokes (anchors derived from MMH medians)
1. `draw_pie(t, from=('TC', 0.248, 0.312), to=('ML', 0.7, 0.404))`
2. `draw_shu(t, from=('ML', 0.188, 0.412), to=('BL', 0.62, 1.196))`
3. `draw_heng_zhe(t, from=('ML', 0.392, 0.436), to=('BR', 0.232, 1.3))`
4. `draw_heng(t, from=('BL', 0.6, 0.208), to=('BC', 0.932, 0.128))`
5. `draw_heng(t, from=('BL', 0.696, 0.948), to=('BR', 0.072, 0.904))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 1.0) ⇆ stroke 4 (frac 0.097) @ ML (dist_mmh=30.6)
- stroke 3 (frac 0.071) ⇆ stroke 4 (frac 0.0) @ ML (dist_mmh=29.2)
- stroke 3 (frac 0.417) ⇆ stroke 5 (frac 0.0) @ BL (dist_mmh=44.6)
- stroke 3 (frac 0.822) ⇆ stroke 6 (frac 0.0) @ BL (dist_mmh=44.3)
- stroke 4 (frac 0.942) ⇆ stroke 6 (frac 1.0) @ BR (dist_mmh=66.8)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_41/generated.py + attempts/cycle_41/01_白.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
