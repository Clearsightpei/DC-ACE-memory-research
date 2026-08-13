"""p3_char_0569_得 (dé, "get/obtain") — 11 strokes.

Decomposition:
  Left  : 彳 (chi_step, 3 strokes)      — s1 short pie, s2 long pie, s3 short shu
  Right : 日 (ri, 4 strokes)             — s4 left shu, s5 heng-zhe, s6 mid heng, s7 bottom heng
  Right : 一 (heng, 1 stroke)            — s8 wide horizontal below 日
  Right : 寸 (cun, 3 strokes)            — s9 heng, s10 shu-gou, s11 dian

Fresh render: bank chi_step / ri primitives skipped (see BANK_DEVIATION).
"""
# BANK_DEVIATION
# skipped: chi_step.py, ri.py
# reason: chi_step defaults center on col-1 (TC/C/BC) but 得's 彳 must
#         stay in the left column (col 0) to leave space for 日+一+寸.
#         ri defaults are wall-to-wall for standalone 日; here 日 must
#         be compact in the upper-right slot only.
# fresh_component: chi_step_for_de, ri_top_slot_for_de

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '11 strokes = 彳(3)+日(4)+一(1)+寸(3). 日 rendered as closed rectangle.'
}


def _pie(draw, head, tail, head_w=9, tail_w=2, curve=0.10, n=48):
    hx, hy = head; tx, ty = tail
    dx, dy = tx - hx, ty - hy
    nx, ny = -dy, dx
    L = (nx * nx + ny * ny) ** 0.5 or 1
    mx = (hx + tx) / 2 + nx / L * curve * ((dx*dx+dy*dy)**0.5)
    my = (hy + ty) / 2 + ny / L * curve * ((dx*dx+dy*dy)**0.5)
    pts = quad_bezier((hx, hy), (mx, my), (tx, ty), n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6: return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_de(draw):
    strokes_drawn = 0

    # ================ 彳 (left radical, col 0) ================
    # s1 upper short 撇
    _pie(draw, (75, 55), (35, 95), head_w=7, tail_w=3, curve=0.08)
    strokes_drawn += 1
    # s2 lower long 撇 — sweeps from mid-top down-left
    _pie(draw, (90, 95), (12, 195), head_w=10, tail_w=2, curve=0.10)
    strokes_drawn += 1
    # s3 short 竖 — dropping from mid-lower toward bottom
    fat_line(draw, (75, 175), (78, 245), width=9)
    strokes_drawn += 1

    # ================ 日 (upper right, compact rectangle) ================
    # slot: x=130..215, y=50..135
    L, R = 130, 215
    T, B = 50, 135
    MID = 92
    # s4 left 竖  (top → bottom of 日)
    fat_line(draw, (L, T), (L, B), width=9)
    strokes_drawn += 1
    # s5 横折 (top-left corner across to top-right, then down to bottom-right)
    fat_line(draw, (L, T), (R, T), width=9)
    fat_line(draw, (R, T), (R, B), width=9)
    draw.ellipse([R-5, T-5, R+5, T+5], fill=(0, 0, 0))  # weld corner
    strokes_drawn += 1
    # s6 middle 横 (inside 日, doesn't touch right wall — small N gap)
    fat_line(draw, (L + 6, MID), (R - 6, MID), width=8)
    strokes_drawn += 1
    # s7 bottom 横 (closes 日, welds both sides)
    fat_line(draw, (L, B), (R, B), width=9)
    strokes_drawn += 1

    # ================ 一 (long middle bar below 日) ================
    # spans roughly x=105..285, y=170
    fat_line(draw, (105, 170), (285, 170), width=9)
    strokes_drawn += 1

    # ================ 寸 (bottom right) ================
    # slot: x=115..280, y=175..290
    # s9 top heng of 寸 — shorter than the 一 above, y=205
    fat_line(draw, (135, 210), (270, 210), width=8)
    strokes_drawn += 1
    # s10 竖钩 (vertical hook) — pierces s9 (P — welded), goes down, hooks left
    top = (215, 178)          # pierces the s9 heng
    bot = (215, 270)          # bottom of vertical
    hook_end = (188, 258)     # hooks up-left
    fat_line(draw, top, bot, width=9)
    fat_line(draw, bot, hook_end, width=8)
    draw.ellipse([bot[0]-5, bot[1]-5, bot[0]+5, bot[1]+5], fill=(0, 0, 0))
    strokes_drawn += 1
    # s11 丶 dot — small diagonal blob right of the vertical near mid
    _pie(draw, (235, 225), (258, 250), head_w=4, tail_w=10, curve=0.02, n=16)
    strokes_drawn += 1

    assert strokes_drawn == 11, f'stroke count {strokes_drawn} != 11'
    return strokes_drawn


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    n = draw_de(draw)
    out = os.path.join(os.path.dirname(__file__), '01_得.png')
    img.save(out)
    print(f'wrote {out}; strokes={n}')


if __name__ == '__main__':
    main()
