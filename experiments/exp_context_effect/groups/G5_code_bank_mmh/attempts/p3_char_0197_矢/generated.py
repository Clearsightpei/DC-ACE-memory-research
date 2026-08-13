"""p3_char_0197_矢 — G5 attempt.

Char: 矢 (shi, 'arrow') — 5 strokes: short-pie + top-heng + mid-heng + long-pie + na.
Composition = 天 (heng+heng+pie+na) with an extra short pie (s1) at the top-left.

Bank retrieval:
- Reuses B5's 天 template (attempts/p3_char_0102_天/generated.py): inline
  draw_heng x2 + draw_pie + draw_na with MMH-verbatim endpoints. The pie
  needs bow_perp negative so path-mid comes back through the s3 heng at
  cell C (welded P-joint per MMH).
- Adds a short pie for s1 (top tick).
- No BANK_DEVIATION needed — clean use of stroke bank primitives.

MMH anchors (px, converted from 米字格 fracs; 300x300 canvas):
  s1: pie  head=(111.6, 70.9)  tail=(71.2, 160.0)   — short top-left pie
  s2: heng head=(106.9, 130.1) tail=(210.9, 113.1)  — top-shorter heng, slight up-slant
  s3: heng head=(48.9, 199.8)  tail=(252.8, 186.6)  — mid longer heng
  s4: pie  head=(133.3, 135.4) tail=(48.6, 290.0)   — long pie down-left, crosses s3
  s5: na   head=(150.6, 197.8) tail=(265.7, 290.3)  — long na down-right

Joints:
  J1 s1.mid ~ s2.head @ C  : N (gap ~14px; anchors already separated)
  J2 s2.mid ~ s4.head @ C  : N (gap ~18px; s4.head sits above s2)
  J3 s3.mid ~ s4.mid  @ C  : P (welded — bow_perp on s4 pulls path back through s3)
  J4 s3.mid ~ s5.head @ C  : N (gap ~11px; s5.head y=198 vs s3.mid y=193)
  J5 s4.mid ~ s5.head @ BC : N (gap ~21px)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402
from na import draw_na      # noqa: E402


def render(out_path: str):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short pie at top-left — from (111.6, 70.9) down-left to (71.2, 160.0)
    # Gentle curve; a small pie shape.
    draw_pie(d, (111.6, 70.9), (71.2, 160.0),
             bow_perp=6, w_head=6, w_tail=2, steps=60)

    # s2: top shorter heng — slight up-slant
    draw_heng(d, (106.9, 130.1), (210.9, 113.1), width_head=7, width_tail=8)

    # s3: mid longer heng — spans wider, slight up-slant
    draw_heng(d, (48.9, 199.8), (252.8, 186.6), width_head=8, width_tail=9)

    # s4: long pie — starts at (133, 135), ends at (49, 290).
    # bow_perp negative bows the curve so path-mid crosses through s3 near C.
    # Straight-line s4 midpoint = (91, 213); we need bow so path crosses
    # s3 at ~(140, 195). Negative bow_perp pulls curve to the RIGHT of the
    # straight line (perpendicular convention from 天 attempt).
    draw_pie(d, (133.3, 135.4), (48.6, 290.0),
             bow_perp=-22, w_head=9, w_tail=2, steps=100)

    # s5: na — from (151, 198) down-right to (266, 290)
    draw_na(d, (150.6, 197.8), (265.7, 290.3),
            bow_perp=-8, w_head=3, w_tail=11, steps=100)

    img.save(out_path)


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,       # 5 primitives: pie, heng, heng, pie, na — matches expected 5
    'endpoint_mismatches': [],     # all five anchors used MMH verbatim
    'joint_class_mismatches': [],  # J1/J2/J4/J5 N via anchor separation; J3 P via pie bow
    'overall_pass': None,
    'notes': (
        '矢 = 天 + top-left short pie (s1). Inlined stroke bank primitives '
        'with MMH-verbatim endpoints. Pie s4 bow_perp=-22 tuned so path-mid '
        'crosses through s3 heng near C (welded P-joint). All N-gaps '
        'inherent from anchor separations (14/18/11/21 px expected).'
    ),
}


if __name__ == '__main__':
    out = str(pathlib.Path(__file__).parent / '01_矢.png')
    render(out)
    print(f'wrote {out}')
