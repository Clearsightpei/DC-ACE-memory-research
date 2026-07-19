"""
p2_radical_048_干 (3画部首) — G2 retry_1

Prior attempt failed: top 横 was too close in length to bottom 横 (ambiguous
with 千/士). Fix per errata: length ratio top:bottom = ~0.50-0.60, plus more
pronounced up-tilt on the top 横 so it reads clearly as the "shorter upper".

Per memory rule 6 (length-ratio distinguishers for stacked-horizontal
radicals): 干 = short top 横 (~65% of bottom, target ~110px), LONGER bottom
横 (~170-190px), pass-through vertical with NO hook.

Design:
  1. Top 横: length ~100px, upper region, tilted upward left→right (bow up).
  2. Bottom 横: length ~200px (2x top), across middle, mild up-tilt.
  3. Vertical: straight through both, pokes slightly above top 横, extends
     well below bottom 横, blunt terminal (NO hook — else reads as 千).

Ratio delivered: 100/200 = 0.50 (comfortably in <0.65 band).
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
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: TOP short 横 (length ~100 px, ~0.50 of bottom) ----
# Center it around x=150. Extends from x=100 to x=200 (100 px wide).
# Slight up-tilt with mild bow upward.
p0 = (100, 112)
p2 = (200, 102)      # ends 10 px higher -> up-tilt
p1 = (150, 100)      # bow apex slightly higher than either end
dab(p0[0], p0[1], 5.5)
stroke_bezier(p0, p1, p2, r0=5, r1=5)
dab(p2[0], p2[1], 5)

# ---- Stroke 2: BOTTOM long 横 (length ~200 px, dominant width) ----
# From x=50 to x=250 (200 px). Mild up-tilt (~10 px rise across width).
q0 = (50, 175)
q1 = (250, 165)
dab(q0[0], q0[1], 6.5)  # slight 顿 press at start
stroke_line(q0[0], q0[1], q1[0], q1[1], r0=5.5, r1=5.5)
dab(q1[0], q1[1], 5.5)

# ---- Stroke 3: 竖 pass-through, NO hook ----
# Top pokes ~10 px above top 横; bottom extends well below middle 横.
v_top = (150, 92)
v_bot = (150, 265)
dab(v_top[0], v_top[1], 6)
stroke_line(v_top[0], v_top[1], v_bot[0], v_bot[1], r0=5.5, r1=5.5)
dab(v_bot[0], v_bot[1], 5.5)  # blunt — NO hook

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_干.png")
img.save(out_path)
print(f"wrote {out_path}")
