"""Attempt: p1_stroke_10_横钩 (G4 — grid-bank memory).

Target: 横钩 — a horizontal stroke ending in a short, sharp hook that
        flicks DOWN and LEFT. Canonical examples: the top-cover strokes
        of 冖 / 宀 (roof radicals), the top stroke of 买, 页, 皮, 又'd
        stroke on top of 皮, etc.

Shape decomposition:
  1. Body — a nearly-flat 横 running left→right along the upper area of
     the character region, with a very subtle upward arch (concave-down).
  2. 顿笔 (shoulder) — at the right end, the brush presses to form a
     small squared/blocky shoulder before the hook change of direction.
  3. Hook flick — a short, sharp curve going DOWN-and-LEFT from the
     shoulder to a fine tip. Direction distinguishes 横钩 from other
     hook variants (contrast: 竖钩's hook goes UP-left; 弯钩's hook
     goes UP-left).

米字格 anchor plan:
  head     = ('TL', 0.30, 0.60)   — 起笔, upper-left area, slight press
  shoulder = ('TR', 0.75, 0.55)   — 顿笔 at the right end of the heng
  tip      = ('TR', 0.55, 0.95)   — hook tip flicks down-and-left, well
                                    below and to the LEFT of shoulder

Rationale:
  - Body spans TL → TR horizontally: reads unambiguously as 横.
  - Slight upward arch (y_frac dips from 0.60 → ~0.50 near mid, back to
    0.55): the classic 横 rising-then-flat calligraphic feel.
  - The hook goes DOWN-LEFT (Δx < 0, Δy > 0 in PIL coords): this is the
    signature of 横钩. Length ≈ 25–30% of body length.
  - Width profile: head medium (7 px, gentle press), taper thin through
    body middle (6 px), thicken at shoulder (10 px 顿笔), then taper
    fast to fine tip (2 px) in the hook flick.

Joint spec: single primitive stroke, no joints.

Reused approach: same variable-width Bezier polyline rasterizer as
p1_stroke_07_弯钩 (see principle_bank.md → "Tapered stroke").
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

def draw_henggou(draw, head, shoulder, tip,
                 head_w=7, mid_w=6, shoulder_w=10, tip_w=2):
    """Render a 横钩: horizontal body from `head` to `shoulder`, then a
    short down-and-left hook flick to `tip`."""
    p_head = anchor_to_xy(head)
    p_shldr = anchor_to_xy(shoulder)
    p_tip = anchor_to_xy(tip)

    # Body: quad Bezier from head → shoulder with a control point that
    # gives a very subtle upward arch (concave-down: control y is
    # slightly ABOVE the chord, i.e. smaller PIL y).
    # Chord midpoint.
    mx = (p_head[0] + p_shldr[0]) / 2.0
    my = (p_head[1] + p_shldr[1]) / 2.0
    # Lift control 6 px upward (PIL: smaller y) for a gentle arch.
    ctrl_body = (mx, my - 6)
    body_pts = quad_bezier(p_head, ctrl_body, p_shldr, n=80)

    # Width profile along body: head_w → mid_w (thin middle) → shoulder_w
    # (thick press at right end, 顿笔).
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        if t <= 0.45:
            u = t / 0.45
            w = head_w * (1 - u) + mid_w * u
        else:
            u = (t - 0.45) / 0.55
            w = mid_w * (1 - u) + shoulder_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Hook flick: short curve shoulder → tip going down-and-left.
    # Control point placed slightly right of the chord midpoint and
    # below the shoulder so the flick curls outward (natural brush
    # motion: press, then whip down-and-left with the tip trailing).
    ctrl_hook = (
        p_shldr[0] + (p_tip[0] - p_shldr[0]) * 0.15,
        p_shldr[1] + (p_tip[1] - p_shldr[1]) * 0.55,
    )
    hook_pts = quad_bezier(p_shldr, ctrl_hook, p_tip, n=25)
    hook_widths = [
        shoulder_w * (1 - i / (len(hook_pts) - 1))
        + tip_w * (i / (len(hook_pts) - 1))
        for i in range(len(hook_pts))
    ]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_横钩.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_henggou(
        draw,
        head=('TL', 0.30, 0.60),
        shoulder=('TR', 0.75, 0.55),
        tip=('TR', 0.55, 0.95),
        head_w=8,
        mid_w=6,
        shoulder_w=11,
        tip_w=2,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
