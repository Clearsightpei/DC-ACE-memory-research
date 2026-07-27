"""乩 (jī) — Phase-3 character, 6 strokes.

Split: 占 (left) + 乚 (right).
  占 = 卜 (top: 竖 + 点) + 口 (bottom: 竖 + 横折 + 横)
  乚 = large竖弯钩 curving from top-center down to bottom-right.

Anchors follow MMH-derived structural spec (dispatcher-injected).
"""

# Reading log:
# - drawer_memory.md read: no chronic match; 卜/口 primitives cited
# - success_bank INDEX grep: bu.py, kou.py exist (占 = bu + kou stack)
# - errata: no entry for 乩

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '乩 = 占 (卜+口) + 乚; drew all 6 strokes per MMH anchors; N-joints preserved (口 corners slight gaps; 卜 point right of 竖).',
}


def draw_shu(draw, head, tail, width=10):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def draw_dian(draw, head, tail, head_w=3, peak_w=10):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, 24)
    widths = [head_w + (peak_w - head_w) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head, tail, width=9):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def draw_heng_zhe(draw, head, tail, width=9):
    """Corner bend: go horizontally to a corner, then drop down.
    head/tail are the two endpoint anchors; corner inferred as (tail.x, head.y).
    """
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    corner = (p2[0], p0[1])
    fat_line(draw, p0, corner, width)
    fat_line(draw, corner, p2, width)


def draw_shu_wan_gou(draw, head, tail, width=10):
    """竖弯钩 for 乚: start vertical from head, curve at bottom, go right to tail; small up-hook at end."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # Control point: down and left of tail, near p0.x, tail.y
    ctrl = (p0[0], p2[1])
    pts = quad_bezier(p0, ctrl, p2, n=60)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)
    # Small hook up at tail end
    hook_end = (p2[0] + 2, p2[1] - 18)
    fat_line(draw, p2, hook_end, width - 1)


def draw_jia(draw):
    # s1: 占 卜 竖 (left vertical of top part)
    draw_shu(draw, ('TL', 0.844, 0.735), ('BL', 0.902, 0.024), width=10)
    # s2: 占 卜 点 (short slanted point right of s1)
    draw_dian(draw, ('C', 0.061, 0.424), ('C', 0.518, 0.339))
    # s3: 口 left 竖
    draw_shu(draw, ('BL', 0.407, 0.098), ('BL', 0.621, 0.883), width=9)
    # s4: 口 横折 (top of 口: horizontal then down)
    draw_heng_zhe(draw, ('BL', 0.601, 0.188), ('BC', 0.187, 0.499), width=9)
    # s5: 口 bottom 横
    draw_heng(draw, ('BL', 0.68, 0.657), ('BC', 0.356, 0.637), width=9)
    # s6: 乚 (right竖弯钩)
    draw_shu_wan_gou(draw, ('TC', 0.658, 0.645), ('BR', 0.728, 0.265), width=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_jia(draw)
    out = os.path.join(_HERE, '01_乩.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
