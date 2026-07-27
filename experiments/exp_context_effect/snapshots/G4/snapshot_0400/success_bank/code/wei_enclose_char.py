"""囗 (wéi, enclosure as Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of wei_enclose.py (Phase-2 radical).
TR9 span already baked into the underlying primitive; MMH anchors for
the char match the radical's default full-grid span, so we call the
mastered primitive with its defaults (per TR1 the wrapper name itself
functions as the override signal for the CHAR context).

Strokes: 竖 + 横折 + 横. Joints: 3 × N (corner gaps ~7-12 px).
"""
from wei_enclose import draw_wei_enclose


def draw_wei_enclose_char(draw):
    draw_wei_enclose(draw)
