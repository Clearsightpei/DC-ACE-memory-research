"""Render 宀 (roof radical) using PIL at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# 宀 has 3 strokes:
# 1) 点 (dot) on top-center
# 2) 点/short-left stroke on left
# 3) 横钩 (horizontal + hook down at right end)

# Stroke 1: top dot (short diagonal, upper-left to lower-right)
draw.line([(150, 75), (170, 105)], fill=INK, width=LW)

# Stroke 2: left short dot/tick — starts above horizontal, crosses down-left below it
draw.line([(88, 115), (68, 195)], fill=INK, width=LW)

# Stroke 3: horizontal stroke starting at left, going right, then hook down at end
# horizontal part (slight slant down then up? keep near flat, slight rise)
draw.line([(78, 145), (230, 138)], fill=INK, width=LW)
# hook down-left at right end
draw.line([(230, 138), (215, 185)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_宀.png")
img.save(out_path)
print(f"Saved {out_path}")
