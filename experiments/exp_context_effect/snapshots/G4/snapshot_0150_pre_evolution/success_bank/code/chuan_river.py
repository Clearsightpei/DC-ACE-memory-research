"""巛 (chuān, "river/stream", 3 strokes) — B1 pass.

Three parallel gentle-curve strokes with thin-head → belly → tapered
tail. No bank primitive fits, so we inline a helper.

Joints: none (S-class — three separate strokes).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def _draw_chuan_stroke(draw, head_anchor, tail_anchor,
                       head_w=6, belly_w=8, tail_w=2,
                       curve=0.06, segments=60):
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= 0.5:
            u = t / 0.5
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.5) / 0.5
            w = belly_w + (tail_w - belly_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_chuan_river(draw,
                     s1=(('TL', 0.885, 0.858), ('BC', 0.081, 0.842)),
                     s2=(('TC', 0.494, 0.829), ('BC', 0.699, 0.798)),
                     s3=(('TR', 0.145, 0.797), ('BR', 0.414, 0.818))):
    for head, tail in (s1, s2, s3):
        _draw_chuan_stroke(draw, head, tail, curve=0.06)
