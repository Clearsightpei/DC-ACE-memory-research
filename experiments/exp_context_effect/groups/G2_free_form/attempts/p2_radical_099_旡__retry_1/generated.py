"""
p2_radical_099_旡 — G2 retry #1.

Prior-attempt diagnosis vs GT:
  - 撇 was TOO dominant: it swept from very top-right (y=62) all the
    way to bottom-left (y=260), crossing the entire glyph and burying
    the middle 横折. In GT, the 撇 is the LEFT LEG of the 儿-base —
    it starts INSIDE the middle-band (around y=140) and only descends
    to lower-left. It doesn't originate above the top 横.
  - Middle 横折 was too small and got visually swallowed.
  - Top 横 was too short and off-center.
  - Overall stack too cramped in the top half.

Fix (this retry): treat 旡 as a THREE-LAYER stack, like 无:
   Layer 1 (top): short 横 (upper 一)
   Layer 2 (middle): 横折 forming a small tucked corner — a short 横
       to the right, then shoulder, then short 竖-drop
   Layer 3 (bottom): 儿-legs — 撇 (left leg) starting from the middle
       and sweeping down-left, PLUS 竖弯钩 (right leg) starting from
       middle-right, dropping, arcing rightward at baseline, hook up-left.

Total: 4 strokes.  Compact-square silhouette (radical_position_rules).

Canvas 300×300, white bg, black ink. PIL brush-dab. y grows DOWN.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(60, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, easing=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** easing
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: TOP 横 — short, up-tilted, upper-center.
# ---------------------------------------------------------------
h1_x0, h1_y0 = 105, 92
h1_x1, h1_y1 = 200, 86
r_h = 4.5
dab(h1_x0, h1_y0, r_h + 0.8)
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, r_h, r_h)
dab(h1_x1, h1_y1, r_h + 0.8)

# ---------------------------------------------------------------
# Stroke 2: MIDDLE 横折 — short 横 + shoulder + short 竖-drop.
# Forms a small tucked-corner just below the top 横.
# ---------------------------------------------------------------
hz_x0, hz_y0 = 90, 138       # start of short 横 (a bit left of top 横)
hz_x1, hz_y1 = 180, 132      # end of 横 / start of 竖 (up-tilt)
hz_x2, hz_y2 = 176, 170      # end of 竖-drop
r_hz = 4.5
dab(hz_x0, hz_y0, r_hz + 0.8)
line_dabs(hz_x0, hz_y0, hz_x1, hz_y1, r_hz, r_hz + 0.3)
dab(hz_x1, hz_y1, r_hz + 2.0)  # shoulder 顿
line_dabs(hz_x1, hz_y1, hz_x2, hz_y2, r_hz + 0.3, r_hz)
dab(hz_x2, hz_y2, r_hz + 0.5)

# ---------------------------------------------------------------
# Stroke 3: LEFT LEG 撇 — starts INSIDE middle band (not above the
#   top 横) and sweeps down-and-LEFT.  Only descends to lower-left,
#   not all the way to the bottom corner.
# ---------------------------------------------------------------
p_p0 = (118, 148)   # starts inside middle band (below top 横)
p_p2 = (55, 255)    # bottom-left, but tail lifted a bit
p_p1 = (95, 210)    # ctrl for gentle bow (belly slightly left)
dab(p_p0[0], p_p0[1], 7.5)     # small 顿笔 at start
bezier_dabs(p_p0, p_p1, p_p2, r_start=6.5, r_end=1.4, steps=260, easing=1.15)

# ---------------------------------------------------------------
# Stroke 4: RIGHT LEG 竖弯钩 — vertical descends from middle-right,
#   arcs smoothly rightward along the baseline, terminal hook flicks
#   up-and-slightly-left.
# ---------------------------------------------------------------
v_x0, v_y0 = 176, 170         # start of vertical (continues from horzhe end area)
v_x1, v_y1 = 148, 240         # bottom-of-vertical / start-of-arc
bezier_dabs(
    (v_x0, v_y0),
    (166, 210),               # ctrl pulls slightly inward — mild bow
    (v_x1, v_y1),
    r_start=6.0, r_end=5.5, steps=220, easing=1.0,
)

# Tangent-continuous arc: descending-vertical → rightward-horizontal.
R = 30
arc_steps = 100
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = v_x1 + R * (1 - math.cos(t * math.pi / 2))
    y = v_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.5)

arc_end_x = v_x1 + R
arc_end_y = v_y1 + R

# Rightward 横 baseline segment — extend farther right to match GT.
h2_x1 = arc_end_x + 75
h2_y1 = arc_end_y
line_dabs(arc_end_x, arc_end_y, h2_x1, h2_y1, 5.5, 5.5)

# Terminal hook flick: up-and-slightly-left.
hook_len = 38
hook_angle = math.radians(-118)
hook_x1 = h2_x1 + hook_len * math.cos(hook_angle)
hook_y1 = h2_y1 + hook_len * math.sin(hook_angle)
dab(h2_x1, h2_y1, 5.5)
hook_steps = 110
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = h2_x1 + (hook_x1 - h2_x1) * t
    y = h2_y1 + (hook_y1 - h2_y1) * t
    r = 5.5 + (1.2 - 5.5) * t
    dab(x, y, r)


out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_旡.png")
img.save(out_path)
print(f"Saved: {out_path}")
