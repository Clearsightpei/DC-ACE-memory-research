# yue_speak.py — 曰 (yuē, "to say"), 4 strokes.
# PASSed at p2_radical_129_曰 (B3 pos 156, 2026-07-22).
# Squat rectangle (width>height ~1.15:1) + middle heng. Inline recipe.
def draw_yue_speak(t, ox=0, oy=0, scale=1.0):
    x_left = 80 + ox
    x_right = 220 + ox
    y_top = 90 + oy
    y_bot = 210 + oy
    y_mid = 150 + oy
    w = max(1, int(round(11 * scale)))
    w_mid = max(1, int(round(9 * scale)))
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    t.line([(x_left + 2, y_mid), (x_right - 5, y_mid)], fill=(0, 0, 0), width=w_mid)
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)
