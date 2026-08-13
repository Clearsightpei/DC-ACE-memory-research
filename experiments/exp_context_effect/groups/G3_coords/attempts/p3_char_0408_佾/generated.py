# 佾 (yì) — 亻 (left) + 八 over 月 (right stack).
# Composition: ren_pang left; ba small top-right; yue bottom-right.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from ba import draw_ba  # noqa: E402
from yue import draw_yue  # noqa: E402


def draw_yi_char(D):
    # Left: 亻 person radical — taller/slightly bigger for tall char
    draw_ren_pang(D, ox=-65, oy=-5, scale=0.62)
    # Right-top: 八 small splayed cap, sitting well above 月
    draw_ba(D, ox=55, oy=95, scale=0.32)
    # Right-bottom: 月 (yue) — PIL-space primitive, shift right & slight down
    draw_yue(D, ox=45, oy=25, scale=0.60)


def main():
    img = Image.new("RGB", (300, 300), "white")
    D = ImageDraw.Draw(img)
    draw_yi_char(D)
    out = os.path.join(os.path.dirname(__file__), "01_佾.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
