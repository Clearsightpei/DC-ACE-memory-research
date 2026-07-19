"""p1_stroke_26_横折折 attempt.

横折折 (héng zhé zhé) — 横折加横折.
Two 横折 chained: horizontal → down turn → horizontal → down turn.
Four segments forming a stepped-down zigzag going right-and-down.

Segments (using 米字格 anchors, PIL-native y-down convention):
  1. heng1  : head1 (TL 0.30, 0.35)  →  corner1 (TC 0.85, 0.40)
  2. shu1   : corner1                →  corner2 (C  0.85, 0.55)  (short drop)
  3. heng2  : corner2                →  corner3 (MR 0.60, 0.60)  (second heng)
  4. shu2   : corner3                →  tail    (BR 0.60, 0.75)  (final drop)

Joints: three internal P (welded) at corner1, corner2, corner3.
Reuses `fat_line` from `_anchor.py`; small 顿笔 disc at each corner.
"""
import sys
import os

# Make success_bank/code importable for the shared _anchor helper (READ ONLY).
_SB_CODE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
if _SB_CODE not in sys.path:
    sys.path.insert(0, _SB_CODE)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def draw_heng_zhe_zhe(draw,
                      head, corner1, corner2, corner3, tail,
                      h_width=10, v_width=10, shoulder=13,
                      color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tail = anchor_to_xy(tail)

    # Sanity assertions (principle_bank: catch silent geometric bugs).
    # heng1 should be near-horizontal, going right.
    assert p_c1[0] > p_head[0], "heng1 must go rightward"
    # shu1 short drop: c2 below c1, roughly same x.
    assert p_c2[1] > p_c1[1], "shu1 must drop downward"
    # heng2 should go rightward again.
    assert p_c3[0] > p_c2[0], "heng2 must go rightward"
    # shu2 final drop.
    assert p_tail[1] > p_c3[1], "shu2 must drop downward"

    # Four segments.
    fat_line(draw, p_head, p_c1, h_width, color)
    fat_line(draw, p_c1, p_c2, v_width, color)
    fat_line(draw, p_c2, p_c3, h_width, color)
    fat_line(draw, p_c3, p_tail, v_width, color)

    # 顿笔 discs at every welded corner.
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_heng_zhe_zhe(
        draw,
        head    =('TL', 0.30, 0.35),
        corner1 =('TC', 0.85, 0.40),
        corner2 =('C',  0.85, 0.55),
        corner3 =('MR', 0.60, 0.60),
        tail    =('BR', 0.60, 0.75),
        h_width=10, v_width=10, shoulder=13,
    )

    out = os.path.join(os.path.dirname(__file__), '01_横折折.png')
    img.save(out)
    print(f"wrote {out} size={img.size}")


if __name__ == '__main__':
    main()
