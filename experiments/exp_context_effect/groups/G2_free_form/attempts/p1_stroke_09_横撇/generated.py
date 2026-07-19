"""
p1_stroke_09_横撇 (heng-pie): a horizontal 横 that turns sharply and
throws down-left as a 撇 tail.

Strategy (using PIL brush-dabs per drawer_memory.md):
- Segment 1 (横): mostly-uniform horizontal bar, slight 顿笔 press at
  start, small terminal thickening at the joint.
- At the joint: a small 顿 (press) that transitions into the 撇.
- Segment 2 (撇): from the joint, sweeps down-and-left along a gentle
  arc (concave to lower-right), thick at joint, tapered to a sharp tip.

Image coord convention: y grows DOWN. 300x300 canvas, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=400):
    """Straight tapered stroke via stacked filled circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r_start, r_end, steps=400):
    """Quadratic Bezier tapered stroke via stacked filled circles."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Segment 1: 横 (horizontal), left -> right ---------------------
# 顿笔 initial press (slightly bigger dab)
heng_start = (55, 105)
heng_end = (235, 100)  # slight upward tilt is characteristic of 横
# Initial press dab
draw.ellipse(
    (heng_start[0] - 8, heng_start[1] - 8,
     heng_start[0] + 8, heng_start[1] + 8),
    fill="black",
)
# Body: roughly uniform, tapering very slightly to the joint
dab_line(heng_start, heng_end, r_start=6.5, r_end=6.5, steps=500)

# ---- Joint press (顿) at the turn ---------------------------------
# 横撇's defining feature: a distinct downward press at the corner
# before the pie throws down-left. Place a slightly larger dab here.
joint = (238, 108)
draw.ellipse(
    (joint[0] - 9, joint[1] - 9, joint[0] + 9, joint[1] + 9),
    fill="black",
)

# ---- Segment 2: 撇 (throw down-left) -------------------------------
# From the joint, curve down-and-left. Gentle arc, concave to the
# lower-right (control point pulled toward upper-left of the chord's
# midpoint so the belly bulges up-right just slightly).
pie_start = joint
pie_end = (85, 245)          # lower-left tip
# Chord midpoint ~ (161.5, 176.5). Pull control up-right to make the
# stroke bow gently outward (a natural 撇 curvature).
pie_ctrl = (200, 150)
dab_bezier(pie_start, pie_ctrl, pie_end, r_start=8.0, r_end=1.2, steps=500)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_09_横撇/01_横撇.png"
)
print("saved 01_横撇.png")
