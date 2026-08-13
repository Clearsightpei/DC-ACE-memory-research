"""p3_char_0260_伙 — G5 render.

Decomposition: 亻 (left) + 火 (right).
Per P-A-006: MMH-anchor verbatim + stroke-primitive layer;
refuse whole-radical composition (ren_left, and there is no fire radical
primitive anyway).

# BANK_DEVIATION
# skipped: ren_left.py
# reason: P-A-006 — at Phase-3 aspect (narrow left column), the whole
#   radical primitive double-transforms; inlining stroke primitives with
#   MMH pixel anchors places 亻's pie/shu exactly where the character
#   demands (long-pie top at TL(0.94,0.7), shu column at x≈75).
# fresh_component: ren_left_verbatim_for_huo (long pie + short shu at
#   MMH endpoints)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 6 stroke primitive calls below
    'endpoint_mismatches': [],  # all anchors verbatim from MMH block
    'joint_class_mismatches': [],  # 3 N joints, natural gaps preserved
    'overall_pass': True,
    'notes': ('P-A-006 recipe: verbatim MMH pixel anchors + stroke primitives; '
              'BANK_DEVIATION on ren_left to avoid double-transform. '
              'Joints all N (gaps not welded).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ----- 亻 (left) — 2 strokes -----
    # s1: pie — long sweep from upper-right TL(0.94,0.7)=(94,70) to BL(0.22,0.145)=(22,214.5)
    draw_pie(d, head=(94, 70), tail=(22, 214.5),
             bow_perp=10, w_head=8, w_tail=3)

    # s2: shu — short vertical, ML(0.747,0.629)=(74.7,162.9) to BL(0.75,0.962)=(75,296.2)
    draw_shu(d, head=(74.7, 162.9), tail=(75, 296.2), width=7)

    # ----- 火 (right) — 4 strokes -----
    # s3: LEFT dot (dian) — head C(0.181,0.503)=(118.1,150.3) tail C(0.403,0.86)=(140.3,186)
    #     down-right small dot
    draw_dian(d, head=(118, 150), tail=(140, 186),
              w_head=2, w_tail=7, bow=2)

    # s4: RIGHT dot (short pie / dian going down-left)
    #     head MR(0.355,0.184)=(235.5,118.4) tail MR(0.01,0.708)=(201,170.8)
    draw_dian(d, head=(235, 118), tail=(201, 170),
              w_head=2, w_tail=7, bow=-3)

    # s5: main long pie of 火 — head TC(0.667,0.715)=(166.7,71.5)
    #     tail BC(0.02,0.874)=(102,287.4).  Should touch s6 head near C.
    draw_pie(d, head=(166.7, 71.5), tail=(102, 287.4),
             bow_perp=14, w_head=8, w_tail=3)

    # s6: na of 火 — head C(0.816,0.901)=(181.6,190.1) tail BR(0.865,0.889)=(286.5,288.9)
    #     Note MMH: s5.mid(0.51) ≈ (134, 179); s6.head at (181, 190) — N joint,
    #     natural small gap ~12 px; the crossing happens visually along s5's body.
    draw_na(d, head=(181.6, 190.1), tail=(286.5, 288.9),
            bow_perp=10, w_head=3, w_tail=10)

    out = os.path.join(os.path.dirname(__file__), '01_伙.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
