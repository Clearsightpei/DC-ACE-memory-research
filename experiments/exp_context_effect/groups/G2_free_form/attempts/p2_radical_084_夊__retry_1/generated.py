"""
p2_radical_084_夊 — retry 1

Prior attempt (retry 0) was too compact and lacked the extended
horizontal foot on the 捺. GT shows 夊 as:
  - a small hooked mark at top (short 横撇 / small ㄋ shape)
  - a long 撇 body sweeping from upper-middle down to lower-LEFT
  - a long, dramatic 捺 sweeping from upper area down to lower-RIGHT
    with a nearly horizontal terminal foot extending well to the right

Cross-refs:
- form_catalog "捺 as right-leg of two-stroke apex" — 捺 dominates
- form_catalog "撇 as body-crossing diagonal" — 撇 crosses through
- errata fix for 夂 (sibling): "shorten top 撇, lengthen 捺"
- 夊 vs 夂: 夊 has FOUR strokes (extra top mark), 夂 has three

Strategy: PIL, brush-dabs along Bezier curves for calligraphic feel.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="black")


def bezier(p0, p1, p2, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_bezier(p0, p1, p2, r_start, r_end, n=200):
    pts = bezier(p0, p1, p2, n)
    for i, (x, y) in enumerate(pts):
        t = i / n
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def stroke_line(p0, p1, r_start, r_end, n=120):
    for i in range(n + 1):
        t = i / n
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ------------------------------------------------------------------
# Stroke 1: small top mark (short 撇 / horizontal-flick at top)
# Small hook-like mark near top-center, slightly leaning
# ------------------------------------------------------------------
stroke_bezier((150, 62), (148, 72), (140, 88), r_start=3, r_end=4)

# ------------------------------------------------------------------
# Stroke 2: short 横撇 (top-right of the top region) — the small
# hooked shape visible at the top of GT. Short horizontal → down-left
# ------------------------------------------------------------------
# short 横 segment
stroke_line((140, 88), (170, 82), r_start=4, r_end=4, n=50)
# shoulder dab
dab(170, 82, 5)
# short 撇 going down-left
stroke_bezier((170, 82), (160, 100), (135, 130), r_start=5, r_end=3)

# ------------------------------------------------------------------
# Stroke 3: long 撇 body — sweeps from upper-middle down to lower-left
# Starts near top-middle around (160,100), curves down-left ending
# near (50, 275). Bezier control pulled right for leftward bow.
# Thicker start for calligraphic weight.
# ------------------------------------------------------------------
stroke_bezier((162, 100), (140, 180), (50, 275), r_start=7, r_end=2)

# ------------------------------------------------------------------
# Stroke 4: dominant 捺 — sweeps down-right with wide, near-horizontal
# terminal foot. Starts near (155, 115), curves down-right, ends with
# an extended horizontal foot around (255, 245).
# Split into two arcs: (a) main descending curve; (b) horizontal foot.
# ------------------------------------------------------------------
# Main 捺 body (thin -> thick)
stroke_bezier((155, 115), (175, 175), (215, 235), r_start=3, r_end=9)
# Horizontal terminal foot — sweeping rightward with slight taper
stroke_bezier((215, 235), (240, 244), (272, 248), r_start=9, r_end=4)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_084_夊__retry_1/01_夊.png"
)
print("done")
