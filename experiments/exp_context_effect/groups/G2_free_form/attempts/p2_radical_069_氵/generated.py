"""
氵 (three-drops water radical) — 3 strokes: 点 + 点 + 提
Standalone radical, 300x300 white canvas, black PIL brush-dab render.

Layout (image coords, y grows DOWN):
  - top 点: teardrop, upper-left area, slant down-right
  - middle 点: teardrop, middle-left area, slightly right of top, slant down-right
  - bottom 提: rising stroke, lower-left → upper-right, thick→thin sharp tip

The three-drop cluster reads as diagonal descending line from upper-left
to lower-middle then springing back up-right with the 提.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def teardrop(p0, p1, r0, r1, steps=200, easing=1.4):
    """Thin->thick teardrop dot (点). Radius eases with t**easing."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        tt = t ** easing
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    # small terminal press
    dab(x1, y1, r1 + 1)


def ti_stroke(p0, p1, r_start, r_end, steps=300):
    """提 (rising): thick -> thin sharp tip. Small 顿 press at start."""
    x0, y0 = p0
    x1, y1 = p1
    # start press
    dab(x0, y0, r_start + 2)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- 点 #1 (top) — small teardrop upper-middle-left, slanting down-right ---
# GT shows top mark positioned around upper-middle, small and restrained.
teardrop(p0=(135, 55), p1=(160, 95), r0=1.8, r1=6.0)

# --- 点 #2 (middle) — small teardrop middle-left, offset left of top ---
# GT shows this dot is left of top and mid-height, smaller than top.
teardrop(p0=(95, 125), p1=(125, 155), r0=1.8, r1=5.5)

# --- 提 (bottom rising stroke) ---
# Lower-left thick, rises up-and-right to sharp tip. Angle ~30°.
# This is the longest stroke and anchors the cluster.
ti_stroke(p0=(90, 250), p1=(180, 190), r_start=6.5, r_end=1.0, steps=350)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_069_氵/01_氵.png")
