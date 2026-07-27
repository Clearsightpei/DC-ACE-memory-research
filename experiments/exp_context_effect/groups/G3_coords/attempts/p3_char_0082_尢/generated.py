# p3_char_0082_尢 — 尢 (wāng), 3 strokes: 横, 撇, 竖弯钩.
#
# Composition (per GT gt/phase3/尢.png):
#   1. 横 — short slightly-slanted top bar, upper-mid, ~110 px wide.
#   2. 撇 — long sweeping arm from a bit above the heng (near mid) down
#      to bottom-left corner. Bow slight (-8 perp), tapers thick->thin.
#   3. 竖弯钩 — right leg: short shaft down, curve right, tiny upward
#      hook (GT has very mild hook, uniform-thin line style).
#
# Revision 1 vs first render: reduced overall stroke width (GT is MMH-style
# thin uniform lines per catalog P12 candidate); shrunk the shu_wan_gou hook
# and increased its shaft length so proportions match. Inlined the
# shu_wan_gou so widths/hook size are tunable.

import math
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie, tapered_line, to_px  # noqa: E402

CANVAS = 300


def _draw_shu_wan_gou_thin(d, shaft_top, shaft_bot, tail_end_x,
                           hook_h=10, thickness=6):
    """Inline mild-hook 竖弯钩 in math coords.

    shaft descends from shaft_top -> shaft_bot;
    quarter-circle arc curving right (radius = (shaft_bot.x -> tail_start.x));
    tail_end horizontal to tail_end_x at shaft_bot.y - radius;
    small upward hook (hook_h px)."""
    # Shaft
    x_shaft = shaft_top[0]
    y_top = shaft_top[1]
    y_bot = shaft_bot[1]
    p0 = to_px(x_shaft, y_top)
    p1 = to_px(x_shaft, y_bot)
    d.line([p0, p1], fill=(0, 0, 0), width=thickness)

    # Arc: center at (x_shaft + r, y_bot), radius r; from 180° to 270°
    r = (tail_end_x - x_shaft) * 0.5
    if r < 8:
        r = 8
    arc_cx = x_shaft + r
    arc_cy = y_bot
    n_arc = 16
    prev = None
    for i in range(n_arc + 1):
        u = i / n_arc
        ang = math.pi + u * (math.pi / 2)
        px_m = arc_cx + r * math.cos(ang)
        py_m = arc_cy + r * math.sin(ang)
        curr = to_px(px_m, py_m)
        if prev is not None:
            d.line([prev, curr], fill=(0, 0, 0), width=thickness)
        prev = curr

    # Tail horizontal from (arc end = x_shaft+r, y_bot-r) to (tail_end_x, y_bot-r)
    tail_y = y_bot - r
    p_ts = to_px(x_shaft + r, tail_y)
    p_te = to_px(tail_end_x, tail_y)
    d.line([p_ts, p_te], fill=(0, 0, 0), width=thickness)

    # Small upward hook — from tail_end upward, tapered
    hook_base = (tail_end_x, tail_y)
    hook_tip = (tail_end_x - 2, tail_y + hook_h)
    n_seg = 6
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        m0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        m1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((thickness - 1) * (1 - (u0 + u1) / 2) + 1)))
        d.line([to_px(*m0), to_px(*m1)], fill=(0, 0, 0), width=w)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: 横 — spans upper-mid, slight downward slope right side.
    # GT: left end ~x=-55, right end ~x=+45, y just above center.
    tapered_line(d, (-55, 32), (45, 28), 6, 6, n=32)

    # Stroke 2: 撇 — starts a hair above heng near mid-left crossing (x≈-15, y≈+55),
    # sweeps down to (-95, -105). Slight bow.
    variant_pie(d, head=(-15, 55), tail=(-95, -105),
                bow_perp=-7.0, w_head=7.0, w_tail=1.5, n=56)

    # Stroke 3: 竖弯钩 right leg. Shaft top at right end of heng area (~+25, +25),
    # shaft descends to (+25, -45), curves right and ends near (+85, -75) with
    # a small upward hook.
    _draw_shu_wan_gou_thin(
        d,
        shaft_top=(25, 25),
        shaft_bot=(25, -50),
        tail_end_x=85,
        hook_h=12,
        thickness=6,
    )

    out = os.path.join(_HERE, "01_尢.png")
    img.save(out)
    return out


if __name__ == "__main__":
    print(render())
