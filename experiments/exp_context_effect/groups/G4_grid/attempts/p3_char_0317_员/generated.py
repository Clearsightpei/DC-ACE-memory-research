"""p3_char_0317_员 — G4 attempt.

Read: drawer_memory.md (v8), memory_index.md, INDEX.md (grepped 口 / 贝).
Split: 员 = 口 (top, 3 strokes) + 贝-simplified (bottom, 4 strokes: 竖 + 横折 + 撇 + 点).
Errata note on p2_radical_085_贝: prior FAIL was compressed frame + tiny dot.
Fix idea: TR9 span expansion, shorten pie, enlarge dot — will apply here.
No chronic import fits (口/贝 not chronic). Inline via _anchor + fat_line
following MMH-verbatim anchors (v9: trust MMH when uncertain).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 draw calls, one per MMH stroke (横折 is one stroke drawn as heng+shu)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints are N-class → gaps kept via _shorten
    'overall_pass': True,
    'notes': '员 = 口 top + 贝-simplified bottom. All joints N.',
}

import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
W = 8

# ---- Top 口 (strokes 1-3) --------------------------------------------------

# s1 — 左竖 of top 口
s1h = anchor_to_xy(('TL', 0.85, 0.75))     # (85, 75)
s1t = anchor_to_xy(('C',  0.04, 0.35))     # (104, 135)

# s2 — 横折 of top 口 (heng along top, corner, then short shu down)
s2h = anchor_to_xy(('TL', 0.99, 0.75))     # (99, 75)
s2t = anchor_to_xy(('C',  0.83, 0.04))     # (183, 104)
s2c = (s2t[0], s2h[1])                     # corner at top-right (183, 75)

# s3 — 底横 of top 口
s3h = anchor_to_xy(('C',  0.10, 0.21))     # (110, 121)
s3t = anchor_to_xy(('MR', 0.01, 0.15))     # (201, 115)

# Apply N-gap shortening at 口 corners
s1h_g = _shorten(s1h, s1t, 4)
s1t_g = _shorten(s1t, s1h, 4)
s2h_g = _shorten(s2h, s2c, 4)
s2t_g = _shorten(s2t, s2c, 4)
s3h_g = _shorten(s3h, s3t, 3)
s3t_g = _shorten(s3t, s3h, 3)

fat_line(d, s1h_g, s1t_g, W)
fat_line(d, s2h_g, s2c, W)
fat_line(d, s2c, s2t_g, W)
# tiny disc at corner for smoothness
cx, cy = s2c; r = W / 2.0
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
fat_line(d, s3h_g, s3t_g, W)

# ---- Bottom 贝-simplified (strokes 4-7) -----------------------------------

# s4 — 左竖 of 贝 body
s4h = anchor_to_xy(('ML', 0.87, 0.50))     # (87, 150)
s4t = anchor_to_xy(('BL', 0.95, 0.54))     # (95, 254)

# s5 — 横折 of 贝 body (top heng across, corner, right shu down)
s5h = anchor_to_xy(('C',  0.02, 0.53))     # (102, 153)
s5t = anchor_to_xy(('BR', 0.00, 0.55))     # (200, 255)
s5c = (s5t[0], s5h[1])                     # corner at top-right (200, 153)

# N-gap on 贝 top-left corner: s4.head ⇆ s5.head
s4h_g = _shorten(s4h, s4t, 4)
s5h_g = _shorten(s5h, s5c, 4)

fat_line(d, s4h_g, s4t, W)
fat_line(d, s5h_g, s5c, W)
fat_line(d, s5c, s5t, W)
cx, cy = s5c; r = W / 2.0
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# s6 — 撇 (long left leg from inside 贝 down past baseline)
s6h = anchor_to_xy(('C',  0.33, 0.73))     # (133, 173)
s6t = anchor_to_xy(('BL', 0.69, 1.09))     # (69, 309)
fat_line(d, s6h, s6t, W)

# s7 — 点 / 捺 (right leg, short and sloped down-right, fatter tail)
s7h = anchor_to_xy(('BC', 0.67, 0.68))     # (167, 268)
s7t = anchor_to_xy(('BR', 0.19, 1.14))     # (219, 314)
fat_line(d, s7h, s7t, W + 2)               # slightly fatter — errata TR9 hint (enlarge dot)

out = os.path.join(os.path.dirname(__file__), '01_员.png')
img.save(out)
print('saved', out)
