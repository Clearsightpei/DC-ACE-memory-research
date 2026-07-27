"""
p3_char_0029_入 — retry #1

Memory consulted:
- memory_index HARD RULE: sibling-pair 人/入 signature-bit — 入 has 捺
  starting HIGHER than 撇 (overhang).
- form_catalog "捺 as right-leg of two-stroke apex": in 入 the 捺 STARTS
  HIGHER and overhangs.
- errata prior fix: 捺 starts at y≈50, 撇 starts at y≈90 (>=30 px offset).
  捺's top must be visibly above and LEFT of the 撇's top.
- GT observation: the 捺 is the visually dominant thick-footed sweeping
  stroke from upper-left to lower-right (long); the 撇 is shorter,
  starts below and RIGHT of the 捺's top and sweeps down-left.

Wait — re-check GT vs canonical: in 入 (as in the GT image), the top-left
stroke is the 撇 (upper-left to lower-left sweep) and the right stroke is
the 捺 (upper-middle to lower-right sweep). Actually 入's canonical order
is 撇 first then 捺. The signature: 撇 starts LOWER than the 捺's top;
the 捺 STARTS at the peak and OVERHANGS the 撇 to the left.

Concretely: in the GT the peak is the top of the 捺 (upper-left area of
the apex). The 撇 attaches to the 捺 body a bit BELOW that peak, sending
its own body down-left. So the 捺 pokes UP-LEFT beyond where the 撇 joins.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, r_start, r_end):
    """Draw a variable-width stroke by dabbing circles along a Bezier/poly path."""
    n = len(points)
    if n < 2:
        return
    # Densify path with linear interpolation between consecutive points
    dense = []
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        seg_len = math.hypot(x2 - x1, y2 - y1)
        steps = max(2, int(seg_len))
        for s in range(steps):
            t = s / steps
            dense.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
    dense.append(points[-1])
    m = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(1, m - 1)
        r = r_start + (r_end - r_start) * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

def bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

# --- Stroke 2 (drawn FIRST for z-ordering): 捺 ---
# The dominant sweeping stroke. Starts HIGH in the upper-left region.
# 捺 start: (120, 50). Its top must be VISIBLY above and LEFT of where
# the 撇 later starts on its body.
# 捺 end: (260, 255) - broad thick terminal foot in lower-right.
na_pts = bezier((120, 50), (180, 155), (260, 255), steps=120)
stroke(na_pts, r_start=3, r_end=12)  # thin -> thick (捺 signature taper)

# Terminal 顿 press on 捺 foot for the broad flat foot
draw.ellipse([248, 246, 270, 262], fill="black")

# --- Stroke 1: 撇 ---
# Starts on the 捺's BODY, well BELOW the 捺's top (y=50).
# 撇 start: (163, 105) - attaches to 捺 body at ~55 px below 捺 top.
# 撇 end: (50, 260) - sweeps to lower-left.
# The 捺 thus visibly OVERHANGS the 撇 to the upper-left — 入 signature.
pie_pts = bezier((163, 105), (105, 180), (50, 260), steps=100)
stroke(pie_pts, r_start=7, r_end=2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0029_入__retry_1/01_入.png")
print("Saved 01_入.png")
