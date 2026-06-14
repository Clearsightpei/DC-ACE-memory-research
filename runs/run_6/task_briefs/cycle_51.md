# Cycle 51 — Focus: 自 (zi)

## Phase
2 — character composition.

## MMH stroke count
6

## Joint-snap fix applied
Anchor heads (frac<0.15) and tails (frac>0.85) overridden with joint `meeting_canvas` coords from `find_joints`. Mid-stroke joints (frac 0.15-0.85) need no snap (the brush passes through naturally).

## Corner heuristic by primitive type
- heng_zhe / heng_zhe_gou / heng_gou / heng_zhe_wan_gou: geometric `(to_x, from_y)`
- shu_zhe / shu_gou / shu_wan_gou: geometric `(from_x, to_y)`
- heng_pie / heng_pie_wan_gou: MMH median max-x point

## Strokes
1. `draw_pie(t, from=('TC', 0.308, 0.224), to=('C', 0.144, 0.062))`
2. `draw_shu(t, from=('ML', 0.852, 0.136), to=('BL', 0.816, 1.214))`
3. `draw_heng_zhe(t, from=('ML', 0.852, 0.136), corner1=('C', 0.898, 0.136), to=('BC', 0.898, 1.07))`
4. `draw_heng(t, from=('ML', 0.859, 0.91), to=('C', 0.796, 0.704))`
5. `draw_heng(t, from=('BL', 0.852, 0.46), to=('BC', 0.812, 0.332))`
6. `draw_heng(t, from=('BL', 0.816, 1.214), to=('BR', 0.048, 1.048))`

## Joints
- s1(frac 1.0) ⇆ s2(frac 0.082) @ ML
- s1(frac 0.934) ⇆ s3(frac 0.067) @ C
- s2(frac 0.082) ⇆ s3(frac 0.0) @ ML
- s2(frac 0.432) ⇆ s4(frac 0.0) @ ML
- s2(frac 0.652) ⇆ s5(frac 0.0) @ BL
- s2(frac 1.0) ⇆ s6(frac 0.0) @ BL
- s3(frac 1.0) ⇆ s6(frac 0.822) @ BC

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_51/generated.py + attempts/cycle_51/01_自.png
