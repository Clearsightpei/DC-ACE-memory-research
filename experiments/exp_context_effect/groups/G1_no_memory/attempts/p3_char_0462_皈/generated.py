"""Render 皈 (bai + fan) to 01_皈.png at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ---------- Left component: 白 (bai) ----------
# Top ノ leading into 白
line([(95, 62), (65, 108)], width=4)
# 白 box: top, right vertical, left vertical, bottom
line([(65, 108), (135, 100)], width=4)   # top
line([(135, 100), (132, 235)], width=4)  # right vertical
line([(65, 108), (60, 240)], width=4)    # left vertical
line([(60, 240), (132, 235)], width=4)   # bottom
# two inner horizontals
line([(68, 148), (130, 143)], width=4)
line([(65, 190), (131, 185)], width=4)

# ---------- Right component: 反 (fan) ----------
# 厂: leading tick + top horizontal (goes far right/up), then long down-left sweep
# leading tick (small ノ before top horizontal)
line([(160, 92), (175, 78)], width=4)
# top horizontal of 厂 — goes right and up, ending high right
line([(170, 82), (270, 62)], width=4)
# long left-down sweep from left of top-horizontal down to bottom-left
line([(170, 82), (168, 130), (160, 180), (145, 235), (128, 280)], width=4)

# 又 inside 反:
# short horizontal-ish stroke (top of 又)
line([(190, 140), (240, 128)], width=4)
# left-down flick from that horizontal (small ノ of 又)
line([(215, 128), (185, 200)], width=4)
# long right-down sweep (捺) starting near top of 又, going bottom-right
line([(215, 138), (240, 190), (270, 245), (285, 275)], width=4)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_皈.png"))
print("saved", os.path.join(out_dir, "01_皈.png"))
