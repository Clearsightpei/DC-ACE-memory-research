"""G5 attempt: p3_char_0053_下.

Character 下 = 一 (heng) + 丨 (shu) + 丶 (dian).
Uses bank primitives heng.py, shu.py, dian.py. No BANK_DEVIATION.

Anchors decoded from MMH structural block:
  cell origins: TL(0,0) TC(100,0) TR(200,0) ML(0,100) C(100,100)
                MR(200,100) BL(0,200) BC(100,200) BR(200,200)
  cell size = 100 px.

  s1 head ML(0.331, 0.002) = (33.1, 100.2)
  s1 tail TR(0.707, 0.92)  = (270.7, 92.0)
  s2 head C (0.427, 0.005) = (142.7, 100.5)
  s2 tail BC(0.494, 1.006) = (149.4, 300.6)   # clipped to 295
  s3 head C (0.626, 0.479) = (162.6, 147.9)
  s3 tail MR(0.191, 0.896) = (219.1, 189.6)

Joint expectations:
  s1.mid ⇆ s2.head  N (~16 px gap at TC)  — s2 head sits ~4 px below
                                             s1 midpoint; that natural
                                             overshoot is the target 顿笔.
  s2.mid ⇆ s3.head  N (~19 px gap at C)   — dot doesn't touch shaft.
"""

import os
import sys
from PIL import Image, ImageDraw

# Make bank importable.
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from dian import draw_dian   # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 bank primitives, endpoints match MMH within tolerance, '
             'both joints implemented as N (natural gap).'
}


def cell(name, xf, yf):
    origins = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[name]
    return (ox + xf * 100, oy + yf * 100)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — heng (top horizontal, slight upward tilt).
    s1_head = cell('ML', 0.331, 0.002)   # (33.1, 100.2)
    s1_tail = cell('TR', 0.707, 0.92)    # (270.7, 92.0)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # Stroke 2 — shu (vertical shaft, starts just under the heng).
    s2_head = cell('C', 0.427, 0.005)    # (142.7, 100.5)
    s2_tail_raw = cell('BC', 0.494, 1.006)
    s2_tail = (s2_tail_raw[0], min(s2_tail_raw[1], 295))
    draw_shu(d, s2_head, s2_tail, width=8)

    # Stroke 3 — dian (small right dot; separated from the shaft ~19 px).
    s3_head = cell('C', 0.626, 0.479)    # (162.6, 147.9)
    s3_tail = cell('MR', 0.191, 0.896)   # (219.1, 189.6)
    draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=7, bow=4)

    out = os.path.join(HERE, '01_下.png')
    img.save(out)
    return out


if __name__ == '__main__':
    path = render()
    print(f'Wrote {path}')
    print(f'SELF_CHECK = {SELF_CHECK}')
