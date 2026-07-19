"""p1_stroke_21_横折弯 (héng zhé wān) — 横 → 90° drop → rounded 弯 to horizontal.

Structure (single compound stroke, three visual parts):
  1. 横 (horizontal top segment): head_h (ML) → corner (MR, top of drop).
  2. 折 press + short vertical descent: corner (MR) → belly (near BR top).
  3. 弯 (rounded rightward bend): belly (BR upper) → tail (BR, horizontal finish).

Distinguishing features vs siblings:
  - vs 横折 (heng_zhe): has an additional rounded 弯 tail (no hook).
  - vs 横折钩 (heng_zhe_gou): 弯 finishes FLAT to the right, no upward hook.
  - vs 竖弯 (shu_wan): begins with a 横 stroke on top before the descent.

Anchors (米字格, PIL-native — y grows DOWN within each cell):
  head_h = ('ML', 0.25, 0.45)   起笔 of 横
  corner = ('MR', 0.55, 0.45)   折 pivot (top of vertical drop)
  belly  = ('MR', 0.55, 0.90)   Bezier control keeping top straight
  bend   = ('BR', 0.20, 0.55)   turning point of the rounded 弯
  tail   = ('BR', 0.80, 0.55)   horizontal finish (flat, no hook)

Joints: P (welded) at corner (横→折), welded round bend at bend (折→弯).

NOTE: Success-bank primitives are LOCKED (imports allowed, no writes).
"""
import os
import sys
from PIL import Image, ImageDraw

# Make the success_bank/code/ helpers importable.
SB_CODE = os.path.normpath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, SB_CODE)

from _anchor import (  # noqa: E402
    anchor_to_xy, quad_bezier, stroke_variable_width, fat_line,
)

CANVAS = 300
OUT_PNG = os.path.join(os.path.dirname(__file__), '01_横折弯.png')


def draw_heng_zhe_wan(draw,
                      head_h, corner, belly, bend, tail,
                      h_width=10, v_head_w=10, v_belly_w=12,
                      bend_w=11, tail_w=9,
                      shoulder=13, color=(0, 0, 0)):
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_b = anchor_to_xy(belly)
    p_bend = anchor_to_xy(bend)
    p_t = anchor_to_xy(tail)

    # Sanity assertions per principle_bank guidance.
    assert p_c[0] > p_h[0], "横 must go left→right (corner right of head)"
    assert p_b[1] > p_c[1], "折 descent must go downward (belly below corner)"
    assert p_t[0] > p_bend[0], "弯 finish must go rightward (tail right of bend)"

    # 1. 横 top segment (uniform).
    fat_line(draw, p_h, p_c, h_width, color)

    # 2. 折 press disc at corner (顿笔).
    r = shoulder / 2.0
    draw.ellipse((p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r), fill=color)

    # 3. 竖 descent corner → bend, via belly control (keeps top straight,
    #    concentrates the round-off near the bend).
    body_pts = quad_bezier(p_c, p_b, p_bend, n=60)
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        if t <= 0.55:
            u = t / 0.55
            w = v_head_w * (1 - u) + v_belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = v_belly_w * (1 - u) + bend_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color)

    # 4. 弯 rounded rightward finish bend → tail. Slight downward-then-flat
    #    curl using a control biased below the chord midpoint.
    ctrl = (p_bend[0] + (p_t[0] - p_bend[0]) * 0.55,
            p_bend[1] + (p_t[1] - p_bend[1]) * 0.25 + 6)
    tail_pts = quad_bezier(p_bend, ctrl, p_t, n=42)
    n = len(tail_pts) - 1
    tail_widths = [bend_w * (1 - i / n) + tail_w * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, tail_pts, tail_widths, color)

    # 5. Flat termination disc (no hook).
    r_t = tail_w / 2.0 + 0.5
    draw.ellipse([p_t[0] - r_t, p_t[1] - r_t,
                  p_t[0] + r_t, p_t[1] + r_t], fill=color)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    draw_heng_zhe_wan(
        draw,
        head_h=('ML', 0.25, 0.45),
        corner=('MR', 0.55, 0.45),
        belly=('MR', 0.55, 0.90),
        bend=('BR', 0.20, 0.55),
        tail=('BR', 0.80, 0.55),
    )

    img.save(OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == '__main__':
    main()
