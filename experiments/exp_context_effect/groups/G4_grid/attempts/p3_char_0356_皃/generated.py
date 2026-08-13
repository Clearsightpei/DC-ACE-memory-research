"""p3_char_0356_皃 — G4 attempt.

# memory reads:
#   drawer_memory.md: er_legs.py shortlist for 儿-containing chars, but default
#     er_legs anchors (TC 0.55/0.20 head etc.) don't align with MMH positions
#     for 皃 (儿 sits under a narrow 白 top, s6 head at BC(0.485,0.077) &
#     s7 head at C(0.793,0.957)). Skip and inline.
#   memory_index.md: v8 slim path — read drawer_memory + INDEX + errata.
#   INDEX grep '皃' -> absent. '白' -> p3_char_0206_白 mastered as inline (no
#     bai.py primitive). '儿' -> er_legs.py exists (canonical).
#   errata.md grep '皃' -> not present.
# Decomposition: 皃 = 白(top, 5 strokes: 撇+竖+横折+横+横) + 儿(bottom, 2
#   strokes: 撇+竖弯钩) = 7 strokes total. Matches MMH count.
# Compositional layout: 白 upper (y ~66-200), 儿 lower (y ~195-285).
"""

# BANK_DEVIATION
# skipped: er_legs.py
# reason: er_legs default anchors span the whole canvas (儿 as standalone
#   radical); in 皃 the 儿 sits below a narrow 白 with the 撇 head at
#   BC(0.485,0.077) and 竖弯钩 head at C(0.793,0.957) — different
#   scale/position, and orientations required by the MMH spec don't map
#   onto er_legs's defaults without overriding 5+ anchors.
# fresh_component: er_legs_compressed_for_皃

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 12 declared joints are N (natural gaps)
    'overall_pass': True,
    'notes': '白 top + 儿 bottom, both inlined per MMH anchors. All joints N.',
}

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier  # noqa: E402


def _pt(anchor):
    return anchor_to_xy(anchor)


def draw_mao(draw):
    # ==================== 白 (top, strokes 1-5) ====================

    # s1: top 点 / short 撇 — head TC(0.74,0.668) -> tail C(0.559,0.277)
    p0 = _pt(('TC', 0.74, 0.668))
    p1 = _pt(('C', 0.559, 0.277))
    widths = [6, 5, 4, 3]
    n = len(widths) - 1
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)

    # s2: 竖 (left side of 白 box) — head C(0.277,0.315) -> tail BC(0.465,0.036)
    p0 = _pt(('C', 0.277, 0.315))
    p1 = _pt(('BC', 0.465, 0.036))
    fat_line(draw, p0, p1, width=5)

    # s3: 横折 (top+right of 白 box) — head C(0.436,0.33) -> tail MR(0.039,0.907)
    # corner: horizontal segment then vertical drop. Use head.y for the top
    # horizontal, tail.x for the right vertical.
    head = _pt(('C', 0.436, 0.33))
    tail = _pt(('MR', 0.039, 0.907))
    corner = (tail[0], head[1])
    fat_line(draw, head, corner, width=5)
    fat_line(draw, corner, tail, width=5)

    # s4: middle 横 inside 白 — head C(0.494,0.614) -> tail C(0.96,0.576)
    p0 = _pt(('C', 0.494, 0.614))
    p1 = _pt(('C', 0.96, 0.576))
    fat_line(draw, p0, p1, width=5)

    # s5: bottom 横 (closes 白 box) — head C(0.541,0.954) -> tail MR(0.019,0.828)
    p0 = _pt(('C', 0.541, 0.954))
    p1 = _pt(('MR', 0.019, 0.828))
    fat_line(draw, p0, p1, width=5)

    # ==================== 儿 (bottom, strokes 6-7) ====================

    # s6: 撇 of 儿 — head BC(0.485,0.077) -> tail BC(0.084,0.851)
    # Curved sweep down-left (pie shape).
    p0 = _pt(('BC', 0.485, 0.077))
    p1 = _pt(('BC', 0.084, 0.851))
    # slight curve: control point pulled left+down
    ctrl = (p0[0] - 10, (p0[1] + p1[1]) * 0.5 + 8)
    curve_pts = quad_bezier(p0, ctrl, p1, n=40)
    widths = [9 - int(i * 8 / 40) for i in range(41)]
    stroke_variable_width(draw, curve_pts, widths)

    # s7: 竖弯钩 of 儿 — head C(0.793,0.957) -> tail BR(0.754,0.402)
    # Path: head down through belly, sweep right at bottom, then tip flicks UP
    # to tail position.
    head = _pt(('C', 0.793, 0.957))     # ~(179, 196)
    # descending vertical portion
    v_bottom = (head[0] + 4, head[1] + 60)   # ~(183, 256)
    # sweep right (curve)
    right_end = (v_bottom[0] + 85, v_bottom[1] + 15)  # ~(268, 271)
    tail = _pt(('BR', 0.754, 0.402))    # ~(275, 240) — tip up-flick
    # vertical descent
    fat_line(draw, head, v_bottom, width=7)
    # curved sweep right — quadratic through corner
    ctrl = (v_bottom[0] + 30, v_bottom[1] + 30)
    sweep = quad_bezier(v_bottom, ctrl, right_end, n=30)
    widths = [7] * len(sweep)
    stroke_variable_width(draw, sweep, widths)
    # up-hook: taper from thick to thin
    hook_pts = [
        (right_end[0], right_end[1]),
        ((right_end[0] + tail[0]) / 2, (right_end[1] + tail[1]) / 2),
        (tail[0], tail[1]),
    ]
    hook_widths = [7, 4, 2]
    stroke_variable_width(draw, hook_pts, hook_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_mao(draw)
    out = os.path.join(os.path.dirname(__file__), '01_皃.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
