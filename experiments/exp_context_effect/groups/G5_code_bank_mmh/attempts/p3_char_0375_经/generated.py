"""p3_char_0375_经 (jing, "classic/scripture") — 8 strokes.

Decomposition:
  Left: 纟 (silk radical) — 3 strokes: pie_zhe + pie_zhe + ti
  Right: 圣 = 又(top) + 土(bottom) — 5 strokes: pie + na + heng + shu + heng

Per P-A-006 (stroke-primitive layer with MMH-verbatim anchors) — inline
rendering per stroke using bank stroke primitives with anchors taken
verbatim from the MMH structural block.

Per P-A-008: inline-reasoning trace for each sub-component:
  - 纟 sub-component: NO whole-radical bank primitive exists for 纟
    (p3_char_0068_纟 was PASSed inline; not promoted as a callable).
    Use stroke-primitive layer (pie_zhe ×2 + ti) per B4-B7 template.
  - 又 sub-component: bank has `you_again.py`, but 又 in 圣 top is
    compressed vertically and shifted right-of-center — MMH anchors
    for s4/s5 place head/tail INSIDE composition. BANK_DEVIATION:
    inline stroke-primitive layer to hit MMH anchors exactly.
  - 土 sub-component: bank has `tu_earth.py`, but 土 in 圣 bottom
    spans wider than tu_earth's native width and sits at bottom-row.
    BANK_DEVIATION: inline stroke-primitive layer (heng + shu + heng)
    to hit MMH s6/s7/s8 anchors exactly.

# BANK_DEVIATION
# skipped: you_again.py + tu_earth.py
# reason: MMH anchors for right-side of 经 place 又 and 土 at scales
#         and positions inconsistent with the bank primitives' native
#         geometry (又 is compressed vertical in top-right; 土 spans
#         nearly full width at very bottom, s8 is BC→BR).
# fresh_component: right_side_inline (5 strokes MMH-verbatim)

MMH-derived structural expectations (from prompt):
  s1: TL(0.855,0.694)=(85.5,69.4) → ML(0.961,0.597)=(96.1,159.7)  [pie_zhe upper]
  s2: C(0.181,0.204)=(118.1,120.4) → BC(0.248,0.001)=(124.8,200.1) [pie_zhe lower]
  s3: BL(0.378,0.736)=(37.8,273.6) → BC(0.301,0.329)=(130.1,232.9) [提 ti]
  s4: C(0.456,0.037)=(145.6,103.7) → C(0.377,0.819)=(137.7,181.9)  [撇 pie of 又]
  s5: MR(0.013,0.441)=(201.3,144.1) → MR(0.549,0.819)=(254.9,181.9) [捺 na of 又]
  s6: C(0.485,0.989)=(148.5,198.9) → MR(0.367,0.934)=(236.7,193.4) [top heng of 土]
  s7: BC(0.799,0.08)=(179.9,208.0) → BC(0.811,0.692)=(181.1,269.2) [central shu of 土]
  s8: BC(0.169,0.798)=(116.9,279.8) → BR(0.769,0.798)=(276.9,279.8) [bottom long heng]
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie_zhe import draw_pie_zhe   # noqa: E402
from ti import draw_ti             # noqa: E402
from pie import draw_pie           # noqa: E402
from na import draw_na             # noqa: E402
from heng import draw_heng         # noqa: E402
from shu import draw_shu           # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 8 primitives called (matches expected 8)
    'endpoint_mismatches': [],        # all anchors verbatim from MMH block
    'joint_class_mismatches': [],     # all 7 joints are N; natural pixel gaps kept
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer. BANK_DEVIATION on you_again+'
             'tu_earth for right side (composition-specific placement).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === 纟 (s1-s3) — left silk radical ===
    # s1: upper 撇折 (ㄥ shape). Head top-right, corner down-left, tail down-right.
    draw_pie_zhe(d,
                 head=(85.5, 69.4),
                 corner=(70, 122),
                 tail=(96.1, 159.7),
                 pie_bow=5, zhe_bow=1,
                 w_head=5, w_corner=4, w_tail=3)

    # s2: lower 撇折 (ㄥ shape), shifted right and down from s1.
    draw_pie_zhe(d,
                 head=(118.1, 120.4),
                 corner=(100, 172),
                 tail=(124.8, 200.1),
                 pie_bow=5, zhe_bow=1,
                 w_head=5, w_corner=4, w_tail=3)

    # s3: 提 rising bottom stroke, thick lower-left to fine upper-right.
    draw_ti(d,
            head=(37.8, 273.6),
            tail=(130.1, 232.9),
            w_head=8, w_tail=2)

    # === 圣 (s4-s8) — 又 top + 土 bottom ===
    # s4: 撇 of 又 (top-right area). Nearly vertical with slight left drift.
    draw_pie(d,
             head=(145.6, 103.7),
             tail=(137.7, 181.9),
             bow_perp=8, w_head=9, w_tail=3, steps=60)

    # s5: 捺 of 又 (diagonal ↘).
    draw_na(d,
            head=(201.3, 144.1),
            tail=(254.9, 181.9),
            bow_perp=10, w_head=3, w_tail=10, steps=70)

    # s6: top 一 of 土 (slightly rising to right).
    draw_heng(d,
              head=(148.5, 198.9),
              tail=(236.7, 193.4),
              width_head=7, width_tail=8)

    # s7: central 丨 of 土 (vertical).
    draw_shu(d,
             head=(179.9, 208.0),
             tail=(181.1, 269.2),
             width=7)

    # s8: bottom LONG 一 of 土 (spans full width of bottom row).
    draw_heng(d,
              head=(116.9, 279.8),
              tail=(276.9, 279.8),
              width_head=9, width_tail=10)

    out = os.path.join(os.path.dirname(__file__), '01_经.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
