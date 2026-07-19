"""p1_stroke_25 — 横折弯钩 (héng zhé wān gōu).

Shape: short 横 across the top → sharp 90° 折 (corner) down → 弯 (curved
descent that swings LEFT as it drops) → short up-and-LEFT 钩 flick at the
bottom. One continuous compound stroke.

Anchors (米字格, PIL-native; y grows DOWN):
  head    = ('TL', 0.30, 0.55)   # 横 起笔, upper-left of top row
  corner  = ('TR', 0.55, 0.55)   # 折 corner, upper-right area
  belly   = ('MR', 0.15, 0.60)   # Bezier control for the 弯 body
                                 #   (stays right early, drifts left near bottom)
  hook_pt = ('BC', 0.55, 0.55)   # end of the curved body / base of hook
  tip     = ('BC', 0.15, 0.25)   # hook tip, up-and-left of hook_pt

Segments:
  1. 横 head → corner (uniform).
  2. 折 shoulder disc at corner (顿笔).
  3. 弯 corner → hook_pt via `belly` control (quad Bezier, variable width).
  4. 钩 hook_pt → tip (short quad Bezier, tapered to needle).

Joint: single compound stroke; internal P (welded) at corner, internal
hook flick at bottom (per principle_bank: hooks are internal, not
declared joints).

Composed from Success Bank primitives:
  - Reuses `_anchor.anchor_to_xy`, `fat_line`, `quad_bezier`,
    `stroke_variable_width` from `_anchor.py`.
  - Structurally: 横折 opening (mirrors `heng_zhe.py`) + 弯钩 tail
    (mirrors `wan_gou.py`). Not calling those primitives directly
    because their signatures don't line up with a shared-corner
    compound; instead reusing the low-level rasterizer helpers as
    `wan_gou.py` and `heng_zhe.py` both do.
"""
import os
import sys

# Make Success Bank primitives importable.
_HERE = os.path.dirname(os.path.abspath(__file__))
_SB = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _SB not in sys.path:
    sys.path.insert(0, _SB)

from PIL import Image, ImageDraw
from _anchor import (
    anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, CANVAS,
)


def draw_heng_zhe_wan_gou(draw, head, corner, belly, hook_pt, tip,
                          h_width=10, v_head_w=10, belly_w=12,
                          hook_start_w=10, tip_w=2, shoulder=13,
                          color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Sanity assertions (per principle_bank: sanity check pixel invariants).
    assert p_corner[0] > p_head[0], "横 must go rightward (corner right of head)"
    assert p_hook[1] > p_corner[1], "弯 body must descend (hook_pt below corner)"
    assert p_tip[0] < p_hook[0], "钩 tip must be LEFT of hook_pt (up-left flick)"
    assert p_tip[1] < p_hook[1], "钩 tip must be ABOVE hook_pt (upward flick)"
    assert p_hook[0] < p_corner[0], (
        "弯 must swing LEFT: hook_pt should end left of the corner column"
    )

    # 1. 横: head → corner (uniform).
    fat_line(draw, p_head, p_corner, h_width, color)

    # 2. 折 shoulder disc (顿笔) at corner.
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)

    # 3. 弯: quad Bezier corner → hook_pt via `belly` control.
    body_pts = quad_bezier(p_corner, p_belly, p_hook, n=60)
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        # Slight thickening near belly, then taper toward hook base.
        if t <= 0.55:
            u = t / 0.55
            w = v_head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color)

    # 4. 钩 flick: short quad Bezier hook_pt → tip, tapered.
    ctrl = (p_hook[0] - (p_hook[0] - p_tip[0]) * 0.3,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.15)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=20)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1))
                   + tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    head    = ('TL', 0.30, 0.55)
    corner  = ('TR', 0.55, 0.55)
    belly   = ('MR', 0.15, 0.60)
    hook_pt = ('BC', 0.55, 0.55)
    tip     = ('BC', 0.15, 0.25)

    draw_heng_zhe_wan_gou(draw, head, corner, belly, hook_pt, tip)

    out = os.path.join(_HERE, '01_横折弯钩.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
