"""Render 北 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
INK = "black"
LW = 5

# 北 has 5 strokes:
# Left side: 横 (short horizontal), 竖 (vertical), 提 (rising)
# Right side: 撇 (short slanting down-left) + 竖弯钩 (vertical bending right with hook)

# --- Left component ---
# short horizontal (upper-left)
draw.line([(50, 115), (135, 108)], fill=INK, width=LW)

# vertical, from top of the horizontal down through bottom
draw.line([(90, 75), (90, 230)], fill=INK, width=LW)

# rising 提 at bottom-left
draw.line([(55, 215), (135, 180)], fill=INK, width=LW)

# --- Right component (匕-like) ---
# 撇 — short slanting stroke, upper right going down-left inside right cell
draw.line([(155, 130), (200, 175)], fill=INK, width=LW)

# 竖弯钩 — starts near top-right, comes down, curves right at bottom, small hook up
# top vertical portion
draw.line([(215, 90), (215, 220)], fill=INK, width=LW)
# curve/turn bottom-right
draw.line([(215, 220), (245, 245)], fill=INK, width=LW)
draw.line([(245, 245), (265, 240)], fill=INK, width=LW)
# small hook upward
draw.line([(265, 240), (263, 225)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_北.png")
img.save(out)
print("wrote", out)
