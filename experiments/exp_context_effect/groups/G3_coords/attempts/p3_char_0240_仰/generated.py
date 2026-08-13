#!/usr/bin/env python3
# 仰 (yang) — 亻 (left) + 卬 (right). ~6 strokes.
# 亻 from bank (ren_pang, compressed & left-shifted).
# 卬 inline: middle cluster = short 撇 + short 竖; right = 横折钩 (rendered
# as 3 line segments: heng + long shu + short left hook).
# Coord convention: math (center origin, +y up); to_px converts to PIL.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402

CANVAS_SIZE = 300


def to_px(x, y):
    return (CANVAS_SIZE / 2 + x, CANVAS_SIZE / 2 - y)


def line(t, p0, p1, w=6):
    t.line([to_px(*p0), to_px(*p1)], fill=(0, 0, 0), width=w)


def tapered(t, p0, p1, w0=8, w1=3, n=24):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        x0 = p0[0] * (1 - u0) + p1[0] * u0
        y0 = p0[1] * (1 - u0) + p1[1] * u0
        x1 = p0[0] * (1 - u1) + p1[0] * u1
        y1 = p0[1] * (1 - u1) + p1[1] * u1
        w = int(round(w0 * (1 - u0) + w1 * u0))
        t.line([to_px(x0, y0), to_px(x1, y1)],
               fill=(0, 0, 0), width=max(1, w))


def draw(t):
    # 亻 on left — compressed left-shift, lifted up.
    draw_ren_pang(t, ox=-70, oy=25, scale=1.15)

    # 卬 middle cluster: short 撇 (down-left, tapered) + short 竖 that
    # descends nearly full height so the left half of 卬 reads clearly.
    tapered(t, (-5, 75), (-30, 30), w0=8, w1=3, n=22)
    line(t, (-27, 32), (-24, -80), w=7)

    # 卬 right: 横折钩 — heng across top, long shu down (through baseline),
    # small hook back left at the bottom.
    line(t, (5, 70), (78, 70), w=6)
    line(t, (78, 72), (78, -115), w=7)
    line(t, (78, -115), (58, -108), w=6)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)
    draw(t)
    out = os.path.join(os.path.dirname(__file__), "01_仰.png")
    img.save(out)


if __name__ == "__main__":
    main()
