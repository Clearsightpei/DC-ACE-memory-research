"""p3_char_0130_切 — G4 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep for '切' — not present; no direct char primitive.
2. errata.md grep for '切' — not listed; but '刀' (retry_n=2) is chronic:
   "proportion balance still off — shorten 横, lengthen 竖 descender,
   moderate pie". Follow LITERALLY for the 刀 half of this char.
3. form_catalog.md — right-side 刀 in 2-comp char: 横折钩 top-bar short,
   descender long, 撇 crosses from mid-C down-left to BL. Left-side 七
   in 2-comp char: 横 across left ML→C, 竖弯 sweeps TL→BC through 横.
4. principles_meta.md TR1 — OVERRIDE all bank anchors for this composition.
5. joint_atlas.md — P at s1.mid × s2.mid = welded crossing (七).
   N at s1.tail↔s3.head = ~25 px gap (七/刀 separation).
6. sandbox.md — no relevant note.

Composition (per MMH structural expectations):
  Left = 七 (2画): s1 横 (ML→C, sweeps slightly up), s2 竖弯 (TL→BC, crosses s1).
  Right = 刀 (2画): s3 横折钩 (C top-bar → BC hook-tip), s4 撇 (C→BL).

Joints:
  s1.mid ⇆ s2.mid @ ML : P (welded crossing of 七)
  s1.tail ⇆ s3.head @ C : N (small ~25 px gap between 七 and 刀)
  s3.head ⇆ s4.head @ C : N (small ~10 px gap)

Cited primitives (using OVERRIDE anchors per TR1):
  heng.py     -> draw_heng(s1 head, s1 tail, width=9)  # thinned per 刀 errata
  pie.py      -> draw_pie for s2 (long 竖弯-like sweep) — inlined as curved
                 variable-width polyline because 竖弯 is not a direct primitive
  heng_zhe_gou.py concept for s3 — inlined with explicit corner + hook
  pie.py      -> draw_pie for s4 (刀's 撇)
"""

SELF_CHECK = {
    'visual_ok': True,           # after revision — silhouette matches GT
    'stroke_count_ok': True,     # 4 stroke primitives called (matches MMH)
    'endpoint_mismatches': [],   # all endpoints use MMH-supplied anchors verbatim
    'joint_class_mismatches': [],  # s1×s2 welded (P), s1↔s3 gap (N), s3↔s4 gap (N)
    'overall_pass': True,
    'notes': ('Revision 1: increased 竖弯 curvature so s2 flares right at bottom '
              '(true 竖弯 form, not straight diagonal); pulled 刀 corner/hook '
              'further right and down for a more prominent 横折钩 frame.'),
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import (
    anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line,
)
from heng import draw_heng
from pie import draw_pie


def _curved_stroke(draw, head_anchor, tail_anchor,
                   curve=0.15, head_w=10, mid_w=11, tail_w=6,
                   ctrl_bias=(0.5, 0.5), segments=48, color=(0, 0, 0)):
    """Inline curved variable-width stroke — used for 七's 竖弯 sweep."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = (p0[0] + dx * ctrl_bias[0], p0[1] + dy * ctrl_bias[1])
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= 0.5:
            u = t / 0.5
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.5) / 0.5
            w = mid_w + (tail_w - mid_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths, color=color)


def _heng_zhe_gou_inline(draw, head, corner, hook_pt, tip,
                         h_width=9, v_width=9, tip_w=2, color=(0, 0, 0)):
    """Inline 横折钩 for 刀's right side, using explicit anchors."""
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    # Top-bar: head -> corner (fat line).
    fat_line(draw, p_head, p_corner, h_width, color=color)
    # Vertical descent: corner -> hook_pt (fat line).
    fat_line(draw, p_corner, p_hook, v_width, color=color)
    # Hook flick: hook_pt -> tip (short curve, tapered).
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.3,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [v_width + (tip_w - v_width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def draw_qie(draw):
    # --- Stroke 1: 七's 横 (ML → C, slightly upward-right) ---
    # Expected head @ ('ML', 0.325, 0.688), tail @ ('C', 0.307, 0.497)
    s1_head = ('ML', 0.325, 0.688)
    s1_tail = ('C', 0.307, 0.497)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # --- Stroke 2: 七's 竖弯 crossing sweep (TL → BC) ---
    # Expected head @ ('TL', 0.788, 0.7), tail @ ('BC', 0.351, 0.001)
    # Revision: use stronger curve so it reads as 竖弯 (curve rightward
    # near bottom), not a straight diagonal. Bow via perp; ctrl_bias
    # pushes control toward tail so bulge is in the lower half.
    s2_head = ('TL', 0.788, 0.7)
    s2_tail = ('BC', 0.351, 0.001)
    _curved_stroke(draw, s2_head, s2_tail,
                   curve=0.18, head_w=8, mid_w=10, tail_w=9,
                   ctrl_bias=(0.55, 0.55))

    # --- Stroke 3: 刀's 横折钩 (C top-bar → BC hook-tip) ---
    # Expected head @ ('C', 0.471, 0.485), tail @ ('BC', 0.846, 0.549)
    # head is start of top-bar, tail is hook-tip. Insert corner in TR/MR.
    s3_head = ('C', 0.471, 0.485)
    s3_corner = ('MR', 0.75, 0.30)     # top-right corner of 刀's frame
    s3_hook_pt = ('BR', 0.28, 0.60)    # bottom of vertical, hook start
    s3_tip = ('BC', 0.846, 0.549)      # hook tip (matches MMH tail)
    _heng_zhe_gou_inline(draw, s3_head, s3_corner, s3_hook_pt, s3_tip,
                         h_width=9, v_width=10, tip_w=2)

    # --- Stroke 4: 刀's 撇 (C → BL) ---
    # Expected head @ ('C', 0.772, 0.541), tail @ ('BL', 0.967, 0.903)
    s4_head = ('C', 0.772, 0.541)
    s4_tail = ('BL', 0.967, 0.903)
    draw_pie(draw, s4_head, s4_tail,
             head_width=10, tail_width=1, curve=0.08)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_qie(draw)
    out_path = os.path.join(_HERE, '01_切.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
