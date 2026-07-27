# p3_char_0066_囗 — character 囗 (wei).
# Orthographically identical to the Phase-2 radical 囗 (wei_radical).
# Per form_catalog.md "Character-vs-radical scaling" pattern: try IDENTITY
# alias with wei_radical at (0, 0, 1.0). GT shows a large box occupying
# most of canvas — same aspect/size as the wei_radical PASS at B2 pos 105.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from wei_radical import draw_wei_radical  # noqa: E402


def draw_wei_char(t, ox=0.0, oy=0.0, scale=1.0):
    """囗 character: identity alias of wei_radical."""
    draw_wei_radical(t, ox=ox, oy=oy, scale=scale)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wei_char(draw, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_囗.png")
    img.save(out)
    print(f"wrote {out}")
