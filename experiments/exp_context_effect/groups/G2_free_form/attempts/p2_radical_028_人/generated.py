"""
p2_radical_028_人 — G2 free-form drawer

人 is a 2-stroke radical:
  1) 撇 (pie): starts near top-center (apex), sweeps down-and-left,
     gently bowing (belly on the lower-left side of the chord),
     tapering to a sharp tip at lower-left.
  2) 捺 (na): starts at the SAME apex point (shared joint, no inset),
     sweeps down-and-right, straight then gently curving, thickening
     into a broad foot at lower-right, ending with a small tapered
     tail flick.

Renderer: PIL brush-dabs along Bezier paths for calligraphic taper.
Canvas: 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300

img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def bezier_quad(p0, p1, p2, t):
    """Quadratic Bezier point at t in [0,1]."""
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def stroke_bezier(p0, p1, p2, r_start, r_end, steps=500,
                  head_press=None):
    """Draw a Bezier stroke via brush-dabs with linear radius ramp.

    head_press: if not None, add a slightly-larger dab at p0 with this
    radius (for 顿 press at start).
    """
    if head_press is not None:
        dab(p0[0], p0[1], head_press)
    for i in range(steps + 1):
        t = i / steps
        x, y = bezier_quad(p0, p1, p2, t)
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Apex (shared joint) near top-center ---
apex = (150, 62)

# --- Stroke 1: 撇 ---
# Start at apex, sweep down-and-left in a long bowed curve,
# tapering to a sharp tip near the lower-left corner.
# Belly on the LOWER-LEFT of the chord (concave toward upper-right).
pie_start = apex
pie_end = (38, 258)
# Control point pulled left-and-down to bow the curve outward.
pie_ctrl = (85, 210)
stroke_bezier(pie_start, pie_ctrl, pie_end,
              r_start=4.5, r_end=1.2, steps=600,
              head_press=5.5)

# --- Stroke 2: 捺 ---
# Start at the SAME apex, sweep down-and-right, thin -> thick,
# broadening into a foot at the lower-right, then a short tail
# flick tapering to a sharp tip going right (and very slightly up).
na_start = apex
na_body_end = (232, 238)  # broad-foot base, lower-right
# Gentle curve, belly on the lower-left (concave toward upper-right).
na_body_ctrl = (185, 155)
stroke_bezier(na_start, na_body_ctrl, na_body_end,
              r_start=2.5, r_end=9.0, steps=600,
              head_press=None)

# Broad-foot press: one slightly-larger dab to seat the foot.
dab(na_body_end[0], na_body_end[1], 9.5)

# Tail flick: from broad foot, sweep right and very slightly up,
# tapering to a sharp tip. Characteristic 捺 exit.
tail_end = (275, 232)
tail_ctrl = (255, 238)
stroke_bezier(na_body_end, tail_ctrl, tail_end,
              r_start=9.0, r_end=1.0, steps=300,
              head_press=None)

# --- Save ---
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_人.png")
img.save(out_path)
print(f"wrote {out_path}")
