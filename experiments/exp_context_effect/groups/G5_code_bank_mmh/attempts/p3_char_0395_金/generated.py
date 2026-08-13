"""p3_char_0395_金 — 金 (jin, "gold/metal") — 8 strokes.

BANK_DEVIATION reasoning (P-A-009 quantitative):
- Bank has `ren.py` (draw_ren) for 人 (top of 金). Native ren aspect
  (bbox from primitive coords): head~(141,84), tails~(21,272)/(289,274)
  → width ≈ 268, height ≈ 190, native aspect W/H ≈ 1.41.
  金's top-人 target (MMH s1+s2 endpoints): pie head (135.6, 61.2) →
  tail (17.6, 208), na head (155, 88.8) → tail (283.3, 173.4) →
  bbox width ≈ 265.7, height ≈ 147, target aspect ≈ 1.81.
  Aspect delta = 1.81 / 1.41 = 1.28 (28% wider than native).
  Scale ratio for width: 265.7/268 = 0.99; for height 147/190 = 0.77.
  Non-uniform scale (x=0.99, y=0.77) → cannot cleanly call draw_ren
  with a single scale arg without distorting the pie/na curves.
  DECISION: skip draw_ren; call draw_pie + draw_na directly with the
  MMH endpoints for s1 and s2. Same primitive layer, cleaner fit.
  (P-A-006 stroke-primitive layer, P-A-007-v2 hard-check: whole-radical
  native aspect 1.41 vs target 1.81 exceeds ±20% band → decompose.)

- Bank also has `wang_king.py` for 王 (4 strokes). But 金's lower zone
  is NOT 王 — it's 全 minus top? Actually inspection: bottom portion
  of 金 has 8-4 = 6 strokes below 人: 2 horizontals + 1 vertical +
  2 dots + 1 bottom horizontal, which is 王 + 丷 inside. But MMH
  stroke order gives us: s3 top-heng, s4 mid-heng, s5 vertical,
  s6/s7 two dots, s8 bottom-heng. That's NOT wang_king (which is
  heng+heng+shu+heng, 4 strokes, no dots). So wang_king does not
  apply — the middle horizontal + vertical of 王 is present but
  the two 点 make it structurally different. DECISION: skip
  wang_king, inline all 6 lower strokes from MMH.

# BANK_DEVIATION
# skipped: ren.py — aspect target 1.81 vs native 1.41 (+28%)
# skipped: wang_king.py — 金 lower zone has 2 dots (6 strokes) vs 王 (4 strokes)
# reason: non-uniform scale on ren, structural mismatch on wang
# fresh_component: 金 as stroke-primitive layer (P-A-006)

Strokes (MMH cell + x_frac/y_frac → pixel via col*100+xf*100, row*100+yf*100):
  s1: pie   TC(0.356,0.612)→BL(0.176,0.08)  = (135.6, 61.2)→(17.6, 208.0)
  s2: na    TC(0.55,0.888)→MR(0.833,0.734)  = (155.0, 88.8)→(283.3, 173.4)
  s3: heng  ML(0.955,0.717)→C(0.901,0.608)  = (95.5, 171.7)→(190.1, 160.8)
  s4: heng  BL(0.864,0.194)→BC(0.96,0.086)  = (86.4, 219.4)→(196.0, 208.6)
  s5: shu   C(0.354,0.77)→BC(0.389,0.821)   = (135.4, 177.0)→(138.9, 282.1)
  s6: dian  BL(0.773,0.405)→BC(0.049,0.684) = (77.3, 240.5)→(104.9, 268.4)
  s7: dian  BC(0.954,0.227)→BC(0.646,0.625) = (195.4, 222.7)→(164.6, 262.5)
  s8: heng  BL(0.513,0.959)→BR(0.405,0.909) = (51.3, 295.9)→(240.5, 290.9)

Joint plan:
  s1.head N s2.head TC — N-gap at pyramid top (~22 px) → pie head y=61,
     na head y=89, natural gap.
  s3.mid N s5.head C — s5 starts below s3 with ~14 px gap (s3 y~166,
     s5 head y=177). No welding.
  s4.mid P s5.mid BC — vertical pierces mid-heng at BC (welded).
  s4.tail N s7.head BC — 24 px gap between s4 right end (196, 209) and
     s7 head (195, 223).
  s6/s7 are the two 丷 dots inside the 王-frame.
  s8 is the longest heng at the very bottom.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu import draw_shu
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 8 stroke calls: pie+na+heng+heng+shu+dian+dian+heng
    'endpoint_mismatches': [],   # all endpoints MMH-verbatim
    'joint_class_mismatches': [],# N joints preserve natural gaps; P joint s4×s5 welds at BC
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: skipped ren.py (aspect +28%) and wang_king.py '
             '(金 has dots — structural mismatch). Fell back to stroke-primitive '
             'layer per P-A-006, following P-A-007-v2 hard-check.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 撇 (pie) — top-left of 人, from mid-top down to lower-left
    # N-joint with s2 at TC (natural gap at pyramid apex)
    draw_pie(d, (135.6, 61.2), (17.6, 208.0),
             bow_perp=14, w_head=9, w_tail=3)

    # s2: 捺 (na) — top-right of 人, from just below s1 head sweeping
    # down-right to mid-right. N-joint w/ s1 at TC.
    draw_na(d, (155.0, 88.8), (283.3, 173.4),
            bow_perp=12, w_head=4, w_tail=11)

    # s3: 短横 (top horizontal in the box below 人) — short, mildly rising
    draw_heng(d, (95.5, 171.7), (190.1, 160.8),
              width_head=8, width_tail=9)

    # s4: 中横 (middle horizontal) — pierced by vertical s5 at BC (P joint)
    draw_heng(d, (86.4, 219.4), (196.0, 208.6),
              width_head=8, width_tail=9)

    # s5: 竖 (vertical) — head N-gap below s3, body P-welds through s4
    # tail is just below s4 (in BC cell). Simple straight vertical.
    draw_shu(d, (135.4, 177.0), (138.9, 282.1), width=7)

    # s6: 左点 — inside the 王-box, going down-right (like a 提-style dot)
    # MMH head→tail goes right-down (dx=+27, dy=+28). Render as slim
    # tapered dian.
    draw_dian(d, (77.3, 240.5), (104.9, 268.4),
              w_head=2, w_tail=7, bow=3)

    # s7: 右点 — inside the 王-box, going down-left (like a 撇点)
    # MMH head→tail goes left-down (dx=-31, dy=+40). Tapered dian.
    draw_dian(d, (195.4, 222.7), (164.6, 262.5),
              w_head=2, w_tail=7, bow=3)

    # s8: 底长横 (bottom longest heng — 金 shape marker)
    draw_heng(d, (51.3, 295.9), (240.5, 290.9),
              width_head=10, width_tail=11)

    out = os.path.join(os.path.dirname(__file__), '01_金.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
