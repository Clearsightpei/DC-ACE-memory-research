"""Bank primitive: 一 (heng — horizontal stroke).

Promoted from p2_radical_005_一 (G5 bootstrap PASS, 2026-08-08).

Simple thick horizontal with rounded end caps and a small 顿笔 dab at
the tail. Signature is endpoint-based so callers can drop it wherever
MMH gives the anchor pair.
"""

from PIL import ImageDraw


def draw_heng(draw: ImageDraw.ImageDraw, head, tail,
              width_head=9, width_tail=10):
    """Draw a horizontal (横) stroke from head to tail.

    head, tail  : (x, y) pixel tuples
    width_head  : nominal body width at the head
    width_tail  : nominal body width at the tail (slightly heavier for 顿笔)
    """
    hx, hy = head
    tx, ty = tail

    draw.line([head, tail], fill='black', width=width_head)

    # end-cap dabs for calligraphic feel
    r = width_head / 2
    draw.ellipse([hx - r + 1, hy - r, hx + r - 1, hy + r], fill='black')
    r2 = width_tail / 2 + 1
    draw.ellipse([tx - r2, ty - r2, tx + r2, ty + r2], fill='black')
