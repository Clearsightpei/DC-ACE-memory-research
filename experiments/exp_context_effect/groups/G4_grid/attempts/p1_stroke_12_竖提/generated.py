"""p1_stroke_12_竖提 — Drawer attempt (G4 grid-bank).

竖提 (shù tí): a compound stroke.
  Part 1 — 竖 (vertical): starts at top-center area, descends straight
    down. Head has a small 顿笔 press (thick), body a steady width.
  Part 2 — 提 (rising flick): at the bottom of the vertical, the brush
    turns and flicks up-and-to-the-right, tapering to a needle tip.

The join between 竖 and 提 is a **welded bend** (P/T-like) at the
bottom of the vertical — no gap, the vertical's tail is the flick's
head.

米字格 anchors:
  竖.head @ ('TC', 0.30, 0.20)  — top-of-center, slightly left of exact center
  竖.tail @ ('BC', 0.30, 0.75)  — bottom-of-center, same x (straight down)
  提.head @ ('BC', 0.30, 0.75)  — welded to 竖.tail
  提.tail @ ('MR', 0.60, 0.40)  — up-and-to-the-right needle tip

Joint spec:
  stroke1.tail @ BC  ⇆  stroke2.head @ BC   (P — welded bend, shared point)

Canvas: 300×300, white background, black ink.

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
    """(cell, x_frac, y_frac) → (mx, my) math-coords.
    y_frac = 0 → cell top edge; y_frac = 1 → cell bottom edge."""
    cell, xf, yf = anchor
    x_left, x_right, y_top, y_bot = CELLS[cell]
    mx = x_left + xf * (x_right - x_left)
    my = y_top + yf * (y_bot - y_top)
    return float(mx), float(my)


def math_to_pil(mx, my):
    """Math-coords (origin center, y up) → PIL pixel (origin TL, y down)."""
    return mx + 150.0, 150.0 - my


# ── Tapered variable-width polyline via quadratic Bézier + discs ──
def _stroke_bezier(draw, p_head, p_ctrl, p_tail,
                   head_width, tail_width, segments=48):
    """Rasterize a quadratic Bézier from head→tail in math-coords, with
    width linearly tapering head→tail. Filled discs at every sample plus
    a fat line between adjacent samples avoid gaps under aggressive taper."""
    hx, hy = p_head
    cx, cy = p_ctrl
    tx, ty = p_tail
    prev = None
    for i in range(segments + 1):
        t = i / segments
        bxm = (1 - t) ** 2 * hx + 2 * (1 - t) * t * cx + t * t * tx
        bym = (1 - t) ** 2 * hy + 2 * (1 - t) * t * cy + t * t * ty
        w = head_width + (tail_width - head_width) * t
        r = max(0.5, w / 2.0)
        px, py = math_to_pil(bxm, bym)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        if prev is not None:
            ppx, ppy = prev
            draw.line([ppx, ppy, px, py], fill=(0, 0, 0),
                      width=max(1, int(round(w))))
        prev = (px, py)


def draw_shu_ti(draw,
                shu_head_anchor, shu_tail_anchor,
                ti_tail_anchor,
                shu_head_width=13, shu_tail_width=11,
                ti_head_width=13, ti_tail_width=1,
                shu_segments=40, ti_segments=40):
    """竖提 = 竖 (nearly straight vertical, mild taper) + 提 (rising flick).

    The 竖 body is drawn as a Bézier with control point at the chord
    midpoint (effectively a straight line, but the routine keeps the
    same taper machinery as other strokes).

    The 提 flick starts at 竖's tail (welded bend) and curves up-and-right
    with a mild upward bow, ending in a needle tip.
    """
    # 竖 body — head is the top-center 起笔, tail is the bottom-center
    # corner where the flick will spring from. Mild taper (13→11) so
    # the 顿笔 head reads as slightly heavier than the base.
    hx, hy = anchor_to_math(shu_head_anchor)
    tx, ty = anchor_to_math(shu_tail_anchor)
    # Straight vertical — control at chord midpoint.
    cx = (hx + tx) / 2.0
    cy = (hy + ty) / 2.0
    _stroke_bezier(draw, (hx, hy), (cx, cy), (tx, ty),
                   shu_head_width, shu_tail_width, segments=shu_segments)

    # A small 顿笔 press at the bottom of 竖 — a slightly larger disc
    # at the bend point to sell the "brush pressed and turned" feel.
    bpx, bpy = math_to_pil(tx, ty)
    br = shu_tail_width / 2.0 + 1.5
    draw.ellipse([bpx - br, bpy - br, bpx + br, bpy + br], fill=(0, 0, 0))

    # 提 flick — from the welded bend at (tx,ty) rising to ti_tail_anchor.
    # Head is thick (same as 竖 tail region), tail tapers to a needle tip.
    fhx, fhy = tx, ty
    ftx, fty = anchor_to_math(ti_tail_anchor)

    # Bow the arc slightly upward-left (concave-down feel of a rising flick).
    fmx = (fhx + ftx) / 2.0
    fmy = (fhy + fty) / 2.0
    dx = ftx - fhx
    dy = fty - fhy
    length = (dx * dx + dy * dy) ** 0.5
    perp_x = -dy / length
    perp_y = dx / length
    if perp_y < 0:  # ensure perp points into +y (upward bow)
        perp_x, perp_y = -perp_x, -perp_y
    bow = 0.08 * length
    ccx = fmx + perp_x * bow
    ccy = fmy + perp_y * bow
    _stroke_bezier(draw, (fhx, fhy), (ccx, ccy), (ftx, fty),
                   ti_head_width, ti_tail_width, segments=ti_segments)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shu_ti(
        d,
        shu_head_anchor=('TC', 0.30, 0.20),  # 起笔, top-center-ish
        shu_tail_anchor=('BC', 0.30, 0.75),  # bend point, bottom-center-ish
        ti_tail_anchor=('MR', 0.60, 0.40),   # 出锋 needle-tip, up-right
        shu_head_width=13,
        shu_tail_width=11,
        ti_head_width=13,
        ti_tail_width=1,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_竖提.png")
    img.save(out)
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"wrote {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
