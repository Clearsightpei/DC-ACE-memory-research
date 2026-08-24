# BANK_DEVIATION
# skipped: mu.py (for the 禾 left radical)
# reason: 禾 = 木 + top slant AND left-radical form replaces na with dian;
#         mu.py bakes-in an outward na sweep that would collide with 中 on
#         the right; inline a fresh compressed 禾-radical instead.
# fresh_component: he_radical_left_for_种
#
# 种 = 禾 (left, compressed, na→dian) + 中 (right, bank zhong.py)

import os
import sys
import math
from PIL import Image, ImageDraw

_BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from zhong import draw_zhong  # noqa: E402

CANVAS = 300


def _to_pixel(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def _line(t, x0, y0, x1, y1, w):
    p0 = _to_pixel(x0, y0)
    p1 = _to_pixel(x1, y1)
    t.line([p0, p1], fill=(0, 0, 0), width=w)


def _tapered_curve(t, x0, y0, x1, y1, w_head=8.0, w_tail=1.5, bow_perp=0.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
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


def _dian(t, x, y, sz=9, angle_deg=135):
    a = math.radians(angle_deg)
    dx = math.cos(a) * sz
    dy = math.sin(a) * sz
    # Draw as a small tapered stroke (dot with slight teardrop)
    n = 20
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x + dx * u
        by = y - dy * u
        px, py = _to_pixel(bx, by)
        w = 3 + 6 * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_he_radical(t, ox=-70, oy=0, scale=1.0):
    """禾 as left radical: top pie + heng + shu + long left pie + dian.
    Compressed for left-half slot."""
    s = scale
    # Top short pie/slant (from upper-right down to upper-left)
    _tapered_curve(t,
                   x0=ox + 18 * s, y0=oy + 85 * s,
                   x1=ox + (-20) * s, y1=oy + 55 * s,
                   w_head=6.0 * s, w_tail=2.0 * s, bow_perp=3.0 * s)
    # Heng — spans left radical width (slightly shorter to leave room for 中)
    _line(t,
          ox + (-55) * s, oy + 40 * s,
          ox + 40 * s, oy + 40 * s,
          w=max(1, int(round(6 * s))))
    # Central shu (long vertical)
    _line(t,
          ox + 0, oy + 40 * s,
          ox + 0, oy + (-95) * s,
          w=max(1, int(round(7 * s))))
    # Left pie — sweeps from the shu-heng cross down-left
    _tapered_curve(t,
                   x0=ox + 0, y0=oy + 40 * s,
                   x1=ox + (-55) * s, y1=oy + (-50) * s,
                   w_head=7.0 * s, w_tail=1.5 * s, bow_perp=-5.0 * s)
    # Dian (right-side dot, replaces na in left-radical form)
    _dian(t, x=ox + 10 * s, y=oy + 25 * s, sz=42 * s, angle_deg=-55)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Left half: 禾 radical
    draw_he_radical(t, ox=-70, oy=-5, scale=0.95)

    # Right half: 中 via bank primitive (bigger to match 禾 vertical extent)
    draw_zhong(t, ox=70, oy=-10, scale=1.0)

    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0437_种/01_种.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
