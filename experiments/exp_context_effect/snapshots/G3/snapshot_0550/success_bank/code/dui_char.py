# p3_char_0164_对 — 对 (duì), L-R compose: 又 (left) + 寸 (right).
# Uses two mastered bank primitives with deliberate (ox, oy, scale).
# Per principles_meta TR1-TR3 and index guidance for L-R compositions.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from you import draw_you   # noqa: E402
from cun import draw_cun   # noqa: E402


CANVAS = 300


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # 又 on the LEFT: compact, shifted left. Heng_pie unit spans -80..+65
    # at scale 1.0; at scale 0.65 that's -52..+42 wide. Place center at
    # ox=-40 so it occupies roughly x=[-92, +2]. oy slightly below center.
    draw_you(t, ox=-40, oy=-10, scale=0.65)

    # 寸 on the RIGHT: heng half_len at scale 0.75*0.75 = 0.56 -> 56 px.
    # Place ox=+55 -> heng spans -1..+111. Shu_gou at ox_delta +15*scale
    # gives vertical near x=+66. Dian in lower-left pocket around x=+43.
    draw_cun(t, ox=+55, oy=-5, scale=0.75)

    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_对.png")
    render().save(out)
    print(f"wrote {out}")
