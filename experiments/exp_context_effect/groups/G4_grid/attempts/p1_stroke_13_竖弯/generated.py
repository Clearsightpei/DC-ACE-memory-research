"""Attempt: p1_stroke_13_竖弯 (G4 — grid-bank memory).

Target: 竖弯 — a vertical stroke that curves smoothly at the bottom
        into a rightward horizontal segment. Canonical example: the
        base stroke of 四 (bottom, before the closing right side) or
        the enclosing sweep in 西. Descends straight from the top,
        arcs through the bottom-left corner, and finishes with a
        short horizontal run to the right. Crucially — unlike 竖弯钩
        — there is NO hook flick at the end. The stroke ends flat
        (may have a slight 顿笔 pressing at the tail).

米字格 anchor plan:
  head    = ('TC', 0.20, 0.40)   — 起笔 near top, slightly left of the
                                    centre column (px ≈ 120, py ≈ 40)
  belly   = ('BC', 0.20, 0.30)   — SAME x as head → vertical descent
                                    stays truly straight through the
                                    top two thirds (px ≈ 120, py ≈ 230)
  corner  = ('BC', 0.30, 0.50)   — turning point of the bend, tucked
                                    into the bottom (px ≈ 130, py ≈ 250)
  tail    = ('BR', 0.30, 0.50)   — flat horizontal finish extending
                                    right (px ≈ 230, py ≈ 250); ends
                                    FLAT (no hook, no upward flick)

Rationale:
  - Runs top-to-bottom through the left-center column (TC → ML) then
    turns 90° smoothly into a rightward horizontal (→ BC).
  - x_frac holds ~near-constant through the top two thirds, then the
    turn is concentrated in the bottom third (弯 = bend, not a sweep).
  - No hook — the horizontal ends with a small 顿笔 (slight widening
    then flat termination), NOT tapering to a needle tip and NOT
    flicking up. This is the key contrast with 弯钩 / 竖弯钩.
  - Width tapers: 起笔 medium (7 px), belly widest (11 px, 顿笔 press
    through the vertical), corner ~10 px (thickness carries around
    the bend), tail 9 px flat (no needle taper).
  - Curvature: single smooth quadratic-ish arc head → belly → corner,
    then a second gentle Bezier corner → tail so that the transition
    from vertical to horizontal is a rounded L, not a sharp angle.

Joint spec: single primitive stroke, no joints.

Convention: PIL-native anchor helper (y grows DOWN within cell),
matching p1_stroke_07_弯钩. See sandbox.md re: the outstanding
principle-bank vs. PIL-native anchor-convention question.
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

    `widths` has the same length as `pts`; segment i uses the mean
    of the two endpoint widths. Vertices are covered with filled
    circles so width changes remain smooth.
    """
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- The stroke -------------------------------------------------------

def draw_shuwan(draw, head, belly, corner, tail,
                head_w=7, belly_w=11, corner_w=10, tail_w=9):
    """Render a 竖弯: vertical body head→belly→corner, then a
    smooth horizontal finish corner→tail with a flat termination."""
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)

    # --- Body: head → corner, using `belly` as the Bezier control so the
    # vertical descent stays nearly straight until near the bottom, then
    # bends left/down toward the corner point. This concentrates the
    # "弯" in the bottom third rather than curving the whole descent.
    body_pts = quad_bezier(p_head, p_belly, p_corner, n=60)
    body_widths = []
    for i, _ in enumerate(body_pts):
        t = i / (len(body_pts) - 1)
        # Piecewise taper: 0..0.55 head→belly (peak press mid-lower);
        # 0.55..1 belly→corner (carry thickness through the turn).
        if t <= 0.55:
            u = t / 0.55
            w = head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + corner_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # --- Tail: corner → tail, a gentle rightward Bezier. Control point
    # sits slightly below-right of the corner so the curve rounds out
    # of the vertical smoothly (a rounded-L rather than a sharp 90°).
    # Width tapers very mildly corner_w → tail_w (no needle, no hook).
    ctrl = (p_corner[0] + (p_tail[0] - p_corner[0]) * 0.55,
            p_corner[1] + (p_tail[1] - p_corner[1]) * 0.25 + 6)
    tail_pts = quad_bezier(p_corner, ctrl, p_tail, n=40)
    tail_widths = [corner_w * (1 - i / (len(tail_pts) - 1)) +
                   tail_w * (i / (len(tail_pts) - 1))
                   for i in range(len(tail_pts))]
    stroke_variable_width(draw, tail_pts, tail_widths)

    # --- Flat termination (顿笔): a tiny disc at the tail tip, same
    # width as tail_w, to emphasize the flat/blocky ending. Explicitly
    # NOT a needle-taper and NOT an upward flick.
    r = tail_w / 2.0 + 0.5
    draw.ellipse([p_tail[0] - r, p_tail[1] - r,
                  p_tail[0] + r, p_tail[1] + r], fill=(0, 0, 0))


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_竖弯.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_shuwan(
        draw,
        # Head px ~ 120, py ~ 40 — top of TC, x slightly left of centre.
        # Belly px ~ 120, py ~ 230 — SAME x as head → truly vertical
        # descent through the top two thirds (弯 concentrated at corner).
        # Corner px ~ 130, py ~ 250 — turning point in BC.
        # Tail px ~ 230, py ~ 250 — flat horizontal finish in BR.
        head=('TC',   0.20, 0.40),
        belly=('BC',  0.20, 0.30),
        corner=('BC', 0.30, 0.50),
        tail=('BR',   0.30, 0.50),
        head_w=8,
        belly_w=12,
        corner_w=11,
        tail_w=9,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
