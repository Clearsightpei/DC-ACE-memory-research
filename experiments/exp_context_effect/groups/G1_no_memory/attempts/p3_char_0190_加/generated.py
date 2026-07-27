"""Render 加 (jiā) to a 300x300 PNG.
力 on the left + 口 on the right.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# --- Left component: 力 (2 strokes) ---
# Stroke 1: 横折钩 — short horizontal from upper-left, turns down, hooks left
# Horizontal top
d.line([(40, 70), (130, 60)], fill=INK, width=LW)
# Vertical turn coming down and curving left into a hook
# Approximate with a series of segments
d.line([(130, 60), (128, 130)], fill=INK, width=LW)
d.line([(128, 130), (110, 175)], fill=INK, width=LW)
# hook
d.line([(110, 175), (90, 180)], fill=INK, width=LW)

# Stroke 2: 撇 — long left-falling from top area down through and past bottom-left
d.line([(95, 55), (75, 130)], fill=INK, width=LW)
d.line([(75, 130), (55, 200)], fill=INK, width=LW)
d.line([(55, 200), (35, 260)], fill=INK, width=LW)

# --- Right component: 口 (3 strokes, forming a rectangle) ---
# Positioned to the right, roughly middle-lower
box_left, box_top = 170, 130
box_right, box_bottom = 265, 220

# Stroke 1: 竖 (left vertical)
d.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=LW)
# Stroke 2: 横折 (top horizontal then right vertical)
d.line([(box_left, box_top), (box_right, box_top - 2)], fill=INK, width=LW)
d.line([(box_right, box_top - 2), (box_right + 2, box_bottom)], fill=INK, width=LW)
# Stroke 3: 横 (bottom horizontal)
d.line([(box_left - 3, box_bottom), (box_right + 5, box_bottom - 2)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_加.png")
img.save(out)
print(f"wrote {out}")
