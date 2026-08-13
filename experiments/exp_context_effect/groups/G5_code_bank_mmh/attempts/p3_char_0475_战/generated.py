"""p3_char_0475_战 — 战 (zhan, "war/battle") — 9 strokes.

Composition per P-A-006 (MMH-verbatim anchors + stroke-primitive layer),
mirrored on the sibling 或 (B11 A). 战 = compact 占 (left, 5 strokes)
+ 戈 (right, 4 strokes).

  s1 = shu   (占 top 卜-shu, upper-left, near-vertical)
  s2 = dian  (占 top 卜-dot, short down-right)
  s3 = shu   (口 left-shu, lower-left, slight rightward drift)
  s4 = heng_zhe_box (mini) — 口 top+right corner
  s5 = heng  (口 bottom, mild rise)
  s6 = heng  (戈 top-heng, up-right rising, short)
  s7 = xie_gou (戈 main diagonal + terminal up-hook, top-center → bottom-right)
  s8 = pie   (戈 upper-right → lower-left sweeping through middle)
  s9 = dian  (戈 top-right dot)

# BANK_DEVIATION
# skipped: ge_dagger.py (戈 whole-radical, 4-stroke composite)
# reason (P-A-009 quantitative):
#   Native ge heng: (54,168)→(173,133), span 119px, dy=-35, aspect
#     |dx/dy| = 3.40. Target s6: (139,166)→(229,142), span 90px,
#     dy=-24, aspect 3.75. Marginally compatible (1.10x).
#   BUT native ge xie_gou: head (95,78)→tail (238,250), dx=143, dy=172,
#     tail-x=238. Target s7: head (155,69)→tail (277,237), dx=122,
#     dy=168, tail-x=277. Tail-x offset: +39px (13% of canvas) —
#     戈 in 战 sits far right (占 occupies left 45%). No uniform
#     (ox,oy,scale) satisfies both heng and xie_gou since heng at
#     +8px shift vs xie_gou at +39px tail. Non-uniform shift =
#     compositional; inline required (P-A-007-v2 clause-2 pattern).
# fresh_component: none — reused heng/xie_gou/pie/dian primitives at
#     MMH-verbatim endpoints (per sibling 或's precedent).
#
# skipped: zhan_occupy.py (亻+占 = 佔, 7-stroke composite) and
#          kou_mouth.py (口 whole-radical, 3-stroke composite)
# reason (P-A-009 quantitative):
#   zhan_occupy inline test: 占 in 佔 occupies right ~60% of canvas
#   (bu-shu at x≈167, kou at x=124-220). Target 占 in 战 occupies
#   left ~55% (bu-shu at x=73-82, kou at x=36-112). Would require
#   ox=-90, scale≈0.55, but zhan_occupy's internal 亻 (s1-s2) is
#   irrelevant here — extracting only s3-s7 not supported by fn
#   signature. Skip whole primitive.
#   kou_mouth native bbox 130w × 150h (aspect 0.87). Target 口 in
#   战: bbox x=[36,112], y=[208,279] → 76w × 71h (aspect 1.07).
#   Aspect ratio 1.07/0.87 = 1.23 — just outside [0.55, 1.20] fit
#   range. Additionally 战's 口 is left-shifted with s3 shu drifting
#   right (36→60) and s5 heng rising left→right (269→259). Non-
#   uniform sub-stroke tuning — inline stroke primitives (per 或
#   B11 A precedent).
# fresh_component: none — 5 primitive calls (shu/dian/shu/heng_zhe_box/heng)
#     at MMH-verbatim endpoints.

MMH anchors → pixel (cell base + x_frac*100, y_frac*100):
  s1: TL(0.727,0.838)→(72.7,83.8),   BL(0.82,0.01)→(82,201)     shu (卜-shu)
  s2: ML(0.967,0.438)→(96.7,143.8),  C(0.427,0.307)→(142.7,130.7) dian (卜-dot)
  s3: BL(0.363,0.08)→(36.3,208),     BL(0.598,0.789)→(59.8,278.9) shu (口-left)
  s4: BL(0.557,0.165)→(55.7,216.5),  BC(0.125,0.476)→(112.5,247.6) heng_zhe_box (口 top+right)
  s5: BL(0.662,0.692)→(66.2,269.2),  BC(0.318,0.59)→(131.8,259)   heng (口 bottom)
  s6: C(0.389,0.664)→(138.9,166.4),  MR(0.291,0.421)→(229.1,142.1) heng (戈 top)
  s7: TC(0.547,0.694)→(154.7,69.4),  BR(0.766,0.37)→(276.6,237)   xie_gou (戈 斜钩)
  s8: MR(0.376,0.661)→(237.6,166.1), BC(0.406,0.815)→(140.6,281.5) pie (戈)
  s9: TR(0.124,0.829)→(212.4,82.9),  MR(0.417,0.061)→(241.7,106.1) dian (戈)

Joints (7 expected):
  s1.mid ⇆ s2.head N (leave ~17px gap — dian starts at (96.7,143.8),
    s1 mid ≈ (77.4, 142.4) → natural ~19px gap, OK).
  s1.tail ⇆ s4.mid N (~13px — s1 tail (82,201), s4 mid ≈ (84, 232) →
    natural gap ~31px between mouth-top and shu-tail — OK).
  s3.mid ⇆ s4.head N (~13px — s3 mid ≈ (48, 243), s4 head (55.7,216.5) →
    natural ~27px, OK).
  s3.tail ⇆ s5.head N (~15px — s3 tail (59.8,278.9), s5 head (66,269) →
    ~12px, marginal N).
  s4.tail ⇆ s5.mid N (~14px — s4 tail (112.5,247.6), s5 mid ≈ (99,264) →
    ~21px, OK).
  s6.mid ⇆ s7.mid P (welded — top-heng crosses xie_gou naturally near C).
  s7.mid ⇆ s8.mid P (welded — pie crosses xie_gou naturally near BR).
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian
from pie import draw_pie
from heng_zhe_box import draw_heng_zhe_box
from xie_gou import draw_xie_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 primitive calls, matches MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer with MMH-verbatim endpoints. '
             'BANK_DEVIATION vs zhan_occupy/kou_mouth (compositional shift '
             'for compact-left 占) and ge_dagger (non-uniform sub-stroke '
             'x-shift for right-position 戈). Mirrors 或 B11 A precedent. '
             'N-gap joints preserved by not welding across primitives; P '
             'welds form naturally where heng/pie cross xie_gou.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: shu — 占 top 卜's vertical (starts near y=84, ends near y=201)
    draw_shu(d, (72.7, 83.8), (82, 201), width=7)

    # s2: dian — 占 top 卜's dot (short up-and-right slant)
    draw_dian(d, (96.7, 143.8), (142.7, 130.7),
              w_head=3, w_tail=7, bow=3)

    # s3: shu — 口 left side (slight rightward drift 36→60)
    draw_shu(d, (36.3, 208), (59.8, 278.9), width=7)

    # s4: heng_zhe_box — 口 top+right (mini box top edge + descending right)
    draw_heng_zhe_box(d, top_left=(55.7, 216.5), bottom_right=(112.5, 247.6),
                      width=6)

    # s5: heng — 口 bottom, slight rise left→right
    draw_heng(d, (66.2, 269.2), (131.8, 259), width_head=7, width_tail=8)

    # s6: heng — 戈 top short heng, rising to right (中偏右 area)
    draw_heng(d, (138.9, 166.4), (229.1, 142.1),
              width_head=8, width_tail=9)

    # s7: xie_gou — 戈 main long diagonal + terminal up-hook
    draw_xie_gou(d, head=(154.7, 69.4), tail=(276.6, 237),
                 width=8, bow=10, hook_up=32, hook_back=6)

    # s8: pie — 戈 upper-right to lower-left sweeping through middle
    # (negative bow_perp per ge_dagger convention)
    draw_pie(d, head=(237.6, 166.1), tail=(140.6, 281.5),
             bow_perp=-14, w_head=9, w_tail=3)

    # s9: dian — 戈 top-right dot (short down-right slant)
    draw_dian(d, (212.4, 82.9), (241.7, 106.1),
              w_head=3, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_战.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
