"""Render 阝 (left-ear radical) as a 300x300 PNG.

阝 has two strokes:
  1. 横撇弯钩 (héng piě wān gōu) — the "ear" shape on the upper-left,
     a smooth "3"-like curve with two rounded bumps.
  2. 竖 (shù) — a straight vertical stroke going down from the ear.

Rendered with quadratic Bezier segments for smoothness.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 6  # ink thickness


def quad_bezier(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_path(points, width=TH):
    draw.line(points, fill=INK, width=width, joint="curve")
    r = width / 2
    for x, y in (points[0], points[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---- Stroke 1: 横撇弯钩 (the "ear") — two rounded bumps ----
# Start upper-left, arc right-up-right (upper bump), curve back to a waist,
# arc out again (lower bump), then hook back-left at the bottom.

# Upper bump: from A -> waist B via control C (up-right of the bump)
A = (118, 92)
C1 = (170, 78)   # control: top-right, pulls the arc up and out
B = (128, 138)   # waist point (where two bumps meet)

upper = quad_bezier(A, C1, B, steps=50)

# Lower bump: from B -> D via control C2 (down-right, bigger bump)
C2 = (185, 158)  # control: further right for a fuller lower bump
D = (128, 188)   # bottom of the ear (just before hook)

lower = quad_bezier(B, C2, D, steps=50)

# Small hook tail: from D angling slightly back-left
hook_end = (112, 182)
hook = [D, (120, 187), hook_end]

ear = upper + lower + hook
draw_path(ear, width=TH)


# ---- Stroke 2: 竖 (vertical) ----
# Runs from just under the ear's attachment straight down.
vert = [(118, 100), (118, 268)]
draw_path(vert, width=TH)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_020_阝/01_阝.png"
)
