"""Render 卬 (character) to a 300x300 PNG with PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

# 卬 = left ㄏ-like + right 卩. 4 strokes.

# --- LEFT COMPONENT (like inverted 卩 / ㄏ shape) ---
# Stroke 1: short piě at top (slanting down-right)
d.line([(75, 90), (125, 105)], fill=INK, width=LW)

# Stroke 2: vertical going down then bending down-right (the long left stroke)
d.line([(100, 100), (100, 175)], fill=INK, width=LW)
d.line([(100, 175), (145, 235)], fill=INK, width=LW)

# --- RIGHT COMPONENT 卩 ---
# Stroke 3: top-horizontal + right-vertical + small inner hook (橫折鉤)
d.line([(160, 95), (200, 100)], fill=INK, width=LW)   # top horizontal
d.line([(200, 100), (200, 170)], fill=INK, width=LW)  # vertical down
d.line([(200, 170), (185, 175)], fill=INK, width=LW)  # small hook to the left

# Stroke 4: long descending stroke (shù) — starts near top-center of right side, goes straight down past baseline
d.line([(170, 100), (170, 270)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_卬.png")
img.save(out_path)
print(f"Wrote {out_path}")
