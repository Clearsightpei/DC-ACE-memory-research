# p3_char_0035_丁 — G3 drawer attempt.
# 丁 = 2 strokes: top horizontal (heng) + vertical hook (shu_gou / 亅).
# Composition via bank primitives per TR1-TR3: heng at top, shu_gou centered
# beneath, its top touching under the heng.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng      # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


CANVAS_SIZE = 300


def draw_ding(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 丁: heng on top, shu_gou below (vertical hook curving up-left)."""
    # Top horizontal — spans most of canvas width. Canonical heng = 200 px.
    # GT has heng at roughly y=+40 (a bit above center), width ~200 px.
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 40 * scale, scale=0.95 * scale)

    # Vertical hook — shaft top just under the heng, extending down close
    # to canvas bottom. Canonical shaft half-len = 90*scale.
    # Use scale=0.95 → shaft ~171 px. Center at (ox+5, oy-45) so shaft top
    # is at y = -45 + 90*0.95 = +40.5 (touches heng) and bottom at
    # y = -45 - 85 = -130 (near bottom of canvas). Hook flick scaled with it.
    draw_shu_gou(t, ox=ox + 5 * scale, oy=oy + (-45) * scale, scale=0.95 * scale)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ding(draw, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_丁.png")
    img.save(out)


if __name__ == "__main__":
    main()
