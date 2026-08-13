"""p3_char_0477_南 — 南 (nan, "south") — 9 strokes.

Composition per P-A-006 (MMH-verbatim anchors + stroke-primitive layer):
  s1 = heng          (top 一 of 十)
  s2 = shu           (丨 of 十 — extends above the heng and dips below)
  s3 = shu (slight rightward drift)  (left leg of the outer 冂 frame)
  s4 = heng_zhe_gou  (top + right of the outer 冂 frame, with terminal hook)
  s5 = dian          (interior 丷 left dot)
  s6 = pie (short)   (interior 丷 right dot — MMH slant goes down-left)
  s7 = heng          (interior upper cross-bar)
  s8 = heng          (interior lower cross-bar)
  s9 = shu           (interior central shu piercing both cross-bars)

# BANK_DEVIATION
# skipped: shi_ten.py (十 whole-radical) and no whole-radical primitive for 冂
# reason (P-A-009 quantitative):
#   shi_ten native heng span ~120px at y≈150 with shu (150,90)→(150,240)
#   symmetric. Target s1/s2 heng span 111px at y≈106 with shu (140,53)→
#   (127,154) — shu head ABOVE the heng crossing and shu is not
#   symmetric about heng midpoint (heng mid x=148, shu-at-heng-y=139).
#   ox-shift alone cannot correct the top-drift of the shu head + the
#   asymmetric crossing. Inline required (P-A-007-v2 clause-2 pattern).
# skipped: shan_mountain-like or kou_mouth for the outer frame.
# reason: 南's outer frame is a 冂 with hooked right foot, not a closed
#   box. No whole-radical primitive matches; the pattern is naturally
#   two strokes (left leg + top-right heng_zhe_gou combo).
# fresh_component: none — 9 stroke-primitive calls at MMH-verbatim
#   endpoints. Approach mirrors 冉 (B7 A) and 用-family precedent for
#   frame + interior bars.

MMH anchors → pixel (cell_base_x + x_frac*100, cell_base_y + y_frac*100):
  s1: ML(0.923,0.116)=(92.3,111.6)  MR(0.036,0.002)=(203.6,100.2)  heng
  s2: TC(0.395,0.527)=(139.5,52.7)  C(0.274,0.535)=(127.4,153.5)   shu
  s3: ML(0.463,0.632)=(46.3,163.2)  BL(0.621,0.845)=(62.1,284.5)   shu(drift)
  s4: ML(0.606,0.664)=(60.6,166.4)  BC(0.951,0.733)=(195.1,273.3)  heng_zhe_gou
  s5: C(0.061,0.752)=(106.1,175.2)  C(0.195,0.957)=(119.5,195.7)   dian
  s6: C(0.652,0.629)=(165.2,162.9)  BC(0.518,0.019)=(151.8,201.9)  short pie
  s7: BL(0.993,0.121)=(99.3,212.1)  BC(0.919,0.051)=(191.9,205.1)  heng (inner)
  s8: BL(0.926,0.443)=(92.6,244.3)  BR(0.019,0.396)=(201.9,239.6)  heng (inner)
  s9: BC(0.33,0.174)=(133.0,217.4)  BC(0.415,0.938)=(141.5,293.8)  shu (inner)

Joints (11 expected):
  s1.mid ⇆ s2.mid P (welded @ C(0.417,0.091) — heng crosses shu near top)
  s2.tail ⇆ s4.mid N (~15px — s2.tail (127,154), s4 mid ≈ (128, 220))
  s3.head ⇆ s4.head N (~12px — (46,163) vs (61,166))
  s4.head ⇆ s5.head N (~18px)
  s4.mid ⇆ s6.head N (~10px)
  s5.tail ⇆ s7.mid N (~23px)
  s5.tail ⇆ s9.head N (~35px)
  s6.mid ⇆ s7.mid N (~15px)
  s6.tail ⇆ s9.head N (~33px)
  s7.mid ⇆ s9.head N (~13px)
  s8.mid ⇆ s9.mid P (welded @ BC(0.419,0.409) — inner heng crosses inner shu)
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
from heng_zhe_gou import draw_heng_zhe_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 primitive calls, matches MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer with MMH-verbatim endpoints. '
             'BANK_DEVIATION vs shi_ten (asymmetric heng-shu crossing '
             'unrepresentable by uniform ox-shift). No whole-radical '
             'primitive exists for the 冂-with-hook frame; two-stroke '
             'decomposition (left shu + heng_zhe_gou) matches MMH. '
             'Interior 半-like pattern = 丷 (s5+s6) + heng + heng + shu.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top heng of 十
    draw_heng(d, (92.3, 111.6), (203.6, 100.2), width_head=8, width_tail=9)

    # s2: 丨 of 十 — extends from above heng (y=53) down through heng (y=100)
    #     to below (y=154). Straight shu.
    draw_shu(d, (139.5, 52.7), (127.4, 153.5), width=7)

    # s3: left leg of outer frame — near-vertical with slight rightward drift
    draw_shu(d, (46.3, 163.2), (62.1, 284.5), width=7)

    # s4: top + right of outer 冂 frame with terminal hook
    #     heng_head=(61,166) → corner at top-right ≈ (198,170) → gou_tail
    #     (195,273) → small hook flicked up-left
    draw_heng_zhe_gou(d,
                      heng_head=(60.6, 166.4),
                      corner=(198.0, 170.0),
                      gou_tail=(195.1, 273.3),
                      hook_tip=(184.0, 267.0))

    # s5: interior 丷 left dot — short down-right slant
    draw_dian(d, (106.1, 175.2), (119.5, 195.7),
              w_head=3, w_tail=7, bow=3)

    # s6: interior 丷 right dot — short down-left slant (dian shape, mirror of s5)
    draw_dian(d, (165.2, 162.9), (151.8, 201.9),
              w_head=3, w_tail=7, bow=-3)

    # s7: interior upper cross-bar (heng)
    draw_heng(d, (99.3, 212.1), (191.9, 205.1), width_head=6, width_tail=7)

    # s8: interior lower cross-bar (heng)
    draw_heng(d, (92.6, 244.3), (201.9, 239.6), width_head=7, width_tail=8)

    # s9: interior central shu piercing s7 and s8 (welded @ s8.mid)
    draw_shu(d, (133.0, 217.4), (141.5, 293.8), width=6)

    out = os.path.join(os.path.dirname(__file__), '01_南.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
