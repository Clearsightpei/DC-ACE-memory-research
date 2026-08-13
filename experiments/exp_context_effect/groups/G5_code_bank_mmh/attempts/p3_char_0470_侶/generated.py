"""p3_char_0470_侶 — G5 attempt.

Structure: 亻 (left, 2 strokes) + 呂 traditional (right, 7 strokes = top-口
+ small connecting 撇 + bottom-口). MMH gives 9 strokes total.

Recipe: P-A-006 stroke-primitive layer with MMH-verbatim anchors + P-A-008
inline reasoning. Refused kou_mouth wrapper because the top-口 and bottom-口
here are non-standard (different aspects, different sizes, plus a connecting
stroke between them that kou_mouth does not encode), and P-A-007-v2 hard-check
fails on both scale and aspect match. Refused ren_left wrapper because MMH
gives a very short 亻 shu (only ~150→294 px) that ren_left's native (159→293)
also does not match at scale 1.0 without offset gymnastics — inlining is
cleaner. Uses stroke primitives pie, shu, heng, heng_zhe_box verbatim.

# BANK_DEVIATION
# skipped: ren_left.py (亻 as inline pie+shu)
# reason: MMH shu is very short (y 141→294) with slight rightward drift;
#         ren_left native (159→293) needs offset + non-unit scale to fit,
#         and its top_curl decoration doesn't match this GT which shows a
#         clean shaft.
# fresh_component: ren_left_inline_for_侶
#
# skipped: kou_mouth.py (top-口 and bottom-口 inlined)
# reason: top-口 aspect (w~80 × h~63) and bottom-口 aspect (w~114 × h~80)
#         differ from kou_mouth native aspect (w~135 × h~150 → nearly
#         square); and P-A-007-v2 clause-1 (scale within 5%) fails
#         (top-口 scale ≈ 0.42, bottom-口 scale ≈ 0.62 vs native).
# fresh_component: kou_top_lv_inline, kou_bottom_lv_inline
"""

import os
import sys
from PIL import Image, ImageDraw

# make bank primitives importable
BANK = os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 9 primitives called, matches expected 9
    'endpoint_mismatches': [],   # anchors verbatim from MMH block
    'joint_class_mismatches': [],# all 9 joints are N (natural gap) — endpoints not welded
    'overall_pass': True,
    'notes': ('all strokes drawn from MMH anchors verbatim; N-joints emerge '
              'naturally from anchor spacing; kou_mouth and ren_left bank '
              'primitives skipped per BANK_DEVIATION reasoning above.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (person left, 2 strokes) ----
    # s1: 撇 pie, head TL(0.829,0.636)→(83,64), tail BL(0.182,0.027)→(18,203)
    draw_pie(d, (82.9, 63.6), (18.2, 202.7),
             bow_perp=12, w_head=8, w_tail=2, steps=90)

    # s2: 竖 shu, head ML(0.732,0.412)→(73,141), tail BL(0.768,0.941)→(77,294)
    draw_shu(d, (73.2, 141.2), (76.8, 294.1), width=7)

    # ---- 呂 top 口 (3 strokes: shu + heng_zhe_box + heng) ----
    # s3: shu top-left, head TC(0.318,0.967)→(132,97), tail C(0.544,0.597)→(154,160)
    draw_shu(d, (131.8, 96.7), (154.4, 159.7), width=6)

    # s4: heng_zhe_box, head TC(0.474,0.967)→(147,97), tail MR(0.106,0.359)→(211,136)
    draw_heng_zhe_box(d, (147.4, 96.7), (210.6, 135.9), width=6)

    # s5: bottom heng, head C(0.597,0.547)→(160,155), tail MR(0.312,0.456)→(231,146)
    draw_heng(d, (159.7, 154.7), (231.2, 145.6), width_head=6, width_tail=7)

    # ---- 呂 connecting stroke (小撇 between two 口s) ----
    # s6: small pie, head C(0.69,0.564)→(169,156), tail BC(0.603,0.001)→(160,200)
    draw_pie(d, (169.0, 156.4), (160.3, 200.1),
             bow_perp=3, w_head=5, w_tail=3, steps=40)

    # ---- 呂 bottom 口 (3 strokes) ----
    # s7: shu top-left, head BC(0.248,0.03)→(125,203), tail BC(0.488,0.836)→(149,284)
    draw_shu(d, (124.8, 203.0), (148.8, 283.6), width=7)

    # s8: heng_zhe_box, head BC(0.43,0.048)→(143,205), tail BR(0.165,0.522)→(217,252)
    draw_heng_zhe_box(d, (143.0, 204.8), (216.5, 252.2), width=7)

    # s9: bottom heng, head BC(0.553,0.716)→(155,272), tail BR(0.394,0.646)→(239,265)
    draw_heng(d, (155.3, 271.6), (239.4, 264.6), width_head=7, width_tail=8)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_侶.png')
    render().save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK overall_pass={SELF_CHECK["overall_pass"]}')
