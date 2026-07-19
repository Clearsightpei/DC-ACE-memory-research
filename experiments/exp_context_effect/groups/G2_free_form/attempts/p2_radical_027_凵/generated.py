"""
p2_radical_027_凵  — 2 strokes.

Structure (from GT):
  凵 is a U-container radical. Two strokes:
    Stroke 1 = 竖折: a vertical descending on the LEFT that turns
      at the bottom-left corner into a horizontal running RIGHTWARD
      to the bottom-right. One shoulder-dab at the corner. Blunt end.
    Stroke 2 = 竖: a short vertical on the RIGHT, descending from the
      top-right down to (or slightly past) the level of the horizontal
      base of stroke 1 — meeting the base near its right end.

Placement fills roughly the middle band of a 300x300 canvas: left
column ~x=80, right column ~x=220, top ~y=110, bottom ~y=225. The
right 竖 typically extends slightly BELOW the horizontal base at its
foot in the MMH glyph (hence in the GT it slightly overshoots).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(40, int(dist * 2.2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------- Stroke 1: 竖折 (left vertical -> bottom horizontal) ----------
# Left vertical segment
LV_TOP = (85, 108)
LV_BOT = (85, 218)   # bottom-left corner (shoulder)
R_STEM = 5.2

# 顿-dab at very top of the left 竖 (start press). Standalone-scale: r+1 subtle.
dab(LV_TOP[0], LV_TOP[1], R_STEM + 1.2)
line_dabs(LV_TOP[0], LV_TOP[1], LV_BOT[0], LV_BOT[1], R_STEM, R_STEM + 0.4)

# Shoulder dab at the bottom-left corner (顿 press for the 折).
dab(LV_BOT[0], LV_BOT[1], R_STEM + 2.4)

# Bottom horizontal — running rightward. Slight upward tilt (calligraphic).
BH_END = (222, 214)
line_dabs(LV_BOT[0], LV_BOT[1], BH_END[0], BH_END[1], R_STEM + 0.4, R_STEM)
# Blunt end dab (subtle) at right end of horizontal.
dab(BH_END[0], BH_END[1], R_STEM + 0.5)


# ---------- Stroke 2: 竖 (right vertical, descending) ----------
# Descends from top-right to slightly below the horizontal base near its
# right endpoint. Standalone: light 顿 at start; blunt small end.
RV_TOP = (222, 112)
RV_BOT = (222, 228)   # slightly past the base — matches MMH overshoot

dab(RV_TOP[0], RV_TOP[1], R_STEM + 1.2)
line_dabs(RV_TOP[0], RV_TOP[1], RV_BOT[0], RV_BOT[1], R_STEM, R_STEM + 0.2)
dab(RV_BOT[0], RV_BOT[1], R_STEM + 0.5)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_027_凵/01_凵.png")
