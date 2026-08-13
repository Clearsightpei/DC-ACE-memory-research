"""p3_char_0415_转 — G5 attempt (8 strokes).

转 = 车 (left radical, 4 strokes) + 专 (right, 4 strokes).

BANK_DEVIATION vs che_car whole-radical:
- native che_car spans x=33..267 (width=234); target 车-radical here spans
  x≈25..127 (width≈102). Aspect ratio 102/234 = 0.44, well below P-A-007-v2
  threshold [0.55, 1.2]. Also stroke morphology differs: standalone 车 has
  bottom-heng (s3 of che_car), radical form has ti (rising) instead.
- Decision: DO NOT call draw_che; inline 4 strokes per MMH endpoints.
- fresh_component: che_left_compressed_for_zhuan (could be reused for
  软/连/轻/较/较-family).

BANK_DEVIATION vs (no zhuan primitive exists) for 专: no bank entry;
inline s5-s8 per MMH endpoints. 专 is 4 strokes: 2 short heng + long
vertical spine + bottom diagonal sweep.

Per-sub-component reasoning trace (P-A-008):
  - 车-radical (s1-s4): compressed to left half. s1 top heng, s2 pie-like
    diagonal (compound 撇折 median), s3 long shu spine, s4 ti rising.
  - 专 (s5-s8): s5 short top heng, s6 long crossing heng, s7 long right
    spine, s8 short bottom diagonal (the tail of the final compound).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from heng import draw_heng
from pie import draw_pie
from pie_zhe import draw_pie_zhe
from shu import draw_shu
from ti import draw_ti


SELF_CHECK = {
    'visual_ok': None,           # to fill after render
    'stroke_count_ok': True,     # 8 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'BANK_DEVIATION vs che_car (aspect 0.44 < 0.55); '
             '专 has no bank entry; inline both from MMH anchors.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 车 radical (compressed left) ----
    # s1 top short heng (up-slanted)
    draw_heng(draw, head=(42, 121), tail=(127, 109),
              width_head=7, width_tail=8)
    # s2 撇折 compound (pie down-left, then short zhe right)
    draw_pie_zhe(draw, head=(82, 65),
                 corner=(70, 168),
                 tail=(122, 176),
                 pie_bow=6, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=5)
    # s3 long central shu (spine of 车-radical)
    draw_shu(draw, head=(90, 144), tail=(96, 295),
             width=7)
    # s4 ti (rising stroke, replaces bottom heng in radical form)
    draw_ti(draw, head=(25, 239), tail=(124, 207),
            w_head=9, w_tail=2)

    # ---- 专 (right half) ----
    # s5 short top heng
    draw_heng(draw, head=(144, 137), tail=(232, 122),
              width_head=6, width_tail=7)
    # s6 long crossing heng
    draw_heng(draw, head=(127, 185), tail=(266, 171),
              width_head=8, width_tail=9)
    # s7 long right spine (nearly vertical, from top to bottom)
    draw_shu(draw, head=(176, 64), tail=(196, 269),
             width=7)
    # s8 bottom diagonal sweep (final tail of 专 — clip tail to canvas)
    draw_pie(draw, head=(163, 252), tail=(211, 298),
             bow_perp=4, w_head=6, w_tail=4)

    out = os.path.join(os.path.dirname(__file__), '01_转.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
