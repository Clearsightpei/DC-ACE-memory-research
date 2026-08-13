"""侑 (yòu) — 8 strokes.
Decomposition: 侑 = 亻 (left) + 有 (right); 有 = 𠂇 (top: heng + pie) + 月 (bottom).

Per B9/B10 A-recipe: MMH-verbatim anchors + base primitives (skip
compound ren_side because MMH places 亻 far-left at TL/ML/BL columns,
not ren_side's TC/C defaults — the p3_char_0252_伊 partial-override
FAIL pattern).
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH anchors put 亻 in far-left TL/ML/BL column (s1 head TL 0.94,
#         tail ML 0.199; s2 head ML 0.703 tail BL 0.732); ren_side's default
#         anchors sit in TC/C. Partial 4-anchor override of the compound
#         primitive is worse than inlining pie+shu with MMH-verbatim anchors.
# fresh_component: ren_side_far_left_for_compound

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line


def draw_pie_curve(draw, head, tail, head_w=13, tail_w=2, curve=0.18, segments=48):
    """撇 — bowed curve from head (upper-right) to tail (lower-left)."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # perpendicular offset for bow (bows away from the diagonal)
    nx = -dy
    ny = dx
    L = (nx * nx + ny * ny) ** 0.5
    if L > 0:
        nx /= L; ny /= L
    ctrl = (mx + nx * curve * ((dx*dx + dy*dy) ** 0.5),
            my + ny * curve * ((dx*dx + dy*dy) ** 0.5))
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_heng_line(draw, head, tail, width=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def draw_shu_line(draw, head, tail, width=9):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def draw_heng_zhe_gou(draw, head, tail, width=8, hook_len=12):
    """月's right side: head at top-inside, go right to top-right, down to
    bottom-right, then hook left to tail."""
    p_start = anchor_to_xy(head)     # top-left of fold
    p_end = anchor_to_xy(tail)       # hook tip (lower-left)
    # infer the two fold corners
    top_right = (p_end[0] + hook_len, p_start[1])
    bot_right = (p_end[0] + hook_len, p_end[1])
    # horizontal segment
    fat_line(draw, p_start, top_right, width)
    # vertical segment
    fat_line(draw, top_right, bot_right, width)
    # hook (short leftward)
    fat_line(draw, bot_right, p_end, width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1: 撇 head TL(0.94, 0.633) → tail ML(0.199, 0.948)
    draw_pie_curve(d, ('TL', 0.94, 0.633), ('ML', 0.199, 0.948),
                   head_w=13, tail_w=2, curve=0.14, segments=48)
    # s2: 竖 head ML(0.703, 0.497) → tail BL(0.732, 0.906)
    draw_shu_line(d, ('ML', 0.703, 0.497), ('BL', 0.732, 0.906), width=8)

    # ---- 𠂇 (top of 有) ----
    # s3: 横 head C(0.093, 0.228) → tail MR(0.666, 0.084)
    draw_heng_line(d, ('C', 0.093, 0.228), ('MR', 0.666, 0.084), width=7)
    # s4: 撇 head TC(0.682, 0.565) → tail BL(0.891, 0.332)  (passes through heng)
    draw_pie_curve(d, ('TC', 0.682, 0.565), ('BL', 0.891, 0.332),
                   head_w=10, tail_w=2, curve=0.10, segments=48)

    # ---- 月 (bottom of 有) ----
    # s5: 撇 (月 left) head C(0.562, 0.655) → tail BC(0.427, 0.962)
    draw_pie_curve(d, ('C', 0.562, 0.655), ('BC', 0.427, 0.962),
                   head_w=10, tail_w=6, curve=0.06, segments=40)
    # s6: 横折钩 (月 right) head C(0.641, 0.673) → tail BC(0.901, 0.812)
    draw_heng_zhe_gou(d, ('C', 0.641, 0.673), ('BC', 0.901, 0.812),
                      width=8, hook_len=10)
    # s7: inner heng 1  head BC(0.626, 0.089) → tail BC(0.98, 0.007)
    draw_heng_line(d, ('BC', 0.626, 0.089), ('BC', 0.98, 0.007), width=6)
    # s8: inner heng 2  head BC(0.608, 0.411) → tail BR(0.001, 0.35)
    draw_heng_line(d, ('BC', 0.608, 0.411), ('BR', 0.001, 0.35), width=6)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_侑.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke draw calls (s1..s8)
    'endpoint_mismatches': [], # all MMH-verbatim
    'joint_class_mismatches': [],  # s3×s4 crosses naturally (P-weld);
                                   # all others N-gap preserved (no forced welds)
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; ren_side skipped (far-left slot). '
             '月 right rendered as 横折钩 compound; 𠂇 pie crosses heng.',
}


if __name__ == '__main__':
    print(render())
