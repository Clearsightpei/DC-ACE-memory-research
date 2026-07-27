# yao.py — 爻 (yáo), 4 strokes: two stacked 乂.
# PASSed at p2_radical_128_爻 (B3 pos 155, 2026-07-22).
# Inline PIL recipe. Reuses the _tb helper from wen.py-style local defn.
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


def draw_yao(t, ox=0, oy=0, scale=1.0):
    """Draw 爻. Stacked 乂 pair; base coords PIL px on 300x300."""
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy
    # TOP 乂
    _tb(t, X(178), Y(55), X(90), Y(155), ctrl_perp=-8, w_head=8, w_tail=1, n=60)
    _tb(t, X(122), Y(60), X(218), Y(158), ctrl_perp=8, w_head=2, w_tail=2,
        belly_pos=0.72, w_belly=8, n=60)
    # BOTTOM 乂
    _tb(t, X(182), Y(155), X(80), Y(260), ctrl_perp=-8, w_head=7, w_tail=1, n=60)
    _tb(t, X(118), Y(160), X(228), Y(262), ctrl_perp=8, w_head=2, w_tail=2,
        belly_pos=0.72, w_belly=9, n=60)
