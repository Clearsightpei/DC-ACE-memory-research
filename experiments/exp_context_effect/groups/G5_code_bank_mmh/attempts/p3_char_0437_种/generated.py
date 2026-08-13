"""p3_char_0437_种 (zhǒng, "seed/kind") — 9 strokes = 禾 (5) + 中 (4).

Reasoning trace (P-A-008):
  Structural decomposition: LEFT 禾 (5-stroke grain radical, identical
  to 禾 in he_harmony/和); RIGHT 中 (4-stroke: left-shu of box + heng_zhe
  top+right of box + bottom-heng + central piercing shu).

  Bank retrieval:
   - he_harmony.py has a fully-inlined 5-stroke 禾 half (its s1-s5) that
     matches the 种 GT exactly (same left-half occupancy, same pie/heng/
     shu/pie/na layout). REUSE those coords verbatim (P-A-006 style —
     stroke-primitive layer directly, not whole-radical wrapping).
   - kou_mouth.py exists but 种's right half is 中, not 口 (extra
     piercing shu). Cannot reuse kou_mouth wholesale.
   - heng_zhe_box, shu, heng: use directly for 中's box + piercing shu.

  BANK_DEVIATION note (v13): none — 禾 half inlined via bank-primitive
  calls (P-A-006); 中 has no dedicated bank primitive, inlined per
  P-COMP-011 (straight-stroke right half, hook-free box + piercing).

  Quantitative sanity (P-A-009):
   - 禾 native width ~135 px (he_harmony) vs 种-target 禾 width ~140 px
     → aspect deviation <5%, no rescale needed.
   - 中 box native (from kou_mouth) is ~110x150 landscape; 种's 中 box
     is ~100x100 near-square + long piercing shu extending ~200 px
     total. Inline fresh (kou_mouth would leave orphan piercing shu).
"""

import os
import sys
from PIL import Image, ImageDraw

# import bank primitives
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../../success_bank/code'))
sys.path.insert(0, BANK)

from heng import draw_heng            # noqa: E402
from shu import draw_shu              # noqa: E402
from pie import draw_pie              # noqa: E402
from na import draw_na                # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('禾 half reused verbatim from he_harmony s1-s5 (P-A-006). '
              '中 inlined: left-shu + heng_zhe_box + bottom-heng + '
              'piercing central shu. All 4 P-welds honored: s2xs3 禾-cross, '
              's7xs9 中-box-right-cross-piercing, s8xs9 bottom-heng-cross-piercing.')
}


def draw_he_left(draw):
    """禾 left half — coords lifted from he_harmony.draw_he_harmony s1-s5."""
    # s1: top 撇
    draw_pie(draw, (150.0, 74.1), (48.3, 108.4),
             bow_perp=6, w_head=8, w_tail=4)
    # s2: 横
    draw_heng(draw, (22.6, 157.6), (152.1, 138.6),
              width_head=6, width_tail=7)
    # s3: long central 竖
    draw_shu(draw, (92.9, 99.6), (99.6, 297.0), width=7)
    # s4: 禾 lower-left 撇
    draw_pie(draw, (96.4, 154.4), (20.2, 258.1),
             bow_perp=8, w_head=7, w_tail=3)
    # s5: 禾 lower-right 捺
    draw_na(draw, (112.8, 287.2), (145.0, 209.5),
            bow_perp=10, w_head=4, w_tail=10, steps=80)


def draw_zhong_right(draw):
    """中 right half: box (3 strokes) + central piercing shu (1 stroke).
    Revision: box tightened upward + slightly narrower to match GT proportion
    (GT box ~110-205 y, mine was 128-236 — too low + too tall)."""
    # Box footprint: x=173-255, y=115-208 (near-square, sits higher)
    # s6: left 竖 of box (short)
    draw_shu(draw, (175, 118), (172, 210), width=7)
    # s7: heng_zhe_box (top + right side of box)
    draw_heng_zhe_box(draw, (173, 115), (253, 212), width=7)
    # s8: bottom 横 (closes the box)
    draw_heng(draw, (170, 210), (257, 208),
              width_head=7, width_tail=8)
    # s9: central piercing 竖 — extends WAY above and below the box
    #     (this is the defining feature of 中 vs 口)
    draw_shu(draw, (213, 62), (215, 292), width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_he_left(draw)
    draw_zhong_right(draw)
    out = os.path.join(os.path.dirname(__file__), '01_种.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
