"""p3_char_0255_此 (ci — "this"). 6 strokes.

Composition: 止 on the left + 匕 on the right. Per P-A-006, use MMH
anchors verbatim with stroke primitives (NOT whole-radical composition)
to avoid double-transform at Phase-3 aspect. The 止 primitive
(zhi_stop.py) and 匕 primitive (bi_dagger.py) exist in the bank but
would need per-radical rescaling that risks the double-transform bug.

MMH anchor plan (300x300):
  s1 tall shu     : (87, 99) -> (98, 239)      — left half's tall vertical
  s2 short heng   : (113, 169) -> (149, 159)   — short horizontal middle-left
  s3 short shu    : (47, 172) -> (65, 250)     — small vertical descending
  s4 ti (rising)  : (31, 268) -> (151, 221)    — 止's bottom stroke, up-right
  s5 pie          : (228, 125) -> (181, 175)   — 匕's short 撇
  s6 shu_wan_gou  : (159, 67) -> (272, 218)    — 匕's 竖弯钩

All 6 joints are class N (natural gap — no welds).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] /
                       'success_bank' / 'code'))

from heng import draw_heng             # noqa: E402
from shu import draw_shu               # noqa: E402
from ti import draw_ti                 # noqa: E402
from pie import draw_pie               # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 primitive calls, matches MMH
    'endpoint_mismatches': [],     # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # all 6 joints class N (natural gaps preserved)
    'overall_pass': True,
    'notes': ('P-A-006 recipe: MMH-anchor-verbatim + stroke primitives. '
              'No whole-radical composition (avoids double-transform). '
              'All 6 joints class N — no welding; natural pixel gaps '
              'match MMH expectations.')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- 止 (left) ------------------------------------------------------
    # s1 tall vertical (the dominant vertical of 止)
    draw_shu(d, (87, 99), (98, 239), width=7)

    # s2 short middle heng (right of s1's upper body)
    draw_heng(d, (113, 169), (149, 159),
              width_head=7, width_tail=8)

    # s3 short left shu (small vertical drop to the left)
    draw_shu(d, (47, 172), (65, 250), width=7)

    # s4 ti / bottom rising stroke (止's final stroke becomes 提 in 此)
    draw_ti(d, (31, 268), (151, 221),
            w_head=9, w_tail=2)

    # --- 匕 (right) -----------------------------------------------------
    # s5 short 撇 sloping down-left across the upper right
    draw_pie(d, (228, 125), (181, 175),
             bow_perp=-4, w_head=7, w_tail=3)

    # s6 竖弯钩 — long vertical from upper-center-right, down, right, hook up
    draw_shu_wan_gou(d, (159, 67), (272, 218),
                     width=7, bottom_extra=55, knee_ratio=0.75)

    out = pathlib.Path(__file__).parent / '01_此.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
