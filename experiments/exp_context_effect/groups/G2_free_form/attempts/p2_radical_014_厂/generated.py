"""Render 厂 (2-stroke radical) at 300x300, black ink on white.

Structure:
  - Stroke 1 (横): a heng starting slightly left, ending upper-right, with
    a small initial dun press. In the GT the heng is short-ish and tilted
    slightly downward toward the right (actually looks near-flat).
  - Stroke 2 (撇): a long bowed pie that starts near the LEFT END of the
    heng (they SHARE that joint), then drops down and curves gently to
    the lower-left. Thick at top, tapering thin at the tip.

PIL brush-dab technique per drawer_memory.md.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400, ease=1.0):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# --- Stroke 1: 横 across the top ---------------------------------------------
# Heng starts at upper-left area, tilts up to the right. The 撇 will
# start slightly to the RIGHT of the heng's left end (creating the small
# hooked-notch signature of 厂), not exactly at the corner.
HENG_START = (75, 105)
HENG_END = (245, 82)   # noticeable up-tilt (23 px rise over 170 px run)

# initial dun press (subtle, standalone scale — small)
dab(HENG_START[0], HENG_START[1], 6)
line_dabs(HENG_START, HENG_END, r0=5.0, r1=4.5, steps=400)
# terminal endpoint (plain, thin tip-off)
dab(HENG_END[0], HENG_END[1], 4)


# --- Stroke 2: 撇 dropping and curving ---------------------------------------
# Signature 厂 pie: starts near the LEFT PORTION of the heng (slightly
# inset from the very corner, with a small notch/hook back-and-down),
# then a LONG curve descending down-and-slightly-left with belly on the
# right (concave-left). Ends in a fine thin tip near lower-left — NO
# upward hook.
# GT reads: initial nub goes down-and-slightly-LEFT then bows back to
# nearly vertical, tapering to a thin tip around (75, 265).
PIE_START = (110, 95)        # inset right of heng's leftmost point
PIE_END = (72, 268)          # long, ends low-left
PIE_CTRL = (135, 210)        # control point pulled RIGHT → belly on right

# small initial press at the pie's origin (the visible top-nub of 厂)
dab(PIE_START[0], PIE_START[1], 7)

bezier_dabs(PIE_START, PIE_END, PIE_CTRL, r0=7.5, r1=1.2, steps=600, ease=1.4)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_014_厂/01_厂.png"
)
