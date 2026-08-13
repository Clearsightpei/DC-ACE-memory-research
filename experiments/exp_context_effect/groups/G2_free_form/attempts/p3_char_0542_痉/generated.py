"""Render 痉 (jìng, spasm) at 300x300, black on white.

TIER-0 F 4-move + TIER-0 H (components must touch).
Frozen radical: 疒 (14x attested). 圣 body (又 top + 土 bottom).

Structure (10 strokes total):
  疒 canopy (5 strokes) — decomposition per drawer_memory pos-900:
    1. 点 top-right (short slanted dot ABOVE the 横)
    2. 横 top (long horizontal spanning canopy width)
    3. 点 inside-upper-left
    4. 提 inside-lower-left (rising flick)
    5. 长撇 sweeping from top-横's left endpoint down to bottom-left

  圣 body (5 strokes) tucked INSIDE the canopy:
    又 top (2 strokes):
      6. 横撇 (short horizontal → down-left slant)
      7. 捺 (S-curve, right-down sweep with foot flare)
    土 bottom (3 strokes):
      8. 横 (short top)
      9. 竖 (vertical center)
     10. 横 (longer bottom, extends further right)

Components MUST touch: 圣 sits against/inside the 撇 sweep.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab_line(pts, width_start=8, width_end=8):
    """Variable-width polyline via overlapping circles (tapered stroke)."""
    if len(pts) < 2:
        return
    n_seg = len(pts) - 1
    for si in range(n_seg):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for t in range(steps + 1):
            u = t / steps
            global_u = (si + u) / n_seg
            w = width_start * (1 - global_u) + width_end * global_u
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = ((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0]
             + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0])
        y = ((1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1]
             + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1])
        pts.append((x, y))
    return pts


# ============= 疒 CANOPY (5 strokes) =============
# Stroke 1: 点 top-right (above the 横)
dab_line([(140, 42), (158, 70)], width_start=4, width_end=8)

# Stroke 2: 横 top (long horizontal — spans canopy width)
dab_line([(85, 92), (150, 90), (245, 96)], width_start=6, width_end=7)

# Stroke 3: 点 inside upper-left (below the 横, right of the 撇)
dab_line([(58, 128), (78, 148)], width_start=4, width_end=8)

# Stroke 4: 提 inside lower-left (rising flick)
dab_line([(48, 195), (85, 175)], width_start=8, width_end=3)

# Stroke 5: 长撇 (long sweeping descender from top-横's left end)
long_pie = [
    (88, 92),
    (86, 135),
    (80, 180),
    (65, 225),
    (45, 265),
    (30, 282),
]
dab_line(long_pie, width_start=9, width_end=4)


# ============= 圣 BODY (5 strokes) — inside canopy, tucked under 撇 =============
# 又 top: (~x=110..250, y=100..170)
# Stroke 6: 横撇 (short 横 then 撇 sweeping down-left)
you_hp = [(125, 118), (200, 116), (198, 130)]
dab_line(you_hp, width_start=5, width_end=7)
# 撇 down-left part continues from shoulder
you_pie = bez((198, 130), (185, 155), (160, 175), (130, 200))
dab_line(you_pie, width_start=7, width_end=3)

# Stroke 7: 捺 (S-curve from top-inner sweeping down-right, foot flare)
you_na = bez((175, 135), (200, 165), (225, 185), (250, 200))
dab_line(you_na, width_start=3, width_end=9)
# foot flare (short flick right)
dab_line([(250, 200), (258, 198)], width_start=9, width_end=4)

# 土 bottom: (~x=125..255, y=215..275)
# Stroke 8: 横 (short top of 土)
dab_line([(150, 225), (230, 225)], width_start=6, width_end=6)

# Stroke 9: 竖 (vertical of 土)
dab_line([(190, 225), (190, 270)], width_start=7, width_end=7)

# Stroke 10: 横 (longer bottom of 土)
dab_line([(125, 272), (255, 272)], width_start=7, width_end=8)


img.save("01_痉.png")
print("saved 01_痉.png")
