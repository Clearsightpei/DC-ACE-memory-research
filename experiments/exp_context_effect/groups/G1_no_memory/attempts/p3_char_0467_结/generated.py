"""Draw 结 (jie) — left: 纟 silk radical, right: 吉 (士 over 口)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# ============ LEFT: 纟 (silk radical) ============
# Upper 撇折 — diagonal down-left then hook right (like a "<")
line([(80, 75), (60, 95), (85, 105)], w=LW)
# Middle 撇折
line([(75, 115), (55, 135), (85, 145)], w=LW)
# Bottom 提 stroke (long rising diagonal)
line([(40, 210), (105, 175)], w=LW)

# ============ RIGHT: 吉 (士 over 口) ============
# --- 士 on top ---
# Top horizontal (long) — 士 has top wider than bottom
line([(140, 80), (255, 80)], w=LW)
# Vertical (through both horizontals)
line([(198, 80), (198, 150)], w=LW)
# Bottom horizontal (short)
line([(165, 150), (232, 150)], w=LW)

# --- 口 on bottom ---
# Left vertical
line([(155, 175), (155, 245)], w=LW)
# Top + right vertical (横折)
line([(155, 175), (240, 175), (240, 245)], w=LW)
# Bottom horizontal (closing)
line([(155, 245), (240, 245)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_结.png")
img.save(out)
print("saved:", out)
