"""Bank primitive: 撇 (pie — leftward-sweeping curve).

Extracted from p2_radical_009_八 (left stroke, PASS 2026-08-08).
Note: the bare 丿 radical (p2_radical_003) got a C verdict — its own
placement was off, but the underlying pie shape used in 八's left stroke
worked. That component is what's promoted here.

Signature: endpoint-based with tunable bow, taper, and head/tail widths.
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


def draw_pie(draw: ImageDraw.ImageDraw, head, tail,
             bow_perp=12, w_head=9, w_tail=3, steps=80):
    """Draw a 撇 (leftward sweep) from head (upper) to tail (lower-left).

    head, tail : (x, y) pixel tuples
    bow_perp   : perpendicular bow magnitude (px). Positive bows toward
                 the RIGHT of the head->tail direction (yielding a curve
                 that arches right — the usual pie shape).
    w_head     : ink radius at head (thicker)
    w_tail     : ink radius at tail (thinner — pie tapers to a fine point)
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2

    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular unit vector, "right of travel" in image y-down coords
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp

    pts = _bezier(head, (cx, cy), tail, steps=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w_head + (w_tail - w_head) * t)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
