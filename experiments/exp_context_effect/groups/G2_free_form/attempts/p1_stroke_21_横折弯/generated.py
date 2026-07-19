"""
横折弯 (heng-zhe-wan) — 300x300 white canvas, black ink.

Structure (per drawer_memory.md):
  1. 横 (horizontal), slight upward tilt (~3-5 deg), uniform width.
  2. 折 shoulder — one slightly-larger dab at the corner.
  3. 竖 dropping straight down (shorter than in plain 横折 because a
     smooth 弯 arc follows).
  4. 弯 smooth quarter-arc from vertical into rightward horizontal
     (tangent-continuous, NO shoulder dab — this is 弯, not 折).
  5. Short 横 running rightward, ending with a small terminal press
     (blunt round end — NO upward hook flick; that would make it
     横折弯钩).

Technique: PIL brush-dab (many small filled circles along each
segment), r ~ 5 px, 顿-dabs r+2 at strokes endpoints and at the 折
shoulder joint. Bezier not needed — arc is parameterized directly.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

R = 5          # baseline stroke radius
DUN = R + 2    # 顿笔 / shoulder dab radius


def dab(x, y, r=R):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0=R, r1=R, n=None):
    if n is None:
        d = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(d * 3))
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def arc_dabs(cx, cy, radius, a0, a1, r=R, n=200):
    """Sweep angle a0 -> a1 (radians, math convention). Draw a dab at each step."""
    for i in range(n + 1):
        t = i / n
        a = a0 + (a1 - a0) * t
        x = cx + radius * math.cos(a)
        y = cy + radius * math.sin(a)
        dab(x, y, r)


# --- Layout (image coords, y grows DOWN) ---
# 横 from (55, 105) slightly up to (215, 92) — same tilt as our 横折 template.
heng_start = (55, 105)
heng_end   = (215, 92)

# 竖 drops from the 折 shoulder straight down. Shorter than plain 横折's
# 竖 because a 弯 arc must follow. End the straight run above the arc
# center so the quarter-arc can sweep into a horizontal.
ARC_R = 40                    # arc radius
arc_cx = heng_end[0] - ARC_R  # arc center x = 175
arc_cy = 175                  # arc center y (chosen so bottom sits near y=215)
shu_top = (heng_end[0], heng_end[1])  # continues from shoulder
shu_bot = (heng_end[0], arc_cy)       # top of the arc tangent point

# The arc: from angle 0 (rightmost point of the circle = (arc_cx+R, arc_cy)
# is where the horizontal starts) sweeping backwards to -pi/2
# (topmost = (arc_cx, arc_cy - R) = (175, 135)) — i.e. we draw FROM the
# top-of-arc DOWN and around to the right side.
# In our sweep: start angle = -pi/2 (top of circle), end angle = 0
# (right of circle). That traces top -> lower-right, which is the
# vertical-into-horizontal 弯 shape.

# Terminal 横 running rightward from arc's right tangent point.
horiz_start = (arc_cx + ARC_R, arc_cy)  # (215, 175)
horiz_end   = (265, 175)


# --- Render ---
# 1. 横 with 顿-dabs at both ends. Radius ramps slightly up toward the
#    shoulder (visualizes the pre-corner press per the 折 rules).
dab(*heng_start, r=DUN)
line_dabs(heng_start[0], heng_start[1], heng_end[0], heng_end[1],
          r0=R, r1=R + 1)

# 2. 折 shoulder dab at the corner.
dab(heng_end[0], heng_end[1], r=DUN + 1)

# 3. 竖 straight down from shoulder to the top of the arc.
line_dabs(shu_top[0], shu_top[1], shu_bot[0], shu_bot[1],
          r0=R + 1, r1=R)

# 4. 弯 smooth quarter-arc, tangent-continuous with the 竖 and the
#    terminal 横. No shoulder dab here.
arc_dabs(arc_cx, arc_cy, ARC_R,
         a0=-math.pi / 2, a1=0.0, r=R, n=200)

# 5. Terminal 横 rightward, blunt round end (terminal press, no flick).
line_dabs(horiz_start[0], horiz_start[1], horiz_end[0], horiz_end[1],
          r0=R, r1=R)
dab(*horiz_end, r=DUN)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "01_横折弯.png")
img.save(out)
print(f"Wrote {out}")
