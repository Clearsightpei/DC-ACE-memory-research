"""横折 (héng zhé) — horizontal then sharp 90° turn downward.

Signature:
  draw_heng_zhe(draw, head, corner, tail,
                h_width=10, v_width=10, shoulder=13)

Anchors:
  head   — 起笔 upper-left (ML region).
  corner — 折 point (MR region, top of corner).
  tail   — end of vertical drop (BR region).

Segments: horizontal head→corner, vertical corner→tail, plus a filled
shoulder disc at corner for the 顿笔 press.

Joint spec: P (welded) at corner — corner is SHARED between 横 tail
and 竖 head.
Ref: batch1 p1_stroke_11_横折 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_heng_zhe(draw, head, corner, tail,
                  h_width=10, v_width=10, shoulder=13,
                  color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)
    fat_line(draw, p_head, p_corner, h_width, color=color)
    fat_line(draw, p_corner, p_tail, v_width, color=color)
    # Shoulder press at corner.
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
