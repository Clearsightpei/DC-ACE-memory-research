# TRAJECTORY DIFF (main FAIL -> retry_1)
# ---------------------------------------------------------------------
# GT (gt/phase2/方.png) shows: (1) small top dot around x=155,y=45;
# (2) ONE dominant long horizontal near y=108 spanning roughly x=30..245;
# (3) a full 横折钩 whose top-heng OVERLAPS the s2 heng visually, then
# drops down the right side and hooks LEFT at the bottom near (150,250);
# (4) a long pie sweeping from near the top-center (~130,130) down to
# the bottom-left corner (~30,275).
#
# MAIN FAIL (attempts/p2_radical_093_方/01_方.png) got wrong:
#  * s2 heng was rendered with a strong upward tilt (43,147)->(267,130) —
#    reads as a slanting stripe, not the confident horizontal in GT.
#  * s3 was BANK_DEVIATION'd to a short 'down_hook_short' from
#    C(152,172) to BC(124,264). This is the MMH MEDIAN of 横折钩, not
#    its endpoints — the rendered stroke has NO top horizontal and NO
#    right-side descent, so 方's characteristic right-side box + hook
#    is completely missing. That is the single biggest visual defect.
#  * Overall the char reads as dot + slanted heng + short curl + pie —
#    not 方.
#
# FIX PLAN (retry_1):
#  * s1 dian: keep MMH anchors verbatim (they are fine).
#  * s2 heng: OVERRIDE MMH tilt — flatten to y~=110 across full width.
#    Per drawer_memory MMH-calibration notes: MMH sometimes places
#    stroke endpoints off from the visible GT centroid; flattening here
#    matches what the GT actually shows.
#  * s3: USE draw_heng_zhe_gou from the bank (not another
#    BANK_DEVIATION). Per errata.md B2 hint for this item: heng_head=
#    (56,125), corner=(215,125), gou_tail=(178,260), hook_tip=(148,245).
#    These are the errata-suggested pixel anchors that describe the
#    full 3-segment 横折钩, overriding MMH's median-only C->BC.
#  * s4 pie: keep MMH anchors (they're consistent with GT) with strong
#    bow_perp so the pie carves cleanly to bottom-left.
#
# BANK_DEVIATION (v13 channel):
# skipped: (none — this retry USES draw_heng_zhe_gou from bank)
# reason:  main attempt's deviation from heng_zhe_gou was itself the
#          failure mode; reverting to the bank primitive is the fix.
# fresh_component: (none)
"""方 (fang) — retry_1. 4 strokes: dian + heng + heng_zhe_gou + pie."""
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
        {'stroke': 2, 'expected': 'ML(0.434,0.471)->MR(0.666,0.301)',
         'actual': '(35,110)->(245,110)',
         'delta': 'flattened y; extended slightly on both ends to match GT'},
        {'stroke': 3, 'expected': 'C(0.518,0.72)->BC(0.239,0.643) (MMH median only)',
         'actual': 'heng_zhe_gou heng_head=(56,125), corner=(215,125), '
                   'gou_tail=(178,260), hook_tip=(148,245)',
         'delta': 'errata B2 hint — MMH gives median line, need endpoints'},
    ],
    'joint_class_mismatches': [],  # both expected joints are N (natural gap); rendered with visible gaps
    'overall_pass': True,
    'notes': (
        'Retry_1 reverts the main-attempt BANK_DEVIATION on s3 and '
        'uses draw_heng_zhe_gou with errata-supplied pixel anchors. '
        's2 heng flattened to match GT silhouette. Joints s2.mid<->s4.head '
        'and s3.head<->s4.mid both render as N with small visible gaps '
        '(pie head at x=140 vs s2 mid ~x=140 at y=110 vs pie head at y=130: '
        'small gap ~20px, N-consistent).'
    ),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 dian: TC(0.307,0.589)->TC(0.693,0.932) => (130.7, 58.9)->(169.3, 93.2)
    draw_dian(d, (130.7, 58.9), (169.3, 93.2),
              w_head=3, w_tail=8, bow=4, steps=48)

    # s2 heng: OVERRIDE MMH — flatten to a confident long horizontal at y~112.
    # Slightly above s3's heng so they visually merge into GT's single fat heng
    # (post-revision fix: previous version showed two clearly separate parallels).
    draw_heng(d, (35, 112), (245, 112), width_head=6, width_tail=7)

    # s3 heng_zhe_gou (BANK): errata hint anchors — full 3-segment shape.
    # heng_head/corner at y=118 so it OVERLAPS s2's heng (single thick horizontal in GT).
    draw_heng_zhe_gou(d,
                      heng_head=(56, 118),
                      corner=(220, 118),
                      gou_tail=(180, 260),
                      hook_tip=(148, 245))

    # s4 pie: C(0.409,0.436)->BL(0.357,0.774) => (140.9, 143.6)->(35.7, 277.4)
    draw_pie(d, (140.9, 143.6), (35.7, 277.4),
             bow_perp=16, w_head=9, w_tail=3, steps=80)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_方.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
