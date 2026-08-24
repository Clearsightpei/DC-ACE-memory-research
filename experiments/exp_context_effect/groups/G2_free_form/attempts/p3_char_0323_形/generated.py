"""
形 = 开 (left) + 彡 (right).
Left 开: two horizontals + a 撇 (left leg) + a 竖 (right leg).
Right 彡: three parallel short 撇, stacked diagonally.

Consulted memory:
- form_catalog "撇 as parallel-repetition (彡...)": three copies at
  ~40 px offset, short (~60 px), moderate slope (~60°),
  aligned diagonally so tips stack roughly on a diagonal line.
- p2_radical_064_彡 PASS PNG: three tapered flicks, thin→thick then
  taper to point at tail; middle stroke sits between top and bottom.

Layout on 300x300 canvas:
- 开 fills the left ~55% (x=25..175).
- 彡 fills right ~35% (x=190..270).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def tapered_stroke(p0, p1, w_start, w_end, steps=40):
    """Draw a straight tapered stroke as a series of shrinking circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = w_start + (w_end - w_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def curved_pie(points, w_start, w_end, steps=60):
    """Bezier-ish curved tapered stroke through given points list (poly)."""
    # Sample along piecewise-linear points; for a smooth 撇 use quadratic bezier
    # with 3 control points.
    if len(points) == 3:
        p0, p1, p2 = points
        for i in range(steps + 1):
            t = i / steps
            x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
            y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
            r = w_start + (w_end - w_start) * t
            draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
    else:
        for i in range(len(points) - 1):
            tapered_stroke(points[i], points[i + 1], w_start, w_end, steps=steps // (len(points) - 1))


# ============ 开 (left half, ~55% width) ============
# Top horizontal (short, upper)
tapered_stroke((35, 95), (160, 90), 4.0, 4.5)

# Second horizontal (longer, middle) — crosses both legs
tapered_stroke((20, 155), (170, 150), 5.0, 5.5)

# 撇 (left leg) — curves down-left from top area to bottom-left
curved_pie([(70, 100), (55, 190), (30, 275)], 5.0, 2.0, steps=60)

# 竖 (right leg) — straight vertical from just below top horizontal to bottom
tapered_stroke((135, 100), (140, 275), 4.5, 4.5)

# ============ 彡 (right half) — three parallel 撇 ============
# Per form_catalog: consistent x-offset (~40 px apart), short (~60 px),
# moderate slope (~60°), tips stack on a diagonal line.
# GT shows substantially longer flicks than a compressed 彡 — the right
# half of 形 gets ~40% of the width and each 撇 spans ~80 px.
strokes_pie = [
    # (start, control, end)  — quadratic bezier tapered thin at tail
    ((255, 80), (245, 105), (225, 140)),
    ((240, 130), (225, 165), (200, 205)),
    ((225, 185), (205, 225), (175, 280)),
]
# Progressive: bottom stroke is longest and most curved (per 彡 tradition)
tapered_specs = [
    (5.0, 1.2),
    (5.5, 1.2),
    (6.0, 1.2),
]
for pts, (ws, we) in zip(strokes_pie, tapered_specs):
    curved_pie(list(pts), ws, we, steps=50)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0323_形/01_形.png")
print("saved 01_形.png")
