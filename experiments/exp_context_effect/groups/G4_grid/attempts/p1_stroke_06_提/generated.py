"""p1_stroke_06_提 — Drawer attempt (G4 grid-bank).

Renders a standalone 提 (tí) stroke: a rising diagonal from
lower-left to upper-right. Calligraphic convention:
  - Head (起笔) at lower-left: pressed down, thick (heaviest weight).
  - Tail (出锋) at upper-right: swept out to a sharp needle-tip.
  - Slight upward-arcing curve (concave-down / slightly convex-up
    relative to the straight chord).

米字格 anchors:
  head @ ('BL', 0.30, 0.75)  — thick 起笔 in lower-left cell
  tail @ ('TR', 0.75, 0.30)  — needle-tip 出锋 in upper-right cell

Joint spec: single stroke, no joints.

Because the shared Success Bank is empty (locked until human PASS),
the 米字格 anchor helper and tapered-stroke rasterizer are inlined
below rather than imported.
"""

import os
from PIL import Image, ImageDraw


# ── 米字格 anchor helper (subset of run_6/_anchor.py) ─────────────
# Character region: turtle math-coords x,y ∈ [-150, +150].
# We draw at 300×300 PIL pixels — map math (x,y) → PIL (px, py):
#   px = x + 150            (math x=-150 → left edge)
#   py = 150 - y            (math y=+150 → top edge; PIL y grows DOWN)
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


def anchor_to_math(anchor):
    """(cell, x_frac, y_frac) → (mx, my) math-coords."""
    cell, xf, yf = anchor
    x_left, x_right, y_top, y_bot = CELLS[cell]
    mx = x_left + xf * (x_right - x_left)
    my = y_top + yf * (y_bot - y_top)  # y_frac=0 → top edge (high y)
    return float(mx), float(my)


def math_to_pil(mx, my):
    """Math-coords (origin center, y up) → PIL pixel (origin TL, y down)."""
    return mx + 150.0, 150.0 - my


# ── 提 rasterizer: tapered curved sweep, thick head → sharp tail ──
def draw_ti(draw, head_anchor, tail_anchor,
            head_width=13, tail_width=1, curve=0.09, segments=48):
    """Rasterize a 提 stroke: cubic-ish arc with linearly tapered width.

    curve>0 bows the stroke slightly *upward* (toward the reader's
    upper-left when going lower-left→upper-right), which matches the
    subtle concave-down calligraphic shape of 提.
    """
    hx, hy = anchor_to_math(head_anchor)   # lower-left
    tx, ty = anchor_to_math(tail_anchor)   # upper-right

    # Chord midpoint.
    mx = (hx + tx) / 2.0
    my = (hy + ty) / 2.0
    # Perpendicular direction (rotate chord 90° CCW), used to bow the arc.
    dx = tx - hx
    dy = ty - hy
    length = (dx * dx + dy * dy) ** 0.5
    # Perp (dy, -dx)/length rotated: pick the sign that lifts the arc UP
    # (positive math-y) so the belly points toward the upper-left.
    perp_x = -dy / length
    perp_y = dx / length
    # Ensure perp points into the +y half (upward bow).
    if perp_y < 0:
        perp_x, perp_y = -perp_x, -perp_y
    bow = curve * length
    cx = mx + perp_x * bow
    cy = my + perp_y * bow

    # Sample a quadratic Bézier from (hx,hy) via control (cx,cy) to (tx,ty),
    # laying down circles whose radius tapers head→tail.
    prev = None
    for i in range(segments + 1):
        t = i / segments
        # Quadratic Bézier
        bxm = (1 - t) ** 2 * hx + 2 * (1 - t) * t * cx + t * t * tx
        bym = (1 - t) ** 2 * hy + 2 * (1 - t) * t * cy + t * t * ty
        # Width tapers linearly from head_width → tail_width.
        w = head_width + (tail_width - head_width) * t
        r = max(0.5, w / 2.0)
        px, py = math_to_pil(bxm, bym)
        # Filled disc.
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        # Also draw a fat line between adjacent samples to avoid gaps
        # when the taper is aggressive.
        if prev is not None:
            ppx, ppy = prev
            draw.line([ppx, ppy, px, py], fill=(0, 0, 0), width=max(1, int(round(w))))
        prev = (px, py)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ti(
        d,
        head_anchor=('BL', 0.30, 0.75),   # thick 起笔, lower-left
        tail_anchor=('TR', 0.75, 0.30),   # 出锋 needle-tip, upper-right
        head_width=13,
        tail_width=1,
        curve=0.09,
        segments=48,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_提.png")
    img.save(out)
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"wrote {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
