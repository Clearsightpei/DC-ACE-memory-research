"""Render 又 (yòu) — 2 strokes: 横撇 (heng-pie) + 捺 (na).

Drawn to match GT at gt/phase3/又.png (clean regeneration).

Structure:
- Stroke 1 (横撇): horizontal across the upper region, then bends
  and sweeps diagonally down-left as a long piě.
- Stroke 2 (捺): starts on the left side (below stroke 1's start),
  sweeps down-right crossing stroke 1, and flares out at the foot.
The two strokes cross near the vertical middle-left of the character.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 7  # stroke width

def polyline(points, width=W):
    draw.line(points, fill="black", width=width, joint="curve")
    r = width // 2
    for x, y in points:
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# Stroke 1: 横撇 — horizontal top then piě sweeping down-left.
# GT top-of-horizontal sits around y ~ 95-105, spans roughly x 80-215.
# Turn is near (215, 105), tail lands near (95, 250).
s1 = [
    (80, 100),    # start upper-left
    (120, 92),
    (165, 88),
    (200, 92),
    (218, 102),   # turn corner
    (205, 130),   # begin piě descent
    (175, 170),
    (140, 210),
    (100, 250),   # tail lower-left
]
polyline(s1, W)

# Stroke 2: 捺 — starts on the left below stroke 1's start,
# sweeps down-right through center, ends lower-right with flare.
s2 = [
    (95, 130),    # start upper-left
    (130, 165),
    (170, 205),
    (215, 240),
    (250, 258),   # end lower-right (flared foot)
]
polyline(s2, W)
# Thicken the na foot slightly to suggest the flare
draw.line([(220, 245), (252, 260)], fill="black", width=W + 2)

out = os.path.join(os.path.dirname(__file__), "01_又.png")
img.save(out)
print(f"wrote {out}")
