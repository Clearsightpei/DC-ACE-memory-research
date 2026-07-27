# zhong.py — 中 (zhōng), 4 strokes: kou + central 竖 protruding.
# PASSed at p3_char_0100_中 (B5, pos 259). Composition: bank kou at
# scale 0.55 (nudged up) + inline central shu at thickness 10.
from kou import draw_kou


def draw_zhong(t, ox=0, oy=0, scale=1.0):
    """中 — kou box + central shu protruding above and below."""
    CANVAS = 300

    def _to_pixel(mx, my):
        return CANVAS / 2 + mx, CANVAS / 2 - my

    draw_kou(t,
             ox=ox + 0 * scale,
             oy=oy + 5 * scale,
             scale=0.55 * scale)

    top_y = 55 * scale
    bot_y = -110 * scale
    thickness = max(1, int(round(10 * scale)))
    x_top, y_top = _to_pixel(ox + 0, oy + top_y)
    x_bot, y_bot = _to_pixel(ox + 0, oy + bot_y)
    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)
