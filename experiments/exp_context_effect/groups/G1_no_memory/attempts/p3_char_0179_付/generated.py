"""Render 付 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 5  # stroke thickness


def line(p1, p2, w=T):
    draw.line([p1, p2], fill=INK, width=w)


def curve(points, w=T):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], w)


# 付 = 亻 (left) + 寸 (right)

# --- Left radical 亻 ---
# Stroke 1: 撇 (pie) - diagonal from upper area sweeping down-left
curve([(100, 65), (90, 100), (78, 140), (60, 200)], w=T)

# Stroke 2: 竖 (shu) - vertical starts where the 撇 bends (about y=130)
line((92, 130), (92, 265), w=T)

# --- Right side 寸 ---
# Stroke 3: 横 (heng) - horizontal across upper-mid, slight rise
line((135, 130), (265, 128), w=T)

# Stroke 4: 竖钩 (shu-gou) - long vertical with small hook at bottom-left
curve([(198, 90), (198, 235), (192, 250), (178, 253), (165, 248)], w=T)

# Stroke 5: 点 (dian) - short diagonal stroke to lower-left of vertical (mid area)
curve([(150, 170), (162, 178), (172, 188)], w=T + 1)

out_path = os.path.join(os.path.dirname(__file__), "01_付.png")
img.save(out_path)
print(f"Saved {out_path}")
