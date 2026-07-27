# p3_char_0105_仂 — 仂 = 亻 (left) + 力 (right).
# 亻: reuse bank ren_pang (row 45) at reduced scale for side-radical fit.
# 力: heng_zhe_gou + pie composed fresh (力 not yet in bank).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402


CANVAS_SIZE = 300


def draw_li_component(draw, ox=0.0, oy=0.0, scale=1.0):
    """力 (li, "power"): heng_zhe_gou top + pie sweeping down-left crossing
    the vertical shaft. Two strokes."""
    # heng_zhe_gou: at scale 0.60, horizontal spans ~(-54, +48) to (+48, +48),
    # vertical drops from (+48,+48) to (+48, -42).
    hzg_scale = 0.60
    draw_heng_zhe_gou(draw, ox=ox + 0, oy=oy + 10, scale=hzg_scale)

    # 撇 for 力: head near upper-mid of the top-horizontal (~ ox+5, oy+45),
    # tail sweeps down-left past the frame (~ ox-45, oy-70).
    # pie head at (+65s, +90s), tail (-45s, -85s). Choose scale 0.65.
    pie_scale = 0.65
    # head: ox_off + 65*0.65 = ox+5   → ox_off = ox + 5 - 42.25 = ox - 37.25
    #        oy_off + 90*0.65 = oy+45 → oy_off = oy + 45 - 58.5 = oy - 13.5
    draw_pie(draw, ox=ox - 37.0, oy=oy - 13.0, scale=pie_scale)


def draw_le(draw):
    """仂 top-level: 亻 on the left, 力 on the right."""
    # 亻 side radical, compressed for left third of canvas.
    # scale 0.65 keeps ren_pang's pie modest; shift left so shu sits near x=-45.
    draw_ren_pang(draw, ox=-55.0, oy=-10.0, scale=0.65)
    # 力 on the right, centered around x=+30, filling right two-thirds.
    draw_li_component(draw, ox=+35.0, oy=-5.0, scale=1.0)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_le(draw)
    out = os.path.join(_HERE, "01_仂.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
