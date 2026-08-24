"""
p3_char_0358_盯 = 目 (left) + 丁 (right).

# SIGNATURE CHECK: 丁 = 一 + straight 亅 (no top flick). Vertical hook flicks
# UP-and-slightly-LEFT at bottom (~-100° to -110°). 丁-component is right half.
# 目 = tall rectangle with 3 evenly-spaced horizontal bars inside (top, mid, bottom rungs).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 6  # brush width

def line(p1, p2, w=BW):
    d.line([p1, p2], fill=INK, width=w)

def hook_v(x, y_top, y_bot, w=BW, flick_len=14):
    # vertical stroke with terminal hook flicking up-and-left
    line((x, y_top), (x, y_bot), w=w)
    # flick from bottom up-and-left (~-110°)
    import math
    ang = math.radians(-110)
    fx = x + flick_len * math.cos(ang)
    fy = y_bot + flick_len * math.sin(ang)
    line((x, y_bot), (fx, fy), w=w)

# ---------- 目 on left ----------
# Bounding box for 目: x 55..135, y 60..250 (tall & narrow)
mx0, my0, mx1, my1 = 55, 60, 135, 250
# Left vertical (竖)
line((mx0, my0), (mx0, my1))
# Top horizontal + right-turn = 横折 (top and right side as one gesture)
line((mx0, my0), (mx1, my0))
line((mx1, my0), (mx1, my1))
# Bottom horizontal
line((mx0, my1), (mx1, my1))
# Three interior bars: at ~1/3, ~2/3, and the bottom already covers close.
# Standard 目 has 3 internal horizontals: at y ~ my0+50, my0+110, my0+170 (bottom).
# We already drew bottom. Add two middle bars.
inner_y1 = my0 + (my1 - my0) * 1 // 3   # ~123
inner_y2 = my0 + (my1 - my0) * 2 // 3   # ~186
line((mx0, inner_y1), (mx1, inner_y1))
line((mx0, inner_y2), (mx1, inner_y2))

# ---------- 丁 on right ----------
# 丁: top 一 stretches wide, vertical hook centered-ish descending.
# Right half of canvas: x 145..280, top y ~ 75
tx0, ty0, tx1 = 150, 78, 285
# Top horizontal 一
line((tx0, ty0), (tx1, ty0))
# Vertical hook 亅: from just under middle of top bar, going down, then hook up-left
vx = (tx0 + tx1) // 2 + 8   # slightly right of center to match GT
vy_top = ty0 + 2
vy_bot = 245
hook_v(vx, vy_top, vy_bot, flick_len=16)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0358_盯/01_盯.png")
