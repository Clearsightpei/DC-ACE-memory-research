"""Render 纟 (silk radical) as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 5  # stroke width

def polyline(points, w=W):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill="black", width=w)

# 纟 (silk radical) — 3 strokes
# 1) upper 撇折 with a small loop/hook (looks like a curly 2 / small ㄥ with head)
# 2) middle 撇折 (larger ㄥ shape) below
# 3) bottom 提 (rising line going up-right)

# --- Stroke 1: upper 撇折 (small, with a slight top curl) ---
# Small down-left diagonal starting from upper right area,
# then hook back up-right creating a small ㄥ
polyline([
    (160, 65), (158, 75), (150, 85),        # small curl at top
    (140, 100), (132, 115), (128, 125),     # 撇 going down-left
    (145, 122), (162, 120)                  # 折 hooking right
])

# --- Stroke 2: middle 撇折 (larger ㄥ) ---
polyline([
    (158, 140), (148, 158), (135, 178),
    (122, 195), (115, 205),                 # 撇 going down-left, longer
    (140, 202), (168, 200)                  # 折 hooking right
])

# --- Stroke 3: bottom 提 (rising line) ---
polyline([
    (100, 245), (130, 236), (162, 226), (195, 218)
])

out_path = os.path.join(os.path.dirname(__file__), "01_纟.png")
img.save(out_path)
print(f"Wrote {out_path}")
