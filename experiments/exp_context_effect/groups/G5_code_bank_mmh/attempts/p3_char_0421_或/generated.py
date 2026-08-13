"""p3_char_0421_或 — 或 (huo, "or") — 8 strokes.

Composition per P-A-006 (MMH-verbatim anchors + stroke-primitive layer):
  s1  = heng (top of 或, short-medium, slight up-right rise)
  s2  = shu (left side of small 口, minor rightward drift)
  s3  = heng_zhe (mini, top+right of small 口)
  s4  = heng (short lower-mouth horizontal, rising to right)
  s5  = heng (long lower-mid horizontal — the character's carrying base)
  s6  = xie_gou (main diagonal top-center → bottom-right + up-hook)
  s7  = pie (upper-right sweeping down-left through middle)
  s8  = dian (top-right dot)

# BANK_DEVIATION
# skipped: ge_dagger.py (戈, whole-radical, 4-stroke composite)
# reason (P-A-009 quantitative):
#   Native ge heng: (54,168)→(173,133), span 119px, dy=-35, aspect
#     119/35 = 3.40. Target s1: (66,129)→(198,111), span 132, dy=-18,
#     aspect 132/18 = 7.33. Ratio target/native aspect = 2.16 — target
#     is 2.16x SHALLOWER than bank. Also y-offset: native heng y-mid=150,
#     target y-mid=120 → Δy = -30px = 20% of char height, non-uniform
#     shift from other ge sub-strokes (xie_gou head Δy = -18, tail Δy =
#     -3, pie head Δy = -3, tail Δy = +3, dian Δy = -10). No single
#     (ox,oy,scale) triple satisfies all 4 sub-strokes. Outside P-A-007-v2
#     [0.55, 1.2] aspect fit range for the heng component (2.16).
# fresh_component: none — reused stroke primitives (heng/xie_gou/pie/dian)
#   at MMH-verbatim endpoints.
#
# skipped: kou_mouth.py (口, whole-radical, 3-stroke composite)
# reason (P-A-009 quantitative):
#   Native kou bbox 130w × 150h (aspect 0.867). Target small-mouth bbox
#   x=[56,110], y=[167,221] → 54w × 54h (aspect 1.0). Scale ratios
#   width 54/130=0.42, height 54/150=0.36 — non-uniform (Δ=0.06, 17%
#   spread). Aspect ratio target/native = 1.0/0.867 = 1.15 (marginal).
#   BUT the heng_zhe_box sub-part: native (110w × 136h, aspect 0.81),
#   target (36w × 23h, aspect 1.57). Target/native aspect = 1.94 —
#   target box is nearly 2x more squat. Outside [0.55, 1.2] fit range.
#   Additionally, this 或's mouth structure has s4 BELOW s3-corner
#   (s3 tail y=196, s4 head y=215) — atypical mouth topology, so inlining
#   stroke-primitives at MMH anchors is required.
# fresh_component: none — reused shu/heng_zhe_box/heng stroke primitives.

MMH anchors → pixel (cell base + x_frac*100, y_frac*100):
  s1: ML(0.662,0.292)→(66,129),  C(0.978,0.113)→(198,111)   heng
  s2: ML(0.557,0.67)→(56,167),   BL(0.771,0.206)→(77,221)   shu
  s3: ML(0.735,0.729)→(74,173),  C(0.096,0.96)→(110,196)    heng_zhe (mini)
  s4: BL(0.826,0.147)→(83,215),  BC(0.263,0.06)→(126,206)   heng (short)
  s5: BL(0.398,0.587)→(40,259),  BC(0.43,0.279)→(143,228)   heng (long rising)
  s6: TC(0.257,0.601)→(126,60),  BR(0.689,0.473)→(269,247)  xie_gou
  s7: MR(0.112,0.538)→(211,154), BC(0.289,0.81)→(129,281)   pie
  s8: TC(0.919,0.683)→(192,68),  TR(0.265,0.935)→(227,94)   dian
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
    'stroke_count_ok': True,   # 8 stroke primitive calls, matches MMH expected 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION vs ge_dagger + kou_mouth applied per '
             'P-A-007-v2 + P-A-009 quantitative reasoning (see docstring). '
             'Reused 6 stroke primitives (heng/shu/heng_zhe_box/pie/dian/'
             'xie_gou) at MMH-verbatim endpoints. Joint s1×s6 P forms as '
             'natural weld near cell C where the top heng crosses the '
             'xie_gou. Joint s6×s7 P forms near cell BC as the pie '
             'crosses the xie_gou. N joints around small mouth (s2/s3/s4) '
             'preserved by leaving ~10px gaps per MMH.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: heng — top of 或 (moderate length, slight up-right rise)
    draw_heng(d, (66, 129), (198, 111), width_head=8, width_tail=9)

    # s2: shu — left side of small mouth (slight rightward drift OK)
    draw_shu(d, (56, 167), (77, 221), width=7)

    # s3: heng_zhe (mini) — top+right of small mouth
    draw_heng_zhe_box(d, top_left=(74, 173), bottom_right=(110, 196), width=6)

    # s4: heng — short lower-mouth horizontal (rising to right)
    draw_heng(d, (83, 215), (126, 206), width_head=7, width_tail=8)

    # s5: heng — long lower-mid horizontal, slight rise (carries 戈 base)
    draw_heng(d, (40, 259), (143, 228), width_head=9, width_tail=10)

    # s6: xie_gou — main diagonal from top-center down to bottom-right + hook
    draw_xie_gou(d, head=(126, 60), tail=(269, 247),
                 width=8, bow=8, hook_up=30, hook_back=6)

    # s7: pie — upper-right sweeping down-left through middle (negative bow_perp
    # per ge_dagger convention: curves the belly down-right of travel dir)
    draw_pie(d, head=(211, 154), tail=(129, 281),
             bow_perp=-14, w_head=9, w_tail=3)

    # s8: dian — small top-right dot (short down-right slant)
    draw_dian(d, (192, 68), (227, 94),
              w_head=3, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_或.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
