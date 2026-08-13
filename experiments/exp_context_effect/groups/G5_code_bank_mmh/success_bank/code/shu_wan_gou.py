"""Bank primitive: 竖弯钩 (shu-wan-gou — vertical, bend right, hook up).

Extracted from p2_radical_011_匕 stroke 2 (PASS 2026-08-08).
Same class also appears in 儿 stroke 2 (C-verdict — placement issue in
儿, not stroke-shape). Bare form: descends vertically from head, curves
right along a bottom shoulder, then hooks up-right into tail.
"""

from PIL import ImageDraw


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def draw_shu_wan_gou(draw: ImageDraw.ImageDraw, head, tail,
                     width=7, bottom_extra=60, knee_ratio=0.75):
    """Draw 竖弯钩 from head (top) to tail (upper-right after hook).

    head, tail    : (x, y) pixel tuples
    width         : ink width
    bottom_extra  : how far below tail.y the bottom of the curve extends
                    before hooking up (px)
    knee_ratio    : x-position of the horizontal shoulder as a fraction
                    from head.x to tail.x
    """
    hx, hy = head
    tx, ty = tail

    bottom_y = ty + bottom_extra
    c1 = (hx, bottom_y - 40)
    c2 = (hx + (tx - hx) * knee_ratio * 0.7, bottom_y + 15)
    knee = (hx + (tx - hx) * knee_ratio, bottom_y)

    body = _bezier3(head, c1, c2, knee, n=60)
    hook_ctrl = (tx + 5, ty + 45)
    hook = _bezier2(knee, hook_ctrl, tail, n=20)
    pts = body + hook[1:]

    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')
