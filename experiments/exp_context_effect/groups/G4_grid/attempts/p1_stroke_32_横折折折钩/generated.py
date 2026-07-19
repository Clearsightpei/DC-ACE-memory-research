"""p1_stroke_32_横折折折钩 (héng zhé zhé zhé gōu)

The canonical five-phase compound stroke found in characters like 乃 and 及.
Trace: short 横 → 折 down → short 横 back-right/slant → 折 down → longer
vertical/curving descent → hook flick UP-and-LEFT at the tail.

Composition strategy:
- Reuse the batch-1 staircase pattern from `p1_stroke_30_横折折折`
  (fat_line segments + 顿笔 shoulder disc at every welded corner).
- Append a hook flick at the tail using the same technique as
  `heng_gou.py` / `p1_stroke_22_横折钩` (short tapered quad-Bezier
  from tail up-and-left to a needle tip).

Segments (all welded at declared corners, small 顿笔 disc at each):
  1. 横 head A → corner1 B         (rightward)
  2. 竖 (short) B → corner2 C      (downward)
  3. 横 C → corner3 D              (rightward, slightly longer)
  4. 竖 D → tail E                 (downward, longest)
  5. hook flick E → tip F          (UP-and-LEFT, needle tip)

Joints:
  seg1.tail @ B ⇆ seg2.head @ B   (P — welded, shoulder disc)
  seg2.tail @ C ⇆ seg3.head @ C   (P — welded, shoulder disc)
  seg3.tail @ D ⇆ seg4.head @ D   (P — welded, shoulder disc)
  seg4.tail @ E ⇆ hook.head @ E   (internal, part of same primitive — per
                                    principle_bank "hook is not a joint")

Anchors (米字格, PIL-native y-down convention):
  head    A = ('TL', 0.55, 0.60)   起笔 upper-left, y≈60
  corner1 B = ('TC', 0.90, 0.60)   after 横 segment
  corner2 C = ('C',  0.20, 0.30)   after short 竖 down
  corner3 D = ('MR', 0.55, 0.30)   after 横 (slightly longer)
  tail    E = ('BR', 0.55, 0.55)   bottom of long descent (hook base)
  tip     F = ('BR', 0.20, 0.30)   hook tip, up-and-LEFT of tail

Sanity invariants (asserted before render, per principle_bank):
  - Segment directions: seg1→right, seg2→down, seg3→right, seg4→down.
  - Hook flick: tip.x < tail.x AND tip.y < tail.y (up-and-left).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Locate the shared Success Bank primitives (read-only import).
_HERE = Path(__file__).resolve()
_BANK = _HERE.parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa: E402


CANVAS = 300
H_WIDTH = 10
V_WIDTH = 10
SHOULDER = 13
TIP_W = 2


def draw_heng_zhe_zhe_zhe_gou(draw, head, corner1, corner2, corner3, tail, tip,
                              h_width=H_WIDTH, v_width=V_WIDTH,
                              shoulder=SHOULDER, tip_w=TIP_W,
                              color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tail = anchor_to_xy(tail)
    p_tip = anchor_to_xy(tip)

    # --- Sanity assertions (principle_bank: catch silent geometric bugs). ---
    assert p_c1[0] > p_head[0], "seg1 must go right (head→c1)"
    assert p_c2[1] > p_c1[1],   "seg2 must go down  (c1→c2)"
    assert p_c3[0] > p_c2[0],   "seg3 must go right (c2→c3)"
    assert p_tail[1] > p_c3[1], "seg4 must go down  (c3→tail)"
    assert p_tip[0] < p_tail[0], "hook must flick LEFT"
    assert p_tip[1] < p_tail[1], "hook must flick UP"

    # --- Four fat-line segments (reuse of stroke-30 pattern). ---
    fat_line(draw, p_head, p_c1,   h_width, color)
    fat_line(draw, p_c1,   p_c2,   v_width, color)
    fat_line(draw, p_c2,   p_c3,   h_width, color)
    fat_line(draw, p_c3,   p_tail, v_width, color)

    # --- 顿笔 shoulder discs at every welded corner (P joints). ---
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)

    # --- Hook flick: short tapered Bezier from tail up-and-left. ---
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=25)
    hook_widths = [v_width * (1 - i / (len(hook_pts) - 1))
                   + tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 米字格 anchors — staircase descending toward BR, then hook flick.
    #
    # Pixel layout (each cell = 100x100, PIL y-down):
    #   A(55,60)   ─── B(190,60)          seg1 横, y=60
    #                    │                 seg2 竖, x=190, y: 60→130
    #                    C(120,130) ── D(255,130)  seg3 横, y=130
    #                                     │         seg4 竖, x=255, y: 130→255
    #                                     E(255,255)
    #                                     │
    #                                     ↖ tip F(220,230)  hook up-left
    head    = ('TL', 0.55, 0.60)   # px= 55, py= 60
    corner1 = ('TC', 0.90, 0.60)   # px=190, py= 60
    corner2 = ('C',  0.20, 0.30)   # px=120, py=130
    corner3 = ('MR', 0.55, 0.30)   # px=255, py=130
    tail    = ('BR', 0.55, 0.55)   # px=255, py=255
    tip     = ('BR', 0.20, 0.30)   # px=220, py=230

    draw_heng_zhe_zhe_zhe_gou(draw, head, corner1, corner2, corner3, tail, tip)

    out_path = _HERE.parent / "01_横折折折钩.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
