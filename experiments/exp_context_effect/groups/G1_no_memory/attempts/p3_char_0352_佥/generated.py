"""G1 render for 佥 (qiān)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# 人 top: two diagonals meeting at apex ~ (150, 55)
apex = (150, 55)
# left diagonal (撇) — from apex down-left
left_pen = [apex, (120, 90), (85, 130), (55, 170)]
stroke(left_pen, width=6)
# right diagonal (捺) — from apex down-right
right_pen = [apex, (180, 90), (215, 130), (250, 165)]
stroke(right_pen, width=6)

# 一 horizontal under 人 apex, short
stroke([(115, 120), (185, 122)], width=6)

# Two small inner strokes (like 从 miniature) below the horizontal
# left small 撇
stroke([(130, 160), (115, 200)], width=5)
# right small 捺 / dot
stroke([(155, 165), (175, 205)], width=5)

# Bottom 一 — long horizontal at the base
stroke([(70, 245), (240, 248)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佥.png"))
print("wrote 01_佥.png")
