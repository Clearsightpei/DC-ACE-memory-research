# p3_char_0154_他 — 他 (tā, "he/other")
# Composition: 亻 (ren_pang, left) + 也 (right).
# 也 = heng_zhe_gou (top box, hook down) + shu (inner short vertical)
#      + shu_wan_gou (bottom wrap, hook up-right).
#
# Revision 1: enlarge overall, fix ox/oy typo, reposition 也 strokes to
# match GT proportions (taller box, inner shu clearly visible, wrap
# stroke sweeping under and up on the right).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from shu import draw_shu  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


CANVAS_SIZE = 300


def draw_ta(t, ox=0, oy=0, scale=1.0):
    # ---- 亻 (left third) ---------------------------------------------
    # Centered around x ≈ -75. Scale 0.95 so it's tall like GT.
    draw_ren_pang(t, ox=ox + (-70) * scale, oy=oy + 10 * scale, scale=0.95 * scale)

    # ---- 也 (right two-thirds) ---------------------------------------
    # 也's local anchor at ≈ (+40, 0). Overall component scale 0.85.
    s = 0.85 * scale
    hx = ox + 40 * scale
    hy = oy + 0 * scale

    # 1. heng_zhe_gou — top bar spans local x∈[-90,+80], drops down to y=-70.
    #    In its own coords the corner is at (+80,+60) and hook base at (+80,-70).
    #    Place origin so hook base sits near (hx+80*s, hy-70*s).
    draw_heng_zhe_gou(t, ox=hx + 0, oy=hy + 10 * s, scale=s)

    # 2. shu — inner short vertical inside 也.
    #    Local shu is 200 px tall at scale 1.0. Use scale=0.35 → ~60 px.
    #    Position at x ≈ hx-25 (left-of-center inside box), y centered.
    draw_shu(t, ox=hx + (-25) * s, oy=hy + 20 * s, scale=0.35 * s)

    # 3. shu_wan_gou — bottom-left descending shaft that curves under
    #    and hooks up on the right, wrapping the whole 也.
    #    Local coords: shaft top (0,+70), shaft bot (0,-30), tail end (+80,-70),
    #    hook tip (+75,-48). We want shaft top near left side of the top box
    #    (≈ hx-55, hy+35) and tail sweeping to right edge below.
    draw_shu_wan_gou(t, ox=hx + (-55) * s, oy=hy + (-35) * s, scale=0.90 * s)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ta(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_他.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
