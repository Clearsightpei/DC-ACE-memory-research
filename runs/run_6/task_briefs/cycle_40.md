# Cycle 40 — Focus: 目 (mu)
## Phase
2 — character composition.
## MMH stroke count
5
## Strokes (anchors derived from MMH medians)
1. `draw_shu(t, from=('TL', 0.576, 0.656), to=('BL', 0.684, 1.244))`
2. `draw_heng_zhe(t, from=('TL', 0.804, 0.704), to=('BC', 0.872, 1.02))`
3. `draw_heng(t, from=('ML', 0.844, 0.556), to=('C', 0.764, 0.42))`
4. `draw_heng(t, from=('BL', 0.836, 0.18), to=('BC', 0.776, 0.072))`
5. `draw_heng(t, from=('BL', 0.792, 1.064), to=('BC', 0.956, 0.948))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.062) ⇆ stroke 3 (frac 0.0) @ TL (dist_mmh=34.1)
- stroke 2 (frac 0.386) ⇆ stroke 4 (frac 0.0) @ ML (dist_mmh=33.6)
- stroke 2 (frac 0.621) ⇆ stroke 5 (frac 0.0) @ BL (dist_mmh=33.0)
- stroke 2 (frac 0.962) ⇆ stroke 6 (frac 0.0) @ BL (dist_mmh=35.4)
- stroke 3 (frac 1.0) ⇆ stroke 6 (frac 0.829) @ BC (dist_mmh=40.3)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_40/generated.py + attempts/cycle_40/01_目.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
