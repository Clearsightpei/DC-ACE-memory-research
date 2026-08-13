# BANK_DEVIATION
# skipped: si_zi_pang.py
# reason: bank 纟 has a wide 提 (spans -65..+60 native) that in LR composition
#         intrudes deep into the right column; GT shows a short 提 confined
#         to the left column.
# fresh_component: si_zi_pang_LR_left (compressed 提, hooks in left column)
#
# p3_char_0451_给 — 给 (gěi/jǐ)
# L-R composition: 纟 (silk radical, fresh compressed) on left
#                + 合 (top: 亼 = 人-roof + 一, bottom: 口) on right.
# Right column still uses bank primitives ji_meet_char + kou_char.
# L/R split ~ 35/65. Left column x ~ [-140,-10]; right column x ~ [-5,+130].

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.normpath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ji_meet_char import draw_ji_meet_char   # noqa: E402
from kou_char import draw_kou_char           # noqa: E402


CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
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


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=6):
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    h0 = (cx, cy)
    h2 = (cx + size * 1.5, cy + size * 0.45)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)


def draw_si_zi_pang_LR_left(draw):
    """Fresh 纟 for LR-left column: hooks stacked, short 提 confined left."""
    # Upper small hook (higher, smaller)
    _draw_pie_zhe_hook(draw, cx=-90, cy=+55, size=15, ink=5)
    # Middle hook (slightly bigger)
    _draw_pie_zhe_hook(draw, cx=-95, cy=+10, size=18, ink=6)
    # Short 提 (short bottom stroke) — from lower-left up-right, kept in left column.
    p0 = (-115, -55)
    p2 = (-10, -30)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 5)
    _tapered_bezier(draw, p0, p1, p2, w_head=11, w_tail=1.5, n=50, head_ramp=0.08)


img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)

# Left: fresh compressed 纟
draw_si_zi_pang_LR_left(d)

# Right column: 合 = 亼 top + 口 bottom
# 亼 top (roof): scale ~ 0.50 gives ~90px roof span; oy=+55 lifts it up.
draw_ji_meet_char(d, ox=+55, oy=+55, scale=0.50)

# 口 bottom: scale ~ 0.42 gives ~55px box; oy=-55 below the roof.
draw_kou_char(d, ox=+55, oy=-55, scale=0.42)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "01_给.png")
img.save(out_path)
print("wrote", out_path)
