"""
G1 no-memory attempt: p1_stroke_09_横撇
Renders 横撇: a horizontal segment, then a turn down-left as a pie (撇).
Output: 300x300 PNG, white background, black ink.
"""
import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_横撇.png")

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 横撇 shape:
# 1) Horizontal segment (横) starting mid-left, going right with slight upward tilt.
# 2) At the turn point, a small "顿" (pressure dot) — implied by slight thickening.
# 3) A 撇 (pie) sweeping from the turn point down and to the left,
#    tapering to a point.
#
# We approximate ink strokes using thick lines with rounded joins,
# and taper the 撇 by drawing overlapping segments with decreasing width.

# Coordinates in PIL image-space (y grows DOWN).

# --- Horizontal 横 segment ---
heng_start = (70, 110)
heng_end   = (215, 100)   # slight upward tilt to the right
heng_width = 12
draw.line([heng_start, heng_end], fill="black", width=heng_width)

# Small "顿" (pressure) at end of 横 — a small filled ellipse just past the turn
turn = heng_end
r = 9
draw.ellipse([turn[0]-r, turn[1]-r+2, turn[0]+r-2, turn[1]+r+2], fill="black")

# --- 撇 (pie) sweeping down-left, tapering ---
# We render it as many small overlapping segments with decreasing width
# along a curve from `turn` down and to the left to a tip.
tip = (95, 235)  # end of the pie, lower-left

# Quadratic-Bezier-ish curve control point pulled toward down-right of turn
# to give the characteristic 撇 curvature.
ctrl = (200, 190)

def bezier(t, p0, p1, p2):
    x = (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
    y = (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
    return (x, y)

N = 60
prev = turn
for i in range(1, N+1):
    t = i / N
    pt = bezier(t, turn, ctrl, tip)
    # width tapers from ~13 at the head to ~1 at the tip
    w = max(1, int(round(13 * (1 - t) + 1 * t)))
    draw.line([prev, pt], fill="black", width=w)
    prev = pt

# Ensure size
assert img.size == (W, H)
img.save(OUT_PNG)
print(f"Saved {OUT_PNG}")
