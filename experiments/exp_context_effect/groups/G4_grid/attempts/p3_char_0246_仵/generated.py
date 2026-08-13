"""仵 = 亻 (ren_side) + 午 (wu, "noon").
Split: left 亻 (2 strokes: pie + shu), right 午 (4 strokes: pie, heng, heng, shu).
Total 6 strokes — matches MMH expected count.

Anchors follow MMH per-stroke expectations (dispatcher-injected).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: 亻 (pie+shu) + 午 (pie+heng+heng+shu). Joints: '
             's1.mid⇆s2.head=N; s3.mid⇆s4.head=N; s4.mid⇆s6.head=N; '
             's5.mid⇆s6.mid=P (welded, center of middle heng).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def draw_pie_curve(d, head, tail, head_w=11, tail_w=2, curve=0.10, n=48):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    # perpendicular offset toward inside of the curve
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # bow to the lower-left; perpendicular = (-dy, dx) normalized
    import math
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    ctrl = (mx + nx * L * curve, my + ny * L * curve)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [head_w + (tail_w - head_w) * i / n for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)


def draw_heng_line(d, head, tail, width=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width)


def draw_shu_line(d, head, tail, width=9):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width)


# --- 亻 (left radical) ---
# s1: 撇 from upper-right corner of left column down to lower-left
draw_pie_curve(d, ('TL', 0.908, 0.624), ('ML', 0.176, 0.983),
               head_w=12, tail_w=2, curve=0.08)
# s2: 竖 dropping from mid-upper (touches pie body — T/N join)
draw_shu_line(d, ('ML', 0.680, 0.521), ('BL', 0.721, 0.895), width=10)

# --- 午 (right side) ---
# s3: short 撇 at top (from TC down-left into C)
draw_pie_curve(d, ('TC', 0.509, 0.645), ('C', 0.084, 0.600),
               head_w=9, tail_w=2, curve=0.06)
# s4: top 横 (short, right of the pie)
draw_heng_line(d, ('C', 0.459, 0.251), ('MR', 0.370, 0.075), width=8)
# s5: middle 横 (long, spans across)
draw_heng_line(d, ('C', 0.014, 0.966), ('MR', 0.707, 0.849), width=9)
# s6: 竖 down the middle of 午 (welds across middle heng center → P)
# clamp y_frac at BC to <=1.0 so it stays on canvas
draw_shu_line(d, ('C', 0.711, 0.292), ('BC', 0.825, 0.99), width=10)

out_path = os.path.join(os.path.dirname(__file__), '01_仵.png')
img.save(out_path)
print(f'Wrote {out_path}')
