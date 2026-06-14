# Cycle 48 — Focus: 山 (shan)

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
1. `draw_shu(t, from=('TC', 0.34, 0.556), to=('BC', 0.37, 0.785))`
2. `draw_shu_zhe(t, from=('ML', 0.236, 0.956), corner1=('BL', 0.236, 0.659), to=('BR', 0.637, 0.659))`
3. `draw_shu(t, from=('MR', 0.692, 0.588), to=('BR', 0.644, 1.3))`

## Joints
- s1(frac 1.0) ⇆ s2(frac 0.613) @ BC
- s2(frac 0.974) ⇆ s3(frac 0.627) @ BR

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_48/generated.py + attempts/cycle_48/01_山.png
