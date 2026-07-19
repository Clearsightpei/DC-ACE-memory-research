"""
㔾 (radical, 2 strokes)
Structure:
  Stroke 1: 横折 — short 横 at upper-left tilting slightly up, then 折 shoulder
            down into a short vertical with a small hooked tick going down-left
            (the little inward "tongue" visible in the GT).
  Stroke 2: 竖弯钩 — vertical descends from top-left area of the radical,
            arcs smoothly right along the bottom, ends with a small blunt
            press at right (in 㔾 the 钩 is very subtle/absent — GT shows
            an open right side ending in a small upward tick).

Rendered PIL brush-dab technique at 300x300, black on white.
Standalone-scale: primary radii moderate, subtle press-dabs (no fat balls).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(30, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ------------------- Stroke 1: 横折 with a small inward tick -------------------
# Short 横 at upper area, tilting slightly up. Positioned so its right endpoint
# aligns roughly above the RIGHT side of the bowl (about x=200).
h1_start = (110, 100)
h1_end = (205, 92)
r_body = 5.5

# 顿 at start (small — standalone rules)
dab(h1_start[0], h1_start[1], r_body + 1.5)
line_dabs(h1_start[0], h1_start[1], h1_end[0], h1_end[1], r_body, r_body)

# shoulder dab at 折 corner
sh1 = (h1_end[0], h1_end[1])
dab(sh1[0], sh1[1], r_body + 2)

# short 竖 dropping from corner
v1_end = (200, 145)
line_dabs(sh1[0], sh1[1], v1_end[0], v1_end[1], r_body, r_body)

# small inward tick — a tiny 撇-like flick from the base of the short 竖 going
# down-and-left into the interior of the radical
tick_end = (160, 170)
# joining dab where the tick starts, to hide seam
dab(v1_end[0], v1_end[1], r_body + 0.5)
line_dabs(v1_end[0], v1_end[1], tick_end[0], tick_end[1], r_body, 1.5)


# ------------------- Stroke 2: 竖弯钩 forming the outer bowl -------------------
# Big bowl — vertical descends from upper-left, arcs into rightward bottom,
# ends near right side. Sized to fill the canvas.
v2_start = (75, 80)
v2_bottom = (75, 225)

# 顿 at start (small)
dab(v2_start[0], v2_start[1], r_body + 1.5)
line_dabs(v2_start[0], v2_start[1], v2_bottom[0], v2_bottom[1], r_body, r_body)

# tangent-continuous quarter-arc from vertical into rightward horizontal
R = 55
x0, y0 = v2_bottom
arc_steps = 140
last_arc_x, last_arc_y = x0, y0
for i in range(arc_steps + 1):
    t = i / arc_steps
    ax = x0 + R * (1 - math.cos(t * math.pi / 2))
    ay = y0 + R * math.sin(t * math.pi / 2)
    dab(ax, ay, r_body)
    last_arc_x, last_arc_y = ax, ay

# rightward 横 continuing from arc endpoint
h2_end = (235, last_arc_y)
line_dabs(last_arc_x, last_arc_y, h2_end[0], h2_end[1], r_body, r_body)

# small terminal hook flick — 㔾's tail flicks up-and-slightly-left,
# short and subtle (standalone: r+0.5 joining dab, no big ball)
hook_end_x = h2_end[0] - 6
hook_end_y = h2_end[1] - 32
dab(h2_end[0], h2_end[1], r_body + 0.5)
line_dabs(h2_end[0], h2_end[1], hook_end_x, hook_end_y, r_body, 1.5)


# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_038_㔾/01_㔾.png"
img.save(out_path)
print(f"Wrote {out_path}")
