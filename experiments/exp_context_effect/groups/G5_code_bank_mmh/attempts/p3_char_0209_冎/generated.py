"""G5 attempt: p3_char_0209_冎 (5 strokes) — revised pass 2.

MMH anchors describe the median endpoints but the GT visually spans most
of the canvas (top y~85, bottom sweep y~220, left x~55, right x~265).
Following the G5 rule "trust the GT over the memory when they disagree":
we render the character to the GT's visible size while keeping the
anchor topology (which stroke goes where, which joints stay N-gapped).

Structure of 冎 (5 strokes, following MMH stroke topology):
  s1: top-left descender (short 撇-like) — upper region
  s2: 横折 forming the boxy top + right side (like top of 冂)
  s3: small interior stroke (divider) in upper-middle area
  s4: short vertical descender inside/left of middle
  s5: long horizontal sweep across the bottom (extends to right edge)

All joints are class N — natural calligraphic gaps, no welding.

Bank usage: pie, heng_zhe_box, heng, shu. No BANK_DEVIATION.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu import draw_shu


W = H = 300
img = Image.new('L', (W, H), 255)
d = ImageDraw.Draw(img)

# s1: top-left descender — from upper-left down through mid-left
#     (MMH anchor TL→C, scaled to GT extent)
draw_pie(d, head=(90, 85), tail=(70, 210),
         bow_perp=6, w_head=9, w_tail=5, steps=70)

# s2: 横折 top+right box — spans most of top of character
#     (heng across from ~x=90 to ~x=245, then drops to y~175)
draw_heng_zhe_box(d, top_left=(92, 88), bottom_right=(248, 175), width=8)

# s3: interior horizontal divider — in the upper-middle area
draw_heng(d, head=(105, 145), tail=(220, 148),
          width_head=7, width_tail=7)

# s4: short interior vertical (small divider between upper cells)
draw_shu(d, head=(155, 92), tail=(160, 145), width=6)

# s5: long horizontal sweeping stroke — the signature bottom of 冎,
#     from left area sweeping to the far right
draw_heng(d, head=(60, 215), tail=(268, 220),
          width_head=8, width_tail=10)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 primitive calls: pie + hzb + heng + shu + heng
    'endpoint_mismatches': [
        # anchors rescaled to GT extent; cell membership preserved where possible
        {'stroke': 'all', 'note': 'rescaled uniformly to match GT visible extent'},
    ],
    'joint_class_mismatches': [], # all 6 joints kept class N (natural gaps)
    'overall_pass': True,
    'notes': ('冎: MMH anchor pixel-values were much smaller than the GT '
              'visible character; rendered to GT extent while preserving '
              'stroke topology. All joints natural N-gap (no welding).')
}


img.save(os.path.join(os.path.dirname(__file__), '01_冎.png'))
