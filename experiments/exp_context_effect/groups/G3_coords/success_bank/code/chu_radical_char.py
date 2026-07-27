# chu_radical_char.py — 屮 (chè), 3 strokes.
# PASSed at p3_char_0084_屮 (B5, pos 251).
# Recipe: inline PIL rendering — central vertical shaft + two mirrored
# 竖折 side arms turning into a horizontal crossbar at y ~= -25 (math).
# Thin uniform ~5px per P12.

from PIL import Image  # noqa: F401 (import kept for parity with source)


def draw_chu_radical_char(t, ox=0, oy=0, scale=1.0):
    """屮 (chu radical/char). Inline PIL-pixel recipe adapted from
    p3_char_0084_屮. ox/oy/scale threaded via math-coord conversion."""
    ink = (0, 0, 0)
    lw = max(1, int(round(5 * scale)))

    def P(mx, my):
        return (150 + ox + mx * scale, 150 - oy - my * scale)

    # Center vertical shaft.
    t.line([P(0, 90), P(0, -125)], fill=ink, width=lw)

    # Left 竖折: high-left, down, right to shaft.
    t.line([P(-50, 20), P(-50, -25)], fill=ink, width=lw)
    t.line([P(-50, -25), P(0, -25)], fill=ink, width=lw)

    # Right 竖折: high-right, down, left to shaft.
    t.line([P(50, 40), P(50, -25)], fill=ink, width=lw)
    t.line([P(50, -25), P(0, -25)], fill=ink, width=lw)
