# p2_radical_074_兀 — retry_1
#
# Prior fail (retry_0): leg widths mismatched (left ~9px tapered to 5;
# right uniform ~10). 竖弯钩 base too flat with no hook; leg tops didn't
# weld cleanly to the heng. Errata fix idea: "inline both legs with
# matched widths via variant_pie + inline bezier for curve+hook."
#
# Composition (兀 = top 一 + 儿):
#   Stroke 1: 横 (top) — bank primitive draw_heng, narrower than 一 stroke.
#     GT shows heng at ~y=100 (PIL), spanning ~x=[85, 215]. Uniform ~11 px.
#   Stroke 2: 撇 (left leg) — near-vertical with mild leftward curl at bottom.
#     Head welds under heng's LEFT end. Uniform-ish width ~10 -> tapers to ~3.
#     Use variant_pie with bow_perp = -3 (subtle left bow), matched w_head.
#   Stroke 3: 竖弯钩 (right leg) — vertical shaft → quarter-arc → short
#     horizontal → small upward hook. Head welds under heng's RIGHT end.
#     Matched shaft width to left leg (~10 px). Inline bezier for the
#     arc+tail+hook so widths match the left leg.
#
# Matched widths: both legs use w_head=10 near the top, tapering to ~3-4
# at their extreme tail (the pie tip / the hook tip). The 竖弯钩 shaft
# stays ~10 uniform until the arc, then tapers on the flick.

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

from heng import draw_heng  # noqa: E402
from _shared_helpers import variant_pie, tapered_line, tapered_bezier  # noqa: E402


CANVAS = 300


def draw_wu(draw):
    # Stroke 1: 横 (top). Placement: center at math (0, +52) → PIL (150, 98).
    # scale 0.65 → half-length 65 px, so spans PIL x=[85, 215]. Thickness 11.
    draw_heng(draw, ox=0, oy=+52, scale=0.65)

    # Stroke 2: 撇 (left leg). Head weld: PIL (~90, 105) = math (-60, +45).
    # Tail: PIL (~75, 235) = math (-75, -85). Slight leftward bow.
    # Use variant_pie with w_head=10, w_tail=4 to match the right leg's shaft.
    variant_pie(
        draw,
        head=(-60, +45),
        tail=(-75, -85),
        bow_perp=-4.0,
        w_head=10.0,
        w_tail=4.0,
    )

    # Stroke 3: 竖弯钩 (right leg) — inline for matched width control.
    # Shaft: PIL (205, 105) = math (+55, +45) → PIL (207, 210) = math (+57, -60).
    # Then quarter-arc curving right ending near PIL (232, 224) = math (+82, -74).
    # Small upward hook to PIL (228, 210) = math (+78, -60).
    # Widths: shaft uniform 10; taper on the flick down to 3.

    # Shaft: straight vertical, uniform width 10 (matches pie head width).
    tapered_line(
        draw,
        p0=(+55, +45),
        p1=(+57, -60),
        w0=10.0,
        w1=10.0,
    )
    # Curve+tail: bezier from shaft bottom → elbow → tail end.
    # REV1: extend the tail further right so the horizontal sweep is
    # visible (P4-ish: 弯 needs a clear horizontal reach, not just a
    # rounded corner). Control point pulled down-right for smooth arc.
    tapered_bezier(
        draw,
        p0=(+57, -60),
        p1=(+65, -80),   # elbow (bottom-right corner)
        p2=(+92, -78),   # tail end further right for visible sweep
        w_head=10.0,
        w_tail=7.0,
    )
    # Upward hook: short tapered flick UP-and-slightly-LEFT from tail
    # end (P1: hook must go UP; classic 竖弯钩 hook rises nearly
    # vertically or tilts slightly inward).
    tapered_line(
        draw,
        p0=(+92, -78),
        p1=(+86, -58),
        w0=7.0,
        w1=2.0,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_兀.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
