# p3_char_0272_伪 — L-R composition: 亻 (left) + 为 (right).
# G3 v8: reference-only bank; drawing fresh with PIL for control.
# Revision 1: 亻 was too tall/aggressive; 为 was too small.
# Rebalanced to L~0.3, R~0.7 with 亻 shorter and 为 filling right area.

import os
from PIL import Image, ImageDraw

SIZE = 300
INK = (0, 0, 0)
BG = (255, 255, 255)
LW = 5


def _line(draw, p0, p1, w=LW):
    draw.line([p0, p1], fill=INK, width=w)


def _bezier(draw, p0, p1, p2, w=LW, steps=48):
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        cur = (x, y)
        _line(draw, prev, cur, w=w)
        prev = cur


def draw_dan_ren(draw, ox, oy, h=140):
    """Draw 亻 (single-person radical). Anchor: pie start top-right."""
    # pie: gentle sweep down-left, not too extreme
    p_start = (ox + 8, oy)
    p_ctrl = (ox + 2, oy + h * 0.5)
    p_end = (ox - 22, oy + h * 0.98)
    _bezier(draw, p_start, p_ctrl, p_end, w=LW)
    # short vertical shu meeting mid-pie, ends slightly below pie
    shu_top = (ox + 2, oy + h * 0.42)
    shu_bot = (ox + 2, oy + h * 1.15)
    _line(draw, shu_top, shu_bot, w=LW)


def draw_wei_right(draw, ox, oy, w=170, h=200):
    """Draw 为 in bounding box starting at (ox, oy)."""
    # Stroke 1: top dot — short slant down-right
    _bezier(draw,
            (ox + w * 0.25, oy + 2),
            (ox + w * 0.32, oy + 12),
            (ox + w * 0.40, oy + 25),
            w=LW)
    # Stroke 2: big pie — sweeping down-left, dominant stroke
    _bezier(draw,
            (ox + w * 0.78, oy + 15),
            (ox + w * 0.50, oy + h * 0.55),
            (ox + w * 0.02, oy + h * 1.02),
            w=LW)
    # Stroke 3: 横折折钩 — top horizontal, turn down, small折, long curve+hook
    x0 = ox + w * 0.28   # start on the pie
    y0 = oy + h * 0.38
    x1 = ox + w * 0.92   # right end of top heng
    y1 = y0
    _line(draw, (x0, y0), (x1, y1), w=LW)
    # turn down
    x2 = x1 - 3
    y2 = y0 + h * 0.18
    _line(draw, (x1, y1), (x2, y2), w=LW)
    # small horizontal inward (折)
    x3 = x2 - w * 0.16
    y3 = y2
    _line(draw, (x2, y2), (x3, y3), w=LW)
    # long descending curve to bottom + hook up-left
    end_x = ox + w * 0.48
    end_y = oy + h * 1.05
    _bezier(draw,
            (x3, y3),
            (x3 + w * 0.20, y3 + h * 0.35),
            (end_x, end_y),
            w=LW)
    # hook (small tick up-left)
    _line(draw, (end_x, end_y), (end_x - 14, end_y - 12), w=LW)
    # Stroke 4: inner dot — inside the enclosure
    _bezier(draw,
            (ox + w * 0.52, oy + h * 0.60),
            (ox + w * 0.60, oy + h * 0.70),
            (ox + w * 0.68, oy + h * 0.80),
            w=LW)


def draw_wei_composite(img_path):
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)
    # Left radical 亻: narrower and shorter than v1
    draw_dan_ren(draw, ox=68, oy=75, h=155)
    # Right 为: larger, fills right ~2/3
    draw_wei_right(draw, ox=100, oy=55, w=180, h=200)
    img.save(img_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伪.png")
    draw_wei_composite(out)
    print(f"wrote {out}")
