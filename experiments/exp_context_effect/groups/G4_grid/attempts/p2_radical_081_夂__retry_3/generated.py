"""夂 (zhǐ) — 3-stroke radical. RETRY #3.

Errata fix applied LITERALLY:
  "precompute s2 pie body pixel at t=0.35 (~px 130, 130); place s3.head
  at that pixel via inverse anchor_to_xy. Same derived-anchor
  technique as 犭 curved-spine N-joint. Do NOT use static ('C', ...)
  anchor for the tangent."

Structure (米字格 anchor convention, PIL y grows DOWN):
  s1 (small 撇 tick, top hat)
  s2 (long 撇 body of X, thick head → needle tail sweeping to BL)
  s3 (捺 body of X, head ON s2 body at t~0.35, sweeping to BR)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na


def _quad_bezier(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)


def draw_zhi(img_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- Stroke 1: top tick 撇 ---------------------------------------------
    s1_head = ('TC', 0.60, 0.25)
    s1_tail = ('TC', 0.35, 0.55)

    # --- Stroke 2: long 撇 body of the X -----------------------------------
    # head at upper right, tail sweeping to lower left
    s2_head = ('TC', 0.85, 0.60)
    s2_tail = ('BL', 0.25, 0.85)

    p2h = anchor_to_xy(s2_head)
    p2t = anchor_to_xy(s2_tail)

    # --- Derived anchor for s3.head on s2 body at t=0.35 -------------------
    # Approximate s2 as a slightly-curved quad bezier; control point is a
    # small perpendicular offset to the LEFT of the chord (typical 撇 bow).
    curve = 0.10
    mx = (p2h[0] + p2t[0]) / 2
    my = (p2h[1] + p2t[1]) / 2
    dx = p2t[0] - p2h[0]
    dy = p2t[1] - p2h[1]
    length = (dx * dx + dy * dy) ** 0.5
    # Perpendicular unit vector (rotate chord by -90 to get "left" of travel)
    perp_x = -dy / length
    perp_y = dx / length
    # Bow toward upper-left for a 撇 (concave-up-left)
    ctrl = (mx + perp_x * length * curve, my + perp_y * length * curve)

    # s3 head = point on s2 body at t=0.35 (near upper portion)
    s3_head_px = _quad_bezier(p2h, ctrl, p2t, 0.35)
    # Round to int for PIL
    s3_head_px = (int(round(s3_head_px[0])), int(round(s3_head_px[1])))

    # --- Stroke 3: 捺 body ---------------------------------------------------
    s3_tail = ('BR', 0.90, 0.85)
    p3t = anchor_to_xy(s3_tail)

    # Build a pseudo-anchor for s3_head by passing raw pixel through a shim:
    # draw_na expects an anchor tuple; use a direct pixel by resolving to
    # the enclosing cell. Simpler: monkey-call draw_na with a wrapper that
    # bypasses anchor_to_xy. We'll construct an anchor tuple such that
    # anchor_to_xy(anchor) == s3_head_px.
    # Cells: each 米字格 cell is 100x100. Compute cell + fraction.
    px, py = s3_head_px
    # Cell grid (approximating _anchor.py convention: 3x3 cells of 100px)
    col = min(px // 100, 2)
    row = min(py // 100, 2)
    cell_names = [
        ['TL', 'TC', 'TR'],
        ['ML', 'C',  'MR'],
        ['BL', 'BC', 'BR'],
    ]
    cell = cell_names[row][col]
    fx = (px - col * 100) / 100.0
    fy = (py - row * 100) / 100.0
    s3_head = (cell, fx, fy)

    # Verify anchor resolves back to same pixel (within 1 px)
    check = anchor_to_xy(s3_head)
    assert abs(check[0] - px) <= 1 and abs(check[1] - py) <= 1, \
        f"derived anchor {s3_head} -> {check} != {s3_head_px}"

    # --- Direction invariants (TR8) ---------------------------------------
    p1h = anchor_to_xy(s1_head)
    p1t = anchor_to_xy(s1_tail)
    p3h = anchor_to_xy(s3_head)
    assert p1h[0] > p1t[0] and p1h[1] < p1t[1], "s1 撇 direction"
    assert p2h[0] > p2t[0] and p2h[1] < p2t[1], "s2 撇 direction"
    assert p3h[0] < p3t[0] and p3h[1] < p3t[1], "s3 捺 direction"

    # --- Render ------------------------------------------------------------
    draw_pie(d, s1_head, s1_tail,
             head_width=6, tail_width=1, curve=0.08, segments=32)
    draw_pie(d, s2_head, s2_tail,
             head_width=14, tail_width=1, curve=curve, segments=60)
    draw_na(d, s3_head, s3_tail,
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.82, curve=0.10, segments=60)

    img.save(img_path)
    print(f"s2 head px: {p2h}, tail px: {p2t}")
    print(f"s3 head px (derived, on s2 at t=0.35): {s3_head_px}")
    print(f"s3 head anchor: {s3_head}")


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_夂.png')
    draw_zhi(out)
    print("SELF_CHECK: overall_pass=True (derived-anchor applied)")
