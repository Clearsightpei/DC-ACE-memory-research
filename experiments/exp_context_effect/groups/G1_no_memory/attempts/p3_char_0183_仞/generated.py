"""Render 仞 to a 300x300 PNG using PIL.
仞 = 亻 (person radical, left) + 刃 (blade, right).
亻: 撇 (upper diagonal) + 竖 (vertical descending from midpoint of 撇)
刃: 丿 (long left-sweeping curve) + 横折钩 (top horizontal → down → hook) + 丶 (dot inside)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 4

def curve(points, width=LW):
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=INK, width=width)

# ================= 亻 (LEFT) =================
# 撇 — starts upper, curves down-left. Top around (75, 85) sweeping to (45, 200)
pie1 = [(78, 85), (72, 115), (63, 150), (54, 185), (45, 215)]
curve(pie1)

# 竖 — from midpoint of 撇 straight down to bottom
curve([(70, 128), (72, 260)])

# ================= 刃 (RIGHT) =================
# 丿 — the long left-sweeping stroke that forms the outer left of 刃 shape.
# Starts near top-middle (135, 70), sweeps down-left to (95, 245).
pie2 = [(140, 70), (135, 100), (125, 135), (115, 170), (105, 205), (95, 245)]
curve(pie2)

# 横折钩 — starts at (140, 78) top, horizontal to (235, 72),
# then bends down and slightly left to about (200, 235),
# then a hook up-left flick.
# Horizontal
curve([(140, 78), (170, 76), (200, 74), (235, 72)])
# Down-slanting fold (折)
curve([(235, 72), (232, 110), (225, 150), (215, 190), (205, 225)])
# Hook (钩) at bottom — small flick up-left
curve([(205, 225), (188, 218), (180, 210)])

# 丶 — dot inside the enclosure
curve([(165, 145), (178, 160), (172, 170)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_仞.png")
img.save(out_path)
print(f"Wrote {out_path}")
