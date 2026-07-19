# p2_radical_030_入 — 入 radical (2 strokes: 撇 + 捺).
#
# 入 vs 人 (key distinction, critical for this item):
#   - 人: pie and na MEET at the top apex (both stroke heads converge to
#     a single point).
#   - 入: the pie is the DOMINANT stroke. It starts at the top-CENTER (or
#     slightly right-of-center at the peak), sweeps down-left. The na
#     starts NOT at the apex but PARTWAY DOWN the pie's shaft (roughly
#     upper-third), then sweeps right-and-down. The na's head "kisses"
#     the pie's shaft interior; it does NOT reach the pie's own head.
#     Result: top of 入 shows a single small peak with the pie's head
#     sticking slightly up-left above the na's head.
#
# GT-derived plan:
#   - Pie: peak at math (~+5, +85), tail at (~-70, -80). Long sweeping
#     curve — bowed left in the middle. Full-canvas height.
#   - Na: head lands on pie shaft at ~30% of the way down from pie head.
#     Pie head PIL (155, 65), pie tail PIL (80, 230). 30% down: PIL
#     (~132, 115) = math (~-18, +35).
#     Na standalone head is at math (-70*s, +80*s). To place head at
#     (-18, +35), pass ox = -18 - (-70*s), oy = 35 - 80*s.
#   - Na tail should land right-of-center at similar height to pie tail.
#     Standalone na tail is (+80*s, -90*s); scale 0.85 -> tail lands
#     around (+68, -76). With the ox we computed, na tail PIL will be
#     ~(150+50+68, 150+41+76) = (~268, 267) — too far off. Reduce scale
#     to 0.75.
#
# TR6 comment trail:
#   pie: scale=0.85, ox=-60 (so head is upper-center), oy=-5.
#     pie head standalone at math (+65*0.85, +90*0.85)=(+55, +77).
#     Placed head math = ox+55, oy+77 = (-5, +72). PIL (145, 78). Good.
#     pie tail standalone at (-45*0.85, -85*0.85)=(-38, -72).
#     Placed tail math = (-60-38, -5-72) = (-98, -77). PIL (52, 227).
#     Long sweep across canvas. Good.
#   na: scale=0.75, head placement — want head at ~PIL (145, 130) which
#     is math (-5, +20).
#     na head standalone at math (-70*0.75, +80*0.75) = (-52.5, +60).
#     ox = -5 - (-52.5) = +47.5, oy = 20 - 60 = -40.
#     na tail standalone at (+80*0.75, -90*0.75) = (+60, -67.5).
#     Placed tail math = (+47.5+60, -40-67.5) = (+107.5, -107.5).
#     PIL (257.5, 257.5). Right-and-down. Good — but slightly outside
#     margin. Nudge scale to 0.70.
#     scale=0.70: na head at (-49, +56). ox = -5 - (-49) = +44, oy = 20-56=-36.
#     na tail at (+56, -63). Placed = (+44+56, -36-63) = (+100, -99).
#     PIL (250, 249). Better.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # REVISION notes (pass 2):
    # - First pass: na head sat in empty space, not on pie shaft — gap.
    # - Fix: shift na left (reduce ox) and up (increase oy) so head lands
    #   directly on the pie shaft at ~PIL (140, 115).
    # - Also tighten pie curvature: original placement OK, keep pie.

    # 撇 (pie): dominant sweep, head near top-center, tail lower-left.
    # scale=0.85, ox=-60, oy=-5 → head math (-5, +72), tail math (-98, -77).
    # PIL head (145, 78), PIL tail (52, 227). Shaft midline at PIL x ≈
    # linear interp; at PIL y=115, x ≈ 145 + (115-78)/(227-78) * (52-145)
    #    = 145 + 0.248 * (-93) = 145 - 23 = 122. So shaft point at ~(122, 115).
    #    math coord: (-28, +35).
    draw_pie(t, ox=-60.0, oy=-5.0, scale=0.85)

    # 捺 (na): head must land ON pie shaft at ~PIL (122, 115) = math (-28, +35).
    # scale=0.75, na head standalone at (-52.5, +60).
    #   ox = -28 - (-52.5) = +24.5, oy = 35 - 60 = -25.
    #   na tail standalone at (+60, -67.5). Placed math = (+84.5, -92.5).
    #   PIL (234.5, 242.5). Right-and-down, within canvas margin. Good.
    draw_na(t, ox=+24.5, oy=-25.0, scale=0.75)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_入.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
