"""横折折折 (héng zhé zhé zhé) — 4-segment staircase: 横→竖→横→竖.

Signature:
  draw_heng_zhe_zhe_zhe(draw, head, corner1, corner2, corner3, tail,
                        h_width=10, v_width=10, shoulder=13)

Anchors trace a staircase descending toward BR:
  head    — 起笔 (TL).
  corner1 — end of first 横 (TR).
  corner2 — end of first 竖 (MR).
  corner3 — end of second 横 (MR, right of corner2).
  tail    — end of final 竖 (BR).

Joint spec: P × 3 (welded at each corner).
Ref: batch2 p1_stroke_30_横折折折 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_heng_zhe_zhe_zhe(draw, head, corner1, corner2, corner3, tail,
                          h_width=10, v_width=10, shoulder=13,
                          color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tail = anchor_to_xy(tail)

    assert p_c1[0] > p_head[0], 'seg1 must go right'
    assert p_c2[1] > p_c1[1], 'seg2 must go down'
    assert p_c3[0] > p_c2[0], 'seg3 must go right'
    assert p_tail[1] > p_c3[1], 'seg4 must go down'

    fat_line(draw, p_head, p_c1, h_width, color=color)
    fat_line(draw, p_c1, p_c2, v_width, color=color)
    fat_line(draw, p_c2, p_c3, h_width, color=color)
    fat_line(draw, p_c3, p_tail, v_width, color=color)

    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
