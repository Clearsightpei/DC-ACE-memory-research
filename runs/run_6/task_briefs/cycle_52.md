# Cycle 52 — Focus: 半 (ban)

## Phase
2 — character composition.

## MMH stroke count
5

## Joint-snap fix applied
Anchor heads (frac<0.15) and tails (frac>0.85) overridden with joint `meeting_canvas` coords from `find_joints`. Mid-stroke joints (frac 0.15-0.85) need no snap (the brush passes through naturally).

## Corner heuristic by primitive type
- heng_zhe / heng_zhe_gou / heng_gou / heng_zhe_wan_gou: geometric `(to_x, from_y)`
- shu_zhe / shu_gou / shu_wan_gou: geometric `(from_x, to_y)`
- heng_pie / heng_pie_wan_gou: MMH median max-x point

## Strokes
1. `draw_dian(t, from=('TL', 0.604, 0.716), to=('C', 0.012, 0.108))`
2. `draw_pie(t, from=('TR', 0.308, 0.368), to=('TC', 0.908, 0.956))`
3. `draw_heng(t, from=('ML', 0.712, 0.528), to=('MR', 0.256, 0.38))`
4. `draw_heng(t, from=('BL', -0.144, 0.26), to=('BR', 1.192, 0.116))`
5. `draw_shu(t, from=('TC', 0.264, 0.228), to=('BC', 0.48, 1.3))`

## Joints
- s3(frac 0.511) ⇆ s5(frac 0.378) @ C
- s4(frac 0.491) ⇆ s5(frac 0.553) @ BC

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_52/generated.py + attempts/cycle_52/01_半.png
