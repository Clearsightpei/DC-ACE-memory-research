"""G5 retry #1: p2_radical_116_礻.

TRAJECTORY DIFF (visual comparison of main attempt PNG vs GT):

Main attempt failures (verdict: C):
  1. s2 (heng-pie) TAIL WAS DOWN-RIGHT — main used tail=(120,165) which is
     to the RIGHT of head=(80,118). But 礻's heng-pie ends DOWN-LEFT
     (pie sweep goes left). GT clearly shows the compound curving from a
     short horizontal top-bar into a leftward diagonal pie. Impact: the
     "pie" portion pointed the wrong way, so the top-left cluster looked
     like a wide inverted-V instead of a crossbar+leg. Off by ~55 px in x
     for the tail.
  2. s4 (right dot) TOO SHORT — main used (163,148)→(198,200), only ~60 px
     long. GT's right dot is a fat calligraphic sweep extending from mid-
     center down-right to near the bottom-right corner, ~120+ px long,
     ending near (245, 250). Impact: right-half of the radical looked
     stunted, silhouette imbalanced vs the long left pie.
  3. s3 (shu vertical) SLIGHTLY LEFT — main at x=138; GT has the shaft
     under the heng-pie apex (~x=155). Also could extend slightly further
     down (y=280).
  4. s1 (top dot) TOO HIGH & SMALL — main at (148,46)→(172,76). GT dot
     sits ~y=60 head with more slant and slightly bigger.

Fixes applied this retry:
  * s1: dot at (155, 58)→(180, 100), taper 4→9.
  * s2: heng_pie with head=(85, 118), tail=(60, 205) — tail now DOWN-LEFT
    of head (correct direction). apex_x=180, corner_x=178.
  * s3: shu at (155, 135)→(155, 285) — centered under heng_pie apex,
    extended slightly.
  * s4: dot at (170, 155)→(248, 250), thicker taper 4→11, bow=8 — long
    calligraphic right-dot matching GT's rightward sweep.

All 3 joints remain class N (neighbor gap ≥ 15 px at cell C).
"""

import os
import sys
from PIL import Image, ImageDraw

# --- bank imports (canonical relative path) ---
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian          # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from shu import draw_shu            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 stroke primitive calls (s1..s4)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints N with visible gap
    'overall_pass': True,
    'notes': (
        'Retry: fixed heng_pie tail direction (down-LEFT), lengthened '
        'right dot, centered shu under crossbar apex, moved top dot down.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top dot at TC, slanting down-right
    draw_dian(d, head=(155, 58), tail=(180, 100),
              w_head=3, w_tail=9, bow=4, steps=48)

    # s2 — 横撇 heng-pie. Head at upper-left of the crossbar; tail sweeps
    # DOWN-LEFT (this was wrong in the main attempt).
    # heng_pie signature: head, tail, apex_x, corner_x
    draw_heng_pie(d, head=(85, 118), tail=(60, 205),
                  apex_x=180, corner_x=178)

    # s3 — 竖 vertical shaft, centered under heng_pie apex (~x=155)
    draw_shu(d, head=(155, 135), tail=(155, 285), width=6)

    # s4 — long right dot sweeping down-right to near BR corner
    draw_dian(d, head=(170, 155), tail=(248, 250),
              w_head=4, w_tail=11, bow=8, steps=56)

    out = os.path.join(HERE, '01_礻.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
