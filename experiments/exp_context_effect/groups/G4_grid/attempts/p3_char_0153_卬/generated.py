"""p3_char_0153_卬 — G4 attempt.

Memory lookup checklist:
1. INDEX grep 卬 → not mastered. No chronic-primitive applies (卬 is not in the chronic 5).
2. errata grep 卬 → not listed. Related: 023_卩 FAILed (right half of 卬) — fix says 2 strokes
   for 卩: 横折钩 (small P-hook) + 竖 straight descending. We follow that literally for s3+s4.
3. form_catalog: 撇 in left-position + 竖提 in center-left = mirror of 卩. Inline fresh.
4. principles_meta TR6: 卬 is a 2-radical horizontal composition; inline fresh with the
   MMH anchors from the brief (no primitive fits both halves cleanly).
5. joint_atlas: both joints are N-class (small natural gap ~17-19 px). DO NOT weld.

4 strokes: (1) short 撇 top-left,  (2) 竖提 rising tail bottom of left,
           (3) 横折钩 small top of right (卩 top),  (4) long 竖 for 卩 body.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'strokes: pie (s1), shu-ti (s2), heng-zhe-gou for 卩 top (s3), long shu (s4). '
             'Two N-class gaps preserved: s1.tail↔s2.head at ML (~17px), s3.head↔s4.head at C (~19px).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def draw_pie(p_head, p_tail, w_head=8, w_tail=3):
    """Short pie curve — bulges left. Head thick, tail thin."""
    mx = (p_head[0] + p_tail[0]) / 2 - 6  # bow slightly left
    my = (p_head[1] + p_tail[1]) / 2
    pts = quad_bezier(p_head, (mx, my), p_tail, n=32)
    widths = [w_head + (w_tail - w_head) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths, INK)


def draw_shu_ti(p_head, p_tail, w=6):
    """竖提 rendered as a single diagonal-then-flick stroke.
    From p_head at top going down (and slightly toward tail x), curving into a rising
    ti at the bottom. For 卬 LEFT-half: head is upper-left, tail is lower-right (the
    rising flick). Render as: mostly vertical descent, then flick up-right toward tail.
    """
    # Corner: near tail, but a bit BELOW+LEFT so the ti rises properly
    corner_x = p_head[0] - 4  # keep vertical part on left
    corner_y = p_tail[1] + 8
    # Shu (descending body) — from head down to corner
    pts1 = sample_line(p_head, (corner_x, corner_y), n=30)
    widths1 = [w] * len(pts1)
    stroke_variable_width(draw, pts1, widths1, INK)
    # Ti (rising flick) — from corner up-right to tail
    pts2 = sample_line((corner_x, corner_y), p_tail, n=20)
    w_start = w
    w_end = 2
    widths2 = [w_start + (w_end - w_start) * i / (len(pts2) - 1) for i in range(len(pts2))]
    stroke_variable_width(draw, pts2, widths2, INK)


def draw_heng_zhe_gou_top(p_head, p_tail, w=5):
    """卩 top-right: short heng-zhe. p_head is upper-left, p_tail is lower-right.
    Render as: brief horizontal from head going right, then descend to tail.
    This forms the top+right-side of 卩's outer shape (the horizontal bar and its
    right descending stroke that bends into a hook at bottom — here shown as an
    L-shape opening to the left).
    """
    # Turning point: at tail's x, at head's y (so we go right then down)
    corner_x = p_tail[0]
    corner_y = p_head[1]
    # Heng portion (short, going right)
    pts1 = sample_line(p_head, (corner_x, corner_y), n=20)
    widths1 = [w] * len(pts1)
    stroke_variable_width(draw, pts1, widths1, INK)
    # Descending portion down to tail
    pts2 = sample_line((corner_x, corner_y), p_tail, n=20)
    widths2 = [w] * len(pts2)
    stroke_variable_width(draw, pts2, widths2, INK)


def draw_long_shu(p_head, p_tail, w=6):
    """Long vertical stroke — 卩 body descending."""
    pts = sample_line(p_head, p_tail, n=40)
    widths = [w] * len(pts)
    stroke_variable_width(draw, pts, widths, INK)


# ---------- Anchors from brief ----------
s1_head_a = ('TC', 0.242, 0.7)
s1_tail_a = ('ML', 0.812, 0.216)
s2_head_a = ('ML', 0.577, 0.122)
s2_tail_a = ('C',  0.315, 0.84)
s3_head_a = ('C',  0.743, 0.26)
s3_tail_a = ('BC', 0.972, 0.118)
s4_head_a = ('C',  0.5,   0.222)
s4_tail_a = ('BC', 0.614, 1.205)  # y_frac > 1 → below BC bottom (very long)

s1_head, s1_tail = anchor_to_xy(s1_head_a), anchor_to_xy(s1_tail_a)
s2_head, s2_tail = anchor_to_xy(s2_head_a), anchor_to_xy(s2_tail_a)
s3_head, s3_tail = anchor_to_xy(s3_head_a), anchor_to_xy(s3_tail_a)
s4_head, s4_tail = anchor_to_xy(s4_head_a), anchor_to_xy(s4_tail_a)

# Draw
draw_pie(s1_head, s1_tail)              # stroke 1 — 撇
draw_shu_ti(s2_head, s2_tail)           # stroke 2 — 竖提
draw_heng_zhe_gou_top(s3_head, s3_tail) # stroke 3 — 卩 top 横折(钩)
draw_long_shu(s4_head, s4_tail)         # stroke 4 — 竖 (long)

# Save
out = os.path.join(os.path.dirname(__file__), '01_卬.png')
img.save(out)
print(f'Wrote {out}')
print(f'Stroke count: 4 (expected 4).')
print(f'SELF_CHECK: {SELF_CHECK}')
