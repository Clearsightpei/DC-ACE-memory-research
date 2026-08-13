"""Bank primitive: 丶 (dian — dot stroke, calligraphic tapered form).

Promoted from p2_radical_008_丶 (G5 bootstrap PASS, 2026-08-08).

Draws a tapered curved dot: thin at head, thickening toward tail with a
small perpendicular bow. Suitable for the 4th stroke in 之, top dot in 主/宝,
right dot of 冫 etc. Direction is fully parametric via endpoints.
"""

from PIL import ImageDraw


def draw_dian(draw: ImageDraw.ImageDraw, head, tail,
              w_head=3, w_tail=8, bow=5, steps=48):
    """Draw a tapered 点 from head (thin) to tail (thick).

    head, tail : (x, y) pixel tuples
    w_head     : ink radius at head
    w_tail     : ink radius at tail
    bow        : perpendicular bow magnitude (px). Positive bows to the
                 right of the head->tail direction (image y-down convention).
    steps      : sampling density along the arc
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2

    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length  # perpendicular (right of travel)
    cx, cy = mx + px * bow, my + py * bow

    prev = None
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * hx + 2 * u * t * cx + t * t * tx
        y = u * u * hy + 2 * u * t * cy + t * t * ty
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
        if prev is not None:
            draw.line((prev[0], prev[1], x, y), fill='black',
                      width=int(round(r * 2)))
        prev = (x, y)
