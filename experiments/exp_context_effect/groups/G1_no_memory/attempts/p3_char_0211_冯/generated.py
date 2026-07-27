"""G1 render of 冯 — 冫 (left radical) + 马 (right)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def line(pts, width=4):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---- Left radical 冫 (two short strokes, upper-left of char body) ----
# Upper dot: short diagonal to the down-right
line([(55, 115), (78, 140)], width=5)
# Lower ti: rising short stroke up-right
line([(45, 195), (78, 175)], width=5)

# ---- Right component 马 (occupies right ~65% of frame) ----
# Stroke 1 (横折): top horizontal, then down (right side of the box top)
line([(115, 90), (215, 90), (215, 150)], width=4)
# Stroke 2: middle horizontal (from left edge across into right wall)
line([(115, 150), (215, 150)], width=4)
# Stroke 3 (竖折折钩): starts at top-right area, sweeps down and around bottom, hooks up
pts = [
    (215, 150),
    (220, 200),
    (215, 245),
    (170, 260),
    (125, 250),
    (135, 235),   # small hook
]
line(pts, width=5)
# Stroke 4: the long bottom horizontal (long slightly-rising stroke through lower area)
line([(100, 220), (240, 210)], width=4)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_冯.png")
img.save(out)
print("Saved", out)
