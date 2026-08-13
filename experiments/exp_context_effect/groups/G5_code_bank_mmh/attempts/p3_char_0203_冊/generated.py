"""p3_char_0203_冊 — G5 attempt.

Structure (5 strokes per MMH):
  s1: 撇 (long left descender) — pie head=(73.8, 86.4) → tail=(43.1, 289.5)
  s2: 横折钩 (top+right frame, hooks left at bottom)
        heng_head=(92, 89.4), corner=(221, 90), gou_tail=(221, 275),
        hook_tip=(184.6, 275.7)
  s3: 横 (middle bar spanning entire char) — head=(24.6, 174.9) → tail=(283.6, 164.1)
  s4: 竖 (inner-left vertical) — head=(116.6, 95.8) → tail=(121, 267.5)
  s5: 竖 (inner-right vertical) — head=(161.1, 90.5) → tail=(167.6, 273)

Bank primitives used: pie, heng_zhe_gou, heng, shu, shu — clean composition,
no BANK_DEVIATION.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('s2 modeled as heng_zhe_gou with corner at (221,90) and hook '
              'flicking left; s3 crosses s2 near (221,167) as a P joint; s4/s5 '
              'are simple shus piercing s3 (P joints). s1.head↔s2.head is N '
              '(natural gap ~14px preserved by keeping heads at 74 and 92).')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: left descender pie (curves down-left) — revision: bump bow to match
    # GT's pronounced leftward sweep in the lower half.
    draw_pie(d, head=(73.8, 86.4), tail=(43.1, 289.5),
             bow_perp=22, w_head=9, w_tail=3)

    # s2: heng-zhe-gou spanning the top and right side of the character
    draw_heng_zhe_gou(d,
                      heng_head=(92.0, 89.4),
                      corner=(221.0, 90.0),
                      gou_tail=(221.0, 275.0),
                      hook_tip=(184.6, 275.7))

    # s3: long middle horizontal bar (crosses entire character)
    draw_heng(d, head=(24.6, 174.9), tail=(283.6, 164.1),
              width_head=8, width_tail=9)

    # s4: inner-left vertical
    draw_shu(d, head=(116.6, 95.8), tail=(121.0, 267.5), width=7)

    # s5: inner-right vertical
    draw_shu(d, head=(161.1, 90.5), tail=(167.6, 273.0), width=7)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_冊.png'
    img = render()
    img.save(out)
    print(f'wrote {out}')
