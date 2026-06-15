# FROZEN — cycle 67 个 (3-attempt rule)

Attempts c44(or c45), c58, c67. All 0/3 or 1/3 with same root cause.

## Root cause
The shu's dunbi (起笔) head blob renders BELOW the centerline endpoint. Even with apex_lift of 20 px (c67), the blob still sits below the apex meeting point because:
1. The shu primitive's dunbi blob extends ~25 px below the centerline start.
2. apex_lift of 20 px doesn't fully compensate.
3. Lifting more (e.g. 40 px) would put the centerline outside the canvas top-bound.

## Renderer ceiling
This is a shu primitive issue — the dunbi blob's downward extent is too large for compact characters like 个 where shu meets at a high apex. Affects: 个 (and likely 不, 一 in compound chars where shu touches a heng from below).

Logged to to_be_learned.md.
