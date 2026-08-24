"""
p3_char_0319_听 — G2 free-form
听 = 口 (left, small, upper) + 斤 (right)
斤 strokes: 撇 (top diagonal), 一 (horizontal shoulder),
           短撇 (short flick down-left), 丨 (long vertical)
No sibling-risk row for 听.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)

def bezier(p0, p1, p2, w=LW, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    for a, b in zip(pts, pts[1:]):
        d.line([a, b], fill=BLACK, width=w)

# ---- 口 on left (small, upper-middle) ----
# box roughly x: 45..105, y: 130..190
kx0, ky0, kx1, ky1 = 45, 130, 105, 190
# 竖 (left)
line((kx0, ky0), (kx0, ky1))
# 横折 (top + right)
line((kx0, ky0), (kx1, ky0 + 2))
line((kx1, ky0 + 2), (kx1 + 3, ky1))
# 横 (bottom, slightly protruding)
line((kx0 - 2, ky1), (kx1 + 5, ky1))

# ---- 斤 on right ----
# occupies roughly x: 130..280, y: 55..275

# 撇 (top diagonal, from upper-right sweeping down-left) — top of 斤
bezier((250, 65), (200, 80), (140, 110), w=LW)

# 一 (horizontal shoulder), starting a bit right of the 撇 top
line((175, 105), (275, 92), w=LW)
# small right-hook down (subtle)
line((275, 92), (272, 108), w=LW)

# 短撇 (short flick starting just below shoulder, going down-left)
bezier((185, 115), (170, 175), (150, 235), w=LW)

# 丨 (long vertical down from right side of shoulder)
line((235, 100), (232, 285), w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0319_听/01_听.png")
print("saved")
