"""Render 仑 to 01_仑.png using PIL.
Structure (matching GT more closely):
  - Top: 人-shape roof — wider spread, apex slightly lower, curved 撇
  - Bottom: 匕 — short 撇 on the left, a short horizontal, and a 竖弯钩
    with a clear flat bottom sweeping right and small upturn.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=5):
    d.line(points, fill="black", width=width, joint="curve")

# --- Top: 人 roof (wider, curved) ---
# 撇 - curving from upper-center to lower-left, wider spread
pie_pts = [
    (150, 40),
    (138, 65),
    (120, 100),
    (95, 140),
    (65, 180),
    (45, 215),
]
stroke(pie_pts, width=5)

# 捺 - from apex going down-right, wider spread with heavier tail
na_pts = [
    (152, 50),
    (170, 80),
    (195, 120),
    (225, 165),
    (255, 210),
]
stroke(na_pts, width=6)

# --- Bottom: 匕 ---
# Short 撇 on the upper-left of the bottom part
short_pie = [
    (128, 165),
    (120, 190),
    (110, 215),
]
stroke(short_pie, width=5)

# Short horizontal stroke crossing the short pie
stroke([(125, 195), (175, 190)], width=5)

# 竖弯钩: vertical down, curves right along the bottom, small upturn hook at end
hook_pts = [
    (160, 165),
    (158, 195),
    (156, 225),
    (160, 250),
    (175, 262),
    (200, 265),
    (225, 262),
    (240, 255),
    (245, 245),
]
stroke(hook_pts, width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_仑.png")
img.save(out_path)
print(f"Saved {out_path}")
