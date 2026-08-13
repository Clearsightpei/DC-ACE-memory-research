"""p3_char_0325_状 (zhuàng, "condition/appearance") — 7 strokes.

Composition: 丬 (left, 3 strokes: dot, ti, shu) + 犬 (right, 4 strokes:
heng, pie, na, top-right dot).

Strategy: MMH anchors are trustworthy for chars — use them verbatim.
Left 丬 anchors line up with jiang_side/pan.py convention but are
inlined here for simplicity given they only fire once.
Right side is essentially 大 + a top-right dot (犬 = 大 + 丶).
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, sample_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim. 丬 (dot+ti+shu) + 犬 (heng+pie+na+dot).',
}


def draw_stroke_line(draw, a_head, a_tail, width=6):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    fat_line(draw, p0, p1, width)


def draw_pie_curve(draw, a_head, a_tail, head_w=10, tail_w=2, curve=-0.15):
    """Concave-right pie: sweep down-left with a slight bow."""
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    # perpendicular offset for the control point
    ctrl = (mx + curve * dy, my - curve * dx)
    pts = quad_bezier(p0, ctrl, p2, n=48)
    widths = [head_w + (tail_w - head_w) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_na_curve(draw, a_head, a_tail, head_w=2, peak_w=12, tail_w=1, peak_t=0.75, curve=0.10):
    """Na (right-falling): thin head, swells to peak, thin foot."""
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    ctrl = (mx + curve * dy, my - curve * dx)
    pts = quad_bezier(p0, ctrl, p2, n=48)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        if t < peak_t:
            w = head_w + (peak_w - head_w) * (t / peak_t)
        else:
            w = peak_w + (tail_w - peak_w) * ((t - peak_t) / (1 - peak_t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_dot(draw, a_head, a_tail, head_w=3, tail_w=10):
    """Small dot stroke — thickens toward the tail."""
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = sample_line(p0, p1, n=16)
    widths = [head_w + (tail_w - head_w) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_zhuang(draw):
    # -------- 丬 (left, 3 strokes) --------
    # s1: dot 丶 — short down-right in ML
    draw_dot(draw,
             a_head=('ML', 0.437, 0.175),
             a_tail=('ML', 0.762, 0.482),
             head_w=3, tail_w=9)

    # s2: ti 提 — rising stroke from BL up to ML/right
    p0 = anchor_to_xy(('BL', 0.249, 0.314))
    p1 = anchor_to_xy(('ML', 0.943, 0.813))
    pts = sample_line(p0, p1, n=24)
    widths = [10 - 8 * i / (len(pts) - 1) for i in range(len(pts))]  # thick base, thin tip
    stroke_variable_width(draw, pts, widths)

    # s3: shu 竖 — long right vertical from TL down to BL
    draw_stroke_line(draw,
                     a_head=('TL', 0.92, 0.724),
                     a_tail=('BL', 0.984, 0.971),
                     width=8)

    # -------- 犬 (right, 4 strokes) --------
    # s4: heng 横 — short, slight upward slope in C→MR
    draw_stroke_line(draw,
                     a_head=('C', 0.263, 0.726),
                     a_tail=('MR', 0.426, 0.588),
                     width=7)

    # s5: pie 撇 — from TC down-left through C to BC, curved
    draw_pie_curve(draw,
                   a_head=('TC', 0.696, 0.668),
                   a_tail=('BC', 0.169, 0.748),
                   head_w=10, tail_w=2, curve=-0.10)

    # s6: na 捺 — from C down-right to BR (heavy, swelling)
    draw_na_curve(draw,
                  a_head=('C', 0.854, 0.98),
                  a_tail=('BR', 0.851, 0.821),
                  head_w=2, peak_w=13, tail_w=1, peak_t=0.75, curve=0.10)

    # s7: top-right dot (犬 identifier)
    draw_dot(draw,
             a_head=('MR', 0.136, 0.017),
             a_tail=('MR', 0.414, 0.283),
             head_w=3, tail_w=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_zhuang(draw)
    out = os.path.join(_HERE, '01_状.png')
    img.save(out)
    print(f"Saved: {out}")


if __name__ == '__main__':
    main()
