"""Render 疋 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# 疋 — 5 strokes (looking at GT):
# 1. Top horizontal 一 with small down-right tick at right end
# 2. Small vertical / left tick below top-right
# 3. Middle short horizontal 一 (short, right of center)
# 4. Long 撇 (left slanting) from mid-upper going down-left
# 5. Bottom horizontal-turn-捺 (from mid down then flat right)

# 1. Top horizontal with small hook at right
d.line([(70, 110), (215, 105)], fill=BLACK, width=LW)
d.line([(215, 105), (225, 125)], fill=BLACK, width=LW)

# 2. Short middle horizontal (like a small 一 in center-right)
d.line([(140, 160), (195, 158)], fill=BLACK, width=LW)

# 3. Small vertical connector on right side (down-left tick)
d.line([(195, 158), (185, 175)], fill=BLACK, width=LW)

# 4. Long 撇 - left slanting stroke from upper area going down-left
# starts near top-left, curves gently
points_pie = [(120, 125), (110, 165), (90, 215), (65, 260)]
d.line(points_pie, fill=BLACK, width=LW)

# 5. Bottom stroke - short vertical from mid down, then long flat 捺 to right
# starts around (135, 165), goes down curving to (155, 250), then flat right to (250, 260)
points_bot = [(135, 170), (135, 210), (150, 245), (180, 258), (220, 260), (255, 258)]
d.line(points_bot, fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_疋.png")
img.save(out)
print("wrote", out)
