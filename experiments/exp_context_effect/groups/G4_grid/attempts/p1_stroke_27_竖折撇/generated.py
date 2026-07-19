"""p1_stroke_27_竖折撇 — 竖 down → 折 right → 撇 diagonal down-left.

竖折撇 is a compound stroke:
  1. 竖 vertical descent from head (upper area) to a first corner.
  2. 折 short horizontal to the right (like 竖折) to a second pivot.
  3. 撇 diagonal sweep down-and-left from that pivot, tapering to a
     needle tip.

Both bends are P (welded) joints reinforced with 顿笔 discs.

Anchors (米字格, PIL-native y-down):
  head   — TC 起笔 (upper-center).
  knee1  — ML/BL area (bottom of vertical, top of the small 横).
  knee2  — end of the short 横 (a bit to the right of knee1).
  tail   — 撇 needle tip (BL area, well below knee2, to the left).

Approach: reuse the primitives compositionally in spirit — the vertical
segment is uniform width (like 竖折's 竖), the short 横 is uniform, and
the 撇 uses a tapered quad-Bezier with slight leftward bow. Import the
shared _anchor helper for anchor→pixel + rendering utilities.

Rule guard: NEVER writes to success_bank/code/. This script only writes
its own attempt PNG.
"""
import sys
import os
from PIL import Image, ImageDraw

# Import shared primitives from the group's success_bank/code.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from _anchor import (  # noqa: E402
    anchor_to_xy, fat_line, quad_bezier, stroke_variable_width,
)


def draw_shu_zhe_pie(draw,
                     head, knee1, knee2, tail,
                     v_width=11, h_width=10,
                     pie_head_w=12, pie_tail_w=1,
                     shoulder1=14, shoulder2=14,
                     pie_curve=0.10,
                     color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_k1 = anchor_to_xy(knee1)
    p_k2 = anchor_to_xy(knee2)
    p_tail = anchor_to_xy(tail)

    # Sanity assertions (see principle_bank: cheap invariants).
    assert p_k1[1] > p_head[1], "vertical must descend (knee1 below head)"
    assert p_k2[0] > p_k1[0], "short 横 must go rightward"
    assert p_tail[1] > p_k2[1], "撇 must descend from knee2"
    assert p_tail[0] < p_k2[0], "撇 must sweep left of knee2"

    # 1. 竖 vertical from head to knee1 (uniform width).
    fat_line(draw, p_head, p_k1, v_width, color)

    # 2. 短横 from knee1 to knee2 (uniform).
    fat_line(draw, p_k1, p_k2, h_width, color)

    # 3. 顿笔 discs at the two corners (P joints).
    for (cx, cy), sd in ((p_k1, shoulder1), (p_k2, shoulder2)):
        r = sd / 2.0
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)

    # 4. 撇 from knee2 → tail: tapered quad-Bezier with slight bow.
    dx = p_tail[0] - p_k2[0]
    dy = p_tail[1] - p_k2[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    # Perpendicular to chord.
    perp = (-dy / length, dx / length)
    bow = pie_curve * length
    mid = ((p_k2[0] + p_tail[0]) / 2.0, (p_k2[1] + p_tail[1]) / 2.0)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    segments = 48
    pts = quad_bezier(p_k2, ctrl, p_tail, n=segments)
    widths = [pie_head_w + (pie_tail_w - pie_head_w) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 米字格 anchors for 竖折撇.
    # 竖 sits at the center, descending straight down.
    # Short 横 pushes right (compact — this stroke's 横 is short).
    # 撇 sweeps down-and-left from knee2, well to the lower-left.
    # Straight-vertical invariant: head.x_pixel == knee1.x_pixel.
    #   head  ('TC', 0.30, 0.30) -> px=130
    #   knee1 ('C',  0.30, 0.60) -> px=130   (same x, straight 竖)
    #   knee2 ('C',  0.85, 0.60) -> px=185
    #   tail  ('BL', 0.20, 0.75) -> px=20, py=275
    head  = ('TC', 0.30, 0.30)
    knee1 = ('C',  0.30, 0.60)
    knee2 = ('C',  0.85, 0.60)
    tail  = ('BL', 0.20, 0.75)

    draw_shu_zhe_pie(draw, head, knee1, knee2, tail)

    out = os.path.join(_HERE, "01_竖折撇.png")
    img.save(out)
    print(out)


if __name__ == "__main__":
    main()
