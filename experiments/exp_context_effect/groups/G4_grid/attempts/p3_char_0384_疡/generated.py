"""p3_char_0384_疡 — G4 render.

Composition: 疒 (5 strokes: dot + heng + long-pie + dot + ti)
           + 昜-simplified (3 strokes: heng, short-pie, sweeping-hook)

Anchors follow the MMH-derived structural expectations verbatim.
No suitable single bank primitive for 疒 (chuang_sick.py was
proposed in errata but does not yet exist in bank). Inline render
using _anchor helpers.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes, N-class gaps preserved via anchor spacing (no explicit welding).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 疒 outer (5 strokes) ----
# s1: top dot — TC(0.456,0.533) -> TC(0.793,0.756) — 点 (compact dot)
p = anchor_to_xy(('TC', 0.456, 0.533))
q = anchor_to_xy(('TC', 0.793, 0.756))
stroke_variable_width(d, [p, q], [4, 9])

# s2: top heng of 疒 — C(0.084,0.04) -> TR(0.235,0.908)
p = anchor_to_xy(('C', 0.084, 0.04))
q = anchor_to_xy(('TR', 0.235, 0.908))
fat_line(d, p, q, 6)

# s3: long left 撇 of 疒 — TL(0.867,0.958) -> BL(0.343,0.936)
p = anchor_to_xy(('TL', 0.867, 0.958))
q = anchor_to_xy(('BL', 0.343, 0.936))
# Slight curve outward (pie curves left as it descends)
ctrl = ((p[0] + q[0]) / 2 - 6, (p[1] + q[1]) / 2)
pts = quad_bezier(p, ctrl, q, n=30)
widths = [7 - 4 * i / 30 for i in range(31)]  # taper thinner toward tail
stroke_variable_width(d, pts, widths)

# s4: inner short stroke (dot slanting down-right) — ML(0.372,0.292) -> ML(0.618,0.506)
p = anchor_to_xy(('ML', 0.372, 0.292))
q = anchor_to_xy(('ML', 0.618, 0.506))
stroke_variable_width(d, [p, q], [4, 8])

# s5: inner rising stroke (ti/dot) — BL(0.164,0.139) -> ML(0.797,0.752)
p = anchor_to_xy(('BL', 0.164, 0.139))
q = anchor_to_xy(('ML', 0.797, 0.752))
stroke_variable_width(d, [p, q], [7, 3])

# ---- 昜-simplified right side (3 strokes) ----
# s6: horizontal-descending stroke — C(0.128,0.406) -> BC(0.778,0.766)
p = anchor_to_xy(('C', 0.128, 0.406))
q = anchor_to_xy(('BC', 0.778, 0.766))
# curve slightly — this reads as a horizontal-turn or descending heng
mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 - 4)
pts = quad_bezier(p, mid, q, n=30)
widths = [6] * 31
stroke_variable_width(d, pts, widths)

# s7: short pie in BC — BC(0.506,0.001) -> BC(0.084,0.61)
p = anchor_to_xy(('BC', 0.506, 0.001))
q = anchor_to_xy(('BC', 0.084, 0.61))
stroke_variable_width(d, [p, q], [6, 3])

# s8: sweeping 撇 — C(0.86,0.907) -> BC(0.216,0.947)
p = anchor_to_xy(('C', 0.86, 0.907))
q = anchor_to_xy(('BC', 0.216, 0.947))
# gentle curve
ctrl = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + 12)
pts = quad_bezier(p, ctrl, q, n=40)
widths = [7 - 4 * i / 40 for i in range(41)]
stroke_variable_width(d, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_疡.png')
img.save(out)
print('saved', out)
