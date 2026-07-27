# dian_radical.py — 丶 (dian) radical, 1 stroke.
# Bootstrap batch (position 40) — human PASSed.
#
# Per TR5: standalone dian primitive was too stubby/heavy for the 丶
# radical form. The PASSing render inlined a longer, slimmer, curved
# diagonal (head width 2, tail width 9). Recorded verbatim.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_dian_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """丶 radical: longer, slimmer, curved diagonal (upper-left to lower-right).

    Bezier head (-22,+32) → tail (+25,-28), with ctrl pulled slightly
    down-left for a gentle bow. Width 2 (head) → 9 (tail).
    """
    x0, y0 = -22.0 * scale, 32.0 * scale
    x1, y1 = 25.0 * scale, -28.0 * scale
    mx = (x0 + x1) / 2.0 - 5.0 * scale
    my = (y0 + y1) / 2.0 - 5.0 * scale

    n_segments = 50
    thickness_head = 2.0
    thickness_tail = 9.0

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if prev_pt is not None:
            w = thickness_head * (1 - u) + thickness_tail * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
