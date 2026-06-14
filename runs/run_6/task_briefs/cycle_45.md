# Cycle 45 — Focus: 七 (qi)

## Phase
2 — character composition.

## MMH stroke count
2

## Joint-snap fix applied
Anchor heads (frac<0.15) and tails (frac>0.85) overridden with joint `meeting_canvas` coords from `find_joints`. Mid-stroke joints (frac 0.15-0.85) need no snap (the brush passes through naturally).

## Corner heuristic by primitive type
- heng_zhe / heng_zhe_gou / heng_gou / heng_zhe_wan_gou: geometric `(to_x, from_y)`
- shu_zhe / shu_gou / shu_wan_gou: geometric `(from_x, to_y)`
- heng_pie / heng_pie_wan_gou: MMH median max-x point

## Strokes
1. `draw_heng(t, from=('BL', -0.144, 0.188), to=('MR', 0.98, 0.704))`
2. `draw_shu_wan_gou(t, from=('TL', 0.908, 0.548), corner1=('BL', 0.908, 1.1), to=('BR', 0.588, 1.1))`

## Joints
- s1(frac 0.398) ⇆ s2(frac 0.38) @ C

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_45/generated.py + attempts/cycle_45/01_七.png
