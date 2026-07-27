"""
Draw 三 (three) — three horizontal strokes, PIL.
Rules from form_catalog:
- 横 stacked family: bottom LONGEST, middle SHORTEST, top medium.
- Slight upward-right tilt (calligraphic), 顿 dab at start and end.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = 0
BG = 255

img = Image.new("L", (W, H), BG)
draw = ImageDraw.Draw(img)


def heng(cx, cy, length, width, tilt=-4):
    """Draw a 横 stroke centered near (cx, cy) with given length.
    tilt: vertical offset of right end relative to left (negative = up-right)."""
    x0 = cx - length // 2
    x1 = cx + length // 2
    y0 = cy
    y1 = cy + tilt
    # main bar (rounded ends for a brush feel)
    draw.line([(x0, y0), (x1, y1)], fill=INK, width=width)
    # 顿 dab at start (slightly thicker)
    r = width // 2 + 2
    draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], fill=INK)
    # 顿 dab at end
    r2 = width // 2 + 3
    draw.ellipse([x1 - r2, y1 - r2, x1 + r2, y1 + r2], fill=INK)


# Top 横 — medium length
heng(cx=150, cy=95, length=110, width=8, tilt=-3)

# Middle 横 — shortest (visually smaller in GT)
heng(cx=150, cy=155, length=85, width=8, tilt=-3)

# Bottom 横 — longest
heng(cx=150, cy=225, length=175, width=9, tilt=-5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_三.png")
img.save(out_path)
print(f"Saved {out_path}")
