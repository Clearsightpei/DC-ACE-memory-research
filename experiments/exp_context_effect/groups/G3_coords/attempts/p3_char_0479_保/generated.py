# 保 (bao, "protect") — p3_char_0479
# Composition: 亻 (left) + 呆 (right, stacked 口 above 木)
# Uses bank primitives: ren_pang (left), kou (top-right, small),
# mu (bottom-right, compressed).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from kou import draw_kou            # noqa: E402
from mu import draw_mu              # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # 亻 (left radical) — bank primitive, tall on the left, spans most height.
    draw_ren_pang(t, ox=-70, oy=-10, scale=0.85)

    # Right side: 呆 = 口 (top) stacked on 木 (bottom).
    # 口 sits above 木's crossbar, moderately sized.
    draw_kou(t, ox=45, oy=55, scale=0.42)

    # 木 lower-right; heng crossbar just under 口, na/pie legs down.
    draw_mu(t, ox=45, oy=-25, scale=0.55)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_保.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
