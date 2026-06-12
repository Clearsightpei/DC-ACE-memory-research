"""米字格 anchor notation ↔ turtle math-coords translator.

run_6 representation: every spatial decision is named in 9-cell grid
coordinates (or axis-intersection sugar), never in raw (x, y) magic
numbers. This module is the single translator between the two
representations.

Coordinate conventions:
- The character region spans turtle math-coords x ∈ [-150, +150],
  y ∈ [-150, +150] (the central 300×300 of the 800×600 canvas, math
  convention with origin at canvas center, y growing UP).
- The 米字格 partitions this region into 9 equal 100×100 cells.

Cells (named by row-then-column, like a phone keypad):

           x: [-150,-50)    [-50,+50]    (+50,+150]
y: (+50, +150]       TL          TC           TR
y: [-50, +50]        ML           C           MR
y: [-150, -50)       BL          BC           BR

Anchor notation (the user-facing form):
    (cell, x_frac, y_frac)
- cell ∈ {'TL','TC','TR','ML','C','MR','BL','BC','BR'}
- x_frac ∈ [0,1]: fraction from cell's LEFT edge (0 = left, 1 = right)
- y_frac ∈ [0,1]: fraction from cell's TOP edge (0 = top, 1 = bottom)
  (Reading-order convention — matches how a person says "upper-third
  of the cell".)

Axis-intersection sugar (also accepted as anchor input):
    {'V_left','V_mid','V_right','H_top','H_mid','H_bot'}
- 'V_left'  = x = -150         'H_top' = y = +150
- 'V_midL' = x = -50           'H_midT' = y = +50
- 'V_midR' = x = +50            'H_midB' = y = -50
- 'V_right' = x = +150         'H_bot' = y = -150
- An axis tuple like ('V_mid', 'H_mid') is resolved to a single point at
  the intersection. 'V_mid' is ambiguous between the two interior
  vertical lines; we treat 'V_mid' as the canvas-center vertical (x=0)
  and 'H_mid' as the canvas-center horizontal (y=0). For the cell
  boundary lines specifically use 'V_midL' / 'V_midR' / 'H_midT' /
  'H_midB'.

For the typical Drawer use case, the cell-relative form
`(cell, x_frac, y_frac)` is preferred. The axis form is sugar for
endpoints of stroke primitives that explicitly run along an axis (e.g.
一 starts at 'V_left ∩ H_mid', ends at 'V_right ∩ H_mid').
"""

# Cell name → (x_left, x_right, y_top, y_bottom) in turtle math-coords.
# y_top has the LARGER math-y (since y grows up); y_bottom has the smaller.
CELLS = {
    'TL': (-150, -50, +150, +50),
    'TC': (-50, +50, +150, +50),
    'TR': (+50, +150, +150, +50),
    'ML': (-150, -50, +50, -50),
    'C':  (-50, +50, +50, -50),
    'MR': (+50, +150, +50, -50),
    'BL': (-150, -50, -50, -150),
    'BC': (-50, +50, -50, -150),
    'BR': (+50, +150, -50, -150),
}

# Axis name → x value (for V_*) or y value (for H_*).
AXIS_X = {
    'V_left':  -150,
    'V_midL':  -50,
    'V_mid':    0,
    'V_midR':  +50,
    'V_right': +150,
}
AXIS_Y = {
    'H_top':   +150,
    'H_midT':  +50,
    'H_mid':    0,
    'H_midB':  -50,
    'H_bot':   -150,
}


