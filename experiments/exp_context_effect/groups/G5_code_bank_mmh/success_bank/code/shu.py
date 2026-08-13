"""Bank primitive: 丨 (shu — vertical stroke).

Promoted from p2_radical_001_丨 (G5 bootstrap PASS, 2026-08-08).

Signature: endpoint-based. Callers pass MMH anchors directly.
The GT for the bare 丨 radical has a soft leftward top-hook curl before
the descent; that decoration is optional and off by default so this
primitive can be reused as a plain vertical shaft in composed characters.
"""

from PIL import ImageDraw


def draw_shu(draw: ImageDraw.ImageDraw, head, tail, width=7, top_curl=False):
    """Draw a vertical stroke from head to tail.

    head, tail : (x, y) pixel tuples
    width      : nominal ink width (px)
    top_curl   : if True, prepend a short leftward top curl (matches
                 the bare-radical GT for 丨). Off by default so composed
                 characters get a clean shaft.
    """
    hx, hy = head
    tx, ty = tail

    if top_curl:
        # quadratic Bezier arc: up-and-left, curling back down to head
        p0 = (hx + 1, hy - 22)
        p1 = (hx - 6, hy - 10)
        p2 = (hx, hy)
        prev = p0
        steps = 24
        for i in range(1, steps + 1):
            u = i / steps
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
            draw.line([prev, (x, y)], fill='black', width=width)
            prev = (x, y)

    # Straight-ish body head -> tail (allows a slight lateral drift)
    n = 40
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0 = hx + (tx - hx) * t0
        y0 = hy + (ty - hy) * t0
        x1 = hx + (tx - hx) * t1
        y1 = hy + (ty - hy) * t1
        draw.line([(x0, y0), (x1, y1)], fill='black', width=width)
