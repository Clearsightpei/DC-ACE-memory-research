# Cycle 44 — Focus: 力 (li)

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
1. `draw_heng_zhe_gou(t, from=('ML', 0.364, 0.464), corner1=('C', 0.444, 0.464), to=('BC', 0.444, 0.996))`
2. `draw_pie(t, from=('TC', 0.364, 0.368), to=('BL', -0.04, 1.3))`

## Joints
- s1(frac 0.228) ⇆ s2(frac 0.303) @ C

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_44/generated.py + attempts/cycle_44/01_力.png
