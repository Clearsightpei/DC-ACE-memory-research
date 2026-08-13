"""Bank primitive: 斜钩 (xie-gou — long diagonal descent + terminal up-hook).

Extracted from p2_radical_079_弋 s2 and p2_radical_096_戈 s2
(both G5 B2 PASS 2026-08-08 via BANK_DEVIATION). Two independent PASSes
confirm the shape; promote per P-RET-003.

Signature: endpoint (head, tail) — matches stroke-primitive convention.
The stroke descends diagonally from head (upper-left/center) to tail
(lower-right) with a slight down-left belly (bow), then flicks up a
short hook. Idiomatic for 弋, 戈, 我, 成, 找, 戏, 战, ...
"""

from PIL import ImageDraw


def _bezier2(p0, p1, p2, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_xie_gou(draw: ImageDraw.ImageDraw, head, tail,
                 width=8, bow=10, hook_up=32, hook_back=6):
    """Draw 斜钩 from head to tail with a short up-hook at the terminal.

    head, tail : (x, y) pixel tuples (tail is the corner where hook begins)
    width      : ink width
    bow        : perpendicular belly-drop (lower-left of chord)
    hook_up    : how far the hook rises above tail
    hook_back  : how far the hook drifts left of tail
    """
    hx, hy = head
    tx, ty = tail
    mx = (hx + tx) / 2
    my = (hy + ty) / 2
    dx = tx - hx
    dy = ty - hy
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # perpendicular pointing "lower-left" (belly of xie-gou)
    px = -dy / L
    py = dx / L
    ctrl = (mx + px * bow, my + py * bow)
    body = _bezier2(head, ctrl, tail, n=60)

    hook_tip = (tx - hook_back, ty - hook_up)
    hook_ctrl = (tx + 4, ty - hook_up * 0.4)
    hook = _bezier2(tail, hook_ctrl, hook_tip, n=20)

    pts = body + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')
