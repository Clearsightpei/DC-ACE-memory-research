# p3_char_0171_疒 — 疒 (sickness radical), 5 strokes.
# Structure: 广 (dian + heng + long-pie down-left) + 冫-like mirror dot
# pair tucked into the pie's belly on the left.
#
# Bank reuse: draw_guang (广 base), then two inline dots that mimic
# a 冫 pair — top dot slanting down-right, bottom dot slanting up-right
# (a mini提). Do NOT reuse bing.py wholesale — its lower stroke is too
# long/curved for a 疒 inner dot; inline shorter marks instead.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from guang import draw_guang  # noqa: E402


def _px(cx, cy):
    return 150 + cx, 150 - cy


def _draw_tapered_line(draw, p0, p1, w_head, w_tail, n=20):
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


def _draw_inner_dot_top(draw, ox, oy):
    # Upper inner dot — short slash down-right, sitting to the LEFT of the
    # pie body, roughly at the middle-upper region. Math coords with ox/oy.
    p0 = _px(ox + -70, oy + 0)
    p1 = _px(ox + -50, oy + -15)
    _draw_tapered_line(draw, p0, p1, w_head=3.5, w_tail=8.5, n=20)


def _draw_inner_dot_bottom(draw, ox, oy):
    # Lower inner mark — short up-right flick (提-like), sits below+left
    # of the upper dot, still on the belly-left side of the pie.
    p0 = _px(ox + -95, oy + -45)
    p1 = _px(ox + -70, oy + -35)
    _draw_tapered_line(draw, p0, p1, w_head=8.5, w_tail=2.5, n=20)


def draw_nechuang(t, ox=0.0, oy=0.0, scale=1.0):
    """疒 radical: 广 base + two inner dot marks on left side."""
    draw_guang(t, ox=ox, oy=oy, scale=scale)
    _draw_inner_dot_top(t, ox, oy)
    _draw_inner_dot_bottom(t, ox, oy)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Shift 广 up-right so pie tail lands near bottom-center; dots go
    # into left of pie belly.
    draw_nechuang(draw, ox=25, oy=-5, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疒.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
