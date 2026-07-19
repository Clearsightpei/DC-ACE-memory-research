"""Render 亅 (radical) to 300x300 PNG using PIL brush-dab technique.

GT observation:
- Vertical stroke positioned RIGHT of center (not centered).
- Small entry curve at top (subtle downturn from the left).
- Vertical descends straight.
- Terminal is a leftward-flick HOOK at the bottom (nearly horizontal
  going LEFT), not an up-left flick. This is the calligraphic form
  of 竖钩 as a radical.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Entry curve at top (small hook entering the vertical) ----
# Short arc from upper-left curving down into the vertical.
# Anchor: vertical is at x=180. Entry starts a little left/up.
entry_pts = []
cx_e, cy_e = 180, 82
R_e = 12
# quarter arc from angle 180° to 90° (left-of-center curving down to top)
steps_e = 60
for i in range(steps_e + 1):
    t = i / steps_e
    ang = math.radians(180 - 90 * t)  # 180 -> 90
    x = cx_e + R_e * math.cos(ang)
    y = cy_e + R_e * math.sin(ang) * (-1) + R_e  # small downward arc
    # Actually simpler: hand-place a shallow arc.
    pass

# Simpler entry: a short slanted stub from (162, 70) curving to top of 竖 (180, 82).
# Using bezier sample.
def bezier(p0, p1, p2, r0, r1, steps=120):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# Entry: short down-right curve into top of vertical
bezier((160, 72), (168, 72), (180, 82), 3.5, 6.0, steps=100)

# ---- Main vertical (竖) ----
# From top of vertical (180, 82) down to (180, 235). Uniform r=6.
line_taper((180, 82), (180, 235), 6.0, 6.0, steps=400)

# 顿 dab at top of vertical (subtle, since entry curve already provides press)
dab(180, 82, 6.5)

# ---- Bottom hook: leftward flick (nearly horizontal) ----
# From (180, 235) going LEFT to about (140, 240), tapering to sharp tip.
# Slight downward curve at start to keep continuity.
# Use bezier for smoother curl.
bezier((180, 235), (172, 246), (138, 240), 6.5, 1.2, steps=140)

# Small joining dab at hook root to hide seam
dab(180, 235, 7.0)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_002_亅/01_亅.png"
)
print("saved")
