# p3_char_0580_疵 — 疵 (cī, flaw), 11 strokes.
# Composition: 疒 envelope (5) + 此 interior (6 = 止 4 + 匕 2).
#
# Bank use:
# - ne_sick.draw_ne_chuang(draw): 疒 envelope + 冫 marks (proven bank primitive,
#   PIL-native thin ink; used unchanged on 疰/疴/疸/疠/疥).
# - 此 (止 + 匕) inlined; no bank entry for 此 or 止 (bi_char is 比, distinct
#   composition — mirrored 匕s side-by-side, not 止+匕).
#
# GT observations (looked at gt/phase3/疵.png):
# - Standard 疒 envelope: small top-right dot, thin heng roof, long left pie
#   descending to lower-left, two small 冫 marks inside upper-left of belly.
# - Interior 此 sits in the RIGHT half of the envelope interior:
#     - 止 on the left of interior: short left 竖, small top tick,
#       taller right 竖, and a bottom 横 extending across;
#     - 匕 on the right: a 撇 sweeping down-left crossing near middle,
#       then 竖弯钩 curving right and up.
# - Interior baseline sits around y≈250; interior top around y≈145.
# - Thin uniform ink to match MMH GT weight.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from ne_sick import draw_ne_chuang  # noqa: E402


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


def _polyline(draw, pts, w=5):
    for i in range(len(pts) - 1):
        _tapered_line(draw, pts[i], pts[i + 1], w_head=w, w_tail=w, n=14)


def draw_ci_flaw(draw):
    # ---- 疒 envelope (5 strokes) via bank ---------------------------------
    draw_ne_chuang(draw)

    # ---- 止 interior-left (4 strokes) -------------------------------------
    # Occupies roughly x=140..195, y=150..250 in the envelope's right belly.
    W = 5

    # Stroke 1: left 竖 — short vertical on left of 止
    _tapered_line(draw, (145, 175), (145, 245), w_head=W, w_tail=W, n=20)

    # Stroke 2: short 横 (top tick going right from top of left 竖)
    _tapered_line(draw, (145, 175), (172, 172), w_head=W, w_tail=W, n=14)

    # Stroke 3: right 竖 — taller vertical to the right, extends higher
    _tapered_line(draw, (178, 150), (178, 245), w_head=W, w_tail=W, n=22)

    # Stroke 4: bottom 横 — long horizontal spanning across 止 base
    _tapered_line(draw, (130, 248), (200, 248), w_head=W, w_tail=W, n=22)

    # ---- 匕 interior-right (2 strokes) ------------------------------------
    # Occupies roughly x=200..260, y=155..255.

    # Stroke 5: 撇 — starts upper-right, sweeps down-left crossing near mid
    _tapered_line(draw, (240, 165), (205, 220), w_head=W + 1, w_tail=W - 1, n=24)

    # Stroke 6: 竖弯钩 — vertical from mid then curves right and hooks up
    # Vertical shaft
    _tapered_line(draw, (218, 190), (218, 235), w_head=W, w_tail=W, n=18)
    # Curve along bottom to the right
    _polyline(draw, [(218, 235), (225, 248), (240, 255), (258, 250)], w=W)
    # Small hook up at right end
    _tapered_line(draw, (258, 250), (258, 232), w_head=W, w_tail=W - 1, n=10)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ci_flaw(draw)
    out = os.path.join(_HERE, "01_疵.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
