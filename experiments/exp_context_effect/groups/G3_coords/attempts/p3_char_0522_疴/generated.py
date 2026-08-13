# p3_char_0522_疴 — 疴 (kē) = 疒 envelope + 可 interior
#
# Approach: reuse draw_ne_chuang envelope from bank (ne_sick.py — v9 rerun
# graduate). Inline 可 interior in the belly (right of pie shaft, below
# heng roof). Bank ke_can.py uses a turtle-flavored ox/oy signature and
# would clash with the envelope's PIL pixel space — inline is cleaner.
# (Same pattern as shan_hernia.py for 疝 = 疒 + 山.)
#
# GT decomposition (gt/phase3/疴.png):
#   - 疒 envelope: top dot, thin heng roof (~y 108), long left-descending
#     pie curving to (~85, 278), two 冫 marks tucked upper-left interior.
#   - 可 interior (right belly): short heng roof around y≈150,
#     small 口 (mouth) in lower-left of interior around y 180..215,
#     long 竖钩 on right edge running from y≈145 down to y≈285 with
#     a small hook flick left at the bottom.
#
# No BANK_DEVIATION: envelope is used as-is; interior 可 is inlined for
# coord-system compatibility (documented in shan_hernia.py precedent).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang  # noqa: E402

_CANVAS = 300


def draw_ke_interior(draw,
                     heng_x0=140, heng_x1=272, heng_y=150,
                     kou_x0=150, kou_x1=200, kou_y0=180, kou_y1=222,
                     shu_x=252, shu_y_top=145, shu_y_bot=285,
                     hook_dx=14, hook_dy=10, w=6):
    """可 rendered inline in the belly of 疒.

    heng — short top horizontal.
    kou — small square (口) at lower-left of interior.
    shu_gou — long vertical on right with left hook at bottom.
    """
    # Stroke 1: top 一 (heng) — short horizontal across belly top.
    draw.line([(heng_x0, heng_y), (heng_x1, heng_y)],
              fill=(0, 0, 0), width=w)

    # Stroke 2-4: 口 — small closed rectangle (three-stroke calligraphic
    # 口 rendered as four lines for clean corners).
    # Left 竖.
    draw.line([(kou_x0, kou_y0), (kou_x0, kou_y1)],
              fill=(0, 0, 0), width=w)
    # Top 横折 (top edge + right descending).
    draw.line([(kou_x0, kou_y0), (kou_x1, kou_y0)],
              fill=(0, 0, 0), width=w)
    draw.line([(kou_x1, kou_y0), (kou_x1, kou_y1)],
              fill=(0, 0, 0), width=w)
    # Bottom 一.
    draw.line([(kou_x0, kou_y1), (kou_x1, kou_y1)],
              fill=(0, 0, 0), width=w)

    # Stroke 5: 竖钩 — long right vertical + hook flick.
    draw.line([(shu_x, shu_y_top), (shu_x, shu_y_bot)],
              fill=(0, 0, 0), width=w)
    # Hook flick to upper-left.
    draw.line([(shu_x, shu_y_bot), (shu_x - hook_dx, shu_y_bot - hook_dy)],
              fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # 疒 envelope from bank.
    draw_ne_chuang(draw)
    # 可 interior (belly, right of pie shaft, below heng roof).
    draw_ke_interior(draw)
    out = os.path.join(_HERE, "01_疴.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
