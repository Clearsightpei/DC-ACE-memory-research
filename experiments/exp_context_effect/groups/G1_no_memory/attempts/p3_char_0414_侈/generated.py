"""Render 侈 (chǐ) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# === Left: 亻 (person radical) ===
# 撇 (diagonal top-right to lower-left)
stroke([(105, 80), (95, 110), (80, 155), (68, 200)], width=5)
# 竖 (vertical) — meets pie about 1/3 from top
stroke([(95, 130), (95, 275)], width=5)

# === Right: 多 (upper 夕 + lower 夕, offset) ===
# --- Upper 夕 ---
# 撇 (top diagonal, short)
stroke([(180, 55), (160, 90), (145, 115)], width=5)
# 横折钩 (curved rectangle-ish hook)
stroke([(150, 88), (180, 92), (210, 100),
        (208, 125), (200, 145),
        (180, 152), (158, 152)], width=5)
# 点 inside
stroke([(178, 122), (195, 135)], width=4)

# --- Lower 夕 (bigger, offset down-right) ---
# 撇 — the long defining stroke
stroke([(200, 150), (180, 190), (155, 225), (135, 260)], width=5)
# 横折钩 (larger)
stroke([(170, 178), (210, 185), (245, 195),
        (240, 220), (228, 245),
        (200, 258), (170, 260)], width=5)
# 点
stroke([(200, 220), (218, 232)], width=4)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_侈.png"))
print("saved")
