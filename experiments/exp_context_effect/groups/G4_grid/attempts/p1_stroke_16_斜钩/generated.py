"""Attempt: p1_stroke_16_斜钩 (G4 — grid-bank memory).

Target: 斜钩 (xié gōu) — a SLANTED (top-left → bottom-right) stroke
        with a gentle concave-up bow, ending in a short hook flick
        that points UP (or slightly up-and-left). Canonical examples:
        the main stroke of 我, 戈, 戊, 成. Contrast with 卧钩 (nearly
        horizontal, hook goes up-and-left) and with 竖弯钩 (vertical
        body that curves to horizontal at bottom).

Structural family:
  - 斜钩 body slants ~45–60° from horizontal (steeper than a 捺 but
    slanted, not vertical).
  - Body is subtly bowed (concave to the upper-right — i.e. the belly
    dips lower-left of the straight chord). This bowing gives the
    stroke its characteristic "sabre" feel.
  - The 顿笔 press is around the mid-to-lower belly (thickest zone),
    tapering slightly at the head and tapering into the hook.
  - Hook flick at the tail: short, sharp, points UP (upward, not
    up-left as in 竖钩) — this is the distinguishing feature of
    斜钩's hook.

米字格 anchor plan:
  head    = ('TL', 0.65, 0.35)   — 起笔 upper-left region, slight
                                    indent from corner
  belly   = ('C',  0.55, 0.60)   — the curve's lowest point (relative
                                    to chord), lands in center cell
  hook_pt = ('BR', 0.55, 0.65)   — bottom-right where the body ends
                                    and the hook turns
  tip     = ('BR', 0.55, 0.30)   — hook tip flicks UPWARD, staying at
                                    ~same x_frac (hook goes up, not
                                    left)

Rationale:
  - head at TL (col=0, row=0) with x_frac=0.65, y_frac=0.35 puts the
    起笔 near ~(88, 45) px — upper-left region.
  - hook_pt at BR (col=2, row=2) with x_frac=0.55, y_frac=0.65 puts
    the hook turn near ~(255, 265) px — lower-right region. Chord
    from head→hook_pt slants down-right at ~55°.
  - belly at C (col=1, row=1) x=0.55, y=0.60 puts belly near
    ~(155, 160) px — slightly BELOW the chord midpoint (chord mid is
    ~(171, 155)), giving the concave-up bow.
  - tip at BR x=0.55 y=0.30 puts tip near ~(255, 230) px — 35px
    directly above hook_pt. Hook flick length ~35px vs body length
    ~285px → ~12% of body, sharp and short.
  - Width: taper up head→belly (顿笔 press mid-lower), hold through
    hook_pt, then taper to needle at tip.

Joint spec: single primitive stroke, no joints.

Contrast recorded (for principle_bank when curator promotes):
  - 弯钩: curved-vertical body, hook up-left.
  - 竖钩: straight vertical body, hook up-left.
  - 卧钩: nearly-horizontal shallow-arc body, hook up-left.
  - 斜钩: SLANTED body (top-left→bottom-right), gentle concave-up
    bow, hook straight UP.
"""

from pathlib import Path
from PIL import Image, ImageDraw


# ---- 米字格 helpers ----------------------------------------------------

CANVAS = 300  # px. PIL pixel coords: (0,0) top-left, y grows DOWN.

_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor_to_xy(anchor):
    """(cell, x_frac, y_frac) → PIL pixel coords (px, py).

    x_frac / y_frac are 0..1 within the cell, with (0,0) at cell's
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
    """Polyline with per-vertex width; discs at each vertex for smoothness."""
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) / 2.0)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    for (x, y), w in zip(pts, widths):
        r = max(1, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- The stroke -------------------------------------------------------

def draw_xiegou(draw, head, belly, hook_pt, tip,
                head_w=8, belly_w=14, hook_start_w=12, tip_w=1):
    """Render 斜钩: slanted concave-up body head→hook_pt (with belly
    as bezier control), then short upward hook flick to tip."""
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # --- Body: quad Bezier head → hook_pt with control derived so the
    # curve passes near the belly point (concave-up bow). For a quad
    # bezier B(t) at t=0.5, B = (p0 + 2*ctrl + p2) / 4.
    # Solve ctrl = 2*belly - (p_head + p_hook)/2.
    ctrl_body = (2 * p_belly[0] - (p_head[0] + p_hook[0]) / 2.0,
                 2 * p_belly[1] - (p_head[1] + p_hook[1]) / 2.0)
    body_pts = quad_bezier(p_head, ctrl_body, p_hook, n=60)

    body_widths = []
    for i, _ in enumerate(body_pts):
        t = i / (len(body_pts) - 1)
        # Width profile: head thin (light 起笔), swell to belly_w at
        # ~65% (the 顿笔 press is mid-lower), then hold near
        # hook_start_w at the tail.
        if t <= 0.65:
            u = t / 0.65
            w = head_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.65) / 0.35
            w = belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # --- Hook flick: short curve hook_pt → tip. Control point placed
    # so the flick curls slightly right-then-up, giving the tight
    # calligraphic corner typical of 斜钩's hook.
    ctrl_hook = (p_hook[0] + (p_hook[0] - p_tip[0]) * 0.0 + 6,
                 p_hook[1] - (p_hook[1] - p_tip[1]) * 0.15)
    hook_pts = quad_bezier(p_hook, ctrl_hook, p_tip, n=25)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1)) +
                   tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_斜钩.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_xiegou(
        draw,
        head=('TL', 0.65, 0.35),
        belly=('C',  0.55, 0.60),
        hook_pt=('BR', 0.55, 0.65),
        tip=('BR', 0.55, 0.30),
        head_w=8,
        belly_w=15,
        hook_start_w=13,
        tip_w=2,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
