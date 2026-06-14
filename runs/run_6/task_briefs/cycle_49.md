# Cycle 49 — Focus: 五 (wu)

## Phase
2 — character composition.

## MMH stroke count
4

## Joint-snap fix applied
Anchor heads (frac<0.15) and tails (frac>0.85) overridden with joint `meeting_canvas` coords from `find_joints`. Mid-stroke joints (frac 0.15-0.85) need no snap (the brush passes through naturally).

## Corner heuristic by primitive type
- heng_zhe / heng_zhe_gou / heng_gou / heng_zhe_wan_gou: geometric `(to_x, from_y)`
- shu_zhe / shu_gou / shu_wan_gou: geometric `(from_x, to_y)`
- heng_pie / heng_pie_wan_gou: MMH median max-x point

## Strokes
1. `draw_heng(t, from=('TL', 0.668, 0.772), to=('TR', 0.464, 0.616))`
2. `draw_shu(t, from=('TC', 0.237, 0.839), to=('BL', 0.893, 0.929))`
3. `draw_heng_zhe(t, from=('ML', 0.544, 0.808), corner1=('C', 0.762, 0.808), to=('BC', 0.762, 0.877))`
4. `draw_heng(t, from=('BL', -0.296, 1.076), to=('BR', 1.3, 1.108))`

## Joints
- s1(frac 0.287) ⇆ s2(frac 0.0) @ TC
- s2(frac 0.435) ⇆ s3(frac 0.253) @ C
- s2(frac 0.973) ⇆ s4(frac 0.314) @ BL
- s3(frac 1.0) ⇆ s4(frac 0.552) @ BC

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_49/generated.py + attempts/cycle_49/01_五.png
