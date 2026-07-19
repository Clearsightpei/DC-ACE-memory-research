# p2_radical_103_毛 (máo) — G3 coord-format
#
# GT analysis (from gt/phase2/毛.png): 4 strokes.
#   1) 撇 (short pie at top, from upper-right ~ (170, 90) sweeping down-left to (110, 130))
#   2) 短横 (top short horizontal, from ~(115, 130) to (200, 125))
#   3) 长横 (middle horizontal, wider, from ~(80, 175) to (215, 170))
#   4) 竖弯钩 (starts near top-mid ~ (155, 100), descends through the two heng,
#       curves right at bottom (~y=245), horizontal tail, hook up at right end)
#
# TR8 inline-fresh test applied per stroke:
#   - Stroke 1 pie: short and shallow — DIFFERENT from bank pie (which is long
#     tapered chord). INLINE fresh as short tapered bezier.
#   - Strokes 2 & 3 heng: two DIFFERENT lengths + slight upward tilt to the right.
#     Bank heng is a uniform straight 200x12 centered rectangle. INLINE fresh
#     to control length + subtle upward tilt (typical calligraphic 横 in 毛).
#   - Stroke 4 竖弯钩: shape matches the shu_wan_gou primitive's canonical form
#     (vertical shaft, quarter-arc right, horizontal tail, hook up). REUSE
#     the bank primitive with deliberate (ox, oy, scale).

import sys
import os
from PIL import Image, ImageDraw

# Add success_bank/code to path for the shu_wan_gou reuse.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "success_bank", "code"))
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math coords (center origin, +y up) -> PIL pixels (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_tapered_line(draw, p_start, p_end, w_start, w_end, n=24):
    """Draw a straight tapered line via segmented widths (spine + width profile, P3)."""
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        x0 = p_start[0] + u0 * (p_end[0] - p_start[0])
        y0 = p_start[1] + u0 * (p_end[1] - p_start[1])
        x1 = p_start[0] + u1 * (p_end[0] - p_start[0])
        y1 = p_start[1] + u1 * (p_end[1] - p_start[1])
        w = w_start + (w_end - w_start) * ((u0 + u1) / 2)
        w_int = max(1, int(round(w)))
        draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=w_int)


def draw_bezier_tapered(draw, p0, p_ctrl, p1, w_start, w_end, n=40):
    """Tapered quadratic bezier from p0 (thick head) to p1 (thin tail)."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p_ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p_ctrl[1] + u ** 2 * p1[1]
        w = w_start + (w_end - w_start) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
        prev = (bx, by)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---------- Stroke 1: short 撇 at top ----------
    # Revision: extend the pie a bit further down-left and start it higher,
    # to match GT's more prominent top 撇.
    pie_head = (168.0, 78.0)
    pie_tail = (98.0, 128.0)
    pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 - 8.0,
                (pie_head[1] + pie_tail[1]) / 2 + 6.0)
    draw_bezier_tapered(draw, pie_head, pie_ctrl, pie_tail,
                        w_start=8.0, w_end=1.5, n=40)

    # ---------- Stroke 2: 短横 (top short heng) ----------
    # Revision: extend rightward slightly, start at pie tail welding point.
    heng1_left = (102.0, 130.0)   # welds with pie tail area
    heng1_right = (205.0, 125.0)
    draw_tapered_line(draw, heng1_left, heng1_right,
                      w_start=7.0, w_end=6.5)
    r = 4.0
    draw.ellipse([heng1_right[0] - r, heng1_right[1] - r,
                  heng1_right[0] + r, heng1_right[1] + r], fill=(0, 0, 0))

    # ---------- Stroke 3: 长横 (middle heng, longest) ----------
    # Revision: shift left a touch to center the character.
    heng2_left = (65.0, 180.0)
    heng2_right = (220.0, 172.0)
    draw_tapered_line(draw, heng2_left, heng2_right,
                      w_start=8.0, w_end=7.0)
    r = 4.5
    draw.ellipse([heng2_right[0] - r, heng2_right[1] - r,
                  heng2_right[0] + r, heng2_right[1] + r], fill=(0, 0, 0))

    # ---------- Stroke 4: 竖弯钩 ----------
    # REUSE bank primitive draw_shu_wan_gou. Its canonical form:
    #   shaft top (ox,   oy+70*s)   -> shaft bot (ox, oy-30*s)
    #   arc through (ox+40*s, oy-70*s)
    #   tail end (ox+80*s, oy-70*s)
    #   hook tip (ox+75*s, oy-48*s)
    # Target:
    #   shaft top pixel ~ (155, 100)   -> math coord (5, 50)
    #   shaft bottom pixel ~ (155, 240) -> math coord (5, -90)
    #   tail end pixel ~ (245, 245)     -> math coord (95, -95)
    #
    # With scale s: shaft length = 100 s px. Target shaft length = 240 - 100
    # = 140 px  =>  s ≈ 1.4. But that pushes tail to x = 5+80*1.4 = 117
    # (pixel 267) — off-canvas-ish. Use s = 1.15, giving shaft length 115 px
    # (top y +67 -> bot y -48 in math = pixels y=83 to y=198), arc bottom
    # pixel y ≈ 208 (matches GT). Tail end x = 5 + 80*1.15 = 97 (pixel 247).
    # ox = 5 (math), oy = 20 (math) shifts the whole primitive:
    #   shaft top math (5, 20 + 70*1.15) = (5, 100.5) -> pixel (155, 49.5)  [too high]
    # Rework: with oy = -20, shaft top math (5, -20+80.5) = (5, 60.5) ->
    #   pixel (155, 89.5) [close to (155,100)]. Shaft bot math
    #   (5, -20 - 34.5) = (5, -54.5) -> pixel (155, 204.5).
    # Tail end math (5+92, -20-80.5) = (97, -100.5) -> pixel (247, 250.5).
    # Hook tip math (5+86, -20-55.2) = (91, -75.2) -> pixel (241, 225.2).
    # This matches the GT geometry closely.
    draw_shu_wan_gou(draw, ox=5.0, oy=-20.0, scale=1.15)

    # ---------- Save ----------
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_毛.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
