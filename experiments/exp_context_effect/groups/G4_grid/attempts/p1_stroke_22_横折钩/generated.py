"""p1_stroke_22_横折钩 (héng zhé gōu) — 横折 + hook flick.

Structure: horizontal 横 → 折 corner (welded, 顿笔 disc) → vertical
descent → short hook flick UP-and-LEFT at the tail (like 竖钩's tip).

Composition strategy:
- Reuse `draw_heng_zhe` from Success Bank for the 横 + 折 + vertical
  descent portion (P joint welded at corner, matches batch-1 pass).
- Append a short quadratic-Bezier hook flick from tail up-and-left to
  a needle tip, tapered wide→thin — same technique used by
  `draw_heng_gou` for its hook and by `draw_shu_gou`.

Anchors (米字格, PIL-native y-down):
- head    = ('TL', 0.35, 0.35)   起笔 upper-left
- corner  = ('TR', 0.55, 0.45)   折 point at top-right (顿笔 shoulder)
- tail    = ('BR', 0.55, 0.55)   bottom of vertical descent (hook base)
- tip     = ('BR', 0.20, 0.30)   hook tip, up-and-LEFT of tail

Joints:
- P (welded) at `corner`  — 横→竖 turn, 顿笔 disc reinforces
- internal hook flick at `tail` — not a separate joint, per
  principle_bank convention (hook is part of same primitive)

Sanity invariants (asserted before render):
- p_corner.x > p_head.x  (横 goes rightward)
- p_tail.y   > p_corner.y (descent goes downward)
- p_tip.x    < p_tail.x  (hook flicks LEFT)
- p_tip.y    < p_tail.y  (hook flicks UP)
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Locate the shared Success Bank primitives (read-only import).
_HERE = Path(__file__).resolve()
_BANK = _HERE.parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def draw_heng_zhe_gou(draw, head, corner, tail, tip,
                      h_width=10, v_width=10, shoulder=13,
                      tip_w=2, color=(0, 0, 0)):
    # --- Sanity checks (principle_bank: assert invariants before render).
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)
    p_tip = anchor_to_xy(tip)
    assert p_corner[0] > p_head[0], "横 must go rightward"
    assert p_tail[1] > p_corner[1], "descent must go downward"
    assert p_tip[0] < p_tail[0], "hook must flick LEFT"
    assert p_tip[1] < p_tail[1], "hook must flick UP"

    # --- 横折 body reused from Success Bank primitive.
    draw_heng_zhe(draw, head, corner, tail,
                  h_width=h_width, v_width=v_width, shoulder=shoulder,
                  color=color)

    # --- Hook flick: short Bezier from tail up-and-left, tapered v_width -> tip_w.
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=25)
    hook_widths = [v_width * (1 - i / (len(hook_pts) - 1))
                   + tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    head   = ('TL', 0.35, 0.35)
    corner = ('TR', 0.55, 0.45)
    tail   = ('BR', 0.55, 0.55)
    tip    = ('BR', 0.20, 0.30)

    draw_heng_zhe_gou(draw, head, corner, tail, tip)

    out = _HERE.parent / "01_横折钩.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
