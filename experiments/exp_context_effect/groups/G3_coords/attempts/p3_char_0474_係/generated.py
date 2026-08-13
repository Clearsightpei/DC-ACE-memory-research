# 係 (xì) — L-R: 亻 (bank ren_pang) + 系 (inline: top-pie + two curl hooks + 小-like).
# 9 strokes total: 2 (亻) + 7 (系).
#
# Bank use: ren_pang for left. Right side (系) has no bank alias, so
# inline-fresh: top small 丿, two 撇折 curl hooks (like top of 纟), plus
# a bottom shu-hook with two flanking side pie/dian dots (小 flavor).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from _shared_helpers import variant_pie, tapered_bezier, to_px  # noqa: E402


CANVAS = 300


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _pie_zhe_hook(draw, cx, cy, size, ink=6):
    """A curl hook like top of 纟: down-left pie then a small heng out to right."""
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    h0 = (cx, cy)
    h2 = (cx + size * 1.7, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    r = ink * 0.75
    px, py = to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_xi_right(t, ox=0.0, oy=0.0, scale=1.0):
    """系 minus the leading pie context — top pie + two curl hooks + 小-like bottom."""
    s = scale
    # 1) top 丿 pie — small, sweeping down-left
    variant_pie(t,
                head=(ox + 20 * s, oy + 60 * s),
                tail=(ox - 25 * s, oy + 30 * s),
                bow_perp=2.0 * s, w_head=6.0 * s, w_tail=2.0 * s)
    # 2 & 3) two 撇折 curl hooks (纟-style upper region), stacked
    _pie_zhe_hook(t, cx=ox - 10 * s, cy=oy + 20 * s, size=16 * s, ink=6)
    _pie_zhe_hook(t, cx=ox - 15 * s, cy=oy - 10 * s, size=18 * s, ink=6)
    # bottom: 小-like — center shu-hook + left 撇 + right 点
    # center shu with slight hook
    x_shu = ox + 5 * s
    top_shu = oy - 30 * s
    bot_shu = oy - 75 * s
    p_top = to_px(x_shu, top_shu)
    p_bot = to_px(x_shu, bot_shu)
    t.line([p_top, p_bot], fill=(0, 0, 0), width=max(2, int(6 * s)))
    # small hook at bottom left
    p_hook = to_px(x_shu - 8 * s, bot_shu + 6 * s)
    t.line([p_bot, p_hook], fill=(0, 0, 0), width=max(2, int(5 * s)))
    # left short pie
    variant_pie(t,
                head=(ox - 5 * s, oy - 35 * s),
                tail=(ox - 40 * s, oy - 70 * s),
                bow_perp=-2.0 * s, w_head=6.0 * s, w_tail=1.5 * s)
    # right dian (as short falling stroke)
    variant_pie(t,
                head=(ox + 15 * s, oy - 40 * s),
                tail=(ox + 45 * s, oy - 70 * s),
                bow_perp=1.5 * s, w_head=4.0 * s, w_tail=6.0 * s)


def draw_xi_char(t, ox=0.0, oy=0.0, scale=1.0):
    """係: 亻 left + 系 right (inline)."""
    # Left: 亻 via bank ren_pang — compressed, seated near vertical center
    draw_ren_pang(t, ox=ox - 55 * scale, oy=oy - 10 * scale, scale=0.75 * scale)
    # Right: 系 inline — moderate size, centered vertically
    draw_xi_right(t, ox=ox + 30 * scale, oy=oy - 5 * scale, scale=1.05 * scale)


def _main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_xi_char(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_係.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    _main()
