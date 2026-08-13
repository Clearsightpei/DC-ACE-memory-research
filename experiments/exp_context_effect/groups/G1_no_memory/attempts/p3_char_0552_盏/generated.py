"""G1 render of 盏 (zhǎn) — 戋 on top of 皿."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# ---- Top: 戋 ----
# Short top horizontal
line(110, 55, 190, 48)
# Long middle horizontal
line(85, 108, 210, 100)
# Left 撇 (descending slash) from middle horizontal's left
line(120, 95, 90, 150)
# Long 斜钩 (main diagonal): from upper right area, sweeping down to lower right, with hook
line(195, 55, 235, 180)
# hook curl at bottom of 斜钩 (leftward tick)
line(235, 180, 215, 175)
# Small dot / short stroke top-right of 斜钩
line(205, 45, 215, 60)
# secondary 撇 crossing (extra slash within 戋)
line(160, 70, 110, 165)

# ---- Bottom: 皿 ----
# Top horizontal
line(80, 195, 235, 195)
# Left vertical (slight outward tilt)
line(85, 195, 78, 258)
# Right vertical (slight outward tilt)
line(232, 195, 240, 258)
# Inner vertical left
line(130, 200, 128, 253)
# Inner vertical right
line(180, 200, 182, 253)
# Bottom horizontal (widest)
line(58, 262, 258, 262)

img.save(os.path.join(os.path.dirname(__file__), "01_盏.png"))
print("saved")
