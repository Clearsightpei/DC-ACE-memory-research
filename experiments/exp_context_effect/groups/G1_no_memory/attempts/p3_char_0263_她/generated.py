"""Render 她 (she) to a 300x300 PNG. Revised for cleaner shape."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

def curve(pts, width=LW, steps=60):
    (x0, y0), (cx, cy), (x1, y1) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
        d.line([prev, (x, y)], fill=BLACK, width=width)
        prev = (x, y)

# =========================================================
# Left component: 女 (roughly x=25..145, y=85..235)
# 3 strokes: 撇点, 撇, 一(横)
# =========================================================

# Stroke 1: 撇点 — curved diagonal down-left, then a dot going down-right
#   The pie starts near top-center-left, sweeps down-left to lower area,
#   then a small dot/dash to lower-right.
curve([(100, 90), (75, 150), (55, 200)], width=LW)     # pie down-left
curve([(55, 200), (75, 210), (95, 220)], width=LW)     # dian (dot/short) down-right

# Stroke 2: 撇 — from upper-right area, long diagonal to lower-left
curve([(135, 130), (85, 190), (30, 235)], width=LW)

# Stroke 3: 一 (横) — horizontal across the middle
line([(22, 175), (150, 168)], width=LW)

# =========================================================
# Right component: 也 (roughly x=160..280, y=110..245)
# 3 strokes: 横折钩, 竖, 竖弯钩
# =========================================================

# Stroke 1: 横折 (small horizontal, then bend down; part of 也's top-left corner)
line([(170, 130), (175, 205)], width=LW)  # vertical drop on left

# Stroke 2: 竖 in middle — starts near top, goes down through center
line([(215, 115), (213, 225)], width=LW)

# Stroke 3: 横折钩 — top horizontal, then right side going down with hook
line([(180, 135), (270, 128)], width=LW)   # top horizontal
curve([(270, 128), (272, 180), (260, 240)], width=LW)  # right side down curve

# Stroke 4 (visual): the 竖弯钩 sweeping bottom of 也
curve([(175, 205), (185, 245), (255, 248)], width=LW)  # bottom sweep
curve([(255, 248), (272, 245), (275, 220)], width=LW)  # hook up

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_她.png"))
print("saved", os.path.join(out_dir, "01_她.png"))
