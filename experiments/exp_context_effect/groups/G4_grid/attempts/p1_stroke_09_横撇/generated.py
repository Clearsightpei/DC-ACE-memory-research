"""Attempt: p1_stroke_09_横撇 (G4 — grid-bank memory).

Target: 横撇 (héng piě) — a compound stroke: a horizontal 横 (heng)
        that ends with a sharp corner turn (折) into a diagonal 撇
        going down-and-left, tapering to a needle tip.
        Canonical example: the top-right compound stroke of 又, 皮, 巡.

米字格 anchor plan (single continuous stroke, one 折 corner):
  head    = ('TL', 0.30, 0.55)   — 起笔 slightly-thickened head on left
  corner  = ('TR', 0.60, 0.60)   — sharp turn: end of 横, start of 撇
                                    (顿笔 press at the corner, characteristic
                                     of 横撇: the shoulder thickens before
                                     the diagonal descent)
  tip     = ('BL', 0.60, 0.90)   — 撇 tail: needle tip in lower-left cell,
                                    down-and-left of the corner

Rationale:
  - Horizontal segment: TL(0.30,0.55) → TR(0.60,0.60): a nearly flat
    slight downward tilt as calligraphic 横 typically rises very
    slightly then dips at the shoulder. Keeps the 横 in the upper band.
  - Corner (折): the turn point sits high-right (TR cell). This is where
    calligraphers press (顿笔) before pivoting — modeled by a small
    width bump at the corner.
  - Diagonal 撇 segment: from the corner heads down-and-left across the
    center of the canvas, tapering to a sharp needle tip in BL. Δx
    negative and Δy positive → classic left-descending 撇 direction.
  - The 撇 tail lands ~x_frac 0.60 in BL, which is roughly under the
    LEFT half of the horizontal — matching how 横撇 "wraps under" its
    horizontal in real characters.
  - Width profile:
      * 横 head: medium (7 px)
      * along 横 body: taper slightly down (7 → 6)
      * at corner: widen sharply (10 px, 顿笔)
      * along 撇 body: taper down 10 → 2 to a needle
    This gives the characteristic "thin horizontal → thick shoulder →
    tapering diagonal" silhouette of 横撇.

Joint spec: single primitive compound stroke, no cross-stroke joints.
    Internal 折 = P-class corner (welded, sharp direction change).
"""

from pathlib import Path
from PIL import Image, ImageDraw


# ---- 米字格 helpers ----------------------------------------------------

CANVAS = 300  # px (both W and H). PIL pixel coords: (0,0) top-left.

# Cell layout on the 米字格: 3x3 grid, each cell is CANVAS/3 px.
_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor_to_xy(anchor):
    """(cell, x_frac, y_frac) → PIL pixel coords (px, py).

    x_frac / y_frac are 0..1 within the cell; (0,0) at the cell's
    top-left (PIL convention: y grows DOWN).
    """
    cell, xf, yf = anchor
    col, row = _CELL_ORIGIN[cell]
    px = (col + xf) * _CELL
    py = (row + yf) * _CELL
    return (px, py)


# ---- Rendering primitives --------------------------------------------

def stroke_variable_width(draw, pts, widths):
    """Draw a polyline whose per-segment width follows `widths`."""
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    # Round caps / smooth joins.
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def sample_segment(p0, p1, n):
    """Linear sample p0 → p1 with n+1 points (inclusive)."""
    return [(p0[0] + (p1[0] - p0[0]) * i / n,
             p0[1] + (p1[1] - p0[1]) * i / n) for i in range(n + 1)]


# ---- The stroke -------------------------------------------------------

def draw_heng_pie(draw, head, corner, tip,
                  head_w=7, corner_w=10, tip_w=2):
    """Render a 横撇: horizontal 横 head→corner (顿笔 at corner), then a
    tapered diagonal 撇 corner→tip.
    """
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tip = anchor_to_xy(tip)

    # --- 横 segment: head → corner (nearly straight, subtle taper) ---
    heng_pts = sample_segment(p_head, p_corner, n=30)
    # Width profile along the heng: start at head_w, slight dip mid,
    # then swell up to corner_w at the shoulder (顿笔).
    heng_widths = []
    for i, _ in enumerate(heng_pts):
        t = i / (len(heng_pts) - 1)
        if t <= 0.7:
            # gentle taper down: head_w → head_w - 1
            u = t / 0.7
            w = head_w * (1 - u) + (head_w - 1) * u
        else:
            # swell to corner: (head_w-1) → corner_w
            u = (t - 0.7) / 0.3
            w = (head_w - 1) * (1 - u) + corner_w * u
        heng_widths.append(w)
    stroke_variable_width(draw, heng_pts, heng_widths)

    # --- 撇 segment: corner → tip (sharp taper to needle) ---
    # Introduce mild curvature: slight bow to the LEFT (i.e., the belly
    # of the pie curves down-left slightly) via a quadratic Bezier with
    # a control point pushed left of the chord midpoint.
    mx = (p_corner[0] + p_tip[0]) / 2.0
    my = (p_corner[1] + p_tip[1]) / 2.0
    # Push control ~8% of chord length perpendicular-left.
    dx = p_tip[0] - p_corner[0]
    dy = p_tip[1] - p_corner[1]
    length = (dx * dx + dy * dy) ** 0.5
    # Perpendicular pointing left of travel direction:
    # travel = (dx, dy) normalized. Left-perp = (-dy, dx) / length.
    if length > 1:
        perp = (-dy / length, dx / length)
        bow = length * 0.08
        ctrl = (mx + perp[0] * bow, my + perp[1] * bow)
    else:
        ctrl = (mx, my)
    # Sample quadratic Bezier.
    pie_pts = []
    n = 40
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p_corner[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p_tip[0]
        y = (1 - t) ** 2 * p_corner[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p_tip[1]
        pie_pts.append((x, y))
    # Width: corner_w → tip_w, ease-out for a fine needle tip.
    pie_widths = []
    for i, _ in enumerate(pie_pts):
        t = i / (len(pie_pts) - 1)
        # Ease so bulk of taper happens in last 60%.
        eased = t ** 1.4
        w = corner_w * (1 - eased) + tip_w * eased
        pie_widths.append(w)
    stroke_variable_width(draw, pie_pts, pie_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_横撇.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_heng_pie(
        draw,
        head=('TL', 0.30, 0.55),
        corner=('TR', 0.60, 0.60),
        tip=('BL', 0.60, 0.90),
        head_w=7,
        corner_w=11,
        tip_w=2,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
