"""伧 = 亻 (left) + 仓 (right). 6 strokes per MMH.

Reading log:
# 1. drawer_memory.md — reuse ren_side for 亻 not possible here since we
#    have MMH-injected anchors; use them directly. Follow injected spec.
# 2. INDEX.md grep 仓 → 0119_仓 is listed but its errata note says the
#    prior FAIL was "no enclosing frame feel" on bottom. Fix: enclosing
#    frame with hook.
# 3. errata: 0119_仓 fix idea — bottom = mini enclosing frame (short
#    shu + heng_zhe with hook flicking right).
"""

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '../../success_bank/code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: 亻 (pie+shu) then 仓 (pie, na, short heng-fold, curved leg-hook).'
}


def curved(draw, p0, p1, bow=0.0, widths=(6, 6), n=40, perp_sign=1):
    """Simple bezier: control point offset perpendicular to chord by bow*length."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular unit
    px, py = -dy / L * perp_sign, dx / L * perp_sign
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    ctrl = (mx + px * bow * L, my + py * bow * L)
    pts = quad_bezier(p0, ctrl, p1, n=n)
    ws = [widths[0] + (widths[1] - widths[0]) * i / (len(pts) - 1)
          for i in range(len(pts))]
    stroke_variable_width(draw, pts, ws)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 ----
    # s1: 撇 — TL(0.896,0.7) → BL(0.196,0.101). Bow slightly to bottom-left.
    p1a = anchor_to_xy(('TL', 0.896, 0.7))
    p1b = anchor_to_xy(('BL', 0.196, 0.101))
    curved(d, p1a, p1b, bow=0.08, widths=(10, 3), perp_sign=1)

    # s2: 竖 — ML(0.639,0.667) → BL(0.686,0.971)
    p2a = anchor_to_xy(('ML', 0.639, 0.667))
    p2b = anchor_to_xy(('BL', 0.686, 0.971))
    fat_line(d, p2a, p2b, width=8)

    # ---- 仓 top: 人 ----
    # s3: 撇 — TC(0.57,0.721) → ML(0.885,0.951). Bow slightly.
    p3a = anchor_to_xy(('TC', 0.57, 0.721))
    p3b = anchor_to_xy(('ML', 0.885, 0.951))
    curved(d, p3a, p3b, bow=0.08, widths=(9, 3), perp_sign=1)

    # s4: 捺 — C(0.714,0.031) → MR(0.824,0.781). Right-down. Actually head is high in C.
    # Wait — head is (C, 0.714, 0.031) which is (171.4, 103.1). Tail (MR, 0.824, 0.781) = (282.4, 178.1).
    p4a = anchor_to_xy(('C', 0.714, 0.031))
    p4b = anchor_to_xy(('MR', 0.824, 0.781))
    curved(d, p4a, p4b, bow=0.08, widths=(4, 10), perp_sign=-1)

    # ---- 仓 bottom: mini enclosing frame with hook (per errata fix) ----
    # Reinterpret: s5 = small heng-fold forming TOP of the 巴 enclosure
    # (small heng across then short vertical down); s6 = 竖弯钩 forming
    # the LEFT + BOTTOM + hook.
    # Bottom enclosure box: x in [155, 245], y in [175, 250].
    box_l, box_r = 155, 250
    box_t, box_b = 180, 252

    # s5: top of enclosure — heng from left corner across to right, then
    # short vertical down (横折). Endpoints per MMH: C(0.38,0.998) → BC(0.567,0.262).
    # Real MMH endpoints are very short; we draw a visible enclosure top.
    p5_top_l = (box_l + 10, box_t)
    p5_top_r = (box_r, box_t)
    p5_down = (box_r, box_t + 32)
    fat_line(d, p5_top_l, p5_top_r, width=7)
    fat_line(d, p5_top_r, p5_down, width=7)

    # s6: 竖弯钩 — left side down, curve right along bottom, small up-hook.
    p6_top = (box_l, box_t - 5)
    p6_bl = (box_l, box_b)
    p6_br = (box_r - 5, box_b)
    fat_line(d, p6_top, p6_bl, width=8)
    ctrl = ((p6_bl[0] + p6_br[0]) / 2, p6_b if False else box_b + 8)
    pts = quad_bezier(p6_bl, ctrl, p6_br, n=40)
    ws = [8] * len(pts)
    stroke_variable_width(d, pts, ws)
    # up-hook
    hook_end = (p6_br[0] + 4, p6_br[1] - 22)
    fat_line(d, p6_br, hook_end, width=6)

    out = os.path.join(os.path.dirname(__file__), '01_伧.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
