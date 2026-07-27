# generated.py — 小 (xiǎo, "small"). 3 strokes:
#   center 竖钩 + left short 撇 + right 点.
#
# Per memory_index.md read-order: Phase-3 character 小 shares its shape
# with the mastered radical 小 (draw_xiao in success_bank). Use IDENTITY
# alias — TR-compliant (ox=0, oy=0, scale=1.0 chosen deliberately for
# centered rendering).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from xiao import draw_xiao  # noqa: E402


def draw_xiao_char(t, ox=0, oy=0, scale=1.0):
    """Identity alias: 小 character == 小 radical shape."""
    draw_xiao(t, ox=ox, oy=oy, scale=scale)


def main():
    canvas = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(canvas)
    draw_xiao_char(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_小.png")
    canvas.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
