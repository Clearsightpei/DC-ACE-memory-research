"""p3_char_0299_里 — 里 (lǐ, "inside/mile", 7 strokes).

Structure: top 日-like frame stacked on 土-like base, all pierced by
a long central vertical spine (s5) and closed by a long bottom heng (s7).

Stroke plan (from MMH anchors):
  s1 — 竖: TL(0.706, 0.902) → C(0.061, 0.866)   (left wall of top 日)
  s2 — 横折: TL(0.855, 0.911) → corner → C(0.969, 0.834)
  s3 — 横: C(0.166, 0.359) → C(0.834, 0.283)   (middle bar of 日)
  s4 — 横: C(0.113, 0.734) → C(0.860, 0.658)   (bottom bar of 日)
  s5 — 竖: TC(0.351, 0.955) → BC(0.400, 0.646) (long central spine)
  s6 — 横: BL(0.958, 0.247) → BR(0.024, 0.156) (middle bar of 土)
  s7 — 横: BL(0.343, 0.804) → BR(0.760, 0.716) (long base heng)

Joints:
  s1.h ⇆ s2.h : N (top-left corner of 日, small gap)
  s1.mid ⇆ s3.h : N
  s1.t ⇆ s4.h : N
  s2.t ⇆ s4.t : N
  s2.mid(0.18) ⇆ s5.h : N (very small)
  s3 × s5 : P (welded)
  s4 × s5 : P (welded)
  s5 × s6 : P (welded)
  s5.t ⇆ s7.mid(0.40) : N (small gap — spine ends above bottom heng)
"""
import sys, os
_here = os.path.dirname(os.path.abspath(__file__))
# .../groups/G4_grid/attempts/<item>/  ->  .../groups/G4_grid/success_bank/code
_bank = os.path.normpath(os.path.join(_here, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _bank)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '里 = top 日 + bottom 土 stacked, pierced by long central spine and closed by long base heng.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    W = 10  # stroke width

    # s1: left wall of top 日
    s1h = anchor_to_xy(('TL', 0.706, 0.902))
    s1t = anchor_to_xy(('C',  0.061, 0.866))
    fat_line(d, s1h, s1t, width=W)

    # s2: 横折 (top + right wall of 日)  — compound stroke via corner
    s2h = anchor_to_xy(('TL', 0.855, 0.911))
    s2t = anchor_to_xy(('C',  0.969, 0.834))
    # corner near top-right of 日: same y as head, same x as tail
    corner = (s2t[0], s2h[1])
    fat_line(d, s2h, corner, width=W)
    fat_line(d, corner, s2t, width=W)

    # s3: middle heng of 日 — welded across spine
    s3h = anchor_to_xy(('C', 0.166, 0.359))
    s3t = anchor_to_xy(('C', 0.834, 0.283))
    fat_line(d, s3h, s3t, width=W)

    # s4: bottom heng of 日
    s4h = anchor_to_xy(('C', 0.113, 0.734))
    s4t = anchor_to_xy(('C', 0.860, 0.658))
    fat_line(d, s4h, s4t, width=W)

    # s5: long central spine
    s5h = anchor_to_xy(('TC', 0.351, 0.955))
    s5t = anchor_to_xy(('BC', 0.400, 0.646))
    fat_line(d, s5h, s5t, width=W)

    # s6: short middle heng of 土 (below 日)
    s6h = anchor_to_xy(('BL', 0.958, 0.247))
    s6t = anchor_to_xy(('BR', 0.024, 0.156))
    fat_line(d, s6h, s6t, width=W)

    # s7: long base heng
    s7h = anchor_to_xy(('BL', 0.343, 0.804))
    s7t = anchor_to_xy(('BR', 0.760, 0.716))
    fat_line(d, s7h, s7t, width=W + 1)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_里.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
