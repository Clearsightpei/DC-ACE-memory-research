"""Render 刁 (diao) — 2 strokes: 横折弯钩 + 提"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def line(pts, width=LW):
    draw.line(pts, fill=BLACK, width=width, joint="curve")

# Stroke 1: 横折弯钩 — horizontal top, turn down, curve, hook up-left
# Horizontal top (roughly y=80 from x=90 to x=220)
horiz = [(90, 85), (140, 78), (200, 78), (225, 82)]
line(horiz)
# Vertical/curving descent from (225,82) down to about (200, 245),
# curving slightly outward-right then inward
desc = [(225, 82), (232, 130), (230, 180), (215, 225), (200, 245)]
line(desc)
# Hook at the bottom (small upward-left flick)
hook = [(200, 245), (185, 235)]
line(hook)

# Stroke 2: 提 — rising diagonal across the middle
# from lower-left (60, 175) rising to upper-right (185, 140)
ti = [(60, 178), (110, 160), (160, 148), (188, 140)]
line(ti)

out = os.path.join(os.path.dirname(__file__), "01_刁.png")
img.save(out)
print("saved", out)
