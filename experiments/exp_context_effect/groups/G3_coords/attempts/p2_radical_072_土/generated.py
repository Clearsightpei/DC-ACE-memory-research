# p2_radical_072_土 — G3 coord-bank attempt.
#
# 土 (tǔ) is a 3-stroke radical: short top 横 + middle 竖 + long bottom 横.
# It is the visual complement of 士 (shi_male in the bank): in 士 the TOP
# heng is longer; in 土 the BOTTOM heng is longer. Otherwise the layout
# (centered 竖 crossing both heng bars) is analogous.
#
# TR8 INLINE-FRESH TEST:
# - The three strokes (2× 横, 1× 竖) are cosmetically identical to their
#   standalone primitives after simple uniform scaling. No curl, no
#   distinctive taper, no compound geometry required. Both heng bars are
#   straight uniform ~12 px lines; the shu is a straight uniform vertical.
#   The bank primitives are a clean fit — this is exactly the case where
#   the primitives WORK (unlike the wavy/curled radicals from B1).
# - Composition is pure translation of primitive canonical placements.
#   No re-anchoring to a foreign landmark. TR3-compliant.
# - Not the "two-shrunk-primitives" failure signature (TR8 rule of thumb):
#   scales here are 0.55–0.85, but the composition is a well-understood
#   grid layout (two heng bars + centered shu) where the primitives are
#   IDENTICAL in shape to standalone use.
#
# TR3/TR6 transform derivation (math coords, center origin, +y up;
# 300×300 canvas):
#
# GT observation of the target 土:
#   - Top heng at math y ≈ +30, spanning canvas x [-60, +60] (short).
#   - Middle shu at math x ≈ 0, from y ≈ +55 (above top heng) down to
#     y ≈ -80 (touching bottom heng). Length ≈ 135 px → half_len ≈ 67 px
#     → scale ≈ 0.67.
#   - Bottom heng at math y ≈ -80, spanning x [-105, +105] (long).
#
# heng canonical: length 200 px (half_len 100 * scale), thickness 12 * scale.
#   - top: scale 0.60 → span 120 px (x ±60). ox=0, oy=+30.
#   - bottom: scale 1.05 → span 210 px (x ±105). ox=0, oy=-80.
# shu canonical: length 200 px (half_len 100 * scale).
#   - middle: scale 0.68 → length 136 px, center at (0, -12) so top at
#     y=+56 and bottom at y=-80 (welded to bottom heng). ox=0, oy=-12.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: short top 横 (shorter than the bottom bar — this is the
    # defining contrast vs 士). ox=0, oy=+30, scale=0.60.
    draw_heng(t, ox=0, oy=+30, scale=0.60)

    # Stroke 2: centered 竖 crossing both heng bars.
    # Top of shu (y = oy + 100*scale = -12 + 68 = +56) sits ~26 px above
    # the top heng at y=+30 (small tail above). Bottom of shu
    # (y = oy - 100*scale = -12 - 68 = -80) welds onto the bottom heng.
    # ox=0, oy=-12, scale=0.68.
    draw_shu(t, ox=0, oy=-12, scale=0.68)

    # Stroke 3: long bottom 横 — wider than top. ox=0, oy=-80, scale=1.05.
    draw_heng(t, ox=0, oy=-80, scale=1.05)

    out = os.path.join(os.path.dirname(__file__), "01_土.png")
    img.save(out)
    return out


if __name__ == "__main__":
    p = render()
    print(p)
