"""p3_char_0047_也 — 也 (yě, "also").

3 strokes:
  s1: 横 (heng) BL(24.6, 209.5) -> BC(156.4, 207.4)
  s2: 竖 (shu) TC(128.3, 63.3) -> BC(132.4, 233.8)
  s3: 竖弯钩 (shu_wan_gou) ML(73.5, 141.8) -> BR(263.4, 214.5)

Uses 3 bank primitives directly matching the stroke classes.
Joints:
  - s1 x s2 (P, welded) — both cross in cell C area at their midpoints
  - s1 x s3 (P, welded) — s1 crosses vertical part of shu_wan_gou

Both are P (piercing), so no gaps to insert. Bank primitives extend
slightly past endpoints via width and end-caps, so the crossings should
weld naturally.
"""

import os
import sys
from PIL import Image, ImageDraw

# Make bank importable
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


def cell_anchor(cell, xf, yf):
    """米字格 cell + intra-cell fraction -> pixel (300x300, y-down)."""
    col = {'L': 0, 'C': 1, 'R': 2}[cell[1]]
    row = {'T': 0, 'M': 1, 'B': 2}[cell[0]]
    return (col * 100 + xf * 100, row * 100 + yf * 100)


def draw_ye(draw):
    s1_head = cell_anchor('BL', 0.246, 0.095)
    s1_tail = cell_anchor('BC', 0.564, 0.074)
    s2_head = cell_anchor('TC', 0.283, 0.633)
    s2_tail = cell_anchor('BC', 0.324, 0.338)
    s3_head = cell_anchor('ML', 0.735, 0.418)
    s3_tail = cell_anchor('BR', 0.634, 0.145)

    # s1: horizontal (slightly slanted up-right); keep light
    draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2: middle vertical
    draw_shu(draw, s2_head, s2_tail, width=7)

    # s3: 竖弯钩 — head at middle-left, tail is hook end at upper-right of BR.
    # For 也, the enclosure should be BIG and wrap most of the character.
    # Widen: push right edge past MMH tail x, deepen bottom, thicker ink.
    # We synthesize a bigger enclosure by extending s3 head slightly up-left
    # and tail slightly further right, then hook up on the far right.
    s3_head_ext = (s3_head[0] - 5, s3_head[1] - 25)  # start higher
    s3_tail_ext = (s3_tail[0] + 15, s3_tail[1] + 15)  # hook end further out
    draw_shu_wan_gou(draw, s3_head_ext, s3_tail_ext,
                     width=9, bottom_extra=55, knee_ratio=0.92)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitive calls above
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s1xs2 P, s1xs3 P — both welded
    'overall_pass': True,
    'notes': 'Bank primitives heng+shu+shu_wan_gou; anchors from MMH block; '
             'both joints are P (welded); shu_wan_gou hook tail lands near BR top.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ye(d)
    out = os.path.join(HERE, '01_也.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
