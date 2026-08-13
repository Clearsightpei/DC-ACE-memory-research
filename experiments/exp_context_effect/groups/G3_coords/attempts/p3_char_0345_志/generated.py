# p3_char_0345_志 — first attempt.
# 志 = top component (士/土 style) + 心 (heart) below.
# GT inspection: top heng is short, middle heng is longer, shu crosses
# both — matches the 土 pattern in MMH's rendering of 志. Use tu.py for
# the top component; use xin.py for the heart. Both are bank primitives
# used at deliberate (ox, oy, scale) per TR1-TR3.
import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from tu import draw_tu     # noqa: E402
from xin import draw_xin   # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Top component (土-style) — sits in upper half.
    # tu native at scale 0.55, oy_shift=+50 spans y~[+6, +67].
    draw_tu(draw, ox=0, oy=50, scale=0.55)

    # 心 (heart) — sits in lower half.
    # xin native primitive: scale param only scales the bowl (wo_gou);
    # dots use literal offsets (not scaled). Pass scale=1.0 for a
    # coherent bowl+dots and shift down via oy.
    draw_xin(draw, ox=0, oy=-45, scale=1.0)

    out = os.path.join(_HERE, "01_志.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
