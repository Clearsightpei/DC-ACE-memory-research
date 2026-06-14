# Cycle 43 — Focus: 口 (kou)

## Phase
2 — character composition.

## MMH stroke count
3

## Joint-snap fix applied
Anchor heads (frac<0.15) and tails (frac>0.85) overridden with joint `meeting_canvas` coords from `find_joints`. Mid-stroke joints (frac 0.15-0.85) need no snap (the brush passes through naturally).

## Corner heuristic by primitive type
- heng_zhe / heng_zhe_gou / heng_gou / heng_zhe_wan_gou: geometric `(to_x, from_y)`
- shu_zhe / shu_gou / shu_wan_gou: geometric `(from_x, to_y)`
- heng_pie / heng_pie_wan_gou: MMH median max-x point

## Strokes
1. `draw_shu(t, from=('ML', 0.604, 0.314), to=('BL', 0.876, 0.845))`
2. `draw_heng_zhe(t, from=('ML', 0.604, 0.314), corner1=('MR', 0.076, 0.314), to=('BR', 0.076, 0.526))`
3. `draw_heng(t, from=('BL', 0.876, 0.845), to=('BR', 0.428, 0.652))`

## Joints
- s1(frac 0.122) ⇆ s2(frac 0.0) @ ML
- s1(frac 0.967) ⇆ s3(frac 0.0) @ BL
- s2(frac 1.0) ⇆ s3(frac 0.753) @ BR

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_43/generated.py + attempts/cycle_43/01_口.png
