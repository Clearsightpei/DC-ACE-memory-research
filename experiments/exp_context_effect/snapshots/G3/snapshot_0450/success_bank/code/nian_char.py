# nian_char.py — 卄 (nian), 3 strokes: two near-verticals + crossbar.
# PASSed at p3_char_0062_卄 (B4). Inline (bank gong_radical's 撇 too curved).
import os


def _P(bx, by, ox, oy, scale):
    return (150 + ox + bx * scale, 150 - oy - by * scale)


def draw_nian_char(t, ox=0, oy=0, scale=1.0):
    w = max(1, int(round(9 * scale)))
    t.line([_P(-38, +70, ox, oy, scale), _P(-50, -85, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
    t.line([_P(-80, +5, ox, oy, scale), _P(+72, +5, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
    t.line([_P(+42, +70, ox, oy, scale), _P(+52, -85, ox, oy, scale)],
           fill=(0, 0, 0), width=w)
