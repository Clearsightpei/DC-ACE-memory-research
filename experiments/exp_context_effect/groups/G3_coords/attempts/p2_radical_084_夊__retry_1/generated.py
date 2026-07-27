# p2_radical_084_夊 (suī) — retry_1. 3 strokes.
# Prior attempt (retry_0) failed: overall too small, top zigzag not prominent,
# 撇 + 捺 didn't produce the wide crossing-V that dominates GT.
# Fix idea (from errata + fu.py X-crossing recipe): PIL pixel coords,
# 300x300 canvas, use fu.py's _tb tapered-bezier helper pattern.
# 夊 structure (GT read):
#   S1 — short 撇 at top (a small down-left tick from ~x=155,y=70 to ~x=125,y=95).
#   S2 — 横撇/横折撇: small horizontal at top-left, then a curved long 撇
#         sweeping DOWN-LEFT from upper-middle to lower-left corner.
#   S3 — long 捺: starts near the crossing region (mid), sweeps DOWN-RIGHT
#         with a strong belly and flared tail, extending far to lower right.
# 撇 and 捺 CROSS near mid-upper (not kiss-apex like 人). Composition is closer
# to 攵/夂 family — an "X" set with 撇 anchored inside the top zigzag.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    """Tapered quadratic bezier via perp/along control offsets.
    Coordinates are PIL pixels (y grows DOWN)."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_sui(draw, ox=0.0, oy=0.0, scale=1.0):
    """夊 radical (3 strokes), inlined in PIL pixel coords for 300x300."""

    # S1: short 撇 at top — a tiny down-left tick.
    # Head near top-center, tail slightly below-left.
    _tb(draw, 158, 70, 128, 100,
        ctrl_perp=-2, w_head=6, w_tail=2, n=30)

    # S2: 横撇/折 compound. Draw as ONE continuous polyline:
    #   (a) small horizontal from (~118, 95) rightward to (~168, 92)
    #   (b) then sweeping DOWN-LEFT as a big 撇 from (~168, 92) to (55, 245).
    # Segment (a) — small horizontal at top.
    _tb(draw, 115, 92, 168, 88,
        ctrl_perp=1, w_head=3, w_tail=7, n=25)
    # Segment (b) — big 撇, curves outward (belly to the right of the chord).
    _tb(draw, 168, 88, 55, 245,
        ctrl_perp=-14, w_head=8, w_tail=2, n=75)

    # S3: long 捺 — starts inside the top-zigzag area (around x=130,y=125,
    # welded to the pie shaft near its upper portion) and sweeps
    # DOWN-RIGHT with a strong belly and flared tail.
    _tb(draw, 130, 125, 270, 250,
        ctrl_perp=10, w_head=3, w_tail=3,
        belly_pos=0.75, w_belly=14, n=80)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_sui(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_夊.png")
    img.save(out)


if __name__ == "__main__":
    main()
