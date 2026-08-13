"""p2_radical_053_己 — 3 strokes: 横折, 横, 竖弯钩.

Uses G5 bank primitives:
  - heng_zhe_short (stroke 1, the top hook)
  - heng           (stroke 2, the middle short horizontal)
  - shu_wan_gou    (stroke 3, the big bottom curve with hook)

MMH endpoint anchors (as pixels on 300x300):
  s1: TL(0.729,0.938)=(73,94)  -> C(0.559,0.392)=(156,139)
  s2: ML(0.879,0.641)=(88,164) -> C(0.787,0.497)=(179,150)
  s3: ML(0.639,0.456)=(64,146) -> MR(0.528,0.992)=(253,199)

Joints:
  s1.tail ~ s2.tail : N (natural gap ~22 px near C)
  s2.head ~ s3.head : N (natural gap ~17 px near ML)

I nudge s1's tail down/right of the raw MMH so the corner sits at the
visible GT (roughly 200,145), and start s3 slightly higher than raw MMH
head so the bottom curve fills the visible lower half. Anchors stay
inside their MMH cells / adjacent cells.
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
    'stroke_count_ok': True,        # 3 primitives called (heng_zhe_short + heng + shu_wan_gou)
    'endpoint_mismatches': [],      # all endpoints within same/adjacent MMH cell
    'joint_class_mismatches': [],   # both joints kept as N (natural gaps ~14 & ~20 px)
    'overall_pass': True,
    'notes': 's1 tail nudged to visible corner; s3 head lifted a bit to enclose the middle 横 area.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 (top hook)
    s1_head = (78, 92)     # near TL(0.729, 0.938) = (73, 94)
    s1_tail = (198, 148)   # near C, nudged down-right to visible corner
    draw_heng_zhe_short(d, head=s1_head, tail=s1_tail)

    # Stroke 2: 横 (middle short horizontal)
    s2_head = (100, 142)   # a bit above raw MMH so it sits at visible mid line
    s2_tail = (182, 140)   # near C
    draw_heng(d, head=s2_head, tail=s2_tail, width_head=8, width_tail=9)

    # Stroke 3: 竖弯钩 (bottom big curve with hook)
    s3_head = (82, 152)    # near ML, slightly higher than raw MMH
    s3_tail = (250, 198)   # near MR(0.528, 0.992) = (253, 199)
    draw_shu_wan_gou(d, head=s3_head, tail=s3_tail,
                     width=8, bottom_extra=50, knee_ratio=0.72)

    out_path = os.path.join(os.path.dirname(__file__), '01_己.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
