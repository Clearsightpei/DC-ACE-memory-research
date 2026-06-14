# c40 目 — FROZEN

This cycle hit the 3-attempt freeze rule (Drawer SKILL.md). Preserved as evidence; never overwritten.

## Attempt history (this directory holds attempt 3 only)
- **Attempt 1**: `find_corners` angle detection → corner placed at wrong position, internal horizontals scattered. (Not committed; overwritten by attempt 2.)
- **Attempt 2**: geometric heuristic `(to_x, from_y)` → produced a clean rectangular 目 (visually verified, user confirmed). (Not committed; overwritten by attempt 3.)
- **Attempt 3** (the file in this dir): switched to MMH-bend (max-x of heng_zhe median) → REGRESSION. max-x of 目's heng_zhe is at point 6 of the median = (74, -144), the bottom-right of the right vertical, NOT at the top-right L-bend. Renders as a slanted triangle. Panel 0/3.

## What attempt 2 did right
`heng_zhe` corner was `(TC, 0.872, 0.704)` = `(to_x, from_y)` = the rectangular L-corner.

## What attempt 3 did wrong
`heng_zhe` corner was `(BR, 0.24, 0.94)` = MMH median's max-x point = the bottom-right of the right vertical. brushed_bezier then drew the heng segment as a long diagonal from the upper-left to bottom-right, instead of horizontally to the top-right.

## Lesson
MMH-bend heuristic is correct for compound strokes with mid-stroke bends (横撇 family). It's wrong for L-shape strokes where the bend is at a rectangular corner — use geometric `(to_x, from_y)` (or `(from_x, to_y)` for down-then-right) there.

## Restart
Re-attempted in c42 with the geometric heuristic. c42 panel 3/3 YES, promoted.
