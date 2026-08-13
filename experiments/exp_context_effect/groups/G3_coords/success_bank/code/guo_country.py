# guo_country.py — 国 — promoted from p3_char_0363_国 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# p3_char_0363_国 — 8 strokes: outer 囗 envelope + inner 玉 (王 + 丶)
# Recipe: reuse hui_char pattern (outer wei_radical + inner component),
# swap the inner from 口 to inline 玉 (three 横 + one 竖 + one 丶).
# Bank fit: wei_radical is a clean identity fit for 囗 here (thin,
# rectangular, roughly centered). Skipping any bank for 玉 because
# yu_char.py in the bank is 于 (yú), not 玉 — inlining 玉 fresh.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from wei_radical import draw_wei_radical  # noqa: E402


def _line(D, p0, p1, w):
    D.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (x, y) in (p0, p1):
        D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=24):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)

    # ---------- Outer 囗 (envelope, bank identity alias) ----------
    draw_wei_radical(D, ox=0, oy=0, scale=1.0)

    # ---------- Inner 玉 (inline) ----------
    # Layout inside the box: 王 is a stack of 3 横 crossed by 1 竖,
    # plus a small 丶 in the lower-right quadrant.
    # Interior spans roughly x=90..210, y=95..215.
    W = 5
    cx = 150
    # top heng (short)
    _line(D, (110, 118), (185, 118), W)
    # middle heng (shorter, above the vertical's mid)
    _line(D, (115, 160), (180, 160), W)
    # bottom heng (widest of the three)
    _line(D, (100, 205), (200, 205), W)
    # vertical crossing all three
    _line(D, (cx, 118), (cx, 205), W)
    # 丶 (dot) — lower-right quadrant, below the middle heng
    _tapered_bezier(D, (170, 173), (180, 183), (190, 194), 2, W + 2, steps=18)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(out_dir, "01_国.png"))
    print("wrote", os.path.join(out_dir, "01_国.png"))


if __name__ == "__main__":
    main()
