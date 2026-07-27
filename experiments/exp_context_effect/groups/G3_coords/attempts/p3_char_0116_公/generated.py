# p3_char_0116_公 — 公 ("public"), 4 strokes:
#   1) top-left 撇 (splayed left)
#   2) top-right 捺 (splayed right) — the top forms 八-like shape
#      but WITHOUT a V-notch; the two top strokes converge near the
#      top-center (compare 亼's kiss_apex — here they don't fully
#      kiss, they just approach a shared apex).
#   3) bottom 撇 (下 撇 of 厶) — starts near center-top of 厶, curves down-left
#   4) bottom 折/dot (of 厶) — small hook/turn from mid to lower-right
#
# Reading the GT (gt/phase3/公.png): the top opens wider than an 八
# radical; the two top strokes almost meet near center-top (small
# gap ~ 1-3 px). The bottom 厶 sits under the meeting point, its
# 撇 mirroring left, closed by a small right-going hook.
#
# Approach: use variant_pie and variant_na from _shared_helpers for the
# top two strokes with thin uniform widths (P12 — MMH GTs are thin,
# ~3-4 px). Inline the 厶 as a small pie + a short curved segment.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import variant_pie, variant_na, tapered_bezier, tapered_line, to_px  # noqa: E402


def draw_gong_char(draw, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # ---- TOP 八 (open, small gap at apex) ----
    # Left 撇: starts near top-center (slightly left), sweeps down-left.
    pie_head = P(-6, +85)
    pie_tail = P(-95, -20)
    variant_pie(draw, head=pie_head, tail=pie_tail,
                bow_perp=-8.0, w_head=3.5, w_tail=2.0)

    # Right 捺: starts near top-center (slightly right), sweeps down-right,
    # ends with a slight belly-taper.
    na_head = P(-2, +80)
    na_tail = P(+100, -20)
    variant_na(draw, head=na_head, tail=na_tail,
               bow_perp=+8.0, w_head=2.5, w_belly=4.0,
               w_tail=2.0, belly_u=0.72)

    # ---- BOTTOM 厶 ----
    # 厶 in 公 is actually TWO strokes in MMH: 撇折 (a bent stroke —
    # down-left then a horizontal-ish hook) + 点.
    # Looking at the GT: bottom 厶 sits below the top apex, wider than
    # my first pass. The 撇 starts high-right of center, sweeps down-left,
    # then the 折 turns right along the bottom, and a small dot closes it.

    # Stroke 3: 撇 of 厶 — starts under the top apex, curves down-left,
    # ending near the bottom-left of the 厶.
    xie_head = P(+5, -20)
    xie_tail = P(-55, -85)
    variant_pie(draw, head=xie_head, tail=xie_tail,
                bow_perp=-4.0, w_head=3.0, w_tail=2.5)

    # Stroke 4: 折 (bottom horizontal-ish) — turns right from the
    # bottom of stroke 3, curving up slightly with a small terminal dot.
    # Render as a bezier that arcs from bottom-left to right, plus a
    # small terminal dot suggesting the closing 点.
    tapered_bezier(
        draw,
        P(-45, -80),     # start (near stroke 3 tail area)
        P(+15, -95),     # control (down center)
        P(+50, -70),     # end (right side, slightly up)
        w_head=2.5, w_tail=3.5, n=40,
    )
    # small terminal dot / 点 for the 厶 closure
    tapered_line(draw, P(+45, -68), P(+62, -60), w0=3.5, w1=2.0, n=10)


def main():
    W, H = 300, 300
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    # Center of image is (150, 150). variant_pie/na use math coords
    # (center origin at (150,150), +y up) — that's handled by to_px inside
    # the helpers. So we call draw_gong_char at ox=0, oy=0.
    draw_gong_char(draw, ox=0, oy=0, scale=1.0)

    out = os.path.join(os.path.dirname(__file__), "01_公.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
