"""p1_stroke_24_横撇弯钩 — attempt.

横撇弯钩 (héng piě wān gōu) is a compound stroke of FOUR segments:
  1. 横 — a short horizontal at the top.
  2. 撇 — a short diagonal descent down-and-to-the-left from the
         end of the 横 (welded pivot).
  3. 弯 — a curved body sweeping down-then-out (concave-left arc),
         basically the belly of a 弯钩.
  4. 钩 — a short up-and-left hook flick at the bottom.

Occurs in characters like 阝 (as in 队/防/阳) and 那/邓.

Approach: draw the 横 as a fat_line; add a 撇 tapered segment
(corner → knee) with a 顿笔 disc at the corner; then a 弯 body Bezier
knee → hook_pt with a belly control (like wan_gou); then a short
hook flick hook_pt → tip. Anchors chosen so the whole stroke reads
top-right → bottom-center, with the leftward hook flick.
"""
import os
import sys
from PIL import Image, ImageDraw

# Import the shared anchor helper + primitives from the success bank.
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _anchor import (
    anchor_to_xy,
    quad_bezier,
    stroke_variable_width,
    fat_line,
    sample_line,
)


def draw_heng_pie_wan_gou(draw,
                          head_h, corner, knee, belly, hook_pt, tip,
                          h_width=8,
                          corner_shoulder=12,
                          pie_head_w=11, pie_knee_w=8,
                          knee_shoulder=11,
                          wan_head_w=8, wan_belly_w=12,
                          hook_start_w=11, tip_w=2,
                          color=(0, 0, 0)):
    """横撇弯钩 — 4-segment compound: 横 → 撇 → 弯 → 钩.

    Anchors:
      head_h   — 起笔 of the 横 (upper-left of the top bar, TC region).
      corner   — end of the 横 / start of the 撇 (顿笔; TR region).
      knee     — end of the 撇 / start of the 弯 (below and left of
                 corner, near ML/C boundary).
      belly    — Bezier control for the 弯 body (bowed rightward-down
                 for the outward-swinging arc).
      hook_pt  — end of the 弯 body / start of the hook (BC region).
      tip      — hook tip, up-and-left of hook_pt.

    Joints (internal to this single compound stroke):
      P (welded) at `corner` between 横 and 撇.
      P (welded) at `knee`   between 撇 and 弯.
      Internal hook at `hook_pt` (no external joint).
    """
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_b = anchor_to_xy(belly)
    p_hk = anchor_to_xy(hook_pt)
    p_t = anchor_to_xy(tip)

    # Sanity assertions — direction invariants (see principle_bank).
    assert p_c[0] > p_h[0], '横 must run left→right (corner right of head)'
    assert p_k[0] < p_c[0] and p_k[1] > p_c[1], '撇 must go down-left from corner'
    assert p_hk[1] > p_k[1], '弯 body must descend below knee'
    assert p_t[1] < p_hk[1] and p_t[0] < p_hk[0], 'hook flick must go up-and-left'

    # 1. 横 — uniform short horizontal.
    fat_line(draw, p_h, p_c, h_width, color)

    # 2. 顿笔 disc at the 横→撇 corner.
    r = corner_shoulder / 2.0
    draw.ellipse((p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r), fill=color)

    # 3. 撇 — mild left-bowed tapered segment corner → knee.
    mx = (p_c[0] + p_k[0]) / 2.0
    my = (p_c[1] + p_k[1]) / 2.0
    dx = p_k[0] - p_c[0]
    dy = p_k[1] - p_c[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    perp = (-dy / length, dx / length)  # left-perp of down-left chord bows outward-down
    bow = length * 0.05
    pie_ctrl = (mx + perp[0] * bow, my + perp[1] * bow)
    pie_pts = quad_bezier(p_c, pie_ctrl, p_k, n=30)
    pie_widths = []
    for i in range(len(pie_pts)):
        t = i / (len(pie_pts) - 1)
        eased = t ** 1.2
        pie_widths.append(pie_head_w * (1 - eased) + pie_knee_w * eased)
    stroke_variable_width(draw, pie_pts, pie_widths, color)

    # 4. 顿笔 disc at the 撇→弯 knee.
    r = knee_shoulder / 2.0
    draw.ellipse((p_k[0] - r, p_k[1] - r, p_k[0] + r, p_k[1] + r), fill=color)

    # 5. 弯 body — quad Bezier knee → hook_pt via belly (raw control).
    body_pts = quad_bezier(p_k, p_b, p_hk, n=60)
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        if t <= 0.55:
            u = t / 0.55
            w = wan_head_w * (1 - u) + wan_belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = wan_belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color)

    # 6. 钩 flick — short quad Bezier hook_pt → tip, tapered to needle.
    hook_ctrl = (p_hk[0] - (p_hk[0] - p_t[0]) * 0.3,
                 p_hk[1] + (p_t[1] - p_hk[1]) * 0.15)
    hook_pts = quad_bezier(p_hk, hook_ctrl, p_t, n=20)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1))
                   + tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Anchor plan — position the compound roughly in the right half of the
    # canvas so the shape reads as the right-hand descending compound
    # stroke it is (as in 阝, 队, 邓 territory).
    #   head_h  TC (0.35, 0.35)  — starts high, slightly left of TC center
    #   corner  TR (0.35, 0.40)  — 横 runs across cell boundary into TR
    #   knee    C  (0.25, 0.55)  — end of a short 撇 down-and-left
    #   belly   C  (0.75, 0.90)  — control point pulled down-right (outward
    #                              bow of the 弯 body)
    #   hook_pt BC (0.55, 0.55)  — bottom of the arc, near BC
    #   tip     BC (0.15, 0.15)  — hook tip up-and-left of hook_pt
    head_h  = ('TC', 0.35, 0.35)
    corner  = ('TR', 0.35, 0.40)
    knee    = ('C',  0.25, 0.55)
    belly   = ('C',  0.75, 0.90)
    hook_pt = ('BC', 0.55, 0.55)
    tip     = ('BC', 0.15, 0.15)

    draw_heng_pie_wan_gou(draw, head_h, corner, knee, belly, hook_pt, tip)

    out = os.path.join(os.path.dirname(__file__), '01_横撇弯钩.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
