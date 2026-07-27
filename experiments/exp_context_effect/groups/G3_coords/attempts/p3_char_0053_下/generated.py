# 下 (xia, "down") — Phase-3 char, 3 strokes:
#   1. 横 across upper portion (wide)
#   2. 竖 from mid-heng, going down (short)
#   3. 点 to the right of shu, upper portion
#
# Uses G3 bank primitives: draw_heng, draw_shu, draw_dian.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from dian import draw_dian   # noqa: E402


def draw_xia(t, ox=0.0, oy=0.0, scale=1.0):
    """下: wide top heng + centered shu below + small dian at upper-right of shu."""
    # 横 — top horizontal. GT heng is ~200 px wide.
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 60 * scale, scale=1.05 * scale)

    # 竖 — vertical from mid-heng down to lower canvas.
    draw_shu(t, ox=ox + (-2) * scale, oy=oy + (-30) * scale, scale=0.90 * scale)

    # 点 — small diagonal dot to the right of shu, slightly lower than heng.
    # Push it further right and lower so it clearly separates from shu.
    draw_dian(t, ox=ox + 40 * scale, oy=oy + 15 * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_xia(t, ox=0, oy=0, scale=1.0)

    out_path = os.path.join(os.path.dirname(__file__), "01_下.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
