"""Render 听 (tīng) — mouth radical 口 on left, 斤 on right."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=3):
    d.line(pts, fill="black", width=width)

# ---- 口 (left side, small, upper-mid area) ----
# stroke 1: left vertical
line([(50, 115), (55, 175)], 3)
# stroke 2: top+right (横折)
line([(50, 115), (100, 112)], 3)
line([(100, 112), (98, 172)], 3)
# stroke 3: bottom close
line([(55, 175), (98, 172)], 3)

# ---- 斤 (right side) ----
# Stroke 1: 短撇 — top-left tick sweeping down-left
line([(160, 65), (135, 110)], 3)
# Stroke 2: top horizontal — connects from the 撇 endpoint area, going right
line([(135, 105), (240, 85)], 3)
# Stroke 3: long 撇 — starts near top-left inside, sweeps down-left to bottom
line([(170, 110), (125, 275)], 3)
# Stroke 4: short middle horizontal tick
line([(165, 155), (230, 145)], 3)
# Stroke 5: long vertical right leg
line([(225, 145), (222, 285)], 3)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_听.png"))
print("wrote 01_听.png")
