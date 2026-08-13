"""Bank primitive: 平捺 (ping-na — flat, long, slightly-bowed na with tail flare).

Extracted from p2_radical_044_辶 s3 (PASS 2026-08-08, B1) via BANK_DEVIATION.
Signature: (head, tail) — a much flatter/longer variant of the diagonal na
in na.py. Used for 辶/廴/走 whose bottom sweep spans nearly the full width.
"""

from PIL import ImageDraw


def draw_ping_na(draw: ImageDraw.ImageDraw, head, tail, belly_drop=8):
    """Draw a 平捺 (flat, wide na) from head (upper-left) to tail (lower-right).

    Thin at head, thickens across the belly, peaks near 0.85 of length,
    then slight taper into a soft flare at the tail.
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2 + belly_drop

    steps = 100
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * hx + 2 * u * t * mx + t * t * tx
        y = u * u * hy + 2 * u * t * my + t * t * ty
        if t < 0.15:
            r = 3 + (5 - 3) * (t / 0.15)
        elif t < 0.85:
            r = 5 + (10 - 5) * ((t - 0.15) / 0.70)
        else:
            r = 10 - (10 - 6) * ((t - 0.85) / 0.15)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
