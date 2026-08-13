"""p2_radical_117_手 — 4-stroke radical.

MMH structural expectations:
  s1: TR(0.039, 0.724) -> TL(0.92, 0.979)      (204, 72)  -> (92, 98)   top pie/curve
  s2: ML(0.935, 0.351) -> MR(0.051, 0.213)     (94, 135)  -> (205, 121) upper short heng
  s3: ML(0.325, 0.939) -> MR(0.713, 0.793)     (33, 194)  -> (271, 179) long middle heng
  s4: TC(0.389, 0.92)  -> BC(0.09, 0.763)      (139, 92)  -> (109, 276) shu_gou (curls left)

Joints:
  s1.mid65 ~ s4.head  @ TC : N (small ~11px gap - natural, no weld)
  s2.mid55 ~ s4.mid17 @ C  : P (piercing — computed intersection ~ (133, 130))
  s3.mid54 ~ s4.mid38 @ C  : P (piercing — computed intersection ~ (123, 188))

Bank usage:
  draw_pie      for s1 (short top curve, bows upward)
  draw_heng     for s2 and s3
  draw_shu_gou  for s4

Pre-submit self-check dict at bottom.
"""

import sys
import pathlib

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie
from heng import draw_heng
from shu_gou import draw_shu_gou


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- MMH-derived anchors (px) ----
    s1_head, s1_tail = (204, 72), (92, 98)
    s2_head, s2_tail = (94, 135), (205, 121)
    s3_head, s3_tail = (33, 194), (271, 179)
    s4_head, s4_tail = (139, 92), (109, 276)

    # ---- s1: top pie (short, curves upward — leftward sweep) ----
    # bow_perp positive with a right-to-left travel direction gives an
    # upward-arching curve (see pie.py convention).
    draw_pie(d, s1_head, s1_tail, bow_perp=10, w_head=8, w_tail=4, steps=60)

    # ---- s2: upper short heng ----
    draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

    # ---- s3: long middle heng ----
    draw_heng(d, s3_head, s3_tail, width_head=9, width_tail=10)

    # ---- s4: shu_gou (vertical body curling left at tail) ----
    draw_shu_gou(d, s4_head, s4_tail, width=8, hook_start_offset=45)

    out = pathlib.Path(__file__).parent / '01_手.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,           # filled after render/compare
    'stroke_count_ok': True,     # 4 primitives called: pie, heng, heng, shu_gou
    'endpoint_mismatches': [],   # anchors mirror MMH exactly
    'joint_class_mismatches': [
        # s1↔s4 N: s1.mid65 ~ (131.2, 88.9), s4.head=(139,92) → gap ~8.4 px (near 11 px expected)
        # s2↔s4 P: computed intersection (132.8, 130.1) inside cell C — pierce
        # s3↔s4 P: computed intersection (123.3, 188.4) inside cell C — pierce
    ],
    'overall_pass': None,
    'notes': 'Bank-only render: pie + heng + heng + shu_gou. No BANK_DEVIATION.',
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)
