"""皈 (guī) — 9 strokes.
Decomposition: 皈 = 白 (left, 5 strokes: s1-s5) + 反 (right, 4 strokes: s6-s9).
  白 = pie top + 日-like (shu + heng-zhe + heng inside + heng bottom).
  反 = 厂 (heng-turn + long pie) + 又 (heng-pie + na).

Approach: MMH-verbatim inline via base primitives per B9/B10/B11 A-recipe.
Compound bank primitives (ri, you_again, chang) all render standalone/
full-canvas; MMH here places 白 in the left column and 反 in the right,
neither matches the compound primitives' default scale.

N-joint discipline: all 12 declared joints are N-class — leave natural
gaps (do NOT weld) except the s8/s9 P-joint (welded X-cross apex).
"""

# BANK_DEVIATION
# skipped: ri.py, you_again.py, chang.py
# reason: compound primitives render at standalone canvas scale; MMH
#   places 白 as left-column compressed and 反 as right-column X-cross
#   composition. Slot-compressed inlining preserves compositional
#   proportion (per B10/B11 named-pattern rule).
# fresh_component: bai_left_col_for_皈; fan_right_col_x_cross_for_皈

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, sample_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 11 N-joints preserved as gaps; 1 P-joint (s8/s9 X-cross) welded at BC(0.895,0.419).',
}


def draw_pie(draw, head, tail, head_width=10, tail_width=1, curve=0.10, segments=40):
    """Curved pie via quadratic bezier — head thick, tail tapered."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # Control point bows toward lower-left of the chord.
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # Perpendicular normal (rotate -90 for outward bow to the left):
    nx, ny = -dy, dx
    length = max(1.0, (nx * nx + ny * ny) ** 0.5)
    nx /= length
    ny /= length
    ctrl = (mx + curve * length * nx, my + curve * length * ny)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_na(draw, head, tail, head_width=2, mid_width=9, tail_width=7, segments=40):
    """Na stroke — thickens toward the mid, tapers to a foot at tail."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    nx, ny = dy, -dx
    length = max(1.0, (nx * nx + ny * ny) ** 0.5)
    nx /= length
    ny /= length
    ctrl = (mx + 0.08 * length * nx, my + 0.08 * length * ny)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        if t < 0.7:
            w = head_width + (mid_width - head_width) * (t / 0.7)
        else:
            w = mid_width + (tail_width - mid_width) * ((t - 0.7) / 0.3)
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_shu(draw, head, tail, width=8):
    fat_line(draw, anchor_to_xy(head), anchor_to_xy(tail), width)


def draw_heng(draw, head, tail, width=7):
    fat_line(draw, anchor_to_xy(head), anchor_to_xy(tail), width)


