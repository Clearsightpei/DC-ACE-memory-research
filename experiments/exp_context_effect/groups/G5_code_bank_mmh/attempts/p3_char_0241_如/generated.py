"""如 (ru) — 6 strokes = 女 (3) + 口 (3), left-right composition.

P-A-006 route: MMH-anchor verbatim + stroke-primitive layer (NOT whole-radical
composition), per B7 signature discovery. 6 strokes fits P-A-006's 5-6 stroke band.

Whole-radical primitives nu_woman.py and kou_mouth.py exist in bank but are
SKIPPED to avoid double-transform aspect distortion (P-COMP-009); each stroke
is inlined at MMH-anchor pixel coords.
"""
# BANK_DEVIATION
# skipped: nu_woman.py, kou_mouth.py
# reason: 6-stroke Phase-3 char fits P-A-006 (MMH-anchor verbatim beats whole-radical composition; avoids double-transform aspect distortion per P-COMP-009).
# fresh_component: ru_char_from_mmh_anchors (all 6 strokes placed at MMH pixel coords, using stroke primitives)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "success_bank", "code")
sys.path.insert(0, _BANK)

from pie import draw_pie                       # noqa: E402
from heng import draw_heng                     # noqa: E402
from shu import draw_shu                       # noqa: E402
from heng_zhe_short import draw_heng_zhe_short # noqa: E402

_INK = (0, 0, 0)
_CELL = 100

_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}

def A(cell, xf, yf):
    col, row = _ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)


def _bezier_quad(p0, p1, p2, n):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0]
        y = u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts


def _taper(n, w_head, w_mid, w_tail):
    out = []
    for i in range(n + 1):
        t = i / n
        if t < 0.5:
            u = t / 0.5
            out.append(w_head * (1 - u) + w_mid * u)
        else:
            u = (t - 0.5) / 0.5
            out.append(w_mid * (1 - u) + w_tail * u)
    return out


def _stamp_chain(draw, pts, widths):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w = max(widths[i], widths[i + 1])
        dx, dy = x1 - x0, y1 - y0
        dist = (dx*dx + dy*dy) ** 0.5
        steps = max(1, int(dist / 0.8))
        for s in range(steps + 1):
            t = s / steps
            xs, ys = x0 + dx * t, y0 + dy * t
            r = max(0.5, w / 2.0)
            draw.ellipse([xs - r, ys - r, xs + r, ys + r], fill=_INK)


def _draw_pie_dian_compound(draw, head, corner, tail, mid_pie=None, mid_dian=None):
    """s1 of 女 = 撇点: pie from head→corner, then dian from corner→tail."""
    if mid_pie is None:
        mid_pie = ((head[0] + corner[0]) / 2 - 4, (head[1] + corner[1]) / 2)
    if mid_dian is None:
        mid_dian = ((corner[0] + tail[0]) / 2 + 8, (corner[1] + tail[1]) / 2 + 6)
    pie_pts = _bezier_quad(head, mid_pie, corner, 40)
    pie_w = _taper(40, 9.0, 8.0, 6.5)
    dian_pts = _bezier_quad(corner, mid_dian, tail, 50)
    dian_w = _taper(50, 6.0, 8.5, 6.0)
    _stamp_chain(draw, pie_pts, pie_w)
    _stamp_chain(draw, dian_pts, dian_w)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 女 (strokes 1-3) ----
    # s1: 撇点 compound. head TL(0.99, 0.665), tail BC(0.477, 0.739).
    # mid @ 0.43 = ML(0.916, 0.676); mid @ 0.79 = BC(0.106, 0.398).
    s1_head = A('TL', 0.99, 0.665)      # (99, 66.5)
    s1_mid_low = A('ML', 0.916, 0.676)  # (91.6, 167.6) — pie bottom / corner
    s1_mid_dian = A('BC', 0.106, 0.398) # (110.6, 239.8) — mid of dian
    s1_tail = A('BC', 0.477, 0.739)     # (147.7, 273.9)
    _draw_pie_dian_compound(draw, s1_head, s1_mid_low, s1_tail,
                            mid_pie=(85.0, 120.0),
                            mid_dian=s1_mid_dian)

    # s2: pie C(0.318,0.433) → BL(0.48,0.842)
    s2_head = A('C', 0.318, 0.433)  # (131.8, 143.3)
    s2_tail = A('BL', 0.48, 0.842)  # (48.0, 284.2)
    draw_pie(draw, s2_head, s2_tail, bow_perp=10, w_head=9, w_tail=3, steps=70)

    # s3: heng ML(0.229,0.746) → C(0.292,0.553) — short heng across mid of 女
    s3_head = A('ML', 0.229, 0.746)  # (22.9, 174.6)
    s3_tail = A('C', 0.292, 0.553)   # (129.2, 155.3)
    draw_heng(draw, s3_head, s3_tail, width_head=7, width_tail=8)

    # ---- 口 (strokes 4-6) ----
    # s4: 竖 C(0.635,0.661) → BC(0.863,0.473) — left | of 口
    s4_head = A('C', 0.635, 0.661)  # (163.5, 166.1)
    s4_tail = A('BC', 0.863, 0.473) # (186.3, 247.3)
    draw_shu(draw, s4_head, s4_tail, width=7)

    # s5: 横折 C(0.796,0.67) → BR(0.32,0.171) — top ─ + right | of 口
    s5_head = A('C', 0.796, 0.67)   # (179.6, 167.0)
    s5_tail = A('BR', 0.32, 0.171)  # (232.0, 217.1)
    draw_heng_zhe_short(draw, s5_head, s5_tail, corner_offset=(0, 4))

    # s6: bottom 横 BC(0.922,0.376) → BR(0.514,0.285)
    s6_head = A('BC', 0.922, 0.376) # (192.2, 237.6)
    s6_tail = A('BR', 0.514, 0.285) # (251.4, 228.5)
    draw_heng(draw, s6_head, s6_tail, width_head=7, width_tail=8)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_如.png")
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,          # side-by-side vs GT: 女 (left) + 口 (right) match; MMH-native lopsidedness of 口 mirrors GT
    'stroke_count_ok': True,    # 6 primitives: pie_dian_compound(s1) + pie(s2) + heng(s3) + shu(s4) + heng_zhe_short(s5) + heng(s6) = 6
    'endpoint_mismatches': [],  # all 6 head/tail pairs anchored verbatim to the MMH-supplied cells (delta 0 in x_frac, y_frac)
    'joint_class_mismatches': [], # P joints of s1↔s2 and s1↔s3 emerge from shared mid-point cells; N joints at 口 corners are natural pixel gaps
    'overall_pass': True,
    'notes': 'P-A-006 route: MMH-anchor verbatim + stroke primitives. Whole-radical primitives (nu_woman, kou_mouth) skipped per BANK_DEVIATION to avoid double-transform aspect distortion (P-COMP-009).',
}


if __name__ == "__main__":
    print(render())
