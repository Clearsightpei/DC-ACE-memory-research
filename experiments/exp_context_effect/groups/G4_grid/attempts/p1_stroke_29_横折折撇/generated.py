"""p1_stroke_29_横折折撇 attempt.

横折折撇 (héng zhé zhé piě) — 横折折 加 撇.
Compound of a stepped 横折折 (horizontal → short drop → horizontal) that
terminates in a 撇 (tapered diagonal sweep down-and-left) instead of a
final vertical. Occurs in characters like 及, 廷, 建.

Four segments (米字格 anchors, PIL-native y-down convention):
  1. heng1 : head    (TL 0.35, 0.30)  →  corner1 (TC 0.85, 0.35)   [short opening 横]
  2. shu1  : corner1                  →  corner2 (C  0.30, 0.35)   [折 down-left short drop]
  3. heng2 : corner2                  →  corner3 (C  0.85, 0.45)   [second 横 going right]
  4. pie   : corner3                  →  tip     (BL 0.30, 0.85)   [撇 tapered down-left]

Joints: three internal P (welded) at corner1, corner2, corner3.
Reuses `fat_line`, `quad_bezier`, `stroke_variable_width` from `_anchor.py`.
Small 顿笔 disc at each welded corner.

Rationale from principle_bank / sandbox:
  - Compound-stroke corners get a 顿笔 reinforcement disc (compound-stroke
    joint convention).
  - The terminal 撇 uses `curve>0` bowing toward the perpendicular of the
    chord, tapered head_w → tail_w = 1 (needle tip). Same rasterizer as
    the promoted `pie.py`.
  - Sanity assertions catch silent geometry bugs before rendering.
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
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_heng_zhe_zhe_pie(draw,
                          head, corner1, corner2, corner3, tip,
                          h_width=10, drop_width=10,
                          pie_head_w=11, pie_tail_w=1,
                          pie_curve=0.10, shoulder=13,
                          color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tip = anchor_to_xy(tip)

    # Sanity assertions (principle_bank: catch silent geometric bugs).
    assert p_c1[0] > p_head[0], "heng1 must go rightward"
    assert p_c2[1] >= p_c1[1] and p_c2[0] < p_c1[0], \
        "折 short drop should move down and slightly left"
    assert p_c3[0] > p_c2[0], "heng2 must go rightward"
    assert p_tip[0] < p_c3[0] and p_tip[1] > p_c3[1], \
        "撇 tip must be down-and-left of pivot"

    # 1) Opening 横.
    fat_line(draw, p_head, p_c1, h_width, color)
    # 2) Short 折 drop (down-left).
    fat_line(draw, p_c1, p_c2, drop_width, color)
    # 3) Second 横.
    fat_line(draw, p_c2, p_c3, h_width, color)

    # 4) Terminal 撇: tapered quad-Bezier, bowed slightly by pie_curve.
    dx, dy = p_tip[0] - p_c3[0], p_tip[1] - p_c3[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    perp = (-dy / length, dx / length)
    bow = pie_curve * length
    mid = ((p_c3[0] + p_tip[0]) / 2.0, (p_c3[1] + p_tip[1]) / 2.0)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pie_pts = quad_bezier(p_c3, ctrl, p_tip, n=48)
    pie_widths = [pie_head_w + (pie_tail_w - pie_head_w) * (i / 48)
                  for i in range(49)]
    stroke_variable_width(draw, pie_pts, pie_widths, color)

    # 顿笔 discs at every welded corner.
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_heng_zhe_zhe_pie(
        draw,
        head    =('TL', 0.35, 0.30),
        corner1 =('TC', 0.85, 0.35),
        corner2 =('C',  0.30, 0.35),
        corner3 =('C',  0.85, 0.45),
        tip     =('BL', 0.30, 0.85),
        h_width=10, drop_width=10,
        pie_head_w=11, pie_tail_w=1, pie_curve=0.10,
        shoulder=13,
    )

    out = os.path.join(os.path.dirname(__file__), '01_横折折撇.png')
    img.save(out)
    print(f"wrote {out} size={img.size}")


if __name__ == '__main__':
    main()
