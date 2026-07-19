"""Attempt: p1_stroke_07_弯钩 (G4 — grid-bank memory).

Target: 弯钩 — a curved vertical stroke ending in a leftward hook.
        Canonical example: the middle stroke of 手/子/了/事. Comes down
        from the top slightly to the right of center, arcs gently to the
        left as it descends, then flicks up-left into a sharp short hook.

米字格 anchor plan:
  head    = ('TC', 0.55, 0.20)   — 起笔 near top, just right of center
  belly   = ('C',  0.55, 0.70)   — descends nearly straight through the
                                    central column (subtle bend only)
  hook_pt = ('BC', 0.40, 0.75)   — where the body curves LEFT into the
                                    hook turning point
  tip     = ('BC', 0.10, 0.55)   — hook tip flicks sharply up-and-left

Rationale:
  - Runs top-to-bottom through the central column (TC → C → BC).
  - x_frac holds ~0.55 down the body then swings LEFT (→0.40→0.10) in
    the final third → the "弯" (bend) is concentrated near the bottom.
  - Final hook segment goes UP-LEFT (Δy < 0, Δx < 0) → the "钩" (hook).
  - Width tapers: 起笔 medium (7 px), belly widest (11 px, 顿笔 press),
    hook slim (5 px → 2 px) for the characteristic sharp flick.
  - Curvature: single smooth quadratic-ish arc from head → belly → hook
    turning point, sampled as a Bezier and stroked as adjoining line
    segments so we can vary width per-segment.

Joint spec: single primitive stroke, no joints.
"""

from pathlib import Path
from PIL import Image, ImageDraw


# ---- 米字格 helpers ----------------------------------------------------

CANVAS = 300  # px (both W and H). PIL pixel coords: (0,0) top-left.

# Cell layout on the 米字格: 3x3 grid, each cell is CANVAS/3 px.
_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
    # (col, row) 0-indexed from top-left in PIL coords.
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor_to_xy(anchor):
    """(cell, x_frac, y_frac) → PIL pixel coords (px, py).

    x_frac / y_frac are 0..1 within the cell, with (0,0) at the cell's
    top-left (PIL convention: y grows DOWN).
    """
    cell, xf, yf = anchor
    col, row = _CELL_ORIGIN[cell]
    px = (col + xf) * _CELL
    py = (row + yf) * _CELL
    return (px, py)


# ---- Curve sampling ---------------------------------------------------

def quad_bezier(p0, p1, p2, n=60):
    """Sample a quadratic Bezier from p0 → p2 with control p1."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_variable_width(draw, pts, widths):
    """Draw a polyline whose per-segment width follows `widths`.

    `widths` has the same length as `pts`; the segment between pts[i]
    and pts[i+1] is drawn with width = round(mean(widths[i], widths[i+1])).
    Endpoints are joined with filled circles so width changes look smooth.
    """
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    # Round caps / joins.
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- The stroke -------------------------------------------------------

def draw_wangou(draw, head, belly, hook_pt, tip,
                head_w=7, belly_w=11, hook_start_w=8, tip_w=2):
    """Render a 弯钩 from `head` down through `belly` to `hook_pt`, then
    flick to `tip`."""
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Main body: single smooth quadratic Bezier head → hook_pt with the
    # belly as the control point → gives a gentle leftward bulge as it
    # descends.
    body_pts = quad_bezier(p_head, p_belly, p_hook, n=60)
    # Width profile: taper from head_w → belly_w (peak near 55%) → hook_start_w.
    body_widths = []
    for i, _ in enumerate(body_pts):
        t = i / (len(body_pts) - 1)
        # Piecewise: 0..0.55 → head_w → belly_w; 0.55..1 → belly_w → hook_start_w.
        if t <= 0.55:
            u = t / 0.55
            w = head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Hook flick: short curve from hook_pt → tip, tapering to a sharp point.
    # Use a control point just below-left of hook_pt so the flick curls
    # naturally.
    ctrl = (p_hook[0] - (p_hook[0] - p_tip[0]) * 0.3,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.15)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=20)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1)) +
                   tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_弯钩.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_wangou(
        draw,
        head=('TC', 0.55, 0.20),
        belly=('C',  0.55, 0.70),   # stays mostly vertical through mid
        hook_pt=('BC', 0.40, 0.75), # then curves left near bottom
        tip=('BC', 0.10, 0.55),     # hook flicks sharply up-and-left
        head_w=8,
        belly_w=12,
        hook_start_w=10,
        tip_w=2,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
