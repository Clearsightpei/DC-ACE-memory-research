"""p3_char_0299_里 — 7 strokes, MMH-anchor stroke-primitive layer.

Structure: 日 on top (s1-s4) stacked over 土-like bottom (s5-s7).
s5 is the central 竖 that pierces s3, s4, s6 (three P-welds) and
has an N-gap to s7 (the long bottom heng).

Recipe: P-A-006 stroke-primitive layer with MMH anchors verbatim.
Whole-radical draw_ri/draw_tu don't fit 里's compressed proportions
(日 shrinks to ~90px tall, 土 widens; central 竖 shared between the
two visual halves), so we inline every stroke with anchor endpoints.

# BANK_DEVIATION
# skipped: ri_sun.py, tu_earth.py
# reason: 里 compresses 日 vertically (~90px tall vs 190 native) and
#         shares a central 竖 across 日+土 halves — whole-radical primitives
#         would overshoot P-A-007 guardrail. Inline strokes at MMH anchors.
# fresh_component: li_seven_stroke_stack (not a reusable sub-element by itself)
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 7 primitive calls (shu, heng_zhe_box, heng, heng, shu, heng, heng)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes via stroke-primitive layer at MMH anchors (y-down conv). '
             's5 central shu pierces s3/s4/s6 (three P-welds naturally satisfied '
             'because s5 spans y=95..265 covering all three heng y-values). '
             's7 (long bottom heng) at y=276 sits below s5 tail → N-gap preserved.',
}


def _anchor(cell, xf, yf):
    xoff = {'TL': 0, 'TC': 100, 'TR': 200,
            'CL': 0, 'C': 100, 'CR': 200,
            'BL': 0, 'BC': 100, 'BR': 200}[cell]
    yoff = {'TL': 0, 'TC': 0, 'TR': 0,
            'CL': 100, 'C': 100, 'CR': 100,
            'BL': 200, 'BC': 200, 'BR': 200}[cell]
    return (xoff + xf * 100, yoff + yf * 100)


def draw_li_inside(d: ImageDraw.ImageDraw):
    # s1: left 竖 of 日 box.  TL(0.706, 0.902) -> C(0.061, 0.866)
    s1_h = _anchor('TL', 0.706, 0.902)
    s1_t = _anchor('C',  0.061, 0.866)
    draw_shu(d, s1_h, s1_t, width=8)

    # s2: 横折 top+right of 日 box.  TL(0.855, 0.911) -> C(0.969, 0.834)
    s2_h = _anchor('TL', 0.855, 0.911)
    s2_t = _anchor('C',  0.969, 0.834)
    draw_heng_zhe_box(d, s2_h, s2_t, width=8)

    # s3: middle heng inside 日.  C(0.166, 0.359) -> C(0.834, 0.283)
    s3_h = _anchor('C', 0.166, 0.359)
    s3_t = _anchor('C', 0.834, 0.283)
    draw_heng(d, s3_h, s3_t, width_head=7, width_tail=8)

    # s4: bottom heng of 日 (closes box).  C(0.113, 0.734) -> C(0.86, 0.658)
    s4_h = _anchor('C', 0.113, 0.734)
    s4_t = _anchor('C', 0.86, 0.658)
    draw_heng(d, s4_h, s4_t, width_head=8, width_tail=9)

    # s5: central 竖 piercing s3/s4/s6.  TC(0.351, 0.955) -> BC(0.4, 0.646)
    s5_h = _anchor('TC', 0.351, 0.955)
    s5_t = _anchor('BC', 0.4,   0.646)
    draw_shu(d, s5_h, s5_t, width=8)

    # s6: middle heng of 土 half.  BL(0.958, 0.247) -> BR(0.024, 0.156)
    s6_h = _anchor('BL', 0.958, 0.247)
    s6_t = _anchor('BR', 0.024, 0.156)
    draw_heng(d, s6_h, s6_t, width_head=8, width_tail=9)

    # s7: bottom LONG heng.  BL(0.343, 0.804) -> BR(0.76, 0.716)
    s7_h = _anchor('BL', 0.343, 0.804)
    s7_t = _anchor('BR', 0.76,  0.716)
    draw_heng(d, s7_h, s7_t, width_head=10, width_tail=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_li_inside(d)
    out = os.path.join(os.path.dirname(__file__), '01_里.png')
    img.save(out)
    print('WROTE', out)


if __name__ == '__main__':
    main()
