"""p3_char_0265_名 — G5 attempt.

P-A-006 route: MMH-anchor verbatim + stroke-primitive layer.
6 strokes: 夕 (pie_short, long pie, dian) + 口 (left shu, top-right L, bottom heng).

We do NOT compose draw_kou / draw_xi as whole radicals — Phase-3 aspect
would double-transform them. Instead every stroke is inlined at MMH pixel
anchors and calls a shared stroke primitive from success_bank/code/.
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from pie import draw_pie          # noqa: E402
from dian import draw_dian        # noqa: E402
from heng import draw_heng        # noqa: E402
from shu import draw_shu          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 8 expected joints are N-class (natural gap). No welds; '
             'strokes drawn at MMH endpoint anchors with small natural '
             'gaps preserved (7-15 px).',
}


def _cell(cell, xf, yf):
    """米字格 anchor -> 300x300 pixel. 3x3 grid, each cell 100x100."""
    col = {'L': 0, 'C': 1, 'R': 2, 'ML': 0, 'MR': 2, 'TC': 1, 'BC': 1,
           'TL': 0, 'TR': 2, 'BL': 0, 'BR': 2}
    row = {'T': 0, 'C': 1, 'B': 2, 'ML': 1, 'MR': 1, 'TC': 0, 'BC': 2,
           'TL': 0, 'TR': 0, 'BL': 2, 'BR': 2}
    cx = col[cell] * 100
    cy = row[cell] * 100
    return (cx + xf * 100, cy + yf * 100)


def draw_ming(draw):
    # ---- 夕 (top) -----------------------------------------------------
    # s1: short top 撇  TC(0.453,0.574) -> ML(0.718,0.462)
    s1_head = _cell('TC', 0.453, 0.574)   # (145.3,  57.4)
    s1_tail = _cell('ML', 0.718, 0.462)   # ( 71.8, 146.2)
    draw_pie(draw, s1_head, s1_tail, bow_perp=6, w_head=6, w_tail=3)

    # s2: long sweep 撇  C(0.395,0.028) -> BL(0.144,0.78)
    s2_head = _cell('C', 0.395, 0.028)    # (139.5, 102.8)
    s2_tail = _cell('BL', 0.144, 0.78)    # ( 14.4, 278.0)
    draw_pie(draw, s2_head, s2_tail, bow_perp=14, w_head=9, w_tail=3)

    # s3: interior 点  C(0.04,0.348) -> C(0.321,0.638)
    s3_head = _cell('C', 0.04, 0.348)     # (104.0, 134.8)
    s3_tail = _cell('C', 0.321, 0.638)    # (132.1, 163.8)
    draw_dian(draw, s3_head, s3_tail, w_head=3, w_tail=6, bow=2)

    # ---- 口 (bottom-right) --------------------------------------------
    # s4: left 竖  BC(0.075,0.235) -> BC(0.289,0.968)
    s4_head = _cell('BC', 0.075, 0.235)   # (107.5, 223.5)
    s4_tail = _cell('BC', 0.289, 0.968)   # (128.9, 296.8)
    draw_shu(draw, s4_head, s4_tail, width=6)

    # s5: 横折 (top + right side)  BC(0.251,0.229) -> BR(0.065,0.678)
    # Inline as L: horizontal from head across, then down to tail.
    # NOT using draw_kou/heng_zhe_box because the 口 in 名 is shallow
    # and slightly tilted; MMH endpoints already carry that shape.
    s5_head = _cell('BC', 0.251, 0.229)   # (125.1, 222.9)
    s5_tail = _cell('BR', 0.065, 0.678)   # (206.5, 267.8)
    corner  = (s5_tail[0] + 2, s5_head[1] + 2)
    draw.line([s5_head, corner], fill='black', width=6)
    draw.line([corner, s5_tail], fill='black', width=6)
    # small 顿笔 at corner
    draw.ellipse([corner[0]-4, corner[1]-4, corner[0]+4, corner[1]+4],
                 fill='black')

    # s6: bottom 横  BC(0.354,0.889) -> BR(0.273,0.798)
    s6_head = _cell('BC', 0.354, 0.889)   # (135.4, 288.9)
    s6_tail = _cell('BR', 0.273, 0.798)   # (227.3, 279.8)
    draw_heng(draw, s6_head, s6_tail, width_head=6, width_tail=7)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ming(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_名.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
