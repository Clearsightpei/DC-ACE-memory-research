# 立 (li) — 5 strokes, thin uniform ink per GT
# 1) top dot (short 丶 slanting down-right)
# 2) short 横 below the top dot
# 3) left small 点 (下-左点)
# 4) right small 撇 (下-右撇)
# 5) long bottom 横 (baseline)
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
THIN = 4  # GT is thin uniform

def line(x0, y0, x1, y1, w=THIN):
    d.line([(x0, y0), (x1, y1)], fill=INK, width=w)

# 1) Top dot — small stroke slanting down-right, centered horizontally
line(148, 55, 168, 78, w=5)

# 2) Short upper 横 — sits under the dot, roughly middle band
line(100, 128, 205, 132, w=4)

# 3) Left small stroke — short 点 slanting down-left
line(115, 158, 100, 185, w=5)

# 4) Right small stroke — short 撇 slanting down-right (mirrors #3)
line(190, 158, 205, 185, w=5)

# 5) Long bottom 横 — full-width baseline
line(55, 235, 250, 238, w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_立.png"))
