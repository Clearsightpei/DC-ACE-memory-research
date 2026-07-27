# 兀 (wu) — 3 strokes: top 一 (heng) + 儿 (er_ren = 撇 + 竖弯钩)
# Compose bank primitives with deliberate (ox, oy, scale) per TR1-TR3.
# GT shows: wide top heng near y=+55, er_ren below spanning most of canvas width.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng            # noqa: E402
from er_ren import draw_er_ren        # noqa: E402


def draw_wu(t, ox=0, oy=0, scale=1.0):
    # Top 一: wide, near the upper third. Length ~170 px => scale 0.85.
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 55 * scale, scale=0.85 * scale)
    # 儿 below: keep it within canvas — scale 0.95, centered lower.
    draw_er_ren(t, ox=ox + 0 * scale, oy=oy + (-10) * scale, scale=0.95 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_wu(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_兀.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
