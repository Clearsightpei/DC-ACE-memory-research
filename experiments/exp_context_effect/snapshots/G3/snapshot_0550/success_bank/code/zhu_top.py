# zhu_top.py — 龶, 4 strokes: 3 stacked hengs (bottom widest) + piercing 竖.
# PASSed at p3_char_0129_龶 (B5, pos 269). Inline thin (~4 px) recipe.


def draw_zhu_top(t, ox=0.0, oy=0.0, scale=1.0):
    """龶 — 3 stacked hengs + 1 piercing shu (main-master-style)."""
    ink = max(2, int(round(4.0 * scale)))

    def _to_pixel(mx, my, size=300):
        return size / 2 + mx, size / 2 - my

    def L(x1, y1, x2, y2):
        p1 = _to_pixel(ox + x1 * scale, oy + y1 * scale)
        p2 = _to_pixel(ox + x2 * scale, oy + y2 * scale)
        t.line([p1, p2], fill=(0, 0, 0), width=ink)

    L(-35, 55, 35, 55)
    L(-40, 25, 40, 25)
    L(-95, -20, 95, -20)
    L(0, 70, 0, -35)
