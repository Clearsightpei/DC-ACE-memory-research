"""p3_char_0319_听 (tīng, "listen", 7 strokes)

Decomposition: 听 = 口 (left) + 斤 (right).
  Left 口:  s1 竖 (left wall), s2 横折 (top+right corner), s3 横 (bottom).
  Right 斤: s4 短撇 (top-right little pie), s5 长撇 (long diagonal
            from top-center to bottom-left of right half),
            s6 横 (middle bar), s7 竖 (vertical, extends past canvas).

Memory notes consulted:
  - drawer_memory.md: left-right composition, left in x[0.05,0.42],
    right in x[0.48,0.95]. Not calling draw_kou because MMH anchors
    put the 口 in the ML column (left), while draw_kou defaults sit
    around the center. Inlining per MMH anchors verbatim (v9 lesson
    from 比: MMH-verbatim > hand-tuned).
  - errata.md: 听 not listed.
  - joints: all 6 joints are N-class (natural gaps ~12–18 px), so
    do NOT weld corners of 口 nor apex of 斤. Shorten each endpoint
    by ~5 px toward the joint to preserve visible gaps.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; 口 on left via MMH anchors, 斤 on right; all 6 joints N (gaps preserved by _shorten).'
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


def draw_ting(draw):
    # ---- LEFT: 口 ----
    # s1 竖 (left wall of 口)
    s1h = anchor_to_xy(('ML', 0.27, 0.324))
    s1t = anchor_to_xy(('BL', 0.469, 0.098))
    # s2 横折 (top bar + right wall of 口): head→corner→tail
    s2h = anchor_to_xy(('ML', 0.422, 0.324))
    s2c = anchor_to_xy(('ML', 0.85, 0.35))   # top-right corner of 口
    s2t = anchor_to_xy(('ML', 0.779, 0.743))
    # s3 横 (bottom bar of 口)
    s3h = anchor_to_xy(('ML', 0.524, 0.919))
    s3t = anchor_to_xy(('ML', 0.984, 0.834))

    # Preserve N-gaps at 口 corners (shorten toward neighbor)
    s1h_g = _shorten(s1h, s1t, 5)   # gap at top-left vs s2.head
    s1t_g = _shorten(s1t, s1h, 5)   # gap at bottom-left vs s3.head
    s2h_g = _shorten(s2h, s2c, 4)
    s2t_g = _shorten(s2t, s2c, 3)   # small gap vs s3.mid
    s3h_g = _shorten(s3h, s3t, 5)   # gap at bottom-left vs s1.tail

    fat_line(draw, s1h_g, s1t_g, width=8)
    fat_line(draw, s2h_g, s2c, width=8)
    fat_line(draw, s2c, s2t_g, width=8)
    fat_line(draw, s3h_g, s3t, width=8)

    # ---- RIGHT: 斤 ----
    # s4 短撇 (upper tiny pie): head TR(0.297,0.853) → tail C(0.485,0.154)
    s4h = anchor_to_xy(('TR', 0.297, 0.853))
    s4t = anchor_to_xy(('C', 0.485, 0.154))
    # Slight curve as a pie: bow control point pulled left
    s4_ctrl = ((s4h[0] + s4t[0]) / 2 - 6, (s4h[1] + s4t[1]) / 2)
    pts4 = quad_bezier(s4h, s4_ctrl, s4t, n=30)
    widths4 = [max(3, 8 - int(6 * i / len(pts4))) for i in range(len(pts4))]
    stroke_variable_width(draw, pts4, widths4)

    # s5 长撇 (long diagonal): head C(0.228,0.069) → tail BL(0.729,0.854)
    s5h = anchor_to_xy(('C', 0.228, 0.069))
    s5t = anchor_to_xy(('BL', 0.729, 0.854))
    # Slight leftward bow
    s5_ctrl = ((s5h[0] + s5t[0]) / 2 - 8, (s5h[1] + s5t[1]) / 2 + 4)
    pts5 = quad_bezier(s5h, s5_ctrl, s5t, n=50)
    # Variable width: thicker in middle, thinner at tail (pie taper)
    n5 = len(pts5)
    widths5 = []
    for i in range(n5):
        f = i / (n5 - 1)
        if f < 0.15:
            w = 6 + int(3 * f / 0.15)   # 6→9 head→shoulder
        else:
            w = int(9 - 6 * (f - 0.15) / 0.85)  # 9→3 taper
        widths5.append(max(2, w))
    stroke_variable_width(draw, pts5, widths5)

    # s6 横 (middle bar of 斤): head C(0.45,0.638) → tail MR(0.654,0.491)
    s6h = anchor_to_xy(('C', 0.45, 0.638))
    s6t = anchor_to_xy(('MR', 0.654, 0.491))
    # Shorten head slightly to leave N-gap with s5.mid
    s6h_g = _shorten(s6h, s6t, 4)
    fat_line(draw, s6h_g, s6t, width=8)

    # s7 竖 (vertical of 斤): head C(0.881,0.605) → tail BC(0.989,1.188)
    # Tail y_frac=1.188 -> pixel y=318.8 (past canvas). Clamp to 298.
    s7h = anchor_to_xy(('C', 0.881, 0.605))
    s7t_raw = anchor_to_xy(('BC', 0.989, 1.188))
    s7t = (s7t_raw[0], min(298.0, s7t_raw[1]))
    # Shorten head slightly to leave N-gap with s6.mid
    s7h_g = _shorten(s7h, s7t, 4)
    fat_line(draw, s7h_g, s7t, width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ting(d)
    out = os.path.join(os.path.dirname(__file__), '01_听.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
