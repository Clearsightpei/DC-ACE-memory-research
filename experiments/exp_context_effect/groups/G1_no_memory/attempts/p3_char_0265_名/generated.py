"""Render 名 (name) to 300x300 PNG using PIL.
Structure: 夕 (top) + 口 (bottom).
Revised: enlarged 夕, repositioned 口 tucked under sweep.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p1, p2, w=5):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=5):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)

# === 夕 (top) ===
# Stroke 1: 撇 - long left-falling sweep from upper-mid to lower-left corner
poly([(180, 40), (160, 80), (130, 130), (90, 195), (50, 270)], w=6)

# Stroke 2: 横折钩 - short heng, turn down, small hook (forms 夕's box)
# heng starts on the 撇, goes right
poly([(155, 75), (215, 80)], w=5)
# turn down (折)
poly([(215, 80), (205, 145)], w=5)
# small hook up-left at end
poly([(205, 145), (170, 148), (160, 138)], w=5)

# Stroke 3: 点 (dot) inside 夕 - short slanted stroke
poly([(150, 108), (170, 125)], w=6)

# === 口 (bottom) ===
# Positioned mid-lower, slightly right; tucked beneath 夕's sweep
# Stroke 4: 竖 (left vertical)
line((110, 200), (110, 265), w=5)
# Stroke 5: 横折 (top horizontal + right vertical)
poly([(108, 200), (215, 200), (215, 265)], w=5)
# Stroke 6: 横 (bottom closing)
line((110, 265), (215, 265), w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_名.png"))
print("saved")
