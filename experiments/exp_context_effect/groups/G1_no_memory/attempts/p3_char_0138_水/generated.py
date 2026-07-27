"""Render 水 (water) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Character 水 has 4 strokes:
# 1) Vertical stroke in center with a small hook at the bottom (竖钩)
# 2) Left side: short horizontal-then-diagonal descending stroke (横撇)
# 3) Left downstroke (撇) below the horizontal-撇
# 4) Right side: short diagonal (撇) at top-right + long diagonal (捺) to lower right

cx, cy = 150, 150

# --- Stroke 1: 竖钩 (vertical with hook) - center vertical ---
# top of vertical near y=55, bottom around y=245, then small hook toward upper-left
draw.line([(cx, 55), (cx, 240)], fill=INK, width=LW)
# hook at bottom
draw.line([(cx, 240), (cx - 18, 225)], fill=INK, width=LW)

# --- Stroke 2: 横撇 on left (short horizontal then descending curve) ---
# short near-horizontal segment then a long 撇 down-left
draw.line([(90, 135), (cx - 10, 140)], fill=INK, width=LW)  # short horizontal
draw.line([(cx - 10, 140), (55, 215)], fill=INK, width=LW)  # 撇 descending to lower-left

# --- Stroke 3: 撇 (short left downstroke) starting from lower-center ---
draw.line([(cx - 12, 178), (85, 240)], fill=INK, width=LW)

# --- Stroke 4a: short 撇 top-right — diagonal from upper-right down-left toward center vertical ---
draw.line([(200, 135), (cx + 8, 168)], fill=INK, width=LW)

# --- Stroke 4b: 捺 - long diagonal from near center going to lower-right ---
draw.line([(cx + 8, 168), (245, 240)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_水.png")
img.save(out_path)
print(f"Wrote {out_path}")
