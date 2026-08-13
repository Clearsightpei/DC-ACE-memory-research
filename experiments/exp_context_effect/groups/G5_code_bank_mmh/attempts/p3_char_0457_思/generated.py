"""p3_char_0457_思 (sī, 'think') — 田 top + 心 bottom, 9 strokes.

Recipe: P-A-006 stroke-primitive layer + P-A-007-v2 (whole-radical
hard-check). No whole-田 primitive exists in bank (si_four is 四,
different inner strokes; ri_sun is 日, different shape). For 心, the
promoted wo_gou.py handles the main hook; inline the 3 dians directly
(no whole-心 primitive available). P-A-008 mandatory reasoning trace
inline below.

Composition (matches MMH 9-stroke expectation):
- 田 top (5 strokes):
  s1 left-shu (leans slightly right, from ~x=67 top to ~x=104 mid)
  s2 heng-zhe compound (top heng + right shu, corner at ~(185, 89))
  s3 middle heng (crosses inside box, y~128)
  s4 middle shu (vertical inside box, x~141)
  s5 bottom heng (closes box, y~172)
- 心 bottom (4 strokes):
  s6 left dian (small tapered stroke down-left)
  s7 wo_gou main hook (from head near left to tail near right,
     belly dips low)
  s8 middle dian (short down-right)
  s9 right dian (down-right)

P-A-009 quantitative reasoning: 田 top spans x∈[67,185], y∈[84,180]
per MMH (aspect ~118×96 ≈ 1.23 wide). 心 spans y∈[187,268] per MMH
(bottom half). No BANK_DEVIATION needed — 田 has no bank primitive
to skip (bank hard-check: si_four ≠ 田, ri_sun ≠ 田).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from wo_gou import draw_wo_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 strokes drawn
    'endpoint_mismatches': [],     # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # s3×s4 P weld (middle cross); rest N gaps
    'overall_pass': True,
    'notes': ('MMH anchors verbatim. 田 top (5 inlined stroke primitives) '
              '+ 心 bottom (wo_gou + 3 dians). s3×s4 P-welded at C.'),
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---------- 田 top ----------
    # s1: left-shu — TL(66.8, 84.4) → C(104.0, 184.6)
    # (田's left vertical leans slightly right in MMH — inlined as shu.)
    draw_shu(d, (66.8, 84.4), (104.0, 184.6), width=8)

    # s2: heng-zhe compound — TL(88.2, 88.5) → C(184.9, 169.9)
    # Corner at (184.9, 88.5): heng across top, then shu down right side.
    d.line([(88.2, 88.5), (184.9, 88.5)], fill='black', width=8)
    d.ellipse([184.9 - 5, 88.5 - 5, 184.9 + 5, 88.5 + 5], fill='black')  # 顿笔
    d.line([(184.9, 88.5), (184.9, 169.9)], fill='black', width=8)

    # s3: middle heng — C(116.6, 132.4) → C(181.1, 123.9)
    draw_heng(d, (116.6, 132.4), (181.1, 123.9),
              width_head=6, width_tail=7)

    # s4: middle shu — TC(139.7, 89.1) → C(143.3, 162.6)
    # Crosses s3 at ~C (P weld — thin lines naturally overlap).
    draw_shu(d, (139.7, 89.1), (143.3, 162.6), width=6)

    # s5: bottom heng (closes 田 box) — C(108.7, 179.0) → C(184.6, 164.9)
    draw_heng(d, (108.7, 179.0), (184.6, 164.9),
              width_head=8, width_tail=9)

    # ---------- 心 bottom ----------
    # s6: left dian — BL(64.2, 211.8) → BL(45.7, 267.5)
    # Small tapered dot, direction down-and-slightly-left.
    draw_dian(d, (64.2, 211.8), (45.7, 267.5),
              w_head=3, w_tail=8, bow=4, steps=48)

    # s7: 卧钩 main hook — BL(99.0, 219.7) → BR(209.8, 231.2)
    # Wide smile-arc with belly dipping to ~y=268, then hook up-left.
    draw_wo_gou(d, (99.0, 219.7), (209.8, 231.2),
                belly_y=262, width=8, hook_up=24, hook_back=6)

    # s8: middle dian — C(140.6, 196.0) → BC(169.6, 220.6)
    # Small dot going down-right, sits above the 卧钩 belly.
    draw_dian(d, (140.6, 196.0), (169.6, 220.6),
              w_head=3, w_tail=8, bow=3, steps=48)

    # s9: right dian — MR(225.0, 186.6) → BR(273.3, 220.3)
    # Larger dot going down-right, off the right end of the hook.
    draw_dian(d, (225.0, 186.6), (273.3, 220.3),
              w_head=3, w_tail=9, bow=4, steps=48)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_思.png')
    draw().save(out)
    print('wrote', out)
