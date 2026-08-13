"""p3_char_0504_畛 (zhěn) — G5 attempt.

Composition: 田 (left, 5 strokes) + 㐱 (right, 5 strokes: 人 over 彡) = 10.

Strategy per P-A-006 (stroke-primitive layer at MMH anchors) + P-A-008
(inline reasoning trace). No whole-radical bank primitive fits both
halves perfectly:
- 田-left: si_four uses pie+shu_zhe inside (wrong marks); you_by (由)
  has a central shu extending above (wrong). Inline 田 from stroke
  primitives at MMH anchors. Not P-A-007-eligible for a uniform-shift
  rescue because no compound-left 田 primitive exists yet.
- 㐱-right: 人 (pie+na) then 彡 (three pies of increasing length &
  slant). Inline from primitives — no bank entry for 㐱.

MMH endpoints (fractions → 300×300 px), computed inline:
  s1 shu   (16.7,129.8) → (39.0, 231.7)   [田 left vertical]
  s2 h_zhe (31.6,138.3) → (100.2,214.2)   [田 top+right box]
  s3 heng  (42.5,173.1) → (91.4, 164.6)   [田 middle heng]
  s4 shu   (58.9,133.6) → (61.2, 203.6)   [田 middle shu] — welds s3 (P)
  s5 heng  (45.1,218.3) → (87.6, 204.8)   [田 bottom heng]
  s6 pie   (174.9,68.0) → (120.1,169.3)   [人 pie]
  s7 na    (189.3,95.5) → (288.6,165.2)   [人 na]
  s8 pie   (179.3,138.3)→ (135.6,205.1)   [彡 top]
  s9 pie   (191.9,173.7)→ (134.5,249.6)   [彡 middle]
  s10 pie  (208.9,208.3)→ (123.3,309.1)   [彡 bottom, longest]

SELF_CHECK dict at bottom.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw  # noqa: E402

from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === 田 left (strokes 1-5) ==============================================
    # s1: left vertical shu — slight rightward drift per MMH anchors
    draw_shu(d, (16.7, 129.8), (39.0, 231.7), width=7)
    # s2: heng_zhe box — top-left corner to bottom-right corner
    draw_heng_zhe_box(d, (31.6, 138.3), (100.2, 214.2), width=8)
    # s3: middle heng inside 田 (short)
    draw_heng(d, (42.5, 173.1), (91.4, 164.6), width_head=7, width_tail=8)
    # s4: middle shu inside 田 (welds s3 at midpoint — P joint)
    draw_shu(d, (58.9, 133.6), (61.2, 203.6), width=7)
    # s5: bottom heng inside 田 (short, closes box)
    draw_heng(d, (45.1, 218.3), (87.6, 204.8), width_head=8, width_tail=9)

    # === 㐱 right (strokes 6-10) ============================================
    # s6: 人 pie (from apex upper-right down to lower-left)
    draw_pie(d, (174.9, 68.0), (120.1, 169.3), bow_perp=10, w_head=8, w_tail=3)
    # s7: 人 na (from near apex diagonally down-right — sweeping heng-na)
    draw_na(d, (189.3, 95.5), (288.6, 165.2), bow_perp=8, w_head=4, w_tail=10)

    # === 彡 three pies (strokes 8-10), increasing length ====================
    # s8: top pie (shortest)
    draw_pie(d, (179.3, 138.3), (135.6, 205.1), bow_perp=6, w_head=7, w_tail=3)
    # s9: middle pie
    draw_pie(d, (191.9, 173.7), (134.5, 249.6), bow_perp=8, w_head=8, w_tail=3)
    # s10: bottom pie (longest — extends off the canvas bottom per MMH)
    draw_pie(d, (208.9, 208.3), (123.3, 309.1), bow_perp=12, w_head=9, w_tail=3)

    img.save(path)


SELF_CHECK = {
    'visual_ok': None,           # filled after render + eyeball vs GT
    'stroke_count_ok': True,     # 10 primitive calls verified above
    'endpoint_mismatches': [],   # all endpoints are MMH-verbatim (identity)
    'joint_class_mismatches': [], # s3xs4 P will weld (lines cross); Ns fall out
    'overall_pass': None,
    'notes': (
        'P-A-006 stroke-primitive layer with MMH-verbatim anchors. '
        'No whole-half bank primitive fits (田 without extending shu, '
        '㐱 has none). All 8 N-gap joints are geometrically natural '
        'from the MMH endpoints; the sole P joint (s3.mid ⇆ s4.mid) '
        'welds automatically because the two lines cross near ML(66,167).'
    ),
}


if __name__ == '__main__':
    render(os.path.join(HERE, '01_畛.png'))
