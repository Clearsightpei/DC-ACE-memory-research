"""Render 别 at 300x300."""
import os
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
W = 4

def line(p1, p2, w=W):
    d.line([p1, p2], fill=BLACK, width=w)

def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=w)

# 别 = 另 (left) + 刂 (right)
# 另 = 口 (upper) + 力 (lower)

# --- 口 (small mouth, upper-left) ---
kx1, ky1, kx2, ky2 = 50, 70, 125, 120
line((kx1, ky1), (kx1, ky2))                     # left vertical
polyline([(kx1, ky1), (kx2, ky1), (kx2, ky2)])   # top + right vertical (横折)
line((kx1, ky2), (kx2, ky2))                     # bottom horizontal

# --- 力 (below 口, spans wider) ---
# horizontal-fold-hook: horizontal then vertical then small left hook
polyline([(35, 155), (165, 150), (155, 225), (140, 235)])
# 撇 stroke from near top-left of the fold, sweeping down-left
polyline([(90, 155), (60, 220), (35, 260)])

# --- 刂 (right side, knife radical) ---
# short left vertical (a bit shorter, upper portion)
line((205, 110), (205, 190))
# tall right vertical with hook (竖钩)
polyline([(255, 60), (255, 255), (238, 265)])

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_别.png")
img.save(out)
print(out)
