# c64 头 — FROZEN

3-attempt freeze rule reached.

## Attempt history
1. **Initial decomp `pie+dian+heng+shu+heng`**: wrong primitive types.
2. **Correct decomp `dian+dian+heng+pie+dian`**: 2 top dians sat on the pie's body (panel said "ticks on the pie" — read as 失/矢).
3. **`dian+dian+heng+pie+dian` with head_share lift** (s1+s2 dians lifted above pie's apex y): s2 dian's tail.y ended up off the BC cell (y_frac > 1.3, clamped). s2 visually disappeared; panel saw only ONE top dot → 0/3.

## Root cause
MMH 头's s1 and s2 dians sit at y=75 and y=17 — both ABOVE the heng (y=-60) but also intersecting with the pie's polyline (pie passes through (24, 85), (24, 77), (8, -40)…). When the dians are at MMH's raw positions, they visually OVERLAP with the pie's upper body. Lifting them higher pushes one off-canvas.

The right fix is to KEEP dians at MMH y but MOVE them HORIZONTALLY away from the pie's path (left and right of the pie body, not on it).

## Restart plan
Future cycle should:
1. Shift s1 dian's x left by ~30 px so its tail x < pie's x at that y.
2. Shift s2 dian's x left or down by similar amount.
3. OR redesign head_share: dians symmetrically positioned at heng_y + small offset, x at (-50, +50).
