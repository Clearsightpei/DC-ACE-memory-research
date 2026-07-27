"""Render 匕 to 300x300 PNG using PIL.

匕 = 2 strokes:
  1. 撇 (piě) — slanted stroke from upper-right down to lower-left, crossing the vertical
  2. 竖弯钩 (shù wān gōu) — starts top with short horizontal-into-vertical,
     goes down, curves right along bottom, ends with small upward hook
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Stroke 2 first (背景骨架): 竖弯钩
# Top small horizontal segment going right
top_h_start = (175, 108)
top_h_end   = (222, 105)
draw.line([top_h_start, top_h_end], fill=INK, width=LW)

# Vertical descent — slightly leaning left at bottom, from top_h_start
desc_pts = [(175, 108), (170, 150), (165, 195), (172, 235)]
draw.line(desc_pts, fill=INK, width=LW)

# Bottom curve right
bot_pts = [(172, 235), (200, 250), (240, 252), (252, 245)]
draw.line(bot_pts, fill=INK, width=LW)

# Upward hook at end
draw.line([(252, 245), (253, 218)], fill=INK, width=LW)

# Stroke 1: 撇 — slanted from upper right through the middle down to lower left,
# crossing the vertical stroke. Starts around (150, 95), ends around (105, 175).
pie_pts = [(152, 92), (135, 130), (118, 160), (100, 180)]
draw.line(pie_pts, fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_匕.png")
img.save(out_path)
print(f"Saved {out_path}")
