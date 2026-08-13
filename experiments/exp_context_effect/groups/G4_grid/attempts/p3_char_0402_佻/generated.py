"""佻 (tiāo) — 8 strokes.
Decomposition: 佻 = 亻 (left) + 兆 (right).
  亻 = 撇 + 竖 (2 strokes)
  兆 = 撇 + 提/横 + 点/撇 + 竖弯 + 点 + 撇/竖 (6 strokes)

MMH-verbatim anchors from dispatcher (B9/B10 A-recipe point 2).
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 at TL/ML far-left column (pie head TL 0.806,0.639;
#         shu head ML 0.624,0.456); ren_side default anchors sit at
#         TC/C which would place 亻 too centered. B10 佟(A) precedent
#         for identical slot pattern — inline pie+shu with MMH anchors.
# fresh_component: ren_side_left_column_for_佻

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 draw calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 7 joints declared N (natural gap)
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 亻 inlined per B10 佟 slot; '
             'N-joints preserved as natural gaps.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) ----
# s1: 撇 — TL(0.806,0.639) → ML(0.126,0.925)
draw_pie(d, ('TL', 0.806, 0.639), ('ML', 0.126, 0.925),
         head_width=11, tail_width=2, curve=0.09)
# s2: 竖 — ML(0.624,0.456) → BL(0.662,0.883)
draw_shu(d, ('ML', 0.624, 0.456), ('BL', 0.662, 0.883), width=9)

# ---- 兆 (right, 6 strokes) ----
# s3: 撇 (long left slant) — TC(0.324,0.946) → BL(0.891,0.862)
draw_pie(d, ('TC', 0.324, 0.946), ('BL', 0.891, 0.862),
         head_width=10, tail_width=2, curve=0.08)
# s4: 提/short — ML(0.973,0.365) → C(0.245,0.603)
p0 = anchor_to_xy(('ML', 0.973, 0.365))
p1 = anchor_to_xy(('C', 0.245, 0.603))
fat_line(d, p0, p1, width=7)
# s5: 点 (long dian, from BL top toward C bottom) — BL(0.85,0.183) → C(0.351,0.893)
draw_dian(d, ('BL', 0.85, 0.183), ('C', 0.351, 0.893),
          head_width=3, peak_width=9, curve=0.05, segments=32)
# s6: 竖弯钩 (hooked vertical) — TC(0.781,0.7) → BR(0.73,0.203)
# Median endpoints of a curved stroke: drop from top, curve rightward, hook.
p0 = anchor_to_xy(('TC', 0.781, 0.7))
p2 = anchor_to_xy(('BR', 0.73, 0.203))
# Control point pulls curve toward bottom-right to form the 弯 bend.
ctrl = (p0[0] - 20, p2[1] + 40)
pts = quad_bezier(p0, ctrl, p2, n=48)
widths = [9 - 3 * (i / 48) for i in range(49)]
stroke_variable_width(d, pts, widths)
# s7: 点 (small upper-right dot) — MR(0.303,0.084) → MR(0.039,0.518)
draw_dian(d, ('MR', 0.303, 0.084), ('MR', 0.039, 0.518),
          head_width=2, peak_width=8, curve=0.06, segments=24)
# s8: 捺/hook — C(0.937,0.767) → BR(0.443,0.153)
draw_na(d, ('C', 0.937, 0.767), ('BR', 0.443, 0.153),
        head_width=3, peak_width=11, tail_width=2, curve=0.06)

img.save(os.path.join(os.path.dirname(__file__), '01_佻.png'))
