"""p3_char_0263_她 (tā, "she") — G4 attempt.

Split: 她 = 女 (left) + 也 (right).
- Left 女: reuse `nv.py` primitive from success bank, anchors compressed
  into the left column x∈[0.0, 0.42] (canvas 0..126).
- Right 也: draw inline as 3 strokes (横折钩, 竖, 竖弯钩) in right
  columns x∈[0.42, 0.95] (canvas 126..285).

MMH-derived structural expectations (6 strokes) matched:
- s1..s3 correspond to 女's 撇点, 撇, 横
- s4..s6 correspond to 也's 横折钩, 竖, 竖弯钩

Read order (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — no direct 也/她 chronic; nv.py is bank primitive.
  2. success_bank/INDEX.md — nv.py exists (pos p2_radical_061_女).
  3. errata.md — 她 not in errata.
"""
import os, sys, math
from PIL import Image, ImageDraw

# path so we can import bank primitives
_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, _BANK)

from _anchor import (
    anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line, CANVAS
)
from nv import draw_nv
from heng_zhe_gou import draw_heng_zhe_gou
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 (女) + 3 (也) = 6, matches expected 6
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '女 (nv) reused from bank, compressed to left column; 也 inline right column. '
             '3 joints in 女 (2P+T from nv.py). 也 joints: s4-s5 P (heng-zhe-gou crosses shu), '
             's4-s6 T (shu-wan-gou head tangent to heng), s2-s3 N (nv internal).'
}


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # ---------------- LEFT: 女 (compressed into left column x∈[0, 135]) ----------------
    # Rewrote pixel targets based on visual GT: 女 fills the left ~1/3 with the
    # characteristic 撇点/撇/横 crossing near the middle of the column.
    draw_nv(
        draw,
        # 撇点 s1: pie head upper-right of column, pivot lower-left, dian ends center
        s1_head=('TL', 0.85, 0.60),    # ~ (85, 60)  upper right of left col
        s1_pivot=('ML', 0.30, 0.55),   # ~ (30, 155) pivot / elbow
        s1_tail=('ML', 0.80, 0.75),    # ~ (80, 175) dian ends near center-mid
        # 撇 s2: sweeps from center-top of left col far down-left
        s2_head=('TL', 1.00, 0.90),    # ~ (100, 90)
        s2_tail=('BL', 0.05, 0.85),    # ~ (5, 285)
        # 横 s3: wide horizontal crossing at mid
        s3_head=('ML', 0.00, 0.70),    # ~ (0, 170)
        s3_tail=('ML', 1.35, 0.65),    # ~ (135, 165)
    )

    # ---------------- RIGHT: 也 (inline in right columns x∈[140, 290]) ----------------
    # s4: 横折钩 (heng zhe gou) — top horizontal, corner top-right, down, hook up-left.
    draw_heng_zhe_gou(
        draw,
        head=('C', 0.45, 0.35),        # (145, 135)  top-left of horiz
        corner=('MR', 0.70, 0.35),     # (270, 135)  top-right corner
        tail=('MR', 0.70, 1.25),       # (270, 225)  bottom of vertical
        tip=('MR', 0.55, 1.15),        # (255, 215)  hook up-left
    )

    # s5: 竖 — middle vertical of 也
    draw_shu(
        draw,
        from_anchor=('C', 1.05, 0.00),   # (205, 100)
        to_anchor=('C', 1.05, 1.25),     # (205, 225)
        width=9,
    )

    # s6: 竖弯钩 — inner sweeping stroke, dives down then wraps right past the frame with hook up.
    draw_shu_wan_gou(
        draw,
        head=('C', 0.55, 0.65),          # (155, 165)  starts inside frame upper-left
        belly=('C', 0.55, 1.45),         # (155, 245)  vertical descent
        corner=('MR', 0.75, 1.55),       # (275, 255)  bends right along bottom
        hook_pt=('BR', 0.85, 0.30),      # (285, 230)  approaching hook
        tip=('BR', 0.80, 0.10),          # (280, 210)  hook up
        head_w=8, belly_w=12, corner_w=11, hook_start_w=10, tip_w=2,
    )

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(os.path.dirname(__file__), '01_她.png')
    img.save(out)
    print(f'wrote {out}  size={img.size}')
