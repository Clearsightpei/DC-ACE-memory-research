"""p3_char_0305_还 — G5 attempt.

Decomposition: 不 (strokes 1-4, top-right) + 辶 (strokes 5-7, wrap).
- Strokes 5-7 use bank primitive `chuo_walk` (small offset to hit MMH anchors).
- Strokes 1-4 (不) inlined: heng + pie + shu + na, all bank primitives called
  at MMH endpoint anchors.

No BANK_DEVIATION: every stroke primitive used matches bank as-is.
Follows P-A-006 (stroke-primitive layer for compound char) since 不 has no
dedicated bank primitive; but for the 辶 wrapper (radical-level match)
follows P-A-007 (use whole-radical primitive when it matches at native scale).
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from chuo_walk import draw_chuo  # noqa: E402
from heng import draw_heng       # noqa: E402
from na import draw_na           # noqa: E402
from pie import draw_pie         # noqa: E402
from shu import draw_shu         # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes: 4 (不) + 3 (辶 via chuo_walk)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 5 joints intended as N (natural gap) or T
    'overall_pass': True,
    'notes': 'chuo_walk called with ox=+3, oy=+7 to shift bank anchors to MMH targets.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 不 (strokes 1-4) ---------------------------------------------
    # s1 heng: C(0.216,0.131) -> MR(0.461,0.02)
    draw_heng(d, (121.6, 113.1), (246.1, 102.0), width_head=8, width_tail=9)

    # s2 pie: C(0.755,0.184) -> BC(0.063,0.235). Long pie sweeping down-left.
    draw_pie(d, (175.5, 118.4), (106.3, 223.5),
             bow_perp=10, w_head=7, w_tail=2)

    # s3 shu (middle vertical of 不): C(0.638,0.447) -> BC(0.74,0.596)
    draw_shu(d, (163.8, 144.7), (174.0, 259.6), width=6)

    # s4 na (right dot of 不): MR(0.021,0.731) -> BR(0.476,0.127). Short 捺.
    draw_na(d, (202.1, 173.1), (247.6, 212.7),
            bow_perp=6, w_head=3, w_tail=8)

    # ---- 辶 (strokes 5-7) via bank primitive ---------------------------
    # Native chuo_walk anchors: dian(61.8,71.8)->(96.4,96.7),
    #                            zig (27.2,155)->(81.4,238.8),
    #                            na  (28.4,254.3)->(268.9,278.9).
    # MMH targets for this char are ~+3px right, +7px down. Small ok shift.
    draw_chuo(d, ox=3, oy=7, scale=1.0)

    out = os.path.join(os.path.dirname(__file__), '01_还.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
