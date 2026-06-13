# Cycle 39 — Focus: 五 (wu)
## Phase
2 — character composition.
## MMH stroke count
4
## Strokes (anchors derived from MMH medians)
1. `draw_heng(t, from=('TL', 0.668, 0.772), to=('TR', 0.464, 0.616))`
2. `draw_shu(t, from=('TC', 0.292, 0.896), to=('BL', 0.9, 0.876))`
3. `draw_heng_zhe(t, from=('ML', 0.544, 0.808), to=('BC', 0.82, 0.832))`
4. `draw_heng(t, from=('BL', -0.296, 1.076), to=('BR', 1.3, 1.108))`

## Joints (from `tools/joint_detector.find_joints`)
- stroke 2 (frac 0.287) ⇆ stroke 3 (frac 0.0) @ TC (dist_mmh=39.3)
- stroke 3 (frac 0.435) ⇆ stroke 4 (frac 0.253) @ C (dist_mmh=0.0)
- stroke 3 (frac 0.973) ⇆ stroke 5 (frac 0.314) @ BL (dist_mmh=48.5)
- stroke 4 (frac 1.0) ⇆ stroke 5 (frac 0.552) @ BC (dist_mmh=36.9)

## Eval gates
- stroke_count == mmh_stroke_count
- anchor placement within 30 px
- joint placement < 20 px AND meeting falls in declared cell
- visual_score informational
- 3-judge panel unanimous YES required for promotion

## Output
attempts/cycle_39/generated.py + attempts/cycle_39/01_五.png

## Drawer instructions
Compose by anchor — call each `draw_<primitive>` with its `from`/`to` exactly as specified above. NO magic numbers, NO inline primitive code. Imports go through `success_bank/code/`. Stroke order must match the brief (MMH order).
