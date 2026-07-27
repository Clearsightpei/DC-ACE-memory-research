"""
夂 (zhǐ) — 3-stroke radical. RETRY #2.

Errata fix (from errata.md B3 note):
  "捺 present but too short/flat; compact 'each' silhouette not
   achieved. Fix: shorten top 撇 (~50 px) and lengthen 捺 (~150 px)
   with r_end ~10 for broad terminal foot. Let the 捺 dominate."

Prior retry_1 (FAILED): 捺 started at y=155 and reached only (240,232)
— total ~120 px chord and thin r_end=3.5. It read as compact but the
捺 didn't dominate; whole glyph felt weak/short-legged.

Retry_2 plan:
  1. Stroke 1: short 撇 flick top-left (~30 px, not the huge 60 the
     first pass had). Compact — this is a "tick" mark, not a body stroke.
  2. Stroke 2 (横撇): small angular horizontal shoulder at top (short
     ~40 px 横) → long sweeping 撇 tail down-and-left to about y=210.
  3. Stroke 3 (捺): the DOMINATING stroke. Starts up near the shoulder
     of stroke-2 (~y=100), sweeps down-and-right in a long slightly-
     bowed arc all the way to (~265, 240) — chord ~180 px. Thin→thick
     taper r_start=1.2 → r_end=10 for a broad calligraphic foot.
     Small horizontal press extension at the terminal for the classic
     捺 "spatula" foot.

Silhouette target: compact upper-body, long right-diagonal foot
sweeping past the right wall. Should read as unambiguous 夂 (each-top).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dab(p0, p1, r_start, r_end, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dab(p0, p1, p2, r_start, r_end, steps=260, ease=1.0):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ------------- Stroke 1: SHORT 撇 flick top-left -----------------------
# A small tick — NOT a body stroke. Above the 横撇 shoulder, tilting
# down-and-left. ~30 px chord.
s1_start = (142, 82)
s1_end = (118, 108)
dab(s1_start[0], s1_start[1], 2.8)
bezier_dab(s1_start, (128, 92), s1_end, r_start=2.6, r_end=0.9, ease=1.3)


# ------------- Stroke 2: 横撇 (short shoulder + LONG 撇 tail) -----------
# Short horizontal shoulder at top
heng_start = (135, 105)
heng_corner = (178, 100)
line_dab(heng_start, heng_corner, r_start=2.6, r_end=2.6, steps=90)
dab(heng_start[0], heng_start[1], 3.0)
# angular shoulder dab (small)
dab(heng_corner[0], heng_corner[1], 3.4)

# 撇 tail: long sweep down-and-left from the shoulder corner
pie_p0 = heng_corner
pie_p2 = (75, 220)         # further down-left than retry_1's (85,235)
pie_ctrl = (160, 170)      # rightward bow
bezier_dab(pie_p0, pie_ctrl, pie_p2, r_start=3.0, r_end=0.8, ease=1.4)


# ------------- Stroke 3: 捺 — DOMINATING right-diagonal -----------------
# REVISION: retry_2 first pass had r_end=10 → wedge blob. GT shows a
# graceful thin→moderate taper. Reduce r_end to ~6 and soften the
# foot extension to a short taper tip rather than a heavy wedge.
# LENGTH is what dominates, not thickness.
na_p0 = (150, 108)         # start high (near shoulder)
na_p2 = (258, 236)         # end far bottom-right
na_ctrl = (195, 165)       # gentle downward-right bow
bezier_dab(na_p0, na_ctrl, na_p2, r_start=1.2, r_end=6.0, ease=1.4)

# Small spatula-foot tip: brief right extension tapering to a point.
foot_start = na_p2
foot_end = (275, 240)
line_dab(foot_start, foot_end, r_start=5.5, r_end=0.8, steps=55)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_081_夂__retry_2/01_夂.png"
)
