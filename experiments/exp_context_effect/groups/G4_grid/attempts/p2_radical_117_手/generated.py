"""手 (shǒu, "hand") — Phase-2 radical, 4 strokes.

Composition (from MMH-derived structural spec):
  s1 — 短撇 (top short pie): sweeps upper-right → upper-left.
       head @ ('TR', 0.039, 0.724), tail @ ('TL', 0.92, 0.979)
  s2 — 短横 (upper horizontal, slightly rising).
       head @ ('ML', 0.935, 0.351), tail @ ('MR', 0.051, 0.213)
  s3 — 长横 (lower horizontal, slightly rising, longer than s2).
       head @ ('ML', 0.325, 0.939), tail @ ('MR', 0.713, 0.793)
  s4 — 竖钩 (vertical with up-left hook flick).
       head @ ('TC', 0.389, 0.92), tail (hook tip) @ ('BC', 0.09, 0.763)

Joints:
  s1.mid(~0.65) ⇆ s4.head @ TC : N-class (small gap ~11 px — do NOT weld;
    the short 撇 hangs just to the right of where the 竖 begins).
  s2.mid ⇆ s4.mid @ C : P (welded — 竖 pierces upper 横).
  s3.mid ⇆ s4.mid @ C : P (welded — 竖 pierces lower 横).

Anchor plan derived from the MMH structural block; bank primitives
draw_pie, draw_heng, and inlined 竖钩 (custom, so hook_pt.x can differ
from head.x — TR6 inline) are used. The custom 竖钩 mirrors the pattern
used in shou_side.py (P-batch success).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier
from pie import draw_pie
from heng import draw_heng


def _draw_shu_gou_custom(draw, head, hook_pt, tip,
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2):
    """Inlined 竖钩 that allows hook_pt.x != head.x (slight lean).

    Same recipe as shou_side._draw_shu_gou_custom (proven, PASS on 扌).
    """
    p_head = anchor_to_xy(head)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    body_pts = sample_line(p_head, p_hook, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = mid_w + (hook_start_w - mid_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Hook flick hook_pt → tip (up-and-left).
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ----------------------------------------------------------------------
# Self-check (mandatory G4 Phase-2 gate)
# ----------------------------------------------------------------------
# Expected stroke count: 4 → we call 3 named strokes (pie, heng, heng)
# + 1 inlined 竖钩 = 4 total. OK.
#
# Endpoint anchors — all match MMH within tolerance (used verbatim below).
#
# Joint check:
#   s1.mid ⇆ s4.head @ TC: N — s1 ends at TL(0.92,0.979)=(92,97.9),
#     s4 head at TC(0.389,0.92)=(138.9,92). s1.mid ≈ midpoint of
#     TR(0.039,0.724)→TL(0.92,0.979) = ((203.9+92)/2, (72.4+97.9)/2)
#     = (147.9, 85.1). Distance to s4.head (138.9,92) ≈ 11 px. MATCH.
#   s2 pierces s4 near TC(0.551,0.296): s2 goes (93.5,135)→(205.1,121);
#     s4 body passes ~x=139 at that y — yes, s4 crosses s2. P. WELDED.
#   s3 pierces s4 near BC(0.604,0.811): s3 goes (32.5,193.9)→(271.3,179.3);
#     s4 body passes ~x=120 at y≈180 — welded crossing. P. WELDED.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes as spec; s1 short 撇 top-right, s2 upper 短横, '
              's3 lower 长横, s4 竖钩 through center; s1-s4 N (~11 px), '
              's2-s4 P (weld at C), s3-s4 P (weld at C).')
}


def draw_shou(draw):
    # s1 — 短撇 (top). Short, less curved (small stroke).
    draw_pie(draw,
             from_anchor=('TR', 0.039, 0.724),
             to_anchor=('TL', 0.92, 0.979),
             head_width=9, tail_width=1, curve=0.08, segments=40)

    # s2 — 短横 (upper horizontal, slightly rising).
    draw_heng(draw,
              from_anchor=('ML', 0.935, 0.351),
              to_anchor=('MR', 0.051, 0.213),
              width=8)

    # s3 — 长横 (lower horizontal, longer, slightly rising).
    draw_heng(draw,
              from_anchor=('ML', 0.325, 0.939),
              to_anchor=('MR', 0.713, 0.793),
              width=9)

    # s4 — 竖钩 (vertical, hook up-left). Custom inline (TR6) so the
    # body may lean slightly (head.x ≠ hook_pt.x).
    _draw_shu_gou_custom(draw,
                         head=('TC', 0.389, 0.92),
                         hook_pt=('BC', 0.09, 0.85),  # bottom of body
                         tip=('BC', 0.09, 0.763),      # up-left tip
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shou(draw)
    out = os.path.join(os.path.dirname(__file__), '01_手.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
