"""p2_radical_041_彳 — 彳 (chì, "step") — 3 strokes.

Structure per MMH spec:
  s1: short 撇 (piě) in the upper area — head TC, tail ML.
  s2: longer 撇 (piě) below, starting near s1's belly — head C (top), tail BL.
  s3: short 竖 (shù) at bottom center — head C (bottom), tail BC (extended down).

Joints (N — small natural gap, do NOT weld):
  j1: s1.mid ⇆ s2.head near cell C (('C', 0.53, 0.142))
  j2: s2.mid ⇆ s3.head near cell C (('C', 0.445, 0.862))
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes (piě, piě, shù); both joints N (small gaps, not welded).'
}

import os
import sys
from PIL import Image, ImageDraw

# Import bank primitives.
BANK_CODE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_CODE)

from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: short 撇 (upper) — head near TC (0.535, 0.612), tail near ML edge (0.938, 0.576).
    draw_pie(draw,
             from_anchor=('TC', 0.535, 0.612),
             to_anchor=('ML', 0.938, 0.576),
             head_width=8, tail_width=1, curve=0.10, segments=48)

    # s2: longer 撇 (middle→bottom-left) — head at C(0.614, 0.242), tail at BL(0.806, 0.479).
    draw_pie(draw,
             from_anchor=('C', 0.614, 0.242),
             to_anchor=('BL', 0.806, 0.479),
             head_width=10, tail_width=1, curve=0.10, segments=48)

    # s3: short 竖 at bottom center — head C(0.456, 0.922), tail BC(0.494, 1.094).
    draw_shu(draw,
             from_anchor=('C', 0.456, 0.922),
             to_anchor=('BC', 0.494, 1.094),
             width=9)

    out = os.path.join(os.path.dirname(__file__), '01_彳.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
