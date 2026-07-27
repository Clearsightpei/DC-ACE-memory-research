"""车 (chē, "cart", 4 strokes) — B2 pass.

Strokes:
  s1 — 横 (top short bar).
  s2 — 撇折 (inlined; pie down-left + short heng flick).
  s3 — 横 (middle bar).
  s4 — 竖 (long spine, extends past bottom edge for prominence).

Joints:
  s1.mid ⇆ s2.mid @ C  — P.
  s2.mid ⇆ s4.mid @ C  — P.
  s3.mid ⇆ s4.mid @ BC — P.
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from shu import draw_shu


def _pie_zhe_inline(draw, head, pivot, tail, color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_pivot = anchor_to_xy(pivot)
    p_tail = anchor_to_xy(tail)
    dx, dy = p_pivot[0]-p_head[0], p_pivot[1]-p_head[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    perp = (-dy/length, dx/length)
    bow = 0.14 * length
    mid = ((p_head[0]+p_pivot[0])*0.5, (p_head[1]+p_pivot[1])*0.5)
    ctrl = (mid[0]+perp[0]*bow, mid[1]+perp[1]*bow)
    pts = quad_bezier(p_head, ctrl, p_pivot, n=40)
    widths = [10 + (5-10)*(i/40) for i in range(41)]
    stroke_variable_width(draw, pts, widths, color=color)
    r = 4
    draw.ellipse([p_pivot[0]-r, p_pivot[1]-r, p_pivot[0]+r, p_pivot[1]+r],
                 fill=color)
    fat_line(draw, p_pivot, p_tail, width=7)


def draw_che(draw,
             s1_head=('ML', 0.809, 0.131), s1_tail=('MR', 0.171, 0.031),
             s2_head=('TC', 0.389, 0.565),
             s2_pivot=('C', 0.15, 0.75),
             s2_tail=('MR', 0.183, 0.778),
             s3_head=('BL', 0.331, 0.385), s3_tail=('BR', 0.669, 0.353),
             s4_head=('C', 0.415, 0.482),  s4_tail=('BC', 0.532, 1.146)):
    draw_heng(draw, s1_head, s1_tail, width=8)
    _pie_zhe_inline(draw, s2_head, s2_pivot, s2_tail)
    draw_heng(draw, s3_head, s3_tail, width=9)
    draw_shu(draw, s4_head, s4_tail, width=9)
