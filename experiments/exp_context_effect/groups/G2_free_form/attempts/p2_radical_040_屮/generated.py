"""屮 (chè) — 3-stroke radical.

Structure (matching GT):
  Stroke 1: 竖 (long central vertical), top → bottom
  Stroke 2: 竖折 on the LEFT — short vertical drops, shoulder, horizontal
            runs rightward under the central 竖 (base of the radical).
  Stroke 3: 竖 on the RIGHT — short vertical, top → bottom, sits on
            the right end of stroke 2's base.

Standalone radical → scale up curvature discipline (memory: standalone
vs compound scale-up).  Small 顿 at endpoints (r+1 only, not r+2 balls).
PIL brush-dabs technique.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def seg(x0, y0, x1, y1, r0, r1, steps=400):
    """Straight tapered segment via brush-dabs."""
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -------- Stroke 1: central 竖 (long vertical) --------
# Top ~(150, 55), bottom ~(150, 270).  Uniform ink.
cx = 150
top_y = 55
bot_y = 270
r_main = 5.5
dab(cx, top_y, r_main + 1.5)  # small 顿 at top
seg(cx, top_y, cx, bot_y, r_main, r_main, steps=420)
dab(cx, bot_y, r_main + 1.0)  # small terminal press

# -------- Stroke 2: 竖折 on the LEFT (base of the radical) --------
# Short vertical drops on the left, shoulder, horizontal runs right
# ACROSS UNDER the central 竖 all the way to the right branch's foot.
# The base spans the full width — this ties the radical together.
left_top = (85, 100)
left_corner = (85, 175)
base_right = (218, 175)  # extends to under the right vertical
r_h = 5.0
dab(left_top[0], left_top[1], r_h + 1.0)  # small 顿 at start
seg(left_top[0], left_top[1], left_corner[0], left_corner[1], r_h, r_h + 0.5, steps=260)
# shoulder dab at the corner
dab(left_corner[0], left_corner[1], r_h + 2.0)
seg(left_corner[0], left_corner[1], base_right[0], base_right[1], r_h + 0.5, r_h, steps=340)
dab(base_right[0], base_right[1], r_h + 1.0)  # small blunt end

# -------- Stroke 3: right short 竖 --------
# From (~218, 100) down to (~218, 175), sits on the right end of base.
right_top = (218, 100)
right_bot = (218, 175)
dab(right_top[0], right_top[1], r_h + 1.0)  # 顿 at top
seg(right_top[0], right_top[1], right_bot[0], right_bot[1], r_h, r_h, steps=260)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_040_屮/01_屮.png")
