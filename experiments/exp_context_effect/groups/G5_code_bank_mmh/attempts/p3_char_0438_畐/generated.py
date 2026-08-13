"""p3_char_0438_畐 (fu, "brimful") — 9 strokes.

Structure (top-to-bottom): 一 (short top heng) + 口 (small mouth, 3 strokes)
+ 田 (field, 5 strokes).

Reasoning trace (P-A-008):
- draw_kou natural box is ~133×153 px which at even scale=0.75 renders 115 px
  tall — too big for the small middle 口 in 畐 (which visually sits at ~70 px
  tall in the GT). Skip draw_kou; inline 口 with 3 stroke primitives at target
  footprint for exact aspect control.
- 田 has no direct bank primitive. Inline 5-stroke 田 from shu + heng_zhe_box
  + middle heng + middle shu + bottom heng.
- Top 一: short heng.

BANK_DEVIATION
# skipped: kou_mouth.py, hui_return.py
# reason: kou_mouth's natural aspect (~133 wide × 153 tall = w/h ≈ 0.87) is
#   TALLER than the middle 口 in 畐 which is visually WIDER-than-tall
#   (~100 × 65 = w/h ≈ 1.54 from GT). Scaling kou uniformly can't hit both
#   dimensions; anisotropic re-inlining needed. hui_return is nested-口 not
#   stacked 口+田, wrong composition entirely.
# fresh_component: kou_wide_shallow_for_畐 (3-stroke inline 口 tuned to
#   w:h ≈ 1.5, and tian_inline_for_畐 (5-stroke inline 田).

SELF_CHECK reported at the bottom of the file.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '..', '..', 'success_bank', 'code')))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: top 一 (short horizontal centered) ----
    draw_heng(d, (108, 55), (200, 60), width_head=8, width_tail=10)

    # ---- s2, s3, s4: middle 口 (inlined, wide + shallow) ----
    # Footprint: x[100, 200], y[75, 148]  → width 100, height 73.
    KL, KR, KT, KB = 100, 200, 75, 148
    # s2 left 丨
    draw_shu(d, (KL + 2, KT + 2), (KL - 2, KB), width=7)
    # s3 top+right 横折
    draw_heng_zhe_box(d, (KL + 6, KT), (KR, KB - 2), width=7)
    # s4 bottom 一 closing
    draw_heng(d, (KL - 2, KB), (KR - 2, KB - 3), width_head=7, width_tail=8)

    # ---- s5, s6, s7, s8, s9: 田 (bottom field, 5 strokes inlined) ----
    # Box footprint: x[72, 226], y[162, 285]. Larger than the 口 above.
    TL, TR = 72, 226
    TT, TB = 162, 285
    MIDX = (TL + TR) // 2  # 149
    MIDY = (TT + TB) // 2  # 223

    # s5 left 丨 (shu)
    draw_shu(d, (TL + 2, TT + 2), (TL - 2, TB), width=8)
    # s6 top+right 横折 (heng_zhe_box)
    draw_heng_zhe_box(d, (TL + 6, TT), (TR, TB - 2), width=8)
    # s7 middle 一 (crosses full box)
    draw_heng(d, (TL + 4, MIDY), (TR - 6, MIDY - 2),
              width_head=7, width_tail=8)
    # s8 middle 丨 (crosses full box, welded to s7 → P joint)
    draw_shu(d, (MIDX, TT + 4), (MIDX, TB - 4), width=7)
    # s9 bottom 一 (closes the box)
    draw_heng(d, (TL - 2, TB), (TR - 2, TB - 4),
              width_head=8, width_tail=10)

    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 1 (top heng) + 3 (kou) + 5 (tian) = 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s7.mid ⇆ s8.mid welded (P); others N by geometry
    'overall_pass': True,
    'notes': ('Inlined both 口 and 田 for anisotropic control. Top 一 is short. '
              'Middle 口 wide+shallow; bottom 田 wider + full-height with '
              'welded middle cross.'),
}


if __name__ == '__main__':
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img = draw()
    img.save(os.path.join(out_dir, '01_畐.png'))
    print('wrote 01_畐.png')
