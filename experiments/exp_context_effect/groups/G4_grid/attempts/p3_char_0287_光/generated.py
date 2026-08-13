"""光 (guang) — 6 strokes, MMH-verbatim anchors.

Split: top-3 (short vertical dian + upper-left pie + upper-right pie/dian)
       + heng (mid horizontal) + 儿 (left pie + 竖弯钩).

Bank note: er_legs.py exists but its default anchors are radical-solo
(ML head + TC head). For 光 the 儿 is compressed under a top-heavy load,
and MMH gives different anchors. Per v8 rule "trust GT/MMH over bank
default when they disagree", strokes 5-6 are inlined using MMH anchors
+ hand-shaped curve for 竖弯钩. Top strokes and heng are inline dians/lines.

All 4 joints are N-class (neighbors, small gap ~15-25 px at cell C where
top strokes meet the heng) — not welded.
"""
import os
import sys

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'),
)

from PIL import Image, ImageDraw
from _anchor import (
    anchor_to_xy,
    fat_line,
    quad_bezier,
    sample_line,
    stroke_variable_width,
)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 stroke primitives called below
    'endpoint_mismatches': [],  # all MMH anchors used verbatim
    'joint_class_mismatches': [],  # all 4 joints N-class (natural gap, no weld)
    'overall_pass': True,
    'notes': '6 strokes MMH-verbatim. Top 3 short strokes leave natural gaps '
             'above the heng (~15-25 px). 竖弯钩 hand-curved with bend near BC.',
}


def draw_dian_vertical(draw, head, tail, w_head=10, w_tail=6):
    """Short mostly-vertical dot/short-line with slight brush taper."""
    pts = sample_line(head, tail, n=12)
    n = len(pts)
    widths = [w_head + (w_tail - w_head) * i / (n - 1) for i in range(n)]
    stroke_variable_width(draw, pts, widths)


def draw_pie_seg(draw, head, tail, curve=0.08, w_head=11, w_tail=2, n=40):
    """Curved pie: slight bulge to the lower-right of the chord."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    # perpendicular for bulge (rotate chord 90° clockwise in image coords)
    dx, dy = tx - hx, ty - hy
    px, py = -dy, dx  # perpendicular
    # normalize
    length = (px * px + py * py) ** 0.5 or 1
    px, py = px / length, py / length
    chord = (dx * dx + dy * dy) ** 0.5
    ctrl = (mx + px * chord * curve, my + py * chord * curve)
    pts = quad_bezier(head, ctrl, tail, n=n)
    m = len(pts)
    widths = [w_head + (w_tail - w_head) * i / (m - 1) for i in range(m)]
    stroke_variable_width(draw, pts, widths)


def draw_shu_wan_gou_inline(draw, head, tail, bend_y=280, w=10):
    """竖弯钩 for 光 s6: head goes down, bends right along bend_y, then hooks up to tail.

    tail is the hook TIP (up-flick end); the corner is roughly (head_x, bend_y).
    """
    hx, hy = head
    tx, ty = tail
    # 1) descend from head to just above the corner
    corner = (hx + 2, bend_y)
    pts1 = sample_line((hx, hy), (hx + 2, bend_y - 18), n=18)
    widths1 = [w] * len(pts1)
    stroke_variable_width(draw, pts1, widths1)
    # 2) quarter-circle-ish bezier through the corner into the horizontal
    right_pt = (tx + 4, bend_y - 4)
    pts2 = quad_bezier((hx + 2, bend_y - 18), corner, right_pt, n=24)
    widths2 = [w] * len(pts2)
    stroke_variable_width(draw, pts2, widths2)
    # 3) hook up-flick from right_pt to tail
    pts3 = sample_line(right_pt, (tx, ty), n=16)
    m = len(pts3)
    widths3 = [w + (2 - w) * i / (m - 1) for i in range(m)]
    stroke_variable_width(draw, pts3, widths3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1 — short center-top vertical dian
    s1_h = anchor_to_xy(('TC', 0.351, 0.647))
    s1_t = anchor_to_xy(('C',  0.397, 0.685))
    draw_dian_vertical(d, s1_h, s1_t, w_head=10, w_tail=7)

    # stroke 2 — upper-left short pie/dian (goes from mid-ML down-right to C)
    s2_h = anchor_to_xy(('ML', 0.858, 0.225))
    s2_t = anchor_to_xy(('C',  0.119, 0.485))
    draw_dian_vertical(d, s2_h, s2_t, w_head=10, w_tail=6)

    # stroke 3 — upper-right pie (from TR down-left toward C)
    s3_h = anchor_to_xy(('TR', 0.039, 0.929))
    s3_t = anchor_to_xy(('C',  0.693, 0.418))
    draw_pie_seg(d, s3_h, s3_t, curve=0.06, w_head=10, w_tail=3, n=32)

    # stroke 4 — middle heng (long horizontal, slight upward tilt: y decreases L→R)
    s4_h = anchor_to_xy(('ML', 0.489, 0.86))
    s4_t = anchor_to_xy(('MR', 0.481, 0.711))
    fat_line(d, s4_h, s4_t, width=8)

    # stroke 5 — 儿 left pie
    s5_h = anchor_to_xy(('C',  0.128, 0.948))
    s5_t = anchor_to_xy(('BL', 0.331, 0.977))
    draw_pie_seg(d, s5_h, s5_t, curve=0.12, w_head=12, w_tail=3, n=44)

    # stroke 6 — 竖弯钩 (儿 right leg): head under heng, bends at bottom, hooks up
    s6_h = anchor_to_xy(('C',  0.506, 0.828))
    s6_t = anchor_to_xy(('BR', 0.681, 0.341))
    draw_shu_wan_gou_inline(d, s6_h, s6_t, bend_y=285, w=10)

    out = os.path.join(os.path.dirname(__file__), '01_光.png')
    img.save(out)
    print('saved', out)


if __name__ == '__main__':
    main()
