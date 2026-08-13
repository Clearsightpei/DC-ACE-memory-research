"""Render 疳 (gan1, infantile malnutrition) at 300x300, black on white.

Structure: 疒 canopy (5 strokes) + 甘 body (5 strokes) tucked INSIDE the
canopy — body's top-横 aligns with canopy 一 so components touch.

疒 canopy (5 strokes) — per form_catalog.md B10 addition:
  1. 丶 top-dot (crown, right-of-center above the 横)
  2. 一 top-横 (running from left of dot to right edge)
  3. 丿 long down-left 撇 (from left end of 横 to bottom-left)
  4. 丶 inner upper dot (冫-upper, inside upper-left wedge)
  5. 提 inner lower rising tick (冫-lower, below the dot)

甘 body (5 strokes) — rectangle box + middle horizontal, sits inside
the wedge (right of the 冫 pair, below the 一):
  6. 一 top-横 of 甘 (leftmost point touches the canopy 撇 area)
  7. 丨 left-vertical
  8. 丨 right-vertical
  9. 一 middle-短横 (interior)
  10. 一 bottom-横 (closes the box)

Sibling / canopy compliance:
  - 疒 NOT 广: interior 冫 pair present (form_catalog line 599).
  - Components TOUCH: 甘 top-横 aligns/overlaps with canopy 一
    (drawer_memory TIER-0 H).
  - Hook rule: no hooks in 疳.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab_line(pts, width_start=8, width_end=8):
    """Draw a variable-width polyline via overlapping ellipses."""
    if len(pts) < 2:
        return
    n_seg = len(pts) - 1
    for si in range(n_seg):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for t in range(steps + 1):
            u = t / steps
            gu = (si + u) / n_seg
            w = width_start * (1 - gu) + width_end * gu
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ============== 疒 canopy ==============

# 1. Top 丶 (crown dot, slanted top-left to bottom-right, small)
dab_line([(148, 40), (168, 68)], width_start=4, width_end=8)

# 2. 一 top-横 (wide horizontal; slightly rising toward right)
dab_line([(80, 92), (170, 90), (260, 94)], width_start=6, width_end=7)

# 3. 丿 long left-falling 撇 from left end of 横 down to bottom-left
curve = [
    (82, 92),
    (78, 130),
    (72, 175),
    (60, 220),
    (48, 260),
    (38, 278),
]
dab_line(curve, width_start=9, width_end=4)

# 4. Inner 丶 (冫 upper), teardrop slanting down-right, INSIDE the wedge
#    between canopy 撇 (at this y ~x=78) and 甘 body (starts x=128).
dab_line([(95, 118), (115, 138)], width_start=4, width_end=8)

# 5. Inner 提 (冫 lower), rising short flick, thick->thin, below the dot
dab_line([(85, 172), (118, 155)], width_start=8, width_end=4)

# ============== 甘 body (right side, inside canopy wedge) ==============
# Box: x in [130, 255], y in [125, 250]
# The top of 甘 touches the underside of canopy 一.

# 6. 甘 top 一 (short-medium horizontal, sits just below canopy 一)
dab_line([(128, 128), (200, 126), (258, 128)], width_start=6, width_end=6)

# 7. 甘 left 丨 (vertical descending from left end of top横 to bottom)
dab_line([(135, 124), (135, 180), (135, 252)], width_start=7, width_end=7)

# 8. 甘 middle 短横 (short interior horizontal, centered)
dab_line([(155, 188), (232, 188)], width_start=5, width_end=5)

# 9. 甘 right 丨 (vertical descending from right end of top横 to bottom)
dab_line([(252, 124), (252, 185), (252, 252)], width_start=7, width_end=7)

# 10. 甘 bottom 一 (wide horizontal closing the box)
dab_line([(125, 252), (200, 254), (258, 252)], width_start=7, width_end=7)

img.save("01_疳.png")
print("saved 01_疳.png")
