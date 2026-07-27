# p3_char_0110_分 — G3 (coord-bank)
# Composition: 八 on top (pie + na V-notch) + 刀 on bottom (横折钩 + long 撇).
# 分 = 4 strokes total.
#
# Bank primitives used:
#   - draw_ba (八 splayed)      → top of char, small scale
#   - draw_heng_zhe_gou         → 刀's frame stroke
#   - variant_pie (helper)      → 刀's long left-swept 撇 crossing under the frame
# TR-compliant: every call has deliberate (ox, oy, scale).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ba import draw_ba  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from _shared_helpers import variant_pie  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # --- 八 top: splayed pie+na occupying upper ~40% ---
    # Wider spread so 八 dominates top like the GT.
    draw_ba(draw, ox=0, oy=70, scale=0.75)

    # --- 刀 bottom: 横折钩 (short 横 + 竖钩) in lower-right ---
    # Smaller & shifted right — its horizontal top is short.
    draw_heng_zhe_gou(draw, ox=15, oy=-15, scale=0.45)

    # Long 撇 (刀's second stroke): starts high near 刀's top-left corner,
    # sweeps down-left crossing under the 竖钩. Head near the left of 横折钩's
    # 横 (approx ox=-25, oy=+30 area), tail at lower-left.
    variant_pie(
        draw,
        head=(-20, 30),       # near left tip of 刀's 横
        tail=(-100, -105),    # sweep to lower-left
        bow_perp=-12.0,
        w_head=10.0,
        w_tail=1.5,
        n=60,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_分.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
