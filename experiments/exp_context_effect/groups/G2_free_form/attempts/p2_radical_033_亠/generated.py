"""
Render radical 亠 (tou) at 300x300, white bg, black ink.

亠 = 2 strokes:
  1) 点 (dian, dot) — small tapered stroke, top-center. Written top-left → bottom-right,
     thin → thick, short (~30 px length). Positioned above the horizontal.
  2) 横 (heng) — long horizontal stroke below the dot. Slight upward tilt (3-5 deg),
     small end press. Wider than the dot's horizontal span.

Rendered with PIL brush-dabs (per drawer_memory principle).
Looking at GT: the dot is oriented as a 撇-like short throw (upper-right → lower-left is
NOT what GT shows). GT shows the dot going top-left → bottom-right (standard 点).
Actually re-reading GT: the dot appears to slant top-right → lower-left. In modern
brush 亠, both orientations occur; standard printed form is top-right → bottom-left
diagonal (i.e., a 点 written with rightward-slanting body). We'll match GT.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_stroke(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r_start, r_end, steps=400):
    """Quadratic Bezier with per-step radius."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Stroke 1: 点 (dot on top) ----
# GT shows dot slanting from upper-LEFT (thin) → lower-RIGHT (thick), with a
# gentle curve (concave-down / belly bowing to the right). This is a standard
# "right-falling" 点. In 亠 it typically sits offset slightly left of center.
# Positioned so its lower-right tip lands well above the 横.
p0_dot = (135, 130)   # top-left (thin)
p1_dot = (148, 142)   # control — pulls curve slightly right (bow)
p2_dot = (158, 168)   # bottom-right (thick)
dab_bezier(p0_dot, p1_dot, p2_dot, r_start=1.5, r_end=4.5, steps=200)
# Small terminal press
draw.ellipse((p2_dot[0] - 5, p2_dot[1] - 5, p2_dot[0] + 5, p2_dot[1] + 5), fill="black")


# ---- Stroke 2: 横 (long horizontal, mildly bowed) ----
# GT shows a long horizontal below the dot with a subtle upward bow (belly-down)
# in the middle — it dips slightly. Left end and right end sit slightly higher
# than the middle. Use a shallow bezier to capture this.
# Left ≈ (55, 195), right ≈ (250, 190), belly middle ≈ (150, 205).
p0_h = (55, 195)
p1_h = (150, 208)  # control pulled downward → belly-down curve
p2_h = (250, 190)
dab_bezier(p0_h, p1_h, p2_h, r_start=3.5, r_end=3.5, steps=400)
# Small initial 顿 press
draw.ellipse((p0_h[0] - 5, p0_h[1] - 5, p0_h[0] + 5, p0_h[1] + 5), fill="black")
# End press (small terminal 顿)
draw.ellipse((p2_h[0] - 5, p2_h[1] - 5, p2_h[0] + 5, p2_h[1] + 5), fill="black")


out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_033_亠/01_亠.png"
img.save(out)
print(f"Saved {out}")
