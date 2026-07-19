"""干 (gān, 3画 radical) — G4 attempt.

Structure (3 strokes):
  1. Top 横 (short horizontal, upper)
  2. Middle 横 (longer horizontal, middle-band)
  3. 竖 (vertical descending through both, piercing the middle 横)

Anchor plan (before render — TR7):
  s1 (top heng):  head=('TL', 0.80, 0.10) tail=('TC', 1.00, 0.10) width=10
                  -> px (80,110) -> (200,110); short top bar
  s2 (mid heng):  head=('ML', 0.50, 0.60) tail=('MR', 0.50, 0.60) width=10
                  -> px (50,160) -> (250,160); longer, spans nearly full width
  s3 (shu):       head=('TC', 0.50, 0.20) tail=('BC', 0.50, 0.60) width=10
                  -> px (150,120) -> (150,260); vertical piercing

Joint plan:
  J1 (s1.mid ⇆ s3.head): N-class small gap.
      s1.mid = (140, 110); s3.head = (150, 120); dist ≈ 14.1 px  (≤25 px, TR10 ok).
  J2 (s2.mid ⇆ s3.mid): P-class welded crossing.
      s2 line y=160 crosses s3 line x=150 at (150,160). Both strokes pass
      through that point by construction.

Visual comparison with GT (per TR11 — name 2 specific agreements):
  1. Top 横 is SHORTER than middle 横 (s1 span=120 px vs s2 span=200 px).
  2. Vertical descends through the middle 横 and ends BELOW it (tail
     y=260 > s2 y=160), matching GT's downward extension.
"""

import sys
import os
from PIL import Image, ImageDraw

# Import bank primitives (via success_bank/code path)
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Top heng SHORTER than mid heng (120 vs 200 px). '
        'Vertical pierces mid heng at (150,160), continues to y=260 below. '
        'J1 N-gap ~14 px (≤25 TR10). J2 P-weld by construction (both pass through (150,160)).'
    ),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Anchors
    s1_head = ('TL', 0.80, 0.10)
    s1_tail = ('TC', 1.00, 0.10)
    s2_head = ('ML', 0.50, 0.60)
    s2_tail = ('MR', 0.50, 0.60)
    s3_head = ('TC', 0.50, 0.20)
    s3_tail = ('BC', 0.50, 0.60)

    # Pixel sanity (TR8)
    p_s1h = anchor_to_xy(s1_head); p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head); p_s2t = anchor_to_xy(s2_tail)
    p_s3h = anchor_to_xy(s3_head); p_s3t = anchor_to_xy(s3_tail)

    # s1 horizontal — head left of tail, same y
    assert p_s1h[0] < p_s1t[0], 's1 head must be left of tail'
    assert abs(p_s1h[1] - p_s1t[1]) < 1, 's1 must be horizontal'
    # s2 horizontal — same
    assert p_s2h[0] < p_s2t[0], 's2 head must be left of tail'
    assert abs(p_s2h[1] - p_s2t[1]) < 1, 's2 must be horizontal'
    # s3 vertical — head above tail, same x
    assert p_s3h[1] < p_s3t[1], 's3 head must be above tail'
    assert abs(p_s3h[0] - p_s3t[0]) < 1, 's3 must be vertical'
    # s1 shorter than s2
    len_s1 = p_s1t[0] - p_s1h[0]
    len_s2 = p_s2t[0] - p_s2h[0]
    assert len_s1 < len_s2, 'top heng should be shorter than mid heng'
    # J1 N-gap
    s1_mid = ((p_s1h[0] + p_s1t[0]) / 2, p_s1h[1])
    dist_j1 = ((s1_mid[0] - p_s3h[0])**2 + (s1_mid[1] - p_s3h[1])**2) ** 0.5
    assert dist_j1 <= 25, f'J1 N-gap {dist_j1:.1f}px exceeds TR10 threshold 25'
    # J2 weld: s3 line x == 150 crosses s2 line y == 160 → cross exists inside both segments
    assert p_s2h[0] <= p_s3h[0] <= p_s2t[0], 'P-weld: crossing x must lie within s2'
    assert p_s3h[1] <= p_s2h[1] <= p_s3t[1], 'P-weld: crossing y must lie within s3'

    # Render
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_heng(draw, s2_head, s2_tail, width=10)
    draw_shu(draw, s3_head, s3_tail, width=10)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '01_干.png')
    img.save(out_path)
    print(f'Wrote {out_path}')
    print(f'  s1 len={len_s1:.1f}px  s2 len={len_s2:.1f}px  J1 dist={dist_j1:.1f}px')


if __name__ == '__main__':
    render()
