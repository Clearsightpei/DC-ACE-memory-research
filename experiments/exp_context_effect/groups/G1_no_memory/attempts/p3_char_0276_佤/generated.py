"""Render 佤 (person + tile) at 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ===== Left: 亻 (person radical) =====
# Stroke 1: 撇 — diagonal from upper area down-left
line([(90, 70), (55, 210)], width=7)
# Stroke 2: 竖 — vertical
line([(78, 140), (78, 270)], width=7)

# ===== Right: 瓦 (tile) =====
# Positioned x=125..270, y=70..270

# Stroke 1: 横 — top horizontal, gentle rise
line([(140, 95), (240, 85)], width=7)

# Stroke 2: 竖 — vertical from just under top-left of 横 going down-left
line([(148, 95), (128, 200)], width=7)

# Stroke 3: 横折弯钩 — from top-right of 横, descend, curve back left through middle,
# then across bottom and up-hook at right end
line([
    (240, 85),
    (245, 130),        # descend
    (225, 165),        # curve inward
    (170, 175),        # cross to left
    (180, 210),        # drop
    (220, 250),        # across bottom
    (265, 250),        # right end
    (270, 225),        # hook up
], width=7)

# Stroke 4: 点 — small dot inside upper-right area
line([(210, 130), (225, 155)], width=9)

out = os.path.join(os.path.dirname(__file__), "01_佤.png")
img.save(out)
print(f"Wrote {out}")