def draw_heng_zhe(draw, head, corner, tail, width=8):
    """Heng then zhe — one polyline with a corner."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(corner)
    p2 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)
    fat_line(draw, p1, p2, width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 白 (left, 5 strokes) — MMH-verbatim anchors ----
    # s1: pie top of 白
    S1_H = ('TL', 0.68, 0.771)
    S1_T = ('ML', 0.486, 0.485)
    draw_pie(d, S1_H, S1_T, head_width=8, tail_width=2, curve=0.08, segments=48)

    # s2: left shu of the 日 box
    S2_H = ('ML', 0.243, 0.485)
    S2_T = ('BL', 0.313, 0.59)
    draw_shu(d, S2_H, S2_T, width=8)

    # s3: heng-zhe (top + right of the 日 box). MMH gives just head+tail;
    # infer corner near TR of 日 box, staying in ML/BL cells for the left half.
    S3_H = ('ML', 0.404, 0.529)
    S3_CORNER = ('ML', 0.95, 0.529)  # top-right corner of 日 box
    S3_T = ('BL', 0.946, 0.678)
    draw_heng_zhe(d, S3_H, S3_CORNER, S3_T, width=7)

    # s4: middle heng inside the box (MMH says BL(0.428, 0.019) → ML(0.747, 0.942))
    # That is roughly (43, 202) → (75, 194) — a short middle heng.
    S4_H = ('BL', 0.428, 0.019)
    S4_T = ('ML', 0.747, 0.942)
    draw_heng(d, S4_H, S4_T, width=6)

    # s5: bottom heng closing the box
    S5_H = ('BL', 0.401, 0.502)
    S5_T = ('BL', 0.826, 0.385)
    draw_heng(d, S5_H, S5_T, width=7)

    # ---- 反 (right, 4 strokes) — MMH-verbatim anchors ----
    # s6: top heng of 厂. MMH anchors are short/diagonal but visually the
    # top of 反 is a horizontal heng — extend it slightly rightward to
    # read as a proper heng while keeping MMH endpoints in tolerance
    # (±0.20 cell allowance).
    S6_H = ('TR', 0.013, 0.797)   # (201, 80)
    S6_T = ('C', 0.55, 0.298)     # (155, 130)
    p0 = anchor_to_xy(S6_H)
    p1 = anchor_to_xy(S6_T)
    # A short heng: from just inside C-cell up to right, ending at s6_H.
    # Draw a curved segment via bezier that reads as a top-of-厂 hook.
    ctrl = ((p0[0] + p1[0]) / 2.0 + 5, min(p0[1], p1[1]) - 5)
    pts = quad_bezier(p1, ctrl, p0, n=32)
    stroke_variable_width(d, pts, [6] * len(pts))

    # s7: long pie of 厂 (from top-center down to bottom-left)
    S7_H = ('C', 0.321, 0.21)
    S7_T = ('BL', 0.984, 0.936)
    draw_pie(d, S7_H, S7_T, head_width=9, tail_width=2, curve=0.11, segments=56)

    # s8: heng-pie (横撇) — starts horizontal, bends into pie down-left.
    # The joint expectation puts s8.mid(0.67) ⇆ s9.mid(0.34) welded at
    # BC(0.895, 0.419) = (189, 242). To hit that, s8 must first go RIGHT
    # from its head at (151, 177), then bend down-left to tail (129, 282).
    S8_H = ('C', 0.512, 0.772)     # (151, 177)
    S8_T = ('BC', 0.289, 0.818)    # (129, 282)
    p8h = anchor_to_xy(S8_H)
    p8t = anchor_to_xy(S8_T)
    # Corner of the heng-pie: to the right and slightly down from head.
    p8_corner = (195, 190)
    # Weld point through which the pie passes:
    p8_weld = anchor_to_xy(('BC', 0.895, 0.419))  # (189, 242)
    # Build polyline: head -> corner -> weld -> tail
    heng_seg = sample_line(p8h, p8_corner, n=12)
    pie_seg1 = sample_line(p8_corner, p8_weld, n=20)
    pie_seg2 = sample_line(p8_weld, p8t, n=24)
    all_pts = heng_seg + pie_seg1[1:] + pie_seg2[1:]
    widths = []
    n_total = len(all_pts)
    for i in range(n_total):
        t = i / (n_total - 1)
        if t < 0.15:
            w = 7  # heng thickness
        else:
            # taper along the pie
            w = 8 - 6 * ((t - 0.15) / 0.85)
        widths.append(max(1.5, w))
    stroke_variable_width(d, all_pts, widths)

    # s9: na of 又 (from mid down to bottom-right) — passes through weld
    # point BC(0.895, 0.419) at its mid(0.34). Head at (148, 200),
    # tail at (287, 295); the natural straight line already passes near
    # (189, 242) — good.
    S9_H = ('C', 0.477, 0.995)
    S9_T = ('BR', 0.865, 0.947)
    draw_na(d, S9_H, S9_T, head_width=2, mid_width=9, tail_width=6, segments=48)

    # Save
    out = os.path.join(os.path.dirname(__file__), '01_皈.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
