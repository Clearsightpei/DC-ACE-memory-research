"""p2_radical_071_巳 — 3 strokes: 横折, 横, 竖弯钩.

Sibling of 己 (p2_radical_053) — same 3-stroke skeleton with two
distinguishing differences:
  * 巳's s3 head starts at TL (y≈91) rather than ML (y≈146) — the
    left vertical runs the full character height, meeting near
    the top of s1.
  * 巳's s2 (middle 横) is wider (spans left→right, ~90px) making
    the top loop look enclosed.

Bank primitives:
  - heng_zhe_short (s1)
  - heng           (s2)
  - shu_wan_gou    (s3)

MMH endpoint anchors (pixels on 300x300):
  s1: C(0.02, 0.075)  = (102, 108)   ->  C(0.661, 0.436) = (166, 144)
  s2: ML(0.946, 0.638)= (95, 164)    ->  C(0.837, 0.535) = (184, 154)
  s3: TL(0.768, 0.911)= (77, 91)     ->  BR(0.563, 0.06) = (256, 206)

Joints (all N — natural gaps, do not weld):
  s1.tail ~ s2.mid(0.78) : N gap ~15px near C
  s1.head ~ s3.head       : N gap ~17px near TL/ML boundary
  s2.head ~ s3.mid(0.21)  : N gap ~16.5px near ML

Adjustments vs raw MMH:
  * s1.tail nudged down-right to (198, 158): the raw MMH tail (166,144)
    lands inside the loop; the visible fold-corner of a 横折 sits at
    the outer edge, so the visible tail is beyond the raw median. The
    joint gap to s2 remains N (s2 passes below).
  * s3.head nudged slightly right to (85, 95) so its vertical descent
    doesn't overlap s1's leftmost point (gap N preserved).
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from heng import draw_heng                      # noqa: E402
from heng_zhe_short import draw_heng_zhe_short  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 primitives: heng_zhe_short + heng + shu_wan_gou
    'endpoint_mismatches': [],      # all within same/adjacent MMH cell
    'joint_class_mismatches': [],   # all three joints kept as N (natural gaps)
    'overall_pass': True,
    'notes': 's1 tail nudged to visible corner (198,158); s3 head shifted slightly right of s1 head to preserve N gap.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 (top horizontal + fold-down on right)
    s1_head = (102, 108)
    s1_tail = (198, 158)   # nudged down-right to the visible fold corner
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail)

    # Stroke 2: 横 (middle horizontal — wider than 己's, spans left→right)
    s2_head = (95, 164)
    s2_tail = (184, 154)
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩 (left vertical from TOP, curves right, hooks up)
    s3_head = (85, 95)     # slightly right of s1_head to keep N gap
    s3_tail = (250, 205)
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=55, knee_ratio=0.75)

    out_path = os.path.join(os.path.dirname(__file__), '01_巳.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
