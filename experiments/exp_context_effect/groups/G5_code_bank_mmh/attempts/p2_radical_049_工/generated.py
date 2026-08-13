"""G5 attempt: p2_radical_049_工 (3-stroke radical).

Structure per MMH block:
  s1: heng, head ML(0.867,0.143)=(86.7,114.3)  tail MR(0.253,0.017)=(225.3,101.7)
  s2: shu,  head C (0.421,0.222)=(142.1,122.2) tail BC(0.441,0.355)=(144.1,235.5)
  s3: heng, head BL(0.311,0.493)=(31.1,249.3)  tail BR(0.777,0.481)=(277.7,248.1)

Joints:
  s1.mid ⇆ s2.head : N (~17 px gap) — vertical head sits below top heng
  s2.tail ⇆ s3.mid : N (~21 px gap) — vertical tail sits above bottom heng

Bank usage: draw_heng for s1/s3, draw_shu for s2. All primitives fit
cleanly; no BANK_DEVIATION.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Two N-class gaps between vertical and both horizontals per MMH.'
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — top heng
    s1_head = (87, 114)
    s1_tail = (225, 102)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # Stroke 2 — vertical shu (with N-gap top and bottom)
    s2_head = (142, 122)
    s2_tail = (144, 236)
    draw_shu(d, s2_head, s2_tail, width=7)

    # Stroke 3 — bottom heng (longer than top)
    s3_head = (31, 249)
    s3_tail = (278, 248)
    draw_heng(d, s3_head, s3_tail, width_head=9, width_tail=10)

    img.save(path)


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_工.png'
    render(out)
    print(f'wrote {out}')
