# p3_char_0320_伾 — 伾 = 亻 (left) + 丕 (right).
# 丕 is 5 strokes: top heng, pie down-left, short shu, right dot, long bottom heng.
# Composition: bank draw_ren_pang for the radical on the left; inline PIL
# recipe adapted from bu_char.py for 丕 on the right (adds a long bottom heng).
import math
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402


def _to_pixel(mx, my):
    return 150 + mx, 150 - my


def _heng(t, xc, yc, half_len, thickness=6):
    xL, yL = _to_pixel(xc - half_len, yc)
    xR, yR = _to_pixel(xc + half_len, yc)
    t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)


def _shu(t, xc, yc, half_len, thickness=6):
    xT, yT = _to_pixel(xc, yc + half_len)
    xB, yB = _to_pixel(xc, yc - half_len)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)


def _bezier_stroke(t, x0, y0, x1, y1, w_head, w_tail, bow_perp=-6.0, n=60):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_pi_right(t, ox=45.0, oy=0.0, scale=0.85):
    """丕 — 5 strokes: top heng, pie down-left, short shu, dot right, long bottom heng."""
    # 1. Top heng — medium length
    _heng(t, ox + 0, oy + 70 * scale, 45 * scale, thickness=6)
    # 2. Pie from just under top heng, sweeping down-left long
    _bezier_stroke(t,
                   ox + 5 * scale, oy + 62 * scale,
                   ox + (-55) * scale, oy + (-55) * scale,
                   w_head=7.0 * scale, w_tail=2.0,
                   bow_perp=-8.0 * scale)
    # 3. Short shu — vertical mid, from top heng center down
    _shu(t, ox + 5 * scale, oy + 20 * scale, 40 * scale, thickness=6)
    # 4. Dot on right (below top heng, upper right area)
    _bezier_stroke(t,
                   ox + 30 * scale, oy + 20 * scale,
                   ox + 52 * scale, oy + (-25) * scale,
                   w_head=3.0 * scale, w_tail=9.0 * scale,
                   bow_perp=-2.0 * scale, n=40)
    # 5. Long bottom heng — wide, near bottom
    _heng(t, ox + 0, oy + (-80) * scale, 72 * scale, thickness=7)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Left: 亻 (ren_pang), shifted left, larger
    draw_ren_pang(t, ox=-75, oy=10, scale=1.15)

    # Right: 丕
    draw_pi_right(t, ox=55, oy=-5, scale=1.05)

    out = os.path.join(_HERE, "01_伾.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
