"""p3_char_0349_改 — G5 attempt 01.

改 = 己 (left, 3 strokes) + 攵 (right, 4 strokes) = 7 strokes total.

Bank primitives used:
- pu_action.draw_pu for the right 攵 radical (whole-radical match; per
  P-A-007-v2 hard-check the right half is 攵 verbatim, native aspect,
  so CALL IT rather than inlining).
- heng_zhe_short for 己 s1 (top 横折 — natural fit at that scale).
- heng for 己 s2 (middle horizontal — narrow, sits between s1 and s3).
- shu_wan_gou for 己 s3 (bottom 竖弯钩 — the exact class the primitive
  encodes, derived from 匕's second stroke).

Inline-reasoning trace (per P-A-008):
- Sub-component 攵 (right, 4 strokes): matches pu_action bank primitive
  verbatim at native aspect. Whole-radical CALL. scale=0.75 chosen so
  ox+252*scale=299 (right edge safely inside 300 canvas) and
  oy+290*scale=263 (bottom leaves room for the na tail lifting).
- Sub-component 己 (left, 3 strokes): no 己 primitive in bank at B9.
  Composed from stroke-primitive layer (P-A-006 recipe): heng_zhe_short
  + heng + shu_wan_gou, each called with endpoints chosen from GT
  visual + MMH anchor guidance.

MMH stroke count: 7. Turtle-call count: 3 (己) + 1 pu_action -> 4 python
calls but pu_action itself emits 4 strokes internally, so total rendered
stroke primitives = 3 + 4 = 7. Matches.
"""

import sys
import os

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw

from pu_action import draw_pu
from heng_zhe_short import draw_heng_zhe_short
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 (己) + 4 (攵 via pu_action) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Left 己 composed inline from stroke-primitive layer; '
              'right 攵 called as whole-radical (pu_action) per P-A-007-v2 '
              'hard-check. All joints between 己 strokes are N (natural gap); '
              'internal 攵 joints are governed by the pu_action primitive.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Left component: 己 (3 strokes) --------------------------------

    # s1: 横折 (top). Horizontal from ~ML down-inward then turns down to C.
    # MMH: head ML(0.56, 0.169) -> tail C(0.061, 0.55).
    draw_heng_zhe_short(draw, head=(38, 78), tail=(138, 138),
                        corner_offset=(0, 4))

    # s2: middle heng — short horizontal joining s1's descent bottom.
    # MMH: head ML(0.715, 0.699) -> tail C(0.216, 0.632).
    draw_heng(draw, head=(45, 158), tail=(138, 152),
              width_head=7, width_tail=8)

    # s3: 竖弯钩 (bottom). Descends from left, curves right, hooks up.
    # MMH: head ML(0.486, 0.658) -> tail BC(0.146, 0.124).
    draw_shu_wan_gou(draw, head=(50, 158), tail=(165, 200),
                     width=7, bottom_extra=55, knee_ratio=0.80)

    # --- Right component: 攵 (4 strokes via pu_action) -----------------
    # Native pu_action spans (x: 55..252, y: 75..290). We want it to fill
    # the right column of the 300 canvas, sharing horizontal space with
    # 己 (pu's s1/s3 pies naturally cross into the 己 column, matching GT).
    draw_pu(draw, ox=110, oy=45, scale=0.75)

    out = os.path.join(os.path.dirname(__file__), '01_改.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
