"""Bank primitive: 回 (huí, 'return' — 6 strokes = double 口, outer + inner).

Promoted from p3_char_0259_回 (G5 B8 PASS). Simply 2 nested draw_kou calls
with different (ox, oy, scale) — a clean composition-of-primitives case.

Reuse targets: 回 (identity), 苘, 迴, 徊, 洄.
"""

from kou_mouth import draw_kou


def draw_hui_return(draw, ox=0, oy=0, scale=1.0):
    # Outer 口 spans most of canvas.
    # draw_kou_mouth natural box: x in [92, 225], y in [122, 275] approx.
    outer_scale = 1.55 * scale
    outer_ox = ox + (50 - 92 * outer_scale)
    outer_oy = oy + (40 - 122 * outer_scale)
    draw_kou(draw, ox=outer_ox, oy=outer_oy, scale=outer_scale)

    # Inner 口 nested near center.
    inner_scale = 0.60 * scale
    inner_ox = ox + (115 - 92 * inner_scale)
    inner_oy = oy + (115 - 122 * inner_scale)
    draw_kou(draw, ox=inner_ox, oy=inner_oy, scale=inner_scale)
