"""丿 (piě) standalone radical — canonical hand-written primitive.

Chronic-cluster item, promoted at position 300 after 4 failed retries.

Baked anchors (do NOT tune per composition):
  head = ('TR', 0.85, 0.15)   # far upper-right corner
  tail = ('BL', 0.15, 0.85)   # far lower-left corner
  head_width = 16, tail_width = 1
  curve = 0.15  (bow perpendicular to chord, gentle)

This is the errata anchor plan verbatim. It fills the 米字格 as a
radical is expected to (TR9). Do NOT override — that is what has
failed 4 times.

Joint: single stroke, no joints.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_pie_radical(draw, color=(0, 0, 0)):
    head = ('TR', 0.85, 0.15)
    tail = ('BL', 0.15, 0.85)
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = 0.15 * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    segments = 64
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [16 + (1 - 16) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
