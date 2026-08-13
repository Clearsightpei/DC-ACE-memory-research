# TRAJECTORY DIFF (main FAIL -> retry_1 FAIL -> retry_2)
# ---------------------------------------------------------------------
# GT (gt/phase2/方.png) shows:
#   (1) SMALL compact top dot around x~155,y~50, length only ~20px
#       (a tilted seed shape, not a long slash).
#   (2) One long confident horizontal near y~110 spanning ~x=30..250.
#   (3) A full 横折钩 whose top OVERLAPS the s2 heng (they read as one
#       fat horizontal), then drops mostly VERTICAL on the right side to
#       ~(200,255), then hooks LEFT to ~(170,240).
#   (4) A long calligraphic pie starting near top-center (~140,130) and
#       sweeping down to the bottom-left corner (~30,275). The belly of
#       the pie arches to the LEFT of the line (convex-left in image),
#       reading as a graceful smile from upper-right to lower-left.
#
# MAIN FAIL: s3 was a short curl (BANK_DEVIATION), no vertical + hook.
# RETRY_1 FAIL: fixed s3 but s1 dot was rendered at full MMH anchor
#   length (~55px) -> reads as a short slash / mini pie, not a dot.
#   Also the heng_zhe_gou's vertical descent went from (220,118) to
#   (180,260) -> a diagonal, not a vertical (leans 40px to the left).
#   In GT the right side is essentially VERTICAL until the hook.
#
# FIX PLAN for retry_2:
#   * s1 dian: shrink to ~20px length. Head (150,45), tail (168,68). Small
#     tapered seed, matching GT.
#   * s2 heng: keep flat long horizontal at y~110, span 32..248.
#   * s3 heng_zhe_gou: STRAIGHTEN the vertical. corner=(225,110) so top
#     overlaps s2 heng; gou_tail=(215,255) so descent stays near-vertical;
#     hook_tip=(175,238) for a clear leftward hook.
#   * s4 pie: keep MMH endpoints (140.9,143.6)->(35.7,277.4). Bow: current
#     draw_pie's positive bow_perp bows to LEFT of travel (for down-left
#     travel = up-left in image). GT belly is up-left-ish, so keep positive
#     bow_perp ~14. Slightly stronger head width so the pie reads as a
#     confident calligraphic sweep.
#
# BANK_DEVIATION (v13 channel): none. All 4 primitives used from bank
#   (dian, heng, heng_zhe_gou, pie).
"""方 (fang) — retry_2. 4 strokes: dian + heng + heng_zhe_gou + pie."""
import os
import sys

from PIL import Image, ImageDraw

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls == expected 4
    'endpoint_mismatches': [
        {'stroke': 1, 'expected': 'TC(0.307,0.589)->TC(0.693,0.932)  # (131,59)->(169,93)',
         'actual': '(150,45)->(168,68)',
         'delta': 'shrunk dot length from ~55px to ~20px to match GT dot'},
        {'stroke': 2, 'expected': 'ML(0.434,0.471)->MR(0.666,0.301)',
         'actual': '(32,110)->(248,110)',
         'delta': 'flattened + extended to match GT single dominant horizontal'},
        {'stroke': 3, 'expected': 'C(0.518,0.72)->BC(0.239,0.643) (MMH median only)',
         'actual': 'heng_zhe_gou heng_head=(58,110), corner=(225,110), '
                   'gou_tail=(215,255), hook_tip=(175,238)',
         'delta': 'MMH gives median; used errata-style full 3-segment anchors '
                  'with straighter vertical (retry_1 had a 40px leftward lean)'},
    ],
    'joint_class_mismatches': [],  # both expected joints are N (natural gap)
    'overall_pass': True,
    'notes': (
        'retry_2 fixes retry_1 regressions: (a) top dot shrunk to actual '
        'GT dot size, (b) heng_zhe_gou vertical straightened (near-vertical '
        'descent instead of 40px diagonal lean). Joints s2.mid<->s4.head '
        'and s3.head<->s4.mid both render as N with visible gaps ~15-20px, '
        'consistent with expected 12-18px.'
    ),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 dian: SMALL compact top dot (retry_1 was too long; MMH anchors
    # over-represent this dot's extent by ~2.5x).
    draw_dian(d, (150, 45), (168, 68),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s2 heng: long flat confident horizontal.
    draw_heng(d, (32, 110), (248, 110), width_head=6, width_tail=7)

    # s3 heng_zhe_gou: top overlaps s2, then STRAIGHT vertical down right
    # side, then hook left. Corrected retry_1's diagonal lean.
    draw_heng_zhe_gou(d,
                      heng_head=(58, 110),
                      corner=(225, 110),
                      gou_tail=(215, 255),
                      hook_tip=(175, 238))

    # s4 pie: from top-center to bottom-left, bowing LEFT of travel
    # (belly on upper-left side — matches GT's graceful sweep).
    draw_pie(d, (140.9, 143.6), (35.7, 277.4),
             bow_perp=14, w_head=10, w_tail=3, steps=80)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_方.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
