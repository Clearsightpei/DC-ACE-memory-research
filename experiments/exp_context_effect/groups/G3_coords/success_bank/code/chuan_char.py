# chuan_char.py — 川 (chuan, char), 3 strokes.
# PASSed at p3_char_0088_川 (B5, pos 253) as identity alias of chuan radical
# with small scale bump 1.15 + oy=-5 nudge for character exam frame.
from chuan import draw_chuan


def draw_chuan_char(t, ox=0, oy=0, scale=1.0):
    """川 character — chuan radical at scale ~1.15, oy nudge -5."""
    draw_chuan(t, ox=ox, oy=oy - 5 * scale, scale=1.15 * scale)
