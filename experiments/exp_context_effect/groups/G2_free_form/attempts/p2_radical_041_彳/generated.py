"""
彳 (chi) — double-standing-person radical, 3 strokes.

Structure (from GT):
  1. Short 撇 (top): starts upper-right, throws down-and-left, short. Sits near
     the vertical column, above and slightly right of the second 撇's start.
  2. Longer 撇 (middle): starts on the vertical column area, throws down-and-
     -left, longer than stroke 1. Its top-right end joins the vertical column
     of stroke 3 near its midpoint.
  3. 竖 (vertical): a straight vertical descending from where stroke 2 meets
     the column, down to bottom. This is the "leg."

Renderer: PIL brush-dabs, black ink on white 300x300 canvas.
Coordinates in image space (y grows DOWN).
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r0, r1, steps=400, dun_start=None):
    """Quadratic Bezier stroke with linear-in-t taper r0->r1.
    dun_start: optional extra dab radius at P0.
    """
    if dun_start is not None:
        dab(p0[0], p0[1], dun_start)
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        # ease radius slightly for smoother taper
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def line_stroke(p0, p1, r0, r1, steps=300, dun_start=None, dun_end=None):
    if dun_start is not None:
        dab(p0[0], p0[1], dun_start)
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)
    if dun_end is not None:
        dab(p1[0], p1[1], dun_end)


# --- Stroke 1: short 撇 (top) ---
# Short throw at the very top-right, well ABOVE stroke 2 with clear vertical
# spacing so both strokes read as distinct.
s1_p0 = (180, 55)
s1_p2 = (150, 100)
s1_p1 = (175, 75)  # gentle rightward bow
bezier_stroke(s1_p0, s1_p1, s1_p2, r0=5.5, r1=1.5, dun_start=7)

# --- Stroke 2: longer 撇 (middle) ---
# Distinctly BELOW stroke 1 with clear gap. Longer sweep down-and-left. The
# top-right of this 撇 is where the 竖 (stroke 3) attaches.
s2_p0 = (185, 120)     # top-right start; joint with stroke 3
s2_p2 = (85, 215)      # lower-left tip, further left/down for length
s2_p1 = (170, 165)     # gentle rightward bow (belly on right)
bezier_stroke(s2_p0, s2_p1, s2_p2, r0=7, r1=1.5, dun_start=8)

# --- Stroke 3: 竖 (vertical leg) ---
# Straight vertical descending from the joint with stroke 2 down to bottom.
dab(185, 120, 8)  # shared-corner 顿 press
line_stroke((185, 120), (185, 255), r0=5.5, r1=5.5, dun_end=7)

img.save("01_彳.png")
