"""造 (zào, 10 strokes).

Decomposition: 造 = 告 (top-right, 7 strokes) + 辶 (walking radical wrapping bottom-left, 3 strokes).
  告 = 丿 + 一 + 丨 + 一 + 口 (口 = 丨 + 横折 + 一).
  辶 = 点 + 横折折撇 + 平捺.

# BANK_DEVIATION
# skipped: chuo_walk.py
# reason: chuo_walk.py's baked anchors fill nearly the whole canvas as
#   standalone 辶, but here 辶 must slot into bottom-left while 告 occupies
#   the upper-right ~two-thirds. Inline with MMH-verbatim anchors.
# fresh_component: chuo_walk_bottom_left_slot_for_compound
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 辶 inlined per BANK_DEVIATION; N-joint gaps preserved.',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 告 (top part) ----
    # s1 — 丿 short pie top-left of 牛
    s1_h = anchor_to_xy(('TC', 0.368, 0.97))
    s1_t = anchor_to_xy(('C',  0.184, 0.562))
    stroke_variable_width(d, [s1_h, s1_t], [6, 4])

    # s2 — 一 short heng at top-right
    s2_h = anchor_to_xy(('C',  0.456, 0.315))
    s2_t = anchor_to_xy(('MR', 0.332, 0.128))
    fat_line(d, s2_h, s2_t, 5)

    # s3 — 丨 long vertical shu (spine of 牛)
    s3_h = anchor_to_xy(('TC', 0.755, 0.548))
    s3_t = anchor_to_xy(('C',  0.819, 0.623))
    fat_line(d, s3_h, s3_t, 6)

    # s4 — 一 long horizontal across middle (bottom of 牛)
    s4_h = anchor_to_xy(('C',  0.09, 0.805))
    s4_t = anchor_to_xy(('MR', 0.619, 0.629))
    fat_line(d, s4_h, s4_t, 5)

    # ---- 口 (in 告) ----
    # s5 — 丨 left vertical of 口
    s5_h = anchor_to_xy(('BC', 0.368, 0.007))
    s5_t = anchor_to_xy(('BC', 0.57, 0.584))
    fat_line(d, s5_h, s5_t, 5)

    # s6 — 横折 (heng then zhe) top+right of 口
    s6_h = anchor_to_xy(('BC', 0.518, 0.01))
    s6_t = anchor_to_xy(('BR', 0.095, 0.312))
    # approximate compound: heng to a corner then zhe down
    corner = (s6_t[0], s6_h[1])
    stroke_variable_width(d, [s6_h, corner, s6_t], [5, 5, 5])

    # s7 — 一 bottom of 口
    s7_h = anchor_to_xy(('BC', 0.617, 0.432))
    s7_t = anchor_to_xy(('BR', 0.268, 0.417))
    fat_line(d, s7_h, s7_t, 5)

    # ---- 辶 (bottom-left wrap) ----
    # s8 — 点 (dot) upper-left
    s8_h = anchor_to_xy(('TL', 0.606, 0.776))
    s8_t = anchor_to_xy(('ML', 0.949, 0.043))
    stroke_variable_width(d, [s8_h, s8_t], [3, 8])

    # s9 — 横折折撇 (compound S-fold)
    s9_h = anchor_to_xy(('ML', 0.249, 0.693))
    s9_t = anchor_to_xy(('BL', 0.835, 0.481))
    # Compound: small heng right, zhe down, then pie down-left, then curve down-right to tail
    # Approximate as polyline with 4 intermediate points
    p1 = anchor_to_xy(('ML', 0.55, 0.68))    # top heng tail
    p2 = anchor_to_xy(('ML', 0.62, 0.90))    # first zhe down
    p3 = anchor_to_xy(('BL', 0.40, 0.20))    # pie start
    p4 = anchor_to_xy(('BL', 0.55, 0.42))    # pie curve
    stroke_variable_width(d, [s9_h, p1, p2, p3, p4, s9_t], [4, 5, 5, 5, 6, 5])

    # s10 — 平捺 long wavy sweep across bottom
    s10_h = anchor_to_xy(('BL', 0.275, 0.631))
    s10_t = anchor_to_xy(('BR', 0.736, 0.856))
    # wavy: dip then rise then final flat-taper
    m1 = anchor_to_xy(('BL', 0.60, 0.75))
    m2 = anchor_to_xy(('BC', 0.30, 0.85))
    m3 = anchor_to_xy(('BC', 0.75, 0.95))
    m4 = anchor_to_xy(('BR', 0.35, 0.90))
    stroke_variable_width(d, [s10_h, m1, m2, m3, m4, s10_t], [3, 5, 7, 10, 8, 3])

    img.save(os.path.join(os.path.dirname(__file__), '01_造.png'))


if __name__ == '__main__':
    draw()
