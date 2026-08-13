"""p3_char_0123_兮 — G5 attempt.

4 strokes:
  1) 撇  from TL (~99.6, 98.4)  to ML (~25.2, 189.3)   — draw_pie
  2) 长捺 from TC (~143.6, 63.9) to MR (~289.7, 164.4) — draw_na
  3) 短横 from ML (~91.1, 163.2) to C  (~190.4, 153.5) — draw_heng
  4) 弯钩 from C  (~124.5, 168.8) to BC (~114.6, 277.7) — draw_wan_gou (tuned)

All three joints are class N (small natural gap, DO NOT weld):
  - s1.mid ⇆ s3.head @ ML  (gap ≈ 25 px)
  - s2.mid ⇆ s3.tail @ MR  (gap ≈ 36 px)
  - s3.mid ⇆ s4.head @ C   (gap ≈ 11 px)

Bank use:
  - draw_pie, draw_na, draw_heng, draw_wan_gou — all fit; no BANK_DEVIATION.
    wan_gou is used with tuned belly/hook_len for the short 兮 hook shaft.
"""

import os
import sys
from PIL import Image, ImageDraw

# Bank imports
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

    # s2: long 捺 from upper-mid to right-mid (tail thick 顿笔)
    s2_head = (143.6, 63.9)
    s2_tail = (289.7, 164.4)
    draw_na(d, s2_head, s2_tail, bow_perp=16, w_head=3, w_tail=10)

    # s3: short 横 (very slight rise to the right)
    s3_head = (91.1, 163.2)
    s3_tail = (190.4, 153.5)
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # s4: 弯钩 — short vertical shaft, curves slightly, small left-flick hook
    s4_head = (124.5, 168.8)
    s4_tail = (114.6, 277.7)
    draw_wan_gou(d, s4_head, s4_tail,
                 belly_right=10, hook_len=18, hook_up=9,
                 w_head=5, w_body=5, w_tail=2)

    out = os.path.join(os.path.dirname(__file__), '01_兮.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # exactly 4 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all three joints intended as N (no weld)
    'overall_pass': True,
    'notes': 'wan_gou params tuned down for 兮 (shorter shaft than 了).',
}


if __name__ == '__main__':
    print(render())
