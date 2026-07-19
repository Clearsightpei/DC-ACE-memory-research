"""撇折 (piě zhé) — 撇 sweep down-left then sharp turn into a uniform 横 rightward.

Signature:
  draw_pie_zhe(draw, head, pivot, tail,
               pie_head_w=13, pie_tip_w=5, heng_w=7, shoulder=4)

Anchors:
  head  — 撇 起笔 upper-right (TR).
  pivot — welded elbow (BL region, low-left).
  tail  — 横 endpoint rightward (BC region), squared 收笔.

Segments:
  1. 撇: head → pivot, tapered thick→thin, slight right-perpendicular bow.
  2. 横: pivot → tail, uniform heng_w, straight.

Joint spec: P (welded) at pivot; small shoulder disc for the elbow.
Ref: batch1 p1_stroke_18_撇折 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def draw_pie_zhe(draw, head, pivot, tail,
                 pie_head_w=13, pie_tip_w=5, heng_w=7, shoulder=4,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_pivot = anchor_to_xy(pivot)
    p_tail = anchor_to_xy(tail)

    # 撇: tapered bezier with gentle perpendicular bow.
    dx, dy = p_pivot[0] - p_head[0], p_pivot[1] - p_head[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    mid = ((p_head[0] + p_pivot[0]) * 0.5, (p_head[1] + p_pivot[1]) * 0.5)
    off = 0.07 * length
    ctrl = (mid[0] + perp[0] * off, mid[1] + perp[1] * off)
    pts = quad_bezier(p_head, ctrl, p_pivot, n=48)
    n = len(pts) - 1
    widths = [pie_head_w + (pie_tip_w - pie_head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths, color=color)

    # 横: straight uniform, squared terminal.
    fat_line(draw, p_pivot, p_tail, heng_w, color=color)

    # Small shoulder disc at pivot to sharpen the elbow.
    r = shoulder / 2.0 + 2
    draw.ellipse([p_pivot[0] - r, p_pivot[1] - r,
                  p_pivot[0] + r, p_pivot[1] + r], fill=color)
