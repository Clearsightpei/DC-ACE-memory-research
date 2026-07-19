# p2_radical_104_木 (mù, "tree") — 4-stroke radical.
# Strokes: 横 (top horizontal), 竖 (vertical through heng center down to bottom),
# 撇 (down-left from crossing), 捺 (down-right from crossing).
#
# TR8 note: heng+shu match bank primitives well and share crossing at
# canvas center (like 十). pie and na however must START at the
# heng-shu crossing (~(0, +25) math coords) and sweep out — the pie/na
# primitives are tuned for a standalone head at (+65,+90)/(-70,+80),
# so force-fitting via ox/oy would land the tail in the wrong place.
# INLINE both pie and na as fresh tapered beziers whose HEADS are at
# the crossing point.
#
# Layout (math coords, center origin, +y up, 300x300):
#   Heng: y = +25, half_len = 100 (spans -100..+100)
#   Shu:  x = 0, from top-hook y=+50 down to y=-115 (small stub above heng)
#   Pie head at (0, +25), tail at (-95, -110)
#   Na  head at (0, +25), tail at (+95, -110)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _inline_pie(t, x0, y0, x1, y1, w_head=9.0, w_tail=1.0, bow_perp=-8.0):
    """Inline 撇: tapered bezier from (x0,y0) head to (x1,y1) tail.
    bow_perp bows the curve perpendicular to chord (negative = left bow)."""
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    # perpendicular direction to chord
    dx, dy = x1 - x0, y1 - y0
    import math
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


def _inline_na(t, x0, y0, x1, y1, w_head=2.0, w_belly=15.0, w_tail=3.0, bow_perp=8.0):
    """Inline 捺: tapered bezier head->belly->tail.  Head thin, belly thick."""
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    import math
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    prev = None
    u_belly = 0.7
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        if u <= u_belly:
            w = w_head + (w_belly - w_head) * (u / u_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - u_belly) / (1 - u_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _inline_heng(t, x_center, y_center, half_len, thickness):
    """Inline heng with configurable thickness (bank heng locks 12px)."""
    x_left, y_left = _to_pixel(x_center - half_len, y_center)
    x_right, y_right = _to_pixel(x_center + half_len, y_center)
    t.line([(x_left, y_left), (x_right, y_right)],
           fill=(0, 0, 0), width=thickness)


def _inline_shu(t, x_center, y_center, half_len, thickness):
    """Inline shu with configurable thickness (bank shu locks 12px)."""
    x_top, y_top = _to_pixel(x_center, y_center + half_len)
    x_bot, y_bot = _to_pixel(x_center, y_center - half_len)
    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)


def draw_mu(t, ox=0.0, oy=0.0, scale=1.0):
    """木: heng crossing shu at (0, +25 math); pie + na sweep out from that point.

    Revised (v2): GT shows thin, delicate strokes — bank heng/shu at 12px
    read as HEAVY versus GT. Inline both at ~7px to match GT stroke
    weight. Also slim the na belly (GT na is graceful, not fat).
    Bank primitives skipped for weight-mismatch reason (TR8: primitive
    was tuned for standalone 12-px feel; here we need matched-weight
    lightness).

    Layout (math coords):
      Heng: y = +25, half_len 95, thickness 7
      Shu:  x = 0, from y=+50 (small stub above heng) to y=-115, thick 7
      Pie:  head (0,+25) -> tail (-95,-110), w_head=7 -> tail 1
      Na:   head (0,+25) -> tail (+95,-110), w_head=2 -> belly 11 -> tail 2
    """
    # Heng (stroke 1) — inline for thickness control
    _inline_heng(t, ox + 0, oy + 25 * scale, 95 * scale, thickness=7)
    # Shu (stroke 2) — inline for thickness control
    _inline_shu(t, ox + 0, oy + (-32.5) * scale, 82.5 * scale, thickness=7)
    # Pie (stroke 3) — inline, head at crossing
    _inline_pie(
        t,
        x0=ox + 0, y0=oy + 25 * scale,
        x1=ox + (-95) * scale, y1=oy + (-110) * scale,
        w_head=7.0 * scale, w_tail=1.0,
        bow_perp=-6.0 * scale,
    )
    # Na (stroke 4) — inline, head at crossing, slimmer belly
    _inline_na(
        t,
        x0=ox + 0, y0=oy + 25 * scale,
        x1=ox + 95 * scale, y1=oy + (-110) * scale,
        w_head=2.0 * scale, w_belly=11.0 * scale, w_tail=2.0 * scale,
        bow_perp=6.0 * scale,
    )


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_mu(t)
    out = os.path.join(os.path.dirname(__file__), "01_木.png")
    img.save(out)
    print(f"saved {out}")
