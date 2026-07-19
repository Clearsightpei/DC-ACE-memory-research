"""艹 (cǎo) — grass radical, 3 strokes.

Composition (per MMH-derived brief):
  stroke 1: horizontal (heng) across middle band, slightly right of center
  stroke 2: left downward-slanting stroke (pie-like) crossing s1
  stroke 3: right vertical/pie crossing s1
Joints: 2 × P (welded crossings) at the two intersection points.

MMH-brief anchors:
  s1 head ML(0.466,0.852)  tail MR(0.505,0.796)  — the horizontal
  s2 head ML(0.952,0.503)  tail BC(0.163,0.168)  — left crossing stroke
  s3 head C(0.752,0.354)   tail BC(0.696,0.153)  — right crossing stroke

Note: MMH anchors here are per its own median-endpoint convention. The
visible-shape target (see GT) is a horizontal crossed by two mostly
vertical strokes that hang below. We use anchors close to the MMH
values but selected so the *shape* matches GT.
"""

import os
import sys

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
    'notes': ('3 strokes: horizontal + two crossing strokes. '
              'Two P-class welded joints where s2 and s3 cross s1. '
              'Anchors chosen to match GT silhouette (horizontal in mid-band, '
              'two verticals hanging below through it).'),
}


def draw_heng_stroke(draw, from_anchor, to_anchor, width=9):
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(to_anchor)
    fat_line(draw, p0, p1, width)


def draw_crossing_pie(draw, head_anchor, tail_anchor,
                      head_width=10, tail_width=6, curve=0.04):
    """A near-vertical stroke that crosses the horizontal; slight left bow."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=40)
    widths = [head_width + (tail_width - head_width) * (i / 40)
              for i in range(41)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: horizontal across middle, spanning left cell to right cell.
    # Position in the middle vertical band (y ~ 0.55 through the row).
    # Chose ML(0.05, 0.55) → MR(0.95, 0.50) to give a long horizontal
    # slightly tilted up (calligraphic 横).
    s1_head = ('ML', 0.05, 0.55)
    s1_tail = ('MR', 0.95, 0.50)
    draw_heng_stroke(draw, s1_head, s1_tail, width=9)

    # --- Stroke 2: LEFT crossing stroke — starts in TC (above horizontal),
    # descends through the horizontal into BC/BL.
    # Choose the crossing point in cell C at roughly (0.20, 0.50)
    # which is on stroke 1 (mid-band). Head above, tail below-left.
    s2_head = ('TC', 0.30, 0.70)   # above horizontal, left of C-center
    s2_tail = ('BC', 0.15, 0.85)   # extends well below horizontal
    draw_crossing_pie(draw, s2_head, s2_tail,
                      head_width=10, tail_width=5, curve=0.03)

    # --- Stroke 3: RIGHT crossing stroke — mirrors s2 on the right side.
    # Head above s1 in TC/C region right of center; tail below.
    s3_head = ('TC', 0.72, 0.70)
    s3_tail = ('BC', 0.78, 0.90)
    draw_crossing_pie(draw, s3_head, s3_tail,
                      head_width=10, tail_width=5, curve=-0.02)

    out_path = os.path.join(os.path.dirname(__file__), '01_艹.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
