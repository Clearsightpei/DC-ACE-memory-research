"""Bank primitive: 乚 (radical — single J-hook curve).

Promoted from p2_radical_007_乚 (G5 bootstrap PASS, 2026-08-08).
Single stroke: descends from upper-left, sweeps right along the bottom,
terminates in a small hook up-right. Useful as a component of 也, 己, 巳.
Rendered as a polyline through hand-tuned control points.
"""

from PIL import ImageDraw


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yi_hook(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 乚 at (ox, oy). Reference canvas 300x300."""
    path = [_tx(95, 130, ox, oy, scale),
            _tx(93, 160, ox, oy, scale),
            _tx(93, 200, ox, oy, scale),
            _tx(98, 225, ox, oy, scale),
            _tx(115, 240, ox, oy, scale),
            _tx(150, 245, ox, oy, scale),
            _tx(190, 245, ox, oy, scale),
            _tx(218, 240, ox, oy, scale),
            _tx(230, 220, ox, oy, scale),
            _tx(233, 195, ox, oy, scale),
            _tx(233, 169, ox, oy, scale)]

    width = int(8 * scale)
    for a, b in zip(path[:-1], path[1:]):
        draw.line([a, b], fill='black', width=width)
    r = width // 2
    for p in path:
        draw.ellipse([p[0] - r, p[1] - r,
                      p[0] + r, p[1] + r], fill='black')
