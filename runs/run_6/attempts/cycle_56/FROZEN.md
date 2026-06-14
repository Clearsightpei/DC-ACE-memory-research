# c56 山 — FROZEN

3-attempt freeze rule reached. Preserved as evidence.

## Attempt history
1. **Initial (raw MMH)**: right shu's 垂露 droplet protruded ~30 px below baseline; panel 0/3 ("right vertical extends below the bottom horizontal").
2. **shu_lift +22**: insufficient — droplet still ~25 px below baseline; panel 0/3.
3. **shu.to.y = baseline_y (current)**: uprights now sit on baseline but middle vertical is grossly off-center to the right, and panel reads structure as 业/disconnected rather than 山.

## Root cause
The "lift shu.to to baseline" override only addresses vertical termination, not the horizontal placement of the three uprights. MMH's 山 places the center long shu at a slightly off-center x, and the left/right uprights at non-symmetric offsets that don't read as a balanced 山 silhouette under the calligraphy-aware panel.

## Restart plan
A future cycle (c65 or later) should:
1. Manually center the long shu (s1 left, s3 right) symmetric around s2 (the 竖折)'s midpoint.
2. Use raw MMH only for stroke ENDPOINTS in y; override x to enforce symmetry.
3. Consider component-based "三-upright on shared base" template — apex_share x-coords for the 3 verticals.
