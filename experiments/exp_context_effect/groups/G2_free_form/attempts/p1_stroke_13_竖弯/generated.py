"""
p1_stroke_13_竖弯 — 竖弯 (shu wan): a vertical stroke that curves smoothly
into a rightward horizontal at the bottom. Distinct from 竖折 (which has a
sharp shouldered corner) and from 竖钩 (which flicks up-left at the end).

Approach (per drawer_memory.md general technique):
  - PIL brush-dabs along a piecewise path: straight vertical top,
    quarter-arc transition, straight horizontal tail.
  - Roughly uniform width; slight 顿 press at the start (top) and a small
    press at the tail end. Corner is a SMOOTH arc, not a shoulder.
"""

from PIL import Image, ImageDraw
import math
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Geometry in image coords (y grows DOWN)
# Vertical part: from (x_top, y_top) straight down to (x_v_end, y_v_end)
# Then a quarter arc curving right, radius R, center at (x_v_end + R, y_v_end)
# Then horizontal tail from arc end going right.
x_top = 110
y_top = 55
R = 40                     # radius of the curve
x_v_end = x_top            # bottom of vertical segment (before arc starts)
y_v_end = 210              # start curving here
# arc center is to the RIGHT of vertical end by R, at same y
cx = x_v_end + R
cy = y_v_end
# arc runs from angle 180deg (left of center) to 90deg (below center)
# in PIL/math convention with y-down: point at angle a is
#   (cx + R*cos(a), cy + R*sin(a)) -- but we want it to sweep from
# (x_v_end, y_v_end) which is (cx - R, cy) DOWN to (cx, cy + R).
# In screen coords, going from angle pi (west) sweeping clockwise
# (through angle pi/2 -> pi (south)) using param t in [0,1]:
#   theta(t) = pi + (pi/2)*t   -> at t=0: theta=pi (west), at t=1: theta=3pi/2 (south)
#   x = cx + R*cos(theta), y = cy + R*sin(theta)  (screen y grows down,
#   so sin(3pi/2) = -1 gives y = cy - R, which is UP -- wrong).
# Easier: parameterize directly.
#   t in [0,1]: x = cx - R*cos(t*pi/2), y = cy + R*sin(t*pi/2)
# t=0 -> (cx-R, cy) = (x_v_end, y_v_end)  good
# t=1 -> (cx, cy+R) = (cx, cy+R)          curve bottom
# Then horizontal tail from (cx, cy+R) going RIGHT.

# Wait - want the horizontal tail to run to the RIGHT at the SAME y as
# the bottom of the arc. So arc must end tangent to horizontal, i.e. tangent
# vector at t=1 must point in +x direction. dx/dt = R*sin(t*pi/2)*(pi/2),
# dy/dt = R*cos(t*pi/2)*(pi/2). At t=1: dx/dt = R*pi/2, dy/dt=0. Good.
# At t=0: dx/dt=0, dy/dt=R*pi/2 -> tangent points DOWN. Good (matches vertical).

# Tail horizontal end
x_tail_end = 235
y_tail_end = cy + R  # = 210 + 40 = 250

# Stroke width
r_body = 7.0         # main uniform radius
r_start_press = 8.5  # 顿笔 at very top
r_tail_press = 8.5   # small press at end

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- Initial press (顿笔) at top ---
dab(x_top, y_top, r_start_press)

# --- Vertical segment: from (x_top, y_top) to (x_v_end, y_v_end) ---
n_v = 260
for i in range(n_v + 1):
    t = i / n_v
    x = x_top + (x_v_end - x_top) * t
    y = y_top + (y_v_end - y_top) * t
    # Slight bulge at very top blends into r_body quickly
    if t < 0.05:
        r = r_start_press + (r_body - r_start_press) * (t / 0.05)
    else:
        r = r_body
    dab(x, y, r)

# --- Arc segment ---
n_a = 120
for i in range(n_a + 1):
    t = i / n_a
    theta = t * (math.pi / 2)
    x = cx - R * math.cos(theta)
    y = cy + R * math.sin(theta)
    dab(x, y, r_body)

# --- Horizontal tail: from (cx, cy+R) to (x_tail_end, y_tail_end) ---
x_h_start = cx
y_h_start = cy + R
n_h = 220
for i in range(n_h + 1):
    t = i / n_h
    x = x_h_start + (x_tail_end - x_h_start) * t
    y = y_h_start + (y_tail_end - y_h_start) * t
    # Small press at very end
    if t > 0.94:
        s = (t - 0.94) / 0.06
        r = r_body + (r_tail_press - r_body) * s
    else:
        r = r_body
    dab(x, y, r)

# Final tail press dab for a clean rounded end
dab(x_tail_end, y_tail_end, r_tail_press)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_竖弯.png"))
print("Saved 01_竖弯.png")
