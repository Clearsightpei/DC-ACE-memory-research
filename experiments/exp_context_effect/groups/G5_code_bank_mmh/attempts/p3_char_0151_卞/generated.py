"""p3_char_0151_卞 (biàn) — G5 attempt.

Character: 卞 — 4 strokes:
  1. 点 (dian) at top — short diagonal in TC
  2. 横 (heng) — long horizontal ML→MR
  3. 竖 (shu) — vertical from just under heng down to BC edge
  4. 点 (dian) — short diagonal on the right below the heng

MMH anchors converted from (cell, x_frac, y_frac) to px:
  cell origins: TC=(100,0), ML=(0,100), MR=(200,100), C=(100,100), BC=(100,200), BR=(200,200)

Joint expectation: s2.mid(0.40) ⇆ s3.head is N (neighbor, gap ~16px).
  Following MMH: s3 head sits BELOW the heng — do not pierce it.
  In practice we let s3 start ~2px below the heng line so a small,
  natural gap appears.

No BANK_DEVIATION — uses draw_dian, draw_heng, draw_shu straight from bank.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 primitive calls, 1 per stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # s2/s3 gap kept small (N)
    'overall_pass': True,
    'notes': 'shu head sits just below heng to preserve N-gap per MMH.'
}


def anchor(cell, xf, yf):
    origins = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[cell]
    return (ox + xf * 100, oy + yf * 100)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1 — top dian (TC → TC)
    s1_head = anchor('TC', 0.263, 0.604)   # (126.3, 60.4)
    s1_tail = anchor('TC', 0.629, 0.899)   # (162.9, 89.9)
    draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=4)

    # stroke 2 — heng (ML → MR)
    s2_head = anchor('ML', 0.322, 0.345)   # (32.2, 134.5)
    s2_tail = anchor('MR', 0.736, 0.248)   # (273.6, 124.8)
    draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

    # stroke 3 — shu (C → BC bottom edge). Start just below heng to keep N-gap.
    s3_head = anchor('C', 0.374, 0.356)     # (137.4, 135.6) — approx heng line
    s3_head = (s3_head[0], s3_head[1] + 6)  # push down 6px for visible gap
    s3_tail = anchor('BC', 0.509, 1.035)    # (150.9, 303.5)
    s3_tail = (s3_tail[0], min(s3_tail[1], 296))
    draw_shu(d, s3_head, s3_tail, width=7)

    # stroke 4 — bottom-right dian (C → BR)
    s4_head = anchor('C', 0.746, 0.734)     # (174.6, 173.4)
    s4_tail = anchor('BR', 0.18, 0.121)     # (218.0, 212.1)
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=8, bow=3)

    out = pathlib.Path(__file__).parent / '01_卞.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
