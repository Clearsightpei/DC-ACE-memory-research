# p3_char_0400_佶 — 佶 (jí): 亻 (left) + 吉 (right), 8 strokes.
# 吉 = 士 (top) + 口 (bottom).
# Composition: ren_pang on left, shi_male stacked over kou on the right.
# Bank primitives use PIL ImageDraw API; t is a PIL ImageDraw object.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang    # noqa: E402
from shi_male import draw_shi_male    # noqa: E402
from kou import draw_kou              # noqa: E402


def draw_ji_char(t, ox=0.0, oy=0.0, scale=1.0):
    """佶 — 亻 (compressed, left) + 吉 stacked (士 top + 口 bottom, right)."""
    # Left 亻 — shifted well left, standard L-R scale
    draw_ren_pang(t, ox=ox + (-75) * scale, oy=oy + 0 * scale,
                  scale=0.95 * scale)
    # Right 吉: 士 on top (roughly upper half of right column),
    # 口 on bottom.
    # shi_male native span ~ shu height 76px scaled 0.76; keep ~0.55 here.
    draw_shi_male(t, ox=ox + 40 * scale, oy=oy + 55 * scale,
                  scale=0.55 * scale)
    # 口 sits below 士; kou native shu 50px at scale 0.55 -> ~55px tall.
    draw_kou(t, ox=ox + 40 * scale, oy=oy + (-55) * scale,
             scale=0.55 * scale)


def _render(out_png):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ji_char(d, ox=0.0, oy=0.0, scale=1.0)
    img.save(out_png, "PNG")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_佶.png")
    _render(out)
    print("Wrote", out)
