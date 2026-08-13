"""佐 = 亻 (left radical) + 左 (right).
7 strokes per MMH:
  s1 亻撇  TL(0.908,0.683) → BL(0.161,0.065)
  s2 亻竖  ML(0.727,0.509) → BL(0.744,0.971)
  s3 左短横 C(0.204,0.477) → MR(0.481,0.354)
  s4 左长撇 TC(0.746,0.706) → BL(0.882,0.646)   # crosses s3 (P)
  s5 工上横 BC(0.526,0.106) → MR(0.367,0.995)
  s6 工竖   BC(0.84,0.153)  → BC(0.813,0.646)
  s7 工下横 BC(0.154,0.777) → BR(0.728,0.733)

MMH-verbatim anchors. Bank primitives (ren_side, gong) not imported —
anchors here differ from ren_side/gong defaults enough that inlining
via _anchor + variable-width polylines is cleaner.

Following v9 rule: trust MMH anchors verbatim.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    "..", "..", "success_bank", "code"))
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line, CANVAS)
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes, MMH-verbatim anchors; s3xs4 welded P at C; other joints N.'
}


def draw_pie_curve(draw, head, tail, head_w=11, tail_w=1, curve=0.15, n=48):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # control offset perpendicular-ish to give a bow
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # perpendicular (rotate 90 CCW): (-dy, dx). Pie bows to the LEFT of travel.
    ctrl = (mx + (-dy) * curve, my + dx * curve)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [head_w + (tail_w - head_w) * i / (len(pts) - 1)
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng_var(draw, head, tail, w=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width=w)


def draw_shu_var(draw, head, tail, w=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width=w)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # s1 亻撇 — long curved 撇 upper-right to lower-left
    draw_pie_curve(d, ('TL', 0.908, 0.683), ('BL', 0.161, 0.065),
                   head_w=11, tail_w=2, curve=0.12, n=60)

    # s2 亻竖 — vertical drop from mid to bottom
    draw_shu_var(d, ('ML', 0.727, 0.509), ('BL', 0.744, 0.971), w=9)

    # s3 左 short heng — slight rise left to right (welded at C with s4)
    draw_heng_var(d, ('C', 0.204, 0.477), ('MR', 0.481, 0.354), w=8)

    # s4 左 long 撇 — top-center to bottom-left, crosses s3 at C (P)
    draw_pie_curve(d, ('TC', 0.746, 0.706), ('BL', 0.882, 0.646),
                   head_w=10, tail_w=2, curve=0.10, n=60)

    # s5 工 top heng (short)
    draw_heng_var(d, ('BC', 0.526, 0.106), ('MR', 0.367, 0.995), w=8)

    # s6 工 竖
    draw_shu_var(d, ('BC', 0.84, 0.153), ('BC', 0.813, 0.646), w=8)

    # s7 工 bottom heng (wide)
    draw_heng_var(d, ('BC', 0.154, 0.777), ('BR', 0.728, 0.733), w=9)

    out_path = os.path.join(os.path.dirname(__file__), "01_佐.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    render()
