# p3_char_0099_予 — 予 (yǔ), 4 strokes.
# Structure (top → bottom):
#   1) small 横撇 top (short heng right, then short pie down-left)
#   2) middle 横撇 forming a wider triangle (heng right, sharp turn, longer pie down-left)
#   3) 竖钩 vertical hook descender through center
# Skeleton draws inspired by liao.py (top hengou), heng_pie.py (turns), wan_gou.py (descender).

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _line(draw, p0, p1, w):
    draw.line([p0, p1], fill=(0, 0, 0), width=max(1, int(w)))


def _heng_pie(draw, x_left, y_left, x_right, y_right, x_tail, y_tail, w_head=8, w_tail=3):
    """Horizontal to (x_right,y_right), then tapered 撇 down-left to (x_tail,y_tail)."""
    # heng
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_left + (x_right - x_left) * t0
        ya = y_left + (y_right - y_left) * t0
        xb = x_left + (x_right - x_left) * t1
        yb = y_left + (y_right - y_left) * t1
        w = int(w_head - 1 * t0)  # slight taper
        _line(draw, (xa, ya), (xb, yb), w)
    # 顿笔 blob at the corner
    r = max(3, int(w_head * 0.7))
    draw.ellipse([x_right - r, y_right - r + 1, x_right + r, y_right + r + 2], fill=(0, 0, 0))
    # pie: down-left tapered
    steps = 24
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_right + (x_tail - x_right) * t0
        ya = y_right + (y_tail - y_right) * t0
        xb = x_right + (x_tail - x_right) * t1
        yb = y_right + (y_tail - y_right) * t1
        w = int(w_head - (w_head - w_tail) * t0)
        _line(draw, (xa, ya), (xb, yb), w)


def _shu_gou(draw, x_top, y_top, x_bot, y_bot, hook_dx=-20, hook_dy=-8, w_head=8, w_tail=10):
    """Vertical (slightly right-of-center) with a hook flick to upper-left at bottom."""
    # main vertical (very slight bow)
    steps = 40
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        # slight rightward bow at middle then back
        bow = 4
        bx0 = bow * (1 - (2 * t0 - 1) ** 2)
        bx1 = bow * (1 - (2 * t1 - 1) ** 2)
        xa = x_top + (x_bot - x_top) * t0 + bx0
        ya = y_top + (y_bot - y_top) * t0
        xb = x_top + (x_bot - x_top) * t1 + bx1
        yb = y_top + (y_bot - y_top) * t1
        # taper: thin at top, thicker in middle, slight taper at end
        if t0 < 0.5:
            w = w_head + (w_tail - w_head) * (t0 / 0.5)
        else:
            w = w_tail - (w_tail - w_head) * ((t0 - 0.5) / 0.5) * 0.3
        _line(draw, (xa, ya), (xb, yb), w)
    # hook: quadratic bezier from bottom flicking up-left
    hx_end = x_bot + hook_dx
    hy_end = y_bot + hook_dy
    hx_ctrl = x_bot - 4
    hy_ctrl = y_bot + 4
    hsteps = 18
    for i in range(hsteps):
        u0 = i / hsteps
        u1 = (i + 1) / hsteps

        def bez(u):
            x = (1 - u) ** 2 * x_bot + 2 * (1 - u) * u * hx_ctrl + u * u * hx_end
            y = (1 - u) ** 2 * y_bot + 2 * (1 - u) * u * hy_ctrl + u * u * hy_end
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(2, int(6 - 4 * u0))
        _line(draw, (xa, ya), (xb, yb), w)


def draw_yu(draw, ox=0, oy=0, scale=1.0):
    # --- Stroke 1: top 横撇 (short) ---
    # a bit more slanted, ending shorter pie
    _heng_pie(draw,
              x_left=115 + ox, y_left=82 + oy,
              x_right=185 + ox, y_right=70 + oy,
              x_tail=155 + ox, y_tail=112 + oy,
              w_head=7, w_tail=3)

    # --- Stroke 2: middle 横撇 (wider triangle) ---
    # slightly shorter pie tail so it doesn't extend beyond the character
    _heng_pie(draw,
              x_left=80 + ox, y_left=138 + oy,
              x_right=220 + ox, y_right=122 + oy,
              x_tail=95 + ox, y_tail=190 + oy,
              w_head=9, w_tail=3)

    # --- Stroke 3: 竖钩 descender through center ---
    _shu_gou(draw,
             x_top=170 + ox, y_top=95 + oy,
             x_bot=163 + ox, y_bot=258 + oy,
             hook_dx=-28, hook_dy=-4,
             w_head=6, w_tail=9)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yu(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_予.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
