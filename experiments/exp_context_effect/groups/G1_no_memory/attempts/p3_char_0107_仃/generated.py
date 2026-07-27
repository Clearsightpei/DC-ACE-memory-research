"""Render 仃 (character) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# 仃 = 亻 (person radical) + 丁 (right side)
# --- 亻 ---
# Stroke 1: 撇 (left-falling slant), from upper-mid down-left
draw.line([(90, 85), (45, 215)], fill=INK, width=LW)
# Stroke 2: 竖 (vertical), touches the 撇 near its middle, drops straight
draw.line([(78, 145), (80, 275)], fill=INK, width=LW)

# --- 丁 (right side) ---
# Stroke 3: 横 (horizontal top bar)
draw.line([(115, 130), (265, 128)], fill=INK, width=LW)
# Stroke 4: 竖钩 (vertical with small left hook at bottom)
draw.line([(195, 130), (198, 260)], fill=INK, width=LW)
# hook (short flick to lower-left)
draw.line([(198, 260), (170, 245)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_仃.png")
img.save(out_path)
print(f"Saved {out_path}")
