"""
Render 丨 (shu, the vertical stroke) as a standalone Phase-3 character.

Observation of GT:
- A single vertical stroke roughly centered horizontally (slight left of
  center in the GT, but for a standalone 丨 it should read as a vertical
  in the middle of the canvas).
- Top has a slight "entry" — the ink appears to curve in gently from the
  upper right into a straight vertical descent (顿笔 dab plus tiny hook-
  down entry). Bottom tapers to a blunt terminal.
- Length ~200 px on a 300x300 canvas.

Approach: PIL brush-dabs (per drawer_memory technique). Draw a small
curved entry arc at the top-right, then a straight vertical body with
mostly uniform radius, tapering slightly at the bottom.
"""

from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def sample_line(x0, y0, x1, y1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def sample_quad_bezier(p0, p1, p2, r_start, r_end, steps=120):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# GT places the vertical slightly LEFT of canvas center.
cx = 142

# Top of stroke: subtle entry curve (small rightward bump at the very top)
# Very gentle — the GT's top hooks right by only ~6 px.
p0 = (cx + 6, 60)     # entry point, upper-right, tiny
p1 = (cx + 4, 66)     # control (short bend)
p2 = (cx, 80)         # settles onto the axis
sample_quad_bezier(p0, p1, p2, r_start=3.0, r_end=4.0, steps=100)

# Straight vertical body from ~y=80 down to ~y=250 — THINNER than default.
sample_line(cx, 80, cx, 250, r_start=4.0, r_end=3.2, steps=350)

# Blunt terminal
dab(cx, 250, 3.2)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_丨.png")
img.save(out)
print(f"wrote {out}")
