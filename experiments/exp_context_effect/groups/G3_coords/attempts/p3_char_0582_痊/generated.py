# p3_char_0582_痊 — 痊 (quán, recover), 疒 (envelope) + 全 (interior).
#
# Composition:
#   - Envelope: 疒 via bank primitive `ne_sick.draw_ne_chuang` (B7 v9 grad).
#   - Interior: 全 = 人 (top pyramid) + 王 (three heng + shu below).
#     No 全 bank entry; inline fresh sized to sit inside the envelope's
#     right belly (roughly x=145..285, y=105..280 per 痂 template).
#
# Bank fit check:
#   - ne_sick envelope shape matches GT 痊 envelope. Use as-is (no
#     BANK_DEVIATION).
#   - wang_char is 亡, not 王. wang_go stub only. No callable 王/全
#     primitive. Inline fresh.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
import ne_sick

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_quan_inside(draw):
    """Inline 全 (人 + 王) sitting inside the 疒 envelope's right belly.

    Interior bounding roughly x=145..285, y=110..280.
    人 pyramid occupies upper portion (y≈115..175), 王 the lower
    portion (y≈180..270).
    """
    # ---- 人 (top pyramid) ----
    apex = (218, 118)
    # 撇 — apex sweeping down-left
    _tapered_bezier(
        draw,
        p0=apex,
        p1=(160, 190),
        ctrl=(190, 155),
        w_head=6.5,
        w_tail=4.0,
        n=60,
    )
    # 捺 — apex sweeping down-right, slight thickening then taper
    _tapered_bezier(
        draw,
        p0=apex,
        p1=(280, 190),
        ctrl=(248, 155),
        w_head=5.0,
        w_tail=6.0,
        n=60,
    )

    # ---- 王 (three 横 + one 竖) ----
    # Top heng (shorter)
    _tapered_line(draw, (180, 200), (260, 200), 4.5, 5.0, n=28)
    # Middle heng (shortest)
    _tapered_line(draw, (185, 230), (255, 230), 4.5, 5.0, n=28)
    # Vertical 竖 through the three heng
    _tapered_line(draw, (220, 195), (220, 270), 5.0, 5.0, n=32)
    # Bottom heng (longest)
    _tapered_line(draw, (170, 268), (272, 268), 5.0, 5.5, n=32)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Envelope: 疒 from bank.
    ne_sick.draw_ne_chuang(draw)

    # Interior: 全 inline.
    draw_quan_inside(draw)

    out = os.path.join(_HERE, "01_痊.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
