# p3_char_0094_不 — 不 (bù), 4 strokes: 横 + 丿 + 丨 + 丶.
# GT observation: wide long heng at top; from just below the heng's
# center, a shu descends short; a pie sweeps from that junction down
# to the lower-left; a small dian sits mid-right of the shu.
#
# Bank consulted: xia_char (heng+shu+dian composition), mu (inline
# thin-line pie/na for the 大-family crossing). 不 differs from 木 in
# that pie and dian START at/near the heng midpoint (not cross through)
# and the right stroke is a short dian not a na.
#
# Approach: inline PIL rendering with matched thin (~7px) weight
# following mu.py's per-stroke helpers, adapted for 不's geometry.

import math
import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _inline_heng(t, xc, yc, half_len, thickness):
    xL, yL = _to_pixel(xc - half_len, yc)
    xR, yR = _to_pixel(xc + half_len, yc)
    t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)


def _inline_shu(t, xc, yc, half_len, thickness):
    xT, yT = _to_pixel(xc, yc + half_len)
    xB, yB = _to_pixel(xc, yc - half_len)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)


def _inline_pie(t, x0, y0, x1, y1, w_head=7.0, w_tail=1.0, bow_perp=-6.0):
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


def _inline_dian(t, x0, y0, x1, y1, w_head=3.0, w_tail=8.0):
    """Small right-falling dot: thin head → fat tail, gentle curve."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    bow_perp = -2.0
    mx = (x0 + x1) / 2.0 + perp_x * bow_perp
    my = (y0 + y1) / 2.0 + perp_y * bow_perp
    n = 40
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


def draw_bu2(t, ox=0.0, oy=0.0, scale=1.0):
    """不 character, 4 strokes. Revision 2: heng higher, strokes longer/lower."""
    # Stroke 1: 横 — long heng near top, y ~ +75
    _inline_heng(t, ox + 0, oy + 75 * scale, 105 * scale, thickness=6)

    # Stroke 2: 丿 — pie from just under heng center, sweeps down-left
    #   Longer and reaches lower-left corner area
    _inline_pie(t, x0=ox + 10 * scale, y0=oy + 65 * scale,
                x1=ox + (-90) * scale, y1=oy + (-110) * scale,
                w_head=7.0 * scale, w_tail=2.0, bow_perp=-7.0 * scale)

    # Stroke 3: 丨 — shu from heng center down further
    _inline_shu(t, ox + 8 * scale, oy + (-45) * scale, 75 * scale, thickness=6)

    # Stroke 4: 丶 — dian on the right, longer and lower
    _inline_dian(t, x0=ox + 40 * scale, y0=oy + (-5) * scale,
                 x1=ox + 85 * scale, y1=oy + (-70) * scale,
                 w_head=3.0 * scale, w_tail=8.0 * scale)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_bu2(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_不.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
