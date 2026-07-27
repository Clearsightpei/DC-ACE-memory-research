"""
巛 (chuan radical, 3 strokes) — G3 coord-bank RETRY #1.
"""

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   No per-item fix idea recorded; entry is just "FAIL" under the B1
#   mass fail list. Prior attempt PNG shows near-straight vertical
#   shafts with tiny hook-heads — the strokes did not read as the
#   three curving-left 撇-scoops of the GT. Fix idea (self-derived):
#   each of the 3 strokes must be a proper 撇-like stroke — pronounced
#   leftward bow along the shaft, with a distinct pen-lift-notch at
#   the top and a tapered needle tail. Model after the LEFT scoop of
#   川 (bank chuan.py _draw_left_curve), applied 3 times side by side.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   The relevant family is "撇 as inline scoop with head-bow" — the
#   exact pattern in chuan.py _draw_left_curve (bezier scoop, w_head
#   ~10 tapering to w_tail ~4). 巛 is 3 clones of that primitive
#   spaced ~35 px apart.
# Q3 (helpers): Does the fail category match any of these helpers?
#   Not really — no X-crossing, no mirror-dot, no MMH uniform thin
#   (GT here is calligraphic-taper). What DOES apply: reuse the
#   chuan.py _draw_left_curve inline pattern verbatim as an inline
#   helper here, drawn 3 times with different origins. No import of
#   `kiss_apex`/`pie_point`/`mirror_dian_pair` — none matches. This
#   is a "clone-a-known-scoop 3x" recipe.

from PIL import Image, ImageDraw
import math

W, H = 300, 300


def _draw_scoop(draw, top_x, top_y, bot_x, bot_y, ctrl_dx=-10.0,
                w_head=6.5, w_tail=1.5, notch_dx=8, notch_dy=-4):
    """
    Draw one 撇-like scoop stroke.

    - Head: small pen-lift notch at (top_x + notch_dx, top_y + notch_dy)
      then curls into the shaft head at (top_x, top_y). Drawn as a
      2-segment polyline so the notch actually reads as an angled
      hook, not a straight ramp.
    - Shaft: quadratic bezier from (top_x, top_y) via a control point
      bowed LEFT (ctrl_dx negative) to (bot_x, bot_y).
    - Width: w_head at top tapering to w_tail (needle) at tail.
    """
    # 1) Head notch — 2-segment tapered polyline: notch tip goes UP-RIGHT
    # from a mid-point, then the mid-point ramps DOWN-LEFT into the
    # shaft head. This gives a distinct pen-lift "kink" like the GT.
    kink = (top_x + 2, top_y + 1)
    notch_tip = (top_x + notch_dx, top_y + notch_dy)
    _tapered_line(draw, notch_tip, kink, 1.4, w_head)
    _tapered_line(draw, kink, (top_x, top_y + 3), w_head, w_head)

    # 2) Main shaft — quadratic bezier bowed left.
    x0, y0 = top_x, top_y + 2
    x2, y2 = bot_x, bot_y
    mx = (x0 + x2) / 2.0 + ctrl_dx
    my = (y0 + y2) / 2.0

    N = 60
    prev = None
    for i in range(N + 1):
        u = i / N
        mu = 1 - u
        x = mu * mu * x0 + 2 * mu * u * mx + u * u * x2
        y = mu * mu * y0 + 2 * mu * u * my + u * u * y2
        if prev is not None:
            _tapered_line(draw, prev, (x, y),
                          w_head + (w_tail - w_head) * (i - 1) / N,
                          w_head + (w_tail - w_head) * i / N)
        prev = (x, y)


def _tapered_line(draw, p0, p1, w0, w1):
    """Stamp circles along p0-p1 with linearly interpolated radius."""
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    length = math.hypot(dx, dy)
    if length < 0.1:
        return
    steps = max(2, int(length * 2))
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + dx * u
        y = p0[1] + dy * u
        r = max(0.4, (w0 + (w1 - w0) * u) / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def main():
    img = Image.new("L", (W, H), 255)
    draw = ImageDraw.Draw(img)

    # 3 evenly spaced 撇-scoops. Y range ~ 95..225 (130 px tall).
    # X centers at 105, 150, 195 (~45 px apart).
    # Each scoop bows LEFT (ctrl_dx = -10) and tail lands ~14 px LEFT
    # of top (bot_x = top_x - 14). Head has small right-facing notch.
    scoops = [
        # (top_x, top_y, bot_x, bot_y)
        (115, 100, 100, 225),
        (155, 100, 140, 225),
        (195, 100, 180, 225),
    ]
    for (tx, ty, bx, by) in scoops:
        # Stronger left bow (ctrl_dx=-16) and larger head notch so the
        # top pen-lift reads clearly, matching GT's distinct 撇-heads.
        _draw_scoop(draw, tx, ty, bx, by,
                    ctrl_dx=-16.0, w_head=6.0, w_tail=1.2,
                    notch_dx=10, notch_dy=-6)

    img.save("01_巛.png")


if __name__ == "__main__":
    main()
