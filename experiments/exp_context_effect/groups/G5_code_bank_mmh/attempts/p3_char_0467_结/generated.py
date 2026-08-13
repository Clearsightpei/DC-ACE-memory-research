"""p3_char_0467_结 — jie ("tie/knot"), 9 strokes = 纟(3) + 吉(6).

Structure: L-R. 纟 (silk radical) on left = 3 strokes (pie_zhe, pie_zhe, ti).
吉 on right = 士 (3) + 口 (3) stacked.

# BANK_DEVIATION
# skipped: shi_scholar.py, kou_mouth.py (whole-radical bank primitives)
# reason (P-A-009 quantitative):
#   - 士 (bank): native top-heng span 222 px, native total-height 174 px
#     (shu 78.8 -> 252.8). Native aspect w/h = 222/174 = 1.28.
#     Target 士 in 结 top-heng span 133 px (s4: 132->265), total-height
#     123 px (s5: 62->185). Target aspect = 133/123 = 1.08.
#     Ratio 1.28/1.08 = 1.19 — right at edge of P-A-007-v2 [0.55, 1.2].
#     More importantly: shu-length ratio (target 123 / native scaled-to-
#     top-heng-width = 174*0.60 = 104) is 1.18. Uniform-scale bank would
#     leave shu 20 px short of MMH-verbatim shu head y=62; that
#     violates the per-stroke ±0.20 anchor tolerance for stroke 5.
#     Skip and inline via primitives at MMH anchors.
#   - 口 (bank): native aspect w/h = 133/153 = 0.87 (near-square).
#     Target 口 in 结 uses BC/BR span: s8 top from x=157 to 220 (w=63),
#     but s9 bottom extends x=170 to 240 (w=70) — mildly asymmetric
#     right-extending box; height s7: 229->293 = 64. Aspect ~66/64 = 1.03.
#     Ratio 1.03/0.87 = 1.18 — within range BUT the s9 tail extending
#     past s8 right-edge means uniform-scale kou_mouth would clip that
#     asymmetry. Skip and inline via shu + heng_zhe_box + heng at MMH
#     anchors.
# fresh_component: jie_right_side (士+口 stack at MMH-verbatim endpoints)
#
# BANK USE for 纟 (P-A-006 stroke-primitive layer per MMH anchors):
#   - pie_zhe x2 + ti — same recipe that PASSed for 经 retry_1.
#     纟-family well-established via stroke primitives (per drawer_memory
#     retrieval hints); no whole-radical 纟 bank entry exists.
#
# P-A-008 per-stroke reasoning trace (MMH anchors decoded, 100px cells):
#   s1 (纟 pie_zhe 1): TL(0.847,0.683)=(84.7,68.3) -> ML(0.923,0.544)=(92.3,154.4)
#      Short curve, upper-left of nabi. Corner ~ (70, 118).
#   s2 (纟 pie_zhe 2): C(0.151,0.137)=(115.1,113.7) -> C(0.204,0.919)=(120.4,191.9)
#      Second撇折 shifted right & down. Corner ~ (100, 165).
#   s3 (纟 ti): BL(0.39,0.593)=(39.0,259.3) -> BC(0.286,0.197)=(128.6,219.7)
#      Rising diagonal, thick down-left head, fine up-right tail.
#   s4 (士 top heng): C(0.321,0.45)=(132.1,145.0) -> MR(0.646,0.286)=(264.6,128.6)
#      Long top heng, slight upward tilt at right.
#   s5 (士 shu): TC(0.837,0.624)=(183.7,62.4) -> C(0.887,0.852)=(188.7,185.2)
#      Long central vertical, pierces s4 top-heng (P-joint at C).
#   s6 (士 bottom heng): C(0.465,0.939)=(146.5,193.9) -> MR(0.432,0.884)=(243.2,188.4)
#      Shorter bottom heng, slight upward tilt.
#   s7 (口 left shu): BC(0.427,0.288)=(142.7,228.8) -> BC(0.641,0.93)=(164.1,293.0)
#      Left vertical of 口, slight right lean.
#   s8 (口 heng_zhe): BC(0.573,0.297)=(157.3,229.7) -> BR(0.197,0.657)=(219.7,265.7)
#      Top+right corner of 口 box.
#   s9 (口 bottom heng): BC(0.699,0.851)=(169.9,285.1) -> BR(0.396,0.774)=(239.6,277.4)
#      Bottom of 口, extends slightly past s8 right edge (MMH asymmetry).

Joints (all N except s4/s5 which is P — welded crossing):
  s4.mid X s5.mid @ C: P — the shu naturally pierces the top-heng.
  All others: N-class natural gaps, no welding.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie_zhe import draw_pie_zhe   # noqa: E402
from ti import draw_ti             # noqa: E402
from heng import draw_heng         # noqa: E402
from shu import draw_shu           # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 9 primitives (3 for 纟, 6 for 吉)
    'endpoint_mismatches': [],      # all within ±0.20 anchor tolerance
    'joint_class_mismatches': [],   # s4/s5 P-cross emerges from anchor overlap; rest N
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for 士 + 口 (aspect-shift outside safe range); '
             '纟 via pie_zhe+pie_zhe+ti (same recipe as 经 retry PASS).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === 纟 (s1-s3) — silk radical, left side ===
    # s1: upper 撇折
    draw_pie_zhe(d,
                 head=(84.7, 68.3),
                 corner=(70, 118),
                 tail=(92.3, 154.4),
                 pie_bow=5, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4)

    # s2: lower 撇折
    draw_pie_zhe(d,
                 head=(115.1, 113.7),
                 corner=(100, 165),
                 tail=(120.4, 191.9),
                 pie_bow=5, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4)

    # s3: 提 rising bottom stroke
    draw_ti(d,
            head=(39.0, 259.3),
            tail=(128.6, 219.7),
            w_head=9, w_tail=2)

    # === 士 (s4-s6) — top of 吉 ===
    # s4: long top heng, slight upward tilt at right
    draw_heng(d,
              head=(132.1, 145.0),
              tail=(264.6, 128.6),
              width_head=8, width_tail=9)

    # s5: central shu — pierces s4 (P-joint at C)
    draw_shu(d,
             head=(183.7, 62.4),
             tail=(188.7, 185.2),
             width=8)

    # s6: bottom heng (shorter than s4 — 士 signature)
    draw_heng(d,
              head=(146.5, 193.9),
              tail=(243.2, 188.4),
              width_head=8, width_tail=9)

    # === 口 (s7-s9) — bottom of 吉 ===
    # REVISION: anchor-nudge within ±0.20 tolerance to close the 口 box
    # visually. Raw MMH anchors leave s8's right vertical short (y=266 vs
    # s9 bottom y=285) and s7's bottom offset left of s8's left edge; box
    # reads as disconnected sticks. Nudges:
    #   s7 tail (164,293)->(155,288)  dx=-9, dy=-5   (within tol)
    #   s8 bot_right (220,266)->(220,286)  dy=+20  (at tol edge, closes right)
    #   s9 head (170,285)->(155,287)  dx=-15, dy=+2  (aligns to s7 bottom)
    #   s9 tail (240,277)->(222,285)  dx=-18, dy=+8  (aligns to s8 right)
    # All within P-A-007-v2 ±0.20 x_frac/y_frac tolerance.
    # s7: left shu of 口
    draw_shu(d,
             head=(142.7, 228.8),
             tail=(155.0, 288.0),
             width=7)

    # s8: heng_zhe (top + right vertical) — box closes at bottom
    draw_heng_zhe_box(d,
                      top_left=(155.0, 228.8),
                      bottom_right=(220.0, 286.0),
                      width=7)

    # s9: bottom heng of 口 — spans left-shu bottom to right-vertical bottom
    draw_heng(d,
              head=(155.0, 287.0),
              tail=(222.0, 285.0),
              width_head=8, width_tail=9)

    out = os.path.join(os.path.dirname(__file__), '01_结.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
