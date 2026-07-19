"""
父 (4 画) — Phase-2 radical.

Strokes (in canonical order):
  1. Top-left 撇 (short, throw-away): upper end starts inside/right,
     sweeps down-and-left. Sits on top-left of the character.
  2. Top-right 点 (dot-like, going down-right):  small teardrop
     dot at top-right. Together with stroke 1 forms the "hat".
  3. Long 撇 (throw-away, main): from upper-right area, big diagonal
     down to lower-left. Thick→thin, gentle rightward bow.
  4. Long 捺 (press-down, main): from upper-left area, big diagonal
     down to lower-right. Thin→thick, broad terminal foot.

Strokes 3 and 4 CROSS in the middle-lower part of the canvas to form
an X shape.  Their crossing signature is central (bootstrap principle 3).

Renderer: PIL brush-dabs, 300×300, black on white.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=400, ease=1.0):
    """Quadratic Bezier, brush-dab stack with linear (or eased) taper."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        # Bezier point
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(P0, P1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = P0[0] + (P1[0] - P0[0]) * t
        y = P0[1] + (P1[1] - P0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ----- Stroke 1: top-left 撇 (short) ------------------------------
# Small throw-away from ~(115, 70) sweeping down-and-left to (75, 115).
# Gently bowed with control point pulled toward interior/right.
bezier_stroke(
    P0=(118, 70),
    P1=(105, 90),
    P2=(72, 118),
    r_start=6.5,
    r_end=1.5,
    ease=1.2,
)
# Small 顿 at start
dab(118, 70, 7.5)

# ----- Stroke 2: top-right stroke (short 横 flicking down-left) -----
# Per GT: this stroke starts up-right, sweeps left-and-down like a
# short 撇/横撇 rather than a plain down-right dot. Model as a curved
# beat from ~(215, 65) arching down-left to ~(175, 115).
bezier_stroke(
    P0=(215, 68),
    P1=(210, 95),
    P2=(178, 118),
    r_start=6.5,
    r_end=2.0,
    ease=1.3,
)
# 顿 at start (upper-right end)
dab(215, 68, 8.0)

# ----- Stroke 3: long 撇 (main throw-away) ------------------------
# From upper-right ~(200, 110) sweeping down to lower-left ~(60, 250).
# Bowed rightward — control point pulled toward interior (right).
bezier_stroke(
    P0=(200, 110),
    P1=(170, 165),
    P2=(58, 250),
    r_start=8.5,
    r_end=1.5,
    ease=1.15,
)
# 顿 at start
dab(200, 110, 10.0)

# ----- Stroke 4: long 捺 (main press-down) ------------------------
# From upper-left ~(100, 130) sweeping down-right to lower-right
# ~(250, 255). Thin→thick, ends in a broad foot.
# Use two-segment: thin bezier body + broad terminal press.
bezier_stroke(
    P0=(102, 130),
    P1=(150, 190),
    P2=(240, 250),
    r_start=2.5,
    r_end=9.5,
    ease=1.4,
)
# broad terminal foot (flatten toe by adding a couple of dabs going out
# horizontally toward the right)
dab(240, 250, 10.5)
dab(247, 252, 9.5)
dab(253, 253, 7.5)
dab(258, 253, 5.5)


out_path = os.path.join(os.path.dirname(__file__), "01_父.png")
img.save(out_path)
print(f"wrote {out_path}")
