from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# 俞 layout:
# Top 人 (roof), a horizontal underneath, a small right tick,
# a short middle 一, then a 月-shape below: left 丿 curving out,
# right vertical with hook, two internal horizontal bars.

# --- Top roof 人 ---
# Left diagonal 丿
line([(150, 35), (70, 120)], width=5)
# Right diagonal 捺
line([(150, 35), (230, 120)], width=5)

# Horizontal closing under the roof (亼)
line([(78, 122), (222, 122)], width=5)

# Small right-side tick (inside roof, near right)
line([(190, 100), (210, 122)], width=4)

# --- Middle short 一 ---
line([(115, 150), (195, 150)], width=4)

# --- Bottom 月-like frame ---
# Left stroke: starts at top, curves down-left like 丿
line([(115, 155), (110, 200)], width=5)
line([(110, 200), (95, 245)], width=5)
line([(95, 245), (80, 275)], width=5)

# Right vertical with hook at bottom
line([(210, 155), (210, 265)], width=5)
line([(210, 265), (195, 273)], width=5)

# Top horizontal of the bottom box (connecting left+right)
line([(115, 155), (210, 155)], width=5)

# Two internal horizontal bars
line([(120, 195), (200, 195)], width=3)
line([(110, 235), (200, 235)], width=3)

out = os.path.join(os.path.dirname(__file__), "01_俞.png")
img.save(out)
print("wrote", out)
