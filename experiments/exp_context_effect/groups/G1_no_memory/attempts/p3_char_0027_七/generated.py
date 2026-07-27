"""Render 七 (qi, seven) to a 300x300 PNG.

七 has 2 strokes:
1. 竖 (short vertical/pie start) turning into 横 — actually canonical
   stroke order is: (1) 横 (heng), (2) 竖弯钩 (shu wan gou).
2. Here we render:
   - Stroke 1: a slightly rising 横, crossing the middle.
   - Stroke 2: 竖弯钩 starting upper-center, coming down, curving right
     along the bottom, ending in a small up-hook.

Using PIL for clean 300x300 rendering.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
BRUSH = 8

def line(pts, width=BRUSH):
    draw.line(pts, fill=INK, width=width, joint="curve")
    for (x, y) in pts:
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)

# Stroke 1: 横 — rising horizontal, crosses at roughly middle height.
heng_pts = [(45, 158), (105, 155), (180, 145), (255, 130)]
line(heng_pts, width=BRUSH)

# Stroke 2: 竖弯钩 — starts near horizontal-center-upper, comes down,
# curves rightward at the bottom, ends with a small upward hook.
shu_pts = [
    (140, 90),   # top start
    (142, 115),
    (143, 145),  # about to cross heng
    (144, 180),
    (146, 210),
    (155, 232),  # begin curve
    (180, 243),
    (215, 245),  # along bottom to right
    (238, 240),
    (245, 225),  # small hook up
]
line(shu_pts, width=BRUSH)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_七.png")
img.save(out_path)
print(f"Saved: {out_path}")
