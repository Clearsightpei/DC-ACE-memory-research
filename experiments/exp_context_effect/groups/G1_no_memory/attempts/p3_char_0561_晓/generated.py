"""G1 render of 晓 (xiao) — 日 + 尧 (revision)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 3

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)

# ---------- LEFT: 日 ----------
lx0, ly0 = 55, 110
lx1, ly1 = 110, 215
# top
line((lx0, ly0), (lx1, ly0))
# left vertical
line((lx0, ly0), (lx0, ly1))
# right vertical (with slight downward hook at bottom)
line((lx1, ly0), (lx1, ly1))
# bottom
line((lx0, ly1), (lx1, ly1))
# middle horizontal
mid_y = (ly0 + ly1) // 2
line((lx0 + 2, mid_y), (lx1 - 2, mid_y))

# ---------- RIGHT: 尧 ----------
# Top row: two small strokes and a horizontal below them (looks like 戈-simplified)
# small vertical dot-stroke
line((165, 55), (163, 80))
# rising slanted stroke to right
poly([(175, 75), (200, 65), (225, 55)])

# First horizontal (below top strokes)
line((145, 100), (230, 95))

# A slanting piece on the right connecting first-horizontal to middle-horizontal
poly([(215, 100), (200, 120), (185, 140)])

# Middle horizontal (longer)
line((140, 155), (240, 150))

# Bottom 儿 (legs)
# Top short horizontal above the legs (top of 儿)
line((155, 195), (235, 190))
# Left leg (curve slightly)
poly([(165, 195), (155, 230), (145, 265)])
# Right leg with hook (竖弯钩)
poly([(220, 195), (222, 235), (235, 260), (260, 262), (272, 250)])

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_晓.png")
img.save(out)
print("wrote", out)
