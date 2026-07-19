"""辶 (chuò, "walk radical", 3 strokes) — B1 pass.

All strokes are inlined as variable-width polylines from MMH medians —
no bank primitive fits the compound S-shape or the wavy 平捺 cleanly.

Strokes:
  s1 — 点 (small dot upper-left, thin head → thick tail).
  s2 — 横折折撇 (compact S-shape sitting in left column).
  s3 — 平捺 (long wavy sweep across the bottom).

Joint: s2.tail ⇆ s3 body near t=0.25 → N (small gap ~14 px).
"""
from _anchor import anchor_to_xy, stroke_variable_width


def _polyline(draw, anchors, widths):
    pts = [anchor_to_xy(a) for a in anchors]
    stroke_variable_width(draw, pts, widths)


def draw_chuo_walk(draw):
    # s1 dot
    _polyline(draw, [
        ('TL', 0.618, 0.718),
        ('TL', 0.867, 0.847),
        ('TL', 0.964, 0.967),
    ], [3, 9, 12])

    # s2 compound S
    s2 = [
        ('ML', 0.272, 0.550), ('ML', 0.390, 0.556),
        ('ML', 0.724, 0.444), ('ML', 0.791, 0.459),
        ('ML', 0.838, 0.500), ('ML', 0.817, 0.623),
        ('ML', 0.727, 0.790), ('ML', 0.706, 0.872),
        ('ML', 0.730, 0.975),
        ('BL', 0.797, 0.095), ('BL', 0.850, 0.256),
        ('BL', 0.855, 0.326), ('BL', 0.841, 0.370),
        ('BL', 0.814, 0.388),
    ]
    _polyline(draw, s2, [4, 7, 9, 10, 10, 10, 10, 9, 9, 8, 7, 5, 4, 3])

    # s3 long 平捺
    s3 = [
        ('BL', 0.284, 0.543), ('BL', 0.410, 0.575),
        ('BL', 0.568, 0.502), ('BL', 0.686, 0.469),
        ('BL', 0.873, 0.469),
        ('BC', 0.037, 0.513), ('BC', 0.638, 0.745),
        ('BR', 0.042, 0.848), ('BR', 0.329, 0.874),
        ('BR', 0.604, 0.821), ('BR', 0.689, 0.789),
    ]
    _polyline(draw, s3, [3, 5, 6, 6, 6, 7, 10, 13, 14, 10, 4])
