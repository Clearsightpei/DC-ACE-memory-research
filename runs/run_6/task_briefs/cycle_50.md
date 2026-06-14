# Cycle 50 — Focus: 白 (bai)

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
1. `draw_pie(t, from=('TC', 0.248, 0.312), to=('ML', 0.748, 0.442))`
2. `draw_shu(t, from=('ML', 0.342, 0.466), to=('BL', 0.62, 1.196))`
3. `draw_heng_zhe(t, from=('ML', 0.342, 0.466), corner1=('MR', 0.156, 0.466), to=('BR', 0.156, 1.008))`
4. `draw_heng(t, from=('BL', 0.524, 0.161), to=('BC', 0.932, 0.128))`
5. `draw_heng(t, from=('BL', 0.616, 0.91), to=('BR', 0.156, 1.008))`

## Joints
- s1(frac 1.0) ⇆ s3(frac 0.097) @ ML
- s2(frac 0.071) ⇆ s3(frac 0.0) @ ML
- s2(frac 0.417) ⇆ s4(frac 0.0) @ BL
- s2(frac 0.822) ⇆ s5(frac 0.0) @ BL
- s3(frac 0.942) ⇆ s5(frac 1.0) @ BR

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_50/generated.py + attempts/cycle_50/01_白.png
