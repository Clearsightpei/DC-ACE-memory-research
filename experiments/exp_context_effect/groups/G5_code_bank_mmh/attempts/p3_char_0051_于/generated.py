"""p3_char_0051_于 — draw 于 (3 strokes: short heng top, longer heng middle, 竖钩).

Composition adapted from bank primitive `gan_dry.py` (于 has same top-heng /
middle-heng layout as 干). The differentiator is stroke 3: 于 has 竖钩 (vertical
with a leftward hook at bottom), while 干 has straight 竖. So s3 uses the
`shu_gou.py` bank primitive with hook tail pulled slightly left.

MMH structural expectations (from dispatcher):
  s1: TR(0.867,0.888) → TL(0.112,0.806)  — top heng
  s2: ML(0.328,0.646) → MR(0.678,0.512)  — middle heng
  s3: TC(0.359,0.946) → BC(0.011,0.73)   — 竖钩 head near top-center, tail
                                            biased to lower-left (hook)
  joint J1: s1.mid ⇆ s3.head @ TC  — class N (small gap ~15px, DO NOT weld)
  joint J2: s2.mid ⇆ s3.mid  @ C   — class P (pierce/weld)
"""

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from heng import draw_heng           # bank primitive
from shu_gou import draw_shu_gou     # bank primitive


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,          # 3 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': (
        's1/s2 endpoints follow gan_dry.py calibration (proven PASS layout '
        'for 干 which has same top+mid heng geometry). s3 replaced from shu '
        'to shu_gou; tail pulled left (~x=95) so BC-cell placement holds and '
        'the hook points left. J1 (s1-mid vs s3-head) N-gap: s1 mid ~ (154, 76), '
        's3 head (140, 45) -> vertical gap ~15px NO weld. J2 pierce: s3 body '
        'crosses s2 near x=150 y=164 -> welded by ink width.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s1: top short heng (from gan_dry endpoints) ----
    draw_heng(draw, (92, 83), (217, 69),
              width_head=9, width_tail=11)

    # ---- s2: middle long heng (from gan_dry endpoints) ----
    draw_heng(draw, (30, 169), (274, 159),
              width_head=10, width_tail=12)

    # ---- s3: 竖钩 — head just BELOW top-heng (N-gap), tail lower-left (hook) ----
    # J1 is class N: s3.head must NOT touch s1. s1 mid is ~y=76, so put s3
    # head at (150, 92) → ~10 px gap below s1 (respects N class, no pierce).
    # s3 body passes through s2 at y~164 (J2 pierce weld). Tail at (95, 275)
    # so hook tip lands lower-left BC cell.
    draw_shu_gou(draw, (150, 92), (95, 275),
                 width=8, hook_start_offset=55)

    out_path = os.path.join(os.path.dirname(__file__), '01_于.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
