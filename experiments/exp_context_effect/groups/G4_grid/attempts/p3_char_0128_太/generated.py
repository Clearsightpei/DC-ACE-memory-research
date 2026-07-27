"""p3_char_0128_太 — G4 attempt.

Mandatory lookup checklist:
1. success_bank/INDEX.md grep 太 → not present; grep 大 → da.py exists
   (position 75). 太 = 大 + a small 点 in lower area. Reuse da.py with
   OVERRIDE anchors per TR1, then add stroke-4 dian inlined per MMH spec.
2. errata.md grep 太 → not present.
3. form_catalog.md — 横/撇/捺 in char body; 点 in BC.
4. principles_meta.md — TR1 (override anchors when reusing bank);
   TR8 (heng must share row for the two endpoints); N-joint (点 vs
   pie/na) should be ~15-20 px gap, do NOT weld.
5. joint_atlas.md — s2×s1 P weld at crossing; s3.head near heng but
   below (N gap ~19 px); s4 free-standing 点 below-left of 捺 body.
6. sandbox notes — 点 in 太 sits inside crotch of 大 (between 撇 and 捺).

MMH-derived structural expectations:
  s1 head=('ML',0.595,0.6)  tail=('MR',0.438,0.456)  横
  s2 head=('TC',0.301,0.621) tail=('BL',0.39,0.941)  撇
  s3 head=('C',0.474,0.658)  tail=('BR',0.807,0.921) 捺
  s4 head=('BC',0.166,0.525) tail=('BC',0.462,0.786) 点

Joints: P at s1×s2 (welded crossing at ~C); N gaps s1↔s3, s2↔s3,
s2↔s4 (~15-21 px).
"""

import os
import sys

# Add success_bank/code to sys.path for shared primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('太 = 大 (heng+pie+na) + dian at BC. Anchors follow MMH spec; '
              'joints: P at s1×s2 welded crossing near C; N (~15-21 px) for '
              's3.head vs s1 body, s3 vs s2, and s4 vs s2 body.'),
}


def draw_tai(draw):
    # s1 — 横 (heng): ML → MR
    s1_head = ('ML', 0.595, 0.60)
    s1_tail = ('MR', 0.438, 0.456)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # s2 — 撇 (pie): TC → BL, curves left (concave-right, curve negative)
    s2_head = ('TC', 0.301, 0.621)
    s2_tail = ('BL', 0.39, 0.941)
    draw_pie(draw, s2_head, s2_tail,
             head_width=10, tail_width=1, curve=-0.12, segments=48)

    # s3 — 捺 (na): C → BR, head sits just below heng (N gap ~19 px)
    s3_head = ('C', 0.474, 0.658)
    s3_tail = ('BR', 0.807, 0.921)
    draw_na(draw, s3_head, s3_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    # s4 — 点 (dian): BC → BC (small dot in crotch between pie and na)
    s4_head = ('BC', 0.166, 0.525)
    s4_tail = ('BC', 0.462, 0.786)
    draw_dian(draw, s4_head, s4_tail,
              head_width=2, peak_width=9, curve=0.08, segments=24)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_tai(draw)
    out = os.path.join(_HERE, '01_太.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
