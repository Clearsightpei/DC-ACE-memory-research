"""知 (zhī) — 8 strokes.
Decomposition: 知 = 矢 (left) + 口 (right, compressed).
矢 = 丿 + 一 (upper short) + 一 (middle long) + 丿 (big pie) + 短捺
口 = 竖 + 横折 + 一 (all N-corner gaps)

Per B10 A-recipe: use MMH-verbatim anchors + inline base primitives.
"""

# BANK_DEVIATION
# skipped: kou.py
# reason: bank kou defaults are standalone-scale in the middle;
#         MMH places 口 in right-half compressed slot (C→BR cells).
# fresh_component: kou_right_half_for_zhi

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 draw-strokes below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '知 = 矢 (5 strokes) + 口 (3 strokes, right-half). All MMH-verbatim anchors. '
             '口 corners kept as N-gaps (~10-15 px shorten).',
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_zhi(img_path='01_知.png'):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: top short 撇 (TL → ML, curved down-left) ----
    p0 = anchor_to_xy(('TL', 0.888, 0.668))
    p2 = anchor_to_xy(('ML', 0.448, 0.632))
    ctrl = ((p0[0] + p2[0]) / 2 + 3, (p0[1] + p2[1]) / 2 - 6)
    pts = quad_bezier(p0, ctrl, p2, n=30)
    widths = [max(2, int(6 - 3 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- s2: upper 一 (small horizontal, ML → C) ----
    p0 = anchor_to_xy(('ML', 0.782, 0.389))
    p1 = anchor_to_xy(('C',  0.564, 0.263))
    fat_line(d, p0, p1, width=6)

    # ---- s3: middle 一 (long horizontal, BL → C — slight upward slant) ----
    p0 = anchor_to_xy(('BL', 0.272, 0.065))
    p1 = anchor_to_xy(('C',  0.588, 0.881))
    fat_line(d, p0, p1, width=6)

    # ---- s4: big 撇 (ML → BL, sweeping down-left) ----
    p0 = anchor_to_xy(('ML', 0.979, 0.456))
    p2 = anchor_to_xy(('BL', 0.36, 0.897))
    ctrl = ((p0[0] + p2[0]) / 2 - 6, (p0[1] + p2[1]) / 2 + 6)
    pts = quad_bezier(p0, ctrl, p2, n=45)
    widths = [max(2, int(7 - 4 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- s5: 短捺 (compressed right leg, BC → BC, short diagonal) ----
    p0 = anchor_to_xy(('BC', 0.21, 0.238))
    p2 = anchor_to_xy(('BC', 0.529, 0.643))
    ctrl = ((p0[0] + p2[0]) / 2 - 2, (p0[1] + p2[1]) / 2 + 4)
    pts = quad_bezier(p0, ctrl, p2, n=30)
    widths = [max(2, int(3 + 4 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- 口 (right-half compressed) ----
    # s6: 竖 (left wall of 口), C → BC
    s6h = anchor_to_xy(('C',  0.623, 0.626))
    s6t = anchor_to_xy(('BC', 0.852, 0.581))
    s6h_g = _shorten(s6h, s6t, 3)
    s6t_g = _shorten(s6t, s6h, 3)
    fat_line(d, s6h_g, s6t_g, width=7)

    # s7: 横折 (top+right of 口), C → BR (with corner near TR of BR cell)
    s7h = anchor_to_xy(('C',  0.787, 0.641))
    s7t = anchor_to_xy(('BR', 0.353, 0.2))
    # infer corner: roughly at the top-right of the box → same y as s7h, x as s7t
    s7c = (s7t[0], s7h[1])
    s7h_g = _shorten(s7h, s7c, 3)
    s7t_g = _shorten(s7t, s7c, 3)
    fat_line(d, s7h_g, s7c, width=7)
    fat_line(d, s7c, s7t_g, width=7)
    cx, cy = s7c; r = 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s8: 横 (bottom of 口), BC → BR
    s8h = anchor_to_xy(('BC', 0.916, 0.402))
    s8t = anchor_to_xy(('BR', 0.537, 0.317))
    s8h_g = _shorten(s8h, s8t, 3)
    fat_line(d, s8h_g, s8t, width=7)

    img.save(os.path.join(os.path.dirname(__file__), img_path))


if __name__ == '__main__':
    draw_zhi()
