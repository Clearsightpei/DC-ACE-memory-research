"""Render 疌 to 01_疌.png at 300x300.
Structure: 聿-like top (vertical + 3 horizontals) + 疋-like bottom
(a small horizontal cap + 撇/捺 legs anchored on a base).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p0, p1, width=4):
    d.line([p0, p1], fill=BLACK, width=width)


def curve(pts, width=4):
    # simple polyline as freehand
    for a, b in zip(pts[:-1], pts[1:]):
        d.line([a, b], fill=BLACK, width=width)


# --- TOP HALF: 聿-like block ---
# horizontal 1 (top short slanted)
curve([(110, 78), (185, 72)], width=4)
# horizontal 2 (middle, longest)
curve([(95, 118), (215, 112)], width=4)
# horizontal 3 (mid-lower)
curve([(105, 155), (200, 150)], width=4)
# central vertical descending through top
curve([(148, 60), (150, 175)], width=5)
# small tick top of vertical (like 聿's top)
curve([(140, 66), (150, 60)], width=3)

# --- BOTTOM HALF: 疋-like / 走-like structure ---
# horizontal base (upper of the bottom half)
curve([(115, 190), (210, 188)], width=4)

# short vertical descender from mid horizontal
curve([(155, 190), (155, 218)], width=4)

# small horizontal accent (like the little tick under horizontal in 疋)
curve([(150, 218), (185, 216)], width=3)

# left leg 撇 — sweeping down-left from left of vertical
curve([(150, 220), (135, 245), (110, 268), (82, 282)], width=5)

# 捺 — long stroke sweeping down-right, ends with flat foot tail
curve([(158, 230), (185, 258), (225, 278), (258, 282)], width=5)
# flat foot tail extending
curve([(245, 282), (270, 283)], width=4)

out = os.path.join(os.path.dirname(__file__), "01_疌.png")
img.save(out)
print(f"wrote {out}")
