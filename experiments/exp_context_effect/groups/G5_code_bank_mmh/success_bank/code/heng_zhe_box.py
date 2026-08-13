"""Bank primitive: 横折 (heng-zhe — BOXY variant with straight corner).

Extracted from p2_radical_057_口 s2 (PASS 2026-08-08, B1) via BANK_DEVIATION.
Distinct from the bootstrap-era heng_zhe_short.py (which was tuned to the
soft 乛 arc). This variant renders the boxy heng_zhe found in 口/日/月/目
etc. — a straight horizontal + right-angle corner + straight vertical drop.

Signature: (top_left, bottom_right, width) — the axis-aligned rectangle
defined by these two corners is the 横折's footprint.
"""

from PIL import ImageDraw


def draw_heng_zhe_box(draw: ImageDraw.ImageDraw, top_left, bottom_right, width=8):
    """A boxy 横折: horizontal from top_left to top-right corner, then
    vertical down to bottom_right. Small calligraphic rise on the top-right
    end and a 顿笔 knob at the corner.
    """
    x0, y0 = top_left
    x1, y1 = bottom_right
    # slight top rise so the right end sits higher than the left
    top_right_y = y0 - 4
    # horizontal segment
    draw.line([(x0, y0), (x1, top_right_y)], fill='black', width=width)
    # 顿笔 knob at the corner
    r = width / 2 + 1
    draw.ellipse([x1 - r, top_right_y - r, x1 + r, top_right_y + r], fill='black')
    # vertical segment
    draw.line([(x1, top_right_y), (x1, y1)], fill='black', width=width)
