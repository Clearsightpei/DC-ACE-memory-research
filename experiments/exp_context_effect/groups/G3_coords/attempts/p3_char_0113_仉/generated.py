# p3_char_0113_仉 — 仉 = 亻 (left radical) + 几 (right component).
# Revision 1: first attempt was too small and 亻's shu too short compared
# to 几's height. GT shows both components filling most of the canvas
# vertically. Rebuild 亻 inline so its shu can be much longer (nearly as
# tall as 几). Keep bank 几 for the right side, sized larger.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from ji import draw_ji    # noqa: E402


def _to_pixel(mx, my, canvas=300):
    return canvas / 2 + mx, canvas / 2 - my


def draw_tall_ren_pang(draw, ox=0.0, oy=0.0, scale=1.0):
    """亻 tuned for compound-character composition — tall shu to match
    right-side 几. pie is compressed/steep, shu is long."""
    # pie: from upper (near top of canvas) down-left to mid, meeting the
    # top of the shu. Use bank pie compressed.
    draw_pie(draw, ox=ox + (-8) * scale, oy=oy + 25 * scale, scale=0.85 * scale)
    # shu: long vertical drop from the pie's mid to near bottom.
    top_x, top_y = _to_pixel(ox + 5 * scale, oy + 30 * scale)
    bot_x, bot_y = _to_pixel(ox + 5 * scale, oy + (-85) * scale)
    thickness = max(1, int(round(9 * scale)))
    draw.line([(top_x, top_y), (bot_x, bot_y)], fill=(0, 0, 0), width=thickness)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # 亻 on the left, made tall to match 几.
    draw_tall_ren_pang(draw, ox=-70.0, oy=0.0, scale=1.0)

    # 几 on the right, larger scale so its height ~= 亻's height and it
    # occupies the right 2/3 of the canvas.
    draw_ji(draw, ox=30.0, oy=-10.0, scale=0.85)

    out = os.path.join(_HERE, "01_仉.png")
    img.save(out)


if __name__ == "__main__":
    main()
