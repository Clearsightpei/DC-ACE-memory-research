"""G1 render for 放 (p3_char_0403). Revised."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# 放 = 方 (left, ~x 30-140) + 攵 (right, ~x 150-280)
# Character body roughly y=50..270

# ============ LEFT: 方 ============
# 1. top dot (点) — short slash upper area
stroke([(70, 60), (85, 78)], width=4)

# 2. horizontal (一) across upper part
stroke([(35, 100), (135, 98)], width=4)

# 3. left leaning stroke (丿) from just under heng, curving down-left
stroke([(78, 105), (60, 175), (35, 260)], width=4)

# 4. inner 横折钩 — box: horizontal top, vertical down, hook left
stroke([(72, 140), (128, 138), (122, 200), (95, 205)], width=4)

# ============ RIGHT: 攵 ============
# 1. short pie top (short diagonal)
stroke([(200, 60), (185, 88)], width=4)

# 2. horizontal short (一)
stroke([(170, 108), (235, 105)], width=4)

# 3. long pie (丿) — main diagonal from upper-mid right down to lower-left
stroke([(215, 90), (185, 160), (155, 230), (140, 270)], width=4)

# 4. 捺 (na) — diagonal down-right from mid area
stroke([(190, 155), (225, 205), (275, 265)], width=4)

out = os.path.join(os.path.dirname(__file__), "01_放.png")
img.save(out)
print("wrote", out)
