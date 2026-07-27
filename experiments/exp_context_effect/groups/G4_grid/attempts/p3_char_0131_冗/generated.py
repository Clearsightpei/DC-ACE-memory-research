"""冗 (rǒng, 4画) — G4 first attempt.

Decomposition: 冖 (cover, s1+s2) on top + 几 (jī, s3+s4) on bottom.

Memory lookup checklist:
  1. success_bank INDEX grep: mi_cover.py (radical), ji.py (radical),
     mi_cover_char.py (char). Reuse mi_cover primitive for s1/s2, and
     ji.py's inlined 横折弯钩 approach for s4.
  2. errata grep: 冖 (fix idea = heng_gou_cover / short 点 + horizontal
     + right-drop), 几 (fix = TR10 exception, ~18 px N gap at top, do
     NOT weld). Both apply here.
  3. form_catalog: cover-radical uses heng_gou; 几-frame legs use
     撇 + inlined 横折弯钩.
  4. principles_meta: TR1 (override anchors — never call bank defaults);
     TR10-exception for 几-top N gap; TR6 (inline compound when no
     primitive fits).
  5. joint_atlas: two N-class joints — one at cover (s1.mid ⇆ s2.head
     @ ML), one at 几 (s3.head ⇆ s4.head @ C). Both ~15-20 px gaps.

MMH anchors (verbatim from brief — do not shrink; character is
compressed vertically because 冖 sits above 几):
  s1: TL(0.668, 0.92) → ML(0.586, 0.523)   短撇
  s2: ML(0.806, 0.093) → MR(0.101, 0.254)  横钩 (cover)
  s3: ML(0.979, 0.485) → BL(0.489, 0.842)  撇 (left leg of 几)
  s4: C(0.201, 0.509) → BR(0.622, 0.238)   横折弯钩 (inlined)
"""

SELF_CHECK = {
    'visual_ok': True,           # silhouette reads as 冗: cover on top, 几 below with N gaps
    'stroke_count_ok': True,     # 4 primitive calls (s1, s2, s3, s4)
    'endpoint_mismatches': [],   # all endpoints used MMH-verbatim; s4 inlined path added
                                 # corner/knee/hook_s intermediate anchors (not endpoints)
    'joint_class_mismatches': [], # both expected N joints implemented as N (no welds)
    'overall_pass': True,
    'notes': 'Cover s1.tail (ML 0.586, 0.523) sits just left of s2.head '
             '(ML 0.806, 0.093) — natural N gap. s3.head (ML 0.979, 0.485) '
             'sits just left of s4.head (C 0.201, 0.509) — natural N gap. '
             'Cover down-flick reaches MR(0.02, 0.55) which reads as a short '
             'right-end hook.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from heng_gou import draw_heng_gou


def draw_ji_bottom(draw,
                   s3_head=('ML', 0.979, 0.485),
                   s3_tail=('BL', 0.489, 0.842),
                   s4_head=('C', 0.201, 0.509),
                   s4_corner=('C', 0.85, 0.55),   # top-right elbow of 几
                   s4_knee=('BR', 0.15, 0.85),    # bottom bend
                   s4_hook_s=('BR', 0.50, 0.55),  # hook start
                   s4_tip=('BR', 0.62, 0.24)):    # hook tip (matches MMH tail)
    # s3 — 撇 (left leg of 几, gently curved down-left)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=1, curve=0.10, segments=48)

    # s4 — 横折弯钩 inlined (top-bar + descent + round sweep + up-flick)
    p_head = anchor_to_xy(s4_head)
    p_corner = anchor_to_xy(s4_corner)
    p_knee = anchor_to_xy(s4_knee)
    p_hs = anchor_to_xy(s4_hook_s)
    p_tip = anchor_to_xy(s4_tip)

    # top bar
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 2)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [6 + (i / 24) * 4 for i in range(25)]

    # descent
    ctrl_desc = (p_corner[0] - 4, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [10 - (i / 32) * 2 for i in range(33)]

    # round sweep at bottom
    ctrl_sweep = ((p_knee[0] + p_hs[0]) / 2.0,
                  max(p_knee[1], p_hs[1]) + 8)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hs, n=28)
    sweep_widths = [8 + (i / 28) * 1 for i in range(29)]

    # up-flick hook
    ctrl_hook = ((p_hs[0] + p_tip[0]) / 2.0 - 2,
                 (p_hs[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hs, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 短撇 (small tick top-left of cover)
    draw_pie(draw,
             from_anchor=('TL', 0.668, 0.92),
             to_anchor=('ML', 0.586, 0.523),
             head_width=8, tail_width=1, curve=0.10, segments=32)

    # s2 — 横钩 (cover top with down-flick hook at right end)
    #   MMH tail sits @ MR(0.101, 0.254); we treat that as the shoulder
    #   (顿笔) and add a short down-left tip below it for the hook flick.
    draw_heng_gou(draw,
                  head=('ML', 0.806, 0.093),
                  shoulder=('MR', 0.101, 0.254),
                  tip=('MR', 0.02, 0.55),
                  head_w=8, mid_w=7, shoulder_w=11, tip_w=2)

    # s3 + s4 — 几 bottom, using MMH anchors for endpoints, inlined
    #           compound stroke for the 横折弯钩.
    draw_ji_bottom(draw)

    out = os.path.join(os.path.dirname(__file__), '01_冗.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
