# 经 (jīng) — Phase 3 character. Left-right layout:
#   Left: 纟 (silk radical, si_zi_pang from bank)
#   Right: 巠-simplified — top 又-like (draw_you) + bottom 工 (draw_gong)
#
# Composition uses bank primitives with deliberate (ox, oy, scale) per TR1-TR3.
# 纟 shifted well left; right side occupies right ~55% of canvas.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from si_zi_pang import draw_si_zi_pang  # noqa: E402
from you import draw_you                # noqa: E402
from gong import draw_gong              # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # LEFT: 纟 silk radical — shift left, small scale so its long 提
    # does not intrude into the right column (提 extends ~+60 in native).
    draw_si_zi_pang(draw, ox=-75, oy=-5, scale=0.65)

    # RIGHT: 巠-simplified — 又-like on top + 工 on bottom.
    # Right column centered near x=+45 (canvas x ~195).
    # 又 upper-right (small: shape between top two dots + arm)
    draw_you(draw, ox=55, oy=40, scale=0.55)
    # 工 lower-right — bottom heng anchors baseline of char
    draw_gong(draw, ox=55, oy=-40, scale=0.60)

    out_path = os.path.join(os.path.dirname(__file__), "01_经.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
