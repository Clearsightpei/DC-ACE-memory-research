# p3_char_0228_乩 — 乩 (jī), 6 strokes.
# Decomposition: 占 on left (卜 top + 口 bottom) + 乚 (竖弯钩) on right.
# Composition uses bank primitives bu (卜), kou (口), shu_wan_gou (乚).
# Revised once: first attempt used la_char which internally amplifies to
# scale=1.5 → oversized/misplaced 乚. Directly calling shu_wan_gou gives
# clean placement control.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bu import draw_bu                        # noqa: E402
from kou import draw_kou                      # noqa: E402
from shu_wan_gou import draw_shu_wan_gou      # noqa: E402


def draw_ji(t, ox=0.0, oy=0.0, scale=1.0):
    # Left: 占 (占字上下结构) centered on left half.
    # 卜 upper half at math (-72, 42), scale 0.55.
    draw_bu(t, ox=ox + (-72) * scale, oy=oy + 42 * scale, scale=0.55 * scale)
    # 口 lower half at math (-72, -55), scale 0.55.
    draw_kou(t, ox=ox + (-72) * scale, oy=oy + (-55) * scale, scale=0.55 * scale)
    # Right: 乚 (竖弯钩) directly, tall and reaching wide.
    draw_shu_wan_gou(t, ox=ox + 30 * scale, oy=oy + 5 * scale, scale=1.05 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ji(t)
    out = os.path.join(_HERE, "01_乩.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
