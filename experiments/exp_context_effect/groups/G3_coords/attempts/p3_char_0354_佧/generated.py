# p3_char_0354_佧 — 佧 (kǎ) = 亻(left) + 卡(right).
# Left: bank ren_pang (亻) at moderate scale, shifted left.
# Right: inline 卡 = long 竖 + short-横 (upper) + long-横 (middle) + 点.
# 卡 is essentially 上 stacked on 卜 sharing the central shaft.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from shu import draw_shu             # noqa: E402
from heng import draw_heng           # noqa: E402
from dian import draw_dian           # noqa: E402

CANVAS = 300


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # -------- Left: 亻 (ren_pang) --------
    # Bank primitive; shift left so radical occupies left third.
    draw_ren_pang(d, ox=-70, oy=0, scale=0.95)

    # -------- Right: 卡 (kǎ) --------
    # Long vertical shu running from near top to near bottom, central-right.
    draw_shu(d, ox=40, oy=0, scale=0.78)

    # Short upper 横 (top of 上) — right of shaft, near y=+35.
    draw_heng(d, ox=68, oy=35, scale=0.28)

    # Long middle 横 (bottom of 上 / top of 卜) — spans wide across shaft.
    draw_heng(d, ox=48, oy=-2, scale=0.75)

    # 点 (dot on right side of shaft, lower half — 卜's dot).
    draw_dian(d, ox=78, oy=-25, scale=0.85)

    out = os.path.join(os.path.dirname(__file__), "01_佧.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
