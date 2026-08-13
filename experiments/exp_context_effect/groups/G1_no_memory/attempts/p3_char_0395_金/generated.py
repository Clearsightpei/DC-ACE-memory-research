"""G1 render of 金 (character)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# 金 — 8 strokes: 人 top (撇, 捺), then 王-like body with two horizontals and a dot pair, base horizontal.
# Layout: top 人 covers top third; body in middle; base horizontal near bottom.

# Stroke 1: 撇 (left-falling from apex)
line([(150, 55), (95, 165)], width=5)

# Stroke 2: 捺 (right-falling from apex)
line([(150, 55), (215, 170)], width=5)

# Stroke 3: short horizontal under the apex (inside the 人)
line([(120, 130), (185, 130)], width=4)

# Stroke 4: left dot (short slash)
line([(130, 155), (120, 175)], width=4)

# Stroke 5: right dot (short slash)
line([(180, 155), (190, 175)], width=4)

# Stroke 6: horizontal 1 (middle bar)
line([(115, 195), (200, 195)], width=4)

# Stroke 7: vertical (center)
line([(155, 175), (155, 245)], width=5)

# Stroke 8: long base horizontal
line([(80, 245), (230, 245)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_金.png"))
