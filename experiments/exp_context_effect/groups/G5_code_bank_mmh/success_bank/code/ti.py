"""Bank primitive: 提 (ti — rising diagonal, thick head → tapered tail).

Extracted from p2_radical_068_扌 s3 (PASS 2026-08-08, B1).
Signature: endpoint (head, tail) — matches stroke-primitive convention.
The 提 sweeps from a heavier down-left head to a fine up-right tail with
a slight downward sag for calligraphic feel.
"""

from PIL import ImageDraw


def draw_ti(draw: ImageDraw.ImageDraw, head, tail,
            w_head=9, w_tail=2, steps=50):
    """Draw a 提 (rising diagonal) from head (lower-left) to tail (upper-right).

    head, tail : (x, y) pixel tuples
    w_head : ink width at head (thicker)
    w_tail : ink width at tail (fine)
    """
    hx, hy = head
    tx, ty = tail
    # slight downward-bow (concave-up) — gives the stroke a soft sag
    mx = (hx + tx) / 2
    my = (hy + ty) / 2 + 4

    for i in range(steps):
        t0, t1 = i / steps, (i + 1) / steps

        def bez(t, hx=hx, hy=hy, mx=mx, my=my, tx=tx, ty=ty):
            x = (1 - t) ** 2 * hx + 2 * (1 - t) * t * mx + t ** 2 * tx
            y = (1 - t) ** 2 * hy + 2 * (1 - t) * t * my + t ** 2 * ty
            return (x, y)

        w = w_head + (w_tail - w_head) * ((t0 + t1) / 2)
        draw.line([bez(t0), bez(t1)], fill='black',
                  width=max(1, int(round(w))))
    # heavy anchor cap at head
    r = w_head // 2
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')
