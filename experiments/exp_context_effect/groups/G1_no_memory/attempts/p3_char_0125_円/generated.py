"""Render 円 (Japanese/simplified form of 圓, 'yen') to a 300x300 PNG.

4 strokes:
  1. left vertical: starts slightly up-right, sweeps down-left then down
  2. top-and-right: horizontal across top, then verticals down with small hook
  3. upper inner horizontal
  4. lower inner horizontal
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Frame bounds (roughly matching GT which sits centered-lower)
LEFT_X_TOP = 80
LEFT_X_BOT = 70
RIGHT_X = 215
TOP_Y = 75
BOT_Y = 260

# Stroke 1: left vertical (piě-like top, curves down)
# Starts slightly right of top-left, sweeps down-left, then straight down
draw.line([(95, 70), (LEFT_X_TOP, 95), (LEFT_X_BOT, BOT_Y)], fill=INK, width=LW)

# Stroke 2: top horizontal + right vertical + small hook (héng-zhé-gōu)
# Top horizontal
draw.line([(LEFT_X_TOP, 80), (RIGHT_X, 75)], fill=INK, width=LW)
# Right vertical down
draw.line([(RIGHT_X, 75), (RIGHT_X - 5, BOT_Y - 5)], fill=INK, width=LW)
# Small hook at bottom-right going left
draw.line([(RIGHT_X - 5, BOT_Y - 5), (RIGHT_X - 25, BOT_Y - 15)], fill=INK, width=LW)

# Stroke 3: middle horizontal (inner)
draw.line([(LEFT_X_TOP + 3, 165), (RIGHT_X - 8, 163)], fill=INK, width=LW)

# Stroke 4: bottom horizontal (closes the box)
draw.line([(LEFT_X_BOT, BOT_Y), (RIGHT_X - 20, BOT_Y - 10)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0125_円/01_円.png")
print("saved")
