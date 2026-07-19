"""Render 爿 (radical 107, 4 strokes) at 300x300, PIL brush-dabs.

Stroke order (爿, 4 画):
  1. Short slanted 竖/点 top-left (upper-left short stroke going down-slightly-left)
  2. 横折 in the middle-left area (short 横 folding down into a short 竖)
  3. Long tall 竖 on the right (dominant right vertical, top→bottom)
  4. Bottom 横 running rightward from left edge through/under the right vertical

Image coords, y grows DOWN. Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(80, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# Standalone-scale discipline: no r+2 balls at plain terminals; use r+0..1 only.

# ---------- Stroke 1: short slanted 撇-like mark, top-left ----------
# Upper-right → lower-left, longer and more diagonal than a dot.
# Gentle rightward bow via Bezier.
p1_p0 = (135, 75)
p1_p2 = (80, 115)
p1_p1 = (120, 92)  # bow control (pull toward interior)
bezier_taper(p1_p0, p1_p1, p1_p2, 6, 1.5)
dab(p1_p0[0], p1_p0[1], 6)  # subtle start press (no ball)

# ---------- Stroke 2: 横折 in middle-left (short 横 + shoulder + short 竖) ----------
s2_hx0, s2_hy0 = 78, 155
s2_hx1, s2_hy1 = 162, 148  # slight up-tilt
dab(s2_hx0, s2_hy0, 6)  # subtle 顿 start (no ball)
line_taper(s2_hx0, s2_hy0, s2_hx1, s2_hy1, 5.5, 5.5)
# Shoulder dab (real 折 corner — allowed to be slightly larger)
dab(s2_hx1, s2_hy1, 7)
# Short 竖 going down from shoulder, slight inward lean
s2_vx0, s2_vy0 = s2_hx1, s2_hy1
s2_vx1, s2_vy1 = s2_hx1 - 3, s2_hy1 + 55
line_taper(s2_vx0, s2_vy0, s2_vx1, s2_vy1, 5.5, 5)
# Blunt end (very subtle, no ball)
dab(s2_vx1, s2_vy1, 5)

# ---------- Stroke 3: long tall right 竖 ----------
# Dominant vertical spans most of canvas height.
s3_x0, s3_y0 = 228, 55
s3_x1, s3_y1 = 228, 265
dab(s3_x0, s3_y0, 7)  # subtle 顿 start
line_taper(s3_x0, s3_y0, s3_x1, s3_y1, 6, 6)
dab(s3_x1, s3_y1, 6.5)  # subtle blunt end (no ball)

# ---------- Stroke 4: bottom 横 running rightward through right 竖 ----------
# Starts at left edge, runs THROUGH the right vertical (per principle 8 spirit —
# bottom stroke joins the body, not floating short of it).
s4_x0, s4_y0 = 55, 240
s4_x1, s4_y1 = 250, 232  # slight up-tilt; extends past right 竖 x=228
dab(s4_x0, s4_y0, 6)  # subtle 顿 start
line_taper(s4_x0, s4_y0, s4_x1, s4_y1, 5.5, 5.5)
dab(s4_x1, s4_y1, 6)  # subtle 顿 end (no ball)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_爿.png")
img.save(out)
print(f"Saved {out}")
