"""
p2_radical_007_乚 — Phase 2 radical, standalone render.

Structure (single stroke, 3 beats + hook flick):
  1. Short 竖 descending from upper-left area.
  2. Smooth tangent-continuous quarter-arc (belly on lower-left)
     turning the vertical into a rightward horizontal.
  3. Rightward 横 running along the bottom.
  4. Small upward-left hook flick at the right endpoint.

Coordinates are image-coords (y grows DOWN). 300x300 white canvas,
black ink, PIL brush-dab technique. Uses the KEY PRIMITIVE
tangent-continuous arc from drawer_memory.md.

GT observation: the vertical is SHORT (upper-left), the horizontal
is LONG (running most of the width), and the terminal hook is small
and points up-left. Scaled up from the Phase-1 乚 mastery entry to
fill the standalone canvas.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Beat 1: short 竖 (vertical) ----
# Standalone-scale: short top segment leaving room for the wide horizontal.
# Scaled up to fill the canvas better (per "move the knob further" rule).
v_x0, v_y0 = 85, 55            # top of vertical (higher)
v_x1, v_y1 = 85, 190           # bottom of vertical (arc entry point) — LONGER
r_v = 6.0

# start 顿 dab (small for standalone per memory — no balloon)
dab(v_x0, v_y0, r_v + 0.5)

steps_v = 220
for i in range(steps_v + 1):
    t = i / steps_v
    x = v_x0 + (v_x1 - v_x0) * t
    y = v_y0 + (v_y1 - v_y0) * t
    dab(x, y, r_v)

# ---- Beat 2: tangent-continuous arc (belly on lower-left) ----
# KEY PRIMITIVE symmetric variant? No — here we need downward -> RIGHTWARD.
# So use the standard variant:
#   x = x0 + R*(1 - cos(t*pi/2))
#   y = y0 + R*sin(t*pi/2)
# Arc entry (t=0) at end-of-竖 with tangent (0,+); arc exit (t=1)
# at (v_x1 + R, v_y1 + R) with tangent (+,0) — perfect for the 横.
R = 55
steps_arc = 200
for i in range(steps_arc + 1):
    t = i / steps_arc
    x = v_x1 + R * (1 - math.cos(t * math.pi / 2))
    y = v_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_v)

arc_end_x = v_x1 + R           # 137
arc_end_y = v_y1 + R           # 207

# ---- Beat 3: rightward 横 ----
# Long horizontal running to the right edge zone.
h_x1, h_y1 = 265, arc_end_y    # keep y level with arc endpoint — extend further right
r_h = 6.0

steps_h = 260
for i in range(steps_h + 1):
    t = i / steps_h
    x = arc_end_x + (h_x1 - arc_end_x) * t
    y = arc_end_y + (h_y1 - arc_end_y) * t
    dab(x, y, r_h)

# ---- Beat 4: hook flick, up-and-slightly-left ----
# Small taper flick from horizontal's right endpoint.
hook_len = 26
hook_angle_deg = -105          # up-and-slightly-left (image coords, 0 = +x, negative = up)
hx0, hy0 = h_x1, h_y1
hx1 = hx0 + hook_len * math.cos(math.radians(hook_angle_deg))
hy1 = hy0 + hook_len * math.sin(math.radians(hook_angle_deg))

# joining 顿 dab at hook base (small)
dab(hx0, hy0, r_h + 1.0)

steps_hook = 140
for i in range(steps_hook + 1):
    t = i / steps_hook
    x = hx0 + (hx1 - hx0) * t
    y = hy0 + (hy1 - hy0) * t
    r = r_h + 0.5 - (r_h + 0.5 - 1.1) * t   # taper thick -> thin
    dab(x, y, r)

img.save("01_乚.png")
