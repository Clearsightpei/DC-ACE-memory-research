# BANK_DEVIATION
# skipped: bao_wrap.py, kou_mouth.py
# reason: 勹 in 佝 needs non-uniform y-stretch — bank bao's reference footprint
#   (~176 x 209 px) vs 佝's right slot (~110 x 220 px) demands scale_x~0.62,
#   scale_y~1.05, outside P-A-007-v2 [0.55, 1.2] aspect-uniform band. kou's
#   absolute layout is tuned for a stand-alone 口, not one nested low-inside
#   a 勹 wrapper at MMH-specified anchors.
# fresh_component: inline_bao_for_gou, inline_kou_for_gou (MMH-anchor-verbatim)
#
# P-A-006 stroke-primitive layer with MMH endpoints verbatim.
# P-A-008 inline-reasoning: each sub-component traced below.
"""p3_char_0344_佝 — 亻 (2) + 句 (5, = 勹(2) + 口(3))  = 7 strokes.

Sub-component decisions:
  1. 亻 (s1 撇, s2 竖): considered draw_ren_left; its reference native aspect
     ~1.10 : 1 fits within [0.55, 1.2]. Could call whole-radical, BUT MMH
     anchor for s1 tail is at ML(0.211, 0.983) — much lower than
     ren_left's tail (80.6, 211.2). Whole-radical would misplace both
     endpoints. Inline via stroke primitives at MMH anchors verbatim
     (P-A-006 primary A-recipe).
  2. 勹 (s3 短撇, s4 横折钩): see BANK_DEVIATION block; inline via
     draw_pie + draw_heng_zhe_gou at MMH anchors. Corner inferred by
     extending s4 head horizontally to the visual right edge of the 勹
     footprint (~x=228), then curving down to gou_tail = s4 MMH tail.
  3. 口 (s5 竖, s6 横折(box), s7 底横): see BANK_DEVIATION block; inline via
     shu + heng_zhe_box + heng at MMH anchors. 口 in 佝 is small/tucked
     inside the 勹 wrap — anchors span only ~48 px wide, so use slim
     widths (6 px) to keep the box clean.
"""

import os
import sys

from PIL import Image, ImageDraw

# ---- bank path ----
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from shu import draw_shu

# ---- MMH anchor helper (3x3 米字格 on 300x300) ----
CELL_ORIGIN = {
    "TL": (0, 0), "TC": (100, 0), "TR": (200, 0),
    "ML": (0, 100), "C": (100, 100), "MR": (200, 100),
    "BL": (0, 200), "BC": (100, 200), "BR": (200, 200),
}


def A(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

# ============ 亻 (2 strokes) ============
# s1 撇: head TL(0.932,0.659) → tail ML(0.211,0.983)
s1_head = A("TL", 0.932, 0.659)   # (93.2, 65.9)
s1_tail = A("ML", 0.211, 0.983)   # (21.1, 198.3)
draw_pie(draw, s1_head, s1_tail, bow_perp=15, w_head=9, w_tail=3, steps=90)

# s2 竖: head ML(0.697,0.556) → tail BL(0.738,0.95)
s2_head = A("ML", 0.697, 0.556)   # (69.7, 155.6)
s2_tail = A("BL", 0.738, 0.95)    # (73.8, 295.0)
draw_shu(draw, s2_head, s2_tail, width=7)

# ============ 勹 (2 strokes) ============
# s3 短撇: head TC(0.649,0.598) → tail C(0.166,0.644)
s3_head = A("TC", 0.649, 0.598)   # (164.9, 59.8)
s3_tail = A("C", 0.166, 0.644)    # (116.6, 164.4)
draw_pie(draw, s3_head, s3_tail, bow_perp=6, w_head=6, w_tail=3, steps=60)

# s4 横折钩: head C(0.479,0.4) → tail BC(0.746,0.774)
# Corner inferred: heng extends right to visual right edge of 勹, then
# curves down/left slightly to the hook.
s4_head = A("C", 0.479, 0.4)      # (147.9, 140.0)
s4_tail = A("BC", 0.746, 0.774)   # (174.6, 277.4)
s4_corner = (228, 134)
s4_hook_tip = (168, 262)
draw_heng_zhe_gou(draw, s4_head, s4_corner, s4_tail, s4_hook_tip)

# ============ 口 (3 strokes, low-center inside 勹) ============
# s5 竖: head C(0.148,0.852) → tail BC(0.324,0.42)
s5_head = A("C", 0.148, 0.852)    # (114.8, 185.2)
s5_tail = A("BC", 0.324, 0.42)    # (132.4, 242.0)
draw_shu(draw, s5_head, s5_tail, width=6)

# s6 横折(box): top_left @ (129.2,185.2), bottom_right @ (163.2,220.0)
s6_head = A("C", 0.292, 0.852)    # (129.2, 185.2)
s6_tail = A("BC", 0.632, 0.2)     # (163.2, 220.0)
draw_heng_zhe_box(draw, s6_head, s6_tail, width=6)

# s7 底横: head BC(0.383,0.353) → tail BC(0.813,0.285)
s7_head = A("BC", 0.383, 0.353)   # (138.3, 235.3)
s7_tail = A("BC", 0.813, 0.285)   # (181.3, 228.5)
draw_heng(draw, s7_head, s7_tail, width_head=6, width_tail=7)

# ---- save ----
out_path = os.path.join(HERE, "01_佝.png")
img.save(out_path)

# ---- MANDATORY SELF-CHECK ----
SELF_CHECK = {
    "visual_ok": None,
    "stroke_count_ok": True,          # 7 primitive calls above
    "endpoint_mismatches": [],        # all anchors verbatim from MMH block
    "joint_class_mismatches": [],     # all 7 joints are N-class (natural gap)
    "overall_pass": None,             # set after visual review
    "notes": (
        "7 strokes via P-A-006 stroke-primitive layer; MMH anchors verbatim. "
        "BANK_DEVIATION on 勹 (non-uniform aspect) + 口 (nested-inside layout). "
        "N-gaps between: s1.mid⇆s2.head (ML), s3.mid⇆s4.head (C), "
        "s3.tail⇆s5.head (C), s3.tail⇆s6.head (C), s5.head⇆s6.head (C), "
        "s5.tail⇆s7.head (BC), s6.tail⇆s7.mid (BC) — all emerge naturally "
        "from placing endpoints at MMH-specified pixels."
    ),
}