def anchor_to_xy(anchor):
    """Translate an anchor (cell-relative tuple or axis-intersection tuple)
    to turtle math-coords (tx, ty).

    Accepted forms:
        ('TL', 0.3, 0.8)        — cell-relative
        ('V_mid', 'H_top')      — axis intersection (V_* then H_*)
        ('H_mid', 'V_left')     — axis intersection (H_* then V_*), order-agnostic

    Returns (tx, ty) as floats.
    """
    if not isinstance(anchor, tuple) or len(anchor) not in (2, 3):
        raise ValueError(f"anchor must be tuple of length 2 or 3, got {anchor!r}")

    # Cell-relative form: ('TL', 0.3, 0.8)
    if len(anchor) == 3:
        cell, xf, yf = anchor
        if cell not in CELLS:
            raise ValueError(f"unknown cell {cell!r}; valid: {sorted(CELLS)}")
        if not (0.0 <= xf <= 1.0 and 0.0 <= yf <= 1.0):
            raise ValueError(f"x_frac and y_frac must be in [0,1], got ({xf}, {yf})")
        x_left, x_right, y_top, y_bot = CELLS[cell]
        tx = x_left + xf * (x_right - x_left)
        # y_frac=0 means top edge (larger y); y_frac=1 means bottom (smaller y)
        ty = y_top + yf * (y_bot - y_top)
        return float(tx), float(ty)

    # Axis-intersection form: ('V_mid', 'H_top') or ('H_top', 'V_mid')
    a, b = anchor
    tx, ty = None, None
    for name in (a, b):
        if name in AXIS_X:
            if tx is not None:
                raise ValueError(f"two vertical axes in anchor {anchor!r}")
            tx = AXIS_X[name]
        elif name in AXIS_Y:
            if ty is not None:
                raise ValueError(f"two horizontal axes in anchor {anchor!r}")
            ty = AXIS_Y[name]
        else:
            raise ValueError(f"unknown axis {name!r} in anchor {anchor!r}")
    if tx is None or ty is None:
        raise ValueError(f"axis anchor needs one V_* and one H_*, got {anchor!r}")
    return float(tx), float(ty)


def xy_to_cell(tx, ty):
    """Identify which 米字格 cell a turtle-math-coord point falls in.

    Returns the cell name (e.g. 'TC'). For points on a cell boundary,
    ties are broken toward the cell with the more 'central' position
    (e.g. a point at x=-50, y=+25 → 'C', not 'ML').
    """
    if -50 <= tx <= 50:
        col = 'C'
    elif tx < -50:
        col = 'L'
    else:
        col = 'R'
    if -50 <= ty <= 50:
        row = 'M'
    elif ty > 50:
        row = 'T'
    else:
        row = 'B'
    return {'TL':'TL','TC':'TC','TR':'TR',
            'ML':'ML','MC':'C','MR':'MR',
            'BL':'BL','BC':'BC','BR':'BR'}[row + ('L' if col=='L' else ('R' if col=='R' else 'C'))]


def cell_relative_for_xy(tx, ty):
    """Inverse of anchor_to_xy: returns the closest (cell, x_frac, y_frac)
    representation for a turtle-math-coord point. Useful for showing the
    Drawer where its rendered endpoint actually landed, vs the declared
    anchor.
    """
    cell = xy_to_cell(tx, ty)
    x_left, x_right, y_top, y_bot = CELLS[cell]
    xf = (tx - x_left) / (x_right - x_left)
    yf = (ty - y_top) / (y_bot - y_top)
    return cell, round(xf, 3), round(yf, 3)


def distance(a, b):
    """Euclidean distance between two turtle-math-coord points."""
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5


# ─────────────────── Self-test ────────────────────────────────────
if __name__ == "__main__":
    # Sanity checks
    assert anchor_to_xy(('C', 0.5, 0.5)) == (0.0, 0.0), "canvas center"
    assert anchor_to_xy(('TC', 0.5, 0.0)) == (0.0, 150.0), "top-center, top edge"
    assert anchor_to_xy(('BC', 0.5, 1.0)) == (0.0, -150.0), "bottom-center, bottom edge"
    assert anchor_to_xy(('TL', 0.0, 0.0)) == (-150.0, 150.0), "top-left corner"
    assert anchor_to_xy(('BR', 1.0, 1.0)) == (150.0, -150.0), "bottom-right corner"
    # 30% from left, 80% from top of TC
    tx, ty = anchor_to_xy(('TC', 0.3, 0.8))
    assert tx == -20.0 and ty == 70.0, f"got ({tx}, {ty})"
    # Axis intersection forms
    assert anchor_to_xy(('V_mid', 'H_mid')) == (0.0, 0.0)
    assert anchor_to_xy(('V_left', 'H_mid')) == (-150.0, 0.0)
    assert anchor_to_xy(('V_right', 'H_bot')) == (150.0, -150.0)
    assert anchor_to_xy(('H_top', 'V_mid')) == (0.0, 150.0), "order-agnostic"
    # Inverse
    assert xy_to_cell(0, 0) == 'C'
    assert xy_to_cell(100, 100) == 'TR'
    cell, xf, yf = cell_relative_for_xy(-20.0, 70.0)
    assert cell == 'TC' and abs(xf - 0.3) < 1e-6 and abs(yf - 0.8) < 1e-6
    print("anchor.py self-test passed")
