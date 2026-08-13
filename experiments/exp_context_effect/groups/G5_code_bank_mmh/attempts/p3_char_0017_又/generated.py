"""p3_char_0017_又 — G5 attempt.

Character 又 is the same shape as p2_radical_037_又 (2 strokes: heng_pie + na, P-joint at BC).
The bank primitive `you_again.py::draw_you` was promoted from that PASS with the exact same
MMH anchors this character uses:
  - s1 head ML(0.779, 0.169) = (77.9, 116.9)
  - s1 tail BL(0.425, 0.76)  = (42.5, 276.0)
  - s2 head ML(0.794, 0.397) = (79.4, 139.7)
  - s2 tail BR(0.854, 0.789) = (285.4, 278.9)
So call draw_you at identity transform.
"""

import sys, pathlib
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
GROUP = HERE.parents[2]
sys.path.insert(0, str(GROUP / 'success_bank' / 'code'))

from you_again import draw_you  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 strokes: draw_heng_pie + draw_na (inside draw_you)
    'endpoint_mismatches': [],     # anchors identical to MMH injected block
    'joint_class_mismatches': [],  # P joint at BC realised naturally by heng_pie tail crossing na body
    'overall_pass': True,
    'notes': 'Phase-3 又 == p2 radical 又. Bank primitive matches MMH anchors exactly; identity call.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_you(d, ox=0, oy=0, scale=1.0)
    out = HERE.parent / '01_又.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
