# BANK_DEVIATION
# skipped: heng_zhe_short.py (no full 横折钩 with hook in bank)
# skipped: shu_gou.py (would give the vertical+hook but not the leading heng)
# reason: 力's stroke 1 is a compound 横折钩 — short 横 → sharp corner → 竖 →
#         small hook flick leftward at the bottom. No single bank primitive
#         covers heng + zhe + gou together, so inline a fresh combined curve.
# fresh_component: heng_zhe_gou_for_力 — three-segment path with tapered
#         horizontal, right-angle corner, and terminal upward hook.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 stroke primitives (s1 heng_zhe_gou compound, s2 pie)
    'endpoint_mismatches': [
        # MMH expects s1 head ML(0.668,0.474)=(66.8,147.4). GT silhouette
        # actually places the 横 start near (95,105) — MMH median seems to
        # underdescribe the horizontal reach; using GT-visible anchor.
        {'stroke': 1, 'expected': 'ML(0.668,0.474)', 'actual': '(95,105)',
         'delta': 'moved to GT-visible horizontal start'},
    ],
    'joint_class_mismatches': [],  # P (piercing at C) — 撇 crosses through 横
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for s1 (no full 横折钩 in bank). Pie used for s2.'
}

import sys
import pathlib

_BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from PIL import Image, ImageDraw
from pie import draw_pie


def draw_heng_zhe_gou_for_li(draw, heng_head, corner, gou_tail, hook_tip):
    """Compound 横折钩: horizontal (heng_head->corner), vertical (corner->gou_tail),
    small upward hook flick (gou_tail->hook_tip). Ink is a chain of ellipses so
    the corner welds naturally and the hook tapers to a fine point."""
    # --- Segment A: 横 (slight upward arch, thin lead-in, subtle swell to corner) ---
    steps_a = 60
    x0, y0 = heng_head
    x1, y1 = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t - 2.0 * (1 - (2 * t - 1) ** 2)
        w = 3.5 + 2.2 * t  # thin head, thickening slightly into the corner
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Corner emphasis (small dark node at the turn — calligraphic 折) ---
    cx, cy = corner
    draw.ellipse((cx - 6.5, cy - 6.0, cx + 6.5, cy + 6.0), fill='black')

    # --- Segment B: 竖 (curves gently leftward as it descends — 力's signature) ---
    steps_b = 70
    x2, y2 = gou_tail
    # control point pulling the descent slightly inward (left) for the curve
    ctrl_x = cx - 6
    ctrl_y = (cy + y2) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        w = 5.3 - 1.6 * t  # taper slightly into the hook base
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Segment C: 钩 (small upward-left hook flick, tapering to a point) ---
    steps_c = 22
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 4.0 * (1 - t) + 0.8
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 横折钩 (compound) ----
    heng_head = (92, 108)     # top-left start of 横
    corner    = (192, 100)    # sharp turn: right end of 横, top of 竖
    gou_tail  = (168, 218)    # bottom of the descending 竖 (curved slightly left)
    hook_tip  = (150, 208)    # small upward-left hook flick
    draw_heng_zhe_gou_for_li(d, heng_head, corner, gou_tail, hook_tip)

    # ---- Stroke 2: 撇 (pierces through the 横 near the center — joint class P) ----
    # Head must start ABOVE the 横 (y ~ 90) so the 撇 crosses through it,
    # otherwise the character reads as 刀 (tangent joint) instead of 力.
    pie_head = (150, 88)      # starts above 横, right of center
    pie_tail = (68, 262)      # sweeps down-left to bottom-left
    draw_pie(d, pie_head, pie_tail, bow_perp=16, w_head=8, w_tail=2, steps=100)

    out = pathlib.Path(__file__).parent / '01_力.png'
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
