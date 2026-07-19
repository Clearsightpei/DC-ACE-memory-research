"""Attempt: p1_stroke_20_橫折提 (G4 grid-bank).

Target: 橫折提 — compound stroke = 横 (horizontal) → 90° 折 (turn down)
        → 提 (rising tapered flick out to upper-right).
        Commonly seen in the 言字旁 (讠) radical bottom and in
        characters like 计, 论, 讨 (simplified 言).

Composition (three sub-strokes fused into one continuous brush path):
  seg1  horizontal 横  head_h → corner       (uniform-ish width)
  seg2  vertical  竖    corner → knee         (uniform width, short drop)
  seg3  提 (rising)     knee → tail (needle)  (thick head → sharp tip,
                                                sweeps UP-RIGHT)

米字格 anchors:
  head_h  = ('ML', 0.30, 0.30)   — 起笔, mid of left mid cell (PIL ~30,130)
  corner  = ('MR', 0.40, 0.30)   — 折 corner (PIL ~240,130)
  knee    = ('BR', 0.15, 0.40)   — foot of the short vertical, in the
                                    bottom-right cell (PIL ~215,240).
                                    Slightly inboard of the corner in x.
  tail    = ('MR', 0.85, 0.75)   — needle tip of 提 (PIL ~285,175),
                                    up-and-right of the knee (rising).

Why these choices:
  - The 横 segment sits high in the mid band so the vertical drop and
    the subsequent 提 have room without crowding either edge.
  - The vertical is INTENTIONALLY short (only from mid-row 0.30 down
    to mid-row 0.85 — about 0.55 cell heights) because 橫折提 is a
    compact radical stroke; the 提 needs the lower half of the canvas.
  - The knee's x_frac (0.65) is slightly LEFT of the corner's x_frac
    (0.75). This matches the calligraphic reality: after the 折 shoulder
    the brush drops with a subtle inward slant so the 提 launch point
    is inboard of the corner, giving the 提 a clean straight run
    outward.
  - The 提 launches from the knee and rises to the upper-right, ending
    at BR (0.85, 0.35) — well inside the bottom-right cell, tapering
    to a needle tip. Direction: up-right, matching a canonical 提.

Width profile:
  - 横 segment: ~10 px uniform.
  - Corner shoulder disc: ~13 px 顿笔 bump.
  - 竖 segment (corner → knee): 10 px at corner, 12 px at knee (a
    slight thickening toward the knee where the brush re-presses
    before launching the 提). This press is the "second 顿笔" that
    gives 橫折提 its characteristic weighted turn before the flick.
  - 提 segment (knee → tail): tapered from 13 px (thick head at knee)
    down to 1 px (needle tip at tail).

Joint spec: single compound stroke with two internal self-joints:
  - corner  @ MR (0.75, 0.30) — P (welded 90° turn between 横 and 竖).
  - knee    @ MR (0.65, 0.85) — P (welded turn between 竖 and 提;
                                    slight direction change ≈120°).
No external joints (this is a standalone stroke).
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
    """(cell, x_frac, y_frac) → PIL pixel coords.
    x_frac / y_frac are 0..1 within cell, (0,0) at cell top-left.
    Uses the PIL-native convention (y grows DOWN within cell) used by
    the other stroke attempts in this run (see 横折, 弯钩).
    """
    cell, xf, yf = anchor
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)


# ---- Primitives -------------------------------------------------------

def fat_line(draw, p0, p1, width, color=(0, 0, 0)):
    """Line with rounded caps (filled discs at both ends)."""
    draw.line([p0, p1], fill=color, width=int(round(width)))
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)


def draw_tapered_ti(draw, head_xy, tail_xy,
                    head_width=13, tail_width=1, curve=0.06, segments=42,
                    color=(0, 0, 0)):
    """Rasterize a 提 stroke (rising, tapered thick→needle).

    Uses a quadratic Bezier with a slight upward bow (concave-down
    relative to the chord). Deposits filled discs and connects each
    pair with a fat line so no gaps appear at the aggressive taper.
    """
    hx, hy = head_xy
    tx, ty = tail_xy

    # Chord midpoint (PIL coords).
    midx = (hx + tx) / 2.0
    midy = (hy + ty) / 2.0

    # Perpendicular to the chord.
    dx = tx - hx
    dy = ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    # In PIL (y-down), a rightward-and-up chord (dx>0, dy<0) means
    # the perpendicular pointing "above the chord" (visually upward)
    # is (-dy, dx) / length reversed-in-y. Concretely: we want the
    # control point to sit visually ABOVE the chord (smaller PIL y).
    perp_x = -dy / length
    perp_y = dx / length
    # Force the perpendicular to point in the negative-y direction
    # (upward on screen).
    if perp_y > 0:
        perp_x, perp_y = -perp_x, -perp_y
    bow = curve * length
    cx = midx + perp_x * bow
    cy = midy + perp_y * bow

    prev = None
    for i in range(segments + 1):
        t = i / segments
        bx = (1 - t) ** 2 * hx + 2 * (1 - t) * t * cx + t * t * tx
        by = (1 - t) ** 2 * hy + 2 * (1 - t) * t * cy + t * t * ty
        w = head_width + (tail_width - head_width) * t
        r = max(0.5, w / 2.0)
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=color)
        if prev is not None:
            ppx, ppy, pw = prev
            draw.line([ppx, ppy, bx, by], fill=color,
                      width=max(1, int(round((pw + w) / 2.0))))
        prev = (bx, by, w)


def draw_heng_zhe_ti(draw,
                     head_h_anchor,
                     corner_anchor,
                     knee_anchor,
                     tail_anchor,
                     h_width=10,
                     v_head_width=10,
                     v_knee_width=12,
                     shoulder=13,
                     knee_shoulder=14,
                     ti_head_width=13,
                     ti_tail_width=1,
                     ti_curve=0.06,
                     color=(0, 0, 0)):
    """Render 橫折提 as: horizontal → 90° corner → short vertical → 提."""
    head_h = anchor_to_xy(head_h_anchor)
    corner = anchor_to_xy(corner_anchor)
    knee   = anchor_to_xy(knee_anchor)
    tail   = anchor_to_xy(tail_anchor)

    # 1. Horizontal 横 (head → corner).
    fat_line(draw, head_h, corner, h_width, color)

    # 2. Vertical 竖 (corner → knee), slightly thickening.
    # Emulate a linear width ramp by drawing several stacked sub-segments.
    steps = 6
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        p0 = (corner[0] + (knee[0] - corner[0]) * t0,
              corner[1] + (knee[1] - corner[1]) * t0)
        p1 = (corner[0] + (knee[0] - corner[0]) * t1,
              corner[1] + (knee[1] - corner[1]) * t1)
        w = v_head_width + (v_knee_width - v_head_width) * ((t0 + t1) / 2.0)
        fat_line(draw, p0, p1, w, color)

    # 3. Corner shoulder disc (顿笔 at 折).
    r = shoulder / 2.0
    cx, cy = corner
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)

    # 4. Knee shoulder disc (second 顿笔 before the 提 launch).
    r2 = knee_shoulder / 2.0
    kx, ky = knee
    draw.ellipse((kx - r2, ky - r2, kx + r2, ky + r2), fill=color)

    # 5. 提 (knee → tail): tapered rising flick.
    draw_tapered_ti(draw, knee, tail,
                    head_width=ti_head_width,
                    tail_width=ti_tail_width,
                    curve=ti_curve,
                    color=color)


# ---- Render -----------------------------------------------------------

OUT_PATH = Path(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G4_grid/attempts/p1_stroke_20_橫折提/"
    "01_橫折提.png"
)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_ti(
        draw,
        head_h_anchor=('ML', 0.30, 0.30),
        corner_anchor=('MR', 0.40, 0.30),
        knee_anchor=('BR', 0.15, 0.40),
        tail_anchor=('MR', 0.85, 0.75),
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (CANVAS, CANVAS), f"expected {CANVAS}x{CANVAS}, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
