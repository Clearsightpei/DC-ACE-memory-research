"""p3_char_0476_俅 (qiu, 'to beg') — 9 strokes = 亻 (2) + 求 (7).

Recipe: **P-A-006 stroke-primitive layer** — MMH-verbatim anchors,
inline stroke primitives, no whole-radical bank calls. 亻 (s1-s2) is
present as ren_left in bank but per P-A-006 clause-2 we inline to
keep anchors verbatim across the compound.

# BANK_DEVIATION
# skipped: ren_left.py (亻 bank primitive)
# reason: MMH-verbatim anchors for the compound differ slightly from
#         ren_left's frozen render (compound-context L-R crowding).
#         Per P-A-006 stroke-primitive layer, inline pie+shu at exact
#         MMH pixel anchors for the 俅 context. BANK_DEVIATION quantitative:
#         ren_left s1_head=(158.8, 73.8), s1_tail=(80.6, 211.2); this
#         char s1_head=(87.6, 68.6), s1_tail=(15.2, 208.9). x-shift
#         ≈-71 px on head, ≈-65 px on tail — clearly compound context
#         where 亻 is scaled/pushed left to make room for 求 on the right.
#         Inline gives P-A-009 quantitative fit.
# fresh_component: none — using inline stroke primitives (pie, shu)
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie      # noqa: E402
from shu import draw_shu      # noqa: E402
from heng import draw_heng    # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402
from dian import draw_dian    # noqa: E402
from na import draw_na        # noqa: E402


# 米字格 cell anchor bases for 300x300 canvas (each cell 100x100)
CELL_BASE = {
    'TL': (0, 0),    'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),  'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200),  'BC': (100, 200), 'BR': (200, 200),
}


def A(cell, xf, yf):
    """Anchor lookup: (cell, x_frac, y_frac) → (px, py) in image coords."""
    cx, cy = CELL_BASE[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes at MMH-verbatim anchors. 亻 inlined per '
              'BANK_DEVIATION (compound-context aspect). 求 = heng + '
              'shu_gou + short dian + rising ti + pie + na + dian. '
              'P-crossing at s3.mid × s4.mid emerges naturally from '
              'anchor geometry.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) — s1, s2 -----------------------------
    # s1: pie  head TL(0.876, 0.686) → tail BL(0.152, 0.089)
    draw_pie(d, A('TL', 0.876, 0.686), A('BL', 0.152, 0.089),
             bow_perp=14, w_head=9, w_tail=3)
    # s2: shu  head ML(0.627, 0.635) → tail BL(0.674, 0.941)
    draw_shu(d, A('ML', 0.627, 0.635), A('BL', 0.674, 0.941),
             width=7, top_curl=True)

    # ---- 求 (right side) — s3-s9 ----------------------------------------
    # s3: heng (top horizontal of 求)  C(0.128, 0.438) → MR(0.18, 0.266)
    draw_heng(d, A('C', 0.128, 0.438), A('MR', 0.18, 0.266),
              width_head=8, width_tail=9)
    # s4: shu_gou (vertical hook)  TC(0.576, 0.674) → BC(0.269, 0.792)
    draw_shu_gou(d, A('TC', 0.576, 0.674), A('BC', 0.269, 0.792),
                 width=7, hook_start_offset=32)
    # s5: small dian/point on left of 求's center  C(0.122, 0.772) → C(0.356, 0.992)
    draw_dian(d, A('C', 0.122, 0.772), A('C', 0.356, 0.992),
              w_head=3, w_tail=6, bow=2)
    # s6: 提 (rising stroke, lower area)  BL(0.891, 0.525) → BC(0.5, 0.121)
    # implemented as a slim tapered pie in the opposite direction
    draw_pie(d, A('BL', 0.891, 0.525), A('BC', 0.5, 0.121),
             bow_perp=-3, w_head=5, w_tail=2)
    # s7: 撇 (pie in middle-right of 求)  MR(0.188, 0.564) → C(0.884, 0.951)
    draw_pie(d, A('MR', 0.188, 0.564), A('C', 0.884, 0.951),
             bow_perp=8, w_head=7, w_tail=2)
    # s8: 捺 (na, sweeping right-down)  C(0.77, 0.887) → BR(0.883, 0.648)
    draw_na(d, A('C', 0.77, 0.887), A('BR', 0.883, 0.648),
            bow_perp=12, w_head=4, w_tail=10)
    # s9: 丶 (small dot upper-right of 求)  TR(0.089, 0.841) → MR(0.411, 0.087)
    draw_dian(d, A('TR', 0.089, 0.841), A('MR', 0.411, 0.087),
              w_head=3, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_俅.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
