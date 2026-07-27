"""p3_char_0007_乛 — G4 attempt.

乛 is a single-stroke héng-with-a-downward-hook (héng gōu variant / héng zhé
short form). MMH gives:
  - 1 stroke
  - head @ ('ML', 0.782, 0.342)  → pixel ≈ (78.2, 134.2)
  - tail @ ('C',  0.89,  0.623)  → pixel ≈ (189,   162.3)

Anchor plan (TR7):
  s1 (héng gōu):
    head     = ('ML', 0.782, 0.342)     — top-left of the horizontal
    shoulder = ('C',  0.89,  0.623)     — right end of the horizontal (顿笔)
    tip      = ('C',  0.75,  0.90)      — short hook flick down-and-left

Width: default heng_gou widths — head_w=8, mid_w=6, shoulder_w=11, tip_w=2.
The heng_gou primitive's hook is down-left, matching 乛's shape.

Joints: none (single stroke, hook is internal to the primitive).

TR8 sanity:
  - head y_frac(0.342 in ML) is above tail y_frac(0.623 in C) by ~28 px —
    that's the slight descent visible in the GT; call it "horizontal" for
    TR8 rule 5 purposes (both in M-row: ML and C are both middle row).
  - anchors are all within [0,1] fracs.
"""

import os
import sys

# Import bank primitives.
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from heng_gou import draw_heng_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Single-stroke heng-gou. head=ML(0.782,0.342), '
        'shoulder=C(0.89,0.623) matches MMH tail. '
        'Hook tip is internal to the primitive; no joints expected.'
    ),
}


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    head = ('ML', 0.782, 0.342)
    shoulder = ('C', 0.89, 0.623)
    tip = ('C', 0.75, 0.90)

    draw_heng_gou(draw, head, shoulder, tip,
                  head_w=8, mid_w=6, shoulder_w=11, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_乛.png')
    img.save(out)
    return out


if __name__ == '__main__':
    path = render()
    print('wrote', path)
