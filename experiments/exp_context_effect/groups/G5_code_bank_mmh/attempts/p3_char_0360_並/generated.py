"""p3_char_0360_並 (bìng, "and, together") — 8 strokes.

Sub-component analysis (P-A-007-v2 hard-check):
  並 = 亚-pattern (6 strokes: top heng + 2 verticals + 2 mid outer dians +
  bottom heng) PLUS 2 additional top pies. Bank has draw_ya_asia (6 strokes)
  but the target's MMH stroke count is 8, so ya_asia does NOT match at any
  scale — the required stroke count differs. Hence: DO NOT call the whole
  radical; use stroke-primitive layer (P-A-006) with MMH-verbatim anchors,
  inlining each stroke with heng/shu/dian/pie primitives.

Per-stroke inline reasoning trace (P-A-008):
  s1: top-left pie (short down-right) — bank draw_pie fits, MMH endpoints TL->C.
  s2: top-inner pie (short down-left) — bank draw_pie fits (mirror bow_perp
      via head/tail direction), MMH endpoints TC->C.
  s3: middle heng (upper crossbeam), left-to-right — draw_heng fits, ML->MR.
  s4: left long vertical (through middle heng to bottom) — draw_shu fits.
  s5: right long vertical (through middle heng to bottom) — draw_shu fits.
  s6: left-outer dian (down-right) — draw_dian fits (like ya s4).
  s7: right-outer dian/pie (down-left) — draw_dian fits (like ya s5).
  s8: baseline heng (longest, heaviest) — draw_heng fits.

All 7 joints per MMH are N-class (natural gap ≈ 14-21 px). We inline all
strokes verbatim from MMH pixel anchors, which produces the correct gaps
naturally (heng ends short of vertical, verticals cross the middle heng
without weld artifacts — PIL uniform-line rendering).
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from dian import draw_dian  # noqa: E402
from pie import draw_pie    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim endpoints. All 7 joints N-class (natural gap).'
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top-left short pie (TL -> C), down-right
    draw_pie(d, (98.4, 76.8), (124.2, 105.2),
             bow_perp=4, w_head=4, w_tail=3, steps=48)

    # s2: top-inner short pie (TC -> C), down-left
    draw_pie(d, (189.3, 57.1), (156.2, 123.0),
             bow_perp=6, w_head=4, w_tail=3, steps=56)

    # s3: middle upper crossbeam heng (ML -> MR), slight rise
    draw_heng(d, (69.7, 139.2), (236.4, 128.6),
              width_head=7, width_tail=8)

    # s4: LEFT long vertical (C -> BC)
    draw_shu(d, (111.6, 144.1), (119.8, 271.9), width=7)

    # s5: RIGHT long vertical (C -> BC)
    draw_shu(d, (163.5, 136.5), (167.0, 268.1), width=7)

    # s6: left-outer dian (down-right)
    draw_dian(d, (65.3, 192.8), (89.9, 230.6),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s7: right-outer dian (down-left)
    draw_dian(d, (223.5, 165.2), (181.1, 227.9),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s8: baseline heng (long, heaviest)
    draw_heng(d, (33.4, 285.1), (273.9, 282.7),
              width_head=9, width_tail=11)

    return img


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img = render()
    img.save(os.path.join(out_dir, "01_並.png"))
    print("wrote 01_並.png")
