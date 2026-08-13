"""p3_char_0167_乎 — G5 attempt.

5 strokes (from MMH):
  1) 撇  wide shallow top arc  from TR(201.3, 71.5) to TL(94.3, 95.2)  — draw_pie
  2) 点  short 左点 (ML→C)      from (90.2, 128.3) to (111.3, 150.6)   — draw_dian
  3) 撇  short right down       from TR(206.8, 99.6) to C(178.7, 145.3) — draw_pie
  4) 横  long middle horizontal from ML(36, 186) to MR(273.9, 179.6)   — draw_heng
  5) 弯钩 descender with small bottom hook
                                from TC(135.6, 90.5) to BC(102.2, 276.6) — draw_wan_gou

Joints:
  - s1.mid ⇆ s5.head @ TC : N (natural gap ≈ 10 px)  — 撇 sweeps just above 竖钩 head
  - s3.tail ⇆ s5.mid(0.21) @ C : N (gap ≈ 35 px)     — right 撇 ends near but not on shaft
  - s4.mid ⇆ s5.mid(0.37) @ C : P (welded)           — 横 crosses 竖钩 shaft

Bank use:
  - draw_pie for s1 (long shallow arc) and s3 (short right stroke)
  - draw_dian for s2
  - draw_heng for s4
  - draw_wan_gou for s5 (similar shape to 兮's descender but taller)
  No BANK_DEVIATION.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from dian import draw_dian
from heng import draw_heng
from wan_gou import draw_wan_gou


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: wide shallow top 撇 — the arching top of 乎.
    s1_head = (201.3, 71.5)
    s1_tail = (94.3, 95.2)
    draw_pie(d, s1_head, s1_tail, bow_perp=-14, w_head=8, w_tail=3)
    # negative bow_perp so the arc curves UP (top-of-乎 arches upward)

    # s2: short 左点 dot on the left, under the arc
    s2_head = (90.2, 128.3)
    s2_tail = (111.3, 150.6)
    draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=7, bow=3)

    # s3: short right-side 撇 heading down-left
    s3_head = (206.8, 99.6)
    s3_tail = (178.7, 145.3)
    draw_pie(d, s3_head, s3_tail, bow_perp=6, w_head=6, w_tail=3)

    # s4: long 横 across middle
    s4_head = (36.0, 186.0)
    s4_tail = (273.9, 179.6)
    draw_heng(d, s4_head, s4_tail, width_head=7, width_tail=8)

    # s5: 弯钩 vertical descender with small left-flick hook
    # Shift head slightly right so the shaft crosses s4 midpoint (~x=155) —
    # welded joint at s4.mid ⇆ s5.mid(0.37) requires the shaft to pass through
    # the middle of the horizontal.
    s5_head = (150.0, 90.5)
    s5_tail = (105.0, 275.0)
    draw_wan_gou(d, s5_head, s5_tail,
                 belly_right=14, hook_len=22, hook_up=11,
                 w_head=6, w_body=6, w_tail=2)

    out = os.path.join(os.path.dirname(__file__), '01_乎.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # exactly 5 primitive calls
    'endpoint_mismatches': [
        {'stroke': 5, 'expected_head': ('TC', 0.356, 0.905),
         'actual_head_px': (150.0, 90.5),
         'note': 'shifted +15px right of MMH anchor so shaft welds through s4.mid'}
    ],
    'joint_class_mismatches': [],  # 3 joints implemented as N/N/P per spec
    'overall_pass': True,
    'notes': 'wan_gou tuned taller than 兮 (shaft ~185 px vs ~110 px).',
}


if __name__ == '__main__':
    print(render())
