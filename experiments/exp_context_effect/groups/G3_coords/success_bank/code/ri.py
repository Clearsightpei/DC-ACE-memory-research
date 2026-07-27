# ri.py — 日 (rì, sun), 4 strokes.
# Batch B2 (position 146) — human PASSed.
# Tall rectangle: kou.py doesn't fit (口 is 1:1, 日 is 1:2). Inline fresh.


def draw_ri(t, ox=0, oy=0, scale=1.0):
    """日 radical, 4 strokes (all straight tapered lines)."""
    x_left = 90 + ox
    x_right = 205 + ox
    y_top = 50 + oy
    y_bot = 250 + oy
    y_mid = 155 + oy
    w = max(1, int(round(11 * scale)))
    w_mid = max(1, int(round(9 * scale)))
    # Stroke 1: left 竖
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横 (with small right gap per GT)
    t.line([(x_left + 2, y_mid), (x_right - 5, y_mid)],
           fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)
