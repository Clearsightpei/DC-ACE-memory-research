# p3_char_0190_加 — 加 (jiā), 5 strokes: 力 (left) + 口 (right).
# 力 has NO bank primitive (per errata & drawer_memory L-R notes).
# Build 力 inline (横折钩 + 撇) and use draw_kou for the right box.
# Layout: 力 on left ~x=-90..-10, 口 on right ~x=+20..+90 (口 sits
# in middle band, 力 slightly taller and lower per GT).
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from kou import draw_kou  # noqa: E402

CX, CY = 150, 150  # canvas center for math->pixel conversion


def m2p(x, y):
    """math coord (y up) -> pixel."""
    return (CX + x, CY - y)


def draw_li_inline(d):
    """力 = 横折钩 (top+right shaft with bottom-left hook) + 撇 (down-left sweep).

    Left component of 加. Placed roughly x=-95..-15, y=+70..-95.
    """
    W = 6  # ink thickness (P12 thin GT convention)

    # 横折钩: horizontal from (-95,+65) → (-25,+65), then down to (-25,-80),
    # ending with a small hook curving up-left to (-40,-70).
    hz_pts = [
        m2p(-95, 65),   # heng start (left)
        m2p(-30, 68),   # heng end / zhe corner (slight rise for calligraphic lift)
        m2p(-25, 65),   # corner
        m2p(-30, -60),  # shu going down
        m2p(-38, -78),  # hook tip (curl up-left)
        m2p(-52, -70),  # hook end
    ]
    d.line(hz_pts, fill=(0, 0, 0), width=W, joint="curve")

    # 撇: from near top of the 横折钩 (around -35, +55) sweeping down-left
    # to bottom-left (around -95, -95). Slightly curved.
    pie_pts = [
        m2p(-35, 55),
        m2p(-55, 15),
        m2p(-75, -30),
        m2p(-92, -85),
    ]
    d.line(pie_pts, fill=(0, 0, 0), width=W, joint="curve")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 力 on left, inline.
    draw_li_inline(d)

    # 口 on right — call bank primitive at moderate scale, shifted right
    # and slightly down (GT shows 口 sitting in mid-lower band).
    draw_kou(d, ox=60.0, oy=-10.0, scale=0.55)

    out = os.path.join(os.path.dirname(__file__), "01_加.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
