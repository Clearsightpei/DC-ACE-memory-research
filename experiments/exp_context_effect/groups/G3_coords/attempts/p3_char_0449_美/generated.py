# BANK_DEVIATION
# skipped: (no 美 or 羊 bank entry; da_char.py exists but 大 here sits below 羊
#          at compressed scale, not standalone — inline is cleaner)
# reason: 美 = 丷 + three-heng + shu + bottom pie/na; needs one integrated
#         composition, not primitive stacking. Bank 大 assumes standalone
#         proportions; here bottom pie/na must nest under the third heng
#         and share the shu's baseline.
# fresh_component: mei_char_inline
#
# p3_char_0449_美 — 美 (měi, beautiful)
#
# Layout (top → bottom):
#   1. 丷 two dots at top (left leans down-left, right leans down-right).
#   2. Three heng, increasing in width top→bottom (羊 body).
#   3. Central shu (vertical) crossing all three heng.
#   4. Bottom pie + na (大 shape) sweeping wide from the third-heng band.

import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
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


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_mei_char(draw):
    # --- 1) 丷 top dots (short, dot-like) ---
    # Left dot (leans down-left)
    _tapered_line(draw, (138, 50), (128, 68), w_head=3.5, w_tail=5.0, n=18)
    # Right dot (leans down-right)
    _tapered_line(draw, (172, 50), (182, 68), w_head=3.5, w_tail=5.0, n=18)

    # --- 2) Three heng (short → medium → wide) ---
    # Top heng
    _tapered_line(draw, (108, 92), (198, 92), w_head=4.5, w_tail=4.5, n=25)
    # Middle heng (slightly slanting up)
    _tapered_line(draw, (95, 132), (215, 130), w_head=4.5, w_tail=4.5, n=25)
    # Bottom (wide) heng of the 羊 body
    _tapered_line(draw, (55, 175), (250, 172), w_head=4.5, w_tail=4.5, n=30)

    # --- 3) Central shu (vertical) crossing all three heng ---
    _tapered_line(draw, (152, 78), (152, 195), w_head=4.5, w_tail=4.5, n=30)

    # --- 4) Bottom 大: pie + na sweeping wide below the third heng ---
    # Pie: starts near top of third heng band, sweeps down-left far
    _tapered_bezier(
        draw,
        p0=(158, 168),
        p1=(40, 292),
        ctrl=(100, 230),
        w_head=5.5,
        w_tail=3.5,
        n=80,
    )
    # Na: starts on the pie's upper portion, sweeps down-right
    _tapered_bezier(
        draw,
        p0=(148, 200),
        p1=(280, 288),
        ctrl=(215, 240),
        w_head=3.5,
        w_tail=7.0,
        n=80,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_mei_char(draw)
    out = os.path.join(_HERE, "01_美.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
