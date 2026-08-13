# p3_char_0404_佼 — 佼 = 亻 (left) + 交 (right)
# 交 = 亠 (top) + 八-like pair (mid) + 乂 crossing (bottom).
# Pattern reuses kang_char's tall-亻 recipe on the left and composes
# tou_radical + inline small pie/dian pair + inline crossing pie/na
# for the right.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from dian import draw_dian  # noqa: E402
from tou_radical import draw_tou_radical  # noqa: E402


CANVAS = 300


def _to_pixel(mx, my, canvas=CANVAS):
    return canvas / 2 + mx, canvas / 2 - my


def _draw_tall_ren_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """亻 tuned for compound composition — pie + tall shu."""
    draw_pie(t, ox=ox + (-8) * scale, oy=oy + 25 * scale, scale=0.85 * scale)
    top_x, top_y = _to_pixel(ox + 5 * scale, oy + 30 * scale)
    bot_x, bot_y = _to_pixel(ox + 5 * scale, oy + (-85) * scale)
    thickness = max(1, int(round(9 * scale)))
    t.line([(top_x, top_y), (bot_x, bot_y)], fill=(0, 0, 0), width=thickness)


def _draw_small_pie(t, head_mx, head_my, tail_mx, tail_my,
                    w_head=6, w_tail=1):
    """Inline small pie between two math-coord points (short 八 left leg)."""
    x0, y0 = head_mx, head_my
    x1, y1 = tail_mx, tail_my
    mx = (x0 + x1) / 2.0 - 3.0
    my = (y0 + y1) / 2.0 + 2.0
    n = 30
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _draw_small_dian(t, head_mx, head_my, tail_mx, tail_my,
                     w_head=2, w_tail=7):
    """Inline small na-ish dian (八 right leg)."""
    x0, y0 = head_mx, head_my
    x1, y1 = tail_mx, tail_my
    mx = (x0 + x1) / 2.0 + 2.0
    my = (y0 + y1) / 2.0 - 2.0
    n = 30
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_jiao_char(t, ox=0.0, oy=0.0, scale=1.0):
    """佼 = 亻 (left) + 交 (right)."""
    # LEFT: 亻 — tall recipe borrowed from kang_char
    _draw_tall_ren_pang(t, ox=ox - 75.0 * scale, oy=oy + 5.0 * scale,
                        scale=0.85 * scale)

    # RIGHT SLOT centered around x = +35
    rx = 35.0
    # TOP: 亠 (dot + heng lid), placed high in the right slot.
    # Use scale 0.42 so the heng ≈ 76px — fits within the right half.
    draw_tou_radical(t, ox=ox + rx * scale, oy=oy + 65.0 * scale,
                     scale=0.42 * scale)

    # MID: small 八 pair (short pie + short dian), just below the lid
    _draw_small_pie(t,
                    head_mx=ox + (rx - 3) * scale, head_my=oy + 40 * scale,
                    tail_mx=ox + (rx - 32) * scale, tail_my=oy + 15 * scale,
                    w_head=6, w_tail=1)
    _draw_small_dian(t,
                     head_mx=ox + (rx + 3) * scale, head_my=oy + 40 * scale,
                     tail_mx=ox + (rx + 32) * scale, tail_my=oy + 15 * scale,
                     w_head=2, w_tail=7)

    # BOTTOM: 乂 crossing — long pie + long na, X shape.
    # Pie: upper-right → lower-left (bank pie head is (+65, +90), tail (-45,-85)).
    # At scale 0.55, span mx ≈ 60, my ≈ 96.
    draw_pie(t,
             ox=ox + (rx - 5) * scale, oy=oy - 50 * scale,
             scale=0.55 * scale)
    # Na: upper-left → lower-right (bank na head is (-70, +80), tail (+80,-90)).
    draw_na(t,
            ox=ox + (rx - 5) * scale, oy=oy - 50 * scale,
            scale=0.55 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_jiao_char(t)
    out_path = os.path.join(os.path.dirname(__file__), "01_佼.png")
    img.save(out_path)
    print(f"wrote {out_path}")
