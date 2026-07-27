# p2_radical_122_王 — G3 coord-bank attempt.
#
# 王 (wáng, king) is a 4-stroke radical: 横 + 横 + 竖 + 横.
# Structure: three horizontal bars stacked, crossed by a centered vertical.
# Bottom heng is the longest; top heng is medium; middle heng is shortest.
# Directly analogous to 土 (bank tu.py) but with an extra middle heng.
#
# Bank fit (TR3): both heng and shu primitives are clean straight lines
# with uniform thickness. The three heng bars differ only in scale/length.
# No taper, no curl, no compound geometry — this is exactly the case
# where the bank primitives WORK (per form_catalog "Enclosing/composition"
# rules — matching heng/shu thickness by staying at scale ~0.6-1.1).
#
# Reading the GT (math coords, center origin, +y up):
#   - Top heng at math y ≈ +55, spans x [-55, +55] (medium ~110 px).
#   - Middle heng at math y ≈ +5, shorter, spans x [-45, +45].
#   - Vertical shu at x ≈ 0, from y ≈ +65 (just above top heng) down
#     to y ≈ -70 (touching bottom heng). Length ≈ 135 px → scale ≈ 0.68.
#   - Bottom heng at math y ≈ -70, spans x [-100, +100] (long).
#
# Scales chosen using form_catalog rows for 土 as anchor:
#   - top heng   : scale 0.55 → span 110 px, oy=+55
#   - middle heng: scale 0.45 → span  90 px, oy=+5   (shorter than top)
#   - shu        : scale 0.68 → length 136 px, oy=-2 (top y=+66, bot y=-70)
#   - bottom heng: scale 1.00 → span 200 px, oy=-70
#
# TR3-clean: pure translation of primitive canonical placements.

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

    # Stroke 1: top 横 (medium length). ox=0, oy=+55, scale=0.55.
    draw_heng(t, ox=0, oy=+55, scale=0.55)

    # Stroke 2: middle 横 (shortest, slightly right-biased per GT).
    # ox=+8, oy=+5, scale=0.42.
    draw_heng(t, ox=+8, oy=+5, scale=0.42)

    # Stroke 3: centered 竖 crossing all three heng bars.
    # Top at y = -2 + 68 = +66 (just above top heng at y=+55).
    # Bottom at y = -2 - 68 = -70 (welds to bottom heng).
    draw_shu(t, ox=0, oy=-2, scale=0.68)

    # Stroke 4: long bottom 横 (widest). ox=0, oy=-70, scale=1.00.
    draw_heng(t, ox=0, oy=-70, scale=1.00)

    out = os.path.join(os.path.dirname(__file__), "01_王.png")
    img.save(out)
    return out


if __name__ == "__main__":
    p = render()
    print(p)
