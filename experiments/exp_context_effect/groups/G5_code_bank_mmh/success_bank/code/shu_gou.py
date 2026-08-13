"""Bank primitive: 竖钩 (shu-gou — vertical then leftward hook).

Extracted from p2_radical_016_刂 stroke 2 (PASS 2026-08-08).
Vertical descent with a sharp curve/hook to the left at the tail.
Used in 刂 right stroke, 亅, 小 middle stroke, 水 middle, etc.
"""

from PIL import ImageDraw


def draw_shu_gou(draw: ImageDraw.ImageDraw, head, tail,
                 width=6, hook_start_offset=40):
    """Draw 竖钩 from head (top) to tail (lower-left after hook).

    head, tail        : (x, y) pixel tuples
    width             : ink width
    hook_start_offset : how many px above tail.y the hook shoulder starts
    """
    hx, hy = head
    tx, ty = tail

    shoulder_x = hx - 2  # very slight lean
    shoulder_y = ty - hook_start_offset

    # straight vertical body
    draw.line([head, (shoulder_x, shoulder_y)], fill='black', width=width)

    # hook: quadratic-ease-in x toward tail, linear y
    steps = 12
    for i in range(steps):
        t0, t1 = i / steps, (i + 1) / steps

        def pt(t):
            x = shoulder_x + (tx - shoulder_x) * (t ** 2)
            y = shoulder_y + (ty - shoulder_y) * t
            return (x, y)

        draw.line([pt(t0), pt(t1)], fill='black', width=width)

    r = width // 2
    for (x, y) in (head, tail):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')
