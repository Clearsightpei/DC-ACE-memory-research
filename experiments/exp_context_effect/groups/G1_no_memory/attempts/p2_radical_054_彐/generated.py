"""G1 render of radical 彐 (3 strokes).

Stroke plan (looking at GT):
  1. 横折 (horizontal-turn-vertical hook): top horizontal from left to right,
     then turns down to form the right side.
  2. 横 (middle horizontal, shorter): from left, roughly to middle.
  3. 横 (bottom horizontal, long): from left across full width.

All three strokes share the same left edge (the left side of 彐 is open —
no vertical spine on the left, just three horizontal starts stacked).
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 7  # brush width

# Layout (based on GT PNG):
# The radical sits roughly in the upper-middle of the canvas.
# Top horizontal spans x ~ 55 to 215 at y ~ 95.
# Right vertical drops from (215, 95) down to (215, 235).
# Middle horizontal at y ~ 155, from x ~ 55 to x ~ 175.
# Bottom horizontal at y ~ 235, from x ~ 55 to x ~ 215.

LEFT_X = 55
RIGHT_X = 215
TOP_Y = 95
MID_Y = 158
BOT_Y = 235

# --- Stroke 1: 横折 (top horizontal + turn down to bottom-right corner) ---
# Horizontal portion
draw.line([(LEFT_X, TOP_Y), (RIGHT_X, TOP_Y)], fill=INK, width=LW)
# Vertical portion (slight lean, small hook feeling at bottom)
draw.line([(RIGHT_X, TOP_Y), (RIGHT_X - 5, BOT_Y)], fill=INK, width=LW)

# --- Stroke 2: middle short horizontal ---
draw.line([(LEFT_X, MID_Y), (RIGHT_X - 40, MID_Y)], fill=INK, width=LW)

# --- Stroke 3: bottom long horizontal ---
draw.line([(LEFT_X, BOT_Y), (RIGHT_X - 5, BOT_Y)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_彐.png")
img.save(out_path)
print(f"Wrote {out_path}")
