"""Render 圆 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# Outer enclosure 囗 (traditional 3-stroke box: left vertical, top+right, bottom)
# Box roughly filling the character area, with slight opening at top-right (like GT)
L, R, T, B = 55, 245, 45, 260
# Stroke 1: left vertical
line(L, T, L, B, 5)
# Stroke 2: top horizontal + right vertical (single stroke 横折)
line(L, T, R, T, 5)
line(R, T, R, B, 5)
# Stroke 3: bottom horizontal (closes box)
line(L, B, R, B, 5)

# Inside: 员 = 口 (top small box) + 贝 body (口 + 八)
# --- 口 on top (taller, less wide) ---
kL, kR, kT, kB = 115, 185, 70, 125
line(kL, kT, kL, kB, 4)
line(kL, kT, kR, kT, 4)
line(kR, kT, kR, kB, 4)
line(kL, kB, kR, kB, 4)

# --- 贝 lower part: small 口 body + 八 legs ---
# Body 口
bL, bR, bT, bB = 105, 195, 135, 205
line(bL, bT, bL, bB, 4)
line(bL, bT, bR, bT, 4)
line(bR, bT, bR, bB, 4)
line(bL, bB, bR, bB, 4)
# Middle horizontal inside 贝 body
line(bL, 170, bR, 170, 3)

# 八 legs beneath 贝
line(130, bB, 105, 235, 4)   # left leg (ノ)
line(170, bB, 200, 235, 4)   # right leg (乀)

out = os.path.join(os.path.dirname(__file__), "01_圆.png")
img.save(out)
print("saved", out)
