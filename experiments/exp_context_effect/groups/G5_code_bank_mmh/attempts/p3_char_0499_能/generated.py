"""p3_char_0499_能 (neng, "can/able") — 10 strokes.

Composition (from GT + MMH anchors — y_frac is PIL top-down):
- top-left 厶-like (2 strokes: s1, s2)
- bottom-left 月 (compressed) (4 strokes: s3-s6)
- top-right 匕 (2 strokes: s7, s8)
- bottom-right 匕 (2 strokes: s9, s10)

# BANK_DEVIATION
# skipped: yue_moon.py, bi_dagger.py
# reason: quantitative aspect + span mismatch.
#   yue_moon native s1 pie: dx=-47/dy=+194 (long slanting sweep).
#   Target s3 (compressed 月-pie): dx=-1/dy=+118 (near-vertical, shorter).
#   yue_moon native box width ~90px; target 月 box width ~18-35px (compressed).
#   bi_dagger native pie dx=-115; top-right target dx=-44 (~2.6x narrower);
#   bottom-right target dx=-46 (~2.5x narrower).
#   Per P-A-007-v2 hard-check: whole-radical promotion requires uniform
#   (ox,oy,scale) shift; both fail — 能 packs 4 sub-radicals into the
#   canvas with very different aspect than each radical's standalone form.
# fresh_component: neng_inline_from_stroke_primitives (P-A-006 recipe:
#   MMH-anchor verbatim + stroke-primitive layer).

Reasoning trace (P-A-008):
  4-quadrant composition. Attempted whole-radical promotion (yue_moon,
  bi_dagger*2) → all fail uniform-shift hard-check (quantitative dx/aspect
  computed above). Fall back to per-stroke MMH endpoints + stroke primitives.
  All 8 joints are class N (natural gap ~9-27px) — do NOT weld any of the
  sub-radicals to each other or to their neighbors.
"""

import sys
import os

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw  # noqa: E402
from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


SELF_CHECK = {
    "visual_ok": None,
    "stroke_count_ok": True,     # 10 primitive calls below
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": None,
    "notes": (
        "P-A-006 recipe. All endpoints derived from MMH anchors using PIL "
        "top-down y convention (verified against 义 A-recipe calibration). "
        "All 8 joints class N — kept natural gaps at s1-s2, s3-s4, s3-s5, "
        "s3-s6, s4-s5, s4-s6, s7-s8, s9-s10."
    ),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # =============== TOP-LEFT 厶 (s1, s2) ===============
    # s1: TL(0.876,0.639)=(88,64) → C(0.242,0.286)=(124,129)
    #   short down-right slant (pie-fold entry stroke of ム-shape)
    draw_pie(d, (88, 64), (124, 129),
             bow_perp=-4, w_head=6, w_tail=3)
    # s2: C(0.166,0.061)=(117,106) → C(0.371,0.403)=(137,140)
    #   short down-right slant below s1 (folded-back tail of ム)
    draw_pie(d, (117, 106), (137, 140),
             bow_perp=-3, w_head=5, w_tail=3)

    # =============== BOTTOM-LEFT 月 (s3-s6) ===============
    # s3: ML(0.574,0.746)=(57,175) → BL(0.56,0.93)=(56,293)
    #   near-vertical pie (compressed 月 left column)
    draw_pie(d, (57, 175), (56, 293),
             bow_perp=3, w_head=8, w_tail=4)
    # s4: ML(0.744,0.781)=(74,178) → BL(0.92,0.795)=(92,280)
    #   heng_zhe_gou — extend heng LEFT toward s3.head, gou_tail at MMH tail
    draw_heng_zhe_gou(d,
                      heng_head=(60, 175),
                      corner=(92, 178),
                      gou_tail=(92, 280),
                      hook_tip=(80, 272))
    # s5: BL(0.735,0.115)=(74,212) → BC(0.031,0.074)=(103,207)
    #   upper inner heng
    draw_heng(d, (74, 212), (100, 209),
              width_head=5, width_tail=6)
    # s6: BL(0.709,0.443)=(71,244) → BC(0.04,0.405)=(104,241)
    #   lower inner heng
    draw_heng(d, (74, 244), (100, 241),
              width_head=5, width_tail=6)

    # =============== TOP-RIGHT 匕 (s7, s8) ===============
    # s7: TR(0.162,0.753)=(216,75) → C(0.723,0.195)=(172,120)
    #   compressed 匕-pie (short — 匕 is tightly packed here)
    draw_pie(d, (216, 75), (172, 120),
             bow_perp=-5, w_head=7, w_tail=3)
    # s8: TC(0.603,0.639)=(160,64) → MR(0.414,0.257)=(241,126)
    #   compressed 匕 shu_wan_gou: head top, gently descends+swings right,
    #   hook up-right to tail. Small bottom_extra since 匕 top-right is tight.
    draw_shu_wan_gou(d, (160, 64), (241, 126),
                     width=6, bottom_extra=40, knee_ratio=0.65)

    # =============== BOTTOM-RIGHT 匕 (s9, s10) ===============
    # s9: MR(0.238,0.919)=(224,192) → BC(0.778,0.338)=(178,234)
    #   short pie for bottom-right 匕
    draw_pie(d, (224, 192), (178, 234),
             bow_perp=-5, w_head=7, w_tail=3)
    # s10: C(0.629,0.811)=(163,181) → BR(0.66,0.373)=(266,237)
    #   shu_wan_gou for bottom-right 匕; bottom of curve near canvas bottom
    draw_shu_wan_gou(d, (163, 181), (266, 237),
                     width=6, bottom_extra=45, knee_ratio=0.6)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_能.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
