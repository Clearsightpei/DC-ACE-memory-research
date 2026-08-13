"""Render 两 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4  # line width

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# 两 has 7 strokes:
# 1) Top horizontal (一) — short, upper-middle
# 2) Left vertical of outer frame (leans slightly, top-left down)
# 3) Long horizontal (top of the box structure)
# 4) Right vertical of outer frame (right side down, slight hook)
# 5) Inner-left: 人-like left stroke
# 6) Inner-right: 人-like right stroke
# 7) Small stroke — actually 两 = 一 on top, then 冂 box, then two 人 inside

# Layout box (main body of the character)
# Top small horizontal
line((110, 55), (185, 58), 4)

# Long horizontal (top of frame)
line((55, 95), (250, 92), 5)

# Left vertical (leans left slightly, curves)
# left slanted stroke going down-left
d.line([(75, 95), (55, 250)], fill="black", width=5)

# Right vertical (slight hook at bottom)
d.line([(240, 95), (240, 240)], fill="black", width=5)
# small hook to left at bottom of right vertical
d.line([(240, 240), (220, 250)], fill="black", width=5)

# Inner short vertical (middle divider top area) — actually 两 has an inner vertical
# The character has two "人" inside the 冂
# Middle vertical (drops from top horizontal down inside)
line((150, 95), (150, 200), 4)

# Left 人 inside: left curved stroke going down-left
d.line([(120, 130), (95, 220)], fill="black", width=4)
# Left 人 right stroke (short, going down-right)
d.line([(120, 130), (140, 195)], fill="black", width=4)

# Right 人 inside: left curved stroke going down-left
d.line([(200, 130), (175, 220)], fill="black", width=4)
# Right 人 right stroke going down-right
d.line([(200, 130), (225, 195)], fill="black", width=4)

out = os.path.join(os.path.dirname(__file__), "01_两.png")
img.save(out)
print("saved", out)
