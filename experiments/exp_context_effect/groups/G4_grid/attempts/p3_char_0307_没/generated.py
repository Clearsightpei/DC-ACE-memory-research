"""没 (méi) — p3_char_0307. 7 strokes = 氵 (3) + 殳 (4).

Split: 没 = 氵 (left radical) + 殳 (right).
  s1-s3: 氵 (2 dots + 提)
  s4-s5: top of 殳 (short 撇 + 横折弯钩 = 几-like)
  s6-s7: 又 (横撇 + 捺, welded X in lower half — joint P)

Anchors follow MMH per-stroke endpoints from brief. Cell size 100 px,
canvas 300 px, PIL convention (y grows DOWN).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; s6/s7 welded X (P); s3.tail-s4.tail-s7.head N gaps at C.',
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from dian import draw_dian


def draw_ti(draw, from_anchor, to_anchor,
            head_width=14, tail_width=2, curve=-0.05, segments=32,
            color=(0, 0, 0)):
    """提 — rising stroke."""
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


def draw_pie_curve(draw, from_anchor, to_anchor,
                   head_width=10, tail_width=2, curve=0.06, segments=48,
                   color=(0, 0, 0)):
    """撇 — thick head at TOP, needle tail at BOTTOM-LEFT."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_heng_zhe_wan_gou(draw, head_anchor, corner_anchor, tail_anchor,
                          width=8, color=(0, 0, 0)):
    """横折弯钩 — starts horizontal from head, sharp corner, then curves
    down to the tail. Two-segment: straight 横 from head→corner, then a
    quadratic curve corner→tail via a control point pulled outward.
    """
    p0 = anchor_to_xy(head_anchor)
    pc = anchor_to_xy(corner_anchor)
    p2 = anchor_to_xy(tail_anchor)
    # Segment 1: straight 横 from head to corner
    fat_line(draw, p0, pc, width=width, color=color)
    # Segment 2: curved 弯 from corner to tail with control pulled down-right
    ctrl = (pc[0] + (p2[0] - pc[0]) * 0.2, pc[1] + (p2[1] - pc[1]) * 0.9)
    pts = quad_bezier(pc, ctrl, p2, n=32)
    widths = [width] * len(pts)
    widths[-1] = max(2, width - 3)
    stroke_variable_width(draw, pts, widths, color=color)


def draw_heng_pie_two_seg(draw, head_anchor, corner_anchor, tail_anchor,
                          width=7, color=(0, 0, 0)):
    """横撇 — straight 横 from head to corner, then straight 撇 tapering
    to the tail. Two-segment for clean angular read.
    """
    p0 = anchor_to_xy(head_anchor)
    pc = anchor_to_xy(corner_anchor)
    p2 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, pc, width=width, color=color)
    # Tapering 撇 segment
    n = 24
    pts = [(pc[0] + (p2[0] - pc[0]) * i / n,
            pc[1] + (p2[1] - pc[1]) * i / n) for i in range(n + 1)]
    widths = [width + (2 - width) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_heng_pie_curve(draw, from_anchor, to_anchor,
                        width=7, curve=0.08, segments=48,
                        color=(0, 0, 0)):
    """横撇 — starts near horizontal then bends down-left. Approximated
    as a curved fat line (endpoints only from MMH)."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths, color=color)


def draw_na_curve(draw, from_anchor, to_anchor,
                  head_width=3, peak_width=14, tail_width=1,
                  peak_t=0.75, curve=0.08, segments=48,
                  color=(0, 0, 0)):
    """捺 — swelling right-diagonal to needle tip."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)  # bow toward BL of chord
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)

    def w_at(t):
        if t < peak_t:
            u = t / peak_t
            return head_width + (peak_width - head_width) * u
        u = (t - peak_t) / (1 - peak_t)
        return peak_width + (tail_width - peak_width) * u

    widths = [w_at(i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 氵 (left radical, s1-s3) ----
    # s1: upper 点 — TL(0.715,0.712) → TC(0.031,0.993)
    draw_dian(draw, ('TL', 0.715, 0.712), ('TC', 0.031, 0.993),
              head_width=2, peak_width=11, curve=0.08)
    # s2: middle 点 — ML(0.425,0.304) → ML(0.694,0.532)
    draw_dian(draw, ('ML', 0.425, 0.304), ('ML', 0.694, 0.532),
              head_width=2, peak_width=11, curve=0.08)
    # s3: 提 — BL(0.595,0.839) → ML(0.996,0.819)
    draw_ti(draw, ('BL', 0.595, 0.839), ('ML', 0.996, 0.819),
            head_width=13, tail_width=2, curve=-0.04)

    # ---- 殳 top: 撇 + 横折弯钩 (几-like), s4-s5 ----
    # s4: 撇 — TC(0.304,0.838) → C(0.043,0.72)  [short pie, goes down-left slightly]
    draw_pie_curve(draw, ('TC', 0.304, 0.838), ('C', 0.043, 0.72),
                   head_width=9, tail_width=2, curve=0.05)
    # s5: 横折弯钩 — TC(0.518,0.873) → MR(0.599,0.538)
    # Two-segment: horizontal from head across TC/TR, sharp corner near
    # top of TR, then curve down to MR tail.
    draw_heng_zhe_wan_gou(draw,
                          head_anchor=('TC', 0.518, 0.873),
                          corner_anchor=('TR', 0.60, 0.90),
                          tail_anchor=('MR', 0.599, 0.538),
                          width=8)

    # ---- 又 (bottom of 殳), s6-s7 welded X ----
    # s6: 横撇 — C(0.371,0.852) → BL(0.987,0.771). Two-segment:
    # horizontal short from head to corner near C(0.9,0.9), then 撇
    # down-left to tail.
    draw_heng_pie_two_seg(draw,
                          head_anchor=('C', 0.371, 0.852),
                          corner_anchor=('C', 0.90, 0.90),
                          tail_anchor=('BL', 0.987, 0.771),
                          width=7)
    # s7: 捺 — C(0.184,0.998) → BR(0.845,0.921)
    draw_na_curve(draw, ('C', 0.184, 0.998), ('BR', 0.845, 0.921),
                  head_width=3, peak_width=14, tail_width=1,
                  peak_t=0.78, curve=0.08)

    out_png = os.path.join(_HERE, '01_没.png')
    img.save(out_png)
    print('Wrote', out_png)


if __name__ == '__main__':
    main()
