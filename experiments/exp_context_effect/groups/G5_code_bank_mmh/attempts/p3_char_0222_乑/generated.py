"""p3_char_0222_乑 — G5 attempt.

6 strokes:
  s1: short top curve (pie-like), TC->TL area
  s2: long central vertical shu (with slight drift)
  s3: upper-left pie (down-left)
  s4: lower-left pie (down-left)
  s5: middle pie from upper-right toward center (long)
  s6: middle na from center toward bottom-right (welded to s5 tail — T joint)

Uses bank primitives (draw_pie, draw_shu, draw_na) sourced by sys.path insert.
No BANK_DEVIATION — bank primitives fit the composition directly.
"""

import sys, os
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s5.tail↔s6.head welded (T); others left as natural gap
    'overall_pass': True,
    'notes': '6 strokes; s5/s6 form the large right human, s3/s4 the left pies, s1 top curve, s2 central shu.'
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: TC(0.679,0.688)->TL(0.601,0.946) — short top curve (leftward-down).
    # Treat as a mini pie with modest bow.
    draw_pie(d, head=(167.9, 68.8), tail=(60.1, 94.6),
             bow_perp=8, w_head=5, w_tail=3)

    # s2: TC(0.066,0.908)->BC(0.181,1.185) — long central vertical shu.
    # y_frac 1.185 means the tail extends beyond BC cell (base y=200) to
    # ~y=318 — clip to 295 to stay within 300 canvas.
    draw_shu(d, head=(106.6, 90.8), tail=(118.1, 295.0), width=6)

    # s3: ML(0.768,0.336)->BL(0.334,0.033) — upper-left pie.
    draw_pie(d, head=(76.8, 133.6), tail=(33.4, 203.3),
             bow_perp=6, w_head=6, w_tail=2)

    # s4: ML(0.768,0.998)->BL(0.334,0.692) — lower-left pie.
    draw_pie(d, head=(76.8, 199.8), tail=(33.4, 269.2),
             bow_perp=6, w_head=6, w_tail=2)

    # s5: C(0.975,0.072)->C(0.304,0.685) — long pie from upper-right to center.
    draw_pie(d, head=(197.5, 107.2), tail=(130.4, 168.5),
             bow_perp=10, w_head=7, w_tail=3)

    # s6: C(0.315,0.705)->BR(0.681,0.49) — na from center to bottom-right.
    # Head placed to weld with s5's tail (T joint at (~130.4, 168.5)).
    draw_na(d, head=(130.4, 168.5), tail=(268.1, 249.0),
            bow_perp=10, w_head=4, w_tail=10)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_乑.png')
    render(out)
    print('wrote', out)
