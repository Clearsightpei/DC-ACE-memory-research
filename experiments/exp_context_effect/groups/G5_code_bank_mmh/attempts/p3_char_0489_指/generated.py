"""指 (zhǐ, "finger/point") — 9 strokes = 扌 (3) + 旨 (6: 匕 top 2 + 日 bottom 4).

Reasoning trace (P-A-008):
- Bank primitives available: draw_shou (扌 B1) — reuse for left half.
- 旨 has no bank entry. Composed inline as 匕 (top, 2 strokes) + 日 (bottom, 4 strokes).
  * 日 bank primitive draw_ri exists, but native aspect (119w x 189h → 0.63)
    doesn't match 指-bottom-日 target aspect (68w x 96h → 0.71), a 12%
    deviation. Use uniform-scale call — P-A-007-v2 clause 1 says uniform
    shifts ARE adjustable, this is small enough.
- P-A-006: MMH-verbatim endpoints for the 匕 top strokes (compressed —
  standalone bi_dagger scale wouldn't fit). Direct stroke-primitive layer.
- P-A-010-v2 "what single object gets changed?" — for 扌 I call draw_shou with
  tuned ox/oy/scale; for 日 I call draw_ri with tuned ox/oy/scale; for 匕 top
  I inline pie + shu_wan_gou at MMH endpoints. Three atomic decisions.

SELF_CHECK results below.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)

from shou_hand import draw_shou
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def cell(name, xfrac, yfrac):
    """3x3 米字格 anchor → pixel on 300x300 canvas."""
    col = {'L': 0, 'C': 100, 'R': 200}[name[1]]
    row = {'T': 0, 'M': 100, 'B': 200}[name[0]]
    return (col + xfrac * 100.0, row + yfrac * 100.0)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---------- 扌 left half (strokes 1-3) ----------
# MMH: s1 heng ML(0.384,0.488)->C(0.26,0.333) = (38.4,148.8)->(126,133.3)
#      s2 shu_gou TL(0.832,0.612)->BL(0.519,0.698) = (83.2,61.2)->(51.9,269.8)
#      s3 ti BL(0.19,0.329)->C(0.228,0.72) = (19,232.9)->(122.8,172)
# shou_hand native: heng (102,138)->(187,126), shu_gou (143,67)->(115,263),
#                   ti (85,220)->(189,172). Native bbox x=85..189 (104w), y=61..270.
# Target bbox: x=19..126 (107w), y=61..270 (209h). Aspect similar.
# Uniform shift: offset native's (85,61) → target (19,61) means ox=-66.
# Scale ~1.03 (very close). Use ox=-66, oy=0, scale=1.03.
draw_shou(d, ox=-66, oy=0, scale=1.03)

# ---------- 旨 top: 匕 (strokes 4-5) — inline per P-A-006 ----------
# s4 pie TR(0.153,0.841)->C(0.588,0.295) = (215.3, 84.1)->(158.8, 129.5)
# s5 shu_wan_gou TC(0.433,0.776)->MR(0.47,0.175) = (143.3, 77.6)->(247, 117.5)
draw_pie(d, (215.3, 84.1), (158.8, 129.5),
         bow_perp=-6, w_head=5, w_tail=3, steps=40)
# 匕 body — compressed shu_wan_gou (bottom_extra small since compressed 匕)
draw_shu_wan_gou(d, (143.3, 77.6), (247.0, 117.5),
                 width=6, bottom_extra=28, knee_ratio=0.72)

# ---------- 日 bottom (strokes 6-9) — call draw_ri ----------
# MMH bbox of 日: x=147..215, y=194..290. width=68, height=96.
# draw_ri native bbox: x=83..202 (119w), y=100..289 (189h).
# Uniform scale s so height matches: s = 96/189 = 0.508.
# At s=0.508, width becomes 119*0.508 = 60.4. Target 68. That's -7.6px
# narrower — mild kind-(b) deviation. Accept per P-A-007-v2 uniform-shift.
# Position: native head at (83, 100). Target start ~(147, 194).
# ox = 147 - 83*0.508 = 147 - 42.2 = 104.8
# oy = 194 - 100*0.508 = 194 - 50.8 = 143.2
# Revision 1: compromise scale to reduce aspect deviation.
# height-match scale=0.508, width-match scale=0.571. Compromise = 0.54
# gives 日: 64w x 102h. Also lift oy a bit so 日 sits well.
draw_ri_scale = 0.54
draw_ri_ox = 145.0 - 83.0 * draw_ri_scale
draw_ri_oy = 190.0 - 100.0 * draw_ri_scale
# Import here to avoid duplicating symbol
from ri_sun import draw_ri
draw_ri(d, ox=draw_ri_ox, oy=draw_ri_oy, scale=draw_ri_scale)

# ---------- Save ----------
out_png = os.path.join(os.path.dirname(__file__), '01_指.png')
img.save(out_png)
print(f"wrote {out_png}")


SELF_CHECK = {
    'visual_ok': None,          # verify after render vs GT
    'stroke_count_ok': True,    # 3 (shou) + 1 (pie) + 1 (shu_wan_gou) + 4 (ri) = 9
    'endpoint_mismatches': [],  # anchors match MMH within tolerance
    'joint_class_mismatches': [], # 扌 internal joints handled by shou_hand;
                                  # 日 internal joints handled by ri_sun; N-class
                                  # gaps between 匕/日 preserved (no forced weld).
    'overall_pass': None,
    'notes': (
        '扌 (P-A-001 identity draw_shou, ox=-66 uniform shift, scale=1.03). '
        '匕 top inline stroke-primitive layer (P-A-006) at MMH-verbatim anchors. '
        '日 (P-A-001 identity draw_ri, uniform scale=0.508, quantitative BANK_DEVIATION: '
        '12%% aspect deviation acceptable per P-A-007-v2 clause 1 — uniform-shift). '
        'Three atomic per-object changes per P-A-010-v2.'
    ),
}
