# p3_char_0448_疥 — 疥 (jiè, scabies), 疒 (envelope) + 介 (interior).
#
# Composition:
#   - Left/envelope: 疒 via bank primitive `ne_sick.draw_ne_chuang`
#     (V9 graduate — thin uniform widths, matches GT posture).
#   - Interior/right: 介 rendered inline (no bank entry exists).
#     介 = 人 (pie + na) apex over two short verticals hanging inward.
#
# Bank fit check:
#   - ne_sick's envelope has heng roof to x=245 and pie sweeping to (85,278).
#     GT 疥 shows same envelope shape at ~same scale. Use as-is.
#   - No 介 primitive. Inline fresh.

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


def draw_jie_inside(draw):
    """Inline 介 sitting inside the 疒 envelope (right/interior band).

    介 has 4 strokes:
      1. pie (apex → bottom-left) — starts near top-center of interior
      2. na (apex → bottom-right) — from same apex, thin→thicker
      3. left short vertical (short dian-like, hanging inside)
      4. right short vertical (mirror)
    """
    # Apex of 人 — inside envelope, upper-right of interior area.
    # Revised: apex moved right/up; pie shortened so it doesn't cross the
    # envelope's descender; na shortened; verticals lengthened.
    apex = (205, 128)
    # Stroke 1: pie (down-left, ends above envelope belly).
    _tapered_bezier(
        draw,
        p0=apex,
        p1=(160, 200),
        ctrl=(180, 170),
        w_head=6.0,
        w_tail=3.5,
        n=60,
    )
    # Stroke 2: na (down-right, thin head → thicker tail).
    _tapered_bezier(
        draw,
        p0=apex,
        p1=(258, 205),
        ctrl=(235, 172),
        w_head=3.5,
        w_tail=6.0,
        n=60,
    )
    # Stroke 3: left short vertical hanging inside 介 (near-vertical).
    _tapered_line(draw, (185, 175), (183, 278), w_head=5.0, w_tail=4.0, n=30)
    # Stroke 4: right short vertical (near-vertical).
    _tapered_line(draw, (225, 175), (228, 278), w_head=5.0, w_tail=4.0, n=30)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Left/envelope: 疒 from bank primitive.
    ne_sick.draw_ne_chuang(draw)

    # Interior: 介 inline.
    draw_jie_inside(draw)

    out = os.path.join(_HERE, "01_疥.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
