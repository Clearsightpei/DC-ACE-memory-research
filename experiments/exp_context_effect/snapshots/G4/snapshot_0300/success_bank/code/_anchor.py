"""米字格 anchor helper (G4 grid-bank).

Standardized on the PIL-native convention (y grows DOWN within each cell,
matching the majority of batch-1 attempts and the sandbox recommendation).

Anchor tuple:  (cell, x_frac, y_frac)
  cell  : one of 'TL','TC','TR','ML','C','MR','BL','BC','BR'
  x_frac: 0..1 from cell LEFT edge
  y_frac: 0..1 from cell TOP  edge  (PIL convention — y grows DOWN)

Canvas: 300 x 300 PIL pixels. Each cell = 100 x 100.
"""

CANVAS = 300
_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor_to_xy(anchor):
    """(cell, x_frac, y_frac) -> PIL pixel coords (px, py)."""
    cell, xf, yf = anchor
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)


# ---- Curve sampling + variable-width polyline (shared primitives) ----

def quad_bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_variable_width(draw, pts, widths, color=(0, 0, 0)):
    """Draw a polyline with per-vertex widths; discs at each vertex for smoothness."""
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=color, width=w)
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)


def fat_line(draw, p0, p1, width, color=(0, 0, 0)):
    """Uniform-width line with rounded caps."""
    draw.line([p0, p1], fill=color, width=int(round(width)))
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)


def sample_line(p0, p1, n=40):
    return [(p0[0] + i / n * (p1[0] - p0[0]),
             p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
