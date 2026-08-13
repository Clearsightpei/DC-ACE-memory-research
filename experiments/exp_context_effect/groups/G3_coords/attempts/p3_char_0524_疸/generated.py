# p3_char_0524_疸 — 疸 (dǎn, jaundice), 10 strokes.
# Composition: 疒 (5 strokes, sickness envelope) + 旦 (5 strokes: 日 + 一).
#
# Bank use:
# - ne_sick.draw_ne_chuang(draw): full 疒 envelope + 冫 marks. Used as-is —
#   its 冫 marks sit at x<105, and 旦 lives at x>135, so no visual clash.
# - 日 + 一 inlined here because 旦 has no bank entry (dan.py in bank = 丹,
#   not 旦), and ri.py is turtle-signature — we're on PIL Draw here.
#
# GT observations:
# - 疒 envelope matches ne_sick geometry (top dot upper-right, thin heng
#   roof, long pie descending down-left, two 冫 interior marks LEFT).
# - Interior 旦: small tall rectangle 日 in upper-right of envelope
#   interior, with middle bar; long horizontal 一 across the bottom
#   spanning the character's full lower width.

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


def draw_dan_jaundice(draw):
    # ---- 疒 envelope (5 strokes) via bank ---------------------------------
    draw_ne_chuang(draw)

    # ---- 旦 interior (5 strokes) -----------------------------------------
    # 日 — small tall rectangle in upper-right of envelope interior.
    # GT places it starting just right of the pie shaft, top just below
    # the heng roof.
    x_l = 148
    x_r = 218
    y_t = 138
    y_b = 218
    y_mid = 180
    w = 5
    # Stroke 1: left 竖
    _tapered_line(draw, (x_l, y_t), (x_l, y_b), w_head=w, w_tail=w, n=20)
    # Stroke 2: top 横 (part of 横折)
    _tapered_line(draw, (x_l, y_t), (x_r, y_t), w_head=w, w_tail=w, n=20)
    # Stroke 3: right 竖 (part of 横折) — slightly hooked feel via w_tail
    _tapered_line(draw, (x_r, y_t), (x_r, y_b), w_head=w, w_tail=w, n=20)
    # Stroke 4: middle 横
    _tapered_line(draw, (x_l + 2, y_mid), (x_r - 3, y_mid),
                  w_head=w - 1, w_tail=w - 1, n=20)
    # Stroke 5 (bottom 横 of 日) — closes rectangle
    _tapered_line(draw, (x_l, y_b), (x_r, y_b), w_head=w, w_tail=w, n=20)

    # ---- 一 base line of 旦 (final stroke) --------------------------------
    # Long horizontal spanning below 日 across most of the lower canvas.
    # Sits between the pie's tail and the right edge.
    _tapered_line(draw, (105, 258), (245, 258), w_head=6, w_tail=6, n=40)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_dan_jaundice(draw)
    out = os.path.join(_HERE, "01_疸.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
