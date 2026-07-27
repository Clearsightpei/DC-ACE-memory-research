# qi_ji.py — 亓 (qi), 4 strokes: short top heng + wide middle heng + pie + shu.
# PASSed at p3_char_0101_亓 (B5, pos 260). Inline PIL thin (~5px) recipe.


def draw_qi_ji(t, ox=0, oy=0, scale=1.0):
    """亓 — 4 strokes rendered inline (thin ~5 px per P12)."""
    CANVAS = 300

    def _to_pixel(mx, my):
        return (CANVAS / 2 + mx, CANVAS / 2 - my)

    def _heng(cx, cy, half_len, width=4):
        x1, y1 = _to_pixel(cx - half_len, cy)
        x2, y2 = _to_pixel(cx + half_len, cy)
        t.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=width)

    def _shu(cx, y_top, y_bot, width=4):
        x1, y1 = _to_pixel(cx, y_top)
        x2, y2 = _to_pixel(cx, y_bot)
        t.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=width)

    def _pie(head_xy, tail_xy, bow_perp=15.0, w_head=5, w_tail=2):
        hx, hy = head_xy
        tx, ty = tail_xy
        mx = (hx + tx) / 2.0 - bow_perp
        my = (hy + ty) / 2.0 + 5.0
        n = 60
        prev = None
        for i in range(n + 1):
            u = i / n
            bx = (1 - u) ** 2 * hx + 2 * (1 - u) * u * mx + u ** 2 * tx
            by = (1 - u) ** 2 * hy + 2 * (1 - u) * u * my + u ** 2 * ty
            px, py = _to_pixel(bx, by)
            w = max(1, int(round(w_head + (w_tail - w_head) * u)))
            if prev is not None:
                t.line([prev, (px, py)], fill=(0, 0, 0), width=w)
            prev = (px, py)

    # Apply scale via multiplication of coords; ox/oy in math space.
    _heng(cx=ox + 5.0 * scale, cy=oy + 75.0 * scale,
          half_len=32.0 * scale, width=max(2, int(round(5 * scale))))
    _heng(cx=ox + 0.0, cy=oy + 25.0 * scale,
          half_len=95.0 * scale, width=max(2, int(round(5 * scale))))
    _pie(head_xy=(ox - 25.0 * scale, oy + 20.0 * scale),
         tail_xy=(ox - 80.0 * scale, oy - 100.0 * scale),
         bow_perp=18.0 * scale, w_head=6, w_tail=2)
    _shu(cx=ox + 45.0 * scale, y_top=oy + 20.0 * scale,
         y_bot=oy - 100.0 * scale, width=max(2, int(round(5 * scale))))
