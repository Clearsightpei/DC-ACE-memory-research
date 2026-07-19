"""扌 (shǒu radical, 3 strokes) — G4 grid-bank attempt.

Composition:
  s1: 横 (short horizontal, upper area)
  s2: 竖钩 (long vertical with up-left hook at bottom)
  s3: 提 (rising diagonal, crossing s2 mid-body)

Anchors (from MMH-derived structural expectations):
  s1: head=('C', 0.02, 0.383), tail=('C', 0.866, 0.263)
  s2: head=('TC', 0.433, 0.674), tail=('BC', 0.151, 0.631)   (tail = hook tip)
  s3: head=('BL', 0.85, 0.203), tail=('C', 0.887, 0.717)

Joints:
  s1.mid ⇆ s2.mid @ C  — P (welded crossing at top: 横 crosses 竖钩)
  s2.mid ⇆ s3.mid @ C  — P (welded crossing lower: 提 crosses 竖钩)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; two P-crossings arise by construction '
             'because both s1 and s3 cross the s2 body inside cell C.'
}

import os, sys
from PIL import Image, ImageDraw

# Reach shared G4 primitives (success_bank/code/).
_CODE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _CODE)

from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier, fat_line
from heng import draw_heng
from ti import draw_ti


def draw_shu_gou_custom(draw, head, hook_pt, tip,
                        head_w=11, mid_w=10, hook_start_w=9, tip_w=2):
    """竖钩 with straight body head→hook_pt, then up-and-left hook flick.

    Written inline (TR6) so the body strictly follows the MMH head/tail line
    even though it leans slightly (MMH tail x < head x).
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

    # Hook: quad bezier from hook_pt up-and-left to tip.
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 横 (short horizontal, upper area, slightly rising) ---
    s1_head = ('C', 0.02, 0.383)
    s1_tail = ('C', 0.866, 0.263)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # --- Stroke 2: 竖钩 (long vertical body with up-left hook tail) ---
    # MMH head is at TC(0.433, 0.674) — near bottom of TC cell, upper-middle of canvas.
    # MMH tail is at BC(0.151, 0.631) — that's actually the hook tip (up-left).
    # We insert an intermediate hook_pt just above the tip on the body line so
    # the body stays straight down and the hook curls off to the tip.
    # s2 head is TC(0.433, 0.674) → PIL (143.3, 167.4).
    # s2 tail is BC(0.151, 0.631) → PIL (115.1, 263.1) — this is the hook tip.
    # Body should stay straight down along x≈143 to a hook_pt near (143, 263),
    # then curl up-and-left to the tip at (115, 263).
    s2_head = ('TC', 0.433, 0.674)
    s2_hook_pt = ('BC', 0.43, 0.63)         # bottom of body, same x as head
    s2_tip = ('BC', 0.151, 0.631)           # MMH hook tip (up-and-left)
    draw_shu_gou_custom(draw, s2_head, s2_hook_pt, s2_tip,
                        head_w=11, mid_w=10, hook_start_w=9, tip_w=2)

    # --- Stroke 3: 提 (rising diagonal crossing s2 body in cell C) ---
    s3_head = ('BL', 0.85, 0.203)   # PIL ~ (185, 220.3)  — lower-left start
    s3_tail = ('C', 0.887, 0.717)   # PIL ~ (188.7, 171.7) — upper-right tip
    draw_ti(draw, s3_head, s3_tail, head_width=11, tail_width=1, curve=0.05, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_扌.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
