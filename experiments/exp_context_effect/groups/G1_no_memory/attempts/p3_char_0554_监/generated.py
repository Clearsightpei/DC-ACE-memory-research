"""G1 render of 监 (jian) - supervise. 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# 监 = top (臣 + 卜-like right) + bottom (皿)
# Top-left: 臣 component (vertical bar + small horizontal marks) simplified
# Top-right: 卜 -- a slanted stroke plus a small dot / short stroke
# Bottom: 皿 (dish) - two verticals inside a rectangle with base

# --- Top-left cluster (臣-like, simplified) ---
# short slanted stroke (like left dot of top)
line(70, 80, 85, 105)
# vertical stroke
line(95, 75, 95, 135)
# small horizontal ticks
line(95, 95, 115, 92)
line(95, 115, 115, 115)
line(95, 135, 130, 135)

# --- Top-right cluster (卜-like) ---
# long descending slanted stroke
line(155, 65, 235, 130)
# short horizontal tick
line(200, 105, 235, 100)
# small dot / short stroke
line(180, 130, 195, 140)

# --- Bottom: 皿 (dish) ---
# Top horizontal (short) of 皿
# left vertical
line(70, 170, 60, 240)
# right vertical
line(230, 170, 240, 240)
# top of dish (short curve/line)
line(70, 170, 230, 170)
# two inner verticals
line(115, 175, 115, 235)
line(175, 175, 175, 235)
# bottom horizontal (extends wider - the long base)
line(45, 245, 265, 250)

out = os.path.join(os.path.dirname(__file__), "01_监.png")
img.save(out)
print("Saved", out)
