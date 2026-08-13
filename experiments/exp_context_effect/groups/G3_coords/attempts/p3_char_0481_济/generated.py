# 济 (jì) — p3_char_0481
# LR composition: 氵 (left, bank san_dian_shui) + 齐 (right, inline fresh).
# 齐 is not in bank (亓/qi_ji is a related but different, simpler char).
# Right side inlined fresh — 6 strokes: 丶 一 丿 乀 丿 丨.
# BANK_DEVIATION not needed — san_dian_shui called directly; 齐 has no bank
# entry so inline is the only option.
#
# Revision 2 (2026-08-04): revision after visual diff vs GT.
# Fix: enlarge 氵 (was scale 0.60 → 0.85), push further left; simplify top
# of 齐 to a single dot above heng; enlarge pie/na X-spread and separate
# the two bottom legs cleanly.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from san_dian_shui import draw_san_dian_shui  # noqa: E402

CANVAS = 300
INK = (0, 0, 0)


def to_px(mx, my):
    return (CANVAS / 2 + mx, CANVAS / 2 - my)


def tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def draw_qi_right(d, ox=0, oy=0, s=1.0):
    """齐 — 6 strokes rendered inline. Coords in math space (y up)."""
    # Stroke 1: 丶 (top dot) — small slanted dot above heng
    tapered_line(d,
                 to_px(ox - 2 * s, oy + 105 * s),
                 to_px(ox + 8 * s, oy + 90 * s),
                 w0=3, w1=8, steps=15)

    # Stroke 2: 一 (heng) — top horizontal, spans the right column width
    tapered_line(d,
                 to_px(ox - 55 * s, oy + 78 * s),
                 to_px(ox + 60 * s, oy + 78 * s),
                 w0=5, w1=5)

    # Apex of the 人 X-cross — just below the heng, near center
    apex = to_px(ox + 3 * s, oy + 60 * s)

    # Stroke 3: 丿 (big pie) — from apex sweeping down-left
    tapered_bezier(d, apex,
                   to_px(ox - 30 * s, oy - 5 * s),
                   to_px(ox - 70 * s, oy - 80 * s),
                   w0=7, w1=2)

    # Stroke 4: 乀 (big na) — from apex sweeping down-right
    tapered_bezier(d, apex,
                   to_px(ox + 32 * s, oy - 5 * s),
                   to_px(ox + 75 * s, oy - 80 * s),
                   w0=4, w1=9)

    # Stroke 5: 丿 (left leg, short pie) — vertical-ish, leans slightly left
    tapered_bezier(d,
                   to_px(ox - 22 * s, oy - 10 * s),
                   to_px(ox - 30 * s, oy - 50 * s),
                   to_px(ox - 42 * s, oy - 95 * s),
                   w0=5, w1=3)

    # Stroke 6: 丨 (right leg, shu) — vertical
    tapered_line(d,
                 to_px(ox + 28 * s, oy - 10 * s),
                 to_px(ox + 28 * s, oy - 100 * s),
                 w0=5, w1=5)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # LEFT: 氵 water radical — bank primitive, well left, moderate scale
    draw_san_dian_shui(d, ox=-85, oy=+5, scale=0.85)

    # RIGHT: 齐 inlined fresh — centered around ox=+35
    draw_qi_right(d, ox=+35, oy=0, s=1.0)

    out = os.path.join(os.path.dirname(__file__), "01_济.png")
    img.save(out)
    print("saved:", out)


if __name__ == "__main__":
    main()
