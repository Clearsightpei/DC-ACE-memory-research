"""
矢 — arrow. 5 strokes:
  1. 撇 short (top-left slant, small)
  2. 横 short (upper horizontal, sits under stroke 1)
  3. 横 longer (middle horizontal, wider than 2)
  4. 撇 long (from top-center sweeping down-left, crossing horizontals)
  5. 捺 (from crossing point down-right)

Not in TIER-0 sibling table (矢 itself isn't listed, though 大/夫/天 family
is nearby). No 钩 anywhere. Silhouette: top-heavy triangle with wide base
formed by 撇+捺 (like 天/夫/矢 family).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p0, p1, width=6):
    d.line([p0, p1], fill=BLACK, width=width)

def stroke_taper(points, w_start=7, w_end=5):
    # brush-dab varying width along polyline
    n = len(points) - 1
    for i in range(n):
        t = i / max(1, n - 1)
        w = int(round(w_start * (1 - t) + w_end * t))
        d.line([points[i], points[i+1]], fill=BLACK, width=max(2, w))

# ---- Stroke 1: 撇 short (top-left area)
# starts near (140, 55), sweeps down-left to (105, 105)
s1 = [(142, 55), (130, 72), (118, 90), (105, 108)]
stroke_taper(s1, w_start=8, w_end=3)

# ---- Stroke 2: 横 short (upper horizontal, ~mid-upper)
# starts at ~(115, 108), ends at ~(210, 100). slight rise.
s2 = [(115, 110), (160, 106), (205, 102), (215, 101)]
stroke_taper(s2, w_start=6, w_end=8)  # slight end thickening

# ---- Stroke 3: 横 longer (middle horizontal, wider)
# from ~(65, 158) to ~(240, 152). Slight upward tilt.
s3 = [(60, 160), (110, 157), (170, 154), (240, 152)]
stroke_taper(s3, w_start=7, w_end=9)

# ---- Stroke 4: 撇 long — starts at top-center of hor2 (~155, 100), sweeps down-left curving
# passes through the horizontals, ends at (55, 265) with a flick
s4 = [
    (155, 100),
    (145, 130),
    (130, 165),
    (110, 205),
    (85, 240),
    (60, 265),
]
stroke_taper(s4, w_start=7, w_end=3)

# ---- Stroke 5: 捺 — starts near where 撇 crosses stroke 3 (~135, 165), sweeps down-right,
# widens toward the end, ends at (255, 275) with a flat tail.
s5 = [
    (140, 165),
    (165, 195),
    (195, 225),
    (225, 255),
    (255, 275),
]
stroke_taper(s5, w_start=5, w_end=10)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0197_矢/01_矢.png")
