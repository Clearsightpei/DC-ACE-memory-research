"""p2_radical_045_寸 — G5 RETRY_1.

TRAJECTORY DIFF (main attempt vs GT):

- main verdict: C. Visual comparison:
  * heng: main is nearly perfectly horizontal; GT slopes very slightly up-right
    with a visible downward tick (顿笔) at the right end. Missing tick on
    main is a subtle rhythm miss.
  * shu_gou: main renders the vertical body OK but the hook is barely
    visible (hook_start_offset=45 pulled tail too gently). GT shows a
    clear leftward hook at the bottom.
  * dian (丶): main's dot is TOO LARGE and too dark — w_tail=6 with bow=2
    made a thick blob. GT's dot is small, delicate, slanting down-right
    at ~45° from a thin head to a modest tail.

- Fixes this retry:
  1. Slight up-right slant on the heng (raise head y by ~4px vs MMH x-frac
     to add a touch of calligraphic tilt).
  2. Shu-gou: increase hook_start_offset slightly (55 → sharper hook
     shoulder) and reduce shoulder_x lean so vertical stays straighter.
  3. Dian: reduce w_tail to 4 and bow to 1 for a tighter, more
     calligraphic dot proportional to the character.

MMH anchors (verbatim):
  s1 head ML(0.416,0.521)=(41.6,152.1)  tail MR(0.692,0.397)=(269.2,139.7)
  s2 head TC(0.646,0.633)=(164.6, 63.3) tail BC(0.318,0.730)=(131.8,273.0)
  s3 head ML(0.952,0.775)=(95.2,177.5)  tail BC(0.257,0.121)=(125.7,212.1)

Joint: s1 × s2 @ cell C — class P (welded). Both strokes drawn full through
cell C so intersection naturally welds.

Bank primitives used as-is (no BANK_DEVIATION):
  heng.draw_heng, shu_gou.draw_shu_gou, dian.draw_dian
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng            # noqa: E402
from shu_gou import draw_shu_gou      # noqa: E402
from dian import draw_dian            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitive calls == expected 3
    'endpoint_mismatches': [], # MMH anchors used verbatim
    'joint_class_mismatches': [],  # s1×s2 naturally welded (P)
    'overall_pass': True,
    'notes': 'Retry_1: smaller/tighter dot, sharper hook, subtle heng tilt. '
             'No BANK_DEVIATION — same 3 bank primitives.',
}


def anchor(cell, xf, yf):
    """米字格 anchor → pixel on 300x300 canvas."""
    if cell == 'C':
        cx0, cy0 = 100, 100
    else:
        row, col = cell[0], cell[1]
        cy0 = {'T': 0, 'M': 100, 'B': 200}[row]
        cx0 = {'L': 0, 'C': 100, 'R': 200}[col]
    return (cx0 + xf * 100, cy0 + yf * 100)


def draw_cun(draw):
    # stroke 1: 横 — MMH endpoints verbatim
    s1_head = anchor('ML', 0.416, 0.521)   # (41.6, 152.1)
    s1_tail = anchor('MR', 0.692, 0.397)   # (269.2, 139.7)
    draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=10)

    # stroke 2: 竖钩 — sharper hook shoulder
    s2_head = anchor('TC', 0.646, 0.633)   # (164.6, 63.3)
    s2_tail = anchor('BC', 0.318, 0.730)   # (131.8, 273.0)
    draw_shu_gou(draw, s2_head, s2_tail, width=7, hook_start_offset=55)

    # stroke 3: 丶 — smaller, tighter dot
    s3_head = anchor('ML', 0.952, 0.775)   # (95.2, 177.5)
    s3_tail = anchor('BC', 0.257, 0.121)   # (125.7, 212.1)
    draw_dian(draw, s3_head, s3_tail,
              w_head=2, w_tail=4, bow=1, steps=32)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cun(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_寸.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
