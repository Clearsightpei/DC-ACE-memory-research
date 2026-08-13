"""Render 条 (tiáo) — 7 strokes.
Top: 夂 (short pie, heng-pie, na); Bottom: 木 (heng, shu, pie, na).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

def curve(pts, width=4, steps=40):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
        d.line([prev, (x, y)], fill="black", width=width)
        prev = (x, y)

# ---- Top: 夂 (upper half y=30..150) ----
# 1) short pie (top small diagonal)
curve([(135, 40), (125, 55), (110, 75)], width=4)

# 2) heng-pie: short heng then bends into a long pie down-left
line([(115, 65), (195, 55)], width=4)
curve([(195, 55), (165, 100), (95, 155)], width=5)

# 3) na (starts inside the 夂, sweeps down-right)
curve([(155, 90), (185, 125), (215, 160)], width=5)

# ---- Bottom: 木 (lower half y=155..275) ----
# 4) heng (horizontal) — modest length
line([(65, 175), (235, 175)], width=4)

# 5) shu (vertical) through center
line([(150, 155), (150, 260)], width=5)

# 6) pie (from upper-center down-left)
curve([(150, 185), (115, 220), (75, 265)], width=5)

# 7) na (from upper-center down-right)
curve([(150, 185), (190, 225), (230, 270)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0333_条/01_条.png")
print("saved")
