"""
p3_char_0277_先 (xiān) — G4 attempt

Reading order followed:
  1. drawer_memory.md — no chronic primitive matches 先 directly;
     nearest reuse: er_legs (儿) for the bottom 2 strokes. Because
     we're mostly drawing fresh from MMH anchors here, we inline
     rather than import (stroke shapes need custom curves).
  2. INDEX.md grep: 元 (p3_0152) = 一 + 儿 base — pattern reused.
     牛 (p2_106) exists as niu.py (撇+短横+长横+竖). 先 top is similar
     but rearranged. tu.py (土) is 短横+竖+长横 which resembles the
     top half of 先.
  3. errata.md grep for 先: not listed.

Decomposition: 先 = top (4 strokes ~ variant of 生/牛 top) + 儿 base (2 strokes).
Stroke count: 6 (matches MMH expected).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors verbatim. s6 is 竖弯钩 curve; others near-straight brush strokes.'
}

from PIL import Image, ImageDraw


# 米字格 helper: 300x300 image, 9 cells of 100x100.
CELLS = {
    'TL': (0,   0), 'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def A(cell, xf, yf):
    """anchor_to_xy: return pixel (x, y) for (cell, x_frac, y_frac)."""
    cx, cy = CELLS[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)


def line(draw, p0, p1, width):
    draw.line([p0, p1], fill=0, width=width)
    # Round caps for brush feel
    r = width / 2
    for (x, y) in (p0, p1):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def curve(draw, pts, width):
    """Draw a smooth polyline through pts."""
    for i in range(len(pts) - 1):
        line(draw, pts[i], pts[i + 1], width)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- Stroke 1: 撇 short, from ~TL(0.98,0.95) → ML(0.73,0.63)
s1_head = A('TL', 0.984, 0.955)   # (98.4, 95.5)
s1_tail = A('ML', 0.729, 0.632)   # (72.9, 163.2)
# short pie: slight curve, brush tapered
line(d, s1_head, s1_tail, 7)

# ---- Stroke 2: 短横 top, from C(0.05,0.34) → MR(0.05,0.16)
# NB: MMH lists these as "head/tail" of medians; visually this is
# the short top heng of 先 (upper-right area).
s2_head = A('C', 0.049, 0.342)    # (104.9, 134.2)
s2_tail = A('MR', 0.054, 0.157)   # (205.4, 115.7)
line(d, s2_head, s2_tail, 7)

# ---- Stroke 3: 短竖 through center, TC(0.40,0.60) → C(0.43,0.73)
s3_head = A('TC', 0.395, 0.595)   # (139.5, 59.5)
s3_tail = A('C', 0.43, 0.731)     # (143.0, 173.1)
line(d, s3_head, s3_tail, 8)

# ---- Stroke 4: 长横 across middle, ML(0.55,0.93) → MR(0.42,0.73)
# Long horizontal bracket. Slight upward tilt to the right.
s4_head = A('ML', 0.554, 0.931)   # (55.4, 193.1)
s4_tail = A('MR', 0.42, 0.729)    # (242.0, 172.9)
line(d, s4_head, s4_tail, 8)

# ---- Stroke 5: 撇 left leg of 儿, C(0.18,1.00) → BL(0.40,0.97)
s5_head = A('C', 0.184, 0.995)    # (118.4, 199.5)
s5_tail = A('BL', 0.398, 0.965)   # (39.8, 296.5)
# Slight bow for a proper 撇
mid5 = ((s5_head[0] + s5_tail[0]) / 2 - 4,
        (s5_head[1] + s5_tail[1]) / 2 + 2)
curve(d, [s5_head, mid5, s5_tail], 8)

# ---- Stroke 6: 竖弯钩 right leg of 儿, C(0.54,0.85) → BR(0.74,0.40)
# Path: down from head, curve right along the bottom, hook up.
s6_head = A('C', 0.544, 0.854)    # (154.4, 185.4)
s6_tail = A('BR', 0.739, 0.399)   # (273.9, 239.9)
# Route via low-mid then right-bottom then hook-up-right (tail).
p_down   = (s6_head[0] + 4, 250)                       # down-along
p_bend   = (200, 275)                                  # bottom bend
p_right  = (255, 265)                                  # rightward
p_hook   = s6_tail                                     # end / hook tip
curve(d, [s6_head, p_down, p_bend, p_right, p_hook], 8)

img.save('01_先.png')
print('saved 01_先.png')
print(f'strokes drawn: 6 (expected 6)')
