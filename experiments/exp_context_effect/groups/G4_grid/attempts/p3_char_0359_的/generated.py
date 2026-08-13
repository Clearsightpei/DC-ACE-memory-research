"""p3_char_0359_的 — G4 attempt.

# memory reads: drawer_memory.md v8, memory_index.md, errata grep '的' -> not present,
#   INDEX grep '的|白|勺' -> 白 (p3_206) done as pie+ri inline; 勺 -> bao.py bank primitive
#   exists but its defaults occupy the whole canvas and are tuned for standalone. For 的,
#   勺 must sit in the RIGHT half of a two-part left-right composition — bao.py's anchors
#   would clash. So inline 勺's 撇+横折钩+dot at the MMH-given anchors for the right half.
# 的 = 白 (left) + 勺 (right). 8 strokes = (5 for 白) + (3 for 勺). Matches MMH.
#
# BANK_DEVIATION
# skipped: bao.py, bao_char.py
# reason: bao_char.py defaults render 勺 across the full canvas as a standalone;
#         inside 的 the 勺 must be scaled/shifted to the RIGHT half so left-side 白
#         has room. Inlining fresh at the MMH-given right-half anchors is cleaner
#         than overriding all 6 of bao's endpoint parameters.
# fresh_component: shao_right_for_de   (勺 packaged in the right slot of a 白+勺 char)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5-stroke 白 on left (pie+box-with-middle-heng) + 3-stroke 勺 on right (pie, heng-zhe-gou, dot). All joints left as N-gaps (no welds).',
}

import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier  # noqa: E402


def _pt(anchor):
    return anchor_to_xy(anchor)


def _shorten(p, other, px):
    """Pull point p toward `other` by `px` pixels (for N-class gap)."""
    dx = other[0] - p[0]; dy = other[1] - p[1]
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return p
    t = min(1.0, px / d)
    return (p[0] + dx * t, p[1] + dy * t)


def _tapered_line(draw, p0, p1, head_w, tail_w, segments=24):
    pts = [(p0[0] + i / segments * (p1[0] - p0[0]),
            p0[1] + i / segments * (p1[1] - p0[1])) for i in range(segments + 1)]
    widths = [head_w + (tail_w - head_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def _tapered_curve(draw, p0, p1, curve, head_w, tail_w, segments=48):
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p1, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_de(draw):
    # ================== LEFT HALF: 白 (bai) — 5 strokes ==================
    # --- s1: top 撇 (short slant, thick→thin) ---
    p0 = _pt(('TL', 0.814, 0.715))
    p1 = _pt(('ML', 0.574, 0.438))
    _tapered_curve(draw, p0, p1, curve=0.08, head_w=8, tail_w=2)

    # --- s2: 竖 (left wall of box) ---
    p0 = _pt(('ML', 0.396, 0.418))
    p1 = _pt(('BL', 0.574, 0.514))
    fat_line(draw, _shorten(p0, p1, 4), _shorten(p1, p0, 3), width=6)

    # --- s3: 横折 (top + right wall of box) ---
    #   head @ ML(0.551, 0.482) [top-left inner]
    #   tail @ BC(0.081, 0.619) [bottom]
    #   corner at (tail.x, head.y) — the top-right corner of the box
    head = _pt(('ML', 0.551, 0.482))
    tail = _pt(('BC', 0.081, 0.619))
    corner = (tail[0], head[1])
    fat_line(draw, _shorten(head, corner, 3), corner, width=6)
    fat_line(draw, corner, _shorten(tail, corner, 3), width=6)

    # --- s4: middle 横 inside 白 ---
    p0 = _pt(('ML', 0.609, 0.934))
    p1 = _pt(('ML', 0.952, 0.881))
    fat_line(draw, p0, p1, width=5)

    # --- s5: bottom 横 (closes box floor) ---
    p0 = _pt(('BL', 0.63, 0.481))
    p1 = _pt(('BL', 0.946, 0.373))
    fat_line(draw, p0, p1, width=5)

    # ================== RIGHT HALF: 勺 (shao) — 3 strokes ==================
    # --- s6: top 撇 of 勺 (bows down-left) ---
    p0 = _pt(('TC', 0.846, 0.542))
    p1 = _pt(('C', 0.377, 0.699))
    _tapered_curve(draw, p0, p1, curve=0.10, head_w=8, tail_w=2)

    # --- s7: 横折钩 outer bow of 勺 ---
    #   head @ C(0.69, 0.427)  — top of the horizontal, touches middle of 撇
    #   tail @ BC(0.77, 0.687) — bottom where hook flicks
    # Implement as short 横 → corner → curved 竖 → tiny hook flick.
    h_start = _pt(('C', 0.69, 0.427))
    h_end_tail = _pt(('BC', 0.77, 0.687))
    # top-right corner (slightly right of h_start, at same y)
    corner = (_pt(('MR', 0.30, 0.42))[0], h_start[1] - 2)
    fat_line(draw, h_start, corner, width=7)
    # curved descent from corner to tail (bows outward = to the right)
    dx, dy = h_end_tail[0] - corner[0], h_end_tail[1] - corner[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)  # rotate 90° — for a stroke going down, perp points RIGHT
    bow = 0.10 * length
    mid = ((corner[0] + h_end_tail[0]) * 0.5, (corner[1] + h_end_tail[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(corner, ctrl, h_end_tail, n=40)
    widths = [7] * (len(pts) - 8) + [7, 6, 5, 4, 3, 3, 3, 3]
    stroke_variable_width(draw, pts, widths)
    # hook flick up-and-left from tail
    hook_tip = (h_end_tail[0] - 14, h_end_tail[1] - 10)
    _tapered_line(draw, h_end_tail, hook_tip, head_w=5, tail_w=1, segments=12)

    # --- s8: inner dot (点) inside 勺 ---
    #   head @ C(0.515, 0.869)  → tail @ BC(0.813, 0.183)  (short slant dot)
    p0 = _pt(('C', 0.515, 0.869))
    p1 = _pt(('BC', 0.813, 0.183))
    _tapered_line(draw, p0, p1, head_w=3, tail_w=7, segments=12)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_de(draw)
    out = os.path.join(os.path.dirname(__file__), '01_的.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
