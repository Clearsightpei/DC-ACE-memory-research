"""
佼 = 亻 (left, ~1/3 width) + 交 (right, ~2/3 width)
交 = 丶 (top-left dot) + 一 (horizontal) + 父-like (two dots + 撇 + 捺 crossing)

Layout:
- 亻: short 撇 top-left of left column, long 竖 dropping straight down
- 交 top: small 丶 top-left, then long 一 across top
- 交 middle: two small 点 (left-point 丶, right-point 丶) just below the 一
- 交 bottom: 撇 from upper-mid to lower-left + 捺 from upper-mid to lower-right (crossing X)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush(pts, width=6):
    # Dab-style smooth line
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

def curve(p0, p1, p2, width=6, steps=30):
    # Quadratic Bezier
    pts = []
    for i in range(steps+1):
        t = i/steps
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t*t * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t*t * p2[1]
        pts.append((x, y))
    brush(pts, width)

# ---- 亻 on left (occupies roughly x=40-95) ----
# 撇: slanted stroke that ends where 竖 begins
curve((90, 60), (78, 100), (55, 145), width=6)
# 竖: long vertical from top of 撇's mid down
brush([(85, 110), (85, 265)], width=7)

# ---- 交 on right (occupies roughly x=115-280) ----
# 丶 (top-left dot of 交)
curve((160, 45), (166, 55), (172, 68), width=8)

# 一 (horizontal across top of 交)
brush([(125, 100), (275, 95)], width=6)

# Two small dots below 一: left-point 丶 and right-point 丶 (small, close to 一)
curve((165, 115), (162, 128), (156, 140), width=7)
curve((235, 115), (240, 128), (246, 140), width=7)

# 撇 (long, crosses X — from just below 一 center-right sweeping to lower-left)
curve((215, 148), (170, 205), (120, 268), width=6)

# 捺 (long, from just below 一 center-left sweeping to lower-right)
curve((195, 148), (240, 205), (280, 268), width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0404_佼/01_佼.png")
print("saved")
