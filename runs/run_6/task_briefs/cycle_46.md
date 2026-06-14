# Cycle 46 — Focus: 八 (ba)

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
1. `draw_pie(t, from=('ML', 0.776, 0.668), to=('BL', -0.192, 1.056))`
2. `draw_na(t, from=('TC', 0.26, 0.768), to=('BR', 1.3, 0.96))`

## Joints
None.

## Eval
- OCR is_correct
- Panel 3/3 YES

## Output
attempts/cycle_46/generated.py + attempts/cycle_46/01_八.png
