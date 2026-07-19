"""
p2_radical_048_干 (3画部首) — G2 attempt 1

干 has 3 strokes:
  1. Short 横 at top (slight upward tilt)
  2. Long 横 across the middle
  3. Long 竖 down the center (top starts slightly above the top 横, extends
     down past the middle 横 to near the bottom)

Canonical stroke order is: 横 (top), 横 (middle), 竖.
GT PNG shows: top short 横 with slight bow/upward tilt, then longer middle
横 (much longer than top), then vertical 竖 dropping straight down through
both 横s, centered.

Rendering with PIL brush-dab technique (per drawer memory).
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(x0, y0, x1, y1, r0, r1, steps=None):
    """Straight line stroke with radius ramp."""
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, r0, r1, steps=200):
    """Quadratic Bezier with radius ramp."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: top short 横 (with slight upward tilt, mild bow) ----
# Position: upper region of canvas, centered horizontally, shorter than middle 横.
# 顿-dab (r+2) at both ends per Phase-1 横 recipe (standalone scale: use r+1).
p0 = (95, 108)
p2 = (200, 100)  # slight up-tilt (left→right, y decreases slightly)
p1 = (150, 100)  # slight bow (curve upward slightly)
dab(p0[0], p0[1], 5.5)  # subtle press at start (standalone: r or r+1, not r+2)
stroke_bezier(p0, p1, p2, r0=5, r1=5)
dab(p2[0], p2[1], 5)   # plain terminal — no visible ball

# ---- Stroke 2: middle long 横 ----
# Longer than top 横, spans most of canvas width, slight up-tilt.
q0 = (55, 168)
q1 = (245, 158)
dab(q0[0], q0[1], 6)   # subtle 顿 press at start (r+0.5)
stroke_line(q0[0], q0[1], q1[0], q1[1], r0=5.5, r1=5.5)
dab(q1[0], q1[1], 5.5)  # plain terminal

# ---- Stroke 3: 竖 down the center ----
# Top starts slightly above the top 横 (so it pokes through), extends down
# past the middle 横 to near the bottom of the canvas.
# Straight vertical.
v_top = (150, 88)
v_bot = (150, 260)
dab(v_top[0], v_top[1], 6)  # subtle 顿 press at top
stroke_line(v_top[0], v_top[1], v_bot[0], v_bot[1], r0=5.5, r1=5.5)
dab(v_bot[0], v_bot[1], 5.5)  # plain blunt terminal

# Save
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_干.png")
img.save(out_path)
print(f"wrote {out_path}")
