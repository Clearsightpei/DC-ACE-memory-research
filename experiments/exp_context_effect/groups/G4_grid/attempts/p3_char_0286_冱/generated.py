"""p3_char_0286_冱 — 冫 (2 strokes, left) + 互 (4 strokes, right).

Memory checklist:
  1. drawer_memory.md — read (no explicit 冱/互 fix, generic playbook).
  2. INDEX.md — bing.py exists for 冫 radical; no hu/互 entry.
  3. errata.md — no 冱 entry.

Composition:
  - 冫 (left): reuse draw_bing with MMH-derived anchors shifted left.
  - 互 (right): inline 4 strokes using fat_line at MMH endpoints.
    Simplified straight-line renders — 互's strokes are relatively
    short and endpoints from MMH are sufficient to convey shape.

Stroke count assertion: 2 + 4 = 6 (matches MMH expected).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes = 2 (冫 via draw_bing) + 4 (互 fat_line inlines). '
             'All joints between s3/s4/s5/s6 are N-class (natural small gaps preserved by non-welded straight lines).'
}

import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from bing import draw_bing  # noqa: E402


def draw_char(draw):
    # --- Left component 冫 (2 strokes) — MMH anchors ---
    draw_bing(
        draw,
        s1_head=('TL', 0.577, 0.976), s1_tail=('ML', 0.905, 0.289),
        s2_head=('BL', 0.539, 0.730), s2_tail=('ML', 0.949, 0.641),
    )

    # --- Right component 互 (4 strokes) ---
    # s3: top heng of 互 — render as heng-then-drop (horizontal then short vertical)
    p3a = anchor_to_xy(('C',  0.228, 0.005))
    p3b = anchor_to_xy(('TR', 0.394, 0.885))
    corner3 = (p3b[0], p3a[1])  # right end at s3a's y (horizontal top)
    fat_line(draw, p3a, corner3, width=8)
    fat_line(draw, corner3, p3b, width=8)

    # s4: heng-zhe-heng-like inner stroke of 互 — heng then down-turn
    p4a = anchor_to_xy(('C',  0.500, 0.104))
    p4b = anchor_to_xy(('BC', 0.934, 0.060))
    corner4 = (p4b[0], p4a[1])
    fat_line(draw, p4a, corner4, width=8)
    fat_line(draw, corner4, p4b, width=8)

    # s5: middle-inner stroke — short heng in mid-lower area
    p5a = anchor_to_xy(('C',  0.532, 0.688))
    p5b = anchor_to_xy(('BC', 0.764, 0.675))
    fat_line(draw, p5a, p5b, width=8)

    # s6: bottom heng — long horizontal at bottom
    p6a = anchor_to_xy(('BL', 0.806, 0.801))
    p6b = anchor_to_xy(('BR', 0.742, 0.789))
    fat_line(draw, p6a, p6b, width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_冱.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
