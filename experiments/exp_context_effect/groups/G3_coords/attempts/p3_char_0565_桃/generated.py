# 桃 (táo, peach) — L-R composition: 木 (mu) + 兆 (zhao).
# 10 strokes total: 4 (木) + 6 (兆).
# Left: bank draw_mu, compressed for LR-left slot.
# Right: 兆 inlined fresh — no bank entry exists for 兆.
# Revision 1: enlarge 木 vertically; rework 兆 layout with clearer
# two-column structure (left 竖弯钩 with tail-right, right long 弯钩 to
# lower-right, upper ticks + right dot).

import os
import sys
import math
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


def _line(t, p0, p1, width):
    a = _to_pixel(*p0)
    b = _to_pixel(*p1)
    t.line([a, b], fill=(0, 0, 0), width=width)


def _pie(t, x0, y0, x1, y1, w_head=6.0, w_tail=2.0, bow_perp=-4.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 50
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
        prev = (px, py)


def _dot(t, x, y, size=8):
    px, py = _to_pixel(x, y)
    r = size / 2
    t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _bezier_stroke(t, p0, p1, p2, w=6, n=50):
    """Quadratic bezier polyline stroke."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _to_pixel(bx, by)
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w)
        prev = (px, py)


def draw_zhao(t, ox=0.0, oy=0.0, scale=1.0):
    """兆 (zhào), 6 strokes.
    Two-column structure. Coords are math (y up).
      Left column (x ~ -35 to +5):
        S1: short pie at top (going down-left)
        S2: small dot below the pie
        S3: 竖弯钩 — starts upper-mid, curves down-left, tail turns right
      Right column (x ~ +25 to +75):
        S4: short pie at top (going down-left)
        S5: long 弯 — sweeps from upper-mid down to lower-right
        S6: dot at bottom-right
    """
    s = scale
    # S1: top-left short pie
    _pie(t,
         x0=ox + (-5) * s, y0=oy + 75 * s,
         x1=ox + (-30) * s, y1=oy + 40 * s,
         w_head=7.0, w_tail=2.0, bow_perp=-2.5 * s)
    # S2: dot just right/below of S1's tail (小点)
    _dot(t, ox + (-8) * s, oy + 15 * s, size=10)
    # S3: left 竖弯钩 — bezier curve from (x~-20, y=+35) down to (x=-40, y=-70),
    # then a short hook segment turning right.
    p0 = (ox + (-15) * s, oy + 40 * s)
    p1 = (ox + (-35) * s, oy + (-30) * s)
    p2 = (ox + (-45) * s, oy + (-70) * s)
    _bezier_stroke(t, p0, p1, p2, w=6, n=60)
    # hook tail at bottom of S3: turn right
    _line(t,
          (ox + (-45) * s, oy + (-70) * s),
          (ox + (-25) * s, oy + (-65) * s),
          6)
    # S4: top-right short pie
    _pie(t,
         x0=ox + 60 * s, y0=oy + 75 * s,
         x1=ox + 35 * s, y1=oy + 40 * s,
         w_head=7.0, w_tail=2.0, bow_perp=-2.5 * s)
    # S5: right long curve — bezier from upper (near S4's tail) to lower-right
    q0 = (ox + 30 * s, oy + 35 * s)
    q1 = (ox + 45 * s, oy + (-20) * s)
    q2 = (ox + 60 * s, oy + (-75) * s)
    _bezier_stroke(t, q0, q1, q2, w=6, n=60)
    # S6: dot at bottom-right (小捺-dot end)
    _dot(t, ox + 78 * s, oy + (-70) * s, size=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Left: 木 via bank draw_mu — compressed narrow for LR-left slot,
    # but tall enough to fill the vertical space.
    draw_mu(t, ox=-85, oy=+15, scale=0.75)

    # Right: 兆 inline fresh.
    draw_zhao(t, ox=+30, oy=0, scale=1.0)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_桃.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
