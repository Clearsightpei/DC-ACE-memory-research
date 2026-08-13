"""G1 render of 物 (character p3_char_0385)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=w)

# ---------- LEFT: 牜 (radical form of 牛) ----------
# 1. short 撇 top-left
curve([(72, 55), (55, 90), (48, 105)])
# 2. short 横 upper (crossing near top of vertical)
line(55, 108, 118, 100)
# 3. 提 / short right-up stroke off vertical
curve([(90, 155), (128, 140)])
# 4. main 竖 vertical (tall)
line(92, 70, 92, 275)
# 5. lower 横 (longer, crosses vertical lower down)
line(45, 165, 120, 158)

# ---------- RIGHT: 勿 ----------
# 1. left 撇 (short slant top-left of 勿)
curve([(165, 75), (150, 100), (142, 118)])
# 2. horizontal-fold-hook (横折钩) — top horizontal then down-curve
line(158, 100, 250, 92)
curve([(250, 92), (255, 120), (250, 155), (232, 195), (200, 225), (180, 235)])
# small hook tip
curve([(180, 235), (192, 225)])
# 3. inner 撇 (middle slanted line)
curve([(185, 135), (162, 195)])
# 4. inner 撇 (right slanted line)
curve([(220, 140), (195, 210)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_物.png"))
print("wrote 01_物.png")
