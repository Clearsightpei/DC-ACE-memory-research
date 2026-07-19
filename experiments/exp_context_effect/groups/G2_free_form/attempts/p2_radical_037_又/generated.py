"""
Render 又 (yòu) — 2画部首 — at 300x300, PIL brush-dab technique.

Structure (2 strokes, per MMH & the GT PNG):
  Stroke 1: 横撇 (heng-pie) — short 横 with slight up-tilt, sharp shouldered
            corner, then a bowed 撇 tail going down-and-left.
  Stroke 2: 捺 (na) — starts on/near the 撇's mid-shaft (crossing it),
            goes down-and-right, thin→thick, ending in a broad flat foot.

Following G2 memory principles:
  - Compound 横撇 = 横 + shoulder dab + bowed 撇 (not ruler-straight).
  - Two strokes CROSS visibly — the 捺 must clearly cross through the 撇.
  - Standalone radical: pronounced curvature, smaller start-press (r=6-8),
    plain-radius terminal (no visible ball).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line_segment(x0, y0, x1, y1, r0, r1, steps=None):
    """Straight tapered segment via brush-dabs."""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(length * 2.5), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

def bezier_taper(P0, P1, P2, r0, r1, steps=200):
    """Quadratic Bezier via brush-dabs with linearly-varying radius."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u*u*P0[0] + 2*u*t*P1[0] + t*t*P2[0]
        y = u*u*P0[1] + 2*u*t*P1[1] + t*t*P2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# =============================================================
# REVISION notes vs GT:
#  - Stroke weights were too thick everywhere. GT has near-uniform
#    thin ink around r=3.  Drop base radius.
#  - 顿-dab balls at start were visible on standalone (memory rule).
#    Reduce start-press to plain radius or +1 only.
#  - 撇 tip was too far down-and-left with too much bow — GT's 撇 tip
#    lands closer to the 捺-start x, giving a slimmer crossing X.
#  - 捺 foot was a fat club — reduce max radius, replace flat-ellipse
#    press with a subtle tapered end.
# =============================================================

BASE_R = 3.2   # uniform "thin" ink

# =============================================================
# Stroke 1: 横撇
# =============================================================
h_start = (85, 105)
h_end   = (200, 93)

# tiny start press
dab(h_start[0], h_start[1], BASE_R + 1.2)
line_segment(h_start[0], h_start[1], h_end[0], h_end[1], BASE_R, BASE_R)

# subtle shoulder press (avoid tumor)
dab(h_end[0], h_end[1], BASE_R + 1.5)

# 撇 tail — bowed Bezier, thick→thin. Tail lands lower-left but not
# quite as far left as before, so the crossing X is clean.
pie_P0 = h_end
pie_P2 = (95, 250)
pie_P1 = (170, 175)          # gentle rightward bow
bezier_taper(pie_P0, pie_P1, pie_P2, r0=BASE_R + 0.8, r1=1.0, steps=260)

# =============================================================
# Stroke 2: 捺  (thin→thick, tapered foot)
# =============================================================
# Start above/on the 撇's upper shaft so it visibly crosses.
na_P0 = (118, 118)
na_P2 = (255, 250)
na_P1 = (185, 175)

# Draw 捺 as a Bezier with growing radius (thin start → thick end)
bezier_taper(na_P0, na_P1, na_P2, r0=1.3, r1=5.5, steps=280)

# Modest terminal foot — small horizontally-biased press, not a club.
foot_x, foot_y = na_P2
draw.ellipse((foot_x - 8, foot_y - 3.5, foot_x + 4, foot_y + 3.5), fill="black")

# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_037_又/01_又.png"
img.save(out_path)
print(f"Wrote {out_path}")
