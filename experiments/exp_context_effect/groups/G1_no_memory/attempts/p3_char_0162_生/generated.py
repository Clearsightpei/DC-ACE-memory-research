"""Render 生 (shēng) as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
T = 4

# 生 — 5 strokes:
# 1. 撇 slanting from upper (around vertical top) down-left, ending near middle horizontal
# 2. 一 short top horizontal (crosses vertical high up)
# 3. 丨 long vertical (top just above top-hz, down through all horizontals)
# 4. 一 medium middle horizontal
# 5. 一 long bottom horizontal (widest)

# Stroke 3 first for reference: vertical center at x=160, top=75 bottom=240
# Stroke 1: 撇 — from top of vertical area, slanting down-left to middle-horizontal level
draw.line([(160, 80), (95, 180)], fill=BLACK, width=T)

# Stroke 2: 一 top horizontal — short, from just right of the slant crossing over to right side
draw.line([(125, 110), (210, 105)], fill=BLACK, width=T)

# Stroke 3: 丨 vertical — from just above top horizontal down to just above bottom horizontal
draw.line([(160, 78), (160, 240)], fill=BLACK, width=T)

# Stroke 4: 一 middle horizontal — medium width
draw.line([(100, 180), (220, 178)], fill=BLACK, width=T)

# Stroke 5: 一 bottom horizontal — longest, spans most of width
draw.line([(55, 248), (255, 245)], fill=BLACK, width=T)

out_path = os.path.join(os.path.dirname(__file__), "01_生.png")
img.save(out_path)
print(f"Saved: {out_path}")
