# BANK_DEVIATION
# skipped: kang_char.py, xiong_char.py (no bank entry for 侃-family composition)
# reason: 侃 = 亻 + 冂-frame with inner strokes + 儿; the middle inner block has
#         no analog in any current bank primitive, so hand-render right fresh.
# fresh_component: kan_right_frame_and_pillars (冂-frame + inner short strokes + 儿)
#
# Revision 2: strengthen 儿 left leg placement, make top-right arch cleaner
# (single 横折 with slight hook), and rebalance inner strokes.

import os
from PIL import Image, ImageDraw

_CANVAS = 300
_INK = (0, 0, 0)
_W = 5


def _line(t, x1, y1, x2, y2, w=_W):
    t.line([(x1, y1), (x2, y2)], fill=_INK, width=w)


def _bezier(t, x1, y1, cx, cy, x2, y2, w=_W, steps=26):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * x1 + 2 * (1 - u) * u * cx + u * u * x2
        by = (1 - u) ** 2 * y1 + 2 * (1 - u) * u * cy + u * u * y2
        pts.append((bx, by))
    for i in range(len(pts) - 1):
        t.line([pts[i], pts[i + 1]], fill=_INK, width=w)


def _pie(t, x1, y1, x2, y2, w=_W, bow=0.10):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    px, py = -dy / length, dx / length
    cx = mx + px * bow * length
    cy = my + py * bow * length
    _bezier(t, x1, y1, cx, cy, x2, y2, w=w)


def _shu_wan_gou(t, top_x, top_y, bot_y, right_x, w=_W):
    """竖弯钩: down then right, with tiny up-hook at end."""
    mid_y = top_y + (bot_y - top_y) * 0.55
    _line(t, top_x, top_y, top_x, mid_y, w=w)
    _bezier(t, top_x, mid_y, top_x, bot_y, right_x, bot_y, w=w)
    # hook up
    _line(t, right_x, bot_y, right_x - 2, bot_y - 14, w=w)


def draw_kan(t):
    # ============== LEFT: 亻 ==============
    _pie(t, 95, 65, 55, 175, bow=0.13)         # long 撇
    _line(t, 88, 100, 88, 265)                  # 竖

    # ============== RIGHT: 冂-frame + inner + 儿 ==============
    # Top-left short 撇 of the arch
    _pie(t, 155, 65, 128, 130, bow=0.05)
    # Top 横 (bar) — connect from around (155, 65) to (235, 72)
    _line(t, 152, 65, 238, 72)
    # 竖 down (right side of 冂)
    _line(t, 238, 72, 238, 165)

    # Inner: three short vertical strokes (川-like)
    _line(t, 158, 108, 152, 165)   # slight lean-left
    _line(t, 188, 108, 188, 165)   # middle
    _line(t, 218, 108, 218, 165)   # right

    # 儿 at bottom of right block
    _pie(t, 150, 170, 118, 275, bow=0.12)                   # left leg 撇
    _shu_wan_gou(t, 225, 170, bot_y=258, right_x=258)       # right leg 竖弯钩


if __name__ == "__main__":
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_kan(t)
    out_path = os.path.join(os.path.dirname(__file__), "01_侃.png")
    img.save(out_path)
    print(f"wrote {out_path}")
