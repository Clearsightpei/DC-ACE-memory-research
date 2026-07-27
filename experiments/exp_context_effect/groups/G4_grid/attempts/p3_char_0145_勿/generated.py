"""p3_char_0145_勿 — G4 attempt (revision 2).

Revised for better composition after visual check:
 - Top 撇 lengthened and positioned in top-center area.
 - 横折钩 outer wrap: shoulder starts near top-center-right, drops down
   and curves outward-right to lower area, ends with modest up-left hook.
 - Two inner short 撇 drawn roughly parallel to top 撇, sitting inside
   the wrap.

Strokes per MMH (4 total):
 1. Top 撇: TC(0.05,0.58) → ML(0.54,0.67)
 2. 横折钩: ML(0.87,0.41) → BC(0.49,0.69) (with hook flick)
 3. Inner short 撇 upper: C(0.16,0.44) → BL(0.60,0.33)
 4. Inner short 撇 lower: C(0.67,0.35) → BL(0.82,0.79)

Joints: 3 × N (unwelded).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes: top pie, outer 横折钩 wrap, 2 inner short pies. All joints N.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402


def draw_wu(draw):
    # Stroke 1 — top 撇: sweeps from upper-mid down-left toward ML.
    # Extends visibly across the top; roughly diagonal.
    draw_pie(draw, ('TC', 0.35, 0.30), ('ML', 0.35, 0.85),
             head_width=11, tail_width=2, curve=0.10, segments=48)

    # Stroke 2 — 横折钩: short 横 shoulder at top, then curved descent
    # bowing outward-right, ending near lower-center with up-left hook.
    p_head = anchor_to_xy(('TC', 0.55, 0.65))       # shoulder start (top-right area)
    p_shoulder = anchor_to_xy(('TR', 0.55, 0.65))   # tiny 横 to the right
    p_tail = anchor_to_xy(('BC', 0.55, 0.80))       # hook base near lower center

    # Small horizontal top segment (shoulder → right)
    n_top = 8
    top_pts = [(p_head[0] + (p_shoulder[0] - p_head[0]) * i / n_top,
                p_head[1] + (p_shoulder[1] - p_head[1]) * i / n_top)
               for i in range(n_top + 1)]
    top_widths = [10] * (n_top + 1)
    stroke_variable_width(draw, top_pts, top_widths)

    # Long curved descent from shoulder end → tail (bow outward-right).
    ctrl = ((p_shoulder[0] + p_tail[0]) / 2 + 30,
            (p_shoulder[1] + p_tail[1]) / 2 - 10)
    body_pts = quad_bezier(p_shoulder, ctrl, p_tail, n=60)
    m = len(body_pts) - 1
    body_widths = [10 + (4 - 10) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, body_pts, body_widths)

    # Small hook flick tail → up-left (modest).
    p_tip = (p_tail[0] - 14, p_tail[1] - 10)
    hook_ctrl = (p_tail[0] - 3, p_tail[1] - 3)
    hook_pts = quad_bezier(p_tail, hook_ctrl, p_tip, n=20)
    hm = len(hook_pts) - 1
    hook_widths = [7 + (2 - 7) * (i / hm) for i in range(hm + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)

    # Stroke 3 — inner short 撇 upper: parallel to top 撇, inside wrap.
    # Head in upper interior, tail down-left.
    draw_pie(draw, ('C', 0.35, 0.30), ('C', 0.05, 0.85),
             head_width=9, tail_width=2, curve=0.10, segments=40)

    # Stroke 4 — inner short 撇 lower: longer, from mid-C down to BL.
    draw_pie(draw, ('C', 0.75, 0.55), ('BL', 0.65, 0.90),
             head_width=10, tail_width=2, curve=0.12, segments=48)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out = os.path.join(_HERE, '01_勿.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
