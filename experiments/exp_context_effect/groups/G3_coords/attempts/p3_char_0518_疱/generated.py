# p3_char_0518_疱 — 疱 (pào, blister), 疒 (envelope) + 包 (interior).
#
# Composition:
#   - Envelope: 疒 via bank primitive `ne_sick.draw_ne_chuang`
#     (V9 graduate — thin uniform widths, matches GT posture).
#     Same recipe pattern as 疥 (B10 PASS) and 疝 (B10 PASS).
#   - Interior: 包 (勹 envelope + 巳-like inner) rendered inline.
#     bao_char bank exists but its coords are baked for full canvas
#     (x∈[60,232], y∈[45,278]) — cannot shrink cleanly into the ~110x140
#     interior slot of 疒 without distortion. Better to inline compact.
#
# BANK_DEVIATION
# skipped: bao_char.py
# reason: bank 勹 primitive's baked coord range (~170x230 canvas span)
#         does not compress into 疒's interior slot without deforming
#         hook geometry; inline lets me match the smaller 包 in GT.
# fresh_component: bao_compact_for_ne (small 勹+巳 for 疒 interior)

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


def _tapered_qbez(draw, p0, p1, ctrl, w_head, w_tail, n=60):
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


def _tapered_cbez(draw, p0, p1, p2, p3, w_head, w_tail, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_bao_inside(draw):
    """Inline 包 sitting inside the 疒 envelope (right/interior band).

    包 = 勹 envelope + 巳-like inner shape.
    Interior slot: roughly x∈[140,260], y∈[110,280].
    """
    # -- 勹 envelope (welded, one continuous shape) --
    # Stroke 1: short 撇 (top-left pie) — small down-left slash,
    # tail welded to envelope top start.
    _tapered_qbez(
        draw,
        p0=(180, 105),
        p1=(158, 140),
        ctrl=(168, 122),
        w_head=6.0,
        w_tail=4.0,
        n=30,
    )

    # Stroke 2: envelope — heng top → shoulder → shaft down → hook up-left.
    # Heng from pie-tail (158,140) rightward to (242,138).
    _tapered_line(draw, (158, 140), (242, 138), w_head=5.0, w_tail=5.0, n=40)
    # Shoulder + shaft: from (242,138) down to (215,258) with slight bow.
    _tapered_cbez(
        draw,
        p0=(242, 138),
        p1=(252, 155),
        p2=(240, 210),
        p3=(215, 258),
        w_head=5.0,
        w_tail=4.0,
        n=50,
    )
    # Hook: small up-left flick from (215,258) to (195,245).
    _tapered_qbez(
        draw,
        p0=(215, 258),
        p1=(205, 258),
        ctrl=(195, 246),
        w_head=4.5,
        w_tail=2.0,
        n=20,
    )

    # -- 巳-like inner (small compact box + rising hook) --
    # Top heng-zhe: small box top-left corner to top-right, then turn down.
    _tapered_line(draw, (170, 175), (222, 173), w_head=4.5, w_tail=4.5, n=30)
    _tapered_line(draw, (222, 173), (222, 210), w_head=4.5, w_tail=4.5, n=20)
    # Interior heng closing the top box (creates the 巳 mid-bar).
    _tapered_line(draw, (170, 205), (222, 207), w_head=4.0, w_tail=4.0, n=25)
    # Left shaft descending, then a rising 竖弯钩 flick.
    _tapered_line(draw, (170, 175), (170, 232), w_head=4.5, w_tail=4.5, n=25)
    _tapered_qbez(
        draw,
        p0=(170, 232),
        p1=(200, 240),
        ctrl=(185, 242),
        w_head=4.5,
        w_tail=3.0,
        n=25,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Envelope: 疒 from bank primitive.
    ne_sick.draw_ne_chuang(draw)

    # Interior: 包 inline.
    draw_bao_inside(draw)

    out = os.path.join(_HERE, "01_疱.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
