# p3_char_0012_丷 (bā_top) — 2画, two mirrored small dots at top-of-radical.
#
# GT observation (from gt/phase3/丷.png):
#   - LEFT stroke: a thin curved "左点" (反点). Head at upper-right,
#     tail at lower-left. Modest downward-left slant, gentle concave-up
#     bow. Ink is fairly slim overall.
#   - RIGHT stroke: a slim "右点" that reads almost like a mini-撇.
#     Head at upper-left, tail tapered lower-right. Straighter than
#     the left dot. Slightly longer than the left dot.
#   - Both dots sit around the vertical middle of the canvas; there is
#     a clear V-notch gap between them.
#
# Prior attempt (retry_1) had the two dots too close, too thick,
# and too "loaded" (heavy dian caps). Fix: WIDER GAP, thinner ink,
# use variant_dian helper twice with mirrored head/tail positions.
#
# Approach: use `variant_dian` from _shared_helpers.py for both dots
# (P11: expose the angle/taper knobs the frozen dian primitive hides).
# Numbers derived fresh for this composition.

import os
import sys

_HELPERS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_HELPERS))

from PIL import Image, ImageDraw  # noqa: E402
from _shared_helpers import variant_dian  # noqa: E402

CANVAS = 300


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Revision (pass 2): left dot in GT is a THINNER, more curved crescent
    # than pass 1 produced. Reduce w_tail (7 not 9) and increase bow_perp
    # magnitude slightly for more visible arc. Also nudge right dot to
    # a slightly steeper vertical drop so the V-notch reads clearly.

    # LEFT dot (左点 / 反点): thin head upper-RIGHT -> moderate tail lower-LEFT.
    # Center roughly around math (-38, +8). Small span ~35 px.
    # More pronounced concave-up arc than pass 1 to match GT's crescent look.
    variant_dian(
        draw,
        head=(-22.0, 20.0),   # thin end, upper-right
        tail=(-55.0, -12.0),  # moderately heavy end, lower-left
        w_head=2.0,
        w_tail=7.0,           # reduced from 9 to slim the tail
        bow_perp=-4.5,        # more arc for the crescent shape
        n=40,
    )

    # RIGHT dot: slim right-leaning stroke, head upper-LEFT -> tail lower-RIGHT.
    # Slightly straighter and slightly more vertical than pass 1.
    variant_dian(
        draw,
        head=(20.0, 22.0),    # thin end, upper-left
        tail=(52.0, -22.0),   # tapered end, lower-right (needle)
        w_head=7.5,           # thicker head, tapered tail
        w_tail=1.8,
        bow_perp=-1.0,        # nearly straight
        n=40,
    )

    return img


if __name__ == "__main__":
    out = render()
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_丷.png"
    )
    out.save(out_path)
    print("Saved", out_path, out.size)
