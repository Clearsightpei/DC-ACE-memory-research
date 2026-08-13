"""
她 — left-right compound: 女 (left) + 也 (right).

# SIGNATURE CHECK: hook family — every 钩 flicks UP-and-LEFT into
# the body, never down. Applies to 横折钩 terminal and 竖弯钩
# terminal in 也.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(x, y, r=3):
    d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def bez(pts, n=60, w=7):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = None
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        if prev is not None:
            d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)
    dab(x0, y0, w // 2)
    dab(x2, y2, w // 2)

def line(a, b, w=7):
    d.line([a, b], fill="black", width=w)
    dab(*a, r=w // 2)
    dab(*b, r=w // 2)

# ---- LEFT: 女  (x ~30..145, y ~85..250) ----
# Stroke 1: 撇点 — Z-like: goes down-left, then a slightly rising
# point stroke to the right (the 点 tail rises).
bez([(105, 95), (75, 155), (50, 200)], w=7)   # 撇 part
bez([(50, 200), (85, 205), (125, 195)], w=7)  # 点 part (rising slightly)

# Stroke 2: 撇 — long diagonal from near the top of area to lower-left.
bez([(120, 115), (85, 180), (35, 250)], w=7)

# Stroke 3: 横 — horizontal beam crossing through the middle-upper of 女.
line((30, 160), (150, 155), w=7)

# ---- RIGHT: 也  (x ~160..280, y ~110..250) ----

# Stroke 1: 竖 — leftmost short vertical (drawn first per stroke order?
# actually 也 order: 横折钩, 竖, 竖弯钩). Keep 横折钩 first.

# 横折钩: top horizontal, turn down, hook up-left.
line((175, 130), (260, 128), w=7)             # top 横
line((260, 128), (263, 235), w=7)             # 折 down
bez([(263, 235), (252, 232), (240, 222)], w=7)  # 钩 up-and-left

# Stroke 2: 竖 — inner middle vertical
line((215, 118), (218, 215), w=7)

# Stroke 3: 竖弯钩 — starts at left, goes down, curves right along the
# bottom, terminal hook flicks UP-and-LEFT.
bez([(180, 150), (176, 215), (205, 248)], w=7)
bez([(205, 248), (250, 252), (278, 240)], w=7)
bez([(278, 240), (273, 225), (265, 215)], w=7)  # 钩 up-and-left

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0263_她/01_她.png")
