# p3_char_0029_入 (rù) — G3 coord-bank drawer. Revised vs clean GT.
#
# GT observations (clean version):
#   - 撇 starts near top-center with 顿笔 head, sweeps down-left,
#     mildly curved, tapers to thin tail at lower-left.
#   - 捺 head sits ON the 撇 shaft near the top (u~0.15-0.20 of pie),
#     with tiny pie tip visible above. 捺 has clear belly + thin
#     tapered tail flick to lower-right.
#   - Both strokes look calligraphic (visible thickness).
#
# Prior errata (p2_radical_030_入 FAIL twice): "Primitive can't
# express 'head on another stroke's u=0.3'. Inline both as fresh
# beziers." Continue with adaptive helpers.
#
# Math coord convention (P5): origin center (150,150), +y up.
# Canvas 300x300.

import os
import sys

from PIL import Image, ImageDraw

_HELPERS = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "success_bank", "code",
    )
)
if _HELPERS not in sys.path:
    sys.path.insert(0, _HELPERS)

from _shared_helpers import variant_pie, variant_na  # noqa: E402


def draw_ru(draw):
    """Render 入 into a PIL ImageDraw.

    Chosen anchors (math coords):
      撇 head: (+8, +90)    — top-center 顿笔 tip
      撇 tail: (-95, -105)  — long down-left sweep, past midline
      捺 head: (-8, +72)    — on pie shaft near u~0.18, pie tip above
      捺 tail: (+100, -105) — long lower-right sweep
    """
    # Stroke 1: 撇 (pie) — dominant left sweep with visible taper.
    # Head thick (顿笔), belly on the right (bow_perp negative = left
    # of centerline because perp is computed dx-based; keep small).
    variant_pie(
        draw,
        head=(8, 90),
        tail=(-95, -105),
        bow_perp=-4.0,      # very mild leftward bow
        w_head=11.0,        # thick 顿笔 head
        w_tail=2.0,         # tapered thin tail
        n=60,
    )

    # Stroke 2: 捺 (na) — head touches pie shaft close to top so
    # only a small pie tip pokes above; head thin (rests on pie),
    # belly heavy in the middle-lower, thin tapered flick tail.
    # pie at u=0.18 ≈ (8 + 0.18*(-103), 90 + 0.18*(-195))
    #             ≈ (-10.5, 54.9). Round to (-8, 72) to visually
    # sit right on the shaft accounting for stroke width.
    variant_na(
        draw,
        head=(-8, 72),
        tail=(100, -105),
        bow_perp=8.0,        # rightward belly bulge
        w_head=2.5,          # thin at start (rests on pie)
        w_belly=16.0,        # heavy calligraphic belly
        w_tail=2.0,          # thin tapered flick
        belly_u=0.72,        # belly bulges past midpoint
        n=64,
    )


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ru(draw)
    out = os.path.join(os.path.dirname(__file__), "01_入.png")
    img.save(out, "PNG")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
