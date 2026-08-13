"""原 (yuán) — 10 strokes.
Decomposition: 原 = 厂 (s1+s2) + 白 (s3-s7) + 小/水底 (s8-s10).
Reading order per memory_index: drawer_memory (A-recipe), INDEX grep,
errata grep. `chang.py` exists for 厂 but its default anchors are for
the standalone radical filling the canvas; here 厂 wraps 白+小 across
the full character so the standalone primitive doesn't fit. Inlining
per MMH-verbatim anchors following B12 A-recipe (points 1-5).
"""
# BANK_DEVIATION
# skipped: chang.py
# reason: chang.py bakes standalone-radical anchors (s1 in TC/TR band,
#   s2 tail at BL); here MMH puts s1 spanning TL(0.98,0.84)->TR(0.24,0.74)
#   and s2 spanning TL(0.77,0.77)->BL(0.23,0.83), i.e. 厂 wraps the
#   full character not just top-left. Inlining with MMH-verbatim anchors.
# fresh_component: chang_wrap_for_compound

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; N-joints preserved as gaps '
             '(no explicit welds). s5 heng-zhe corner synthesized at '
             '(MR,0.01,0.37) since MMH gives only head/tail.',
}


def draw_pie_curve(draw, head_anchor, tail_anchor,
                   head_w=11, tail_w=1, curve=0.10, segs=48):
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segs)
    widths = [head_w + (tail_w - head_w) * (i / segs)
              for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 横 (top of 厂). TL(0.98,0.84) -> TR(0.24,0.74).
    fat_line(d, anchor_to_xy(('TL', 0.984, 0.838)),
                anchor_to_xy(('TR', 0.241, 0.735)), width=8)

    # s2 — 撇 (left sweep of 厂). TL(0.77,0.77) -> BL(0.23,0.83). Long pie.
    draw_pie_curve(d, ('TL', 0.773, 0.771), ('BL', 0.226, 0.83),
                   head_w=11, tail_w=2, curve=0.09)

    # s3 — 撇 (top short pie of 白). TC(0.68,0.94) -> C(0.37,0.33).
    draw_pie_curve(d, ('TC', 0.682, 0.94), ('C', 0.365, 0.327),
                   head_w=6, tail_w=1, curve=0.06)

    # s4 — 竖 (left of 白/日 frame). C(0.09,0.35) -> BC(0.36,0.04).
    fat_line(d, anchor_to_xy(('C', 0.093, 0.351)),
                anchor_to_xy(('BC', 0.356, 0.042)), width=7)

    # s5 — 横折 (top+right of 白 frame). C(0.25,0.37) -> MR(0.01,0.96).
    # MMH gives only head/tail; synthesize corner at right end of top
    # heng (share x with tail, y with head).
    s5_head = anchor_to_xy(('C', 0.248, 0.371))
    s5_tail = anchor_to_xy(('MR', 0.013, 0.96))
    s5_corner = (s5_tail[0], s5_head[1])
    fat_line(d, s5_head, s5_corner, width=7)
    fat_line(d, s5_corner, s5_tail, width=7)

    # s6 — middle 横 inside 白. C(0.35,0.69) -> C(0.84,0.62).
    fat_line(d, anchor_to_xy(('C', 0.354, 0.69)),
                anchor_to_xy(('C', 0.843, 0.617)), width=6)

    # s7 — bottom 横 of 白. C(0.40,0.97) -> C(0.90,0.87).
    fat_line(d, anchor_to_xy(('C', 0.4, 0.969)),
                anchor_to_xy(('C', 0.896, 0.866)), width=6)

    # s8 — 撇 (center of 小 / left leg). C(0.60,0.97) -> BC(0.30,0.72).
    draw_pie_curve(d, ('C', 0.6, 0.972), ('BC', 0.301, 0.722),
                   head_w=8, tail_w=1, curve=0.06)

    # s9 — 短撇/左点 (left dot area of 小). BC(0.13,0.28) -> BL(0.90,0.74).
    fat_line(d, anchor_to_xy(('BC', 0.128, 0.279)),
                anchor_to_xy(('BL', 0.899, 0.739)), width=6)

    # s10 — 右点 (right dot of 小). BR(0.06,0.27) -> BR(0.49,0.68).
    fat_line(d, anchor_to_xy(('BR', 0.057, 0.271)),
                anchor_to_xy(('BR', 0.487, 0.678)), width=7)

    # Save
    out = os.path.join(os.path.dirname(__file__), '01_原.png')
    img.save(out)
    print(f'wrote {out}; strokes=10')


if __name__ == '__main__':
    main()
