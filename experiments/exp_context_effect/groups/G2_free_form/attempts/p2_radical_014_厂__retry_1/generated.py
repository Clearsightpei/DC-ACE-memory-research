"""
G2 retry #1 of p2_radical_014_厂.

Fix idea (from errata):
- Prior attempt separated 横 and 撇 (35 px horizontal gap, 10 px vertical gap)
  producing a stubby 横 + floating comma. The radical's signature is the
  shared top-left CORNER, so the 撇 must start at the SAME pixel as the 横's
  left endpoint.
- Draw a small 顿 dab at the shared corner.
- 横 sweeps slightly UP-and-RIGHT (rise ~5 px), tapering slightly at right end.
- 撇 curls DOWN-and-slightly-LEFT with belly on the RIGHT (concave-left),
  tapering thick-to-thin, ending near the lower-left region.

Renderer: PIL brush-dabs (per drawer_memory) at 300x300 white, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Shared top-left corner of the radical
CORNER = (72, 78)

def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")

def line_dabs(p0, p1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

def bezier_dabs(p0, p1, p2, r0, r1, steps=500):
    # Quadratic bezier
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# --- Stroke 1: 横 (rightward, slight up-tilt) ---
# starts at shared corner, sweeps up-right; 顿 press at start
heng_start = CORNER            # (72, 78)
heng_end = (225, 72)           # rises ~6 px over ~153 px = ~2.2 degrees
# uniform-ish width, gentle taper at right end (small blunt press)
line_dabs(heng_start, heng_end, r0=5.0, r1=3.8, steps=450)
# small terminal blunt press at right end
dab(heng_end[0], heng_end[1], 4.2)

# --- Shared corner 顿 dab (r+2) ---
dab(CORNER[0], CORNER[1], 7.5)

# --- Stroke 2: 撇 (throw-away, belly on RIGHT, curves down-and-slightly-left) ---
# Starts at the SAME corner as the 横.
# Quadratic Bezier: P0 = corner, P2 = lower-left tip, P1 pulled to the RIGHT
# (belly on right ⇒ arc concave toward the LEFT).
pie_start = CORNER              # (72, 78)
pie_end   = (55, 268)           # ends further left+down for a swept tip
pie_ctrl  = (115, 170)          # control pulled right ⇒ belly on right side

# Thick at start (顿 seat), tapering to sharp tip
bezier_dabs(pie_start, pie_ctrl, pie_end, r0=6.5, r1=1.2, steps=600)

# --- Save ---
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "01_厂.png")
img.save(out)
print(f"saved {out}")
