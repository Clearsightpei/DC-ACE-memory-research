"""Render 士 (scholar radical) to a 300x300 PNG.

士 has 3 strokes:
  1. Long horizontal (top)
  2. Vertical (middle, from top to bottom)
  3. Short horizontal (bottom) -- shorter than the top one (this distinguishes 士 from 土)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 8

# Center reference
cx, cy = W // 2, H // 2

# Stroke 1: top long horizontal
top_y = 110
top_left = (cx - 80, top_y)
top_right = (cx + 80, top_y)
draw.line([top_left, top_right], fill=INK, width=STROKE)

# Stroke 2: vertical, from just above top horizontal to a bit below middle
vert_top = (cx, top_y - 15)
vert_bot = (cx, 215)
draw.line([vert_top, vert_bot], fill=INK, width=STROKE)

# Stroke 3: bottom horizontal, shorter than top
bot_y = 215
bot_left = (cx - 55, bot_y)
bot_right = (cx + 55, bot_y)
draw.line([bot_left, bot_right], fill=INK, width=STROKE)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_067_士/01_士.png")
