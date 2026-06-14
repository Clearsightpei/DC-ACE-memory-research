# c63 出 — FROZEN

3-attempt freeze rule reached.

## Attempt history
1. **Initial decomp `shu+shu_zhe+shu+shu_zhe+shu`**: didn't match MMH polyline shapes; rendered as scrambled grid.
2. **Decomp `heng+shu+shu+heng+shu`** (visual heuristic from polyline ranges): rendered as broken H-shape, panel 0/3.
3. **Correct decomp `shu_zhe+shu+shu+shu_zhe+shu`** (after inspecting polyline waypoints): the shu_zhe primitive draws DOWN-then-RIGHT correctly, but MMH 出's s1 starts UPPER-LEFT, dips down to y_min, then sweeps RIGHT — this is NOT a clean down-then-right shu_zhe; it's more like a U-shape. shu_zhe primitive welds the bend as a sharp L, distorting the visual. Panel 0/3.

## Root cause
MMH 出's stroke 1 and stroke 4 are NOT canonical shu_zhe shapes — they start upper-left, dip down a bit, then sweep right with a curved bottom. The mastered `shu_zhe` primitive draws a clean L-corner. The two don't align visually.

## Restart plan
Future cycle should either:
1. Trace each stroke as a brushed_bezier with custom control points (bypass the shu_zhe primitive entirely).
2. Define a new primitive `u_curve` for MMH-style U-shape strokes.
3. Reconsider whether MMH's 出 decomposition is the right pedagogical target — handwritten 出 may use shu+shu_zhe+shu+shu_zhe+shu while print MMH uses U-shape strokes.
