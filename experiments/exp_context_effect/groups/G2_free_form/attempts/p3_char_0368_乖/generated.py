"""Render 乖 (guai) using PIL to 300x300 PNG.

Structure of 乖 (8 strokes):
  1. short 撇 (upper-left slant, near top)
  2. long 一 (horizontal near top, crosses the 撇)
  3. long 丨 (central vertical, runs from top through bottom)
  4. small 横折 on left (upper) - small hook
  5. small 一 on left (lower)
  6. small 一 on right (upper) with small down-tick
  7. right 竖弯 (curving down and right, then up-flick)
Layout: 千-like top, then 北-like body flanking the central 丨.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
BW = 6  # brush width


def line(p0, p1, w=BW):
    d.line([p0, p1], fill=BLACK, width=w)


def poly(pts, w=BW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=w)


# ---- 1. short 撇 near top (angled slant, upper-right of vertical) ----
poly([(190, 50), (150, 78)], w=BW)

# ---- 2. long horizontal near top ----
line((55, 92), (245, 88), w=BW)

# ---- 3. long central vertical (runs top-through-bottom) ----
line((150, 65), (150, 278), w=BW + 1)

# ---- 4. left upper: horizontal tick with small down-flick on right end ----
poly([(50, 148), (100, 145), (100, 165)], w=BW)

# ---- 5. left lower: same shape, lower position ----
poly([(50, 210), (100, 207), (100, 227)], w=BW)

# ---- 6. right upper: short horizontal ----
line((175, 148), (245, 142), w=BW)

# ---- 7. right: 匕-like shape (slanted stroke from mid-upper-right,
#         going down-left, then hook right-up)
poly([(210, 155), (200, 210), (215, 250), (255, 245)], w=BW)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0368_乖/01_乖.png"
)
