# Cycle 42 — Focus: 目 (mù) — restart after c40 froze

## Why a new cycle (not c40 overwrite)
c40 hit the 3-attempt freeze:
- attempt 1: `find_corners` angle detection — corner placed at wrong position, internal horizontals scattered.
- attempt 2: geometric heuristic `(to_x, from_y)` — produced a clean rectangular 目 (user verified visually).
- attempt 3: switched to MMH-bend (max-x of median) — REGRESSION: max-x of 目's heng_zhe is at the bottom-right corner (point 6 of median = (74, -144)), not at the top-right L-bend (point 5 ≈ (70, 78)). Renders as a slanted triangle. Panel rejected 0/3.

Per Drawer SKILL's three-attempt freeze rule, c40's directory is preserved as evidence. This cycle (c42) restarts 目 with a corrected corner heuristic.

## Phase
2 — character composition.

## MMH stroke count
5

## Strokes
1. `draw_shu(t, ('TL', 0.576, 0.656), ('BL', 0.684, 1.244))` — left vertical.
2. `draw_heng_zhe(t, ('TL', 0.804, 0.704), ('TC', 0.872, 0.704), ('BC', 0.872, 1.020))` — top + right vertical. **Corner forced to geometric L-bend `(to_x, from_y)` — NOT MMH max-x.**
3. `draw_heng(t, ('ML', 0.844, 0.556), ('C', 0.764, 0.420))` — first internal horizontal.
4. `draw_heng(t, ('BL', 0.836, 0.180), ('BC', 0.776, 0.072))` — second internal horizontal.
5. `draw_heng(t, ('BL', 0.792, 1.064), ('BC', 0.956, 0.948))` — bottom horizontal.

## Joints (informational)
The 5 strokes form a sealed rectangle with 2 interior horizontals. Joints derived from `find_joints` are documented in `task_briefs/cycle_40_dataset.json` (unchanged from c40 since the underlying MMH skeleton is the same).

## Eval gates
- OCR is_correct.
- Panel 3/3 YES required for promotion.
- visual_score informational.

## Corner-heuristic-rule encoded for future char cycles
For compound strokes whose bend is at a **rectangular L-corner** (横折, 横折钩, 横折弯钩, 横钩, 竖折, 竖钩, 竖弯钩), use the **geometric heuristic**:
- `heng-then-down` family: corner = `(to_x, from_y)`
- `down-then-right` family: corner = `(from_x, to_y)`

For compound strokes whose bend is at the **MMH median's max-extent point** (横撇, 横撇弯钩 — where the bend is mid-stroke and not at a rectangular corner), use the MMH max-x bend point.

## Output
`attempts/cycle_42/generated.py` + `attempts/cycle_42/01_目.png`.
