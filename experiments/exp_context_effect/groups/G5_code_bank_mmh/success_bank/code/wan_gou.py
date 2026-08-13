"""Bank primitive: 弯钩 (wan-gou, curved vertical hook).

Promoted from p3_char_0009_了 (G5 B3 A verdict 2026-08-08 — FIRST A verdict).
The stroke bows RIGHT as it descends, then terminates with a small
LEFT-flick hook at the bottom. Different from shu_wan_gou (which curves
right at the bottom into an upward hook) and different from shu_gou
(nearly straight vertical + upward hook).

High-reuse: appears in 了/子/字/学/宁/寧-family (~5% of common Phase-3
characters have this stroke).

Endpoint signature. head = top of curved shaft; tail = bottom-left
after hook flick. bow_right controls how far the belly bulges right.
"""

from PIL import ImageDraw


def _bezier3(p0, p1, p2, p3, steps=80):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _bezier2(p0, p1, p2, steps=20):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def draw_wan_gou(draw: ImageDraw.ImageDraw, head, tail,
                 belly_right=27, hook_len=26, hook_up=13,
                 w_head=5, w_body=5.5, w_tail=2):
    """Curved-right vertical shaft ending with small left-flick hook.

    head:  top of curved shaft (x, y)
    tail:  bottom-left of shaft, BEFORE the hook flick
    belly_right: how far the belly bulges right of head->tail chord
    hook_len:  horizontal length of the terminal left-flick
    hook_up:   vertical rise of the terminal left-flick
    """
    hx, hy = head
    tx, ty = tail
    mid_y = (hy + ty) * 0.5
    belly = (max(hx, tx) + belly_right, mid_y)
    lower = ((hx + tx) * 0.5 + belly_right * 0.3, ty - abs(ty - hy) * 0.15)

    body = _bezier3(head, belly, lower, tail, steps=80)
    _stamp(draw, body, w_head, w_body)

    # Terminal hook flick: from tail, curl left and slightly up
    hook_p1 = (tx - hook_len * 0.5, ty + 1)
    hook_end = (tx - hook_len, ty - hook_up)
    hook = _bezier2(tail, hook_p1, hook_end, steps=20)
    _stamp(draw, hook, w_body, w_tail)
