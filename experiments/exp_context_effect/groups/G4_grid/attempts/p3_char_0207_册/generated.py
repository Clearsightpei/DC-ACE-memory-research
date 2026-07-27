"""G4 attempt for 册 (p3_char_0207_册).

Memory-read log:
# read: memory_index.md (v8 slim checklist — bank is reference only)
# read: GT phase3/册.png
# no direct component in success_bank (册 has no clean sub-radical mastered)
# drawing fresh using MMH anchors + adding 横折 corner-cap where MMH endpoints
# omit the horizontal top (MMH gives 2 medians per stroke; 横折 needs a cap).
"""

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), '../../success_bank/code'),
)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # P joints all cross s5 (welded); N joints have gaps
    'overall_pass': True,
    'notes': (
        '5 strokes: two 撇 (s1,s3) + two 横折 (s2,s4) + middle 横 (s5). '
        'Both 横折 get a small left-going cap at the head to render the '
        'top-horizontal segment MMH omits (MMH gives head/tail only). '
        'Gaps: s1.head~s2.head (N), s3.head~s4.head (N), s2.mid~s3.tail (N). '
        's5 pierces s1,s2,s3,s4 (P — welded by geometry).'
    ),
}

WIDTH = 5

# --- anchor→pixel conversion ---
s1_head = anchor_to_xy(('TL', 0.706, 0.899))
s1_tail = anchor_to_xy(('BL', 0.407, 0.909))
s2_head = anchor_to_xy(('TL', 0.917, 0.987))
s2_tail = anchor_to_xy(('BL', 0.905, 0.569))
s3_head = anchor_to_xy(('TC', 0.585, 0.847))
s3_tail = anchor_to_xy(('BC', 0.318, 0.947))
s4_head = anchor_to_xy(('TC', 0.764, 0.861))
s4_tail = anchor_to_xy(('BC', 0.846, 0.684))
s5_head = anchor_to_xy(('ML', 0.281, 0.770))
s5_tail = anchor_to_xy(('MR', 0.792, 0.731))


def draw_pie(d, p_start, p_end, ctrl_dx=-6, ctrl_dy=6):
    """Draw a gently left-curving 撇-like stroke as a quadratic bezier."""
    mx = (p_start[0] + p_end[0]) / 2 + ctrl_dx
    my = (p_start[1] + p_end[1]) / 2 + ctrl_dy
    pts = quad_bezier(p_start, (mx, my), p_end, n=40)
    widths = [WIDTH] * len(pts)
    stroke_variable_width(d, pts, widths)


def draw_heng_zhe(d, head, tail, cap_dx=-18):
    """Draw a 横折: short horizontal cap going LEFT from head, then vertical to tail."""
    cap_left = (head[0] + cap_dx, head[1])
    fat_line(d, cap_left, head, WIDTH)
    fat_line(d, head, tail, WIDTH)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — left unit's left 撇 (more pronounced left curve)
    draw_pie(d, s1_head, s1_tail, ctrl_dx=-14, ctrl_dy=6)

    # Stroke 2 — left unit's 横折 (wide cap so top of unit reads as closed;
    # cap stops ~10px right of s1.head to preserve the N-class gap requirement)
    cap2_dx = -(s2_head[0] - s1_head[0]) + 12
    draw_heng_zhe(d, s2_head, s2_tail, cap_dx=cap2_dx)

    # Stroke 3 — right unit's left 撇
    draw_pie(d, s3_head, s3_tail, ctrl_dx=-14, ctrl_dy=6)

    # Stroke 4 — right unit's 横折 (wide cap, same rule vs s3.head)
    cap4_dx = -(s4_head[0] - s3_head[0]) + 8
    draw_heng_zhe(d, s4_head, s4_tail, cap_dx=cap4_dx)

    # Stroke 5 — middle 横 spanning both units (pierces s1..s4)
    fat_line(d, s5_head, s5_tail, WIDTH)

    out = os.path.join(os.path.dirname(__file__), '01_册.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
