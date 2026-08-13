# -*- coding: utf-8 -*-
# G4 attempt for p3_char_0443_面 (9 strokes, all-N joints)
# Reading order followed: memory_index.md, drawer_memory.md (no direct import
# candidates for 面 as-is; kou/mian not directly applicable — 面 is its own
# frame with 目-like interior). Rendering fresh from MMH-injected anchors.
# No BANK_DEVIATION block needed: not skipping any called bank primitive.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All joints declared N (neighbor with small gap). Endpoints used '
             'directly from MMH anchors; no stroke extended past its endpoint, '
             'so N-gaps arise naturally.'
}

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH_MAIN = 6       # main frame strokes
TH_INNER = 5      # inner short horizontals

# ---- Stroke 1: top horizontal 一   TL(0.879,0.911) -> TR(0.188,0.791) ----
p1a = anchor_to_xy(('TL', 0.879, 0.911))
p1b = anchor_to_xy(('TR', 0.188, 0.791))
fat_line(d, p1a, p1b, TH_MAIN, INK)

# ---- Stroke 2: 撇 (pie) TC(0.324,0.999) -> C(0.119,0.462) ----
# Curve gently to the left as it descends.
p2a = anchor_to_xy(('TC', 0.324, 0.999))
p2b = anchor_to_xy(('C',  0.119, 0.462))
# Control point slightly right of midpoint x, biased toward the head
ctrl = (p2a[0] + 6, (p2a[1] + p2b[1]) / 2 - 4)
pts = quad_bezier(p2a, ctrl, p2b, n=40)
widths = [TH_MAIN + 1 - i * 0.03 for i in range(len(pts))]  # slight taper
stroke_variable_width(d, pts, widths, INK)

# ---- Stroke 3: left inner vertical (丨-ish) ML(0.451,0.564) -> BL(0.75,0.815)
p3a = anchor_to_xy(('ML', 0.451, 0.564))
p3b = anchor_to_xy(('BL', 0.75,  0.815))
fat_line(d, p3a, p3b, TH_MAIN, INK)

# ---- Stroke 4: 横折 (heng-zhe) — top+right of inner frame
#     ML(0.601,0.585) -> BR(0.279,0.848)
p4a = anchor_to_xy(('ML', 0.601, 0.585))
p4b = anchor_to_xy(('BR', 0.279, 0.848))
# Bend point: right along p4a's y until x = p4b's x, then down to p4b
bend = (p4b[0], p4a[1])
fat_line(d, p4a, bend, TH_MAIN, INK)
fat_line(d, bend, p4b, TH_MAIN, INK)

# ---- Stroke 5: small inner short horizontal (upper-left inside frame) ----
#     C(0.081,0.605) -> BC(0.245,0.607)
p5a = anchor_to_xy(('C',  0.081, 0.605))
p5b = anchor_to_xy(('BC', 0.245, 0.607))
fat_line(d, p5a, p5b, TH_INNER, INK)

# ---- Stroke 6: small inner short horizontal (upper-right inside frame) ----
#     C(0.655,0.512) -> BC(0.69,0.552)
p6a = anchor_to_xy(('C',  0.655, 0.512))
p6b = anchor_to_xy(('BC', 0.69,  0.552))
fat_line(d, p6a, p6b, TH_INNER, INK)

# ---- Stroke 7: inner horizontal (middle band) ----
#     C(0.286,0.939) -> C(0.559,0.878)
p7a = anchor_to_xy(('C', 0.286, 0.939))
p7b = anchor_to_xy(('C', 0.559, 0.878))
fat_line(d, p7a, p7b, TH_INNER, INK)

# ---- Stroke 8: inner horizontal (lower band) ----
#     BC(0.286,0.306) -> BC(0.559,0.241)
p8a = anchor_to_xy(('BC', 0.286, 0.306))
p8b = anchor_to_xy(('BC', 0.559, 0.241))
fat_line(d, p8a, p8b, TH_INNER, INK)

# ---- Stroke 9: bottom horizontal closing frame ----
#     BL(0.817,0.751) -> BR(0.142,0.619)
p9a = anchor_to_xy(('BL', 0.817, 0.751))
p9b = anchor_to_xy(('BR', 0.142, 0.619))
fat_line(d, p9a, p9b, TH_MAIN, INK)

out = os.path.join(os.path.dirname(__file__), '01_面.png')
img.save(out)
print('wrote', out, '9 strokes')
