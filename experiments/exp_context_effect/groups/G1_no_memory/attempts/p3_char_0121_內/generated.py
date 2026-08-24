"""Render 內 (inside) as 300x300 PNG using PIL.

Structure (4 strokes):
  1. 竖 (vertical) — left side of the outer frame
  2. 横折钩 (horizontal-turn-hook) — top + right + hook of the frame
  3. 撇 (left-falling) — inner 人, left leg
  4. 捺 (right-falling) — inner 人, right leg
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 4

# Outer frame — fill more of canvas to match GT scale
left_x = 55
right_x = 240
top_y = 40
bot_y = 265

# Stroke 1: 竖 — left vertical (slight left lean at bottom)
draw.line([(left_x + 5, top_y + 10), (left_x, bot_y)], fill=INK, width=LW)

# Stroke 2: 横折钩 — top horizontal, right vertical, small hook
# top horizontal (mild upward tilt as in handwriting)
draw.line([(left_x, top_y + 10), (right_x, top_y)], fill=INK, width=LW)
# right vertical
draw.line([(right_x, top_y), (right_x + 4, bot_y - 20)], fill=INK, width=LW)
# hook — small leftward/upward tick
draw.line([(right_x + 4, bot_y - 20), (right_x - 14, bot_y - 32)], fill=INK, width=LW)

# Inner 人 — centered inside the frame, larger and cleaner
# 撇 (left-falling): starts near top-center of interior, sweeps down-left, curved
# Draw as two segments to hint at curve
pie_top = (150, 95)
pie_mid = (128, 160)
pie_end = (85, 240)
draw.line([pie_top, pie_mid], fill=INK, width=LW)
draw.line([pie_mid, pie_end], fill=INK, width=LW)

# 捺 (right-falling): starts from pie mid area, sweeps down-right
na_start = (135, 145)
na_end = (215, 245)
draw.line([na_start, na_end], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0121_內/01_內.png")
print("saved")
