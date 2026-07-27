# pie_radical.py — 丿 (pie) radical, 1 stroke.
# Bootstrap batch (position 35) — human PASSed.
#
# Per P10: the pie stroke primitive is TOO diagonal for the 丿 radical.
# The PASSing render inlined a gentler scoop (nearly-vertical head, thicker
# head width, softer curl). Recorded verbatim from the passing attempt.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_pie_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """丿 radical: gentle scoop, near-vertical head, soft down-left curl.

    Bezier from head (+15,+85) via ctrl (+10,+5) to tail (-45,-100).
    Width 14 (head, held for first 15%) tapering to 1 (tail).
    """
    x0, y0 = 15.0 * scale, 85.0 * scale
    x1, y1 = -45.0 * scale, -100.0 * scale
    mx, my = 10.0 * scale, 5.0 * scale

    n_segments = 80
    w_head = max(1, 14.0 * scale)
    w_tail = 1.0

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if u < 0.15:
            w = w_head
        else:
            u2 = (u - 0.15) / 0.85
            w = w_head + (w_tail - w_head) * u2
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
