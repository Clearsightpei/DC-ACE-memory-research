"""竖折折 (shù zhé zhé) — 竖折 with an extra 折 turn (down-right-down).

Signature:
  draw_shu_zhe_zhe(draw, head, corner1, corner2, tail,
                   v_width=10, h_width=10, shoulder=13)

Anchors:
  head    — 起笔 upper (TL).
  corner1 — bottom of first 竖, start of 横 (ML).
  corner2 — end of 横, start of second 竖 (C).
  tail    — bottom of final 竖 (BC).

Segments (three straight fat_lines):
  1. 竖 head → corner1 (must drop downward).
  2. 横 corner1 → corner2 (must go rightward).
  3. 竖 corner2 → tail (must drop downward).

Joint spec: P × 2 (welded at corner1 and corner2).
Ref: batch2 p1_stroke_28_竖折折 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_shu_zhe_zhe(draw, head, corner1, corner2, tail,
                     v_width=10, h_width=10, shoulder=13,
                     color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_tail = anchor_to_xy(tail)

    # Direction sanity checks.
    assert p_c1[1] > p_head[1], 'shu1 must drop downward'
    assert p_c2[0] > p_c1[0], 'heng must go rightward'
    assert p_tail[1] > p_c2[1], 'shu2 must drop downward'

    fat_line(draw, p_head, p_c1, v_width, color=color)
    fat_line(draw, p_c1, p_c2, h_width, color=color)
    fat_line(draw, p_c2, p_tail, v_width, color=color)

    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
