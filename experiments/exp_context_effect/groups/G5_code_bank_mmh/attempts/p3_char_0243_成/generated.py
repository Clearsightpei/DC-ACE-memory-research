"""p3_char_0243_成 — 成 (cheng, "become") — 6 strokes.

Composition strategy: 成 is essentially 戈 (heng + xie_gou + pie + dian)
plus an inner short pie and a small stubby stroke. Bank has ge_dagger.py
(4-stroke 戈) but 成's proportions differ (heng shifted, xie_gou
starts higher, added strokes 3 and 5). Rather than call draw_ge and
patch, use the individual stroke primitives with MMH-verbatim anchors
per P-A-006.

Strokes (MMH anchors → pixel):
  s1: heng (short, rising top)         (90.5, 147.4) → (208.9, 124.8)
  s2: pie (long down-left)             (67.7, 142.1) → (28.4, 291.2)
  s3: short stub (near-vertical)       (87.9, 205.7) → (95.8, 252.5)
  s4: xie_gou (long diag + hook)       (132.4, 53.6) → (274.8, 248.1)
  s5: inner pie                        (211.5, 164.4) → (146.2, 272.8)
  s6: dian at upper right              (191.3, 72.4)  → (223.5, 92.6)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from xie_gou import draw_xie_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all four joints intended per MMH
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors + stroke primitives per P-A-006 recipe. '
             'xie_gou crosses s1 near C cell (P weld). s5 crosses s4 near BC (P weld).'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng, rising slightly (head lower-left, tail upper-right)
    draw_heng(d, (90.5, 147.4), (208.9, 124.8),
              width_head=8, width_tail=9)

    # s2: long pie from mid-top-left descending to bottom-left, right bow
    draw_pie(d, (67.7, 142.1), (28.4, 291.2),
             bow_perp=14, w_head=9, w_tail=3)

    # s3: short stubby stroke at lower-left (near-vertical, tiny)
    # rendered as a small tapered dian-like segment
    draw_dian(d, (87.9, 205.7), (95.8, 252.5),
              w_head=3, w_tail=6, bow=2)

    # s4: xie_gou — long diagonal from upper-mid to lower-right + up hook
    draw_xie_gou(d, head=(132.4, 53.6), tail=(274.8, 248.1),
                 width=8, bow=10, hook_up=34, hook_back=6)

    # s5: inner pie — from mid-right descending down-left to bottom-center
    draw_pie(d, (211.5, 164.4), (146.2, 272.8),
             bow_perp=10, w_head=8, w_tail=3)

    # s6: dian at upper-right (thin head → thicker tail, curved bow)
    draw_dian(d, (191.3, 72.4), (223.5, 92.6),
              w_head=2, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_成.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
