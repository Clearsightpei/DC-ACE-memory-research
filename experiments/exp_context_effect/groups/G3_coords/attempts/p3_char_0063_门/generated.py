# p3_char_0063_门 — 门 (mén, "door"), 3 strokes.
# Strokes: 点 (upper-left small dot), 竖 (left vertical leg),
#          横折钩 (top + right vertical + hook — tall envelope on the right).
# G3 coord-format: PIL rendering with numeric offsets. Uses bank primitives
# where they fit (dian) and inlines the other two strokes with 门-specific
# proportions (bank shu/heng_zhe_gou both have proportions tuned for their
# own default composition and don't match 门's tall/narrow envelope).

import os
import sys
from PIL import Image, ImageDraw

# Make the bank importable for the dian primitive.
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from dian import draw_dian  # noqa: E402

CANVAS = 300


def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_men(D, ox=0, oy=0, scale=1.0):
    """门 = 点 (upper-left) + 竖 (left leg) + 横折钩 (top + right + hook).

    Layout (PIL px, 300x300 canvas, character occupies roughly y=45..255):
      - Dot at (~90, ~65).
      - Left 竖 vertical leg from (~80, ~95) to (~78, ~255), thin.
      - 横折钩: heng from (~110, ~75) to (~230, ~72), then vertical down
        to (~228, ~245), then short up-left hook.
    """
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    # Stroke 1 — 点 (upper-left small dot)
    # Place dot roughly at (95, 85) PIL — a bit larger and closer to left leg top.
    draw_dian(D, ox=-58, oy=68, scale=0.60)

    # Stroke 2 — 竖 (left leg), fresh inline for 门 proportions.
    # Starts a little to the right of the dot, goes to bottom.
    top = (X(80), Y(110))
    bot = (X(76), Y(258))
    _tapered_line(D, top, bot, w0=int(9 * scale), w1=int(10 * scale), steps=32)
    # Rounded top cap.
    D.ellipse([top[0] - 4, top[1] - 4, top[0] + 4, top[1] + 4], fill=(0, 0, 0))
    # Rounded bottom cap.
    D.ellipse([bot[0] - 5, bot[1] - 5, bot[0] + 5, bot[1] + 5], fill=(0, 0, 0))

    # Stroke 3 — 横折钩 (top + right vertical + hook), inline.
    # Horizontal top from left-side to right-side.
    h_left = (X(110), Y(75))
    h_right = (X(230), Y(72))
    _tapered_line(D, h_left, h_right,
                  w0=int(9 * scale), w1=int(11 * scale), steps=24)
    # Corner blob at top-right.
    D.ellipse([h_right[0] - 6, h_right[1] - 6,
               h_right[0] + 6, h_right[1] + 6], fill=(0, 0, 0))
    # Vertical down on the right.
    v_top = (X(230), Y(72))
    v_bot = (X(228), Y(250))
    _tapered_line(D, v_top, v_bot,
                  w0=int(11 * scale), w1=int(10 * scale), steps=32)
    # Corner blob at bottom-right.
    D.ellipse([v_bot[0] - 6, v_bot[1] - 6,
               v_bot[0] + 6, v_bot[1] + 6], fill=(0, 0, 0))
    # Hook up-and-left.
    hook_start = (v_bot[0] + 1, v_bot[1] + 2)
    hook_end = (v_bot[0] - 26 * scale, v_bot[1] - 20 * scale)
    _tapered_line(D, hook_start, hook_end,
                  w0=int(10 * scale), w1=max(1, int(2 * scale)), steps=16)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_men(D, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_门.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
