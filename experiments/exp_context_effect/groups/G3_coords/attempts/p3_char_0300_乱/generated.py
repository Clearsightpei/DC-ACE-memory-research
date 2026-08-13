# p3_char_0300_乱 (luàn, "chaos") — 7 strokes.
# Decomposition: 舌 on left (丿 一 十 口 — 6 strokes stacked as
# stylized 千 top + 口 bottom) + 乚 (竖弯钩) on right.
# Reference: bank entry #199 乩 (占 left + 乚 right, L-R composition
# via shu_wan_gou at ox=+30, scale=1.05). Same skeleton, replace 占
# with a slightly taller 舌.
# GT is MMH-thin (width ~4). Use thin uniform strokes, not calligraphic.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300
CX = CANVAS // 2
CY = CANVAS // 2


def _p(ox, oy):
    """math-coord -> pixel."""
    return (CX + ox, CY - oy)


def draw_she_left(t, ox=0, oy=0, w=4):
    """舌 on the left half — taller variant to fill vertical band.

    Anchors (math-coords, origin at glyph center):
      pie:  from (18, 110) down-left to (-42, 70)
      top heng: from (-52, 82) to (32, 82)
      shu:  from (-8, 82) down to (-8, 5)
      mid heng: from (-52, 30) to (32, 30)
      kou box: TL (-42, 5) BR (28, -55)
    """
    fill = (0, 0, 0)

    # 撇 (pie) — top diagonal
    t.line([_p(ox + 18, oy + 110), _p(ox - 42, oy + 70)],
           fill=fill, width=w)
    # top 一 (heng) — crosses through the pie
    t.line([_p(ox - 52, oy + 82), _p(ox + 32, oy + 82)],
           fill=fill, width=w)
    # 竖 (vertical) — descends from top heng into the 口
    t.line([_p(ox - 8, oy + 82), _p(ox - 8, oy + 5)],
           fill=fill, width=w)
    # middle 一 (heng)
    t.line([_p(ox - 52, oy + 30), _p(ox + 32, oy + 30)],
           fill=fill, width=w)

    # 口 (kou box) — mouth at bottom
    kx0, ky0 = ox - 42, oy + 5    # top-left
    kx1, ky1 = ox + 28, oy - 55   # bottom-right
    # top
    t.line([_p(kx0, ky0), _p(kx1, ky0)], fill=fill, width=w)
    # left
    t.line([_p(kx0, ky0), _p(kx0, ky1)], fill=fill, width=w)
    # right
    t.line([_p(kx1, ky0), _p(kx1, ky1)], fill=fill, width=w)
    # bottom
    t.line([_p(kx0, ky1), _p(kx1, ky1)], fill=fill, width=w)


def draw_luan(t, ox=0.0, oy=0.0, scale=1.0):
    # Left: 舌 centered around (-58, -10) — shift up a bit
    draw_she_left(t, ox=-58, oy=-10, w=4)
    # Right: 乚 (竖弯钩) — tall, right side, inline thin
    _draw_thin_ya(t, ox=45, oy=15, height=170, w=4)


def _draw_thin_ya(t, ox, oy, height=140, w=4):
    """Thin 乚: vertical shaft descends, curves right, small upward hook.

    Anchored to (ox, oy) roughly at the middle of the shaft.
    """
    import math
    fill = (0, 0, 0)
    # Shaft top / bottom
    top_x, top_y = ox, oy + height * 0.55
    bot_x, bot_y = ox, oy - height * 0.35
    # Vertical shaft
    t.line([_p(top_x, top_y), _p(bot_x, bot_y)], fill=fill, width=w)
    # Arc bottom-right, radius r
    r = 32
    arc_cx = bot_x + r
    arc_cy = bot_y
    n = 14
    prev = None
    for i in range(n + 1):
        u = i / n
        angle = math.pi + u * (math.pi / 2)  # 180 -> 270 deg
        px = arc_cx + r * math.cos(angle)
        py = arc_cy + r * math.sin(angle)
        curr = _p(px, py)
        if prev is not None:
            t.line([prev, curr], fill=fill, width=w)
        prev = curr
    # Tail horizontal
    tail_x0 = arc_cx
    tail_y0 = bot_y - r
    tail_x1 = arc_cx + 32
    tail_y1 = tail_y0
    t.line([_p(tail_x0, tail_y0), _p(tail_x1, tail_y1)],
           fill=fill, width=w)
    # Upward hook
    hook_tip_x = tail_x1 - 3
    hook_tip_y = tail_y1 + 22
    t.line([_p(tail_x1, tail_y1), _p(hook_tip_x, hook_tip_y)],
           fill=fill, width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_luan(t)
    out = os.path.join(_HERE, "01_乱.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
