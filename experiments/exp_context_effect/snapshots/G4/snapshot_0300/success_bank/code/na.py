"""捺 (nà) — right-falling stroke, TL→BR, thin head, peak swell, needle tip.

Signature:
  draw_na(draw, from_anchor, to_anchor,
          head_width=3, peak_width=14, tail_width=1,
          peak_t=0.8, curve=0.10, segments=48)

Head thin, swells to `peak_width` near `peak_t` (~80% of stroke), then
tapers to a needle-tip 出锋. Bowed gently along the chord perpendicular.

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_04_捺 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_na(draw, from_anchor, to_anchor,
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48,
            color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perpendicular; 捺 bows outward (toward BL of the chord).
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= peak_t:
            u = t / peak_t
            w = head_width + (peak_width - head_width) * u
        else:
            u = (t - peak_t) / max(1e-6, (1.0 - peak_t))
            w = peak_width + (tail_width - peak_width) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths, color=color)
