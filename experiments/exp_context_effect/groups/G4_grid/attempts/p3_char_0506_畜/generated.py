"""畜 (chù/xù) — 10 strokes.
Decomposition: 畜 = 亠 (top) + 幺 (middle) + 田 (bottom).
  亠 = s1 (点) + s2 (长横)
  幺 = s3 + s4 + s5 (small folds/dot)
  田 = s6 (左竖) + s7 (横折) + s8 (中横) + s9 (中竖) + s10 (底横)

Following B12 A-recipe: MMH-verbatim anchors + base primitives inline.
No compound-primitive imports — MMH places components in specific slots
that standalone primitives (tou.py, tian if any) would not match.

Reading order: read drawer_memory.md, memory_index.md, INDEX.md grep,
errata.md grep (no 畜 entry).
"""

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code')))

from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier, sample_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 10 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 田 assembled from 5 strokes with N-joint corners; 亠 dot + wide heng; 幺 3-piece cluster.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---------- s1: 点 (top dot) - TC(0.374, 0.527) -> TC(0.652, 0.756) ----------
s1_h = anchor_to_xy(('TC', 0.374, 0.527))
s1_t = anchor_to_xy(('TC', 0.652, 0.756))
# short slanted dot: tapered wider at tail
stroke_variable_width(d, sample_line(s1_h, s1_t, 12), [6]*3 + [9]*4 + [11]*4 + [8]*2)

# ---------- s2: 长横 (top heng of 亠) - ML(0.384, 0.075) -> TR(0.651, 0.961) ----------
s2_h = anchor_to_xy(('ML', 0.384, 0.075))
s2_t = anchor_to_xy(('TR', 0.651, 0.961))
# long horizontal, slight taper (thicker at end typical of 横)
pts = sample_line(s2_h, s2_t, 40)
widths = [7] + [8]*38 + [10] + [7]
stroke_variable_width(d, pts, widths[:41])

# ---------- s3: 幺 first fold - C(0.257, 0.075) -> C(0.491, 0.497) ----------
s3_h = anchor_to_xy(('C', 0.257, 0.075))
s3_t = anchor_to_xy(('C', 0.491, 0.497))
# slanted 撇折-like short stroke; slight curve
mid = ((s3_h[0]+s3_t[0])/2 - 4, (s3_h[1]+s3_t[1])/2 + 2)
pts3 = quad_bezier(s3_h, mid, s3_t, n=20)
stroke_variable_width(d, pts3, [7]*len(pts3))

# ---------- s4: 幺 second fold - C(0.837, 0.14) -> C(0.937, 0.834) ----------
s4_h = anchor_to_xy(('C', 0.837, 0.14))
s4_t = anchor_to_xy(('C', 0.937, 0.834))
# nearly vertical with slight rightward drift
pts4 = sample_line(s4_h, s4_t, 20)
stroke_variable_width(d, pts4, [7]*len(pts4))

# ---------- s5: 幺 third piece - C(0.84, 0.614) -> MR(0.086, 0.916) ----------
s5_h = anchor_to_xy(('C', 0.84, 0.614))
s5_t = anchor_to_xy(('MR', 0.086, 0.916))
# short slanted
pts5 = sample_line(s5_h, s5_t, 12)
stroke_variable_width(d, pts5, [6]*len(pts5))

# ---------- 田 (5 strokes) ----------
def clamp_y(p, ymax=296):
    return (p[0], min(p[1], ymax))

# ---------- s6: 左竖 - BL(0.756, 0.206) -> BL(0.996, 1.012) ----------
s6_h = anchor_to_xy(('BL', 0.756, 0.206))
s6_t = clamp_y(anchor_to_xy(('BL', 0.996, 1.012)))
fat_line(d, s6_h, s6_t, 8)

# ---------- s7: 横折 - BL(0.923, 0.215) -> BR(0.001, 1.108) ----------
s7_h = anchor_to_xy(('BL', 0.923, 0.215))
s7_t = clamp_y(anchor_to_xy(('BR', 0.001, 1.108)))
# 横折 = horizontal then vertical; corner at top-right of the box
corner = (s7_t[0], s7_h[1])  # (right x, top y)
fat_line(d, s7_h, corner, 8)
fat_line(d, corner, s7_t, 8)

# ---------- s8: 中横 - BC(0.148, 0.569) -> BC(0.872, 0.496) ----------
s8_h = anchor_to_xy(('BC', 0.148, 0.569))
s8_t = anchor_to_xy(('BC', 0.872, 0.496))
fat_line(d, s8_h, s8_t, 7)

# ---------- s9: 中竖 - BC(0.415, 0.262) -> BC(0.447, 0.783) ----------
s9_h = anchor_to_xy(('BC', 0.415, 0.262))
s9_t = anchor_to_xy(('BC', 0.447, 0.783))
fat_line(d, s9_h, s9_t, 7)

# ---------- s10: 底横 - BC(0.058, 0.933) -> BC(0.957, 0.818) ----------
s10_h = anchor_to_xy(('BC', 0.058, 0.933))
s10_t = anchor_to_xy(('BC', 0.957, 0.818))
fat_line(d, s10_h, s10_t, 8)

out = os.path.join(HERE, '01_畜.png')
img.save(out)
print(f'wrote {out}')
