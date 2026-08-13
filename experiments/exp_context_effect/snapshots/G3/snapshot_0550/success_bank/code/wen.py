# wen.py — 文 (wén), 4 strokes: 点 + 横 + 撇 + 捺
# PASSed at p2_radical_124_文 (B3 pos 151, 2026-07-22).
# Inline PIL recipe (like fu.py 父) — small top dot, medium heng,
# crossing 撇 + 捺 opening from just below the heng.
from PIL import ImageDraw as _ImageDraw  # noqa: F401 (typing only)


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


def draw_wen(t, ox=0, oy=0, scale=1.0):
    """Draw 文. Base coords are PIL px on 300x300 canvas; ox/oy shift px,
    scale is uniform. Retained for compositional reuse."""
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy
    _tb(t, X(158), Y(55), X(138), Y(78), ctrl_perp=-2, w_head=3, w_tail=8, n=25)
    _tb(t, X(78), Y(112), X(226), Y(108), ctrl_perp=1.5, w_head=6, w_tail=8, n=45)
    _tb(t, X(180), Y(100), X(70), Y(260), ctrl_perp=-12, w_head=9, w_tail=1, n=70)
    _tb(t, X(120), Y(105), X(240), Y(258), ctrl_perp=10, w_head=2, w_tail=3,
        belly_pos=0.72, w_belly=14, n=70)
