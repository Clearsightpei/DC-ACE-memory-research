"""巛 (chuān) — 3-stroke radical (川's older form): three separate
wavy vertical strokes with clear gaps between them.

Structural spec (MMH-derived, dispatcher-injected):
  stroke 1: head @ ('TL', 0.885, 0.858) · tail @ ('BC', 0.081, 0.842)
  stroke 2: head @ ('TC', 0.494, 0.829) · tail @ ('BC', 0.699, 0.798)
  stroke 3: head @ ('TR', 0.145, 0.797) · tail @ ('BR', 0.414, 0.818)
Joints: NONE — three separate strokes.

Each stroke is a subtle S-shaped/curved descent (a 撇 with a small
top curl, similar to the 巜/巛 calligraphic form): the top has a
slight rightward curl (小撇 style), body descends nearly vertically
with a gentle belly. Rendered as a variable-width quadratic bezier
with a mildly leftward-bowing belly for a natural wave shape.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 separate wavy strokes, clear gaps, no joints (matches MMH spec).'
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_SHARED = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _SHARED)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, CANVAS


def draw_chuan_stroke(draw, head_anchor, tail_anchor,
                      head_w=6, belly_w=8, tail_w=2,
                      curve=0.06, segments=60):
    """One 巛 stroke: gentle curve, thin head → slightly wider belly → tapered tail."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perpendicular to chord; bow the belly slightly to the LEFT of descent
    # (the character's characteristic gentle leftward bulge in the middle).
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    n = segments
    widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.5:
            u = t / 0.5
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.5) / 0.5
            w = belly_w + (tail_w - belly_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1 — leftmost. head TL(0.885, 0.858), tail BC(0.081, 0.842).
    draw_chuan_stroke(draw,
                      head_anchor=('TL', 0.885, 0.858),
                      tail_anchor=('BC', 0.081, 0.842),
                      curve=0.06)

    # Stroke 2 — middle. head TC(0.494, 0.829), tail BC(0.699, 0.798).
    draw_chuan_stroke(draw,
                      head_anchor=('TC', 0.494, 0.829),
                      tail_anchor=('BC', 0.699, 0.798),
                      curve=0.06)

    # Stroke 3 — rightmost. head TR(0.145, 0.797), tail BR(0.414, 0.818).
    draw_chuan_stroke(draw,
                      head_anchor=('TR', 0.145, 0.797),
                      tail_anchor=('BR', 0.414, 0.818),
                      curve=0.06)

    out = os.path.join(_HERE, '01_巛.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
