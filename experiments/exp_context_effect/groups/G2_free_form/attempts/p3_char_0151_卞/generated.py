"""
卞 — 4 strokes: top 点(丶) + 横(一) + 竖(丨) + right 点(丶)
Essentially 下 (top一 + 竖 + right点) with an added top 点 above the 横.

# SIGNATURE CHECK: 卞 = 下 (top 一 + central 竖 + right-side 点) PLUS one 点 sitting
#   above the 横, slightly left of the 竖. Total 4 strokes.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(draw, pts, width_start=10, width_end=10, steps=None):
    """Draw a tapered line by stamping ellipses along a polyline of points."""
    # densify
    if steps is None:
        steps = 60
    from math import hypot
    # compute cumulative distances
    dists = [0.0]
    for i in range(1, len(pts)):
        dists.append(dists[-1] + hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]))
    total = dists[-1]
    if total == 0:
        return
    for s in range(steps + 1):
        t = s / steps
        target = t * total
        # find segment
        for i in range(1, len(pts)):
            if dists[i] >= target:
                seg_t = (target - dists[i-1]) / (dists[i] - dists[i-1] + 1e-9)
                x = pts[i-1][0] + seg_t * (pts[i][0] - pts[i-1][0])
                y = pts[i-1][1] + seg_t * (pts[i][1] - pts[i-1][1])
                break
        w = width_start + (width_end - width_start) * t
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Stroke 1: top 点 — small dot above the 横, slightly left of center
# a short diagonal dab from upper-left to lower-right
brush_line(d, [(128, 62), (148, 92)], width_start=6, width_end=11)

# Stroke 2: 横 — long horizontal, slight upward tilt then settling flat
# from around x=40 to x=260, y around 120
brush_line(d, [(42, 128), (150, 120), (262, 124)], width_start=8, width_end=9)

# Stroke 3: 竖 — vertical down through center, from just under the 横 to near bottom
brush_line(d, [(150, 125), (150, 260)], width_start=10, width_end=8)

# Stroke 4: right 点 — small dot to the right of the 竖, slightly below the 横
# diagonal dab from upper-left to lower-right
brush_line(d, [(178, 158), (208, 195)], width_start=6, width_end=12)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0151_卞/01_卞.png")
