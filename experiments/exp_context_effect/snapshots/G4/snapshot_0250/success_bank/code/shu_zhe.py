"""竖折 (shù zhé) — vertical descent then sharp 90° turn to the right.

Signature:
  draw_shu_zhe(draw, head, corner, tail,
               v_width=10, h_width=10, shoulder=13)

Anchors:
  head   — 起笔 (TL region).
  corner — elbow (BL region).
  tail   — end of horizontal (BR region).

Segments: vertical head→corner, horizontal corner→tail, filled shoulder
disc at corner. No hook, no taper-to-tip (squared 收笔).

Joint spec: P (welded) at corner.
Ref: batch1 p1_stroke_15_竖折 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_shu_zhe(draw, head, corner, tail,
                 v_width=10, h_width=10, shoulder=13,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)
    fat_line(draw, p_head, p_corner, v_width, color=color)
    fat_line(draw, p_corner, p_tail, h_width, color=color)
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
