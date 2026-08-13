"""Render 畛 (田 + 㐱) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=4):
    d.line([p1, p2], fill="black", width=w)

# ---- LEFT: 田 (x 35..130, y 105..215) ----
L, R = 35, 130
T, B = 105, 215
# top
line((L, T), (R, T))
# left vertical
line((L, T), (L, B))
# bottom
line((L, B), (R, B))
# right vertical (slight overhang)
line((R, T - 2), (R, B + 6))
# inner cross
midx = (L + R) // 2
midy = (T + B) // 2
line((midx, T), (midx, B))
line((L, midy), (R, midy))

# ---- RIGHT: 㐱 ----
# 人 (top wide inverted-V): apex ~ (200, 60)
apex = (205, 55)
line(apex, (145, 130), w=4)          # 撇 (left)
line(apex, (290, 150), w=4)          # 捺 (right, long)

# three parallel 撇 slants (down-left) beneath, staggered
# top slant
line((210, 130), (170, 175), w=4)
# middle slant
line((235, 155), (195, 205), w=4)
# bottom slant (longer)
line((260, 180), (215, 245), w=4)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畛.png")
img.save(out)
print(f"wrote {out}")
