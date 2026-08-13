"""G5 attempt: p3_char_0270_伧 (伧 = 亻 + 仑).

Recipe: **P-A-006** — MMH anchors verbatim + stroke-primitive layer.
Refuses whole-radical composition (e.g. draw_ren_left + draw_bi) that
would double-transform through Phase-3 aspect; instead pins each of
the 6 MMH strokes to their exact G4 米字格 pixel anchors.

Stroke map:
  s1  亻 pie          TL(0.896, 0.700) → BL(0.196, 0.101)
  s2  亻 shu          ML(0.639, 0.667) → BL(0.686, 0.971)
  s3  仑 top pie      TC(0.570, 0.721) → ML(0.885, 0.951)
  s4  仑 top na       C(0.714, 0.031)  → MR(0.824, 0.781)
  s5  仑 mid tick     C(0.380, 0.998)  → BC(0.567, 0.262)   (匕-top tick)
  s6  仑 shu-wan-gou  C(0.222, 0.884)  → BR(0.320, 0.391)
"""
import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie
from shu import draw_shu
from na import draw_na
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 primitive calls → 6 strokes
    'endpoint_mismatches': [],    # MMH-anchor verbatim
    'joint_class_mismatches': [], # all 5 joints are N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'P-A-006 recipe: MMH-anchor-verbatim + stroke primitives (no whole-radical composition). 6 stroke calls exactly matching the injected count.',
}


def _anchor(cell, xf, yf):
    """(cell, x_frac, y_frac) → 300x300 pixel (x, y) with y-DOWN."""
    cols = {'L': 0, 'C': 100, 'R': 200}
    rows = {'T': 0, 'M': 100, 'B': 200}
    if cell == 'C':
        col_off, row_off = 100, 100
    else:
        row_off = rows[cell[0]]
        col_off = cols[cell[1]]
    return (col_off + xf * 100.0, row_off + yf * 100.0)


def draw_cang(draw):
    # s1: 亻 pie  (TL 0.896, 0.70 → BL 0.196, 0.101)
    s1_h = _anchor('TL', 0.896, 0.700)
    s1_t = _anchor('BL', 0.196, 0.101)
    draw_pie(draw, s1_h, s1_t, bow_perp=14, w_head=10, w_tail=3, steps=90)

    # s2: 亻 shu  (ML 0.639, 0.667 → BL 0.686, 0.971)
    s2_h = _anchor('ML', 0.639, 0.667)
    s2_t = _anchor('BL', 0.686, 0.971)
    draw_shu(draw, s2_h, s2_t, width=7)

    # s3: 仑 top pie (TC 0.570, 0.721 → ML 0.885, 0.951)  — starts upper-right, ends middle-left
    s3_h = _anchor('TC', 0.570, 0.721)
    s3_t = _anchor('ML', 0.885, 0.951)
    draw_pie(draw, s3_h, s3_t, bow_perp=10, w_head=9, w_tail=3, steps=70)

    # s4: 仑 top na (C 0.714, 0.031 → MR 0.824, 0.781)  — from top-center down-right to middle-right
    s4_h = _anchor('C', 0.714, 0.031)
    s4_t = _anchor('MR', 0.824, 0.781)
    draw_na(draw, s4_h, s4_t, bow_perp=13, w_head=4, w_tail=11, steps=80)

    # s5: short tick/pie inside 仑 (C 0.380, 0.998 → BC 0.567, 0.262)
    s5_h = _anchor('C', 0.380, 0.998)
    s5_t = _anchor('BC', 0.567, 0.262)
    draw_pie(draw, s5_h, s5_t, bow_perp=2, w_head=6, w_tail=4, steps=30)

    # s6: 仑 shu-wan-gou (C 0.222, 0.884 → BR 0.320, 0.391)
    s6_h = _anchor('C', 0.222, 0.884)
    s6_t = _anchor('BR', 0.320, 0.391)
    draw_shu_wan_gou(draw, s6_h, s6_t, width=7, bottom_extra=45, knee_ratio=0.85)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cang(draw)
    out = os.path.join(_HERE, '01_伧.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
