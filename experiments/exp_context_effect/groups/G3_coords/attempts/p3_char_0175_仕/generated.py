# p3_char_0175_仕 — 仕 (shì): 亻 (left) + 士 (right), 5 strokes.
# Composition: ren_pang on left, shi_male on right.
# Bank primitives use PIL ImageDraw API (.line/.ellipse), so `t` here
# is a PIL ImageDraw object.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from shi_male import draw_shi_male  # noqa: E402


def draw_shi_char(t, ox=0.0, oy=0.0, scale=1.0):
    """仕 — 亻 (compressed, left) + 士 (right)."""
    # Left 亻 — shifted left, moderate scale (pie top well above center)
    draw_ren_pang(t, ox=ox + (-70) * scale, oy=oy + 0 * scale,
                  scale=0.95 * scale)
    # Right 士 — shifted right
    draw_shi_male(t, ox=ox + 30 * scale, oy=oy + (-5) * scale,
                  scale=0.85 * scale)


def _render(out_png):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shi_char(d, ox=0.0, oy=0.0, scale=1.0)
    img.save(out_png, "PNG")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_仕.png")
    _render(out)
    print("Wrote", out)
