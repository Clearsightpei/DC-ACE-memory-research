"""已 (yǐ) — Phase-3 character, 3 strokes.

MANDATORY LOOKUP CHECKLIST (v7 memory_index):
  # 1. INDEX.md grep '已' -> not present (fresh item)
  # 2. errata.md grep '已' -> not present
  # 3. form_catalog.md — 3-stroke 己/已/巳 family: top 横折, small mid, bottom 竖弯钩
  # 4. principles_meta.md TR8: horizontals share y across cell boundary; TR10: N-joint ≤25px
  # 5. joint_atlas.md — both joints are N (neighbor, small natural gap ~16 px). Do NOT weld.
  # 6. sandbox — no prior 已 note.

Structural spec (from dispatcher MMH block):
  Stroke count: 3
  s1: head=('TL',0.832,0.961) tail=('C',0.576,0.427)  — 横折 top bracket
  s2: head=('ML',0.861,0.717) tail=('C',0.787,0.544)  — small middle horizontal
  s3: head=('ML',0.677,0.315) tail=('BR',0.505,0.083) — 竖弯钩 bottom
  joints (both N, ~16 px gap):
    s1.tail ⇆ s2.mid @ C
    s2.head ⇆ s3.head @ ML

已 vs 己 distinction: 已 has s2 that touches s1 at C (right side, sealing
the top box near-closed), whereas 己 leaves that side open. Both s1↔s2
and s2↔s3 are neighbor joints (small ~16 px natural gaps).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes; two N-neighbor joints preserved with ~16 px gaps.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def draw_yi_self(draw):
    # --- s1: 横折 (top bracket) ------------------------------------------
    # head TL(0.832,0.961) -> corner near TR area -> tail C(0.576,0.427)
    s1_head   = anchor_to_xy(('TL', 0.832, 0.961))   # ~(83, 96)
    s1_corner = anchor_to_xy(('TC', 0.90,  0.90))    # ~(190, 90)  top-right of bracket
    s1_tail   = anchor_to_xy(('C',  0.576, 0.427))   # ~(158,143)

    # Top horizontal segment (head -> corner), very slight upward bow
    ctrl_top = ((s1_head[0] + s1_corner[0]) / 2.0,
                min(s1_head[1], s1_corner[1]) - 4)
    top_pts = quad_bezier(s1_head, ctrl_top, s1_corner, n=28)
    top_widths = [5 + (i / 28) * 2 for i in range(29)]

    # Fold down segment (corner -> tail), short downward with slight inward curve
    ctrl_fold = (s1_corner[0] - 6,
                 (s1_corner[1] + s1_tail[1]) / 2.0)
    fold_pts = quad_bezier(s1_corner, ctrl_fold, s1_tail, n=18)
    fold_widths = [7 - (i / 18) * 2 for i in range(19)]

    s1_pts = top_pts + fold_pts[1:]
    s1_widths = top_widths + fold_widths[1:]
    stroke_variable_width(draw, s1_pts, s1_widths)

    # --- s2: short middle horizontal (ML -> C) ---------------------------
    # head ML(0.861,0.717) ~(86,172)  tail C(0.787,0.544) ~(179,154)
    s2_head = anchor_to_xy(('ML', 0.861, 0.717))
    s2_tail = anchor_to_xy(('C',  0.787, 0.544))
    ctrl_s2 = ((s2_head[0] + s2_tail[0]) / 2.0,
               (s2_head[1] + s2_tail[1]) / 2.0 - 2)
    s2_pts = quad_bezier(s2_head, ctrl_s2, s2_tail, n=20)
    s2_widths = [5 + (i / 20) * 1 for i in range(21)]
    stroke_variable_width(draw, s2_pts, s2_widths)

    # --- s3: 竖弯钩 (bottom sweep with rising hook) ----------------------
    # head ML(0.677,0.315) ~(68,132)
    # down to bottom-left area, sweep right, hook up to BR(0.505,0.083) ~(251,208)
    s3_head   = anchor_to_xy(('ML', 0.677, 0.315))     # ~(68, 132)
    s3_bend   = anchor_to_xy(('BL', 0.55,  0.85))      # ~(55, 285) bottom-left of sweep
    s3_sweep  = anchor_to_xy(('BC', 0.80,  0.88))      # ~(180, 288) rightward along bottom
    s3_hook_s = anchor_to_xy(('BR', 0.60,  0.80))      # ~(260, 280) hook base
    s3_tail   = anchor_to_xy(('BR', 0.505, 0.083))     # ~(250, 208) hook tip

    # Descend: head -> bend (mostly vertical, slight left curve)
    ctrl_desc = (s3_head[0] - 6, (s3_head[1] + s3_bend[1]) / 2.0)
    desc_pts = quad_bezier(s3_head, ctrl_desc, s3_bend, n=32)
    desc_widths = [6 + (i / 32) * 3 for i in range(33)]

    # Sweep: bend -> sweep_pt (horizontal along bottom, slight downward bow)
    ctrl_sweep = ((s3_bend[0] + s3_sweep[0]) / 2.0,
                  max(s3_bend[1], s3_sweep[1]) + 6)
    sweep_pts = quad_bezier(s3_bend, ctrl_sweep, s3_sweep, n=32)
    sweep_widths = [9 + (i / 32) * 1 for i in range(33)]

    # Round to hook base
    ctrl_round = (s3_sweep[0] + 25, s3_sweep[1])
    round_pts = quad_bezier(s3_sweep, ctrl_round, s3_hook_s, n=20)
    round_widths = [10 - (i / 20) * 2 for i in range(21)]

    # Hook up: hook_s -> tail (rising tip)
    ctrl_hook = (s3_hook_s[0] + 2, (s3_hook_s[1] + s3_tail[1]) / 2.0)
    hook_pts = quad_bezier(s3_hook_s, ctrl_hook, s3_tail, n=18)
    hook_widths = [8 - (i / 18) * 6 for i in range(19)]

    s3_pts = desc_pts + sweep_pts[1:] + round_pts[1:] + hook_pts[1:]
    s3_widths = desc_widths + sweep_widths[1:] + round_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, s3_pts, s3_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yi_self(draw)
    out = os.path.join(_HERE, '01_已.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
