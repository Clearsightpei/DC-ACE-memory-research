"""G1 render of 疟 (character p3_char_0380).
疒 radical (top dot, second dot on left, horizontal, sweeping 撇)
+ inner 匚-shape with middle horizontal.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# --- 疒 radical ---
# Top dot (small stroke, upper area, slanted)
line([(140, 40), (155, 55)], w=LW)

# Top horizontal (long, slightly angled down-right)
line([(75, 85), (215, 78)], w=LW)

# Left dot (small stroke on upper-left, going down-right)
line([(90, 110), (110, 135)], w=LW)

# Long left-falling 撇 (sweeping from horizontal down to lower-left)
line([(105, 85), (85, 150), (55, 220), (40, 270)], w=LW)

# --- Inner component (匚 with middle bar) ---
# Top horizontal inside
line([(130, 140), (230, 138)], w=LW)

# Right vertical (short down)
line([(228, 138), (228, 210)], w=LW)

# Middle horizontal
line([(135, 180), (225, 178)], w=LW)

# Bottom long horizontal (extends beyond inner box)
line([(95, 240), (245, 235)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_疟.png")
img.save(out)
print("wrote", out)
