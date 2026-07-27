# generated.py — p3_char_0122_五 (wǔ, "five"), 4 strokes.
# Stroke order:
#   1. Top short 横 (heng).
#   2. Slanted 撇/竖 down-left from under the top heng.
#   3. 横折 (heng-zhe) forming the middle 口-like enclosure to the right.
#   4. Long bottom 横 spanning the character width.
#
# Bank use:
#   - draw_heng for strokes 1 and 4 (top short, bottom long).
#   - Inline strokes 2 and 3 because they need custom slant / enclosure
#     geometry (no bank primitive is a clean fit — per shared_rules
#     "draw fresh the way G1 would" beats forcing an ill-fit primitive).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402

CANVAS = 300


def _P(mx, my, ox=0, oy=0):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox + mx, CANVAS / 2 - oy - my)


def draw_wu_char(t, ox=0, oy=0, scale=1.0):
    # 1. Top short heng: length ~110, centered near x=+5, at y~+80.
    draw_heng(t, ox=ox + 5, oy=oy + 80 * scale, scale=0.55 * scale)

    ink = max(2, int(round(9 * scale)))
    r = ink // 2 + 1

    # 2. Slanted vertical (竖/撇): from just under top heng down-left.
    #    Top at ~(-10, +75), bottom at ~(-55, -5). Leans left, longer.
    p2_top = _P(-10 * scale, 75 * scale, ox, oy)
    p2_bot = _P(-55 * scale, -5 * scale, ox, oy)
    t.line([p2_top, p2_bot], fill=(0, 0, 0), width=ink)

    # 3. Heng-zhe: horizontal from left across to right, then down.
    #    H segment: (-55, -5) -> (+60, -5). Enclosure width ~115.
    #    V segment: (+60, -5) -> (+55, -60). Descends to just above bottom heng.
    p3_hl = _P(-55 * scale, -5 * scale, ox, oy)
    p3_hr = _P(60 * scale, -5 * scale, ox, oy)
    p3_vt = _P(60 * scale, -5 * scale, ox, oy)
    p3_vb = _P(55 * scale, -60 * scale, ox, oy)
    t.line([p3_hl, p3_hr], fill=(0, 0, 0), width=ink)
    t.line([p3_vt, p3_vb], fill=(0, 0, 0), width=ink)

    # End caps to keep the joints solid.
    for cx, cy in (p2_top, p2_bot, p3_hl, p3_hr, p3_vb):
        t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # 4. Long bottom heng: full-width sweep at y~-80.
    draw_heng(t, ox=ox + 0, oy=oy - 80 * scale, scale=1.25 * scale)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_wu_char(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_五.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
