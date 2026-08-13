"""Render 证 (zhèng) — 讠 + 正 — to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=5):
    d.line([p1, p2], fill="black", width=w)

# --- Left: 讠 (speech radical, simplified) ---
# Top dot (丶)
line((60, 70), (78, 92), w=6)

# Horizontal-fold-tick (横折提):
# short horizontal then diagonal down-left then tick out right
line((40, 120), (95, 120), w=5)    # horizontal top
line((95, 120), (55, 175), w=5)    # slant down-left
line((55, 175), (100, 180), w=5)   # tick out right

# --- Right: 正 (5 strokes: 一 丨 一 丨 一) ---
# Stroke 1: top horizontal
line((140, 100), (245, 100), w=5)
# Stroke 2: short vertical (from top-h, down-left)
line((155, 100), (155, 155), w=5)
# Stroke 3: short middle horizontal
line((155, 155), (215, 155), w=5)
# Stroke 4: long vertical (center, from top-h down to bottom-h)
line((195, 100), (195, 225), w=5)
# Stroke 5: bottom horizontal (longest)
line((130, 225), (255, 225), w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_证.png"))
print("saved 01_证.png")
