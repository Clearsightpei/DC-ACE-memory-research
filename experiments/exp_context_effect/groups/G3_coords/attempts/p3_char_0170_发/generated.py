# generated.py — 发 (fā) — 5 strokes
# Structure (from GT):
#   1. Short 撇 top-left (small pie going down-left, top area)
#   2. Small 横折 (short horizontal turning down) top-middle
#   3. Long 撇 crossing from mid-upper to bottom-left (big shaft)
#   4. Long 捺 crossing from center to bottom-right (big shaft) — makes 又-like X
#   5. Dot at top-right
#
# Uses variant_pie / variant_na / variant_dian from _shared_helpers.
# Math coords: origin (150,150), +y up.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, variant_dian, tapered_line, to_px, kiss_apex,
)


def draw_fa(img):
    d = ImageDraw.Draw(img)

    # === Stroke 1: short 撇 top-left ===
    # A small pie in the upper-left, going down-left. Sits above the big-pie start.
    variant_pie(
        d,
        head=(-20, +95),
        tail=(-65, +45),
        bow_perp=-4.0,
        w_head=5.0,
        w_tail=1.5,
    )

    # === Stroke 2: small 横折 (short horizontal then turn down) ===
    # Top-middle small angled piece, sitting to the right of stroke 1.
    tapered_line(d, (-10, +100), (+35, +100), 3.5, 3.0)
    tapered_line(d, (+35, +100), (+22, +55), 3.0, 2.5)

    # === Stroke 5: dot at top-right ===
    variant_dian(
        d,
        head=(+60, +95),
        tail=(+88, +65),
        w_head=2.5,
        w_tail=10.0,
        bow_perp=-3.0,
    )

    # === Strokes 3 & 4: big 撇 + big 捺 forming the lower 又-like X ===
    # Big pie starts near center-upper, sweeps down-left to bottom-left corner.
    # Big na starts on the pie shaft (weld) and sweeps down-right to bottom-right.
    pie_head = (+10, +55)
    pie_tail = (-115, -115)
    na_tail = (+110, -115)

    # Weld the na head onto the pie shaft near u=0.30 for the X-cross look.
    p_head_used, na_head = kiss_apex(
        pie_head, pie_tail, na_tail, u_pie=0.30, bow_pie=-6.0
    )

    # Big pie.
    variant_pie(
        d,
        head=p_head_used,
        tail=pie_tail,
        bow_perp=-6.0,
        w_head=8.0,
        w_tail=1.5,
    )

    # Big na.
    variant_na(
        d,
        head=na_head,
        tail=na_tail,
        bow_perp=+8.0,
        w_head=2.0,
        w_belly=13.0,
        w_tail=3.0,
        belly_u=0.7,
    )


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw_fa(img)
    out = os.path.join(os.path.dirname(__file__), "01_发.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
