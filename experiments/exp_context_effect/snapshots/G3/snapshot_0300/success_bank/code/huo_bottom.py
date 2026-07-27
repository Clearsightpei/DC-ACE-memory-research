# huo_bottom.py — 灬 (four-dots-bottom, fire radical variant), 4 dots.
# Batch B2 (position 119) — human PASSed.
# Fully inlined 4 dots at PIL pixel coords. Uses direct-place recipe.

def _dot(t, head, tail, ctrl, w_head, w_tail, n=30):
    x0, y0 = head
    x1, y1 = tail
    mx, my = ctrl
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head * (1 - u) + w_tail * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_huo_bottom(t, ox=0.0, oy=0.0, scale=1.0):
    """灬 four-dots-bottom (fire radical bottom form). PIL pixel coords.
    ox/oy/scale for API parity."""
    _dot(t, head=(108, 195), tail=(92, 225), ctrl=(104, 212),
         w_head=2.0, w_tail=6.5, n=30)
    _dot(t, head=(139, 200), tail=(146, 224), ctrl=(141, 213),
         w_head=2.0, w_tail=5.5, n=30)
    _dot(t, head=(170, 200), tail=(178, 224), ctrl=(173, 213),
         w_head=2.0, w_tail=5.5, n=30)
    _dot(t, head=(200, 192), tail=(228, 226), ctrl=(210, 214),
         w_head=2.0, w_tail=8.0, n=40)
