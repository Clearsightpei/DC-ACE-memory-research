"""G1 no-memory render of 草 (grass)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 草 = 艹 (grass radical) on top + 早 (early) on bottom
# Grass radical 艹: horizontal bar + two verticals (a bit slanted inward)
# 早: 日 (rectangle with middle bar) + long horizontal + vertical descender

BLACK = (0, 0, 0)
TH = 5  # stroke thickness

def line(a, b, w=TH):
    d.line([a, b], fill=BLACK, width=w)

# --- 艹 grass radical (top) ---
# Long horizontal bar
line((55, 78), (245, 72), w=6)
# Left vertical (slight left-lean top, or vertical)
line((100, 55), (95, 105))
# Right vertical (mirror; slight lean)
line((195, 55), (205, 108))

# --- 早 (bottom) ---
# 日 rectangle: top slightly slanted downward, sides vertical, bottom horizontal
# Top-left corner (top of left side of 日)
tl = (105, 118)
tr = (200, 118)
bl = (105, 195)
br = (200, 195)
# Left vertical
line(tl, bl)
# Top horizontal (with right hook: this is 横折)
line(tl, tr)
# Right vertical from top-right down
line(tr, br)
# Middle horizontal (inside 日)
line((110, 158), (198, 156))
# Bottom horizontal of 日
line(bl, br)

# Long horizontal below 日 (十 top bar)
line((40, 225), (260, 222), w=6)

# Long central vertical (十 descender) starting from bottom of 日 downward
line((152, 195), (152, 285))

out = os.path.join(os.path.dirname(__file__), "01_草.png")
img.save(out)
print("wrote", out)
