# generated.py — 尣 (wāng, "lame") radical, 4画.
#
# GT decomposition (from gt/phase2/尣.png):
#   - top-left small 撇 sweeping from upper-right to lower-left (short, thin)
#   - top-right: small 横撇 (a short horizontal turning down-left into a short pie)
#   - main body: a large 竖弯钩 that starts as a curved 撇/shaft on the LEFT,
#     descends, then curves right along the bottom, ending with a small
#     upward hook on the right side.
#
# GT stroke thickness looks ~3-4 px. Not the heavy 12-px shafts of the
# canonical shu_wan_gou primitive. So we INLINE the whole character with
# tapered_bezier / tapered_line at reduced widths.
#
# Coord convention (P5): (0,0) at canvas center, +y up. PIL pixel = (150+x, 150-y).
#
# Layout targets (all math coords):
#   - Stroke 1 (top-left 撇): head PIL (105, 100) → math (-45, +50);
#     tail PIL ( 85, 130) → math (-65, +20).
#   - Stroke 2 (top-right short 横): PIL (175, 105) → math (+25, +45)
#     to PIL (200, 108) → math (+50, +42).
#   - Stroke 3 (top-right 撇 down from horizontal end): head PIL (200, 108)
#     → math (+50, +42); tail PIL (175, 148) → math (+25, +2).
#   - Stroke 4 (main 竖弯钩): starts PIL (95, 115) → math (-55, +35);
#     descends to PIL (95, 265) → math (-55, -115); curves right to
#     PIL (200, 275) → math (+50, -125); hooks up to PIL (200, 245)
#     → math (+50, -95). Thin (~4 px) throughout.

import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (                       # noqa: E402
    variant_pie, tapered_line, tapered_bezier, to_px,
)


def _draw_main_shu_wan_gou(t):
    """Inline the main 4th stroke of 尣: thin 竖弯钩 sized for this character.

    Segments:
      - descending curved shaft from (-55, +35) down to (-55, -115) —
        very slight leftward bow to give the ink calligraphic curl.
      - quarter-arc curving into horizontal bottom: from (-55, -115) to
        (+50, -125), passing through corner near (-55, -125).
      - short hook up-and-slightly-left from (+50, -125) to (+50, -95).
    """
    import math
    W = 4  # base thickness
    # Shaft — very shallow bow (bow_perp = -3, leftward)
    tapered_bezier(
        t,
        p0=(-55, 35),
        p1=(-56, -40),   # slight leftward mid-bow
        p2=(-55, -115),
        w_head=W, w_tail=W, n=40,
    )
    # Curve from (-55, -115) to (+50, -125) — quarter arc via bezier
    tapered_bezier(
        t,
        p0=(-55, -115),
        p1=(-55, -128),   # pull down and right
        p2=(+50, -125),
        w_head=W, w_tail=W, n=40,
    )
    # Upward hook from (+50, -125) to (+50, -95), tapered to a tip
    tapered_line(t, (50, -125), (50, -95), W, 2)


def draw_wang(t):
    """Render 尣 to PIL ImageDraw t on a 300×300 canvas."""

    # ---- Stroke 1: top-left small 撇 (short, softer) ----
    variant_pie(t,
                head=(-45, 50),
                tail=(-65, 20),
                bow_perp=-4,
                w_head=4, w_tail=1, n=32)

    # ---- Stroke 2: top-right short 横 ----
    tapered_line(t, (25, 45), (50, 42), 4, 4)

    # ---- Stroke 3: top-right 撇 down from horizontal end ----
    variant_pie(t,
                head=(50, 42),
                tail=(25, 2),
                bow_perp=-4,
                w_head=4, w_tail=1, n=32)

    # ---- Stroke 4: main 竖弯钩 (large, thin) ----
    _draw_main_shu_wan_gou(t)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wang(draw)
    out_path = os.path.join(os.path.dirname(__file__), "01_尣.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
