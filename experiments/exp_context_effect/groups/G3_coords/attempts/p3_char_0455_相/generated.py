# 相 (xiāng) — L-R composition: 木 (mu, tree) + 目 (mu, eye).
# 9 strokes total: 4 (木) + 5 (目).
# Uses bank mu.py transformed (ox=-70, scale=0.55) for the left.
# Right 目 is inlined fresh — bank ri.py has only 1 inner heng, but 目
# needs 2 inner hengs (3-row interior). No BANK_DEVIATION block since
# ri.py doesn't cover 目; only ri (日) is banked and it is a different
# character. mu.py is called cleanly.

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from mu import draw_mu  # noqa: E402


CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_mu_eye(t, ox=0.0, oy=0.0, scale=1.0):
    """目 (mù, eye), 5 strokes: shu + heng-zhe + 2 inner heng + bottom heng.
    Tall rectangle with interior split into 3 rows."""
    x_left = ox + (-45) * scale
    x_right = ox + (45) * scale
    y_top = oy + 100 * scale
    y_bot = oy + (-100) * scale
    y_mid_up = oy + 33 * scale
    y_mid_lo = oy + (-33) * scale
    w = max(1, int(round(7 * scale)))
    w_inner = max(1, int(round(6 * scale)))

    # Stroke 1: left 竖
    a = _to_pixel(x_left, y_top)
    b = _to_pixel(x_left, y_bot)
    t.line([a, b], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right shu)
    c = _to_pixel(x_left, y_top)
    d = _to_pixel(x_right, y_top)
    t.line([c, d], fill=(0, 0, 0), width=w)
    e = _to_pixel(x_right, y_top)
    f = _to_pixel(x_right, y_bot)
    t.line([e, f], fill=(0, 0, 0), width=w)
    # Stroke 3: upper inner 横 (small right gap)
    g = _to_pixel(x_left + 2, y_mid_up)
    h = _to_pixel(x_right - 4, y_mid_up)
    t.line([g, h], fill=(0, 0, 0), width=w_inner)
    # Stroke 4: lower inner 横 (small right gap)
    i = _to_pixel(x_left + 2, y_mid_lo)
    j = _to_pixel(x_right - 4, y_mid_lo)
    t.line([i, j], fill=(0, 0, 0), width=w_inner)
    # Stroke 5: bottom 横
    k = _to_pixel(x_left, y_bot)
    l = _to_pixel(x_right, y_bot)
    t.line([k, l], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Left: 木 (bank mu.py) — scaled to ~0.75, pushed left and up.
    # heng lands ~pixel y 100 to match GT (GT has 木 heng in upper third).
    draw_mu(t, ox=-80, oy=+25, scale=0.75)

    # Right: 目 (inline fresh) — pushed right, slightly narrower for L-R balance
    draw_mu_eye(t, ox=65, oy=0, scale=0.95)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_相.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
