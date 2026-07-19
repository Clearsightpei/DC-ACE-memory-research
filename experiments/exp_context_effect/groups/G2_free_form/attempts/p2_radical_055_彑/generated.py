"""Render 彑 (radical 055, 3 strokes) at 300x300, PIL brush-dabs.

Structure (from GT observation):
  Stroke 1: 横折 at the top — a short 横 going right, then a shoulder,
            then a short 竖 going down. (upper-right corner piece)
  Stroke 2: 横 in the middle, roughly aligned with the bottom of
            stroke 1's 竖, extending leftward AND slightly beyond.
            The GT actually shows the middle stroke as a 横折 shape
            too — going left then hooking. Looking more carefully:
            it is a shorter 横 in the middle zone.
  Stroke 3: long 横 at the bottom, spanning the full width, roughly
            uniform, with slight upward tilt at both ends (like a
            gently bowed 横).

Coordinates in image-coords (y grows DOWN).
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_seg(x0, y0, x1, y1, r0, r1, steps=None):
    """Draw a tapered line with brush dabs from (x0,y0) to (x1,y1)."""
    if steps is None:
        steps = int(max(abs(x1 - x0), abs(y1 - y0)) * 3) + 20
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_seg(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ------------------------------------------------------------------
# Stroke 1: 横折 at top-right (short 横 + shoulder + longer 竖)
# The GT shows the top-right corner piece with a taller vertical.
# 横 primary: (135, 75) -> (200, 68)  [slight up-tilt]
# shoulder dab at (200, 68) r+2.5
# 竖 down: (200, 68) -> (185, 170)  [slight left lean, longer]
# ------------------------------------------------------------------
r_main = 4.5
# 横 top
line_seg(135, 75, 200, 68, r_main, r_main + 0.3)
# shoulder press
dab(200, 68, r_main + 2.5)
# 竖 down (slight left lean), longer
line_seg(200, 68, 185, 170, r_main + 0.3, r_main)
# blunt terminal press
dab(185, 170, r_main + 1)

# ------------------------------------------------------------------
# Stroke 2: middle 横 — extends from left across to meet the bottom
# of stroke 1's 竖. In GT it sits around y=155-170 area.
# From (80, 168) to (215, 160) with slight upward tilt.
# ------------------------------------------------------------------
# 顿 start
dab(80, 168, r_main + 1.8)
line_seg(80, 168, 215, 160, r_main, r_main + 0.2)
# terminal press
dab(215, 160, r_main + 1.8)

# ------------------------------------------------------------------
# Stroke 3: long bottom 横 spanning the full canvas width, gentle
# upward bow, 顿 dabs at both ends.
# From (35, 245) to (275, 240).
# ------------------------------------------------------------------
# start 顿
dab(35, 245, r_main + 2)
# shallow Bezier for slight upward bow
bezier_seg((35, 245), (155, 232), (275, 240), r_main + 0.3, r_main + 0.3, steps=280)
# terminal 顿
dab(275, 240, r_main + 2)


# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_彑.png")
img.save(out_path)
print(f"Saved {out_path}")
