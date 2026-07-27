"""氵 (shuǐ, "3 drops of water", 3 strokes) — B2 pass.

Left-side radical. Three strokes clearly separated (S-class); the two
upper 点 are small tilted dots, the bottom is a rising 提.
No bank primitive for 提 yet — inlined here as draw_ti helper.

Strokes:
  s1 — 点 (upper, tilted down-right).
  s2 — 点 (middle, tilted down-right toward center).
  s3 — 提 (rising, thick head at BL / thin tip up-right).

Joints: NONE (all separate, S-class).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from dian import draw_dian


def draw_ti_inline(draw, from_anchor, to_anchor,
                   head_width=14, tail_width=2, curve=-0.05, segments=32,
                   color=(0, 0, 0)):
    """提 — rising stroke, thick head → needle tip up-right."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
    r = head_width / 2.0
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=color)


def draw_shui(draw,
              s1_head=('TC', 0.195, 0.771), s1_tail=('C',  0.629, 0.104),
              s2_head=('ML', 0.929, 0.395), s2_tail=('C',  0.312, 0.688),
              s3_head=('BC', 0.166, 0.944), s3_tail=('C',  0.743, 0.901)):
    draw_dian(draw, s1_head, s1_tail, head_width=2, peak_width=11, curve=0.08)
    draw_dian(draw, s2_head, s2_tail, head_width=2, peak_width=11, curve=0.08)
    draw_ti_inline(draw, s3_head, s3_tail,
                   head_width=14, tail_width=2, curve=-0.05)
