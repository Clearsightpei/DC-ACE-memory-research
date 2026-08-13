"""Bank primitive: 捺 (na — rightward-sweeping thickening stroke).

Extracted from p2_radical_009_八 (right stroke, PASS 2026-08-08).
Signature: endpoint-based, with tunable bow and head/tail widths.
"""

from PIL import ImageDraw


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_na(draw: ImageDraw.ImageDraw, head, tail,
            bow_perp=14, w_head=4, w_tail=11, steps=80):
    """Draw a 捺 (rightward sweep) from head (upper) to tail (lower-right).

    head, tail : (x, y) pixel tuples
    bow_perp   : perpendicular bow magnitude (px). Positive bows toward
                 the RIGHT of head->tail (image y-down); 捺 belly is
                 typically lower-left of the chord, so positive bow with
                 head-upper/tail-lower-right gives that.
    w_head     : ink radius at head (thinner)
    w_tail     : ink radius at tail (much thicker — 捺 thickens outward)
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2

    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp

    pts = _bezier(head, (cx, cy), tail, steps=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w_head + (w_tail - w_head) * t)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
