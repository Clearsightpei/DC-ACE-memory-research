"""Attempt: p1_stroke_19_横斜钩 (G4 — grid-bank memory).

Target: 横斜钩 (héng xié gōu) — compound stroke = 横 (horizontal
        opening) + 斜 (slanted descent, concave to the upper-right) +
        钩 (short hook flicking UP-and-LEFT at the tail). Canonical
        examples: the enclosing stroke of 飞, 风, 凡, 几 (in some
        style variants).

Structural decomposition (three phases along one continuous stroke):
  1. 横 (opening horizontal). Short, tilted very slightly downward
     to the right. Starts thin, thickens through the small 顿笔 at
     the corner where the direction changes.
  2. 斜 (slanted body). Turns sharply at the top-right corner and
     descends toward the lower-left, with a subtle concave-up bow
     (belly dips a little further down-right than the straight chord).
     Widest through the mid-body 顿笔, then tapers toward the hook.
  3. 钩 (hook flick). At the tail, a short sharp flick pointing UP
     and slightly LEFT. Length ≈ 25–30% of the slanted body's chord.

米字格 anchor plan:
  head    = ('TL', 0.35, 0.30)   — 起笔 top-left, well inside canvas.
  corner  = ('TR', 0.55, 0.40)   — end of the 横 opening / start of
                                   the slanted descent. Slight droop
                                   from head (y grows a little).
  belly   = ('C',  0.55, 0.75)   — mid-body of the 斜 phase; sits
                                   slightly below/right of the chord
                                   from corner to hook_pt, giving the
                                   concave-up bow.
  hook_pt = ('BC', 0.30, 0.70)   — where the slanted body ends and
                                   the hook turns.
  tip     = ('BC', 0.10, 0.30)   — hook tip flicks UP-LEFT, tapered
                                   to a needle.

Pixel-level intuition (100px cells, PIL y grows down):
  - head (TL, .35, .30)   ≈ (35, 30)
  - corner (TR, .55, .40) ≈ (255, 40)     — the 横 spans ~220px wide,
                                            drops only ~10px (subtle).
  - belly (C, .55, .75)   ≈ (155, 175)    — mid of the descent.
  - hook_pt (BC, .30, .70)≈ (130, 270)    — lower-center-left.
  - tip (BC, .10, .30)    ≈ (110, 230)    — 40px up-and-left of the
                                            hook_pt (~15% of body).

Width profile:
  - 横 phase: starts thin (head_w=6), thickens to corner_w=13
    (the 顿笔 press at the corner).
  - 斜 phase: begins at corner_w=13, swells to belly_w=15 (mid-body
    press), then narrows to hook_start_w=11 at hook_pt.
  - 钩 phase: from hook_start_w=11 down to tip_w=1 (needle).

Contrast with siblings (recorded for the curator to promote):
  - 横钩 (p1_10): 横 then a short DOWNWARD-LEFT hook, NO slanted
    descent phase.
  - 横折 (p1_11): 横 then a SHORT VERTICAL 折, NO hook.
  - 弯钩 (p1_07): near-vertical curved body, hook up-left, NO 横
    opening.
  - 斜钩 (p1_16): slanted body only, hook UP (not up-left), NO 横
    opening.
  - 横斜钩 is the ONLY stroke that combines all three phases (横 +
    slanted descent + up-left hook). Its most distinguishing feature
    vs 横钩 is the substantial slanted descent between the 横 and
    the hook.

Joint spec: single continuous compound stroke — three internal
  direction changes (横→斜 at `corner`; 斜→钩 at `hook_pt`). No
  external joints (single primitive).
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

    x_frac / y_frac are 0..1 within the cell, (0,0) at cell's
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

def draw_hengxiegou(draw, head, corner, belly, hook_pt, tip,
                    head_w=6, corner_w=13, belly_w=15,
                    hook_start_w=11, tip_w=1):
    """Render 横斜钩 as three connected phases: horizontal opening,
    slanted descending body (concave-up bow), then a short up-left
    hook flick."""
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # --- Phase 1: 横 opening. Nearly-straight, slight downward tilt.
    # A gentle bow with the control just above the chord midpoint
    # yields the very subtle "arch" typical of a 横 that leads into a
    # 折.
    mid_h = ((p_head[0] + p_corner[0]) / 2.0,
             (p_head[1] + p_corner[1]) / 2.0 - 3)
    heng_pts = quad_bezier(p_head, mid_h, p_corner, n=35)
    heng_widths = []
    for i in range(len(heng_pts)):
        t = i / (len(heng_pts) - 1)
        # thin at 起笔, thicken toward the corner 顿笔
        w = head_w * (1 - t) + corner_w * t
        heng_widths.append(w)
    stroke_variable_width(draw, heng_pts, heng_widths)

    # --- Phase 2: 斜 slanted descent. Quadratic Bezier from corner
    # to hook_pt with control derived so the curve passes near the
    # declared belly point (concave-up bow — belly sits slightly
    # right-of-chord).
    ctrl_body = (2 * p_belly[0] - (p_corner[0] + p_hook[0]) / 2.0,
                 2 * p_belly[1] - (p_corner[1] + p_hook[1]) / 2.0)
    body_pts = quad_bezier(p_corner, ctrl_body, p_hook, n=60)
    body_widths = []
    for i in range(len(body_pts)):
        t = i / (len(body_pts) - 1)
        # start at corner_w, swell to belly_w around 55%, taper to
        # hook_start_w at the tail.
        if t <= 0.55:
            u = t / 0.55
            w = corner_w * (1 - u) + belly_w * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w * (1 - u) + hook_start_w * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # --- Phase 3: 钩 hook flick. Short curve hook_pt → tip, pointing
    # up-and-left. A control point placed slightly LEFT of the chord
    # gives the tight calligraphic corner of a 钩 that flicks upward
    # then curls in.
    ctrl_hook = ((p_hook[0] + p_tip[0]) / 2.0 - 4,
                 (p_hook[1] + p_tip[1]) / 2.0 + 2)
    hook_pts = quad_bezier(p_hook, ctrl_hook, p_tip, n=25)
    hook_widths = [hook_start_w * (1 - i / (len(hook_pts) - 1)) +
                   tip_w * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths)


# ---- Main -------------------------------------------------------------

OUT_PATH = Path(__file__).with_name("01_横斜钩.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_hengxiegou(
        draw,
        head=('TL',  0.35, 0.30),
        corner=('TR', 0.55, 0.40),
        belly=('C',   0.55, 0.75),
        hook_pt=('BC', 0.30, 0.70),
        tip=('BC',    0.10, 0.30),
        head_w=6,
        corner_w=13,
        belly_w=15,
        hook_start_w=11,
        tip_w=1,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
