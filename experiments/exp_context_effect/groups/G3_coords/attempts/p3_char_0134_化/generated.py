# p3_char_0134_化 (huà) — 4 strokes: 亻 (left, 撇+竖) + 匕 (right, 撇+竖弯钩)
#
# Composition strategy (revision 2):
# - Left 亻: use bank ren_pang at (-35, 0, 0.85). Bank ren_pang draws
#   pie head at ~(-23+65*0.8, +20+90*0.8) = (+29, +92) offset from ox/oy,
#   pie tail at (-23-45*0.8, +20-85*0.8) = (-59, -48). Shu at
#   (+20, -40) to (+20, -95) approx.
# - Right 匕: inline. shu_wan_gou at scale 0.70, positioned so shaft
#   starts high (top around y=+40) and hook rises. 撇 short, ends
#   ON shaft top per sandbox p2_radical_011_匕 fix.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code"
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie_short(t, head_math, tail_math, thickness=8):
    """Short 撇 as tapered bezier from head to tail (math coords)."""
    x0, y0 = head_math
    x1, y1 = tail_math
    # bow slightly left of chord
    mx = (x0 + x1) / 2.0 - 5.0
    my = (y0 + y1) / 2.0 + 3.0

    n_segments = 40
    w_head = max(2, thickness)
    w_tail = 1.5

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_hua(t, ox=0.0, oy=0.0, scale=1.0):
    """化: left 亻 + right 匕"""
    # --- Left 亻 (ren_pang) — position so radical is comfortably on left ---
    # ren_pang extends roughly x in [-59, +29] relative to its ox.
    # Placing ox_rp = -30 gives bounds ~[-89, -1] — mostly left half.
    draw_ren_pang(t, ox=ox + (-30) * scale, oy=oy + 0 * scale, scale=0.85 * scale)

    # --- Right 匕 ---
    # shu_wan_gou at scale 0.70:
    #   shaft: x=0 (relative), from y=+70*0.7=+49 to y=-30*0.7=-21
    #   arc to (28, -49), tail to (56, -49), hook to (52.5, -33.6)
    # Position ox_swg=+30, oy_swg=-10:
    #   shaft absolute: x=+30, from y=+39 down to y=-31
    #   tail_end absolute: (+86, -59)
    s_swg = 0.70
    ox_swg = ox + 30 * scale
    oy_swg = oy + (-10) * scale
    draw_shu_wan_gou(t, ox=ox_swg, oy=oy_swg, scale=s_swg * scale)

    # Shaft top of shu_wan_gou (where 撇 must terminate):
    shaft_top_x = ox_swg  # (shaft x offset is 0)
    shaft_top_y = oy_swg + 70.0 * s_swg * scale  # +39 abs at scale=1

    # 撇 head: up-and-right of shaft top by ~30px right, ~15px up
    pie_head = (shaft_top_x + 32 * scale, shaft_top_y + 18 * scale)
    pie_tail = (shaft_top_x - 1 * scale, shaft_top_y - 1 * scale)  # lands ON shaft top
    draw_pie_short(t, pie_head, pie_tail, thickness=9)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_hua(draw, ox=0, oy=0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_化.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
