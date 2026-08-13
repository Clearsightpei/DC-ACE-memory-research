# nian_horns.py — 廾 (nian, "clasped hands"), 4 strokes.
# PASSed at p3_char_0092_廾 (B5, pos 254). Inline PIL: short 横 cap +
# long 撇 curve + long crossbar 横 + right 竖. Named "horns" to avoid
# collision with existing nian_char (卄) and gong_radical (廾 variant).

import math  # noqa: F401


def draw_nian_horns(t, ox=0, oy=0, scale=1.0):
    """廾 — 4 strokes, inline PIL bezier + line."""
    w = max(1, int(round(6 * scale)))

    def P(bx, by):
        return (150 + ox + bx * scale, 150 - oy - by * scale)

    def _curve(p0, p1, p2, width, steps=40):
        pts = []
        for i in range(steps + 1):
            u = i / steps
            x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
            y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
            pts.append((x, y))
        t.line(pts, fill=(0, 0, 0), width=width)

    # Stroke 1: short 横 cap top-left.
    t.line([P(-55, +40), P(-18, +40)], fill=(0, 0, 0), width=w)

    # Stroke 2: long 撇 — starts high near cap end, curves down-left.
    _curve(P(-20, +45), P(-40, -25), P(-72, -85), width=w)

    # Stroke 3: long horizontal crossbar.
    t.line([P(-95, -15), P(+90, -15)], fill=(0, 0, 0), width=w)

    # Stroke 4: right 竖 — vertical from upper-mid to bottom.
    t.line([P(+40, +50), P(+45, -90)], fill=(0, 0, 0), width=w)
