"""G1 render of radical 讠 (2-stroke simplified 言字旁).

讠 has two strokes:
  1) 点 — a short diagonal dot in the upper region.
  2) 横折提 — horizontal, sharp fold down, then a rising tick.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE = 6

def line(p0, p1, width=STROKE):
    draw.line([p0, p1], fill=INK, width=width)
    # round endpoints
    r = width // 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)

def polyline(pts, width=STROKE):
    for a, b in zip(pts[:-1], pts[1:]):
        line(a, b, width=width)

# Stroke 1: 点 (short diagonal dot in upper area, slight curve)
polyline([(110, 65), (135, 90)], width=7)

# Stroke 2: 横折提 (horizontal + fold turning down + rising tick)
# In GT: horizontal is short, fold drops mostly-straight down, ends with small tick up-right
horiz_start = (80, 150)
horiz_end   = (150, 145)
fold_bottom = (125, 230)
tick_end    = (160, 210)

polyline([horiz_start, horiz_end, fold_bottom, tick_end], width=6)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_讠.png")
img.save(out)
print(f"Wrote {out}")
