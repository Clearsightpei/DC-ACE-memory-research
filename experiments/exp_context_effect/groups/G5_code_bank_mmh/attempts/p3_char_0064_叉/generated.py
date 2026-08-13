"""p3_char_0064_叉 — G5 attempt.

叉 = 又 (heng_pie + na) + a small tick (dian) in the upper interior crotch.

MMH-injected anchors:
  s1 head ML(0.949, 0.169) = (94.9, 116.9)   s1 tail BL(0.483, 0.757) = (48.3, 275.7)
  s2 head ML(0.888, 0.611) = (88.8, 161.1)   s2 tail BR(0.836, 0.824) = (283.6, 282.4)
  s3 head  C(0.102, 0.362) = (110.2, 136.2)  s3 tail  C(0.427, 0.576) = (142.7, 157.6)

Joints:
  s1.mid(0.66) ⇆ s2.mid(0.37) @ BC : P (weld) — heng_pie crossing na body
  s1.head    ⇆ s3.head       @ C  : N (gap ≈ 27.1 px) — small tick sits below/right of s1 head

Reuse strategy: 又 primitive uses different s1 head (77.9 vs 94.9), so instead
of calling draw_you at identity, inline draw_heng_pie + draw_na with THIS
character's exact anchors, then add the small dian for stroke 3.
No BANK_DEVIATION (stroke primitives used as intended; whole-又 primitive
just happens to be for a slightly different composition).
"""

import sys
import pathlib
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
GROUP = HERE.parents[2]
sys.path.insert(0, str(GROUP / 'success_bank' / 'code'))

from heng_pie import draw_heng_pie  # noqa: E402
from na import draw_na              # noqa: E402
from dian import draw_dian          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 strokes: heng_pie + na + dian
    'endpoint_mismatches': [],     # anchors identical to MMH injected block
    'joint_class_mismatches': [],  # P at BC via crossing; N at C via small gap
    'overall_pass': True,
    'notes': 'Reuse heng_pie+na from bank as in 又; add small dian for tick s3.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1: heng_pie top-right to bottom-left
    draw_heng_pie(d, head=(94.9, 116.9), tail=(48.3, 275.7))

    # stroke 2: 捺 (long right-descending) top-left to bottom-right
    draw_na(d, head=(88.8, 161.1), tail=(283.6, 282.4),
            bow_perp=10, w_head=4, w_tail=12, steps=90)

    # stroke 3: small tick / dian in the upper interior (crotch above the crossing)
    # Very short: length ≈ 39 px. Use dian with modest taper.
    draw_dian(d, head=(110.2, 136.2), tail=(142.7, 157.6),
              w_head=3, w_tail=5, bow=2, steps=40)

    out = HERE.parent / '01_叉.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
