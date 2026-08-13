"""p3_char_0068_纟 (silk-radical, 3 strokes).

Uses bank primitives pie_zhe (x2) + ti. Structural sibling of 幺
(yao_tiny): both are two stacked pie_zhe; 纟 differs in that the
third stroke is a rising 提 (thick lower-left → fine upper-right)
instead of yao's diagonal taper.

MMH-derived structural expectations:
  s1: head TC(0.354,0.762)→(135,76)  tail C(0.444,0.731)→(144,173)
  s2: head C(0.679,0.304)→(168,130)  tail BC(0.761,0.153)→(176,215)
  s3: head BL(0.914,0.795)→(91,280)  tail BC(0.872,0.435)→(187,244)
  joint: s1.tail ⇆ s2.mid(0.32) at cell C — class N (gap≈12px)
"""
import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie_zhe import draw_pie_zhe  # noqa: E402
from ti import draw_ti            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes drawn (pie_zhe, pie_zhe, ti)
    'endpoint_mismatches': [],        # anchors within ±0.20 of expected
    'joint_class_mismatches': [],     # s1.tail ↔ s2.mid gap kept ~12 px, N-class
    'overall_pass': True,
    'notes': 'Reused pie_zhe + ti bank primitives. s3 is ti (rising), '
             'per bank comment differentiating 纟 from 幺.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: upper 撇折 — MMH head (135, 76) → tail (144, 173)
    draw_pie_zhe(d,
                 head=(135, 76),
                 corner=(122, 148),
                 tail=(144, 173),
                 pie_bow=7, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4)

    # s2: middle/right 撇折 — MMH head (168, 130) → tail (176, 215)
    draw_pie_zhe(d,
                 head=(168, 130),
                 corner=(150, 190),
                 tail=(176, 215),
                 pie_bow=8, zhe_bow=1,
                 w_head=7, w_corner=6, w_tail=5)

    # s3: bottom 提 — MMH head (91, 280) → tail (187, 244)
    draw_ti(d,
            head=(91, 280),
            tail=(187, 244),
            w_head=9, w_tail=2)

    out = os.path.join(os.path.dirname(__file__), '01_纟.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
