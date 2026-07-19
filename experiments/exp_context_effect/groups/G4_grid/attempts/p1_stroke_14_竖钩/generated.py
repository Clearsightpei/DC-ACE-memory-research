"""Attempt: p1_stroke_14_竖钩 (G4 — grid-bank memory).

Target: 竖钩 (shù gōu) — a STRAIGHT vertical stroke ending in a short
        leftward hook flick. Canonical examples: the middle stroke of
        小/水/木, the vertical in 才. Contrast with 弯钩 (curved body):
        竖钩's body is straight (no bend); the "钩" appears only at the
        very bottom as a sharp up-left flick.

米字格 anchor plan:
  head    = ('TC', 0.50, 0.20)   — 起笔 near top-center, dead-centered
  belly   = ('C',  0.50, 0.50)   — descends straight down mid-column
  hook_pt = ('BC', 0.50, 0.75)   — bottom of vertical body (hook turning
                                    point) — STILL on the mid-column
                                    (no leftward drift — that's the
                                    key differentiator vs 弯钩)
  tip     = ('BC', 0.20, 0.55)   — hook tip flicks up-and-left; short
                                    and sharp (~30% of body length)

Rationale:
  - x_frac stays at 0.50 through head → belly → hook_pt: this is the
    "竖" (straight vertical) — no bend at all in the body.
  - Only after hook_pt does the stroke swing LEFT (0.50 → 0.20) AND
    UP (y_frac 0.75 → 0.55): this is the "钩" (hook flick).
  - Width: 顿笔 press at head (heavy start), taper down through the
    body to a medium width at hook_pt, then flick tapers to a needle
    tip.
  - Body rendered as a straight variable-width line (no Bezier — that
    was 弯钩's job). Hook rendered as a short quadratic Bezier for
    the natural curl.

Joint spec: single primitive stroke, no joints.

Contrast recorded in principle_bank:
  - 弯钩: body arcs, hook at bottom.
  - 竖钩: body straight, hook at bottom.
  Same hook, different body geometry.
"""

from pathlib import Path
from PIL import Image, ImageDraw


# ---- 米字格 helpers ----------------------------------------------------

CANVAS = 300  # px (both W and H). PIL pixel coords: (0,0) top-left.

_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
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

def quad_bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_variable_width(draw, pts, widths):
    """Draw a polyline whose per-segment width follows `widths`."""
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- The stroke -------------------------------------------------------

def sample_line(p0, p1, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append((p0[0] + t * (p1[0] - p0[0]),
                    p0[1] + t * (p1[1] - p0[1])))
    return pts


def draw_shugou(draw, head, belly, hook_pt, tip,
                head_w=12, belly_w=10, hook_start_w=9, tip_w=1):
    """Render a 竖钩 with a straight vertical body head→belly→hook_pt,
    then a short curved hook flick to tip."""
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Body: straight line head → hook_pt sampled densely so we can vary
    # width per segment. belly is at ~50% between head and hook_pt so
    # we use it as a width-profile knot only, not a curve control.
    body_pts = sample_line(p_head, p_hook, n=50)
    body_widths = []
    for i, _ in enumerate(body_pts):
        t = i / (len(body_pts) - 1)
        # Slight 顿笔 press at head (heaviest), taper to belly then to
        # hook_start_w at hook_pt.
        if t <= 0.10:
            # Head 顿笔 region: hold head_w.
            w = head_w
        elif t <= 0.55:
            u = (t - 0.10) / 0.45
            w = head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Hook flick: short curve from hook_pt → tip. Control point placed
    # so the flick curls slightly DOWN then UP-LEFT, giving the natural
    # calligraphic curl of a 钩.
    ctrl = (p_hook[0] - (p_hook[0] - p_tip[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.10)
    # (ctrl y is slightly below p_hook to give a tiny curl before rising)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1)) +
                   tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_竖钩.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_shugou(
        draw,
        head=('TC', 0.50, 0.20),
        belly=('C',  0.50, 0.50),
        hook_pt=('BC', 0.50, 0.75),  # STRAIGHT body — same x_frac as head
        tip=('BC', 0.20, 0.55),      # hook flicks up-and-left, short
        head_w=13,
        belly_w=11,
        hook_start_w=10,
        tip_w=2,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
