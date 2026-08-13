# p3_char_0418_例 (lì, "example") — 8 strokes.
# Composition: 亻 (left, 2 strokes) + 歹 (middle, 4 strokes) + 刂 (right, 2 strokes).
# Uses bank primitives ren_pang, dai, dao_pang scaled to a three-column L-M-R
# layout (~30% / ~35% / ~35%). This mirrors the men_plural (们) L-R pattern
# but with an additional middle column.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from dai import draw_dai  # noqa: E402
from dao_pang import draw_dao_pang  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — compressed, tall, lowered so pie doesn't tower over 歹.
    draw_ren_pang(d, ox=-95.0, oy=-15.0, scale=0.55)

    # 歹 middle — smaller so its top heng stays within middle column.
    draw_dai(d, ox=15.0, oy=-10.0, scale=0.45)

    # 刂 on right — shifted up so its top aligns with 歹 heng.
    draw_dao_pang(d, ox=100.0, oy=10.0, scale=0.60)

    out = os.path.join(_HERE, "01_例.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
