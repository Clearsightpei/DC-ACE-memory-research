"""
处 (chu) — 5 strokes:
  1. 撇 (short, top-left)
  2. 横撇  (top-center: short 横 then diagonal 撇 down-left)
  3. 捺  (long sweeping foot from center down to lower-right)
  4. 横  (short horizontal, top-right)
  5. 竖  (long vertical falling from the 横 down through the body)

Consulted memory:
  - form_catalog "捺 as right-leg" (long broad foot)
  - errata p2_radical_081_夂 (needs the middle 横撇 tick, not a plain 撇)
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bez(pts, steps=80):
    """Quadratic or cubic Bezier polyline sampler."""
    n = len(pts) - 1
    out = []
    for i in range(steps + 1):
        t = i / steps
        # de Casteljau
        cur = list(pts)
        for k in range(n, 0, -1):
            cur = [((1 - t) * cur[j][0] + t * cur[j + 1][0],
                    (1 - t) * cur[j][1] + t * cur[j + 1][1])
                   for j in range(k)]
        out.append(cur[0])
    return out

def stroke(pts, widths, steps=80):
    """Draw a tapered stroke: sample bezier, dab a circle at each sample
    with linearly-interpolated width."""
    poly = bez(pts, steps)
    w0, w1 = widths
    for i, (x, y) in enumerate(poly):
        t = i / steps
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- Stroke 1: short 撇 (top-left) --------------------------------
# starts around (115, 55), curves down-left, terminates thin at (68, 130)
stroke([(115, 55), (100, 80), (68, 130)], widths=(9, 3))

# --- Stroke 2: 横撇 (short horizontal, then long diagonal down-left) ---
# 横 across top: (110, 92) -> (170, 95)
# folds and slashes down-left to (95, 180)
stroke([(110, 92), (140, 93), (170, 96)], widths=(6, 8))
stroke([(168, 95), (145, 130), (95, 185)], widths=(9, 3))

# --- Stroke 3: 长捺 (long sweeping foot from mid → lower-right) --------
# starts near the fold of stroke-2 (around 130, 140), bows down, broad terminal at (280, 262)
stroke([(128, 140), (175, 185), (225, 230), (280, 262)], widths=(4, 15))
# broad terminal foot flick out (slight up-right tail)
stroke([(278, 262), (288, 258)], widths=(15, 4))

# --- Stroke 4: 短横 (top-right horizontal) --------------------------
# from (165, 72) to (240, 78)
stroke([(165, 72), (200, 74), (240, 78)], widths=(6, 7))

# --- Stroke 5: 长竖 (long vertical from top-right down through body) --
# from (228, 68) straight down to (218, 240), slight left curve
stroke([(228, 68), (222, 130), (218, 200), (215, 245)], widths=(7, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0212_处/01_处.png")
