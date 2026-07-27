# fu.py — 父 (fù, father), 4 strokes.
# Batch B2 (position 127) — human PASSed.
# Inline-fresh crossing-X (short 撇 + short 点 top + big 撇 + big 捺).
# Documents inline-fresh solution for 大/人/入-family compositions.

def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_fu(t, ox=0.0, oy=0.0, scale=1.0):
    """父 radical, 4 strokes. PIL pixel coords."""
    _tb(t, 135, 82, 95, 135, ctrl_perp=-5, w_head=6, w_tail=1, n=35)
    _tb(t, 178, 88, 210, 122, ctrl_perp=3, w_head=2, w_tail=8, n=30)
    _tb(t, 180, 118, 55, 268, ctrl_perp=-8, w_head=9, w_tail=1, n=70)
    _tb(t, 120, 118, 248, 268, ctrl_perp=8, w_head=2, w_tail=3,
        belly_pos=0.72, w_belly=15, n=70)
