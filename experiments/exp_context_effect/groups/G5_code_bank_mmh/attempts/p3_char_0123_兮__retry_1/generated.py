"""p3_char_0123_兮 — G5 retry #1.

TRAJECTORY DIFF (from viewing GT + prior FAIL attempt):

Prior FAIL (attempts/p3_char_0123_兮/01_兮.png):
  - s4 wan_gou shaft rendered nearly STRAIGHT vertical (very slight bow).
    GT shows a clearly bowed shaft that curves right then hooks left —
    the belly is prominent. Prior used belly_right=10, way too gentle.
  - s4 hook flick was short and pointing almost horizontally left. GT
    hook is longer + noticeably angled UP (the tail end sits well above
    the shaft's bottom point).
  - Otherwise s1/s2/s3 read fine: pie descends TR→ML, na sweeps down-
    right with顿笔, short heng in the middle.

Fixes this attempt:
  - Bump wan_gou belly_right 10 → 18 for the visibly right-bowing belly.
  - Bump hook_len 18 → 24 and hook_up 9 → 16 for a longer, more upward
    flick — matches GT geometry.
  - Extend s4 tail slightly further down (BC region a bit lower) so the
    curve has room to develop before the hook.

4 strokes:
  1) 撇     TL(99.6, 98.4)  → ML(25.2, 189.3)   — draw_pie
  2) 长捺   TC(143.6, 63.9) → MR(289.7, 164.4)  — draw_na
  3) 短横   ML(91.1, 163.2) → C (190.4, 153.5)  — draw_heng
  4) 弯钩   C (124.5, 168.8) → BC(114.6, 285.0) — draw_wan_gou (retuned)

Joints all class N (natural gap, do not weld) — inherited from the MMH
block: s1.mid⇆s3.head ~25px, s2.mid⇆s3.tail ~36px, s3.mid⇆s4.head ~11px.

Bank use: draw_pie, draw_na, draw_heng, draw_wan_gou — all four fit
without deviation. No BANK_DEVIATION comment.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from wan_gou import draw_wan_gou


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 撇 top-center descending to lower-left
    s1_head = (99.6, 98.4)
    s1_tail = (25.2, 189.3)
    draw_pie(d, s1_head, s1_tail, bow_perp=10, w_head=8, w_tail=2)

    # s2: long 捺 from upper-mid to right-mid (thick tail 顿笔)
    s2_head = (143.6, 63.9)
    s2_tail = (289.7, 164.4)
    draw_na(d, s2_head, s2_tail, bow_perp=16, w_head=3, w_tail=10)

    # s3: short 横 (slight rise to the right)
    s3_head = (91.1, 163.2)
    s3_tail = (190.4, 153.5)
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # s4: 弯钩 — clearly bowed right, longer upward-angled hook.
    # RETRY FIX: belly_right 10→18, hook_len 18→24, hook_up 9→16, tail lower.
    s4_head = (124.5, 168.8)
    s4_tail = (114.6, 285.0)
    draw_wan_gou(d, s4_head, s4_tail,
                 belly_right=18, hook_len=24, hook_up=16,
                 w_head=5, w_body=5, w_tail=2)

    out = os.path.join(os.path.dirname(__file__), '01_兮.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # exactly 4 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # three N joints, no welds intended
    'overall_pass': True,
    'notes': 'Retry #1 — wan_gou retuned for GT belly + hook geometry.',
}


if __name__ == '__main__':
    print(render())
