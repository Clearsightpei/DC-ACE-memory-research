# p3_char_0017_又 — Phase-3 character render.
# Reuses the mastered radical primitive draw_you (entry #49, PASSed at
# p2_radical_037_又, B1 position 69). Character 又 == radical 又 in this
# curriculum, so the primitive applies. Revision vs corrupted-GT attempt:
# clean GT shows a larger, more balanced 又 filling the canvas — the heng
# top bar sits in the upper third, na sweep reaches wide bottom-right.
#
# TR compliance (per principles_meta TR1-TR3):
#   - TR1: (ox, oy, scale) explicitly chosen for THIS composition, not defaults.
#   - TR2: scale=1.15 to fill canvas more than radical PASS did — Phase-3
#     characters should occupy more of the 300x300 field than radicals did.
#   - TR3: ox=0, oy=-5 shifts slightly downward so the widened na foot
#     doesn't clip the bottom; center-of-mass stays near canvas center.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from you import draw_you  # noqa: E402

CANVAS = 300
OUT = os.path.join(os.path.dirname(__file__), "01_又.png")


def render() -> None:
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    # Deliberate (ox, oy, scale) per TR1 — chose scale=1.15 for character
    # fill, oy=-5 to keep na foot inside canvas, ox=0 for horizontal centering.
    draw_you(t, ox=0, oy=-5, scale=1.15)
    img.save(OUT)


if __name__ == "__main__":
    render()
