"""卩 (jié) — 2画 radical. Stroke order: 横折钩 (P-loop), then 竖.

Revision 1 notes:
  v1 used draw_heng_zhe_gou which gave a boxy P with a very short hook,
  reading more like "7" than a proper P-loop. GT shows a ROUNDED loop
  that flares out at top and curves down-and-INWARD at the bottom,
  ending near the vertical stem. Inlining (TR6) a curved P-shape:
    - a horizontal top bar,
    - a curved descent that arcs slightly right then back left,
    - a distinct leftward hook at the bottom pointing toward the stem.

Anchor plan:
  stroke 1 (横折钩, inlined as rounded loop):
    head    ('TC', 0.55, 0.28)   — top-left of P-bar
    corner  ('TR', 0.30, 0.28)   — top-right of P-bar (折 corner)
    belly   ('TR', 0.40, 0.55)   — rightmost bulge of the loop
    tail    ('C',  0.60, 0.60)   — bottom of loop before hook
    tip     ('C',  0.35, 0.60)   — hook tip pointing left toward stem
  stroke 2 (竖):
    from    ('TC', 0.40, 0.22)   — top of long vertical (slightly ABOVE P-top)
    to      ('BC', 0.40, 0.95)   — bottom of canvas

Joints:
  s1.head @ TC(0.55, 0.28)  ⇆  s2.head @ TC(0.40, 0.22)  — class N.
    Same cell TC, x-frac gap 0.15, y-frac gap 0.06 → ~16 px pixel
    distance (MMH expected gap ≈ 19 px). Do NOT weld.

TR9: expanded MMH under-spans for standalone radical.
TR6: inlined a rounded P-shape because heng_zhe_gou's tight corner and
     short hook do not match the curved loop the GT shows.
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Two specific agreements between my rendered PNG and GT: '
        '(1) The right-side stroke forms a rounded "P" loop with a '
        'horizontal top bar and a curved descent that arcs down and '
        'ends with a leftward hook pointing back toward the vertical. '
        '(2) The left-side vertical is a long straight 竖 that starts '
        'slightly above the top of the P and extends all the way to '
        'the bottom of the canvas. '
        'Joint at top is a small natural gap (~16 px), N-class, matching '
        'MMH expected ~19 px — top of P sits just right of and slightly '
        'below the top of the vertical.'
    ),
}


def _draw_p_loop(draw, head, corner, belly, tail, tip,
                 h_width=10, v_width=10, shoulder=13, tip_w=2,
                 color=(0, 0, 0)):
    """Inline 横折钩 with a rounded (curved) descent instead of a
    sharp fat_line vertical. Used only for 卩's P-loop."""
    p_head   = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_belly  = anchor_to_xy(belly)
    p_tail   = anchor_to_xy(tail)
    p_tip    = anchor_to_xy(tip)

    # 1. Horizontal top bar head -> corner.
    fat_line(draw, p_head, p_corner, h_width, color=color)

    # 2. 顿笔 shoulder press at corner.
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    # 3. Curved descent corner -> belly -> tail.
    #    Use `belly` as raw Bezier control (per principle bank guidance:
    #    raw control is safer than 2*belly - midpoint derivation).
    body_pts = quad_bezier(p_corner, p_belly, p_tail, n=40)
    body_widths = [v_width] * len(body_pts)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # 4. Hook flick tail -> tip (leftward, slightly upward).
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [v_width + (tip_w - v_width) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: P-loop (横折钩, inlined rounded variant) ----
    s1_head   = ('TC', 0.55, 0.28)
    s1_corner = ('TR', 0.30, 0.28)
    s1_belly  = ('TR', 0.40, 0.55)
    s1_tail   = ('C',  0.60, 0.60)
    s1_tip    = ('C',  0.35, 0.60)
    _draw_p_loop(draw, s1_head, s1_corner, s1_belly, s1_tail, s1_tip,
                 h_width=10, v_width=10, shoulder=13, tip_w=2)

    # ---- Stroke 2: 竖 (long vertical on the left) ----
    s2_top = ('TC', 0.40, 0.22)
    s2_bot = ('BC', 0.40, 0.95)
    draw_shu(draw, from_anchor=s2_top, to_anchor=s2_bot, width=10)

    # ---- Direction / joint sanity asserts ----
    p_s1h = anchor_to_xy(s1_head)
    p_s1c = anchor_to_xy(s1_corner)
    p_s1t = anchor_to_xy(s1_tail)
    p_s1tip = anchor_to_xy(s1_tip)
    p_s2h = anchor_to_xy(s2_top)
    p_s2b = anchor_to_xy(s2_bot)

    # s2 descends:
    assert p_s2b[1] > p_s2h[1], 'stroke 2 must descend top->bottom'
    # s1 top-bar goes rightward:
    assert p_s1c[0] > p_s1h[0], 's1 top bar must go head->corner rightward'
    # s1 hook tip is LEFT of tail (leftward hook):
    assert p_s1tip[0] < p_s1t[0], 's1 hook tip must be left of tail'
    # s1 head is to the RIGHT of s2 head:
    assert p_s1h[0] > p_s2h[0], 's1 head must be right of s2 head'
    # N-class gap between s1 head and s2 head:
    dx = p_s1h[0] - p_s2h[0]
    dy = p_s1h[1] - p_s2h[1]
    dist = (dx * dx + dy * dy) ** 0.5
    assert 8 <= dist <= 30, f'N-class gap should be ~15-20 px, got {dist:.1f}'

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_卩.png')
    img.save(out)
    print(f'wrote {out}  |  N-gap={dist:.1f}px')


if __name__ == '__main__':
    main()
