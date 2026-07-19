"""p1_stroke_30_横折折折 (héng zhé zhé zhé)

A four-segment compound stroke: horizontal → vertical → horizontal → vertical,
producing three consecutive welded 90° corners.

The general shape traces a shallow "staircase" descending to the right:

    A ────── B
             │
             C ────── D
                      │
                      E

Segments (all welded at declared corners, small 顿笔 disc at each):
  1. 横 from head A (TL, 0.30, 0.30) → corner1 B (TR, 0.55, 0.30)
  2. 竖 (short) from B → corner2 C (MR, 0.05, 0.65)
  3. 横 from C → corner3 D (MR, 0.85, 0.65)
  4. 竖 from D → tail E (BR, 0.85, 0.75)

Joints (all P — welded, shoulder disc drawn):
  seg1.tail @ corner1 (B) ⇆ seg2.head @ B   (P)
  seg2.tail @ corner2 (C) ⇆ seg3.head @ C   (P)
  seg3.tail @ corner3 (D) ⇆ seg4.head @ D   (P)

Reuses the batch-1 pattern from heng_zhe.py: fat_line segments + shoulder
disc at every welded corner. No new primitive needed — this is 横折 composed
twice more.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


CANVAS = 300
H_WIDTH = 10
V_WIDTH = 10
SHOULDER = 13


def draw_heng_zhe_zhe_zhe(draw, head, corner1, corner2, corner3, tail,
                          h_width=H_WIDTH, v_width=V_WIDTH,
                          shoulder=SHOULDER, color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tail = anchor_to_xy(tail)

    # Sanity assertions (per principle_bank: catch silent geometric bugs).
    # Segment 1: horizontal, head→corner1 goes rightward.
    assert p_c1[0] > p_head[0], "seg1 must go right (head→c1)"
    # Segment 2: vertical down, corner1→corner2 goes downward.
    assert p_c2[1] > p_c1[1], "seg2 must go down (c1→c2)"
    # Segment 3: horizontal right, corner2→corner3 goes rightward.
    assert p_c3[0] > p_c2[0], "seg3 must go right (c2→c3)"
    # Segment 4: vertical down, corner3→tail goes downward.
    assert p_tail[1] > p_c3[1], "seg4 must go down (c3→tail)"

    # Four fat-line segments.
    fat_line(draw, p_head, p_c1, h_width, color)
    fat_line(draw, p_c1, p_c2, v_width, color)
    fat_line(draw, p_c2, p_c3, h_width, color)
    fat_line(draw, p_c3, p_tail, v_width, color)

    # 顿笔 shoulder discs at every welded corner (P joints).
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # 米字格 anchors — staircase descending toward BR.
    # Segments must be perpendicular: horizontals share y, verticals share x.
    #
    # Layout (pixels):
    #   A(60,90) ─── B(230,90)      seg1 横, y=90
    #                │                seg2 竖, x=230, y: 90→170
    #                C(230,170) ─── D(275,170)  seg3 横, y=170  (short)
    #                                │           seg4 竖, x=275, y: 170→255
    #                                E(275,255)
    head    = ('TL', 0.60, 0.90)   # px= 60, py= 90
    corner1 = ('TR', 0.30, 0.90)   # px=230, py= 90
    corner2 = ('MR', 0.30, 0.70)   # px=230, py=170
    corner3 = ('MR', 0.75, 0.70)   # px=275, py=170
    tail    = ('BR', 0.75, 0.55)   # px=275, py=255

    draw_heng_zhe_zhe_zhe(draw, head, corner1, corner2, corner3, tail)

    out_path = os.path.join(os.path.dirname(__file__), '01_横折折折.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
