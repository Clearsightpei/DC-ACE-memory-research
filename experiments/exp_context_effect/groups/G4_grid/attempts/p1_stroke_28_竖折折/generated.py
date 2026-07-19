"""p1_stroke_28_竖折折 attempt.

竖折折 (shù zhé zhé) — 竖折加折.
A 竖折 (down then right) followed by one more 折 (down again).
Three segments forming a step going down-right-down.

Segments (using 米字格 anchors, PIL-native y-down convention):
  1. shu1  : head   (TL 0.40, 0.25)  →  corner1 (ML 0.40, 0.70)   (vertical descent)
  2. heng  : corner1                 →  corner2 (C  0.85, 0.70)   (horizontal right)
  3. shu2  : corner2                 →  tail    (BC 0.85, 0.75)   (final descent, vertical)

Joints: two internal P (welded) at corner1 and corner2.
Reuses `fat_line` from `_anchor.py`; small 顿笔 disc at each corner.

Analogous to `shu_zhe.py` (batch1 pass) but with an extra shu segment
tacked on after the heng — mirrors the 横折折 structure from
p1_stroke_26 (heng-shu-heng-shu) but starts with shu.
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


def draw_shu_zhe_zhe(draw,
                     head, corner1, corner2, tail,
                     v_width=10, h_width=10, shoulder=13,
                     color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_tail = anchor_to_xy(tail)

    # Sanity assertions (principle_bank: catch silent geometric bugs).
    # shu1 must drop downward from head to corner1.
    assert p_c1[1] > p_head[1], "shu1 must drop downward"
    # heng must go rightward from corner1 to corner2.
    assert p_c2[0] > p_c1[0], "heng must go rightward"
    # shu2 must drop downward from corner2 to tail.
    assert p_tail[1] > p_c2[1], "shu2 must drop downward"

    # Three segments.
    fat_line(draw, p_head, p_c1, v_width, color)   # 竖
    fat_line(draw, p_c1, p_c2, h_width, color)     # 折 → 横
    fat_line(draw, p_c2, p_tail, v_width, color)   # 折 → 竖

    # 顿笔 discs at every welded corner.
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_shu_zhe_zhe(
        draw,
        head    =('TL', 0.40, 0.25),
        corner1 =('ML', 0.40, 0.70),
        corner2 =('C',  0.85, 0.70),
        tail    =('BC', 0.85, 0.75),
        v_width=10, h_width=10, shoulder=13,
    )

    out = os.path.join(os.path.dirname(__file__), '01_竖折折.png')
    img.save(out)
    print(f"wrote {out} size={img.size}")


if __name__ == '__main__':
    main()
