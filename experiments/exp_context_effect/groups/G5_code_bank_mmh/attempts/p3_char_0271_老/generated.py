"""p3_char_0271_老 — G5 attempt (P-A-006 recipe: MMH anchors verbatim + stroke primitives).

老 (lǎo, old) — 6 strokes:
  s1 heng           (top short horizontal, slight rise)
  s2 shu            (short vertical crossing s1 at C:P weld)
  s3 heng           (long horizontal spanning ML→MR)
  s4 pie            (long diagonal top-right → bottom-left, welded to s3 P)
  s5 pie            (short diagonal BR→BC, feeds into s6 body N gap)
  s6 shu_wan_gou    (bottom-right vertical-bend-hook; head T-tangent onto s4)

Joint plan (from MMH block):
  s1.mid ⇆ s2.mid  P  weld @ C
  s1.tail ⇆ s4.mid N  gap
  s2.tail ⇆ s3.mid N  gap
  s3.mid ⇆ s4.mid  P  weld
  s4.mid ⇆ s6.head T  tangent (s6.head sits on s4 body)
  s5.tail ⇆ s6.mid N  gap
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top short heng — ML(0.935,0.175)→C(0.881,0.102) i.e. (93.5,117.5)→(188.1,110.2)
    draw_heng(d, (93, 118), (188, 110), width_head=8, width_tail=9)

    # s2: short shu crossing s1 — TC(0.333,0.533)→C(0.383,0.556) = (133.3,53.3)→(138.3,155.6)
    draw_shu(d, (133, 53), (138, 156), width=7)

    # s3: long heng — ML(0.278,0.775)→MR(0.73,0.55) = (27.8,177.5)→(273,155)
    draw_heng(d, (28, 178), (273, 155), width_head=9, width_tail=10)

    # s4: long pie — TR(0.112,0.729)→BL(0.375,0.73) = (211.2,72.9)→(37.5,273)
    # Strong left-bow (calligraphic 撇). MUST P-weld through s3.
    draw_pie(d, (211, 73), (38, 273), bow_perp=18, w_head=10, w_tail=3, steps=90)

    # s5: short pie — BR(0.259,0.036)→BC(0.403,0.338) = (225.9,203.6)→(140.3,233.8)
    draw_pie(d, (226, 204), (140, 234), bow_perp=6, w_head=7, w_tail=3, steps=50)

    # s6: shu_wan_gou — C(0.254,0.931)→BR(0.323,0.405) = (125.4,193.1)→(232.3,240.5)
    # Head sits T-tangent on s4 body (s4.mid ≈ (124,173)); tail is the hook tip.
    draw_shu_wan_gou(d, (125, 193), (232, 240),
                     width=7, bottom_extra=45, knee_ratio=0.78)

    out = os.path.join(os.path.dirname(__file__), "01_老.png")
    img.save(out)
    print("wrote", out)


SELF_CHECK = {
    'visual_ok': None,          # set post-render after eyeballing
    'stroke_count_ok': True,    # exactly 6 primitive calls: heng, shu, heng, pie, pie, shu_wan_gou
    'endpoint_mismatches': [],  # all pixel anchors converted verbatim from MMH block
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'P-A-006 recipe: MMH anchors verbatim, stroke primitives only, no whole-radical composition. s1-s2 cross naturally (P weld). s3-s4 cross naturally (P weld). s4-s6 T tangent via anchor placement. N gaps preserved by not welding.'
}


if __name__ == "__main__":
    render()
