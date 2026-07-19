"""p1_stroke_23_竖弯钩 (shù wān gōu) — vertical descent, rounded turn to
horizontal, ending in a short upward hook.

Composition (grid-bank / G4):
  = 竖弯 (shu_wan) body + tail, but with the rightward tail terminated by
    a short upward hook flick (gou) instead of a flat termination.

Anchors (米字格, PIL-native — y grows DOWN within each cell):
  head    ('TC', 0.50, 0.05)   — 起笔 near top of TC.
  belly   ('C',  0.50, 0.70)   — Bezier control on the vertical column;
                                  keeps the top straight and concentrates
                                  the bend near the bottom.
  corner  ('BC', 0.30, 0.85)   — turning point at the bottom, slightly
                                  left of center in BC.
  hook_pt ('BR', 0.55, 0.80)   — end of horizontal sweep, where the hook
                                  flick begins.
  tip     ('BR', 0.55, 0.35)   — hook tip, directly ABOVE hook_pt (short,
                                  sharp upward flick — the 钩 signature).

Joint: single compound stroke.
  - Internal welded bend at `corner` (竖 → 弯 sweep, 顿笔 disc reinforces
    the join).
  - Internal hook flick from hook_pt → tip (per principle_bank: hooks
    inside a compound-stroke primitive are NOT declared as external
    joints).

Rationale drawn from principle_bank + sandbox:
  - Use `belly` as raw Bezier control (verified crisp in 07 弯钩,
    13 竖弯); do NOT derive control via `2*belly - midpoint` (16/19
    hazard).
  - Concentrate the bend in the lower third; if x_frac drifts left in
    the upper half the stroke reads as 撇.
  - Hook flick is short and sharp: length ~30% of tail sweep, upward
    direction (tip.y < hook_pt.y).
  - Width profile: taper up head→belly (顿笔 press mid-lower), corner
    slightly narrower than belly, then taper down through the hook to
    near-zero tip.

Sanity assertions before rendering (per principle_bank recommendation):
  - hook flick must point UP: p_tip.y < p_hook.y.
  - Sweep goes rightward past corner: p_hook.x > p_corner.x.
  - Body stays roughly vertical through the upper half: |p_belly.x -
    p_head.x| small compared to canvas width.
"""

import sys
import os
from PIL import Image, ImageDraw

# Import shared primitives from the success_bank/code/ package (READ ONLY).
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402


def draw_shu_wan_gou(draw, head, belly, corner, hook_pt, tip,
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2,
                     color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_corner = anchor_to_xy(corner)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Sanity assertions (principle_bank guidance).
    assert p_tip[1] < p_hook[1], "hook flick must point upward"
    assert p_hook[0] > p_corner[0], "sweep must extend rightward past corner"
    assert abs(p_belly[0] - p_head[0]) < 40, \
        "belly x should stay near head x (keep upper body vertical)"

    # ---- Body: head → corner via belly (raw Bezier control). ----
    body_pts = quad_bezier(p_head, p_belly, p_corner, n=60)
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        if t <= 0.55:
            u = t / 0.55
            w = head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + corner_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color)

    # ---- Tail: rounded rightward sweep corner → hook_pt. ----
    ctrl = (p_corner[0] + (p_hook[0] - p_corner[0]) * 0.55,
            p_corner[1] + (p_hook[1] - p_corner[1]) * 0.25 + 6)
    tail_pts = quad_bezier(p_corner, ctrl, p_hook, n=40)
    tail_widths = [corner_w * (1 - i / (len(tail_pts) - 1))
                   + hook_start_w * (i / (len(tail_pts) - 1))
                   for i in range(len(tail_pts))]
    stroke_variable_width(draw, tail_pts, tail_widths, color)

    # 顿笔 reinforcement disc at hook_pt (base of the hook flick).
    r = hook_start_w / 2.0 + 1.0
    draw.ellipse([p_hook[0] - r, p_hook[1] - r,
                  p_hook[0] + r, p_hook[1] + r], fill=color)

    # ---- Hook flick: hook_pt → tip (short, sharp, upward). ----
    # Slight leftward pull on control so the hook curls in slightly
    # (calligraphic feel), while tip stays essentially above hook_pt.
    hook_ctrl = (p_hook[0] - 4,
                 p_hook[1] + (p_tip[1] - p_hook[1]) * 0.35)
    hook_pts = quad_bezier(p_hook, hook_ctrl, p_tip, n=24)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1))
                   + tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_shu_wan_gou(
        draw,
        head=('TC', 0.50, 0.05),
        belly=('C',  0.50, 0.70),
        corner=('BC', 0.30, 0.85),
        hook_pt=('BR', 0.55, 0.80),
        tip=('BR', 0.55, 0.35),
    )

    out = os.path.join(os.path.dirname(__file__), "01_竖弯钩.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
